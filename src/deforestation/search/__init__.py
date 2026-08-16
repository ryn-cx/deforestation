# TODO: Validate
"""Contains the Search class."""

from __future__ import annotations

from logging import NullHandler, getLogger
from typing import Any, override

from deforestation.base_api_endpoint import BaseEndpoint
from deforestation.search.models import SearchModel

logger = getLogger(__name__)
logger.addHandler(NullHandler())


class Search(BaseEndpoint[SearchModel]):
    """Manage the search file.

    Results come back as `containers`, one per row of the results page, and each
    row holds its matches in `entities`. `containerType` says how a row is meant
    to be shown, so a row is not necessarily results: a `LinkWidget` row is a
    set of links rather than titles.

    A match names the page it belongs to in `link.url` and its title id in
    `itemAnalytics.pageTypeId`, which is what `Detail` takes.

    A blank query is not a search, and is answered with a redirect to the
    storefront rather than with an empty result set.

    Source: https://www.amazon.com/gp/video/search?phrase={query}

    Example request:
        - GET /gp/video/search?
            - phrase={query}&
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

    _response_model = SearchModel

    # TODO: Validate
    @override
    def download(self, query: str) -> dict[str, Any]:
        log_id = self.get_log_id(self.download, locals())
        return self._client.download_page(
            path="search",
            params={"phrase": query},
            log_id=log_id,
        )

    # TODO: Validate
    @override
    def download_and_parse(self, query: str) -> SearchModel:
        return self.parse(self.download(query))
