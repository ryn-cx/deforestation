# TODO: Validate
"""Rebuilds DetailModel."""

from __future__ import annotations

import logging

from get_around import build_client_automatically

from deforestation import Deforestation
from generate.constants import DEFORESTATION_PATH, FILES_PATH
from generate.utils import download_if_missing, load_ids, rebuild_model

TITLE_IDS = load_ids("DetailModel")
"""A season, an episode, a movie and a season that fits on one page."""


# TODO: Validate
def generate_detail(client: Deforestation) -> None:
    """Rebuild DetailModel."""
    for title_id in TITLE_IDS:
        download_if_missing(
            FILES_PATH,
            "DetailModel",
            title_id,
            lambda title_id=title_id: client.detail.download(title_id),
        )
    rebuild_model(FILES_PATH, DEFORESTATION_PATH, "DetailModel")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_detail(Deforestation(build_client_automatically()))
