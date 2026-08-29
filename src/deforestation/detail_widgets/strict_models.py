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

class EpisodePage(BaseModel):
    model_config = ConfigDict(defer_build=True)
    is_selected: bool = Field(..., alias='isSelected')
    text: Text
    token: str

class PaginationItem(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text: Text
    token: str
    token_type: str = Field(..., alias='tokenType')

class SortItem(BaseModel):
    model_config = ConfigDict(defer_build=True)
    is_selected: bool = Field(..., alias='isSelected')
    text: Text
    token: str
    token_type: str = Field(..., alias='tokenType')

class Actions(BaseModel):
    model_config = ConfigDict(defer_build=True)
    episode_pages: list[EpisodePage] = Field(..., alias='episodePages')
    pagination: list[PaginationItem]
    sort: list[SortItem]

class DvMessage(BaseModel):
    model_config = ConfigDict(defer_build=True)
    attrs: dict[str, Any]
    string: str

class FocusMessage(BaseModel):
    model_config = ConfigDict(defer_build=True)
    dv_message: DvMessage = Field(..., alias='dvMessage')
    icon: str
    icon_type: str = Field(..., alias='iconType')

class Messages(BaseModel):
    model_config = ConfigDict(defer_build=True)
    entitlement_type: str = Field(..., alias='entitlementType')
    focus_message: FocusMessage = Field(..., alias='focusMessage')

class PurchaseData(BaseModel):
    model_config = ConfigDict(defer_build=True)
    app_fallback_url: str = Field(..., alias='appFallbackUrl')
    family: str
    is_season_or_series_purchase: bool = Field(..., alias='isSeasonOrSeriesPurchase')
    non_js_purchase_url: str = Field(..., alias='nonJsPurchaseUrl')
    offer_type: str = Field(..., alias='offerType')
    text: str

class Transaction(BaseModel):
    model_config = ConfigDict(defer_build=True)
    asin: str
    csrf_token: str = Field(..., alias='csrfToken')
    csrf_token_workflow: str = Field(..., alias='csrfTokenWorkflow')
    display_messages: list[None] = Field(..., alias='displayMessages')
    label: str
    offer_token: str = Field(..., alias='offerToken')
    purchase_data: PurchaseData = Field(..., alias='purchaseData')
    ref_marker: str = Field(..., alias='refMarker')

class Payload1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    payload_type: str = Field(..., alias='payloadType')
    transaction: Transaction

class Presentation(BaseModel):
    model_config = ConfigDict(defer_build=True)
    icon: str
    primary_label: str = Field(..., alias='primaryLabel')
    ref_marker: str = Field(..., alias='refMarker')

class Action1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    action_type: str = Field(..., alias='actionType')
    is_selected: bool = Field(..., alias='isSelected')
    payload: Payload1
    presentation: Presentation

class TextComponent(BaseModel):
    model_config = ConfigDict(defer_build=True)
    tags: dict[str, Any]
    text: str
    text_type: str = Field(..., alias='textType')

class ComponentPayload(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_component: TextComponent = Field(..., alias='textComponent')

class Header(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class ComponentPayload1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_component: TextComponent = Field(..., alias='textComponent')

class TransactionDetail(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload1 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class Components(BaseModel):
    model_config = ConfigDict(defer_build=True)
    header: Header = Field(..., alias='HEADER')
    transaction_detail: TransactionDetail = Field(..., alias='TRANSACTION_DETAIL')

class ExpandingCard(BaseModel):
    model_config = ConfigDict(defer_build=True)
    actions: list[Action1]
    card_type: str = Field(..., alias='cardType')
    components: Components

class Transaction1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    asin: str
    csrf_token: str = Field(..., alias='csrfToken')
    csrf_token_workflow: str = Field(..., alias='csrfTokenWorkflow')
    display_messages: list[None] = Field(..., alias='displayMessages')
    label: str
    offer_token: str = Field(..., alias='offerToken')
    purchase_data: PurchaseData = Field(..., alias='purchaseData')
    ref_marker: str = Field(..., alias='refMarker')

class Payload2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    payload_type: str = Field(..., alias='payloadType')
    transaction: Transaction1

class Action2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    action_type: str = Field(..., alias='actionType')
    is_selected: bool = Field(..., alias='isSelected')
    payload: Payload2
    presentation: Presentation

class Tags(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_theme: str = Field(..., alias='TEXT_THEME')
    brand_glow: str = Field(..., alias='BRAND_GLOW')

class TextComponent2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    tags: Tags
    text: str
    text_type: str = Field(..., alias='textType')

class ComponentPayload2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_component: TextComponent2 = Field(..., alias='textComponent')

class Banner(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload2 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class TextListItem(BaseModel):
    model_config = ConfigDict(defer_build=True)
    tags: dict[str, Any]
    text: str
    text_type: str = Field(..., alias='textType')

class TextComponentCollection(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_list: list[TextListItem] = Field(..., alias='textList')

class ComponentPayload3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_component_collection: TextComponentCollection = Field(..., alias='textComponentCollection')

class TransactionDetail1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload3 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class Components1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    banner: Banner = Field(..., alias='BANNER')
    transaction_detail: TransactionDetail1 = Field(..., alias='TRANSACTION_DETAIL')

class CardOption(BaseModel):
    model_config = ConfigDict(defer_build=True)
    actions: list[Action2]
    card_type: str = Field(..., alias='cardType')
    components: Components1

class Payload(BaseModel):
    model_config = ConfigDict(defer_build=True)
    expanding_card: ExpandingCard | None = Field(None, alias='expandingCard')
    payload_type: str = Field(..., alias='payloadType')
    card_options: list[CardOption] | None = Field(None, alias='cardOptions')

class Presentation2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    primary_label: str = Field(..., alias='primaryLabel')
    ref_marker: str = Field(..., alias='refMarker')

class PrimaryAction(BaseModel):
    model_config = ConfigDict(defer_build=True)
    action_type: str = Field(..., alias='actionType')
    is_selected: bool = Field(..., alias='isSelected')
    payload: Payload
    presentation: Presentation2 | None = None

class Action(BaseModel):
    model_config = ConfigDict(defer_build=True)
    messages: Messages
    primary_actions: list[PrimaryAction] = Field(..., alias='primaryActions')
    secondary_actions: list[None] = Field(..., alias='secondaryActions')
    view_ref_marker: str = Field(..., alias='viewRefMarker')

class Contributors(BaseModel):
    model_config = ConfigDict(defer_build=True)
    cast: list[None]
    directors: list[None]
    producers: list[None]

class EnhancedSubtitle(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text: str

class Genre(BaseModel):
    model_config = ConfigDict(defer_build=True)
    id: str
    search_link: str = Field(..., alias='searchLink')
    text: str

class Images(BaseModel):
    model_config = ConfigDict(defer_build=True)
    covershot: str
    heroshot: str
    packshot: str
    title_logo: str = Field(..., alias='titleLogo')
    titleshot: str

class Detail(BaseModel):
    model_config = ConfigDict(defer_build=True)
    audio_tracks: list[str] = Field(..., alias='audioTracks')
    catalog_id: str = Field(..., alias='catalogId')
    contributors: Contributors
    duration: int
    enhanced_subtitles: list[EnhancedSubtitle] = Field(..., alias='enhancedSubtitles')
    entity_type: str = Field(..., alias='entityType')
    episode_number: int = Field(..., alias='episodeNumber')
    genres: list[Genre]
    images: Images
    is_ad: bool = Field(..., alias='isAd')
    is_closed_caption: bool = Field(..., alias='isClosedCaption')
    is_dolby51: bool = Field(..., alias='isDolby51')
    is_dolby_atmos: bool = Field(..., alias='isDolbyAtmos')
    is_dolby_vision: bool = Field(..., alias='isDolbyVision')
    is_hdr: bool = Field(..., alias='isHdr')
    is_hdr10_plus: bool = Field(..., alias='isHdr10Plus')
    is_prime: bool = Field(..., alias='isPrime')
    is_pse: bool = Field(..., alias='isPse')
    is_starlight_enhanced: bool = Field(..., alias='isStarlightEnhanced')
    is_uhd: bool = Field(..., alias='isUhd')
    is_x_ray: bool = Field(..., alias='isXRay')
    playback_tracks: list[None] = Field(..., alias='playbackTracks')
    release_date: str = Field(..., alias='releaseDate')
    release_year: int = Field(..., alias='releaseYear')
    runtime: str
    studios: list[str]
    subtitles: list[str]
    synopsis: str
    title: str
    title_type: str = Field(..., alias='titleType')

class MaturityRating(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field__type: str = Field(..., alias='__type')
    description: str
    display_text: str = Field(..., alias='displayText')
    id: str

class Metadata1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    maturity_rating: MaturityRating = Field(..., alias='maturityRating')
    traits: list[None]

class Self(BaseModel):
    model_config = ConfigDict(defer_build=True)
    asins: list[str]
    compact_gti: str = Field(..., alias='compactGTI')
    gti: str
    is_launched: bool = Field(..., alias='isLaunched')
    link: str
    sequence_number: int = Field(..., alias='sequenceNumber')
    title_type: str = Field(..., alias='titleType')

class Episode(BaseModel):
    model_config = ConfigDict(defer_build=True)
    action: Action
    detail: Detail
    metadata: Metadata1
    self: Self
    title_id: str = Field(..., alias='titleID')

class EpisodeList(BaseModel):
    model_config = ConfigDict(defer_build=True)
    actions: Actions
    episode_count: int = Field(..., alias='episodeCount')
    episodes: list[Episode]
    header: str

class Features(BaseModel):
    model_config = ConfigDict(defer_build=True)
    is_reviews_submission_enabled: str = Field(..., alias='isReviewsSubmissionEnabled')
    disable_marin_tracking: str = Field(..., alias='disableMarinTracking')
    disable_hover: str = Field(..., alias='disableHover')
    is_record_season_enabled: str = Field(..., alias='isRecordSeasonEnabled')
    is_autoplay_setting_enabled: str = Field(..., alias='isAutoplaySettingEnabled')
    offer_clarity_enabled: str = Field(..., alias='offerClarityEnabled')
    disable_explore_tab: str = Field(..., alias='disableExploreTab')
    disable_whisper_cache_in_draper: str = Field(..., alias='disableWhisperCacheInDraper')
    is_swm_enabled: str = Field(..., alias='isSWMEnabled')
    activate_auto_playing_in_hovers: str = Field(..., alias='activateAutoPlayingInHovers')
    is_detail_page_header_widget_refresh_enabled: str = Field(..., alias='isDetailPageHeaderWidgetRefreshEnabled')
    is_spider_noir: str = Field(..., alias='isSpiderNoir')
    is_detail_page_header_widget_enabled: str = Field(..., alias='isDetailPageHeaderWidgetEnabled')
    disable_player_for_google_bot: str = Field(..., alias='disablePlayerForGoogleBot')
    panorama_treatment: str = Field(..., alias='panoramaTreatment')
    is_stream_selector_modal_enabled: str = Field(..., alias='isStreamSelectorModalEnabled')
    disable_enrich_item_metadata: str = Field(..., alias='disableEnrichItemMetadata')

class PageContext(BaseModel):
    model_config = ConfigDict(defer_build=True)
    app: str
    download_launch_type: str = Field(..., alias='downloadLaunchType')
    enable_hover: bool = Field(..., alias='enableHover')
    features: Features
    form_factor: str = Field(..., alias='formFactor')
    is_cerberus_child: bool = Field(..., alias='isCerberusChild')
    is_recording: bool = Field(..., alias='isRecording')
    os: str
    page_title_id: str = Field(..., alias='pageTitleId')
    page_type: str = Field(..., alias='pageType')
    playback_launch_type: str = Field(..., alias='playbackLaunchType')
    playback_trailer_launch_type: str = Field(..., alias='playbackTrailerLaunchType')
    purchase_launch_type: str = Field(..., alias='purchaseLaunchType')
    purchase_restricted: bool = Field(..., alias='purchaseRestricted')
    swift_parameters: dict[str, Any] = Field(..., alias='swiftParameters')

class Tokens(BaseModel):
    model_config = ConfigDict(defer_build=True)
    watchlist_csrf_token: str = Field(..., alias='watchlistCSRFToken')

class Widgets(BaseModel):
    model_config = ConfigDict(defer_build=True)
    episode_list: EpisodeList = Field(..., alias='episodeList')
    page_context: PageContext = Field(..., alias='pageContext')
    tokens: Tokens

class DetailWidgetsModel(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field__type: str = Field(..., alias='__type')
    degradations: list[None]
    metadata: Metadata
    widgets: Widgets
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
