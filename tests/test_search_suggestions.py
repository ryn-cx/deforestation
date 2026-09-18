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
    assert all(prefix in suggestion.text for suggestion in suggestions.suggestions)
