from typing import Any, Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from datetime import date
from pydantic import BaseModel, ConfigDict

class Episode(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    key: str | None = None
    link_id: str | None = None
    url: str | None = None
    title: str | None = None
    episode_number: int | None = None
    synopsis: str | None = None
    duration: int | None = None
    runtime: str | None = None
    release_date: date | None = None
    image_url: str | None = None
    is_available: bool | None = None
    subscription_ids: list[str] | None = None
    purchasable: bool | None = None

class EpisodePage(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    token: str | None = None
    text: str | None = None
    is_selected: bool | None = None

class ParsedDetailWidgetsModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    header: str | None = None
    episode_count: int | None = None
    episodes: list[Episode] | None = None
    episode_pages: list[EpisodePage] | None = None
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
