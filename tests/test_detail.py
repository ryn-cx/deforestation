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


# TODO: Validate
@pytest.mark.parametrize("title_id", TITLE_IDS)
def test_download(client: Deforestation, title_id: str) -> None:
    # An episode id lands on its season's page, so the page names the title it
    # settled on rather than the one that was asked for.
    assert client.detail(title_id).body.atf.state.page_title_id


# TODO: Validate
def test_download_invalid(client: Deforestation) -> None:
    with pytest.raises(TitleNotFoundError):
        client.detail.download("B000000000")
