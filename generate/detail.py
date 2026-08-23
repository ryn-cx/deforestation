# TODO: Validate
"""Rebuilds DetailModel."""

from __future__ import annotations

import logging

from get_around import build_client_automatically
from good_ass_pydantic_integrator import generate_model

from deforestation import Deforestation
from generate.constants import DEFORESTATION_PATH, FILES_PATH
from generate.utils import download_if_missing

TITLE_IDS = ["B005C8DB7E", "B005C8DBII", "B00BR6F9ZM", "B0CHF9MZXZ"]
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
    generate_model(FILES_PATH, DEFORESTATION_PATH, "DetailModel")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_detail(Deforestation(build_client_automatically()))
