# TODO: Validate
"""Contains the DetailWidgets class."""

from __future__ import annotations

import json
from logging import NullHandler, getLogger
from urllib.parse import quote

from deforestation.base_api_endpoint import BaseEndpoint
from deforestation.detail_widgets.models import DetailWidgetsModel, model_validate_json
from deforestation.exceptions import ResourceNotFoundError, TitleNotFoundError

logger = getLogger(__name__)
logger.addHandler(NullHandler())


# TODO: Validate
class DetailWidgets(BaseEndpoint):
    """Manage the detail widget file.

    A detail page only carries the first 24 episodes of a season, and the rest
    are reached a page at a time through the `EpisodeList` tokens the page
    lists in `episodePages`. A token is minted per response, so it has to be
    read off a fresh detail page rather than stored.

    Source: the episode page buttons on
    https://www.amazon.com/gp/video/detail/{title_id}

    Example request:
        - GET /gp/video/api/getDetailWidgets?
            - titleID={title_id}&
            - widgets=[{"widgetType":"EpisodeList","widgetToken":"{token}"}]
            - HTTP/2
        - Host: www.amazon.com
        - User-Agent: __REDACTED__
        - Accept: application/json
        - Accept-Language: en-US
        - Accept-Encoding: gzip, deflate, br, zstd
        - Referer: https://www.amazon.com/
        - x-requested-with: XMLHttpRequest
        - Sec-Fetch-Dest: empty
        - Sec-Fetch-Mode: cors
        - Sec-Fetch-Site: same-origin
        - Connection: keep-alive
    """

    # TODO: Validate
    def __call__(
        self,
        title_id: str,
        widget_token: str,
        widget_type: str = "EpisodeList",
    ) -> DetailWidgetsModel:
        """Look one widget of a title's page up and return its model."""
        log_id = self.get_log_id(self.__call__, locals())
        return self.load(
            self.download(title_id, widget_token, widget_type),
            log_id,
        )

    # TODO: Validate
    def download(
        self,
        title_id: str,
        widget_token: str,
        widget_type: str = "EpisodeList",
    ) -> str:
        """Download the detail widget file."""
        log_id = self.get_log_id(self.download, locals())
        # The token is escaped inside the JSON and then escaped again as part of
        # it, which is what the site sends.
        widgets = json.dumps(
            [{"widgetType": widget_type, "widgetToken": quote(widget_token, safe="")}],
            separators=(",", ":"),
        )
        try:
            return self._client.download(
                endpoint="api/getDetailWidgets",
                params={"titleID": title_id, "widgets": widgets},
                headers={"x-requested-with": "XMLHttpRequest"},
                log_id=log_id,
            )
        except ResourceNotFoundError as err:
            raise TitleNotFoundError(
                title_id,
                err.status_code,
                err.response,
            ) from err

    # TODO: Validate
    def load(self, data: str, log_id: str = "") -> DetailWidgetsModel:
        """Read a downloaded detail widget file into its model."""
        return model_validate_json(data, log_id or self.default_log_id)
