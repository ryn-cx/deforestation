"""ParsedSearchSuggestionsModel, strict to a type checker, all-optional at runtime.

A type checker reads the strict model, so every field carries the type and
the requiredness the schema recorded. At runtime the all-optional copy is imported
instead, so a response that has drifted still parses and a field the data is
missing is None despite what its type hint says.
"""

from typing import TYPE_CHECKING

from good_ass_pydantic_integrator import load

from .optional_models import ParsedSearchSuggestionsModel as OptionalModel
from .strict_models import ParsedSearchSuggestionsModel as StrictModel

if TYPE_CHECKING:
    from .strict_models import (
        ParsedSearchSuggestionsModel,
        Suggestion,
    )
else:
    from .optional_models import (
        ParsedSearchSuggestionsModel,
        Suggestion,
    )

__all__ = [
    "ParsedSearchSuggestionsModel",
    "Suggestion",
    "model_validate_json",
]


def model_validate_json(data: str | bytes | object, log_id: str) -> ParsedSearchSuggestionsModel:
    """Read a downloaded file into ParsedSearchSuggestionsModel."""
    return load.model_validate_json(StrictModel, OptionalModel, data, log_id)
