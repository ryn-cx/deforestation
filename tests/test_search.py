# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from deforestation.exceptions import RedirectedError
from tests.utils import assert_error, download_and_save, parsed_json

if TYPE_CHECKING:
    from deforestation import Deforestation
    from deforestation.search import Search

QUERY = "thundercats"
# A query nothing is named after. There is no such thing as an empty results
# page: what a query does not match is filled in with what it might have meant.
NONSENSE_QUERY = "qzqzqzqzqz"
# A results page that came back with a set of filters on it. Which sections a
# page is built out of is not decided by the query: the same query answered with
# filters once and without them the next time, so this is recorded rather than
# downloaded.
FILTERED_NAME = "filters"
# A blank query is not a search, it is a redirect to the storefront.
BLANK_QUERY = ""
BLANK_QUERY_NAME = "blank query"


# TODO: Validate
@pytest.fixture(scope="session")
def client(client: Deforestation) -> Search:
    return client.search


# TODO: Validate
def test_download(client: Search) -> None:
    download_and_save(client, QUERY, lambda: client.download(QUERY))


# TODO: Validate
def test_download_nonsense(client: Search) -> None:
    download_and_save(
        client,
        NONSENSE_QUERY,
        lambda: client.download(NONSENSE_QUERY),
    )


# TODO: Validate
def test_download_blank(client: Search) -> None:
    assert_error(
        client,
        BLANK_QUERY_NAME,
        lambda: client.download(BLANK_QUERY),
        RedirectedError,
    )


# TODO: Validate
def test_parse(client: Search) -> None:
    data = parsed_json(client, QUERY)
    assert data.body.phrase == QUERY
    assert not data.body.has_failed
    assert data.body.containers


# TODO: Validate
def test_parse_nonsense(client: Search) -> None:
    data = parsed_json(client, NONSENSE_QUERY)
    assert data.body.phrase == NONSENSE_QUERY
    # A query that matches nothing is not an error and is not empty, so the
    # results have to be read as suggestions rather than as matches.
    assert not data.body.has_failed
    assert [container for container in data.body.containers if container.entities]


# TODO: Validate
def test_parse_filtered(client: Search) -> None:
    data = parsed_json(client, FILTERED_NAME)
    # A section a page does not have is left out rather than sent empty, so
    # every one of them has to be treated as optional.
    assert data.body.filters
    assert not parsed_json(client, QUERY).body.filters


# TODO: Validate
def test_every_result_names_the_page_it_is_for(client: Search) -> None:
    data = parsed_json(client, QUERY)
    entities = [
        entity for container in data.body.containers for entity in container.entities
    ]
    assert entities
    # A result links to its detail page rather than naming a title id, and the
    # id in the link is not always the one `itemAnalytics` reports, so the link
    # is what makes a result resolvable to anything.
    assert all(entity.link.url.startswith("/gp/video/") for entity in entities)
