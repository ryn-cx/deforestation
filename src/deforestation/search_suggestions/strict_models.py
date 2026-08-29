from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import ConfigDict
from typing import Any
from pydantic import BaseModel, Field

class Availability(BaseModel):
    model_config = ConfigDict(defer_build=True)
    description: str
    severity: str

class Metadata(BaseModel):
    model_config = ConfigDict(defer_build=True)
    availability: Availability

class Text(BaseModel):
    model_config = ConfigDict(defer_build=True)
    attrs: dict[str, Any]
    string: str

class Suggestion(BaseModel):
    model_config = ConfigDict(defer_build=True)
    href: str
    ref_marker: str = Field(..., alias='refMarker')
    text: Text

class SearchSuggestionsModel(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field__type: str = Field(..., alias='__type')
    metadata: Metadata
    suggestions: list[Suggestion]
    _raw_input: Any = PrivateAttr(default=None)

    @model_validator(mode='wrap')
    @classmethod
    def _capture_raw_input(cls, data: Any, handler: ModelWrapValidatorHandler[Self]) -> Self:
        """Validate the model and keep the input it was built from."""
        model = handler(data)
        model._raw_input = data
        return model

    @property
    def raw_input(self) -> Any:
        """The input this model was validated from, as it was handed over."""
        return self._raw_input
