# TODO: Validate
"""Contains the SearchSuggestions class."""

from __future__ import annotations

from logging import NullHandler, getLogger
from typing import Any, override

from deforestation.base_api_endpoint import BaseEndpoint
from deforestation.search_suggestions.models import SearchSuggestionsModel

logger = getLogger(__name__)
logger.addHandler(NullHandler())


class SearchSuggestions(BaseEndpoint[SearchSuggestionsModel]):
    """Manage the search suggestions file.

    What the search box offers while a query is being typed. A suggestion is a
    query rather than a title: `href` is the search it stands for, not a detail
    page, so a suggestion has to be searched for to be resolved to anything.

    This is one of the operations the app calls while a page is already open, so
    it answers with the suggestions alone rather than with a page.

    Source: https://www.amazon.com/gp/video/search (the search box)

    Example request:
        - GET /gp/video/api/searchSuggestions?
            - phrase={prefix}
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

    _response_model = SearchSuggestionsModel

    # TODO: Validate
    @override
    def download(self, prefix: str) -> dict[str, Any]:
        log_id = self.get_log_id(self.download, locals())
        return self._client.download_api(
            operation="searchSuggestions",
            params={"phrase": prefix},
            log_id=log_id,
        )

    # TODO: Validate
    @override
    def download_and_parse(self, prefix: str) -> SearchSuggestionsModel:
        return self.parse(self.download(prefix))
