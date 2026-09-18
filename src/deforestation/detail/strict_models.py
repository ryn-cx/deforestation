from typing import Any, Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import ConfigDict
from datetime import date
from pydantic import BaseModel

class Images(BaseModel):
    model_config = ConfigDict(defer_build=True)
    covershot: str
    packshot: str
    titleshot: str
    heroshot: str
    title_logo: str | None

class Channel(BaseModel):
    model_config = ConfigDict(defer_build=True)
    benefit_id: str
    name: str
    logo_url: str

class Season(BaseModel):
    model_config = ConfigDict(defer_build=True)
    key: str
    name: str
    season_number: int
    url: str
    is_selected: bool

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

class Title(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title_id: str
    link_id: str
    url: str
    title: str
    synopsis: str
    entity_type: str
    release_year: str
    runtime: str | None
    image_url: str | None
    maturity_rating: str
    benefit_id: str | None

class Container(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str
    container_type: str
    titles: list[Title]

class ParsedDetailModel(BaseModel):
    model_config = ConfigDict(defer_build=True)
    page_id: str
    link_id: str
    title_key: str
    url: str
    title: str
    parent_title: str | None
    synopsis: str
    entity_type: str
    title_type: str
    season_number: int | None
    release_date: date
    release_year: int
    duration: int | None
    runtime: str | None
    image_url: str
    images: Images
    genres: list[str]
    studios: list[str]
    cast: list[str]
    directors: list[str]
    producers: list[str]
    audio_tracks: list[str]
    subtitles: list[str]
    maturity_rating: str
    amazon_rating: int | float | None
    amazon_rating_count: int | None
    imdb_rating: int | float | None
    moods: list[str]
    included_with_prime: bool
    purchasable: bool
    unavailable_message: None
    channels: list[Channel]
    seasons: list[Season]
    episode_count: int | None
    episodes: list[Episode]
    episode_pages: list[EpisodePage]
    containers: list[Container]
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
