from typing import Any, Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import BaseModel, ConfigDict

class Title(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title_id: str | None = None
    link_id: str | None = None
    url: str | None = None
    title: str | None = None
    synopsis: str | None = None
    entity_type: str | None = None
    release_year: str | None = None
    runtime: str | None = None
    image_url: str | None = None
    maturity_rating: str | None = None
    benefit_id: str | None = None

class Container(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | None = None
    container_type: str | None = None
    titles: list[Title] | None = None

class ParsedSearchModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    query: str | None = None
    has_failed: bool | None = None
    containers: list[Container] | None = None
    titles: list[Title] | None = None
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
