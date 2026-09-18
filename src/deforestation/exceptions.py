# TODO: Validate
"""Exceptions."""

from __future__ import annotations

from typing import Any


# TODO: Validate
class DeforestationError(Exception):
    """Base exception for Deforestation."""

    response: str | dict[str, Any] | None = None


# TODO: Validate
class HTTPError(DeforestationError):
    """Raised when HTTP request fails with unexpected status code."""

    # TODO: Validate
    def __init__(
        self,
        status_code: int,
        response: str | dict[str, Any] | None,
    ) -> None:
        """Initialize the HTTPError with the status code and response body."""
        self.status_code = status_code
        self.response = response
        super().__init__(f"Unexpected response status code: {status_code}")


# TODO: Validate
class BotCheckError(HTTPError):
    """Raised when the request is answered with a bot check instead of data.

    Amazon serves this as a 503 with an HTML body, which is also what a real
    outage looks like.
    """


# TODO: Validate
class ResourceNotFoundError(HTTPError):
    """Raised when the API reports that the requested resource does not exist."""


# TODO: Validate
class TitleNotFoundError(ResourceNotFoundError):
    """Raised when the requested title does not exist."""

    # TODO: Validate
    def __init__(
        self,
        title_id: str,
        status_code: int,
        response: str | dict[str, Any] | None,
    ) -> None:
        """Initialize with the title id and the originating response."""
        self.title_id = title_id
        super().__init__(status_code, response)


# TODO: Validate
class RedirectedError(DeforestationError):
    """Raised when a page answers with a redirect rather than with its data.

    A redirect means the request does not name the page it was asked for, so
    what it points at is where the page it does name is.
    """

    # TODO: Validate
    def __init__(self, location: str, response: str) -> None:
        """Initialize with the path that was redirected to and the response."""
        self.location = location
        self.response = response
        super().__init__(f"Request was redirected to {location}")


# TODO: Validate
class OutsideRegionError(DeforestationError):
    """Raised when a region is asked for from a country it does not cover.

    A page lists the ways to watch a title that the address asking for it can
    use, so a region asked for from elsewhere answers with its own catalogue
    but with only some of what that catalogue offers.
    """

    # TODO: Validate
    def __init__(self, region: str, warning: str, response: str) -> None:
        """Initialize with the region asked for and what the page warned."""
        self.region = region
        self.warning = warning
        self.response = response
        super().__init__(f"{region} was asked for from another country: {warning}")
