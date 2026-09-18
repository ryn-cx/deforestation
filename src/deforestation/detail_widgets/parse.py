# TODO: Validate
"""Read the essentials of a season's episodes out of its episode list."""

from __future__ import annotations

from typing import Any

from deforestation.detail.parse import action_cards, episode, episode_pages
from deforestation.parsing import mapping, number_or_none, sequence, text_or_none


# TODO: Validate
def parse_detail_widgets(widgets: Any) -> dict[str, Any]:  # noqa: ANN401 - Any JSON.
    """Return the essentials of an episode list, as the parsed model reads them."""
    episode_list = mapping(mapping(mapping(widgets).get("widgets")).get("episodeList"))
    return {
        "header": text_or_none(episode_list.get("header")),
        "episode_count": number_or_none(episode_list.get("episodeCount")),
        "episodes": [
            _episode(listed_episode)
            for listed_episode in sequence(episode_list.get("episodes"))
        ],
        "episode_pages": episode_pages(mapping(episode_list.get("actions"))),
    }


# TODO: Validate
def _episode(listed_episode: Any) -> dict[str, Any]:  # noqa: ANN401 - Any JSON value.
    """Return one episode, as a page of the episode list gives it."""
    entry = mapping(listed_episode)
    return episode(
        str(entry.get("titleID")),
        entry.get("detail"),
        mapping(entry.get("self")).get("compactGTI"),
        available=bool(action_cards(entry.get("action"))),
    )
