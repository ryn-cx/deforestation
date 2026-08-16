# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from tests.utils import download_and_save, parsed_json

if TYPE_CHECKING:
    from deforestation import Deforestation
    from deforestation.detail_widgets import DetailWidgets

SEASON_ID = "B005C8DB7E"
# Episodes 25-33 of the season, the page its detail page does not carry.
SECOND_PAGE_NAME = f"{SEASON_ID} episodes 25-33"
FIRST_EPISODE_NUMBER = 25
EPISODES_ON_SECOND_PAGE = 9


# TODO: Validate
@pytest.fixture(scope="session")
def client(client: Deforestation) -> DetailWidgets:
    return client.detail_widgets


# TODO: Validate
def second_page_token(client: DetailWidgets) -> str:
    """Return the token for the season's second page of episodes.

    A token is minted per response rather than being a stable id, so it has to
    be read off a fresh detail page instead of being written down here.
    """
    page = client._client.detail.download_and_parse(SEASON_ID)  # noqa: SLF001
    actions = page.body.btf.state.episode_list.actions
    assert actions
    return next(page.token for page in actions.episode_pages if not page.is_selected)


# TODO: Validate
def test_download(client: DetailWidgets) -> None:
    download_and_save(
        client,
        SECOND_PAGE_NAME,
        lambda: client.download(SEASON_ID, second_page_token(client)),
    )


# TODO: Validate
def test_parse(client: DetailWidgets) -> None:
    data = parsed_json(client, SECOND_PAGE_NAME)
    episodes = data.widgets.episode_list.episodes
    assert len(episodes) == EPISODES_ON_SECOND_PAGE
    # The page picks up where the detail page left off rather than repeating it.
    assert episodes[0].detail.episode_number == FIRST_EPISODE_NUMBER


# TODO: Validate
def test_parse_lists_every_page(client: DetailWidgets) -> None:
    data = parsed_json(client, SECOND_PAGE_NAME)
    pages = data.widgets.episode_list.actions.episode_pages
    # Every page of the season is listed on every page of it, so paging through
    # never has to be a walk from one page to the next.
    assert len(pages) > 1
    assert [page for page in pages if page.is_selected]
