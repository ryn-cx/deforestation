from __future__ import annotations

import json
import logging
from typing import Any

from get_around import build_client_automatically
from good_ass_pydantic_integrator.recordings import (
    RecordingId,
    download_missing,
    load_ids,
)

from deforestation import Deforestation
from deforestation.detail.parse import parse_detail
from deforestation.detail_widgets.parse import (
    detail_with_all_episodes,
    parse_detail_widgets,
)
from generate.constants import GENERATOR_PATHS, REGION
from generate.parsed import rebuild_parsed_model

MODEL_NAME = "DetailModel"
WALK_MODEL_NAME = f"Multipages/{MODEL_NAME}"
PARSED_MODEL_NAME = "ParsedDetailModel"


# TODO: Validate
class DetailId(RecordingId[Deforestation]):
    title_id: str

    # TODO: Validate
    def download(self, client: Deforestation) -> str:
        return client.detail.download(self.title_id)


# TODO: Validate
class DetailWalkId(RecordingId[Deforestation]):
    """A detail page recorded with every page of its episodes."""

    title_id: str

    # TODO: Validate
    def download(self, client: Deforestation) -> str:
        return json.dumps(client.detail.download_all(self.title_id))


TITLE_IDS = load_ids(GENERATOR_PATHS, MODEL_NAME, DetailId)
WALK_TITLE_IDS = load_ids(GENERATOR_PATHS, WALK_MODEL_NAME, DetailWalkId)

logger = logging.getLogger(__name__)


# TODO: Validate
def parse_recording(recording: Any) -> dict[str, Any]:  # noqa: ANN401 - Any JSON.
    """Parse a detail page, or a detail page and its episode pages."""
    if not isinstance(recording, list):
        return parse_detail(recording)
    detail_body, *widget_bodies = recording
    return detail_with_all_episodes(
        parse_detail(json.loads(detail_body)),
        [parse_detail_widgets(json.loads(body)) for body in widget_bodies],
    )


# TODO: Validate
def generate_detail(client: Deforestation) -> None:
    download_missing(GENERATOR_PATHS, MODEL_NAME, TITLE_IDS, client)
    download_missing(GENERATOR_PATHS, WALK_MODEL_NAME, WALK_TITLE_IDS, client)
    rebuild_parsed_model(MODEL_NAME, PARSED_MODEL_NAME, parse_recording)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_detail(Deforestation(build_client_automatically(), region=REGION))
