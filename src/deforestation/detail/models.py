# ruff: noqa: D100
from typing import TYPE_CHECKING

from good_ass_pydantic_integrator import load

from .optional_models import ParsedDetailModel as OptionalModel
from .strict_models import ParsedDetailModel as StrictModel

if TYPE_CHECKING:
    from .strict_models import (
        Channel,
        Container,
        Episode,
        EpisodePage,
        Images,
        Images1,
        Images2,
        ParsedDetailModel,
        Season,
        Title,
    )
else:
    from .optional_models import (
        Channel,
        Container,
        Episode,
        EpisodePage,
        Images,
        Images1,
        Images2,
        ParsedDetailModel,
        Season,
        Title,
    )

__all__ = [
    "Channel",
    "Container",
    "Episode",
    "EpisodePage",
    "Images",
    "Images1",
    "Images2",
    "ParsedDetailModel",
    "Season",
    "Title",
    "model_validate_json",
]


def model_validate_json(data: str | bytes | object, log_id: str) -> ParsedDetailModel:
    """Read a downloaded file into ParsedDetailModel."""
    return load.model_validate_json(StrictModel, OptionalModel, data, log_id)
