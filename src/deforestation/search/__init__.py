# TODO: Validate
"""Contains the Search class."""

from __future__ import annotations

import json
from logging import NullHandler, getLogger

from deforestation.base_api_endpoint import BaseEndpoint
from deforestation.search.models import (
    ParsedSearchModel,
    model_validate_json,
)
from deforestation.search.parse import parse_search

logger = getLogger(__name__)
logger.addHandler(NullHandler())


# TODO: Validate
class Search(BaseEndpoint):
    """Contains the search.

    Results come back as rows, and each row holds its matches. A query that
    matches nothing is filled in with what it might have meant, so the results
    read as suggestions rather than as matches. A blank query is answered with
    a redirect to the storefront, which raises `RedirectedError`.

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

    # TODO: Validate
    def __call__(self, query: str) -> ParsedSearchModel:
        """Download the search file and read the essentials out of it."""
        log_id = self.get_log_id(self.__call__, locals())
        return self.load(self.download(query), log_id)

    # TODO: Validate
    def download(self, query: str) -> str:
        """Download the search file."""
        log_id = self.get_log_id(self.download, locals())
        return self._client.download(
            endpoint="search",
            params={
                "phrase": query,
                "dvWebAppClientVersion": self._client.client_version,
            },
            headers={"x-requested-with": "WebAppSPA"},
            log_id=log_id,
        )

    # TODO: Validate
    def load(self, data: str, log_id: str = "") -> ParsedSearchModel:
        """Read a search file into the titles it matched."""
        return model_validate_json(
            parse_search(json.loads(data)),
            log_id or self.default_log_id,
        )
