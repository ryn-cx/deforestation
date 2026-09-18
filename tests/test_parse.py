# TODO: Validate
from __future__ import annotations

from pathlib import Path

import pytest

from deforestation import Deforestation

FILES_PATH = Path(__file__).parent.parent / "generate" / "_files"
"""The recorded responses, which are parsed without going near the network."""

SERIES_ID = "B005C8DB7E"
"""ThunderCats, a season with more episodes than its detail page carries."""

MOVIE_ID = "B00BR6F9ZM"
"""Teenage Mutant Ninja Turtles, a film."""

CHANNEL_SERIES_ID = "B0CHF9MZXZ"
"""Laid-Back Camp, a season watched with an Amazon Channel."""

SEASON_EPISODE_COUNT = 33
"""How many episodes the recorded season has, across all of its pages."""

FIRST_PAGE_EPISODE_COUNT = 24
"""How many of them the season's own page carries."""

LAST_PAGE_EPISODE_COUNT = 9
"""How many of them the last page of the episode list carries."""

LAST_PAGE_FIRST_EPISODE_NUMBER = 25
"""Which episode that page starts at."""

FIRST_EPISODE_DURATION = 1333
"""How long the first episode runs, in seconds."""


# TODO: Validate
@pytest.fixture(scope="session")
def client() -> Deforestation:
    return Deforestation(region="US")


# TODO: Validate
def recorded(model_name: str, name: str) -> str:
    return (FILES_PATH / model_name / f"{name}.json").read_text(encoding="utf-8")


# TODO: Validate
def test_series(client: Deforestation) -> None:
    page = client.detail.load(recorded("DetailModel", SERIES_ID))

    assert page.page_id == SERIES_ID
    assert page.entity_type == "TV Show"
    assert page.parent_title == "Thundercats"
    assert page.season_number == 1
    assert page.image_url
    assert "Action" in page.genres
    # A series has no page of its own, so its first season stands for it.
    assert page.title_key == SERIES_ID
    assert [season.season_number for season in page.seasons] == [1, 2, 3, 4]


# TODO: Validate
def test_episodes(client: Deforestation) -> None:
    page = client.detail.load(recorded("DetailModel", SERIES_ID))
    first_episode = page.episodes[0]

    # The page carries the first 24 of the 33 episodes, the rest are a page of
    # the episode list away.
    assert page.episode_count == SEASON_EPISODE_COUNT
    assert len(page.episodes) == FIRST_PAGE_EPISODE_COUNT
    assert [page.is_selected for page in page.episode_pages] == [True, False]
    assert first_episode.title == "Exodus"
    assert first_episode.episode_number == 1
    assert first_episode.duration == FIRST_EPISODE_DURATION
    assert str(first_episode.release_date) == "1985-01-22"
    assert first_episode.url.endswith(first_episode.link_id)
    assert first_episode.is_available


# TODO: Validate
def test_movie(client: Deforestation) -> None:
    page = client.detail.load(recorded("DetailModel", MOVIE_ID))

    assert page.entity_type == "Movie"
    assert page.title_key == page.link_id
    assert not page.seasons
    assert not page.episodes
    assert page.purchasable


# TODO: Validate
def test_channels(client: Deforestation) -> None:
    page = client.detail.load(recorded("DetailModel", CHANNEL_SERIES_ID))

    assert [channel.name for channel in page.channels] == ["Crunchyroll"]
    assert not page.included_with_prime
    assert not page.purchasable


# TODO: Validate
def test_episode_list(client: Deforestation) -> None:
    widgets = client.detail_widgets.load(
        recorded("DetailWidgetsModel", f"{SERIES_ID} episodes 25-33"),
    )

    assert widgets.episode_count == SEASON_EPISODE_COUNT
    assert len(widgets.episodes) == LAST_PAGE_EPISODE_COUNT
    assert widgets.episodes[0].episode_number == LAST_PAGE_FIRST_EPISODE_NUMBER


# TODO: Validate
def test_search_suggestions(client: Deforestation) -> None:
    suggestions = client.search_suggestions.load(
        recorded("SearchSuggestionsModel", "thunder"),
    )
    first_suggestion = suggestions.suggestions[0]

    assert "thunder" in first_suggestion.text
    # A suggestion is a search rather than a title, so it links to the search.
    assert first_suggestion.query == first_suggestion.text
    assert "{bold}" in first_suggestion.marked_up_text
