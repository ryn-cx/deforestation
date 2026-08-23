# TODO: Validate
"""Contains the Deforestation class."""

from __future__ import annotations

import json
import time
from http import HTTPStatus
from logging import NullHandler, getLogger
from typing import Any

from get_around import GetAround

from deforestation.detail import Detail
from deforestation.detail_widgets import DetailWidgets
from deforestation.exceptions import (
    BotCheckError,
    HTTPError,
    RedirectedError,
    ResourceNotFoundError,
)
from deforestation.search import Search
from deforestation.search_suggestions import SearchSuggestions

logger = getLogger(__name__)
logger.addHandler(NullHandler())

API_DOMAIN = "www.amazon.com"


# TODO: Validate
class Deforestation:
    """Prime Video API wrapper.

    The store's video section is a single page app, so asking for a page the
    way the app does answers with the JSON the page is rendered from. Nothing
    here is authenticated; an account only changes what a title says about
    itself, never whether the title comes back.
    """

    # TODO: Validate
    def __init__(
        self,
        get_around_client: GetAround | None = None,
        locale: str = "en-US",
        client_version: str = "1.0.127846.0",
    ) -> None:
        """Initializes the Deforestation client.

        The client holds one attribute per endpoint, so `client.detail(id)`
        looks a title up and `client.detail.download(id)` and
        `client.detail.load(data)` are the halves of it.

        Args:
            get_around_client: The HTTP client requests are sent through.
            locale: Language the response is written in.
            client_version: Version the web player sends as
                `dvWebAppClientVersion`, which is what makes a page answer with
                its data instead of its HTML. Any value has been accepted so
                far, but the real one is sent to stay unremarkable.
        """
        self.locale = locale
        self.client_version = client_version
        self.get_around_client = get_around_client or GetAround()

        self.detail = Detail(self)
        self.detail_widgets = DetailWidgets(self)
        self.search = Search(self)
        self.search_suggestions = SearchSuggestions(self)

    # TODO: Validate
    def _default_headers(self) -> dict[str, str]:
        """Return the headers every request is sent with."""
        return {
            # A response is built for whatever browser asks for it, so a user
            # agent that is not a browser gets a page that is not worth parsing.
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                "(KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36"
            ),
            "Accept": "application/json",
            "Accept-Language": self.locale,
            "Referer": f"https://{API_DOMAIN}/",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
        }

    # TODO: Validate
    def download(
        self,
        endpoint: str,
        params: dict[str, Any],
        headers: dict[str, str],
        log_id: str,
    ) -> str:
        """Downloads from the API and returns the body as it was served."""
        logger.debug("Downloading: %s", log_id)
        url = f"https://{API_DOMAIN}/gp/video/{endpoint}"
        start = time.monotonic()
        response = self.get_around_client.get(
            url,
            params=params,
            headers={**self._default_headers(), **headers},
        )

        if response.status_code == HTTPStatus.NOT_FOUND:
            raise ResourceNotFoundError(response.status_code, response.text)
        if response.status_code == HTTPStatus.SERVICE_UNAVAILABLE:
            # A bot check is served as an unavailable page with an HTML body,
            # which is also what a real outage looks like.
            raise BotCheckError(response.status_code, response.text)
        if response.status_code != HTTPStatus.OK:
            raise HTTPError(response.status_code, response.text)

        logger.debug("Downloaded %s (%.4f s)", log_id, time.monotonic() - start)
        return self._validate_download(response.text)

    # TODO: Validate
    @staticmethod
    def _validate_download(response: str) -> str:
        """Raise when the page answered with a redirect instead of its data."""
        try:
            parsed = json.loads(response)
        except ValueError:
            return response
        redirect = parsed.get("redirect") if isinstance(parsed, dict) else None
        if redirect:
            raise RedirectedError(redirect, response)
        return response
