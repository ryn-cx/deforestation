from good_ass_pydantic_integrator import GAPIBaseModel
from pydantic import ConfigDict, Field
from typing import Any

class Availability(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    description: str
    severity: str

class Metadata(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    availability: Availability

class Text(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    attrs: dict[str, Any]
    string: str

class EpisodePage(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    is_selected: bool = Field(..., alias='isSelected')
    text: Text
    token: str

class PaginationItem(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    text: Text
    token: str
    token_type: str = Field(..., alias='tokenType')

class SortItem(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    is_selected: bool = Field(..., alias='isSelected')
    text: Text
    token: str
    token_type: str = Field(..., alias='tokenType')

class Actions(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    episode_pages: list[EpisodePage] = Field(..., alias='episodePages')
    pagination: list[PaginationItem]
    sort: list[SortItem]

class DvMessage(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    attrs: dict[str, Any]
    string: str

class FocusMessage(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    dv_message: DvMessage = Field(..., alias='dvMessage')
    icon: str
    icon_type: str = Field(..., alias='iconType')

class Messages(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    entitlement_type: str = Field(..., alias='entitlementType')
    focus_message: FocusMessage = Field(..., alias='focusMessage')

class PurchaseData(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    app_fallback_url: str = Field(..., alias='appFallbackUrl')
    family: str
    is_season_or_series_purchase: bool = Field(..., alias='isSeasonOrSeriesPurchase')
    non_js_purchase_url: str = Field(..., alias='nonJsPurchaseUrl')
    offer_type: str = Field(..., alias='offerType')
    text: str

class Transaction(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    asin: str
    csrf_token: str = Field(..., alias='csrfToken')
    csrf_token_workflow: str = Field(..., alias='csrfTokenWorkflow')
    display_messages: list[None] = Field(..., alias='displayMessages')
    label: str
    offer_token: str = Field(..., alias='offerToken')
    purchase_data: PurchaseData = Field(..., alias='purchaseData')
    ref_marker: str = Field(..., alias='refMarker')

class Subscription(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    app_fallback_url: str = Field(..., alias='appFallbackUrl')
    app_subscription_url: str = Field(..., alias='appSubscriptionUrl')
    benefit_id: str = Field(..., alias='benefitId')
    channel_link: str = Field(..., alias='channelLink')
    display_messages: list[None] = Field(..., alias='displayMessages')
    label: str
    problems: list[None]
    ref_marker: str = Field(..., alias='refMarker')
    s_type: str = Field(..., alias='sType')
    signup_link: str = Field(..., alias='signupLink')

class Payload1(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    payload_type: str = Field(..., alias='payloadType')
    transaction: Transaction | None = None
    subscription: Subscription | None = None

class Presentation(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    icon: str | None = None
    primary_label: str = Field(..., alias='primaryLabel')
    ref_marker: str = Field(..., alias='refMarker')

class Action1(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    action_type: str = Field(..., alias='actionType')
    is_selected: bool = Field(..., alias='isSelected')
    payload: Payload1
    presentation: Presentation

class TextComponent(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    tags: dict[str, Any]
    text: str
    text_type: str = Field(..., alias='textType')

class Tags(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    logo_height: str = Field(..., alias='LOGO_HEIGHT')
    logo_entity_tag: str = Field(..., alias='LOGO_ENTITY_TAG')
    logo_width: str = Field(..., alias='LOGO_WIDTH')

class LogoComponent(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    tags: Tags
    url: str

class ComponentPayload(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    text_component: TextComponent | None = Field(None, alias='textComponent')
    logo_component: LogoComponent | None = Field(None, alias='logoComponent')

class Header(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    component_payload: ComponentPayload = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class ComponentPayload1(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    text_component: TextComponent = Field(..., alias='textComponent')

class TransactionDetail(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    component_payload: ComponentPayload1 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class Components(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    header: Header = Field(..., alias='HEADER')
    transaction_detail: TransactionDetail = Field(..., alias='TRANSACTION_DETAIL')

class ExpandingCard(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    actions: list[Action1]
    card_type: str = Field(..., alias='cardType')
    components: Components

class Transaction1(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    asin: str
    csrf_token: str = Field(..., alias='csrfToken')
    csrf_token_workflow: str = Field(..., alias='csrfTokenWorkflow')
    display_messages: list[None] = Field(..., alias='displayMessages')
    label: str
    offer_token: str = Field(..., alias='offerToken')
    purchase_data: PurchaseData = Field(..., alias='purchaseData')
    ref_marker: str = Field(..., alias='refMarker')

class Payload2(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    payload_type: str = Field(..., alias='payloadType')
    transaction: Transaction1 | None = None
    subscription: Subscription | None = None

class Action2(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    action_type: str = Field(..., alias='actionType')
    is_selected: bool = Field(..., alias='isSelected')
    payload: Payload2
    presentation: Presentation

class Tags1(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    text_theme: str = Field(..., alias='TEXT_THEME')
    brand_glow: str = Field(..., alias='BRAND_GLOW')

class TextComponent2(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    tags: Tags1
    text: str
    text_type: str = Field(..., alias='textType')

class Tags2(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    logo_height: str = Field(..., alias='LOGO_HEIGHT')
    logo_entity_tag: str = Field(..., alias='LOGO_ENTITY_TAG')
    logo_width: str = Field(..., alias='LOGO_WIDTH')
    brand_glow: str = Field(..., alias='BRAND_GLOW')

class LogoComponent1(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    tags: Tags2
    url: str

class ComponentPayload2(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    text_component: TextComponent2 | None = Field(None, alias='textComponent')
    logo_component: LogoComponent1 | None = Field(None, alias='logoComponent')

class Banner(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    component_payload: ComponentPayload2 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class TextListItem(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    tags: dict[str, Any]
    text: str
    text_type: str = Field(..., alias='textType')

class TextComponentCollection(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    text_list: list[TextListItem] = Field(..., alias='textList')

class ComponentPayload3(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    text_component_collection: TextComponentCollection = Field(..., alias='textComponentCollection')

class TransactionDetail1(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    component_payload: ComponentPayload3 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class TextComponent3(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    tags: dict[str, Any]
    text: str
    text_type: str = Field(..., alias='textType')

class Tags3(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    alt_text: str = Field(..., alias='ALT_TEXT')

class ImageListItem(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    tags: Tags3
    url: str

class ImageListComponent(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    image_list: list[ImageListItem] = Field(..., alias='imageList')

class ComponentPayload5(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    text_component: TextComponent3 | None = Field(None, alias='textComponent')
    image_list_component: ImageListComponent | None = Field(None, alias='imageListComponent')

class ComponentListItem(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    component_payload: ComponentPayload5 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class MixedComponent(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    component_list: list[ComponentListItem] = Field(..., alias='componentList')

class ComponentPayload4(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    mixed_component: MixedComponent = Field(..., alias='mixedComponent')

class RelatedBenefits(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    component_payload: ComponentPayload4 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class Components1(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    banner: Banner = Field(..., alias='BANNER')
    transaction_detail: TransactionDetail1 = Field(..., alias='TRANSACTION_DETAIL')
    related_benefits: RelatedBenefits | None = Field(None, alias='RELATED_BENEFITS')

class CardOption(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    actions: list[Action2]
    card_type: str = Field(..., alias='cardType')
    components: Components1

class Payload(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    expanding_card: ExpandingCard | None = Field(None, alias='expandingCard')
    payload_type: str = Field(..., alias='payloadType')
    card_options: list[CardOption] | None = Field(None, alias='cardOptions')

class Presentation2(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    primary_label: str = Field(..., alias='primaryLabel')
    ref_marker: str = Field(..., alias='refMarker')

class PrimaryAction(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    action_type: str = Field(..., alias='actionType')
    is_selected: bool = Field(..., alias='isSelected')
    payload: Payload
    presentation: Presentation2 | None = None

class Action(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    messages: Messages
    primary_actions: list[PrimaryAction] = Field(..., alias='primaryActions')
    secondary_actions: list[None] = Field(..., alias='secondaryActions')
    view_ref_marker: str = Field(..., alias='viewRefMarker')

class Contributors(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    cast: list[None]
    directors: list[None]
    producers: list[None]

class EnhancedSubtitle(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    text: str

class Genre(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    id: str
    search_link: str = Field(..., alias='searchLink')
    text: str

class Images(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    covershot: str
    heroshot: str
    packshot: str
    title_logo: str = Field(..., alias='titleLogo')
    titleshot: str

class Detail(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
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

class MaturityRating(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    field__type: str = Field(..., alias='__type')
    description: str
    display_text: str = Field(..., alias='displayText')
    id: str
    country_code: str | None = Field(None, alias='countryCode')

class Metadata1(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    maturity_rating: MaturityRating = Field(..., alias='maturityRating')
    traits: list[None]

class Self(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    asins: list[str]
    compact_gti: str = Field(..., alias='compactGTI')
    gti: str
    is_launched: bool = Field(..., alias='isLaunched')
    link: str
    sequence_number: int = Field(..., alias='sequenceNumber')
    title_type: str = Field(..., alias='titleType')

class Episode(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    action: Action
    detail: Detail
    metadata: Metadata1
    self: Self
    title_id: str = Field(..., alias='titleID')

class EpisodeList(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    actions: Actions
    episode_count: int = Field(..., alias='episodeCount')
    episodes: list[Episode]
    header: str

class Features(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
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

class PageContext(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
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

class Tokens(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    watchlist_csrf_token: str = Field(..., alias='watchlistCSRFToken')

class Widgets(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    episode_list: EpisodeList = Field(..., alias='episodeList')
    page_context: PageContext = Field(..., alias='pageContext')
    tokens: Tokens

class DetailWidgetsModel(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    field__type: str = Field(..., alias='__type')
    degradations: list[None]
    metadata: Metadata
    widgets: Widgets
