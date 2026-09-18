# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from deforestation.exceptions import TitleNotFoundError

if TYPE_CHECKING:
    from deforestation import Deforestation

TITLE_IDS = [
    pytest.param("B005C8DB7E", id="thundercats season 1"),
    pytest.param("B005C8DBII", id="thundercats episode, which lands on its season"),
    pytest.param("B0CHF9MZXZ", id="laid-back camp, a season that fits on one page"),
    pytest.param("B00BR6F9ZM", id="teenage mutant ninja turtles, a movie"),
]

REDIRECTED_TITLE_IDS = [
    pytest.param("0RIBYLUTJXI49TXVN225JG9A28", id="the compact GTI of the season"),
    pytest.param("0NHEKIP933W5TY5NAU29EQW96J", id="the compact GTI of an episode"),
    pytest.param(
        "amzn1.dv.gti.d0a9f77d-b9da-4df5-6e0b-ce4d6980a730",
        id="the GTI a share link carries",
    ),
]
"""Ids of ThunderCats season 1 that its page is not addressed by."""

REDIRECTED_PAGE_ID = "B005C8DB7E"
"""The id the page each of them redirects to is addressed by."""


# TODO: Validate
@pytest.mark.parametrize("title_id", TITLE_IDS)
def test_download(client: Deforestation, title_id: str) -> None:
    # An episode id lands on its season's page, so the page names the title it
    # settled on rather than the one that was asked for.
    assert client.detail(title_id).page_id


# TODO: Validate
@pytest.mark.parametrize("title_id", REDIRECTED_TITLE_IDS)
def test_download_redirected(client: Deforestation, title_id: str) -> None:
    # An id the page is not addressed by is answered with where the page is,
    # which is followed rather than raised.
    assert client.detail(title_id).page_id == REDIRECTED_PAGE_ID


# TODO: Validate
def test_download_invalid(client: Deforestation) -> None:
    with pytest.raises(TitleNotFoundError):
        client.detail.download("B000000000")
