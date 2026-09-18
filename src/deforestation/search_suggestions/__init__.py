# TODO: Validate
"""Contains the SearchSuggestions class."""

from __future__ import annotations

import json
from logging import NullHandler, getLogger

from deforestation.base_api_endpoint import BaseEndpoint
from deforestation.search_suggestions.models import (
    ParsedSearchSuggestionsModel,
    model_validate_json,
)
from deforestation.search_suggestions.parse import parse_search_suggestions

logger = getLogger(__name__)
logger.addHandler(NullHandler())


# TODO: Validate
class SearchSuggestions(BaseEndpoint):
    """Contains the search suggestions.

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
    def __call__(self, prefix: str) -> ParsedSearchSuggestionsModel:
        """Download the suggestions file and read the essentials out of it."""
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
    def load(self, data: str, log_id: str = "") -> ParsedSearchSuggestionsModel:
        """Read a search suggestions file into the searches it suggests."""
        return model_validate_json(
            parse_search_suggestions(json.loads(data)),
            log_id or self.default_log_id,
        )
