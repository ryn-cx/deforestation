from typing import Any, Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import BaseModel, ConfigDict

class Suggestion(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    text: str | None = None
    marked_up_text: str | None = None
    query: str | None = None
    url: str | None = None

class ParsedSearchSuggestionsModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
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
