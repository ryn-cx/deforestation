from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import BaseModel, ConfigDict, Field
from typing import Any

class Availability(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    description: str | None = None
    severity: str | None = None

class Metadata(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability: Availability | None = None

class Text(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    attrs: dict[str, Any] | None = None
    string: str | None = None

class EpisodePage(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_selected: bool | None = Field(None, alias='isSelected')
    text: Text | None = None
    token: str | None = None

class PaginationItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    text: Text | None = None
    token: str | None = None
    token_type: str | None = Field(None, alias='tokenType')

class SortItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_selected: bool | None = Field(None, alias='isSelected')
    text: Text | None = None
    token: str | None = None
    token_type: str | None = Field(None, alias='tokenType')

class Actions(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    episode_pages: list[EpisodePage] | None = Field(None, alias='episodePages')
    pagination: list[PaginationItem] | None = None
    sort: list[SortItem] | None = None

class DvMessage(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    attrs: dict[str, Any] | None = None
    string: str | None = None

class FocusMessage(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    dv_message: DvMessage | None = Field(None, alias='dvMessage')
    icon: str | None = None
    icon_type: str | None = Field(None, alias='iconType')

class Messages(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    entitlement_type: str | None = Field(None, alias='entitlementType')
    focus_message: FocusMessage | None = Field(None, alias='focusMessage')

class PurchaseData(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    app_fallback_url: str | None = Field(None, alias='appFallbackUrl')
    family: str | None = None
    is_season_or_series_purchase: bool | None = Field(None, alias='isSeasonOrSeriesPurchase')
    non_js_purchase_url: str | None = Field(None, alias='nonJsPurchaseUrl')
    offer_type: str | None = Field(None, alias='offerType')
    text: str | None = None

class Transaction(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    asin: str | None = None
    csrf_token: str | None = Field(None, alias='csrfToken')
    csrf_token_workflow: str | None = Field(None, alias='csrfTokenWorkflow')
    display_messages: list[Any] | None = Field(None, alias='displayMessages')
    label: str | None = None
    offer_token: str | None = Field(None, alias='offerToken')
    purchase_data: PurchaseData | None = Field(None, alias='purchaseData')
    ref_marker: str | None = Field(None, alias='refMarker')

class Payload1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    payload_type: str | None = Field(None, alias='payloadType')
    transaction: Transaction | None = None

class Presentation(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    icon: str | None = None
    primary_label: str | None = Field(None, alias='primaryLabel')
    ref_marker: str | None = Field(None, alias='refMarker')

class Action1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    action_type: str | None = Field(None, alias='actionType')
    is_selected: bool | None = Field(None, alias='isSelected')
    payload: Payload1 | None = None
    presentation: Presentation | None = None

class TextComponent(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    tags: dict[str, Any] | None = None
    text: str | None = None
    text_type: str | None = Field(None, alias='textType')

class ComponentPayload(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    text_component: TextComponent | None = Field(None, alias='textComponent')

class Header(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    component_payload: ComponentPayload | None = Field(None, alias='componentPayload')
    component_primitive: str | None = Field(None, alias='componentPrimitive')

class ComponentPayload1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    text_component: TextComponent | None = Field(None, alias='textComponent')

class TransactionDetail(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    component_payload: ComponentPayload1 | None = Field(None, alias='componentPayload')
    component_primitive: str | None = Field(None, alias='componentPrimitive')

class Components(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    header: Header | None = Field(None, alias='HEADER')
    transaction_detail: TransactionDetail | None = Field(None, alias='TRANSACTION_DETAIL')

class ExpandingCard(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    actions: list[Action1] | None = None
    card_type: str | None = Field(None, alias='cardType')
    components: Components | None = None

class Transaction1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    asin: str | None = None
    csrf_token: str | None = Field(None, alias='csrfToken')
    csrf_token_workflow: str | None = Field(None, alias='csrfTokenWorkflow')
    display_messages: list[Any] | None = Field(None, alias='displayMessages')
    label: str | None = None
    offer_token: str | None = Field(None, alias='offerToken')
    purchase_data: PurchaseData | None = Field(None, alias='purchaseData')
    ref_marker: str | None = Field(None, alias='refMarker')

class Payload2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    payload_type: str | None = Field(None, alias='payloadType')
    transaction: Transaction1 | None = None

class Action2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    action_type: str | None = Field(None, alias='actionType')
    is_selected: bool | None = Field(None, alias='isSelected')
    payload: Payload2 | None = None
    presentation: Presentation | None = None

class Tags(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    text_theme: str | None = Field(None, alias='TEXT_THEME')
    brand_glow: str | None = Field(None, alias='BRAND_GLOW')

class TextComponent2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    tags: Tags | None = None
    text: str | None = None
    text_type: str | None = Field(None, alias='textType')

class ComponentPayload2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    text_component: TextComponent2 | None = Field(None, alias='textComponent')

class Banner(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    component_payload: ComponentPayload2 | None = Field(None, alias='componentPayload')
    component_primitive: str | None = Field(None, alias='componentPrimitive')

class TextListItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    tags: dict[str, Any] | None = None
    text: str | None = None
    text_type: str | None = Field(None, alias='textType')

class TextComponentCollection(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    text_list: list[TextListItem] | None = Field(None, alias='textList')

class ComponentPayload3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    text_component_collection: TextComponentCollection | None = Field(None, alias='textComponentCollection')

class TransactionDetail1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    component_payload: ComponentPayload3 | None = Field(None, alias='componentPayload')
    component_primitive: str | None = Field(None, alias='componentPrimitive')

class Components1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    banner: Banner | None = Field(None, alias='BANNER')
    transaction_detail: TransactionDetail1 | None = Field(None, alias='TRANSACTION_DETAIL')

class CardOption(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    actions: list[Action2] | None = None
    card_type: str | None = Field(None, alias='cardType')
    components: Components1 | None = None

class Payload(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    expanding_card: ExpandingCard | None = Field(None, alias='expandingCard')
    payload_type: str | None = Field(None, alias='payloadType')
    card_options: list[CardOption] | None = Field(None, alias='cardOptions')

class Presentation2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    primary_label: str | None = Field(None, alias='primaryLabel')
    ref_marker: str | None = Field(None, alias='refMarker')

class PrimaryAction(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    action_type: str | None = Field(None, alias='actionType')
    is_selected: bool | None = Field(None, alias='isSelected')
    payload: Payload | None = None
    presentation: Presentation2 | None = None

class Action(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    messages: Messages | None = None
    primary_actions: list[PrimaryAction] | None = Field(None, alias='primaryActions')
    secondary_actions: list[Any] | None = Field(None, alias='secondaryActions')
    view_ref_marker: str | None = Field(None, alias='viewRefMarker')

class Contributors(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    cast: list[Any] | None = None
    directors: list[Any] | None = None
    producers: list[Any] | None = None

class EnhancedSubtitle(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    text: str | None = None

class Genre(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    id: str | None = None
    search_link: str | None = Field(None, alias='searchLink')
    text: str | None = None

class Images(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    covershot: str | None = None
    heroshot: str | None = None
    packshot: str | None = None
    title_logo: str | None = Field(None, alias='titleLogo')
    titleshot: str | None = None

class Detail(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    audio_tracks: list[str] | None = Field(None, alias='audioTracks')
    catalog_id: str | None = Field(None, alias='catalogId')
    contributors: Contributors | None = None
    duration: int | None = None
    enhanced_subtitles: list[EnhancedSubtitle] | None = Field(None, alias='enhancedSubtitles')
    entity_type: str | None = Field(None, alias='entityType')
    episode_number: int | None = Field(None, alias='episodeNumber')
    genres: list[Genre] | None = None
    images: Images | None = None
    is_ad: bool | None = Field(None, alias='isAd')
    is_closed_caption: bool | None = Field(None, alias='isClosedCaption')
    is_dolby51: bool | None = Field(None, alias='isDolby51')
    is_dolby_atmos: bool | None = Field(None, alias='isDolbyAtmos')
    is_dolby_vision: bool | None = Field(None, alias='isDolbyVision')
    is_hdr: bool | None = Field(None, alias='isHdr')
    is_hdr10_plus: bool | None = Field(None, alias='isHdr10Plus')
    is_prime: bool | None = Field(None, alias='isPrime')
    is_pse: bool | None = Field(None, alias='isPse')
    is_starlight_enhanced: bool | None = Field(None, alias='isStarlightEnhanced')
    is_uhd: bool | None = Field(None, alias='isUhd')
    is_x_ray: bool | None = Field(None, alias='isXRay')
    playback_tracks: list[Any] | None = Field(None, alias='playbackTracks')
    release_date: str | None = Field(None, alias='releaseDate')
    release_year: int | None = Field(None, alias='releaseYear')
    runtime: str | None = None
    studios: list[str] | None = None
    subtitles: list[str] | None = None
    synopsis: str | None = None
    title: str | None = None
    title_type: str | None = Field(None, alias='titleType')

class MaturityRating(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__type: str | None = Field(None, alias='__type')
    description: str | None = None
    display_text: str | None = Field(None, alias='displayText')
    id: str | None = None

class Metadata1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    maturity_rating: MaturityRating | None = Field(None, alias='maturityRating')
    traits: list[Any] | None = None

class Self(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    asins: list[str] | None = None
    compact_gti: str | None = Field(None, alias='compactGTI')
    gti: str | None = None
    is_launched: bool | None = Field(None, alias='isLaunched')
    link: str | None = None
    sequence_number: int | None = Field(None, alias='sequenceNumber')
    title_type: str | None = Field(None, alias='titleType')

class Episode(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    action: Action | None = None
    detail: Detail | None = None
    metadata: Metadata1 | None = None
    self: Self | None = None
    title_id: str | None = Field(None, alias='titleID')

class EpisodeList(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    actions: Actions | None = None
    episode_count: int | None = Field(None, alias='episodeCount')
    episodes: list[Episode] | None = None
    header: str | None = None

class Features(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_reviews_submission_enabled: str | None = Field(None, alias='isReviewsSubmissionEnabled')
    disable_marin_tracking: str | None = Field(None, alias='disableMarinTracking')
    disable_hover: str | None = Field(None, alias='disableHover')
    is_record_season_enabled: str | None = Field(None, alias='isRecordSeasonEnabled')
    is_autoplay_setting_enabled: str | None = Field(None, alias='isAutoplaySettingEnabled')
    offer_clarity_enabled: str | None = Field(None, alias='offerClarityEnabled')
    disable_explore_tab: str | None = Field(None, alias='disableExploreTab')
    disable_whisper_cache_in_draper: str | None = Field(None, alias='disableWhisperCacheInDraper')
    is_swm_enabled: str | None = Field(None, alias='isSWMEnabled')
    activate_auto_playing_in_hovers: str | None = Field(None, alias='activateAutoPlayingInHovers')
    is_detail_page_header_widget_refresh_enabled: str | None = Field(None, alias='isDetailPageHeaderWidgetRefreshEnabled')
    is_spider_noir: str | None = Field(None, alias='isSpiderNoir')
    is_detail_page_header_widget_enabled: str | None = Field(None, alias='isDetailPageHeaderWidgetEnabled')
    disable_player_for_google_bot: str | None = Field(None, alias='disablePlayerForGoogleBot')
    panorama_treatment: str | None = Field(None, alias='panoramaTreatment')
    is_stream_selector_modal_enabled: str | None = Field(None, alias='isStreamSelectorModalEnabled')
    disable_enrich_item_metadata: str | None = Field(None, alias='disableEnrichItemMetadata')

class PageContext(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    app: str | None = None
    download_launch_type: str | None = Field(None, alias='downloadLaunchType')
    enable_hover: bool | None = Field(None, alias='enableHover')
    features: Features | None = None
    form_factor: str | None = Field(None, alias='formFactor')
    is_cerberus_child: bool | None = Field(None, alias='isCerberusChild')
    is_recording: bool | None = Field(None, alias='isRecording')
    os: str | None = None
    page_title_id: str | None = Field(None, alias='pageTitleId')
    page_type: str | None = Field(None, alias='pageType')
    playback_launch_type: str | None = Field(None, alias='playbackLaunchType')
    playback_trailer_launch_type: str | None = Field(None, alias='playbackTrailerLaunchType')
    purchase_launch_type: str | None = Field(None, alias='purchaseLaunchType')
    purchase_restricted: bool | None = Field(None, alias='purchaseRestricted')
    swift_parameters: dict[str, Any] | None = Field(None, alias='swiftParameters')

class Tokens(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    watchlist_csrf_token: str | None = Field(None, alias='watchlistCSRFToken')

class Widgets(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    episode_list: EpisodeList | None = Field(None, alias='episodeList')
    page_context: PageContext | None = Field(None, alias='pageContext')
    tokens: Tokens | None = None

class DetailWidgetsModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__type: str | None = Field(None, alias='__type')
    degradations: list[Any] | None = None
    metadata: Metadata | None = None
    widgets: Widgets | None = None
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
