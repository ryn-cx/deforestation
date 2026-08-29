# TODO: Validate
"""Rebuilds SearchSuggestionsModel."""

from __future__ import annotations

import logging

from get_around import build_client_automatically

from deforestation import Deforestation
from generate.constants import DEFORESTATION_PATH, FILES_PATH
from generate.utils import download_if_missing, load_ids, rebuild_model

PREFIXES = load_ids("SearchSuggestionsModel")


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
    rebuild_model(FILES_PATH, DEFORESTATION_PATH, "SearchSuggestionsModel")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_search_suggestions(Deforestation(build_client_automatically()))
