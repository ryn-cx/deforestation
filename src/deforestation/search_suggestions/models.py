from typing import Any
from good_ass_pydantic_integrator import GAPIBaseModel
from pydantic import ConfigDict, Field

class Availability(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    description: str
    severity: str

class Metadata(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    availability: Availability

class Text(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    attrs: dict[str, Any]
    string: str

class Suggestion(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    href: str
    ref_marker: str = Field(..., alias='refMarker')
    text: Text

class SearchSuggestionsModel(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    field__type: str = Field(..., alias='__type')
    metadata: Metadata
    suggestions: list[Suggestion]
