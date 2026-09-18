from typing import Any, Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import ConfigDict
from pydantic import BaseModel

class Title(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title_id: str
    link_id: str
    url: str
    title: str
    synopsis: str
    entity_type: str
    release_year: str | None
    runtime: str | None
    image_url: str
    maturity_rating: str | None
    benefit_id: str | None

class Container(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str
    container_type: str
    titles: list[Title]

class ParsedSearchModel(BaseModel):
    model_config = ConfigDict(defer_build=True)
    query: str
    has_failed: bool
    containers: list[Container]
    titles: list[Title]
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
