from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import ConfigDict
from pydantic import BaseModel, Field
from typing import Any
from ipaddress import IPv4Address

class MetaTag(BaseModel):
    model_config = ConfigDict(defer_build=True)
    name: str
    content: str

class LinkTag(BaseModel):
    model_config = ConfigDict(defer_build=True)
    rel: str
    href: str

class SeoMetadata(BaseModel):
    model_config = ConfigDict(defer_build=True)
    canonical_url: str = Field(..., alias='canonicalUrl')
    script_tags: list[None] = Field(..., alias='scriptTags')
    meta_tags: list[MetaTag] = Field(..., alias='metaTags')
    meta_tags_rd_fa: list[None] = Field(..., alias='metaTagsRDFa')
    title: str
    link_tags: list[LinkTag] = Field(..., alias='linkTags')

class PageMetadata(BaseModel):
    model_config = ConfigDict(defer_build=True)
    page_type: str = Field(..., alias='pageType')
    sub_page_type: str = Field(..., alias='subPageType')
    page_type_id: str = Field(..., alias='pageTypeId')

class Meta(BaseModel):
    model_config = ConfigDict(defer_build=True)
    name: str
    content: str

class SitewideNavigationBar(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str
    meta: Meta

class SitewideInlineScriptsTop(BaseModel):
    model_config = ConfigDict(defer_build=True)
    include_common_meta: bool = Field(..., alias='includeCommonMeta')
    logging_endpoint: str = Field(..., alias='loggingEndpoint')
    disable_legacy_csm_postbacks: bool = Field(..., alias='disableLegacyCsmPostbacks')
    scope_search: bool = Field(..., alias='scopeSearch')
    include_arabic_font: bool = Field(..., alias='includeArabicFont')
    include_site_verification: bool = Field(..., alias='includeSiteVerification')
    include_min_body_width: bool = Field(..., alias='includeMinBodyWidth')
    include_pwa_manifest: bool = Field(..., alias='includePWAManifest')
    include_smart_app_banner: bool = Field(..., alias='includeSmartAppBanner')
    page_type: str = Field(..., alias='pageType')
    sub_page_type: str = Field(..., alias='subPageType')
    page_type_id: str = Field(..., alias='pageTypeId')

class SitewideInlineScriptsBottom(BaseModel):
    model_config = ConfigDict(defer_build=True)
    include_common_meta: bool = Field(..., alias='includeCommonMeta')
    logging_endpoint: str = Field(..., alias='loggingEndpoint')
    disable_legacy_csm_postbacks: bool = Field(..., alias='disableLegacyCsmPostbacks')
    scope_search: bool = Field(..., alias='scopeSearch')
    include_arabic_font: bool = Field(..., alias='includeArabicFont')
    include_site_verification: bool = Field(..., alias='includeSiteVerification')
    include_min_body_width: bool = Field(..., alias='includeMinBodyWidth')
    include_pwa_manifest: bool = Field(..., alias='includePWAManifest')
    include_smart_app_banner: bool = Field(..., alias='includeSmartAppBanner')
    page_type: str = Field(..., alias='pageType')
    sub_page_type: str = Field(..., alias='subPageType')
    page_type_id: str = Field(..., alias='pageTypeId')

class SitewideHead(BaseModel):
    model_config = ConfigDict(defer_build=True)
    sitewide_navigation_bar: SitewideNavigationBar = Field(..., alias='sitewide-navigation-bar')
    sitewide_footer: dict[str, Any] = Field(..., alias='sitewide-footer')
    sitewide_inline_scripts_top: SitewideInlineScriptsTop = Field(..., alias='sitewide-inline-scripts-top')
    sitewide_inline_scripts_bottom: SitewideInlineScriptsBottom = Field(..., alias='sitewide-inline-scripts-bottom')
    sitewide_conditional: dict[str, Any] = Field(..., alias='sitewide-conditional')
    sitewide_payment_state_message: dict[str, Any] = Field(..., alias='sitewide-payment-state-message')
    sitewide_cross_benefit_modal: dict[str, Any] = Field(..., alias='sitewide-cross-benefit-modal')
    sitewide_deprecated_browsers_banner: dict[str, Any] = Field(..., alias='sitewide-deprecated-browsers-banner')
    sitewide_language_notification: dict[str, Any] = Field(..., alias='sitewide-language-notification')
    sitewide_inspector: dict[str, Any] = Field(..., alias='sitewide-inspector')
    sitewide_alexa: dict[str, Any] = Field(..., alias='sitewide-alexa')

class Head(BaseModel):
    model_config = ConfigDict(defer_build=True)
    seo_metadata: SeoMetadata = Field(..., alias='seoMetadata')
    page_metadata: PageMetadata = Field(..., alias='pageMetadata')
    sitewide_head: SitewideHead = Field(..., alias='sitewideHead')
    title: str

class Availability(BaseModel):
    model_config = ConfigDict(defer_build=True)
    description: str
    severity: str

class Metadata(BaseModel):
    model_config = ConfigDict(defer_build=True)
    availability: Availability

class PangaeaBanner(BaseModel):
    model_config = ConfigDict(defer_build=True)
    csrf_token: str = Field(..., alias='csrfToken')
    metadata: Metadata

class Features(BaseModel):
    model_config = ConfigDict(defer_build=True)
    is_elcano: bool = Field(..., alias='isElcano')
    enable_marin_tracking: bool = Field(..., alias='enableMarinTracking')

class AmazonRating(BaseModel):
    model_config = ConfigDict(defer_build=True)
    count: int
    count_formatted: str = Field(..., alias='countFormatted')
    value: float

class CastItem(BaseModel):
    model_config = ConfigDict(defer_build=True)
    name: str
    search_link: str = Field(..., alias='searchLink')

class Director(BaseModel):
    model_config = ConfigDict(defer_build=True)
    name: str
    search_link: str = Field(..., alias='searchLink')

class Producer(BaseModel):
    model_config = ConfigDict(defer_build=True)
    name: str
    search_link: str = Field(..., alias='searchLink')

class Contributors(BaseModel):
    model_config = ConfigDict(defer_build=True)
    cast: list[CastItem]
    directors: list[Director]
    producers: list[Producer]

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

class RatingBadge(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field__type: str = Field(..., alias='__type')
    description: str
    display_text: str = Field(..., alias='displayText')
    id: str
    country_code: str | None = Field(None, alias='countryCode')

class FiveStar(BaseModel):
    model_config = ConfigDict(defer_build=True)
    hover_text: str | None = Field(None, alias='hoverText')
    percentage: int
    percentage_display: str = Field(..., alias='percentageDisplay')
    rating_display_label: str = Field(..., alias='ratingDisplayLabel')
    url: str | None = None

class FourStar(BaseModel):
    model_config = ConfigDict(defer_build=True)
    hover_text: str | None = Field(None, alias='hoverText')
    percentage: int
    percentage_display: str = Field(..., alias='percentageDisplay')
    rating_display_label: str = Field(..., alias='ratingDisplayLabel')
    url: str | None = None

class OneStar(BaseModel):
    model_config = ConfigDict(defer_build=True)
    hover_text: str | None = Field(None, alias='hoverText')
    percentage: int
    percentage_display: str = Field(..., alias='percentageDisplay')
    rating_display_label: str = Field(..., alias='ratingDisplayLabel')
    url: str | None = None

class ThreeStar(BaseModel):
    model_config = ConfigDict(defer_build=True)
    hover_text: str | None = Field(None, alias='hoverText')
    percentage: int
    percentage_display: str = Field(..., alias='percentageDisplay')
    rating_display_label: str = Field(..., alias='ratingDisplayLabel')
    url: str | None = None

class TwoStar(BaseModel):
    model_config = ConfigDict(defer_build=True)
    hover_text: str | None = Field(None, alias='hoverText')
    percentage: int
    percentage_display: str = Field(..., alias='percentageDisplay')
    rating_display_label: str = Field(..., alias='ratingDisplayLabel')
    url: str | None = None

class RatingsHistogram(BaseModel):
    model_config = ConfigDict(defer_build=True)
    five_star: FiveStar = Field(..., alias='fiveStar')
    four_star: FourStar = Field(..., alias='fourStar')
    one_star: OneStar = Field(..., alias='oneStar')
    three_star: ThreeStar = Field(..., alias='threeStar')
    two_star: TwoStar = Field(..., alias='twoStar')

class ReviewRatingInfo(BaseModel):
    model_config = ConfigDict(defer_build=True)
    average_rating_label: str = Field(..., alias='averageRatingLabel')
    has_half_star: bool = Field(..., alias='hasHalfStar')
    star_count: int = Field(..., alias='starCount')
    total_review_count: int = Field(..., alias='totalReviewCount')
    total_review_count_text: str = Field(..., alias='totalReviewCountText')

class ReviewsAnalysisModel(BaseModel):
    model_config = ConfigDict(defer_build=True)
    ratings_histogram: RatingsHistogram = Field(..., alias='ratingsHistogram')
    review_rating_info: ReviewRatingInfo | None = Field(None, alias='reviewRatingInfo')

class Reviews(BaseModel):
    model_config = ConfigDict(defer_build=True)
    all_reviews_link: str = Field(..., alias='allReviewsLink')
    create_review_link: str = Field(..., alias='createReviewLink')
    locale_language: str = Field(..., alias='localeLanguage')
    review_submission_token: str = Field(..., alias='reviewSubmissionToken')
    reviews_analysis_model: ReviewsAnalysisModel = Field(..., alias='reviewsAnalysisModel')
    title_id: str = Field(..., alias='titleID')

class HeaderDetail(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str
    synopsis: str
    amazon_rating: AmazonRating | None = Field(None, alias='amazonRating')
    audio_tracks: list[str] = Field(..., alias='audioTracks')
    catalog_id: str = Field(..., alias='catalogId')
    contributors: Contributors
    enhanced_subtitles: list[EnhancedSubtitle] = Field(..., alias='enhancedSubtitles')
    entity_type: str = Field(..., alias='entityType')
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
    parent_title: str | None = Field(None, alias='parentTitle')
    playback_tracks: list[None] = Field(..., alias='playbackTracks')
    rating_badge: RatingBadge = Field(..., alias='ratingBadge')
    release_date: str = Field(..., alias='releaseDate')
    release_year: int = Field(..., alias='releaseYear')
    reviews: Reviews
    runtime: str
    season_number: int | None = Field(None, alias='seasonNumber')
    studios: list[str]
    subtitles: list[str]
    title_type: str = Field(..., alias='titleType')
    duration: int | None = None

class Detail(BaseModel):
    model_config = ConfigDict(defer_build=True)
    detail: dict[str, Any]
    header_detail: dict[str, HeaderDetail] = Field(..., alias='headerDetail')
    btf_more_details: dict[str, Any] = Field(..., alias='btfMoreDetails')

class DvMessage(BaseModel):
    model_config = ConfigDict(defer_build=True)
    attrs: dict[str, Any]
    string: str

class FocusMessage(BaseModel):
    model_config = ConfigDict(defer_build=True)
    dv_message: DvMessage = Field(..., alias='dvMessage')
    icon: str
    icon_type: str = Field(..., alias='iconType')

class HighValueMessage(BaseModel):
    model_config = ConfigDict(defer_build=True)
    dv_message: DvMessage = Field(..., alias='dvMessage')
    icon: str

class InformationalMessage(BaseModel):
    model_config = ConfigDict(defer_build=True)
    dv_message: DvMessage = Field(..., alias='dvMessage')

class ProviderLogo(BaseModel):
    model_config = ConfigDict(defer_build=True)
    alt_text: str = Field(..., alias='altText')
    image: str
    link: str

class Messages(BaseModel):
    model_config = ConfigDict(defer_build=True)
    entitlement_type: str = Field(..., alias='entitlementType')
    focus_message: FocusMessage = Field(..., alias='focusMessage')
    high_value_message: HighValueMessage | None = Field(None, alias='highValueMessage')
    informational_messages: list[InformationalMessage] | None = Field(None, alias='informationalMessages')
    provider_logo: ProviderLogo | None = Field(None, alias='providerLogo')

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

class Subscription(BaseModel):
    model_config = ConfigDict(defer_build=True)
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

class Payload1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    payload_type: str = Field(..., alias='payloadType')
    transaction: Transaction | None = None
    subscription: Subscription | None = None

class Presentation(BaseModel):
    model_config = ConfigDict(defer_build=True)
    icon: str | None = None
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

class TransactionDetail(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class Tags(BaseModel):
    model_config = ConfigDict(defer_build=True)
    logo_entity_tag: str = Field(..., alias='LOGO_ENTITY_TAG')
    logo_height: str = Field(..., alias='LOGO_HEIGHT')
    logo_width: str = Field(..., alias='LOGO_WIDTH')

class LogoComponent(BaseModel):
    model_config = ConfigDict(defer_build=True)
    tags: Tags
    url: str

class ComponentPayload1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_component: TextComponent | None = Field(None, alias='textComponent')
    logo_component: LogoComponent | None = Field(None, alias='logoComponent')

class Header(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload1 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class Tags1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_theme: str = Field(..., alias='TEXT_THEME')

class TextComponent2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    tags: Tags1
    text: str
    text_type: str = Field(..., alias='textType')

class ComponentPayload2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_component: TextComponent2 = Field(..., alias='textComponent')

class MotivatorMessaging(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload2 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class Components(BaseModel):
    model_config = ConfigDict(defer_build=True)
    transaction_detail: TransactionDetail = Field(..., alias='TRANSACTION_DETAIL')
    header: Header = Field(..., alias='HEADER')
    motivator_messaging: MotivatorMessaging | None = Field(None, alias='MOTIVATOR_MESSAGING')

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

class Presentation1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    icon: str
    primary_label: str = Field(..., alias='primaryLabel')
    ref_marker: str = Field(..., alias='refMarker')

class Action2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    action_type: str = Field(..., alias='actionType')
    is_selected: bool = Field(..., alias='isSelected')
    payload: Payload2
    presentation: Presentation1

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

class Tags2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    brand_glow: str = Field(..., alias='BRAND_GLOW')
    text_theme: str = Field(..., alias='TEXT_THEME')

class TextComponent3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    tags: Tags2
    text: str
    text_type: str = Field(..., alias='textType')

class ComponentPayload4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_component: TextComponent3 = Field(..., alias='textComponent')

class Banner(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload4 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class IconTextListItem(BaseModel):
    model_config = ConfigDict(defer_build=True)
    icon: str
    tags: dict[str, Any]
    text: str
    text_type: str = Field(..., alias='textType')

class IconTextListComponent(BaseModel):
    model_config = ConfigDict(defer_build=True)
    icon_text_list: list[IconTextListItem] = Field(..., alias='iconTextList')

class ComponentPayload5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    icon_text_list_component: IconTextListComponent = Field(..., alias='iconTextListComponent')

class MotivatorMessaging1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload5 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class Components1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    transaction_detail: TransactionDetail1 = Field(..., alias='TRANSACTION_DETAIL')
    banner: Banner = Field(..., alias='BANNER')
    motivator_messaging: MotivatorMessaging1 | None = Field(None, alias='MOTIVATOR_MESSAGING')

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

class ReactionAction(BaseModel):
    model_config = ConfigDict(defer_build=True)
    csrf_token: str = Field(..., alias='csrfToken')
    reaction: str
    sign_in_url: str = Field(..., alias='signInUrl')

class Playback(BaseModel):
    model_config = ConfigDict(defer_build=True)
    benefit_id: str = Field(..., alias='benefitId')
    correlation_id: str = Field(..., alias='correlationId')
    expiry_time: int = Field(..., alias='expiryTime')
    fallback_url: str = Field(..., alias='fallbackURL')
    is_trailer: bool = Field(..., alias='isTrailer')
    label: str
    playback_envelope: str = Field(..., alias='playbackEnvelope')
    playback_id: str = Field(..., alias='playbackID')
    playback_status: str = Field(..., alias='playbackStatus')
    playback_url: str = Field(..., alias='playbackURL')
    player_ref_marker: str = Field(..., alias='playerRefMarker')
    ref_marker: str = Field(..., alias='refMarker')
    resume_time: int = Field(..., alias='resumeTime')
    run_time: int = Field(..., alias='runTime')
    video_material_type: str = Field(..., alias='videoMaterialType')

class Payload3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    payload_type: str = Field(..., alias='payloadType')
    playback: Playback

class Presentation3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    icon: str
    primary_label: str = Field(..., alias='primaryLabel')
    ref_marker: str = Field(..., alias='refMarker')

class SecondaryAction(BaseModel):
    model_config = ConfigDict(defer_build=True)
    action_type: str = Field(..., alias='actionType')
    is_selected: bool = Field(..., alias='isSelected')
    payload: Payload3
    presentation: Presentation3

class Atf1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    messages: Messages
    primary_actions: list[PrimaryAction] = Field(..., alias='primaryActions')
    reaction_action: ReactionAction = Field(..., alias='reactionAction')
    secondary_actions: list[SecondaryAction] = Field(..., alias='secondaryActions')
    view_ref_marker: str = Field(..., alias='viewRefMarker')

class Action(BaseModel):
    model_config = ConfigDict(defer_build=True)
    btf: dict[str, Any]
    atf: dict[str, Atf1]

class Refund(BaseModel):
    model_config = ConfigDict(defer_build=True)
    fragments: dict[str, Any]
    refunding: None

class Imdb(BaseModel):
    model_config = ConfigDict(defer_build=True)
    max_score: str = Field(..., alias='maxScore')
    score: float
    score_formatted: str = Field(..., alias='scoreFormatted')

class Banner1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    crow: dict[str, Any]
    ui: None

class Notification(BaseModel):
    model_config = ConfigDict(defer_build=True)
    alerts: list[None]
    warnings: list[None]

class Season(BaseModel):
    model_config = ConfigDict(defer_build=True)
    season_id: str = Field(..., alias='seasonId')
    season_link: str = Field(..., alias='seasonLink')
    display_name: str = Field(..., alias='displayName')
    season_selector_icon: str = Field(..., alias='seasonSelectorIcon')
    sequence_number: int = Field(..., alias='sequenceNumber')
    is_selected: bool = Field(..., alias='isSelected')

class Self(BaseModel):
    model_config = ConfigDict(defer_build=True)
    asins: list[str]
    compact_gti: str = Field(..., alias='compactGTI')
    gti: str
    is_launched: bool = Field(..., alias='isLaunched')
    link: str
    sequence_number: int | None = Field(None, alias='sequenceNumber')
    title_type: str = Field(..., alias='titleType')

class Query(BaseModel):
    model_config = ConfigDict(defer_build=True)
    signin: str
    return_url: str = Field(..., alias='returnUrl')
    ref_: str

class Endpoint(BaseModel):
    model_config = ConfigDict(defer_build=True)
    partial_url: str = Field(..., alias='partialURL')
    query: Query

class Text(BaseModel):
    model_config = ConfigDict(defer_build=True)
    attrs: dict[str, Any]
    string: str

class Watchlist(BaseModel):
    model_config = ConfigDict(defer_build=True)
    ajax_enabled: bool = Field(..., alias='ajaxEnabled')
    endpoint: Endpoint
    format_code: str = Field(..., alias='formatCode')
    tag: str
    text: Text

class Restriction(BaseModel):
    model_config = ConfigDict(defer_build=True)
    is_pin_setup_required: bool = Field(..., alias='isPinSetupRequired')
    is_playback_pin_required: bool = Field(..., alias='isPlaybackPinRequired')
    is_purchase_pin_required: bool = Field(..., alias='isPurchasePinRequired')

class Features1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    activate_auto_playing_in_hovers: str = Field(..., alias='activateAutoPlayingInHovers')
    offer_clarity_enabled: str = Field(..., alias='offerClarityEnabled')
    is_reviews_submission_enabled: str = Field(..., alias='isReviewsSubmissionEnabled')
    disable_hover: str = Field(..., alias='disableHover')
    is_autoplay_setting_enabled: str = Field(..., alias='isAutoplaySettingEnabled')
    is_record_season_enabled: str = Field(..., alias='isRecordSeasonEnabled')
    is_detail_page_header_widget_enabled: str = Field(..., alias='isDetailPageHeaderWidgetEnabled')
    disable_player_for_google_bot: str = Field(..., alias='disablePlayerForGoogleBot')
    disable_whisper_cache_in_draper: str = Field(..., alias='disableWhisperCacheInDraper')
    is_detail_page_header_widget_refresh_enabled: str = Field(..., alias='isDetailPageHeaderWidgetRefreshEnabled')
    panorama_treatment: str = Field(..., alias='panoramaTreatment')
    disable_enrich_item_metadata: str = Field(..., alias='disableEnrichItemMetadata')
    disable_marin_tracking: str = Field(..., alias='disableMarinTracking')
    is_stream_selector_modal_enabled: str = Field(..., alias='isStreamSelectorModalEnabled')
    is_swm_enabled: str = Field(..., alias='isSWMEnabled')
    is_spider_noir: str = Field(..., alias='isSpiderNoir')
    disable_explore_tab: str = Field(..., alias='disableExploreTab')

class Btf(BaseModel):
    model_config = ConfigDict(defer_build=True)
    decoration_scheme: str = Field(..., alias='decorationScheme')
    dynamic_features: list[str] = Field(..., alias='dynamicFeatures')
    feature_scheme: str = Field(..., alias='featureScheme')
    widget_scheme: str = Field(..., alias='widgetScheme')

class Atf2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    decoration_scheme: str = Field(..., alias='decorationScheme')
    dynamic_features: list[str] = Field(..., alias='dynamicFeatures')
    feature_scheme: str = Field(..., alias='featureScheme')
    widget_scheme: str = Field(..., alias='widgetScheme')

class SwiftParameters(BaseModel):
    model_config = ConfigDict(defer_build=True)
    btf: Btf = Field(..., alias='BTF')
    atf: Atf2 = Field(..., alias='ATF')

class PageContext(BaseModel):
    model_config = ConfigDict(defer_build=True)
    app: str
    download_launch_type: str = Field(..., alias='downloadLaunchType')
    enable_hover: bool = Field(..., alias='enableHover')
    features: Features1
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
    sub_page_type: str = Field(..., alias='subPageType')
    swift_parameters: SwiftParameters = Field(..., alias='swiftParameters')

class Url(BaseModel):
    model_config = ConfigDict(defer_build=True)
    href: str

class Attrs(BaseModel):
    model_config = ConfigDict(defer_build=True)
    url: Url

class HelpText(BaseModel):
    model_config = ConfigDict(defer_build=True)
    attrs: Attrs
    string: str

class CopyLinkButton(BaseModel):
    model_config = ConfigDict(defer_build=True)
    localized_copy_link: str = Field(..., alias='localizedCopyLink')
    localized_link_copied: str = Field(..., alias='localizedLinkCopied')
    ref_tag: str = Field(..., alias='refTag')
    url: str

class Email(BaseModel):
    model_config = ConfigDict(defer_build=True)
    aria_text: str = Field(..., alias='ariaText')
    localized_text: str = Field(..., alias='localizedText')
    reftag: str
    target: str
    url: str

class Facebook(BaseModel):
    model_config = ConfigDict(defer_build=True)
    aria_text: str = Field(..., alias='ariaText')
    height: int
    localized_text: str = Field(..., alias='localizedText')
    reftag: str
    target: str
    url: str
    width: int

class WhatsApp(BaseModel):
    model_config = ConfigDict(defer_build=True)
    aria_text: str = Field(..., alias='ariaText')
    height: int
    localized_text: str = Field(..., alias='localizedText')
    reftag: str
    target: str
    url: str
    width: int

class XCorp(BaseModel):
    model_config = ConfigDict(defer_build=True)
    aria_text: str = Field(..., alias='ariaText')
    height: int
    localized_text: str = Field(..., alias='localizedText')
    reftag: str
    target: str
    url: str
    width: int

class ShareButtons(BaseModel):
    model_config = ConfigDict(defer_build=True)
    email: Email = Field(..., alias='Email')
    facebook: Facebook = Field(..., alias='Facebook')
    whats_app: WhatsApp = Field(..., alias='WhatsApp')
    x_corp: XCorp = Field(..., alias='XCorp')

class ShareWidgetModel(BaseModel):
    model_config = ConfigDict(defer_build=True)
    copy_link_button: CopyLinkButton = Field(..., alias='copyLinkButton')
    is_creator: bool = Field(..., alias='isCreator')
    localized_share: str = Field(..., alias='localizedShare')
    share_buttons: ShareButtons = Field(..., alias='shareButtons')

class Attrs1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    url: Url

class TermsText(BaseModel):
    model_config = ConfigDict(defer_build=True)
    attrs: Attrs1
    string: str

class Attrs2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    url: Url

class WriteReviewText(BaseModel):
    model_config = ConfigDict(defer_build=True)
    attrs: Attrs2
    string: str

class BottomBar(BaseModel):
    model_config = ConfigDict(defer_build=True)
    feedback_sign_in_url: str = Field(..., alias='feedbackSignInUrl')
    help_text: HelpText = Field(..., alias='helpText')
    share_widget_model: ShareWidgetModel = Field(..., alias='shareWidgetModel')
    terms_text: TermsText = Field(..., alias='termsText')
    write_review_text: WriteReviewText = Field(..., alias='writeReviewText')

class DraperTrackingEvents(BaseModel):
    model_config = ConfigDict(defer_build=True)
    removed_from_watchlist_notification: str = Field(..., alias='removedFromWatchlistNotification')
    resume: str
    default_impression: str = Field(..., alias='defaultImpression')
    add_to_watchlist: str = Field(..., alias='addToWatchlist')
    first_quartile: str = Field(..., alias='firstQuartile')
    pause: str
    accept_invitation: str = Field(..., alias='acceptInvitation')
    skip: str
    mute: str
    expand: str
    playback_blocked: str = Field(..., alias='playbackBlocked')
    unmute: str
    complete: str
    error: str
    third_quartile: str = Field(..., alias='thirdQuartile')
    midpoint: str
    added_to_watchlist_notification: str = Field(..., alias='addedToWatchlistNotification')
    close: str
    rewind: str

class TextMap(BaseModel):
    model_config = ConfigDict(defer_build=True)
    enter_fullscreen: str = Field(..., alias='enterFullscreen')
    exit_fullscreen: str = Field(..., alias='exitFullscreen')
    mute_button: str = Field(..., alias='muteButton')
    unmute_button: str = Field(..., alias='unmuteButton')

class AutoplayTrailerHero(BaseModel):
    model_config = ConfigDict(defer_build=True)
    asset_id: str = Field(..., alias='assetId')
    draper_tracking_events: DraperTrackingEvents = Field(..., alias='draperTrackingEvents')
    is_trailer_autoplay_enabled: bool = Field(..., alias='isTrailerAutoplayEnabled')
    playback_envelope: str = Field(..., alias='playbackEnvelope')
    playback_id: str = Field(..., alias='playbackId')
    ref_marker: str = Field(..., alias='refMarker')
    text_map: TextMap = Field(..., alias='textMap')

class MaturityRating(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field__type: str = Field(..., alias='__type')
    description: str
    display_text: str = Field(..., alias='displayText')
    id: str
    country_code: str | None = Field(None, alias='countryCode')

class Metadata1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    episode_count: str | None = Field(None, alias='episodeCount')
    maturity_rating: MaturityRating = Field(..., alias='maturityRating')
    moods: list[str]

class State(BaseModel):
    model_config = ConfigDict(defer_build=True)
    features: Features
    page_title_id: str = Field(..., alias='pageTitleId')
    detail: Detail
    action: Action
    refund: Refund
    imdb: dict[str, Imdb]
    buy_box: dict[str, Any] = Field(..., alias='buyBox')
    buybox_title_id: dict[str, str] = Field(..., alias='buyboxTitleId')
    creative: dict[str, dict[str, Any]]
    banner: Banner1
    age_verification_banner: dict[str, Any] = Field(..., alias='ageVerificationBanner')
    notification: dict[str, Notification]
    seasons: dict[str, list[Season]]
    self: dict[str, Self]
    watchlist: dict[str, Watchlist]
    restriction: dict[str, Restriction]
    extras: dict[str, Any]
    tokens: dict[str, Any]
    page_link: dict[str, Any] = Field(..., alias='pageLink')
    episode_list: dict[str, Any] = Field(..., alias='episodeList')
    containers: dict[str, Any]
    recordings: dict[str, Any]
    bundles_content: dict[str, Any] = Field(..., alias='bundlesContent')
    other_formats: dict[str, Any] = Field(..., alias='otherFormats')
    page_context: PageContext = Field(..., alias='pageContext')
    bottom_bar: BottomBar = Field(..., alias='bottomBar')
    autoplay_hero: dict[str, Any] = Field(..., alias='autoplayHero')
    autoplay_trailer_hero: dict[str, AutoplayTrailerHero] = Field(..., alias='autoplayTrailerHero')
    playback_integration: dict[str, Any] = Field(..., alias='playbackIntegration')
    coming_soon: dict[str, bool] = Field(..., alias='comingSoon')
    metadata: dict[str, Metadata1]
    widgets: dict[str, dict[str, Any]]
    bottom_menu: dict[str, Any] = Field(..., alias='bottomMenu')
    recording_metadata: dict[str, Any] = Field(..., alias='recordingMetadata')

class Strings(BaseModel):
    model_config = ConfigDict(defer_build=True)
    dv_dp_wp_create_ineligible_swm: str = Field(..., alias='DV_DP_WP_CREATE_INELIGIBLE_SWM')
    dv_web_one_season: str = Field(..., alias='DV_WEB_ONE_SEASON')
    dv_web_dp_eu_cancel_accidental_purchase: str = Field(..., alias='DV_WEB_DP_EU_CANCEL_ACCIDENTAL_PURCHASE')
    dv_dp_wp_unsupported_chat_heading: str = Field(..., alias='DV_DP_WP_UNSUPPORTED_CHAT_HEADING')
    dv_comma_separator: str = Field(..., alias='DV_comma_separator')
    dv_web_sports_record_success_upcoming: str = Field(..., alias='DV_WEB_SPORTS_RECORD_SUCCESS_UPCOMING')
    dv_dp_aria_audio_description: str = Field(..., alias='DV_DP_ARIA_audio_description')
    dv_dp_dv_gcpc_window_title: str = Field(..., alias='DV_DP_DV_GCPC_window_title')
    dv_dp_wp_end: str = Field(..., alias='DV_DP_WP_END')
    dv_web_dp_eu_cancel_purch_modal_submit: str = Field(..., alias='DV_WEB_DP_EU_CANCEL_PURCH_MODAL_SUBMIT')
    dv_dp_select_season: str = Field(..., alias='DV_DP_select_season')
    dv_web_sports_record_success_ended: str = Field(..., alias='DV_WEB_SPORTS_RECORD_SUCCESS_ENDED')
    dv_dp_aria_hdr10_plus: str = Field(..., alias='DV_DP_ARIA_hdr10_plus')
    dv_dp_you_multiple_orders_for_this_title: str = Field(..., alias='DV_DP_you_multiple_orders_for_this_title')
    dv_web_sports_record_league_success_ended: str = Field(..., alias='DV_WEB_SPORTS_RECORD_LEAGUE_SUCCESS_ENDED')
    dv_dp_wl_remove_movie: str = Field(..., alias='DV_DP_WL_removeMovie')
    dv_ab_cancel_accidental_purchase: str = Field(..., alias='DV_AB_CANCEL_ACCIDENTAL_PURCHASE')
    dv_dp_gc_balance_update_failed: str = Field(..., alias='DV_DP_GC_balance_update_failed')
    avod_dp_gc_promotion_message: str = Field(..., alias='AVOD_DP_GC_promotion_message')
    dv_dp_only_playback_available_in_gen4_message: str = Field(..., alias='DV_DP_only_playback_available_in_gen4_message')
    dv_web_linear_program_record_start_success: str = Field(..., alias='DV_WEB_LINEAR_PROGRAM_RECORD_START_SUCCESS')
    assoc_mshop_getlink_close: str = Field(..., alias='assoc-mshop-getlink-close')
    dv_tw_title_genres: str = Field(..., alias='DV_TW_title_genres')
    dv_incompatible_systems_banner_body_update_os: str = Field(..., alias='DV_INCOMPATIBLE_SYSTEMS_BANNER_BODY_UPDATE_OS')
    dv_web_playback_watch_in_app: str = Field(..., alias='DV_WEB_PLAYBACK_WATCH_IN_APP')
    dv_incompatible_systems_banner_body: str = Field(..., alias='DV_INCOMPATIBLE_SYSTEMS_BANNER_BODY')
    dv_web_recording_scheduled: str = Field(..., alias='DV_WEB_RECORDING_SCHEDULED')
    assoc_mshop_getlink_share_copy: str = Field(..., alias='assoc-mshop-getlink-share-copy')
    dv_web_dp_eu_choose_order_to_cancel: str = Field(..., alias='DV_WEB_DP_EU_choose_order_to_cancel')
    dv_dp_none_available: str = Field(..., alias='DV_DP_none_available')
    dv_dp_aria_dolby_atmos: str = Field(..., alias='DV_DP_ARIA_dolby_atmos')
    dv_dp_wp_unsupported_browser_heading: str = Field(..., alias='DV_DP_WP_UNSUPPORTED_BROWSER_HEADING')
    dv_dp_wp_unsupported_chat: str = Field(..., alias='DV_DP_WP_UNSUPPORTED_CHAT')
    dv_web_playback_app_benefits: str = Field(..., alias='DV_WEB_PLAYBACK_APP_BENEFITS')
    dv_dp_wp_error: str = Field(..., alias='DV_DP_WP_ERROR')
    dv_dp_wp_stream_ended: str = Field(..., alias='DV_DP_WP_STREAM_ENDED')
    dv_dp_wl_remove_tv: str = Field(..., alias='DV_DP_WL_removeTv')
    dv_dp_aria_release_year: str = Field(..., alias='DV_DP_ARIA_release_year')
    dv_web_recording_now: str = Field(..., alias='DV_WEB_RECORDING_NOW')
    assoc_mshop_getlink_share_ingress_normal: str = Field(..., alias='assoc-mshop-getlink-share-ingress-normal')
    dv_incompatible_systems_banner_heading_unsupported_browser: str = Field(..., alias='DV_INCOMPATIBLE_SYSTEMS_BANNER_HEADING_UNSUPPORTED_BROWSER')
    dv_dp_wp_join_ineligible_tvod: str = Field(..., alias='DV_DP_WP_JOIN_INELIGIBLE_TVOD')
    dv_dp_wp_join_ineligible_svod_tvod: str = Field(..., alias='DV_DP_WP_JOIN_INELIGIBLE_SVOD_TVOD')
    avod_dp_e_error_ok: str = Field(..., alias='AVOD_DP_E_error_ok')
    dv_dp_tr_dislike_toast: str = Field(..., alias='DV_DP_TR_dislike_toast')
    dv_web_live_not_supported_body: str = Field(..., alias='DV_WEB_LIVE_NOT_SUPPORTED_BODY')
    dv_web_sports_cancel_record_league_success: str = Field(..., alias='DV_WEB_SPORTS_CANCEL_RECORD_LEAGUE_SUCCESS')
    dv_dp_tr_liked_aria: str = Field(..., alias='DV_DP_TR_liked_aria')
    dv_tw_title_producers: str = Field(..., alias='DV_TW_title_producers')
    dv_dp_wp_unsupported_browser: str = Field(..., alias='DV_DP_WP_UNSUPPORTED_BROWSER')
    dv_incompatible_systems_banner_heading_update_os: str = Field(..., alias='DV_INCOMPATIBLE_SYSTEMS_BANNER_HEADING_UPDATE_OS')
    dv_dp_ub_gc_popup_apply: str = Field(..., alias='DV_DP_UB_GC_popup_apply')
    dv_dp_wp_banned_specific_chat: str = Field(..., alias='DV_DP_WP_BANNED_SPECIFIC_CHAT')
    dv_incompatible_systems_banner_heading_update_browser: str = Field(..., alias='DV_INCOMPATIBLE_SYSTEMS_BANNER_HEADING_UPDATE_BROWSER')
    dv_dp_wp_create_ineligible: str = Field(..., alias='DV_DP_WP_CREATE_INELIGIBLE')
    dv_dp_aria_watch_title: str = Field(..., alias='DV_DP_ARIA_watch_title')
    dv_web_playback_watch_in_pv_app: str = Field(..., alias='DV_WEB_PLAYBACK_WATCH_IN_PV_APP')
    dv_dp_wp_join_ineligible: str = Field(..., alias='DV_DP_WP_JOIN_INELIGIBLE')
    dv_dp_aria_dolby_vision: str = Field(..., alias='DV_DP_ARIA_dolby_vision')
    dv_dp_wp_join_ineligible_heading: str = Field(..., alias='DV_DP_WP_JOIN_INELIGIBLE_HEADING')
    dv_tw_title_studio: str = Field(..., alias='DV_TW_title_studio')
    assoc_mshop_getlink_share_trackingid: str = Field(..., alias='assoc-mshop-getlink-share-trackingid')
    dv_cr_review_submission_processing: str = Field(..., alias='DV_CR_review_submission_processing')
    dv_web_linear_program_record_error: str = Field(..., alias='DV_WEB_LINEAR_PROGRAM_RECORD_ERROR')
    dv_dp_aria_dolby_51: str = Field(..., alias='DV_DP_ARIA_dolby_51')
    dv_web_dp_eu_cancel_purch_modal_header: str = Field(..., alias='DV_WEB_DP_EU_CANCEL_PURCH_MODAL_HEADER')
    dv_dp_wp_safari_mac_unsupported_body: str = Field(..., alias='DV_DP_WP_SAFARI_MAC_UNSUPPORTED_BODY')
    dv_dp_gc_widget_heading: str = Field(..., alias='DV_DP_GC_widget_heading')
    dv_dp_tr_err_msg: str = Field(..., alias='DV_DP_TR_err_msg')
    dv_tw_title_languages: str = Field(..., alias='DV_TW_title_languages')
    avod_dp_e_error_text: str = Field(..., alias='AVOD_DP_E_error_text')
    dv_dp_player_timeout_heading: str = Field(..., alias='DV_DP_PLAYER_TIMEOUT_HEADING')
    dv_web_watchlist_label: str = Field(..., alias='DV_WEB_WATCHLIST_LABEL')
    avod_dp_season_selector: str = Field(..., alias='AVOD_DP_season_selector')
    dv_dp_atf_cast: str = Field(..., alias='DV_DP_ATF_CAST')
    dv_rbb_cancel_purch_modal_submit: str = Field(..., alias='DV_RBB_CANCEL_PURCH_MODAL_SUBMIT')
    dv_dp_aria_season_selector: str = Field(..., alias='DV_DP_ARIA_season_selector')
    dv_cr_review_submission_success: str = Field(..., alias='DV_CR_review_submission_success')
    dv_tw_title_content_descriptors: str = Field(..., alias='DV_TW_title_content_descriptors')
    dv_dp_wp_create_ineligible_svod_tvod: str = Field(..., alias='DV_DP_WP_CREATE_INELIGIBLE_SVOD_TVOD')
    dv_mwtw_title_main: str = Field(..., alias='DV_MWTW_TITLE_MAIN')
    dv_tw_title_subtitles: str = Field(..., alias='DV_TW_title_subtitles')
    dv_dp_aria_star_rating: str = Field(..., alias='DV_DP_ARIA_star_rating')
    dv_dot_separator: str = Field(..., alias='DV_dot_separator')
    dv_tw_title_directors: str = Field(..., alias='DV_TW_title_directors')
    dv_dp_unavailable_page_message: str = Field(..., alias='DV_DP_unavailable_page_message')
    dv_dp_player_timeout_body: str = Field(..., alias='DV_DP_PLAYER_TIMEOUT_BODY')
    avod_wl_error_msg: str = Field(..., alias='AVOD_WL_error_msg')
    dv_dp_minutes_remaining: str = Field(..., alias='DV_DP_minutes_remaining')
    dv_mwtw_title: str = Field(..., alias='DV_MWTW_TITLE')
    dv_web_playback_watch_here: str = Field(..., alias='DV_WEB_PLAYBACK_WATCH_HERE')
    dv_rbb_cancel_purch_modal_header: str = Field(..., alias='DV_RBB_CANCEL_PURCH_MODAL_HEADER')
    dv_dp_wp_create_ineligible_tvod: str = Field(..., alias='DV_DP_WP_CREATE_INELIGIBLE_TVOD')
    avod_dp_gc_toc_learn_more: str = Field(..., alias='AVOD_DP_GC_toc_learn_more')
    dv_dp_tr_dislike_btn: str = Field(..., alias='DV_DP_TR_dislike_btn')
    dv_web_sports_cancel_record_success: str = Field(..., alias='DV_WEB_SPORTS_CANCEL_RECORD_SUCCESS')
    dv_dp_gc_balance_type_heading: str = Field(..., alias='DV_DP_GC_balance_type_heading')
    dv_tw_title_cast: str = Field(..., alias='DV_TW_title_cast')
    dv_dp_wl_add_movie: str = Field(..., alias='DV_DP_WL_addMovie')
    dv_incompatible_systems_banner_body_unsupported_browser: str = Field(..., alias='DV_INCOMPATIBLE_SYSTEMS_BANNER_BODY_UNSUPPORTED_BROWSER')
    dv_web_watchlist_csrf_problem: str = Field(..., alias='DV_WEB_WATCHLIST_CSRF_PROBLEM')
    dv_web_settings_head_subtitles: str = Field(..., alias='DV_WEB_SETTINGS_HEAD_SUBTITLES')
    pv_le_ip_watchlist_and_record: str = Field(..., alias='PV_LE_IP_WATCHLIST_AND_RECORD')
    dv_dp_aria_pse_badge: str = Field(..., alias='DV_DP_ARIA_pse_badge')
    dv_web_sports_record: str = Field(..., alias='DV_WEB_SPORTS_RECORD')
    dv_web_seasons_count: str = Field(..., alias='DV_WEB_SEASONS_COUNT')
    dv_dp_aria_imdb_rating: str = Field(..., alias='DV_DP_ARIA_imdb_rating')
    avod_dp_redeem_gift_card_or_promotion: str = Field(..., alias='AVOD_DP_redeem_gift_card_or_promotion')
    dv_dp_atf_more_icon_label: str = Field(..., alias='DV_DP_ATF_MORE_ICON_LABEL')
    dv_dp_wp_create_ineligible_heading: str = Field(..., alias='DV_DP_WP_CREATE_INELIGIBLE_HEADING')
    dv_dp_ub_gc_success_message: str = Field(..., alias='DV_DP_UB_GC_success_message')
    dv_dp_aria_suitable_for: str = Field(..., alias='DV_DP_ARIA_suitable_for')
    dv_dp_wp_geo_restriction_heading: str = Field(..., alias='DV_DP_WP_GEO_RESTRICTION_HEADING')
    dv_incompatible_systems_banner_body_update_browser: str = Field(..., alias='DV_INCOMPATIBLE_SYSTEMS_BANNER_BODY_UPDATE_BROWSER')
    dv_dp_tr_like_btn: str = Field(..., alias='DV_DP_TR_like_btn')
    dv_dp_wp_geo_restriction: str = Field(..., alias='DV_DP_WP_GEO_RESTRICTION')
    dv_tw_title_cast_and_creators: str = Field(..., alias='DV_TW_title_cast_and_creators')
    dv_dp_wp_end_heading: str = Field(..., alias='DV_DP_WP_END_HEADING')
    dv_dp_wp_safari_mac_unsupported_heading: str = Field(..., alias='DV_DP_WP_SAFARI_MAC_UNSUPPORTED_HEADING')
    dv_web_recording_indicator: str = Field(..., alias='DV_WEB_RECORDING_INDICATOR')
    dv_dp_gc_balances_explanation: str = Field(..., alias='DV_DP_GC_balances_explanation')
    assoc_mshop_getlink_share_ineligible_title: str = Field(..., alias='assoc-mshop-getlink-share-ineligible-title')
    dv_dp_gc_wrong_code: str = Field(..., alias='DV_DP_GC_wrong_code')
    dv_dp_choose_order_to_cancel: str = Field(..., alias='DV_DP_choose_order_to_cancel')
    dv_web_linear_program_record_cancel_success: str = Field(..., alias='DV_WEB_LINEAR_PROGRAM_RECORD_CANCEL_SUCCESS')
    dv_dp_wp_banned_specific_chat_heading: str = Field(..., alias='DV_DP_WP_BANNED_SPECIFIC_CHAT_HEADING')
    dv_dp_aria_regulatory_rating: str = Field(..., alias='DV_DP_ARIA_regulatory_rating')
    dv_dp_wp_create_ineligible_svod_tvod_swm: str = Field(..., alias='DV_DP_WP_CREATE_INELIGIBLE_SVOD_TVOD_SWM')
    dv_dp_alt_channel_logo: str = Field(..., alias='DV_DP_ALT_channel_logo')
    dv_dp_ub_gc_enter_code: str = Field(..., alias='DV_DP_UB_GC_enter_code')
    dv_dp_gc_code_input_placeholder: str = Field(..., alias='DV_DP_GC_code_input_placeholder')
    dv_dp_gc_balance_amount_heading: str = Field(..., alias='DV_DP_GC_balance_amount_heading')
    dv_web_sports_record_league_success_upcoming: str = Field(..., alias='DV_WEB_SPORTS_RECORD_LEAGUE_SUCCESS_UPCOMING')
    assoc_mshop_getlink_share_storeid: str = Field(..., alias='assoc-mshop-getlink-share-storeid')
    dv_dp_tr_dislike_aria: str = Field(..., alias='DV_DP_TR_dislike_aria')
    dv_tw_amr_nr_text: str = Field(..., alias='DV_TW_amr_nr_text')
    assoc_mshop_getlink_share_ingress: str = Field(..., alias='assoc-mshop-getlink-share-ingress')
    dv_brand_av: str = Field(..., alias='DV_brand_av')
    dv_dp_aria_runtime: str = Field(..., alias='DV_DP_ARIA_runtime')
    dv_incompatible_systems_banner_heading: str = Field(..., alias='DV_INCOMPATIBLE_SYSTEMS_BANNER_HEADING')
    dv_dp_wp_error_heading: str = Field(..., alias='DV_DP_WP_ERROR_HEADING')
    dv_dp_more_info: str = Field(..., alias='DV_DP_more_info')
    dv_dp_tr_like_toast: str = Field(..., alias='DV_DP_TR_like_toast')
    dv_dp_tr_like_aria: str = Field(..., alias='DV_DP_TR_like_aria')
    dv_dp_unavailable_live_page_message: str = Field(..., alias='DV_DP_unavailable_live_page_message')
    dv_web_sports_cancel_record: str = Field(..., alias='DV_WEB_SPORTS_CANCEL_RECORD')
    dv_dp_tr_disliked_aria: str = Field(..., alias='DV_DP_TR_disliked_aria')
    dv_dp_wl_add_tv: str = Field(..., alias='DV_DP_WL_addTv')

class ResiliencyMetadata(BaseModel):
    model_config = ConfigDict(defer_build=True)
    is_degraded_response: bool = Field(..., alias='isDegradedResponse')
    is_no_content_response: bool = Field(..., alias='isNoContentResponse')
    is_partial_response: bool = Field(..., alias='isPartialResponse')

class Atf(BaseModel):
    model_config = ConfigDict(defer_build=True)
    home_region: str = Field(..., alias='homeRegion')
    state: State
    strings: Strings
    resiliency_metadata: ResiliencyMetadata = Field(..., alias='resiliencyMetadata')

class Features2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    is_elcano: bool = Field(..., alias='isElcano')

class Images1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    packshot: str
    covershot: str

class RatingsHistogram1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    five_star: FiveStar = Field(..., alias='fiveStar')
    four_star: FourStar = Field(..., alias='fourStar')
    one_star: OneStar = Field(..., alias='oneStar')
    three_star: ThreeStar = Field(..., alias='threeStar')
    two_star: TwoStar = Field(..., alias='twoStar')

class ReviewsAnalysisModel1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    ratings_histogram: RatingsHistogram1 = Field(..., alias='ratingsHistogram')
    review_rating_info: ReviewRatingInfo | None = Field(None, alias='reviewRatingInfo')

class Reviews1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    all_reviews_link: str = Field(..., alias='allReviewsLink')
    create_review_link: str = Field(..., alias='createReviewLink')
    locale_language: str = Field(..., alias='localeLanguage')
    review_submission_token: str = Field(..., alias='reviewSubmissionToken')
    reviews_analysis_model: ReviewsAnalysisModel1 = Field(..., alias='reviewsAnalysisModel')
    title_id: str = Field(..., alias='titleID')

class Detail2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str
    synopsis: str
    audio_tracks: list[str] = Field(..., alias='audioTracks')
    duration: int | None = None
    entity_type: str = Field(..., alias='entityType')
    episode_number: int | None = Field(None, alias='episodeNumber')
    is_ad: bool = Field(..., alias='isAd')
    is_closed_caption: bool = Field(..., alias='isClosedCaption')
    is_dolby51: bool = Field(..., alias='isDolby51')
    is_dolby_atmos: bool = Field(..., alias='isDolbyAtmos')
    is_dolby_vision: bool = Field(..., alias='isDolbyVision')
    is_hdr: bool = Field(..., alias='isHdr')
    is_hdr10_plus: bool = Field(..., alias='isHdr10Plus')
    is_prime: bool = Field(..., alias='isPrime')
    is_pse: bool = Field(..., alias='isPse')
    is_uhd: bool = Field(..., alias='isUhd')
    is_x_ray: bool = Field(..., alias='isXRay')
    playback_tracks: list[None] = Field(..., alias='playbackTracks')
    release_date: str = Field(..., alias='releaseDate')
    release_year: int = Field(..., alias='releaseYear')
    runtime: str
    subtitles: list[str]
    title_type: str = Field(..., alias='titleType')
    images: Images1
    amazon_rating: AmazonRating | None = Field(None, alias='amazonRating')
    explore_panel_url: str | None = Field(None, alias='explorePanelURL')
    explore_tab_name: str | None = Field(None, alias='exploreTabName')
    parent_title: str | None = Field(None, alias='parentTitle')
    rating_badge: RatingBadge | None = Field(None, alias='ratingBadge')
    reviews: Reviews1 | None = None
    season_number: int | None = Field(None, alias='seasonNumber')

class Contributors1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    cast: list[CastItem]
    directors: list[Director]
    producers: list[Producer]

class Images2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    covershot: str
    heroshot: str
    packshot: str
    title_logo: str = Field(..., alias='titleLogo')
    titleshot: str

class RatingsHistogram2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    five_star: FiveStar = Field(..., alias='fiveStar')
    four_star: FourStar = Field(..., alias='fourStar')
    one_star: OneStar = Field(..., alias='oneStar')
    three_star: ThreeStar = Field(..., alias='threeStar')
    two_star: TwoStar = Field(..., alias='twoStar')

class ReviewsAnalysisModel2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    ratings_histogram: RatingsHistogram2 = Field(..., alias='ratingsHistogram')
    review_rating_info: ReviewRatingInfo | None = Field(None, alias='reviewRatingInfo')

class Reviews2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    all_reviews_link: str = Field(..., alias='allReviewsLink')
    create_review_link: str = Field(..., alias='createReviewLink')
    locale_language: str = Field(..., alias='localeLanguage')
    review_submission_token: str = Field(..., alias='reviewSubmissionToken')
    reviews_analysis_model: ReviewsAnalysisModel2 = Field(..., alias='reviewsAnalysisModel')
    title_id: str = Field(..., alias='titleID')

class BtfMoreDetails(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str
    synopsis: str
    amazon_rating: AmazonRating | None = Field(None, alias='amazonRating')
    audio_tracks: list[str] = Field(..., alias='audioTracks')
    catalog_id: str = Field(..., alias='catalogId')
    contributors: Contributors1
    enhanced_subtitles: list[EnhancedSubtitle] = Field(..., alias='enhancedSubtitles')
    entity_type: str = Field(..., alias='entityType')
    explore_panel_url: str | None = Field(None, alias='explorePanelURL')
    explore_tab_name: str = Field(..., alias='exploreTabName')
    genres: list[Genre]
    images: Images2
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
    parent_title: str | None = Field(None, alias='parentTitle')
    playback_tracks: list[None] = Field(..., alias='playbackTracks')
    rating_badge: RatingBadge = Field(..., alias='ratingBadge')
    release_date: str = Field(..., alias='releaseDate')
    release_year: int = Field(..., alias='releaseYear')
    reviews: Reviews2
    runtime: str
    season_number: int | None = Field(None, alias='seasonNumber')
    studios: list[str]
    subtitles: list[str]
    title_type: str = Field(..., alias='titleType')
    duration: int | None = None

class Detail1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    detail: dict[str, Detail2]
    header_detail: dict[str, Any] = Field(..., alias='headerDetail')
    btf_more_details: dict[str, BtfMoreDetails] = Field(..., alias='btfMoreDetails')

class FocusMessage1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    dv_message: DvMessage = Field(..., alias='dvMessage')
    icon: str
    icon_type: str = Field(..., alias='iconType')

class Messages1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    entitlement_type: str = Field(..., alias='entitlementType')
    focus_message: FocusMessage1 = Field(..., alias='focusMessage')

class Transaction2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    asin: str
    csrf_token: str = Field(..., alias='csrfToken')
    csrf_token_workflow: str = Field(..., alias='csrfTokenWorkflow')
    display_messages: list[None] = Field(..., alias='displayMessages')
    label: str
    offer_token: str = Field(..., alias='offerToken')
    purchase_data: PurchaseData = Field(..., alias='purchaseData')
    ref_marker: str = Field(..., alias='refMarker')

class Payload5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    payload_type: str = Field(..., alias='payloadType')
    transaction: Transaction2 | None = None
    subscription: Subscription | None = None

class Presentation4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    icon: str | None = None
    primary_label: str = Field(..., alias='primaryLabel')
    ref_marker: str = Field(..., alias='refMarker')

class Action4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    action_type: str = Field(..., alias='actionType')
    is_selected: bool = Field(..., alias='isSelected')
    payload: Payload5
    presentation: Presentation4

class TextComponent4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    tags: dict[str, Any]
    text: str
    text_type: str = Field(..., alias='textType')

class ComponentPayload6(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_component: TextComponent4 = Field(..., alias='textComponent')

class TransactionDetail2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload6 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class Tags3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    logo_entity_tag: str = Field(..., alias='LOGO_ENTITY_TAG')
    logo_height: str = Field(..., alias='LOGO_HEIGHT')
    logo_width: str = Field(..., alias='LOGO_WIDTH')

class LogoComponent1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    tags: Tags3
    url: str

class ComponentPayload7(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_component: TextComponent4 | None = Field(None, alias='textComponent')
    logo_component: LogoComponent1 | None = Field(None, alias='logoComponent')

class Header1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload7 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class Components2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    transaction_detail: TransactionDetail2 = Field(..., alias='TRANSACTION_DETAIL')
    header: Header1 = Field(..., alias='HEADER')

class ExpandingCard1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    actions: list[Action4]
    card_type: str = Field(..., alias='cardType')
    components: Components2

class Transaction3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    asin: str
    csrf_token: str = Field(..., alias='csrfToken')
    csrf_token_workflow: str = Field(..., alias='csrfTokenWorkflow')
    display_messages: list[None] = Field(..., alias='displayMessages')
    label: str
    offer_token: str = Field(..., alias='offerToken')
    purchase_data: PurchaseData = Field(..., alias='purchaseData')
    ref_marker: str = Field(..., alias='refMarker')

class Payload6(BaseModel):
    model_config = ConfigDict(defer_build=True)
    payload_type: str = Field(..., alias='payloadType')
    transaction: Transaction3

class Presentation5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    icon: str
    primary_label: str = Field(..., alias='primaryLabel')
    ref_marker: str = Field(..., alias='refMarker')

class Action5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    action_type: str = Field(..., alias='actionType')
    is_selected: bool = Field(..., alias='isSelected')
    payload: Payload6
    presentation: Presentation5

class TextComponentCollection1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_list: list[TextListItem] = Field(..., alias='textList')

class ComponentPayload8(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_component_collection: TextComponentCollection1 = Field(..., alias='textComponentCollection')

class TransactionDetail3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload8 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class Tags4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    brand_glow: str = Field(..., alias='BRAND_GLOW')
    text_theme: str = Field(..., alias='TEXT_THEME')

class TextComponent6(BaseModel):
    model_config = ConfigDict(defer_build=True)
    tags: Tags4
    text: str
    text_type: str = Field(..., alias='textType')

class ComponentPayload9(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_component: TextComponent6 = Field(..., alias='textComponent')

class Banner2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload9 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class Components3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    transaction_detail: TransactionDetail3 = Field(..., alias='TRANSACTION_DETAIL')
    banner: Banner2 = Field(..., alias='BANNER')

class CardOption1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    actions: list[Action5]
    card_type: str = Field(..., alias='cardType')
    components: Components3

class Payload4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    expanding_card: ExpandingCard1 | None = Field(None, alias='expandingCard')
    payload_type: str = Field(..., alias='payloadType')
    card_options: list[CardOption1] | None = Field(None, alias='cardOptions')

class Presentation6(BaseModel):
    model_config = ConfigDict(defer_build=True)
    primary_label: str = Field(..., alias='primaryLabel')
    ref_marker: str = Field(..., alias='refMarker')

class PrimaryAction1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    action_type: str = Field(..., alias='actionType')
    is_selected: bool = Field(..., alias='isSelected')
    payload: Payload4
    presentation: Presentation6 | None = None

class Btf2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    messages: Messages1
    primary_actions: list[PrimaryAction1] = Field(..., alias='primaryActions')
    secondary_actions: list[None] = Field(..., alias='secondaryActions')
    view_ref_marker: str = Field(..., alias='viewRefMarker')

class Action3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    btf: dict[str, Btf2]
    atf: dict[str, Any]

class Banner3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    crow: dict[str, Any]
    ui: None

class Self1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    asins: list[str]
    compact_gti: str = Field(..., alias='compactGTI')
    gti: str
    is_launched: bool = Field(..., alias='isLaunched')
    link: str
    sequence_number: int = Field(..., alias='sequenceNumber')
    title_type: str = Field(..., alias='titleType')

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

class EpisodeList(BaseModel):
    model_config = ConfigDict(defer_build=True)
    header: str | None = None
    total_card_size: int | None = Field(None, alias='totalCardSize')
    card_title_ids: list[str] | None = Field(None, alias='cardTitleIds')
    actions: Actions | None = None

class CustomerReviewsText(BaseModel):
    model_config = ConfigDict(defer_build=True)
    attrs: dict[str, Any]
    string: str

class CustomerReviews(BaseModel):
    model_config = ConfigDict(defer_build=True)
    count: int
    count_formatted: str = Field(..., alias='countFormatted')
    customer_reviews_text: CustomerReviewsText = Field(..., alias='customerReviewsText')
    link: str
    value: int | float

class FocusMessage2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    icon: str | None = None
    message: str

class GlanceMessage(BaseModel):
    model_config = ConfigDict(defer_build=True)
    icon: str | None = None
    message: str

class HighValueMessage1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    icon: str | None = None
    message: str

class ProviderLogo1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    image_url: str | None = Field(None, alias='imageUrl')
    logo_scalar_horizontal: str | None = Field(None, alias='logoScalarHorizontal')
    message: str | None = None

class TitleMetadataBadge(BaseModel):
    model_config = ConfigDict(defer_build=True)
    entry_type: str | None = Field(None, alias='entryType')
    level: str | None = None
    message: str | None = None

class EntitlementCues(BaseModel):
    model_config = ConfigDict(defer_build=True)
    buybox_message: dict[str, Any] = Field(..., alias='buyboxMessage')
    compact_focus_message: dict[str, Any] = Field(..., alias='compactFocusMessage')
    content_source_logo: dict[str, Any] = Field(..., alias='contentSourceLogo')
    entitlement_type: str | None = Field(None, alias='entitlementType')
    focus_message: FocusMessage2 = Field(..., alias='focusMessage')
    glance_message: GlanceMessage = Field(..., alias='glanceMessage')
    high_value_message: HighValueMessage1 = Field(..., alias='highValueMessage')
    high_value_messages: list[None] = Field(..., alias='highValueMessages')
    informational_message: dict[str, Any] = Field(..., alias='informationalMessage')
    informational_messages: list[None] = Field(..., alias='informationalMessages')
    product_promotion_message: dict[str, Any] = Field(..., alias='productPromotionMessage')
    product_summary_message: dict[str, Any] = Field(..., alias='productSummaryMessage')
    provider_logo: ProviderLogo1 = Field(..., alias='providerLogo')
    title_metadata_badge: TitleMetadataBadge = Field(..., alias='titleMetadataBadge')

class HoverInfo(BaseModel):
    model_config = ConfigDict(defer_build=True)
    can_hover: bool = Field(..., alias='canHover')

class Cover(BaseModel):
    model_config = ConfigDict(defer_build=True)
    url: str

class Hero(BaseModel):
    model_config = ConfigDict(defer_build=True)
    url: str

class Poster2x3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    url: str

class Images3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    cover: Cover | None = None
    hero: Hero | None = None
    poster2x3: Poster2x3 | None = None

class ItemAnalytics(BaseModel):
    model_config = ConfigDict(defer_build=True)
    ref_marker: str = Field(..., alias='refMarker')

class Link(BaseModel):
    model_config = ConfigDict(defer_build=True)
    analytics: dict[str, Any]
    metadata: dict[str, Any]
    url: str

class MaturityRatingBadge(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field__type: str = Field(..., alias='__type')
    description: str
    display_text: str = Field(..., alias='displayText')
    id: str
    country_code: str | None = Field(None, alias='countryCode')

class Endpoint1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    partial_url: str = Field(..., alias='partialURL')
    query: Query

class Action6(BaseModel):
    model_config = ConfigDict(defer_build=True)
    ajax_enabled: bool = Field(..., alias='ajaxEnabled')
    endpoint: Endpoint1
    format_code: str = Field(..., alias='formatCode')
    tag: str
    text: Text

class Item(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field__type: str = Field(..., alias='__type')
    action: Action6
    item_type: str = Field(..., alias='itemType')
    text: str

class OverflowMenu(BaseModel):
    model_config = ConfigDict(defer_build=True)
    items: list[Item]
    title: str

class Endpoint2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    partial_url: str = Field(..., alias='partialURL')
    query: Query

class WatchlistAction(BaseModel):
    model_config = ConfigDict(defer_build=True)
    ajax_enabled: bool = Field(..., alias='ajaxEnabled')
    endpoint: Endpoint2
    format_code: str = Field(..., alias='formatCode')
    tag: str
    text: Text

class CategorizedGenres(BaseModel):
    model_config = ConfigDict(defer_build=True)
    primary_genre: str = Field(..., alias='primaryGenre')
    secondary_genres: list[str] | None = Field(None, alias='secondaryGenres')

class Entity(BaseModel):
    model_config = ConfigDict(defer_build=True)
    buy_box_actions: list[None] = Field(..., alias='buyBoxActions')
    customer_reviews: CustomerReviews | None = Field(None, alias='customerReviews')
    degradations: list[None]
    display_title: str = Field(..., alias='displayTitle')
    entitlement_cues: EntitlementCues = Field(..., alias='entitlementCues')
    entity_type: str = Field(..., alias='entityType')
    hover_info: HoverInfo = Field(..., alias='hoverInfo')
    images: Images3
    impression_id: str = Field(..., alias='impressionId')
    is_closed_caption: bool = Field(..., alias='isClosedCaption')
    item_analytics: ItemAnalytics = Field(..., alias='itemAnalytics')
    link: Link
    maturity_rating_badge: MaturityRatingBadge = Field(..., alias='maturityRatingBadge')
    overflow_menu: OverflowMenu = Field(..., alias='overflowMenu')
    playback_actions: list[None] = Field(..., alias='playbackActions')
    ref_marker: str = Field(..., alias='refMarker')
    release_year: str = Field(..., alias='releaseYear')
    synopsis: str
    title: str
    title_id: str = Field(..., alias='titleID')
    watchlist_action: WatchlistAction = Field(..., alias='watchlistAction')
    widget_type: str = Field(..., alias='widgetType')
    runtime: str | None = None
    categorized_genres: CategorizedGenres | None = Field(None, alias='categorizedGenres')

class EntitlementCues1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    entitled_carousel: str = Field(..., alias='entitledCarousel')
    offer_type: str = Field(..., alias='offerType')

class Container(BaseModel):
    model_config = ConfigDict(defer_build=True)
    container_type: str = Field(..., alias='containerType')
    entities: list[Entity]
    entitlement_cues: EntitlementCues1 = Field(..., alias='entitlementCues')
    estimated_total: int = Field(..., alias='estimatedTotal')
    impression_data: str = Field(..., alias='impressionData')
    inline_container_update_actions: list[None] = Field(..., alias='inlineContainerUpdateActions')
    is_continue_watching: bool = Field(..., alias='isContinueWatching')
    journey_ingress_context: str | None = Field(None, alias='journeyIngressContext')
    pagination_service_token: str | None = Field(None, alias='paginationServiceToken')
    pagination_start_index: int | None = Field(None, alias='paginationStartIndex')
    pagination_target_id: str | None = Field(None, alias='paginationTargetId')
    strings: dict[str, Any]
    text: str
    title: str
    web_uid: str = Field(..., alias='webUid')
    not_expandable: bool | None = Field(None, alias='notExpandable')

class Action7(BaseModel):
    model_config = ConfigDict(defer_build=True)
    format: str
    link: str
    text: Text
    title_id: str = Field(..., alias='titleID')

class OtherFormats(BaseModel):
    model_config = ConfigDict(defer_build=True)
    actions: list[Action7]

class Features3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    activate_auto_playing_in_hovers: str = Field(..., alias='activateAutoPlayingInHovers')
    offer_clarity_enabled: str = Field(..., alias='offerClarityEnabled')
    is_reviews_submission_enabled: str = Field(..., alias='isReviewsSubmissionEnabled')
    disable_hover: str = Field(..., alias='disableHover')
    is_autoplay_setting_enabled: str = Field(..., alias='isAutoplaySettingEnabled')
    is_record_season_enabled: str = Field(..., alias='isRecordSeasonEnabled')
    is_detail_page_header_widget_enabled: str = Field(..., alias='isDetailPageHeaderWidgetEnabled')
    disable_player_for_google_bot: str = Field(..., alias='disablePlayerForGoogleBot')
    disable_whisper_cache_in_draper: str = Field(..., alias='disableWhisperCacheInDraper')
    is_detail_page_header_widget_refresh_enabled: str = Field(..., alias='isDetailPageHeaderWidgetRefreshEnabled')
    panorama_treatment: str = Field(..., alias='panoramaTreatment')
    disable_enrich_item_metadata: str = Field(..., alias='disableEnrichItemMetadata')
    disable_marin_tracking: str = Field(..., alias='disableMarinTracking')
    is_stream_selector_modal_enabled: str = Field(..., alias='isStreamSelectorModalEnabled')
    is_swm_enabled: str = Field(..., alias='isSWMEnabled')
    is_spider_noir: str = Field(..., alias='isSpiderNoir')
    disable_explore_tab: str = Field(..., alias='disableExploreTab')

class Btf3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    decoration_scheme: str = Field(..., alias='decorationScheme')
    dynamic_features: list[str] = Field(..., alias='dynamicFeatures')
    feature_scheme: str = Field(..., alias='featureScheme')
    widget_scheme: str = Field(..., alias='widgetScheme')

class Atf3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    decoration_scheme: str = Field(..., alias='decorationScheme')
    dynamic_features: list[str] = Field(..., alias='dynamicFeatures')
    feature_scheme: str = Field(..., alias='featureScheme')
    widget_scheme: str = Field(..., alias='widgetScheme')

class SwiftParameters1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    btf: Btf3 = Field(..., alias='BTF')
    atf: Atf3 = Field(..., alias='ATF')

class PageContext1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    app: str
    download_launch_type: str = Field(..., alias='downloadLaunchType')
    enable_hover: bool = Field(..., alias='enableHover')
    features: Features3
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
    sub_page_type: str = Field(..., alias='subPageType')
    swift_parameters: SwiftParameters1 = Field(..., alias='swiftParameters')

class Metadata2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    content_descriptors: list[str] | None = Field(None, alias='contentDescriptors')
    content_warnings: list[str] | None = Field(None, alias='contentWarnings')
    maturity_rating: MaturityRating = Field(..., alias='maturityRating')
    traits: list[None] | None = None

class Attrs3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    url: Url

class TermsText1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    attrs: Attrs3
    string: str

class Attrs4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    url: Url

class HelpText1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    attrs: Attrs4
    string: str

class BottomMenu(BaseModel):
    model_config = ConfigDict(defer_build=True)
    feedback_sign_in_url: str = Field(..., alias='feedbackSignInUrl')
    help_text: HelpText1 = Field(..., alias='helpText')

class State1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    features: Features2
    page_title_id: str = Field(..., alias='pageTitleId')
    detail: Detail1
    action: Action3
    refund: Refund
    imdb: dict[str, Any]
    buy_box: dict[str, Any] = Field(..., alias='buyBox')
    buybox_title_id: dict[str, Any] = Field(..., alias='buyboxTitleId')
    creative: dict[str, Any]
    banner: Banner3
    age_verification_banner: dict[str, Any] = Field(..., alias='ageVerificationBanner')
    notification: dict[str, Any]
    seasons: dict[str, Any]
    self: dict[str, Self1]
    watchlist: dict[str, Any]
    restriction: dict[str, Any]
    extras: dict[str, Any]
    tokens: dict[str, Any]
    page_link: dict[str, Any] = Field(..., alias='pageLink')
    episode_list: EpisodeList = Field(..., alias='episodeList')
    containers: dict[str, list[Container]]
    recordings: dict[str, Any]
    bundles_content: dict[str, Any] = Field(..., alias='bundlesContent')
    other_formats: dict[str, OtherFormats] = Field(..., alias='otherFormats')
    page_context: PageContext1 = Field(..., alias='pageContext')
    autoplay_hero: dict[str, Any] = Field(..., alias='autoplayHero')
    autoplay_trailer_hero: dict[str, Any] = Field(..., alias='autoplayTrailerHero')
    playback_integration: dict[str, Any] = Field(..., alias='playbackIntegration')
    coming_soon: dict[str, Any] = Field(..., alias='comingSoon')
    metadata: dict[str, Metadata2]
    widgets: dict[str, dict[str, Any]]
    terms_text: TermsText1 = Field(..., alias='termsText')
    bottom_menu: BottomMenu = Field(..., alias='bottomMenu')
    recording_metadata: dict[str, Any] = Field(..., alias='recordingMetadata')

class Strings1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    dv_cr_review_submission_failure: str = Field(..., alias='DV_CR_review_submission_failure')
    dv_web_one_season: str = Field(..., alias='DV_WEB_ONE_SEASON')
    dv_web_dp_eu_cancel_accidental_purchase: str = Field(..., alias='DV_WEB_DP_EU_CANCEL_ACCIDENTAL_PURCHASE')
    dv_web_aria_previous_title: str = Field(..., alias='DV_WEB_ARIA_PREVIOUS_TITLE')
    dv_web_watchlist_tooltip: str = Field(..., alias='DV_WEB_WATCHLIST_TOOLTIP')
    dv_comma_separator: str = Field(..., alias='DV_comma_separator')
    dv_dp_tab_related: str = Field(..., alias='DV_DP_TAB_related')
    dv_web_sports_record_success_upcoming: str = Field(..., alias='DV_WEB_SPORTS_RECORD_SUCCESS_UPCOMING')
    dv_dp_aria_audio_description: str = Field(..., alias='DV_DP_ARIA_audio_description')
    dv_dp_dv_gcpc_window_title: str = Field(..., alias='DV_DP_DV_GCPC_window_title')
    dv_web_dp_eu_cancel_purch_modal_submit: str = Field(..., alias='DV_WEB_DP_EU_CANCEL_PURCH_MODAL_SUBMIT')
    dv_cr_reviews_explanation_header: str = Field(..., alias='DV_CR_reviews_explanation_header')
    dv_web_sports_record_success_ended: str = Field(..., alias='DV_WEB_SPORTS_RECORD_SUCCESS_ENDED')
    dv_dp_aria_hdr10_plus: str = Field(..., alias='DV_DP_ARIA_hdr10_plus')
    dv_dp_you_multiple_orders_for_this_title: str = Field(..., alias='DV_DP_you_multiple_orders_for_this_title')
    dv_web_sports_record_league_success_ended: str = Field(..., alias='DV_WEB_SPORTS_RECORD_LEAGUE_SUCCESS_ENDED')
    dv_ab_cancel_accidental_purchase: str = Field(..., alias='DV_AB_CANCEL_ACCIDENTAL_PURCHASE')
    dv_web_watchlist_add: str = Field(..., alias='DV_WEB_WATCHLIST_ADD')
    dv_web_feedback_select_option_dropdown_menu: str = Field(..., alias='DV_WEB_FEEDBACK_select_option_dropdown_menu')
    dv_cr_write_review_label_other: str = Field(..., alias='DV_CR_write_review_label_other')
    dv_dp_gc_balance_update_failed: str = Field(..., alias='DV_DP_GC_balance_update_failed')
    avod_dp_gc_promotion_message: str = Field(..., alias='AVOD_DP_GC_promotion_message')
    dv_web_linear_program_record_start_success: str = Field(..., alias='DV_WEB_LINEAR_PROGRAM_RECORD_START_SUCCESS')
    dv_dp_help_support: str = Field(..., alias='DV_DP_Help_Support')
    dv_tw_title_genres: str = Field(..., alias='DV_TW_title_genres')
    dv_web_recording_scheduled: str = Field(..., alias='DV_WEB_RECORDING_SCHEDULED')
    dv_web_dp_eu_choose_order_to_cancel: str = Field(..., alias='DV_WEB_DP_EU_choose_order_to_cancel')
    dv_dp_el_bonus_title_template: str = Field(..., alias='DV_DP_EL_bonus_title_template')
    dv_dp_none_available: str = Field(..., alias='DV_DP_none_available')
    dv_dp_aria_dolby_atmos: str = Field(..., alias='DV_DP_ARIA_dolby_atmos')
    dv_dp_cl_other_formats_title: str = Field(..., alias='DV_DP_CL_other_formats_title')
    dv_dp_aria_release_year: str = Field(..., alias='DV_DP_ARIA_release_year')
    dv_web_recording_now: str = Field(..., alias='DV_WEB_RECORDING_NOW')
    avod_dp_e_error_ok: str = Field(..., alias='AVOD_DP_E_error_ok')
    dv_web_sports_cancel_record_league_success: str = Field(..., alias='DV_WEB_SPORTS_CANCEL_RECORD_LEAGUE_SUCCESS')
    dv_tw_title_producers: str = Field(..., alias='DV_TW_title_producers')
    dv_dp_aria_alt_star_rating: str = Field(..., alias='DV_DP_ARIA_alt_star_rating')
    dv_web_feedback_dropdown_prompt: str = Field(..., alias='DV_WEB_FEEDBACK_dropdown_prompt')
    dv_dp_ub_gc_popup_apply: str = Field(..., alias='DV_DP_UB_GC_popup_apply')
    dv_web_aria_next_n_titles: str = Field(..., alias='DV_WEB_ARIA_NEXT_N_TITLES')
    dv_dp_aria_watch_title: str = Field(..., alias='DV_DP_ARIA_watch_title')
    dv_cr_read_reviews_label: str = Field(..., alias='DV_CR_read_reviews_label')
    dv_dp_aria_dolby_vision: str = Field(..., alias='DV_DP_ARIA_dolby_vision')
    dv_web_more_details: str = Field(..., alias='DV_WEB_MORE_DETAILS')
    dv_tw_title_studio: str = Field(..., alias='DV_TW_title_studio')
    dv_dp_tab_details: str = Field(..., alias='DV_DP_TAB_details')
    dv_web_linear_program_record_error: str = Field(..., alias='DV_WEB_LINEAR_PROGRAM_RECORD_ERROR')
    avod_dp_episode_title: str = Field(..., alias='AVOD_DP_episode_title')
    dv_web_aria_previous_n_titles: str = Field(..., alias='DV_WEB_ARIA_PREVIOUS_N_TITLES')
    dv_dp_aria_dolby_51: str = Field(..., alias='DV_DP_ARIA_dolby_51')
    dv_web_dp_eu_cancel_purch_modal_header: str = Field(..., alias='DV_WEB_DP_EU_CANCEL_PURCH_MODAL_HEADER')
    dv_dp_gc_widget_heading: str = Field(..., alias='DV_DP_GC_widget_heading')
    dv_tw_title_languages: str = Field(..., alias='DV_TW_title_languages')
    avod_dp_e_error_text: str = Field(..., alias='AVOD_DP_E_error_text')
    dv_web_overflow_menu_tooltip: str = Field(..., alias='DV_WEB_OVERFLOW_MENU_TOOLTIP')
    dv_rbb_cancel_purch_modal_submit: str = Field(..., alias='DV_RBB_CANCEL_PURCH_MODAL_SUBMIT')
    dv_tw_title_content_descriptors: str = Field(..., alias='DV_TW_title_content_descriptors')
    dv_web_feedback_submit_button: str = Field(..., alias='DV_WEB_FEEDBACK_submit_button')
    dv_cr_reviews_explanation_text: str = Field(..., alias='DV_CR_reviews_explanation_text')
    dv_mwtw_title_main: str = Field(..., alias='DV_MWTW_TITLE_MAIN')
    dv_tw_title_subtitles: str = Field(..., alias='DV_TW_title_subtitles')
    dv_dp_aria_star_rating: str = Field(..., alias='DV_DP_ARIA_star_rating')
    dv_cr_reviews_header: str = Field(..., alias='DV_CR_reviews_header')
    dv_web_feedback_your_devices: str = Field(..., alias='DV_WEB_FEEDBACK_your_devices')
    dv_dot_separator: str = Field(..., alias='DV_dot_separator')
    dv_tw_title_directors: str = Field(..., alias='DV_TW_title_directors')
    dv_dp_aria_next_tab: str = Field(..., alias='DV_DP_ARIA_next_tab')
    dv_dp_minutes_remaining: str = Field(..., alias='DV_DP_minutes_remaining')
    dv_aw_purchase_options: str = Field(..., alias='DV_AW_PURCHASE_OPTIONS')
    dv_mwtw_title: str = Field(..., alias='DV_MWTW_TITLE')
    dv_rbb_cancel_purch_modal_header: str = Field(..., alias='DV_RBB_CANCEL_PURCH_MODAL_HEADER')
    avod_dp_gc_toc_learn_more: str = Field(..., alias='AVOD_DP_GC_toc_learn_more')
    dv_dp_tab_recordings: str = Field(..., alias='DV_DP_TAB_recordings')
    dv_web_sports_cancel_record_success: str = Field(..., alias='DV_WEB_SPORTS_CANCEL_RECORD_SUCCESS')
    dv_dp_gc_balance_type_heading: str = Field(..., alias='DV_DP_GC_balance_type_heading')
    dv_tw_title_cast: str = Field(..., alias='DV_TW_title_cast')
    dv_cr_write_review_label: str = Field(..., alias='DV_CR_write_review_label')
    dv_web_watchlist_csrf_problem: str = Field(..., alias='DV_WEB_WATCHLIST_CSRF_PROBLEM')
    dv_web_settings_head_subtitles: str = Field(..., alias='DV_WEB_SETTINGS_HEAD_SUBTITLES')
    dv_web_feedback_select_related_device: str = Field(..., alias='DV_WEB_FEEDBACK_select_related_device')
    dv_dp_aria_pse_badge: str = Field(..., alias='DV_DP_ARIA_pse_badge')
    dv_web_details_tooltip: str = Field(..., alias='DV_WEB_DETAILS_TOOLTIP')
    dv_web_sports_record: str = Field(..., alias='DV_WEB_SPORTS_RECORD')
    dv_web_seasons_count: str = Field(..., alias='DV_WEB_SEASONS_COUNT')
    dv_dp_aria_imdb_rating: str = Field(..., alias='DV_DP_ARIA_imdb_rating')
    dv_dp_episode_sort: str = Field(..., alias='DV_DP_EPISODE_SORT')
    avod_dp_redeem_gift_card_or_promotion: str = Field(..., alias='AVOD_DP_redeem_gift_card_or_promotion')
    dv_dp_ub_gc_success_message: str = Field(..., alias='DV_DP_UB_GC_success_message')
    dv_web_watchlist_remove: str = Field(..., alias='DV_WEB_WATCHLIST_REMOVE')
    dv_dp_aria_suitable_for: str = Field(..., alias='DV_DP_ARIA_suitable_for')
    dv_tw_title_cast_and_creators: str = Field(..., alias='DV_TW_title_cast_and_creators')
    dv_web_recording_indicator: str = Field(..., alias='DV_WEB_RECORDING_INDICATOR')
    dv_dp_gc_balances_explanation: str = Field(..., alias='DV_DP_GC_balances_explanation')
    dv_dp_gc_wrong_code: str = Field(..., alias='DV_DP_GC_wrong_code')
    dv_web_feedback_feedback: str = Field(..., alias='DV_WEB_FEEDBACK_feedback')
    dv_dp_choose_order_to_cancel: str = Field(..., alias='DV_DP_choose_order_to_cancel')
    dv_web_linear_program_record_cancel_success: str = Field(..., alias='DV_WEB_LINEAR_PROGRAM_RECORD_CANCEL_SUCCESS')
    dv_dp_aria_regulatory_rating: str = Field(..., alias='DV_DP_ARIA_regulatory_rating')
    dv_dp_ub_gc_enter_code: str = Field(..., alias='DV_DP_UB_GC_enter_code')
    dv_dp_tab_explore: str = Field(..., alias='DV_DP_TAB_explore')
    dv_dp_episode_range_selector: str = Field(..., alias='DV_DP_EPISODE_RANGE_SELECTOR')
    dv_dp_tab_extras: str = Field(..., alias='DV_DP_TAB_extras')
    dv_dp_gc_code_input_placeholder: str = Field(..., alias='DV_DP_GC_code_input_placeholder')
    dv_dp_gc_balance_amount_heading: str = Field(..., alias='DV_DP_GC_balance_amount_heading')
    dv_web_sports_record_league_success_upcoming: str = Field(..., alias='DV_WEB_SPORTS_RECORD_LEAGUE_SUCCESS_UPCOMING')
    dv_web_feedback_no_device_website: str = Field(..., alias='DV_WEB_FEEDBACK_no_device_website')
    dv_dp_el_episode_title: str = Field(..., alias='DV_DP_EL_episode_title')
    dv_tw_amr_nr_text: str = Field(..., alias='DV_TW_amr_nr_text')
    dv_web_feedback__send_us_feedback: str = Field(..., alias='DV_WEB_FEEDBACK__send_us_feedback')
    dv_brand_av: str = Field(..., alias='DV_brand_av')
    dv_dp_tab_episodes: str = Field(..., alias='DV_DP_TAB_episodes')
    dv_dp_aria_runtime: str = Field(..., alias='DV_DP_ARIA_runtime')
    dv_web_aria_next_title: str = Field(..., alias='DV_WEB_ARIA_NEXT_TITLE')
    dv_dp_more_info: str = Field(..., alias='DV_DP_more_info')
    dv_web_sports_cancel_record: str = Field(..., alias='DV_WEB_SPORTS_CANCEL_RECORD')

class Btf1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    home_region: str = Field(..., alias='homeRegion')
    state: State1
    strings: Strings1

class CustomerState(BaseModel):
    model_config = ConfigDict(defer_build=True)
    is_robotic: bool = Field(..., alias='isRobotic')

class FeatureSwitches(BaseModel):
    model_config = ConfigDict(defer_build=True)
    show_floating_join_prime_button: bool = Field(..., alias='showFloatingJoinPrimeButton')

class Metadata3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    availability: Availability

class Image(BaseModel):
    model_config = ConfigDict(defer_build=True)
    alt_text: str = Field(..., alias='altText')
    url: str

class Branding(BaseModel):
    model_config = ConfigDict(defer_build=True)
    image: Image
    label: str
    ref_marker: str = Field(..., alias='refMarker')
    url: str

class NavSection(BaseModel):
    model_config = ConfigDict(defer_build=True)
    desktop: str
    mobile: str

class SubNode(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field__type: str = Field(..., alias='__type')
    id: str
    label: str
    ref_marker: str = Field(..., alias='refMarker')
    url: str

class SubMenuItem(BaseModel):
    model_config = ConfigDict(defer_build=True)
    id: str
    sub_nodes: list[SubNode] = Field(..., alias='subNodes')
    label: str | None = None

class NavigationNode(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field__type: str = Field(..., alias='__type')
    id: str
    label: str
    nav_section: NavSection = Field(..., alias='navSection')
    ref_marker: str = Field(..., alias='refMarker')
    sub_menu: list[SubMenuItem] = Field(..., alias='subMenu')
    url: str
    coachmark_text: str | None = Field(None, alias='coachmarkText')
    enrich_nav: str | None = Field(None, alias='enrichNav')
    icon: str | None = None

class Query3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    ie: str
    ref_: str

class SubmitSearchDestructuredEndpoint(BaseModel):
    model_config = ConfigDict(defer_build=True)
    partial_url: str = Field(..., alias='partialURL')
    query: Query3

class SearchBar(BaseModel):
    model_config = ConfigDict(defer_build=True)
    clear_search_label: str = Field(..., alias='clearSearchLabel')
    close_search_alt_text: str = Field(..., alias='closeSearchAltText')
    is_search_suggestions_disabled: bool = Field(..., alias='isSearchSuggestionsDisabled')
    is_search_suggestions_enhanced: bool = Field(..., alias='isSearchSuggestionsEnhanced')
    search_bar_placeholder_label: str = Field(..., alias='searchBarPlaceholderLabel')
    search_icon_alt_text: str = Field(..., alias='searchIconAltText')
    submit_search_destructured_endpoint: SubmitSearchDestructuredEndpoint = Field(..., alias='submitSearchDestructuredEndpoint')
    submit_search_endpoint: str = Field(..., alias='submitSearchEndpoint')

class Nav(BaseModel):
    model_config = ConfigDict(defer_build=True)
    aria_label: str = Field(..., alias='ariaLabel')
    branding: Branding
    collapsed_nav_browse_label: str = Field(..., alias='collapsedNavBrowseLabel')
    label: str
    navigation_nodes: list[NavigationNode] = Field(..., alias='navigationNodes')
    search_bar: SearchBar = Field(..., alias='searchBar')

class SitewideNavigationBar1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    customer_state: CustomerState = Field(..., alias='customerState')
    feature_switches: FeatureSwitches = Field(..., alias='featureSwitches')
    is_sticky: bool = Field(..., alias='isSticky')
    metadata: Metadata3
    nav: Nav
    hz_page_type: str = Field(..., alias='hzPageType')
    hz_sub_page_type: str = Field(..., alias='hzSubPageType')
    is_roadblocked: bool = Field(..., alias='isRoadblocked')

class SitewideInlineScriptsTop1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    hide_footer_gap: bool = Field(..., alias='hideFooterGap')

class SitewideInlineScriptsBottom1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    hide_footer_gap: bool = Field(..., alias='hideFooterGap')

class Metadata4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    availability: Availability

class SitewideConditional(BaseModel):
    model_config = ConfigDict(defer_build=True)
    degradations: list[None]
    features: dict[str, Any]
    metadata: Metadata4
    page_type: str = Field(..., alias='pageType')
    sub_page_type: str = Field(..., alias='subPageType')
    privacy_prefs_csrf_token: str = Field(..., alias='privacyPrefsCsrfToken')

class SitewideAlexa(BaseModel):
    model_config = ConfigDict(defer_build=True)
    device_config_id: str = Field(..., alias='deviceConfigId')
    iframe_origin: str = Field(..., alias='iframeOrigin')

class Sitewide(BaseModel):
    model_config = ConfigDict(defer_build=True)
    sitewide_navigation_bar: SitewideNavigationBar1 = Field(..., alias='sitewide-navigation-bar')
    sitewide_inline_scripts_top: SitewideInlineScriptsTop1 = Field(..., alias='sitewide-inline-scripts-top')
    sitewide_inline_scripts_bottom: SitewideInlineScriptsBottom1 = Field(..., alias='sitewide-inline-scripts-bottom')
    sitewide_conditional: SitewideConditional = Field(..., alias='sitewide-conditional')
    sitewide_alexa: SitewideAlexa = Field(..., alias='sitewide-alexa')

class Body(BaseModel):
    model_config = ConfigDict(defer_build=True)
    routing_type: str = Field(..., alias='routingType')
    page_classes: list[str] = Field(..., alias='pageClasses')
    pangaea_banner: PangaeaBanner = Field(..., alias='pangaeaBanner')
    atf: Atf
    btf: Btf1
    sitewide: Sitewide

class QueryParameters(BaseModel):
    model_config = ConfigDict(defer_build=True)
    dv_web_app_client_version: list[str] = Field(..., alias='dvWebAppClientVersion')

class Contingencies(BaseModel):
    model_config = ConfigDict(defer_build=True)
    is_testing: bool = Field(..., alias='isTesting')
    values: dict[str, Any]

class RequestContext(BaseModel):
    model_config = ConfigDict(defer_build=True)
    customer_id: None = Field(..., alias='customerID')
    user_agent: str = Field(..., alias='userAgent')
    is_internal: bool = Field(..., alias='isInternal')
    path: str
    query_parameters: QueryParameters = Field(..., alias='queryParameters')
    request_id: str = Field(..., alias='requestID')
    session_id: str = Field(..., alias='sessionID')
    traffic_policies: str = Field(..., alias='trafficPolicies')
    domain: str
    marketplace_id: str = Field(..., alias='marketplaceID')
    customer_ip_address: IPv4Address = Field(..., alias='customerIPAddress')
    original_uri: str = Field(..., alias='originalURI')
    os_locale: str = Field(..., alias='osLocale')
    record_territory: str = Field(..., alias='recordTerritory')
    current_territory: str = Field(..., alias='currentTerritory')
    geo_token: str = Field(..., alias='geoToken')
    cookie_timezone: None = Field(..., alias='cookieTimezone')
    app_name: None = Field(..., alias='appName')
    device_id: None = Field(..., alias='deviceID')
    contingencies: Contingencies
    is_test: bool = Field(..., alias='isTest')
    mocks: None
    service_overrides: None = Field(..., alias='serviceOverrides')
    weblab_overrides: dict[str, Any] = Field(..., alias='weblabOverrides')
    server_name: str = Field(..., alias='serverName')
    resiliency_token: None = Field(..., alias='resiliencyToken')
    is_locale_rtl: bool = Field(..., alias='isLocaleRTL')
    identity_context: str = Field(..., alias='identityContext')
    locale: str

class Weblab(BaseModel):
    model_config = ConfigDict(defer_build=True)
    weblab_name: str = Field(..., alias='weblabName')
    treatment_name: str = Field(..., alias='treatmentName')

class ClickstreamData(BaseModel):
    model_config = ConfigDict(defer_build=True)
    page_type: str = Field(..., alias='pageType')
    sub_page_type: str = Field(..., alias='subPageType')
    request_id: str = Field(..., alias='requestId')
    page_type_id: str = Field(..., alias='pageTypeId')
    ref_marker: None = Field(..., alias='refMarker')
    action: None
    hit_type: None = Field(..., alias='hitType')
    a9_search_fields: None = Field(..., alias='A9SearchFields')
    additional_data: None = Field(..., alias='additionalData')
    weblabs: list[Weblab] = Field(..., alias='Weblabs')
    site_variant: str = Field(..., alias='siteVariant')

class Profile(BaseModel):
    model_config = ConfigDict(defer_build=True)
    age_group: str = Field(..., alias='ageGroup')
    is_child: bool = Field(..., alias='isChild')

class FeaturePivots(BaseModel):
    model_config = ConfigDict(defer_build=True)
    dv_web_feedback_widget_scheme_1382103: bool = Field(..., alias='DV_WEB_FEEDBACK_WIDGET_SCHEME_1382103')
    dv_web_linear_age_restriction_sign_in_explore_scheme_1445266: bool = Field(..., alias='DV_WEB_LINEAR_AGE_RESTRICTION_SIGN_IN_EXPLORE_SCHEME_1445266')
    is_agent_self_declaration_enabled: bool = Field(..., alias='isAgentSelfDeclarationEnabled')
    dv_web_scores_and_gameclock_1279604: bool = Field(..., alias='DV_WEB_SCORES_AND_GAMECLOCK_1279604')
    dv_web_dp_enable_drm_support_for_desktop_1437352: bool = Field(..., alias='DV_WEB_DP_ENABLE_DRM_SUPPORT_FOR_DESKTOP_1437352')
    dv_web_linear_vmvpd_explore_scheme_1407946: bool = Field(..., alias='DV_WEB_LINEAR_VMVPD_EXPLORE_SCHEME_1407946')
    dv_web_linear_search_1434133: bool = Field(..., alias='DV_WEB_LINEAR_SEARCH_1434133')
    is_crw_redesign_enabled: bool = Field(..., alias='isCrwRedesignEnabled')
    is_telemetry_sdk_migration_weblab_on: bool = Field(..., alias='isTelemetrySDKMigrationWeblabOn')
    is_deprecate_dcs_telemetry_weblab_on: bool = Field(..., alias='isDeprecateDCSTelemetryWeblabOn')
    dv_windows_app_pwa_back_to_legacy_1316821: bool = Field(..., alias='DV_WINDOWS_APP_PWA_BACK_TO_LEGACY_1316821')
    pv_web_sterling_sponsored_label_1438224: bool = Field(..., alias='PV_WEB_STERLING_SPONSORED_LABEL_1438224')
    dv_web_linear_station_taps_view_upgrade_1358041: bool = Field(..., alias='DV_WEB_LINEAR_STATION_TAPS_VIEW_UPGRADE_1358041')
    dv_web_tr_persist_1434722: bool = Field(..., alias='DV_WEB_TR_PERSIST_1434722')
    handshake_token: str = Field(..., alias='handshakeToken')
    dv_web_xiaomi_deeplink_with_https_1303012: bool = Field(..., alias='DV_WEB_XIAOMI_DEEPLINK_WITH_HTTPS_1303012')
    pause_refreshes_during_playback: bool = Field(..., alias='pauseRefreshesDuringPlayback')
    dv_web_linear_station_favoriting_1356611: bool = Field(..., alias='DV_WEB_LINEAR_STATION_FAVORITING_1356611')
    is_profile_age_restricted_enabled: bool = Field(..., alias='isProfileAgeRestrictedEnabled')
    is_page_load_clickstream_exp_weblab_on: bool = Field(..., alias='isPageLoadClickstreamExpWeblabOn')
    dv_web_service_worker_1293503: bool = Field(..., alias='DV_WEB_SERVICE_WORKER_1293503')
    pause_downloads_during_playback: bool = Field(..., alias='pauseDownloadsDuringPlayback')
    dv_web_dp_panorama_immersive_cx_autoplay_1222621: bool = Field(..., alias='DV_WEB_DP_PANORAMA_IMMERSIVE_CX_AUTOPLAY_1222621')
    super_draper_safari_minimum_bitrate: None = Field(..., alias='superDraperSafariMinimumBitrate')
    is_seamless_expansion_enabled: bool = Field(..., alias='isSeamlessExpansionEnabled')
    dv_web_enable_pvcom_for_cmp_customers_signed_in_1405793: bool = Field(..., alias='DV_WEB_ENABLE_PVCOM_FOR_CMP_CUSTOMERS_SIGNED_IN_1405793')
    dv_web_ref_marker_as_query_param_1380642: bool = Field(..., alias='DV_WEB_REF_MARKER_AS_QUERY_PARAM_1380642')
    dv_web_fox_followup_1298275: bool = Field(..., alias='DV_WEB_FOX_FOLLOWUP_1298275')
    is_profile_level_parental_controls_enabled: bool = Field(..., alias='isProfileLevelParentalControlsEnabled')
    is_exposed_to_immersive_cx_experiment: bool = Field(..., alias='isExposedToImmersiveCXExperiment')
    dv_web_live_events_music_kahuna_1400248: str = Field(..., alias='DV_WEB_LIVE_EVENTS_MUSIC_KAHUNA_1400248')
    dv_web_dp_enable_whisper_cache_for_unrec_customers_1440503: bool = Field(..., alias='DV_WEB_DP_ENABLE_WHISPER_CACHE_FOR_UNREC_CUSTOMERS_1440503')
    telemetry_client_launch_web_treatment: str = Field(..., alias='telemetryClientLaunchWebTreatment')
    is_runway_post_transition_enabled: bool = Field(..., alias='isRunwayPostTransitionEnabled')
    dv_web_live_events_music_kahuna_test_1411910: bool = Field(..., alias='DV_WEB_LIVE_EVENTS_MUSIC_KAHUNA_TEST_1411910')
    is_less_aggressive_play_button_spinner: bool = Field(..., alias='isLessAggressivePlayButtonSpinner')
    dv_web_enable_pvcom_for_cmp_customers_1365035: bool = Field(..., alias='DV_WEB_ENABLE_PVCOM_FOR_CMP_CUSTOMERS_1365035')
    is_runway_transition_initiation_enabled: bool = Field(..., alias='isRunwayTransitionInitiationEnabled')
    pv_web_common_sense_media_kids_profile_1422829: bool = Field(..., alias='PV_WEB_COMMON_SENSE_MEDIA_KIDS_PROFILE_1422829')
    dv_web_dp_enable_drm_support_1433238: bool = Field(..., alias='DV_WEB_DP_ENABLE_DRM_SUPPORT_1433238')
    pv_linear_carousel_bearded_web_1433664: bool = Field(..., alias='PV_LINEAR_CAROUSEL_BEARDED_WEB_1433664')
    dv_web_live_autoplay_1290319: str = Field(..., alias='DV_WEB_LIVE_AUTOPLAY_1290319')
    dv_web_enable_linear_station_in_all_carousels_1272039: bool = Field(..., alias='DV_WEB_ENABLE_LINEAR_STATION_IN_ALL_CAROUSELS_1272039')
    dv_web_minidetails_expandable_synopsis_1336752: bool = Field(..., alias='DV_WEB_MINIDETAILS_EXPANDABLE_SYNOPSIS_1336752')
    is_page_resiliency_launched: bool = Field(..., alias='isPageResiliencyLaunched')
    is_pvcom_enabled_for_signed_in_cmp_customer: bool = Field(..., alias='isPVCOMEnabledForSignedInCMPCustomer')
    dv_web_linear_vmvpd_recording_card_1405557: bool = Field(..., alias='DV_WEB_LINEAR_VMVPD_RECORDING_CARD_1405557')
    dv_web_title_rating_experiment_1374850: str = Field(..., alias='DV_WEB_TITLE_RATING_EXPERIMENT_1374850')
    pv_web_lighthouse_1438707: bool = Field(..., alias='PV_WEB_LIGHTHOUSE_1438707')

class Resiliency(BaseModel):
    model_config = ConfigDict(defer_build=True)
    resiliency_version: str = Field(..., alias='resiliencyVersion')

class GlobalStore(BaseModel):
    model_config = ConfigDict(defer_build=True)
    request_context: RequestContext = Field(..., alias='RequestContext')
    clickstream_data: ClickstreamData = Field(..., alias='ClickstreamData')
    site_variant: str = Field(..., alias='SiteVariant')
    profile: Profile = Field(..., alias='Profile')
    home_region: str = Field(..., alias='HomeRegion')
    feature_pivots: FeaturePivots = Field(..., alias='FeaturePivots')
    resiliency: Resiliency = Field(..., alias='Resiliency')
    cross_domain_sso_url: None = Field(..., alias='CrossDomainSSOUrl')

class Config(BaseModel):
    model_config = ConfigDict(defer_build=True)
    delay_loading_indicator: bool = Field(..., alias='delayLoadingIndicator')
    csn_deny_list: list[str] = Field(..., alias='csnDenyList')
    disable_downloads_sync: bool = Field(..., alias='disableDownloadsSync')
    client_ttl_mins: int = Field(..., alias='clientTTLMins')
    force_fake_navigation_api: bool = Field(..., alias='forceFakeNavigationAPI')

class DetailModel(BaseModel):
    model_config = ConfigDict(defer_build=True)
    head: Head
    body: Body
    global_store: GlobalStore = Field(..., alias='globalStore')
    config: Config
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
