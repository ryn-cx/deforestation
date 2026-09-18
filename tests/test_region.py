# TODO: Validate
from __future__ import annotations

import json

import httpx
import pytest

from deforestation import Deforestation
from deforestation.exceptions import OutsideRegionError

OUTSIDE_WARNING = (
    "Traveling or based outside United States? Video availability outside of "
    "United States varies. Sign in to see videos available to you."
)
"""What a page warns when it is asked for from a country the region excludes."""


# TODO: Validate
def test_region_is_asked_for_through_its_storefront() -> None:
    client = Deforestation(region="UK")

    assert client.domain == "www.amazon.co.uk"
    assert client.storefront_path == "gp/video/"


# TODO: Validate
def test_no_region_is_served_wherever_it_is_asked_from() -> None:
    client = Deforestation()

    assert client.region is None
    assert client.domain == "www.primevideo.com"
    assert client.storefront_path == ""


# TODO: Validate
def test_region_that_cannot_be_asked_for() -> None:
    # Prime Video is its own site rather than part of the store in France, so
    # there is no storefront to ask.
    with pytest.raises(ValueError, match="cannot be asked for"):
        Deforestation(region="FR")


# TODO: Validate
def page_warning(warning: str) -> str:
    """Return a page served with what it warns about where it was asked from."""
    return json.dumps({"body": {"pangaeaBanner": {"banner": {"string": warning}}}})


# TODO: Validate
def serve(client: Deforestation, body: str, monkeypatch: pytest.MonkeyPatch) -> None:
    """Answer every request this client makes with `body`."""
    monkeypatch.setattr(
        client.get_around_client,
        "get",
        lambda *_args, **_kwargs: httpx.Response(200, text=body),
    )


# TODO: Validate
def test_region_asked_for_from_another_country(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    client = Deforestation(region="US")
    serve(client, page_warning(OUTSIDE_WARNING), monkeypatch)

    with pytest.raises(OutsideRegionError, match="asked for from another country"):
        client.detail.download("B005C8DB7E")


# TODO: Validate
def test_region_asked_for_from_the_country_it_covers(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    client = Deforestation(region="US")
    serve(client, page_warning(""), monkeypatch)

    assert client.detail.download("B005C8DB7E")


# TODO: Validate
def test_no_region_is_never_the_wrong_country(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    # Whoever asks is served their own region, so there is nothing to be outside
    # of and the banner is about the title rather than about the request.
    client = Deforestation()
    serve(client, page_warning(OUTSIDE_WARNING), monkeypatch)

    assert client.detail.download("B005C8DB7E")
