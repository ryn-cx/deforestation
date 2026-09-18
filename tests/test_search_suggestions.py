# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

if TYPE_CHECKING:
    from deforestation import Deforestation

PREFIXES = [pytest.param("thunder", id="the start of a title")]


# TODO: Validate
@pytest.mark.parametrize("prefix", PREFIXES)
def test_download(client: Deforestation, prefix: str) -> None:
    suggestions = client.search_suggestions(prefix)
    # What was typed is wrapped in the markers the site renders it bold with.
    assert all(
        prefix in suggestion.text.string for suggestion in suggestions.suggestions
    )
