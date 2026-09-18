from __future__ import annotations

import logging

from get_around import build_client_automatically
from good_ass_pydantic_integrator.recordings import (
    RecordingId,
    download_named_missing,
    load_named_ids,
    rebuild_model,
)

from deforestation import Deforestation
from generate.constants import GENERATOR_PATHS

MODEL_NAME = "DetailWidgetsModel"


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
class DetailWidgetsId(RecordingId[Deforestation]):
    written_as_fields = True

    season_id: str

    # TODO: Validate
    def download(self, client: Deforestation) -> str:
        return client.detail_widgets.download(
            self.season_id,
            unrecorded_page_token(client, self.season_id),
        )


WIDGET_REQUESTS = load_named_ids(GENERATOR_PATHS, MODEL_NAME, DetailWidgetsId)


# TODO: Validate
def generate_detail_widgets(client: Deforestation) -> None:
    download_named_missing(GENERATOR_PATHS, MODEL_NAME, WIDGET_REQUESTS, client)
    rebuild_model(GENERATOR_PATHS, MODEL_NAME, DetailWidgetsId)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_detail_widgets(Deforestation(build_client_automatically()))
