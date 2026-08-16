# TODO: Validate
"""Contains the Detail class."""

from __future__ import annotations

import re
from logging import NullHandler, getLogger
from typing import TYPE_CHECKING, Any, override

from deforestation.base_api_endpoint import BaseEndpoint
from deforestation.detail.models import DetailModel
from deforestation.exceptions import ResourceNotFoundError, TitleNotFoundError

if TYPE_CHECKING:
    from good_ass_pydantic_integrator.constants import INPUT_TYPE, JSON_VALUE

logger = getLogger(__name__)
logger.addHandler(NullHandler())

TITLE_ID = re.compile(
    r"^(B[0-9A-Z]{9}|0[A-Z0-9]{25}|amzn1\.dv\.gti\.[0-9a-f-]+)$",
)
"""A title id: an ASIN, a GTI, or the compact form of a GTI.

All three name the same title and all three are used as keys, sometimes side by
side in the same map, so a map counts as title keyed whichever of them it uses.
"""

TITLE_ID_KEY = "titleId"
"""Field the key of a title keyed map is moved into."""


class Detail(BaseEndpoint[DetailModel]):
    """Manage the detail file.

    A movie, a series, a season and an episode are all a detail page, and
    `body.btf.state.metadata` tells them apart. A season carries its episodes in
    `body.btf.state.detail.detail`, keyed by the episode's title id, and lists
    them in order in `body.btf.state.episodeList.cardTitleIds`.

    A series is not a page of its own here. Asking for one answers with the
    detail page of a season, and every season of it is listed in
    `body.atf.state.seasons`, each with the title id its own page is under.

    A title id is either an ASIN (`B005C8DB7E`) or the compact form of a GTI
    (`0RIBYLUTJXI49TXVN225JG9A28`). Both name the same title, and both are
    accepted, but only the ASIN is what the site links to.

    The page is split into `atf` and `btf`, above and below the fold, which is
    a rendering order rather than a division of the data: the same keys appear
    in both, and which half a key is filled in on is decided per key.

    Source: https://www.amazon.com/gp/video/detail/{title_id}

    Example request:
        - GET /gp/video/detail/{title_id}?
            - dvWebAppClientVersion=1.0.127846.0
            - HTTP/2
        - Host: www.amazon.com
        - User-Agent: __REDACTED__
        - Accept: application/json
        - Accept-Language: en-US
        - Accept-Encoding: gzip, deflate, br, zstd
        - Referer: https://www.amazon.com/
        - x-requested-with: WebAppSPA
        - Sec-Fetch-Dest: empty
        - Sec-Fetch-Mode: cors
        - Sec-Fetch-Site: same-origin
        - Connection: keep-alive
    """

    _response_model = DetailModel

    # TODO: Validate
    @override
    @classmethod
    def transform_input(cls, data: INPUT_TYPE) -> INPUT_TYPE:  # type: ignore[misc]
        """Turn the title keyed maps into lists before a model is built from them.

        The page keys most of what it holds by the title id it belongs to, so
        modelling it as it is would generate one class per title and a different
        set of classes for every page. The key is moved into the value as
        `titleId` rather than dropped, because nothing in the value records the
        title it is for. The saved file is still the raw response.
        """
        return cls._recursively_transform_input(data)  # ty: ignore[invalid-return-type]

    # TODO: Validate
    @classmethod
    def _recursively_transform_input(cls, value: JSON_VALUE) -> JSON_VALUE:
        """Rewrite every title keyed map inside `value` into a list.

        A map counts as title keyed when it is not empty and every one of its
        keys is a title id, which no map of fields ever is. A value that is not
        an object has nowhere to hold the key, so it is wrapped in one.
        """
        if isinstance(value, list):
            return [cls._recursively_transform_input(item) for item in value]
        if not isinstance(value, dict):
            return value

        unkeyed = {
            key: cls._recursively_transform_input(item) for key, item in value.items()
        }
        if not unkeyed or not all(TITLE_ID.match(key) for key in unkeyed):
            return unkeyed
        return [
            {TITLE_ID_KEY: key, **item}
            if isinstance(item, dict)
            else {TITLE_ID_KEY: key, "value": item}
            for key, item in unkeyed.items()
        ]

    # TODO: Validate
    @override
    def download(self, title_id: str) -> dict[str, Any]:
        log_id = self.get_log_id(self.download, locals())
        try:
            return self._client.download_page(
                path=f"detail/{title_id}",
                params={},
                log_id=log_id,
            )
        except ResourceNotFoundError as err:
            raise TitleNotFoundError(
                title_id,
                err.status_code,
                err.response,
            ) from err

    # TODO: Validate
    @override
    def download_and_parse(self, title_id: str) -> DetailModel:
        return self.parse(self.download(title_id))

    # TODO: Validate
    def download_episode_title_ids(self, title_id: str) -> list[str]:
        """Downloads the title id of every episode of a season, in order.

        A season's page only carries the first page of its episodes, so reading
        `episodeList.cardTitleIds` alone silently stops at 24. The page does
        list every page of episodes from the start though, so the rest are
        fetched one page at a time through the tokens it hands out.

        A title with nothing to page through, which is every movie and every
        episode, comes back with the episodes its page already had, which for
        those two is none.
        """
        page = self.download_and_parse(title_id)
        episode_list = page.body.btf.state.episode_list
        on_page = list(episode_list.card_title_ids or [])

        actions = episode_list.actions
        episode_pages = actions.episode_pages if actions else None
        if not episode_pages:
            return on_page

        title_ids: list[str] = []
        for episode_page in episode_pages:
            # The page that was downloaded is one of the pages listed, and it is
            # already here, so only the others are worth a request.
            if episode_page.is_selected:
                title_ids.extend(on_page)
                continue
            widgets = self._client.detail_widgets.download_and_parse(
                title_id,
                episode_page.token,
            )
            title_ids.extend(
                episode.title_id for episode in widgets.widgets.episode_list.episodes
            )
        return title_ids
