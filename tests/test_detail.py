# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from deforestation.detail.models import DetailModel
from deforestation.exceptions import TitleNotFoundError
from tests.utils import RecordedEndpoint

if TYPE_CHECKING:
    from deforestation import Deforestation

TITLE_IDS = [
    pytest.param("B005C8DB7E", id="thundercats season 1"),
    pytest.param("B005C8DBII", id="thundercats episode, which lands on its season"),
    pytest.param("B0CHF9MZXZ", id="laid-back camp, a season that fits on one page"),
    pytest.param("B00BR6F9ZM", id="teenage mutant ninja turtles, a movie"),
]


# TODO: Validate
class DetailTest(RecordedEndpoint):
    MODEL = DetailModel


# TODO: Validate
@pytest.mark.parametrize("title_id", TITLE_IDS)
def test_download(client: Deforestation, title_id: str) -> None:
    DetailTest.download_test(title_id, lambda: client.detail.download(title_id))


# TODO: Validate
@pytest.mark.parametrize("title_id", TITLE_IDS)
def test_parse(client: Deforestation, title_id: str) -> None:
    detail = client.detail.load(DetailTest.recorded_content(title_id))
    # An episode id lands on its season's page, so the page names the title it
    # settled on rather than the one that was asked for.
    assert detail.body.atf.state.page_title_id


# TODO: Validate
@pytest.mark.parametrize(
    "title_id",
    [pytest.param("B000000000", id="title that does not exist")],
)
def test_download_invalid(client: Deforestation, title_id: str) -> None:
    DetailTest.error_test(
        title_id,
        lambda: client.detail.download(title_id),
        TitleNotFoundError,
    )
