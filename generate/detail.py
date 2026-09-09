# TODO: Validate
"""Rebuilds DetailModel."""

from __future__ import annotations

import json
import logging
import re
from typing import TYPE_CHECKING, cast

from degenson import SchemaBuilder  # type: ignore[import-untyped]
from get_around import build_client_automatically
from good_ass_pydantic_integrator.gapi import GAPI
from good_ass_pydantic_integrator.generate import (
    drop_names_missing_from_optional_models,
    model_directory,
    recorded_responses,
)

from deforestation import Deforestation
from generate.constants import DEFORESTATION_PATH, FILES_PATH
from generate.utils import download_if_missing, drop_redundant_recordings, load_ids

if TYPE_CHECKING:
    from collections.abc import Iterable

    from good_ass_pydantic_integrator.constants import INPUT_TYPE, JSON_VALUE

TITLE_IDS = load_ids("DetailModel")
"""A season, an episode, a movie and a season that fits on one page."""

TITLE_ID_KEY = re.compile(r"^(?:[A-Z0-9]{10}|amzn1\.dv\.gti\.[0-9a-z-]+)$")

logger = logging.getLogger(__name__)


# TODO: Validate
def merged_schema(schemas: Iterable[JSON_VALUE]) -> dict[str, JSON_VALUE]:
    builder = SchemaBuilder()
    for schema in schemas:
        builder.add_schema(schema)
    return builder.to_schema()


# TODO: Validate
def keyed_by_title_id(schema: JSON_VALUE) -> JSON_VALUE:
    if isinstance(schema, list):
        return [keyed_by_title_id(item) for item in schema]
    if not isinstance(schema, dict):
        return schema

    walked: dict[str, JSON_VALUE] = {
        key: keyed_by_title_id(value) for key, value in schema.items()
    }
    properties = walked.get("properties")
    if not isinstance(properties, dict):
        return walked

    title_ids = [key for key in properties if TITLE_ID_KEY.match(key)]
    if not title_ids:
        return walked
    named = [key for key in properties if key not in title_ids]
    if named:
        msg = f"Map keyed by both title ids and field names: {named}"
        raise ValueError(msg)

    return {
        **{
            key: value
            for key, value in walked.items()
            if key not in ("properties", "required")
        },
        "additionalProperties": merged_schema(
            properties[title_id] for title_id in title_ids
        ),
    }


# TODO: Validate
def rebuild_detail_model() -> None:
    recorded = GAPI("DetailModel")
    for response in recorded_responses(FILES_PATH, "DetailModel", json.loads):
        recorded.add_object_from_dict(cast("INPUT_TYPE", response))

    mapped = GAPI("DetailModel")
    mapped.add_schema_from_dict(
        cast(
            "dict[str, INPUT_TYPE]",
            keyed_by_title_id(json.loads(recorded.get_json_schema_content())),
        ),
    )

    directory = model_directory(DEFORESTATION_PATH, "DetailModel")
    logger.info("Writing DetailModel.")
    mapped.write_json_schema_to_file(directory / "models.json")
    mapped.write_strict_models_to_file(directory / "strict_models.py")
    mapped.write_optional_models_to_file(directory / "optional_models.py")
    mapped.write_models_to_file(directory / "models.py")
    drop_names_missing_from_optional_models(directory)
    drop_redundant_recordings(FILES_PATH, "DetailModel")


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
    rebuild_detail_model()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_detail(Deforestation(build_client_automatically()))
