# TODO: Validate
"""Read the essentials of the search suggestions out of their response."""

from __future__ import annotations

import re
from typing import Any
from urllib.parse import parse_qs, urlsplit

from deforestation.parsing import amazon_url, mapping, sequence, text_or_none

BOLD_MARKERS = re.compile(r"\{bold\}|\{end\}")
"""The markers the typed-in part of a suggestion is rendered bold with."""


# TODO: Validate
def parse_search_suggestions(response: Any) -> dict[str, Any]:  # noqa: ANN401
    """Return the essentials of the suggestions, as the parsed model reads them."""
    return {
        "suggestions": [
            _suggestion(suggestion)
            for suggestion in sequence(mapping(response).get("suggestions"))
        ],
    }


# TODO: Validate
def _suggestion(listed_suggestion: Any) -> dict[str, Any]:  # noqa: ANN401 - Any JSON.
    """Return one suggestion, which is a search rather than a title."""
    suggestion = mapping(listed_suggestion)
    marked_up_text = text_or_none(mapping(suggestion.get("text")).get("string"))
    href = text_or_none(suggestion.get("href"))
    return {
        "text": BOLD_MARKERS.sub("", marked_up_text) if marked_up_text else None,
        "marked_up_text": marked_up_text,
        "query": _query(href),
        "url": amazon_url(href) if href else None,
    }


# TODO: Validate
def _query(href: str | None) -> str | None:
    """Return the search a suggestion stands for, read off the link it points at."""
    if not href:
        return None
    phrases = parse_qs(urlsplit(href).query).get("phrase")
    return phrases[0] if phrases else None
