# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from deforestation.exceptions import RedirectedError
from deforestation.search.models import SearchModel
from tests.utils import RecordedEndpoint

if TYPE_CHECKING:
    from deforestation import Deforestation

QUERIES = [
    pytest.param("thundercats", id="a query with matches"),
    pytest.param("qzqzqzqzqz", id="a query with no matches"),
]


# TODO: Validate
class SearchTest(RecordedEndpoint):
    MODEL = SearchModel


# TODO: Validate
@pytest.mark.parametrize("query", QUERIES)
def test_download(client: Deforestation, query: str) -> None:
    SearchTest.download_test(query, lambda: client.search.download(query))


# TODO: Validate
@pytest.mark.parametrize("query", QUERIES)
def test_parse(client: Deforestation, query: str) -> None:
    search = client.search.load(SearchTest.recorded_content(query))
    assert search.body.phrase == query


# TODO: Validate
@pytest.mark.parametrize("query", [pytest.param("", id="blank query")])
def test_download_invalid(client: Deforestation, query: str) -> None:
    # A blank query is not a search, it is a redirect to the storefront.
    SearchTest.error_test(
        query,
        lambda: client.search.download(query),
        RedirectedError,
    )
