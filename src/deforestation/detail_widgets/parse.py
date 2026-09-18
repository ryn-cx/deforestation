# TODO: Validate
"""Read the essentials of a season's episodes out of its episode list."""

from __future__ import annotations

from typing import Any

from deforestation.parsing import (
    action_cards,
    episode,
    episode_pages,
    mapping,
    number_or_none,
    sequence,
    text_or_none,
)


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


# TODO: Validate
def detail_with_all_episodes(
    detail: dict[str, Any],
    widget_pages: list[dict[str, Any]],
) -> dict[str, Any]:
    pages = detail["episode_pages"]
    if not pages:
        return detail

    episodes: list[dict[str, Any]] = []
    downloaded_index = 0
    for page in pages:
        if page["is_selected"]:
            episodes += detail["episodes"]
        else:
            episodes += widget_pages[downloaded_index]["episodes"]
            downloaded_index += 1
    return {**detail, "episodes": episodes}
