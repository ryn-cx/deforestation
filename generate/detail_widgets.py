# TODO: Validate
"""Rebuilds DetailWidgetsModel."""

from __future__ import annotations

import logging

from get_around import build_client_automatically
from good_ass_pydantic_integrator import generate_model

from deforestation import Deforestation
from generate.constants import DEFORESTATION_PATH, FILES_PATH
from generate.utils import download_if_missing

SEASON_ID = "B005C8DB7E"
"""The season whose second page of episodes is recorded."""


# TODO: Validate
def unrecorded_page_token(client: Deforestation) -> str:
    """Return the token for the season's second page of episodes.

    A token is minted per response, so it is read off a fresh detail page rather
    than written down here.
    """
    episode_list = client.detail(SEASON_ID).body.btf.state.episode_list
    episode_pages = episode_list.actions.episode_pages
    return next(page.token for page in episode_pages if not page.is_selected)


# TODO: Validate
def generate_detail_widgets(client: Deforestation) -> None:
    """Rebuild DetailWidgetsModel."""
    download_if_missing(
        FILES_PATH,
        "DetailWidgetsModel",
        f"{SEASON_ID} episodes 25-33",
        lambda: client.detail_widgets.download(
            SEASON_ID,
            unrecorded_page_token(client),
        ),
    )
    generate_model(FILES_PATH, DEFORESTATION_PATH, "DetailWidgetsModel")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_detail_widgets(Deforestation(build_client_automatically()))
