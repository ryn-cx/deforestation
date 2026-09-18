from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from datetime import date
from typing import Any
from pydantic import BaseModel, ConfigDict

class Images(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    covershot: str | None = None
    packshot: str | None = None
    titleshot: str | None = None
    heroshot: str | None = None
    title_logo: str | None = None

class Channel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    benefit_id: str | None = None
    name: str | None = None
    logo_url: str | None = None

class Season(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    key: str | None = None
    name: str | None = None
    season_number: int | None = None
    url: str | None = None
    is_selected: bool | None = None

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

class EpisodePage(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    token: str | None = None
    text: str | None = None
    is_selected: bool | None = None

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

class ParsedDetailModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    page_id: str | None = None
    link_id: str | None = None
    title_key: str | None = None
    url: str | None = None
    title: str | None = None
    parent_title: str | None = None
    synopsis: str | None = None
    entity_type: str | None = None
    title_type: str | None = None
    season_number: int | None = None
    release_date: date | None = None
    release_year: int | None = None
    duration: int | None = None
    runtime: str | None = None
    image_url: str | None = None
    images: Images | None = None
    genres: list[str] | None = None
    studios: list[str] | None = None
    cast: list[str] | None = None
    directors: list[str] | None = None
    producers: list[str] | None = None
    audio_tracks: list[str] | None = None
    subtitles: list[str] | None = None
    maturity_rating: str | None = None
    amazon_rating: int | float | None = None
    amazon_rating_count: int | None = None
    imdb_rating: int | float | None = None
    moods: list[str] | None = None
    included_with_prime: bool | None = None
    purchasable: bool | None = None
    unavailable_message: Any | None = None
    channels: list[Channel] | None = None
    seasons: list[Season] | None = None
    episode_count: int | None = None
    episodes: list[Episode] | None = None
    episode_pages: list[EpisodePage] | None = None
    containers: list[Container] | None = None
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
