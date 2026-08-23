from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from typing import Any
from pydantic import BaseModel, ConfigDict, Field

class Availability(BaseModel):
    model_config = ConfigDict(extra='ignore')
    description: str | None = None
    severity: str | None = None

class Metadata(BaseModel):
    model_config = ConfigDict(extra='ignore')
    availability: Availability | None = None

class Text(BaseModel):
    model_config = ConfigDict(extra='ignore')
    attrs: dict[str, Any] | None = None
    string: str | None = None

class Suggestion(BaseModel):
    model_config = ConfigDict(extra='ignore')
    href: str | None = None
    ref_marker: str | None = Field(None, alias='refMarker')
    text: Text | None = None

class SearchSuggestionsModel(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field__type: str | None = Field(None, alias='__type')
    metadata: Metadata | None = None
    suggestions: list[Suggestion] | None = None
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
