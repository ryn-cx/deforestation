# TODO: Validate
"""Read the essentials of a search out of its results page."""

from __future__ import annotations

from typing import Any

from deforestation.parsing import mapping, sequence, text_or_none, title_row


# TODO: Validate
def parse_search(results: Any) -> dict[str, Any]:  # noqa: ANN401 - Any JSON value.
    """Return the essentials of a search, as the parsed model reads them."""
    body = mapping(mapping(results).get("body"))
    rows = [title_row(container) for container in sequence(body.get("containers"))]
    return {
        "query": text_or_none(body.get("phrase")),
        "has_failed": bool(body.get("hasFailed")),
        "containers": rows,
        # Every match in one list, since a search is read for what it found
        # more often than for which row found it.
        "titles": [card for row in rows for card in row["titles"]],
    }
