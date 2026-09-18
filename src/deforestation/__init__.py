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
    OutsideRegionError,
    RedirectedError,
    ResourceNotFoundError,
)
from deforestation.parsing import mapping, text_or_none
from deforestation.search_suggestions import SearchSuggestions

logger = getLogger(__name__)
logger.addHandler(NullHandler())

AUTOMATIC_DOMAIN = "www.primevideo.com"
"""Serves whichever region the request is made from."""

REGION_DOMAINS = {
    "US": "www.amazon.com",
    "UK": "www.amazon.co.uk",
    "DE": "www.amazon.de",
    "JP": "www.amazon.co.jp",
}
"""The storefront a region is asked for through.

Prime Video is part of the store on these four and is its own site everywhere
else, so nowhere else can be asked for a region other than the one the request
comes from.
"""

STOREFRONT_PATH = "gp/video/"
"""What a storefront serves its video section under."""


# TODO: Validate
def outside_region_warning(page: dict[str, Any]) -> str | None:
    """Return what a page warns about being asked for from another country.

    A page is built for the address asking for it as well as for the region it
    belongs to, and it says so when the two are not the same country.
    """
    body = mapping(page.get("body"))
    banner = mapping(mapping(body.get("pangaeaBanner")).get("banner"))
    return text_or_none(banner.get("string"))


# TODO: Validate
def region_host(region: str | None) -> tuple[str, str]:
    """Return the domain and path a region's pages are served under."""
    if region is None:
        return AUTOMATIC_DOMAIN, ""
    if region not in REGION_DOMAINS:
        msg = f"Region {region!r} cannot be asked for, only {sorted(REGION_DOMAINS)}"
        raise ValueError(msg)
    return REGION_DOMAINS[region], STOREFRONT_PATH


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
        region: str | None = None,
    ) -> None:
        """Initializes the Deforestation client.

        The client holds one attribute per endpoint, so `client.detail(id)`
        looks a title up and `client.detail.download(id)` and
        `client.detail.load(data)` are the halves of it. An endpoint answers
        with the essentials of what it was asked for, read out of the response
        as JSON rather than through a model of the whole of it.

        Args:
            get_around_client: The HTTP client requests are sent through.
            locale: Language the response is written in.
            client_version: Version the web player sends as
                `dvWebAppClientVersion`, which is what makes a page answer with
                its data instead of its HTML. Any value has been accepted so
                far, but the real one is sent to stay unremarkable.
            region: Which region's catalogue is asked for, as one of
                `REGION_DOMAINS`. Left unset the region the request comes from
                is served, so what a title says about itself depends on where
                it was asked from and an id is only found where it is sold.
        """
        self.locale = locale
        self.client_version = client_version
        self.region = region
        self.domain, self.storefront_path = region_host(region)
        self.get_around_client = get_around_client or GetAround()

        self.detail = Detail(self)
        self.detail_widgets = DetailWidgets(self)
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
            "Referer": f"https://{self.domain}/",
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
        url = f"https://{self.domain}/{self.storefront_path}{endpoint}"
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
    def _validate_download(self, response: str) -> str:
        """Raise when the response is not what the request asked for."""
        try:
            parsed = json.loads(response)
        except ValueError:
            return response
        if not isinstance(parsed, dict):
            return response
        if redirect := parsed.get("redirect"):
            raise RedirectedError(redirect, response)
        warning = outside_region_warning(parsed)
        if self.region is not None and warning:
            raise OutsideRegionError(self.region, warning, response)
        return response
