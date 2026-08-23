# TODO: Validate
"""Contains the SearchSuggestions class."""

from __future__ import annotations

from logging import NullHandler, getLogger

from deforestation.base_api_endpoint import BaseEndpoint
from deforestation.search_suggestions.models import (
    SearchSuggestionsModel,
    model_validate_json,
)

logger = getLogger(__name__)
logger.addHandler(NullHandler())


# TODO: Validate
class SearchSuggestions(BaseEndpoint):
    """Manage the search suggestions file.

    A suggestion is a query rather than a title, so what it links to is the
    search it stands for and not a detail page.

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

    # TODO: Validate
    def __call__(self, prefix: str) -> SearchSuggestionsModel:
        """Look the suggestions for what has been typed up and return them."""
        log_id = self.get_log_id(self.__call__, locals())
        return self.load(self.download(prefix), log_id)

    # TODO: Validate
    def download(self, prefix: str) -> str:
        """Download the search suggestions file."""
        log_id = self.get_log_id(self.download, locals())
        return self._client.download(
            endpoint="api/searchSuggestions",
            params={"phrase": prefix},
            headers={"x-requested-with": "XMLHttpRequest"},
            log_id=log_id,
        )

    # TODO: Validate
    def load(self, data: str, log_id: str = "") -> SearchSuggestionsModel:
        """Read a downloaded search suggestions file into its model."""
        return model_validate_json(data, log_id or type(self).__name__)
