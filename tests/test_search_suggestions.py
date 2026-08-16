# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from tests.utils import download_and_save, parsed_json

if TYPE_CHECKING:
    from deforestation import Deforestation
    from deforestation.search_suggestions import SearchSuggestions

PREFIX = "thunder"


# TODO: Validate
@pytest.fixture(scope="session")
def client(client: Deforestation) -> SearchSuggestions:
    return client.search_suggestions


# TODO: Validate
def test_download(client: SearchSuggestions) -> None:
    download_and_save(client, PREFIX, lambda: client.download(PREFIX))


# TODO: Validate
def test_parse(client: SearchSuggestions) -> None:
    data = parsed_json(client, PREFIX)
    assert data.suggestions
    # A suggestion is a query, so what it links to is a search rather than a
    # detail page, and every one of them is for the prefix that was typed.
    assert all(f"prefix={PREFIX}" in suggestion.href for suggestion in data.suggestions)
