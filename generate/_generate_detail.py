from __future__ import annotations

import logging

from get_around import build_client_automatically
from good_ass_pydantic_integrator.recordings import (
    RecordingId,
    download_missing,
    load_ids,
)

from deforestation import Deforestation
from deforestation.detail.parse import parse_detail
from generate.constants import GENERATOR_PATHS, REGION
from generate.parsed import rebuild_parsed_model

MODEL_NAME = "DetailModel"
PARSED_MODEL_NAME = "ParsedDetailModel"


# TODO: Validate
class DetailId(RecordingId[Deforestation]):
    title_id: str

    # TODO: Validate
    def download(self, client: Deforestation) -> str:
        return client.detail.download(self.title_id)


TITLE_IDS = load_ids(GENERATOR_PATHS, MODEL_NAME, DetailId)

logger = logging.getLogger(__name__)


# TODO: Validate
def generate_detail(client: Deforestation) -> None:
    download_missing(GENERATOR_PATHS, MODEL_NAME, TITLE_IDS, client)
    rebuild_parsed_model(MODEL_NAME, PARSED_MODEL_NAME, parse_detail)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_detail(Deforestation(build_client_automatically(), region=REGION))
