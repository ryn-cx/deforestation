# TODO: Validate
"""Rebuilds SearchModel."""

from __future__ import annotations

import logging

from get_around import build_client_automatically
from good_ass_pydantic_integrator import generate_model

from deforestation import Deforestation
from generate.constants import DEFORESTATION_PATH, FILES_PATH
from generate.utils import download_if_missing

QUERIES = ["qzqzqzqzqz", "thundercats"]
"""A query nothing matches and one that matches."""


# TODO: Validate
def generate_search(client: Deforestation) -> None:
    """Rebuild SearchModel."""
    for query in QUERIES:
        download_if_missing(
            FILES_PATH,
            "SearchModel",
            query,
            lambda query=query: client.search.download(query),
        )
    generate_model(FILES_PATH, DEFORESTATION_PATH, "SearchModel")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_search(Deforestation(build_client_automatically()))
