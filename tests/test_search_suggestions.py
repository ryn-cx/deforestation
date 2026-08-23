# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from deforestation.search_suggestions.models import SearchSuggestionsModel
from tests.utils import RecordedEndpoint

if TYPE_CHECKING:
    from deforestation import Deforestation

PREFIXES = [
    pytest.param("thunder", id="the start of a title"),
]


# TODO: Validate
class SearchSuggestionsTest(RecordedEndpoint):
    MODEL = SearchSuggestionsModel


# TODO: Validate
@pytest.mark.parametrize("prefix", PREFIXES)
def test_download(client: Deforestation, prefix: str) -> None:
    SearchSuggestionsTest.download_test(
        prefix,
        lambda: client.search_suggestions.download(prefix),
    )


# TODO: Validate
@pytest.mark.parametrize("prefix", PREFIXES)
def test_parse(client: Deforestation, prefix: str) -> None:
    suggestions = client.search_suggestions.load(
        SearchSuggestionsTest.recorded_content(prefix),
    )
    # What was typed is wrapped in the markers the site renders it bold with.
    assert all(
        prefix in suggestion.text.string for suggestion in suggestions.suggestions
    )
