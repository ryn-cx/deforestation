# TODO: Validate
"""Contains the Deforestation class."""

import time
from http import HTTPStatus
from logging import NullHandler, getLogger
from typing import Any

from get_around import GetAround

from deforestation.constants import CLIENT_VERSION, DEFAULT_HOST, WEB_PATH
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

USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36"
)
"""Browser the web player is pretending to be.

The response is built for whatever browser asks for it, so a user agent that is
not a browser gets a page that is not worth parsing.
"""


class Deforestation:
    """Prime Video API wrapper.

    The website is a single page app: the server renders the first page, and
    every page after it is fetched as JSON by the app itself. Asking for a page
    the way the app does returns that JSON, which is the same state the rendered
    HTML is built from, so nothing has to be scraped out of markup.

    Nothing here is authenticated. An account only changes what a title says
    about itself (owned, in the watchlist, resume position), never whether the
    title comes back.
    """

    def __init__(
        self,
        get_around_client: GetAround | None = None,
        locale: str = "en-US",
        host: str = DEFAULT_HOST,
        client_version: str = CLIENT_VERSION,
    ) -> None:
        """Initializes the Deforestation client.

        Args:
            get_around_client: The HTTP client requests are sent through.
            locale: Language the response is written in.
            host: Marketplace the catalog is read from, see `MARKETPLACES`.
            client_version: Version the web player claims to be.
        """
        self.locale = locale
        self.host = host
        self.client_version = client_version
        self.get_around_client = get_around_client or GetAround()

        self.detail = Detail(self)
        self.detail_widgets = DetailWidgets(self)
        self.search = Search(self)
        self.search_suggestions = SearchSuggestions(self)

    def _headers(self) -> dict[str, str]:
        return {
            # "Host": Set by httpx
            "User-Agent": USER_AGENT,
            "Accept": "application/json",
            "Accept-Language": self.locale,
            # "Accept-Encoding": Set by httpx
            "Referer": f"https://{self.host}/",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
        }

    def _get(
        self,
        url: str,
        params: dict[str, Any],
        headers: dict[str, str],
        log_id: str,
    ) -> dict[str, Any]:
        logger.debug("Downloading: %s", log_id)
        start = time.monotonic()
        response = self.get_around_client.get(
            url,
            params=params,
            headers={**self._headers(), **headers},
        )

        if response.status_code != HTTPStatus.OK:
            if response.status_code == HTTPStatus.NOT_FOUND:
                raise ResourceNotFoundError(response.status_code, response.text)
            # A bot check is served as an unavailable page with an HTML body,
            # which is also what a real outage looks like, so the two are only
            # told apart by how often they happen.
            if response.status_code == HTTPStatus.SERVICE_UNAVAILABLE:
                raise BotCheckError(response.status_code, response.text)
            raise HTTPError(response.status_code, response.text)

        logger.debug("Downloaded %s (%.4f s)", log_id, time.monotonic() - start)
        parsed: dict[str, Any] = response.json()
        # A page that does not exist as asked for answers with the page that
        # does, and the app loads that one instead of rendering anything.
        if "redirect" in parsed:
            raise RedirectedError(parsed["redirect"], parsed)
        return parsed

    # TODO: Validate
    def download_page(
        self,
        path: str,
        params: dict[str, Any],
        log_id: str,
    ) -> dict[str, Any]:
        """Downloads a page as the data it is rendered from.

        `dvWebAppClientVersion` and the `WebAppSPA` header are what the app
        sends when it navigates itself, and together they are what makes the
        page answer with JSON rather than with HTML.
        """
        return self._get(
            url=f"https://{self.host}/{WEB_PATH}/{path}",
            params={**params, "dvWebAppClientVersion": self.client_version},
            headers={"x-requested-with": "WebAppSPA"},
            log_id=log_id,
        )

    # TODO: Validate
    def download_api(
        self,
        operation: str,
        params: dict[str, Any],
        log_id: str,
    ) -> dict[str, Any]:
        """Downloads from an operation the app calls outside of a navigation.

        These are the calls a page makes once it is already open, so they answer
        with one widget's worth of data rather than with a whole page.
        """
        return self._get(
            url=f"https://{self.host}/{WEB_PATH}/api/{operation}",
            params=params,
            headers={"x-requested-with": "XMLHttpRequest"},
            log_id=log_id,
        )
