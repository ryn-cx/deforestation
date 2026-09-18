from __future__ import annotations

import logging

from get_around import build_client_automatically
from good_ass_pydantic_integrator.recordings import (
    RecordingId,
    download_missing,
    load_ids,
)

from deforestation import Deforestation
from deforestation.search_suggestions.parse import parse_search_suggestions
from generate.constants import GENERATOR_PATHS, REGION
from generate.parsed import rebuild_parsed_model

MODEL_NAME = "SearchSuggestionsModel"
PARSED_MODEL_NAME = "ParsedSearchSuggestionsModel"


# TODO: Validate
class SearchSuggestionsId(RecordingId[Deforestation]):
    prefix: str

    # TODO: Validate
    def download(self, client: Deforestation) -> str:
        return client.search_suggestions.download(self.prefix)


PREFIXES = load_ids(GENERATOR_PATHS, MODEL_NAME, SearchSuggestionsId)


# TODO: Validate
def generate_search_suggestions(client: Deforestation) -> None:
    download_missing(GENERATOR_PATHS, MODEL_NAME, PREFIXES, client)
    rebuild_parsed_model(
        MODEL_NAME,
        PARSED_MODEL_NAME,
        parse_search_suggestions,
    )


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_search_suggestions(
        Deforestation(build_client_automatically(), region=REGION),
    )
