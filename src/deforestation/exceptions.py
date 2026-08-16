# TODO: Validate
"""Exceptions."""

from __future__ import annotations

from typing import Any


class DeforestationError(Exception):
    """Base exception for Deforestation."""

    response: str | dict[str, Any] | None = None


class HTTPError(DeforestationError):
    """Raised when HTTP request fails with unexpected status code."""

    def __init__(
        self,
        status_code: int,
        response: str | dict[str, Any] | None,
    ) -> None:
        """Initialize the HTTPError with the status code and response body."""
        self.status_code = status_code
        self.response = response
        super().__init__(f"Unexpected response status code: {status_code}")


class BotCheckError(HTTPError):
    """Raised when the request is answered with a bot check instead of data.

    Amazon serves this as a 503 with an HTML body, so it is told apart from a
    real outage by nothing but how often it shows up.
    """


class ResourceNotFoundError(HTTPError):
    """Raised when the API reports that the requested resource does not exist."""


class TitleNotFoundError(ResourceNotFoundError):
    """Raised when the requested title does not exist."""

    def __init__(
        self,
        title_id: str,
        status_code: int,
        response: str | dict[str, Any] | None,
    ) -> None:
        """Initialize with the title id and the originating response."""
        self.title_id = title_id
        super().__init__(status_code, response)


class RedirectedError(DeforestationError):
    """Raised when a page answers with a redirect rather than with its data.

    The app follows these by loading the target itself, so a redirect is the
    API's way of saying the request does not name a page. An empty search query
    is redirected to the storefront instead of being rejected, for example.
    """

    def __init__(self, location: str, response: dict[str, Any]) -> None:
        """Initialize with the path that was redirected to and the response."""
        self.location = location
        self.response = response
        super().__init__(f"Request was redirected to {location}")
