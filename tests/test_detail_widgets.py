# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from deforestation.detail_widgets.models import DetailWidgetsModel
from tests.utils import RecordedEndpoint

if TYPE_CHECKING:
    from deforestation import Deforestation

SEASON_ID = "B005C8DB7E"

NAMES = [
    pytest.param(
        f"{SEASON_ID} episodes 25-33",
        id="the page of a season its detail page does not carry",
    ),
]


# TODO: Validate
class DetailWidgetsTest(RecordedEndpoint):
    MODEL = DetailWidgetsModel


# TODO: Validate
def unrecorded_page_token(client: Deforestation) -> str:
    """Return the token for the season's second page of episodes.

    A token is minted per response, so it is read off a fresh detail page
    rather than written down here.
    """
    episode_list = client.detail(SEASON_ID).body.btf.state.episode_list
    episode_pages = episode_list.actions.episode_pages
    return next(page.token for page in episode_pages if not page.is_selected)


# TODO: Validate
@pytest.mark.parametrize("name", NAMES)
def test_download(client: Deforestation, name: str) -> None:
    DetailWidgetsTest.download_test(
        name,
        lambda: client.detail_widgets.download(
            SEASON_ID,
            unrecorded_page_token(client),
        ),
    )


# TODO: Validate
@pytest.mark.parametrize("name", NAMES)
def test_parse(client: Deforestation, name: str) -> None:
    widgets = client.detail_widgets.load(DetailWidgetsTest.recorded_content(name))
    episode_list = widgets.widgets.episode_list
    assert len(episode_list.episodes) <= episode_list.episode_count
