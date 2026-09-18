# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from deforestation import Deforestation

SEASON_ID = "B005C8DB7E"
"""A season with more episodes than its detail page carries."""


# TODO: Validate
def unrecorded_page_token(client: Deforestation) -> str:
    """Return the token for the season's second page of episodes.

    A token is minted per response, so it is read off a fresh detail page
    rather than written down here.
    """
    episode_pages = client.detail(SEASON_ID).episode_pages
    return next(page.token for page in episode_pages if not page.is_selected)


# TODO: Validate
def test_download(client: Deforestation) -> None:
    widgets = client.detail_widgets(SEASON_ID, unrecorded_page_token(client))
    assert len(widgets.episodes) <= widgets.episode_count
