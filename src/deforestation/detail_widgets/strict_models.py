from typing import Any, Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import ConfigDict
from datetime import date
from pydantic import BaseModel

class Episode(BaseModel):
    model_config = ConfigDict(defer_build=True)
    key: str
    link_id: str
    url: str
    title: str
    episode_number: int
    synopsis: str
    duration: int
    runtime: str
    release_date: date
    image_url: str
    is_available: bool

class EpisodePage(BaseModel):
    model_config = ConfigDict(defer_build=True)
    token: str
    text: str
    is_selected: bool

class ParsedDetailWidgetsModel(BaseModel):
    model_config = ConfigDict(defer_build=True)
    header: str
    episode_count: int
    episodes: list[Episode]
    episode_pages: list[EpisodePage]
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
