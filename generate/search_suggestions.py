# TODO: Validate
"""Rebuilds SearchSuggestionsModel."""

from __future__ import annotations

import logging

from get_around import build_client_automatically
from good_ass_pydantic_integrator import generate_model

from deforestation import Deforestation
from generate.constants import DEFORESTATION_PATH, FILES_PATH
from generate.utils import download_if_missing

PREFIXES = ["thunder"]


# TODO: Validate
def generate_search_suggestions(client: Deforestation) -> None:
    """Rebuild SearchSuggestionsModel."""
    for prefix in PREFIXES:
        download_if_missing(
            FILES_PATH,
            "SearchSuggestionsModel",
            prefix,
            lambda prefix=prefix: client.search_suggestions.download(prefix),
        )
    generate_model(FILES_PATH, DEFORESTATION_PATH, "SearchSuggestionsModel")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_search_suggestions(Deforestation(build_client_automatically()))
