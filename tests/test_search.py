# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from deforestation.exceptions import RedirectedError

if TYPE_CHECKING:
    from deforestation import Deforestation

QUERIES = [
    pytest.param("thundercats", id="a query with matches"),
    pytest.param("qzqzqzqzqz", id="a query with no matches"),
]


# TODO: Validate
@pytest.mark.parametrize("query", QUERIES)
def test_download(client: Deforestation, query: str) -> None:
    assert client.search(query).query == query


# TODO: Validate
def test_download_invalid(client: Deforestation) -> None:
    # A blank query is not a search, it is a redirect to the storefront.
    with pytest.raises(RedirectedError):
        client.search.download("")
