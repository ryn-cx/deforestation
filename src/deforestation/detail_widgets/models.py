# ruff: noqa: D100
from typing import TYPE_CHECKING

from good_ass_pydantic_integrator import load

from .optional_models import ParsedDetailWidgetsModel as OptionalModel
from .strict_models import ParsedDetailWidgetsModel as StrictModel

if TYPE_CHECKING:
    from .strict_models import (
        Episode,
        EpisodePage,
        Images,
        ParsedDetailWidgetsModel,
    )
else:
    from .optional_models import (
        Episode,
        EpisodePage,
        Images,
        ParsedDetailWidgetsModel,
    )

__all__ = [
    "Episode",
    "EpisodePage",
    "Images",
    "ParsedDetailWidgetsModel",
    "model_validate_json",
]


def model_validate_json(data: str | bytes | object, log_id: str) -> ParsedDetailWidgetsModel:
    """Read a downloaded file into ParsedDetailWidgetsModel."""
    return load.model_validate_json(StrictModel, OptionalModel, data, log_id)
