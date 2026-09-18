# TODO: Validate
"""Rebuilds a parsed model from what its endpoint's recordings parse into.

A parsed model is not downloaded: every recorded response is written out as what
the parse function makes of it, and those files are what the model is generated
from.

Every recording is kept. A parsed model reads a small part of a response, so a
recording that says nothing new about that part is still what catches a change
to the rest of the response.
"""

from __future__ import annotations

import json
import logging
from typing import TYPE_CHECKING, Any

from good_ass_pydantic_integrator.generate import generate_model, recording_paths

from generate.constants import GENERATOR_PATHS

if TYPE_CHECKING:
    from collections.abc import Callable
    from pathlib import Path

logger = logging.getLogger(__name__)


# TODO: Validate
def rebuild_parsed_model(
    model_name: str,
    parsed_model_name: str,
    parse: Callable[[Any], dict[str, Any]],
) -> None:
    """Write what a model's recordings parse into, then build the parsed model.

    Args:
        model_name: What the recorded responses are filed under, e.g.
            `DetailModel`.
        parsed_model_name: The model class name, e.g. `ParsedDetailModel`.
        parse: Returns the essentials of one recorded response.
    """

    # TODO: Validate
    def read(content: str) -> Any:  # noqa: ANN401 - Any JSON value.
        return parse(json.loads(content))

    _write_parsed_recordings(model_name, parsed_model_name, read)
    generate_model(
        GENERATOR_PATHS.files_path,
        GENERATOR_PATHS.package_path,
        parsed_model_name,
    )


# TODO: Validate
def _write_parsed_recordings(
    model_name: str,
    parsed_model_name: str,
    read: Callable[[str], Any],
) -> None:
    """Write what every recorded response parses into, and drop the leftovers."""
    parsed_directory = GENERATOR_PATHS.files_path / parsed_model_name
    parsed_directory.mkdir(parents=True, exist_ok=True)
    written: set[Path] = set()

    for recording in recording_paths(GENERATOR_PATHS.files_path, model_name):
        parsed_path = parsed_directory / recording.name
        parsed_path.write_text(
            json.dumps(read(recording.read_text(encoding="utf-8")), indent=2) + "\n",
            encoding="utf-8",
        )
        written.add(parsed_path)

    for parsed_path in sorted(parsed_directory.glob("*.json")):
        if parsed_path not in written:
            logger.info("Dropping %s/%s.", parsed_model_name, parsed_path.name)
            parsed_path.unlink()
