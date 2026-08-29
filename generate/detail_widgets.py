# TODO: Validate
"""Rebuilds DetailWidgetsModel."""

from __future__ import annotations

import logging

from get_around import build_client_automatically

from deforestation import Deforestation
from generate.constants import DEFORESTATION_PATH, FILES_PATH
from generate.utils import download_if_missing, load_ids, rebuild_model

WIDGET_REQUESTS = load_ids("DetailWidgetsModel")
"""What each recording of a detail widget response was downloaded with."""


# TODO: Validate
def unrecorded_page_token(client: Deforestation, season_id: str) -> str:
    """Return the token for the season's second page of episodes.

    A token is minted per response, so it is read off a fresh detail page rather
    than written down here.
    """
    episode_list = client.detail(season_id).body.btf.state.episode_list
    episode_pages = episode_list.actions.episode_pages
    return next(page.token for page in episode_pages if not page.is_selected)


# TODO: Validate
def generate_detail_widgets(client: Deforestation) -> None:
    """Rebuild DetailWidgetsModel."""
    for name, arguments in WIDGET_REQUESTS.items():
        season_id = arguments["season_id"]
        download_if_missing(
            FILES_PATH,
            "DetailWidgetsModel",
            name,
            lambda season_id=season_id: client.detail_widgets.download(
                season_id,
                unrecorded_page_token(client, season_id),
            ),
        )
    rebuild_model(FILES_PATH, DEFORESTATION_PATH, "DetailWidgetsModel")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_detail_widgets(Deforestation(build_client_automatically()))
