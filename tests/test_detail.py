# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING, Any

import pytest

from deforestation.detail import TITLE_ID_KEY
from deforestation.exceptions import RedirectedError, TitleNotFoundError
from tests.utils import assert_error, download_and_save, loaded_json, parsed_json

if TYPE_CHECKING:
    from deforestation import Deforestation
    from deforestation.detail import Detail

SEASON_ID = "B005C8DB7E"
EPISODE_ID = "B005C8DBII"
MOVIE_ID = "B00BR6F9ZM"
# A second season, because which sections a page is built out of is decided per
# title rather than per kind of title, so one of each does not cover the shape.
OTHER_SEASON_ID = "B0CGT7L7HC"
TITLE_IDS = [SEASON_ID, EPISODE_ID, MOVIE_ID, OTHER_SEASON_ID]
# The compact form of the GTI the season's ASIN names.
COMPACT_GTI = "0RIBYLUTJXI49TXVN225JG9A28"
COMPACT_GTI_NAME = "compact gti"
INVALID_TITLE_ID = "B000000000"

THUNDERCATS_SEASONS = {
    "B005C8DB7E": 33,
    "B005C8DDW2": 32,
    "B005HGA9DA": 34,
    "B005HE8AWY": 31,
}
"""Every season of ThunderCats and the number of episodes in it.

Counted off the site rather than off a response, so a season that comes back
short is the scraper losing episodes rather than the numbers being stale. Every
one of them is longer than the 24 a detail page carries, which is what makes
them worth checking.
"""


# TODO: Validate
@pytest.fixture(scope="session")
def client(client: Deforestation) -> Detail:
    return client.detail


# TODO: Validate
@pytest.mark.parametrize("title_id", TITLE_IDS)
def test_download(client: Detail, title_id: str) -> None:
    download_and_save(client, title_id, lambda: client.download(title_id))


# TODO: Validate
def test_download_compact_gti(client: Detail) -> None:
    # Only an ASIN names a page. A compact GTI names the same title, but it is
    # answered with a redirect to the ASIN rather than with the page.
    assert_error(
        client,
        COMPACT_GTI_NAME,
        lambda: client.download(COMPACT_GTI),
        RedirectedError,
    )


# TODO: Validate
def test_download_invalid(client: Detail) -> None:
    assert_error(
        client,
        INVALID_TITLE_ID,
        lambda: client.download(INVALID_TITLE_ID),
        TitleNotFoundError,
    )


# TODO: Validate
def titles(entries: Any) -> dict[str, Any]:  # noqa: ANN401
    """Return a title keyed section of the page back as a map.

    Every section is a list of a different model, and a section that is empty on
    a given page is still a map, so there is no one type to take here.
    """
    return {entry.title_id: entry for entry in entries or []}


# TODO: Validate
@pytest.mark.parametrize("title_id", TITLE_IDS)
def test_parse(client: Detail, title_id: str) -> None:
    data = parsed_json(client, title_id)
    # The page answers under the title it settled on rather than under the one
    # it was asked for, and `self` is that title.
    assert data.body.atf.state.page_title_id in titles(data.body.atf.state.self)


# TODO: Validate
@pytest.mark.parametrize("season_id", [SEASON_ID, OTHER_SEASON_ID])
def test_parse_season(client: Detail, season_id: str) -> None:
    data = parsed_json(client, season_id)
    assert titles(data.body.atf.state.self)[season_id].title_type == "season"
    # Every episode of the season is listed in order, and its own entry in the
    # detail section is what holds the episode.
    card_title_ids = data.body.btf.state.episode_list.card_title_ids
    assert card_title_ids
    episodes = titles(data.body.btf.state.detail.detail)
    assert all(episodes[title_id] for title_id in card_title_ids)


# TODO: Validate
def test_parse_episode(client: Detail) -> None:
    data = parsed_json(client, EPISODE_ID)
    assert titles(data.body.atf.state.self)[EPISODE_ID].title_type == "episode"


# TODO: Validate
def test_parse_movie(client: Detail) -> None:
    data = parsed_json(client, MOVIE_ID)
    page_title_id = data.body.atf.state.page_title_id
    assert titles(data.body.atf.state.self)[page_title_id].title_type == "movie"
    # A movie is a single title, so it has neither episodes nor seasons.
    assert not data.body.btf.state.episode_list.card_title_ids
    assert not data.body.atf.state.seasons


# TODO: Validate
def test_parse_seasons_are_pages_of_their_own(client: Detail) -> None:
    data = parsed_json(client, SEASON_ID)
    seasons = titles(data.body.atf.state.seasons)[SEASON_ID].value
    # The season that was asked for is the one the page is showing, and every
    # other season is reached by the id it is listed under.
    assert [season for season in seasons if season.is_selected]
    assert all(season.season_id for season in seasons)


# TODO: Validate
@pytest.mark.parametrize(("season_id", "episode_count"), THUNDERCATS_SEASONS.items())
def test_episode_pagination(client: Detail, season_id: str, episode_count: int) -> None:
    """Every episode of a season is reached, not just the first page of them.

    A detail page carries 24 episodes and hands out tokens for the rest, so a
    season that comes back with 24 of them means the further pages were never
    downloaded. This hits the network on every run because a token is minted per
    response and cannot be replayed from a recorded file.
    """
    title_ids = client.download_episode_title_ids(season_id)
    assert len(title_ids) == episode_count
    # A page that were to repeat what another page already had would count up to
    # the right total without actually reaching every episode.
    assert len(set(title_ids)) == episode_count


# TODO: Validate
def test_title_keys_are_moved_into_their_values(client: Detail) -> None:
    # The model only holds the values of the title keyed maps, so this is what
    # makes sure the key they were under is not lost by rewriting them.
    raw = loaded_json(client, SEASON_ID)
    transformed: Any = client.transform_input(raw)
    raw_self = raw["body"]["atf"]["state"]["self"]
    transformed_self = transformed["body"]["atf"]["state"]["self"]
    assert [entry[TITLE_ID_KEY] for entry in transformed_self] == list(raw_self)
