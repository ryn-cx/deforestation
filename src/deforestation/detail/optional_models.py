from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import Field
from datetime import date
from typing import Any
from pydantic import BaseModel, ConfigDict

class Images(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    covershot: str | Any = Field(default=None, union_mode='left_to_right')
    covershot_thumbnail: str | Any = Field(default=None, union_mode='left_to_right')
    packshot: str | Any = Field(default=None, union_mode='left_to_right')
    packshot_thumbnail: str | Any = Field(default=None, union_mode='left_to_right')
    titleshot: str | Any = Field(default=None, union_mode='left_to_right')
    titleshot_thumbnail: str | Any = Field(default=None, union_mode='left_to_right')
    heroshot: str | Any = Field(default=None, union_mode='left_to_right')
    heroshot_thumbnail: str | Any = Field(default=None, union_mode='left_to_right')
    cover: Any | None = None
    cover_thumbnail: Any | None = None
    hero: Any | None = None
    hero_thumbnail: Any | None = None
    poster2x3: Any | None = None
    poster2x3_thumbnail: Any | None = None
    boxart: Any | None = None
    boxart_thumbnail: Any | None = None
    full_background_16x9: str | Any = Field(default=None, union_mode='left_to_right')
    full_background_16x9_thumbnail: str | Any = Field(default=None, union_mode='left_to_right')
    title_logo: str | Any = Field(default=None, union_mode='left_to_right')
    title_logo_thumbnail: str | Any = Field(default=None, union_mode='left_to_right')
    provider_logo: str | Any = Field(default=None, union_mode='left_to_right')
    provider_logo_thumbnail: str | Any = Field(default=None, union_mode='left_to_right')

class Channel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    subscription_id: str | Any = Field(default=None, union_mode='left_to_right')
    name: str | Any = Field(default=None, union_mode='left_to_right')
    logo_url: str | Any = Field(default=None, union_mode='left_to_right')

class Season(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    key: str | Any = Field(default=None, union_mode='left_to_right')
    name: str | Any = Field(default=None, union_mode='left_to_right')
    season_number: int | Any = Field(default=None, union_mode='left_to_right')
    url: str | Any = Field(default=None, union_mode='left_to_right')
    is_selected: bool | Any = Field(default=None, union_mode='left_to_right')

class Images1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    covershot: str | Any = Field(default=None, union_mode='left_to_right')
    covershot_thumbnail: str | Any = Field(default=None, union_mode='left_to_right')
    packshot: str | Any = Field(default=None, union_mode='left_to_right')
    packshot_thumbnail: str | Any = Field(default=None, union_mode='left_to_right')
    titleshot: str | Any = Field(default=None, union_mode='left_to_right')
    titleshot_thumbnail: str | Any = Field(default=None, union_mode='left_to_right')
    heroshot: Any | None = None
    heroshot_thumbnail: Any | None = None
    cover: Any | None = None
    cover_thumbnail: Any | None = None
    hero: Any | None = None
    hero_thumbnail: Any | None = None
    poster2x3: Any | None = None
    poster2x3_thumbnail: Any | None = None
    boxart: Any | None = None
    boxart_thumbnail: Any | None = None
    full_background_16x9: Any | None = None
    full_background_16x9_thumbnail: Any | None = None
    title_logo: Any | None = None
    title_logo_thumbnail: Any | None = None
    provider_logo: Any | None = None
    provider_logo_thumbnail: Any | None = None

class Episode(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    key: str | Any = Field(default=None, union_mode='left_to_right')
    link_id: str | Any = Field(default=None, union_mode='left_to_right')
    url: str | Any = Field(default=None, union_mode='left_to_right')
    title: str | Any = Field(default=None, union_mode='left_to_right')
    episode_number: int | Any = Field(default=None, union_mode='left_to_right')
    synopsis: str | Any = Field(default=None, union_mode='left_to_right')
    duration: int | Any = Field(default=None, union_mode='left_to_right')
    runtime: str | Any = Field(default=None, union_mode='left_to_right')
    release_date: date | Any = Field(default=None, union_mode='left_to_right')
    images: Images1 | Any = Field(default=None, union_mode='left_to_right')
    is_available: bool | Any = Field(default=None, union_mode='left_to_right')
    subscription_ids: list[str] | Any = Field(default=None, union_mode='left_to_right')
    purchasable: bool | Any = Field(default=None, union_mode='left_to_right')

class EpisodePage(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    token: str | Any = Field(default=None, union_mode='left_to_right')
    text: str | Any = Field(default=None, union_mode='left_to_right')
    is_selected: bool | Any = Field(default=None, union_mode='left_to_right')

class Images2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    covershot: Any | None = None
    covershot_thumbnail: Any | None = None
    packshot: Any | None = None
    packshot_thumbnail: Any | None = None
    titleshot: Any | None = None
    titleshot_thumbnail: Any | None = None
    heroshot: Any | None = None
    heroshot_thumbnail: Any | None = None
    cover: str | Any = Field(default=None, union_mode='left_to_right')
    cover_thumbnail: str | Any = Field(default=None, union_mode='left_to_right')
    hero: str | Any = Field(default=None, union_mode='left_to_right')
    hero_thumbnail: str | Any = Field(default=None, union_mode='left_to_right')
    poster2x3: str | Any = Field(default=None, union_mode='left_to_right')
    poster2x3_thumbnail: str | Any = Field(default=None, union_mode='left_to_right')
    boxart: str | Any = Field(default=None, union_mode='left_to_right')
    boxart_thumbnail: str | Any = Field(default=None, union_mode='left_to_right')
    full_background_16x9: Any | None = None
    full_background_16x9_thumbnail: Any | None = None
    title_logo: str | Any = Field(default=None, union_mode='left_to_right')
    title_logo_thumbnail: str | Any = Field(default=None, union_mode='left_to_right')
    provider_logo: Any | None = None
    provider_logo_thumbnail: Any | None = None

class Title(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title_id: str | Any = Field(default=None, union_mode='left_to_right')
    link_id: str | Any = Field(default=None, union_mode='left_to_right')
    url: str | Any = Field(default=None, union_mode='left_to_right')
    title: str | Any = Field(default=None, union_mode='left_to_right')
    synopsis: str | Any = Field(default=None, union_mode='left_to_right')
    entity_type: str | Any = Field(default=None, union_mode='left_to_right')
    release_year: str | Any = Field(default=None, union_mode='left_to_right')
    runtime: str | Any = Field(default=None, union_mode='left_to_right')
    images: Images2 | Any = Field(default=None, union_mode='left_to_right')
    maturity_rating: str | Any = Field(default=None, union_mode='left_to_right')
    subscription_id: str | Any = Field(default=None, union_mode='left_to_right')

class Container(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | Any = Field(default=None, union_mode='left_to_right')
    container_type: str | Any = Field(default=None, union_mode='left_to_right')
    titles: list[Title] | Any = Field(default=None, union_mode='left_to_right')

class ParsedDetailModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    page_id: str | Any = Field(default=None, union_mode='left_to_right')
    link_id: str | Any = Field(default=None, union_mode='left_to_right')
    title_key: str | Any = Field(default=None, union_mode='left_to_right')
    url: str | Any = Field(default=None, union_mode='left_to_right')
    title: str | Any = Field(default=None, union_mode='left_to_right')
    parent_title: str | Any = Field(default=None, union_mode='left_to_right')
    synopsis: str | Any = Field(default=None, union_mode='left_to_right')
    entity_type: str | Any = Field(default=None, union_mode='left_to_right')
    title_type: str | Any = Field(default=None, union_mode='left_to_right')
    season_number: int | Any = Field(default=None, union_mode='left_to_right')
    release_date: date | Any = Field(default=None, union_mode='left_to_right')
    release_year: int | Any = Field(default=None, union_mode='left_to_right')
    duration: int | Any = Field(default=None, union_mode='left_to_right')
    runtime: str | Any = Field(default=None, union_mode='left_to_right')
    images: Images | Any = Field(default=None, union_mode='left_to_right')
    genres: list[str] | Any = Field(default=None, union_mode='left_to_right')
    studios: list[str] | Any = Field(default=None, union_mode='left_to_right')
    cast: list[str] | Any = Field(default=None, union_mode='left_to_right')
    directors: list[str] | Any = Field(default=None, union_mode='left_to_right')
    producers: list[str] | Any = Field(default=None, union_mode='left_to_right')
    audio_tracks: list[str] | Any = Field(default=None, union_mode='left_to_right')
    subtitles: list[str] | Any = Field(default=None, union_mode='left_to_right')
    maturity_rating: str | Any = Field(default=None, union_mode='left_to_right')
    amazon_rating: int | float | Any = Field(default=None, union_mode='left_to_right')
    amazon_rating_count: int | Any = Field(default=None, union_mode='left_to_right')
    imdb_rating: int | float | Any = Field(default=None, union_mode='left_to_right')
    moods: list[str] | Any = Field(default=None, union_mode='left_to_right')
    included_with_prime: bool | Any = Field(default=None, union_mode='left_to_right')
    free_with_ads: bool | Any = Field(default=None, union_mode='left_to_right')
    purchasable: bool | Any = Field(default=None, union_mode='left_to_right')
    unavailable_message: str | Any = Field(default=None, union_mode='left_to_right')
    channels: list[Channel] | Any = Field(default=None, union_mode='left_to_right')
    seasons: list[Season] | Any = Field(default=None, union_mode='left_to_right')
    episode_count: int | Any = Field(default=None, union_mode='left_to_right')
    episodes: list[Episode] | Any = Field(default=None, union_mode='left_to_right')
    episode_pages: list[EpisodePage] | Any = Field(default=None, union_mode='left_to_right')
    containers: list[Container] | Any = Field(default=None, union_mode='left_to_right')
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
