from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from ipaddress import IPv4Address
from typing import Any
from pydantic import BaseModel, ConfigDict, Field

class MetaTag(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    name: str | None = None
    content: str | None = None

class LinkTag(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    rel: str | None = None
    href: str | None = None

class SeoMetadata(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    canonical_url: str | None = Field(None, alias='canonicalUrl')
    script_tags: list[Any] | None = Field(None, alias='scriptTags')
    meta_tags: list[MetaTag] | None = Field(None, alias='metaTags')
    meta_tags_rd_fa: list[Any] | None = Field(None, alias='metaTagsRDFa')
    title: str | None = None
    link_tags: list[LinkTag] | None = Field(None, alias='linkTags')

class PageMetadata(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    page_type: str | None = Field(None, alias='pageType')
    sub_page_type: str | None = Field(None, alias='subPageType')
    page_type_id: str | None = Field(None, alias='pageTypeId')

class Meta(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    name: str | None = None
    content: str | None = None

class SitewideNavigationBar(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | None = None
    meta: Meta | None = None

class SitewideInlineScriptsTop(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    include_common_meta: bool | None = Field(None, alias='includeCommonMeta')
    logging_endpoint: str | None = Field(None, alias='loggingEndpoint')
    disable_legacy_csm_postbacks: bool | None = Field(None, alias='disableLegacyCsmPostbacks')
    scope_search: bool | None = Field(None, alias='scopeSearch')
    include_arabic_font: bool | None = Field(None, alias='includeArabicFont')
    include_site_verification: bool | None = Field(None, alias='includeSiteVerification')
    include_min_body_width: bool | None = Field(None, alias='includeMinBodyWidth')
    include_pwa_manifest: bool | None = Field(None, alias='includePWAManifest')
    include_smart_app_banner: bool | None = Field(None, alias='includeSmartAppBanner')
    page_type: str | None = Field(None, alias='pageType')
    sub_page_type: str | None = Field(None, alias='subPageType')
    page_type_id: str | None = Field(None, alias='pageTypeId')

class SitewideInlineScriptsBottom(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    include_common_meta: bool | None = Field(None, alias='includeCommonMeta')
    logging_endpoint: str | None = Field(None, alias='loggingEndpoint')
    disable_legacy_csm_postbacks: bool | None = Field(None, alias='disableLegacyCsmPostbacks')
    scope_search: bool | None = Field(None, alias='scopeSearch')
    include_arabic_font: bool | None = Field(None, alias='includeArabicFont')
    include_site_verification: bool | None = Field(None, alias='includeSiteVerification')
    include_min_body_width: bool | None = Field(None, alias='includeMinBodyWidth')
    include_pwa_manifest: bool | None = Field(None, alias='includePWAManifest')
    include_smart_app_banner: bool | None = Field(None, alias='includeSmartAppBanner')
    page_type: str | None = Field(None, alias='pageType')
    sub_page_type: str | None = Field(None, alias='subPageType')
    page_type_id: str | None = Field(None, alias='pageTypeId')

class SitewideHead(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    sitewide_navigation_bar: SitewideNavigationBar | None = Field(None, alias='sitewide-navigation-bar')
    sitewide_footer: dict[str, Any] | None = Field(None, alias='sitewide-footer')
    sitewide_inline_scripts_top: SitewideInlineScriptsTop | None = Field(None, alias='sitewide-inline-scripts-top')
    sitewide_inline_scripts_bottom: SitewideInlineScriptsBottom | None = Field(None, alias='sitewide-inline-scripts-bottom')
    sitewide_conditional: dict[str, Any] | None = Field(None, alias='sitewide-conditional')
    sitewide_payment_state_message: dict[str, Any] | None = Field(None, alias='sitewide-payment-state-message')
    sitewide_cross_benefit_modal: dict[str, Any] | None = Field(None, alias='sitewide-cross-benefit-modal')
    sitewide_deprecated_browsers_banner: dict[str, Any] | None = Field(None, alias='sitewide-deprecated-browsers-banner')
    sitewide_language_notification: dict[str, Any] | None = Field(None, alias='sitewide-language-notification')
    sitewide_inspector: dict[str, Any] | None = Field(None, alias='sitewide-inspector')
    sitewide_alexa: dict[str, Any] | None = Field(None, alias='sitewide-alexa')

class Head(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    seo_metadata: SeoMetadata | None = Field(None, alias='seoMetadata')
    page_metadata: PageMetadata | None = Field(None, alias='pageMetadata')
    sitewide_head: SitewideHead | None = Field(None, alias='sitewideHead')
    title: str | None = None

class Availability(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    description: str | None = None
    severity: str | None = None

class Metadata(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability: Availability | None = None

class PangaeaBanner(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    csrf_token: str | None = Field(None, alias='csrfToken')
    metadata: Metadata | None = None

class Features(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_elcano: bool | None = Field(None, alias='isElcano')
    enable_marin_tracking: bool | None = Field(None, alias='enableMarinTracking')

class AmazonRating(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    count: int | None = None
    count_formatted: str | None = Field(None, alias='countFormatted')
    value: float | None = None

class CastItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    name: str | None = None
    search_link: str | None = Field(None, alias='searchLink')

class Director(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    name: str | None = None
    search_link: str | None = Field(None, alias='searchLink')

class Producer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    name: str | None = None
    search_link: str | None = Field(None, alias='searchLink')

class Contributors(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    cast: list[CastItem] | None = None
    directors: list[Director] | None = None
    producers: list[Producer] | None = None

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
    provider_logo: str | None = Field(None, alias='providerLogo')

class RatingBadge(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__type: str | None = Field(None, alias='__type')
    description: str | None = None
    display_text: str | None = Field(None, alias='displayText')
    id: str | None = None
    country_code: str | None = Field(None, alias='countryCode')

class FiveStar(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    hover_text: str | None = Field(None, alias='hoverText')
    percentage: int | None = None
    percentage_display: str | None = Field(None, alias='percentageDisplay')
    rating_display_label: str | None = Field(None, alias='ratingDisplayLabel')
    url: str | None = None

class FourStar(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    hover_text: str | None = Field(None, alias='hoverText')
    percentage: int | None = None
    percentage_display: str | None = Field(None, alias='percentageDisplay')
    rating_display_label: str | None = Field(None, alias='ratingDisplayLabel')
    url: str | None = None

class OneStar(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    hover_text: str | None = Field(None, alias='hoverText')
    percentage: int | None = None
    percentage_display: str | None = Field(None, alias='percentageDisplay')
    rating_display_label: str | None = Field(None, alias='ratingDisplayLabel')
    url: str | None = None

class ThreeStar(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    hover_text: str | None = Field(None, alias='hoverText')
    percentage: int | None = None
    percentage_display: str | None = Field(None, alias='percentageDisplay')
    rating_display_label: str | None = Field(None, alias='ratingDisplayLabel')
    url: str | None = None

class TwoStar(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    hover_text: str | None = Field(None, alias='hoverText')
    percentage: int | None = None
    percentage_display: str | None = Field(None, alias='percentageDisplay')
    rating_display_label: str | None = Field(None, alias='ratingDisplayLabel')
    url: str | None = None

class RatingsHistogram(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    five_star: FiveStar | None = Field(None, alias='fiveStar')
    four_star: FourStar | None = Field(None, alias='fourStar')
    one_star: OneStar | None = Field(None, alias='oneStar')
    three_star: ThreeStar | None = Field(None, alias='threeStar')
    two_star: TwoStar | None = Field(None, alias='twoStar')

class ReviewRatingInfo(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    average_rating_label: str | None = Field(None, alias='averageRatingLabel')
    has_half_star: bool | None = Field(None, alias='hasHalfStar')
    star_count: int | None = Field(None, alias='starCount')
    total_review_count: int | None = Field(None, alias='totalReviewCount')
    total_review_count_text: str | None = Field(None, alias='totalReviewCountText')

class ReviewsAnalysisModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    ratings_histogram: RatingsHistogram | None = Field(None, alias='ratingsHistogram')
    review_rating_info: ReviewRatingInfo | None = Field(None, alias='reviewRatingInfo')

class Reviews(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    all_reviews_link: str | None = Field(None, alias='allReviewsLink')
    create_review_link: str | None = Field(None, alias='createReviewLink')
    locale_language: str | None = Field(None, alias='localeLanguage')
    review_submission_token: str | None = Field(None, alias='reviewSubmissionToken')
    reviews_analysis_model: ReviewsAnalysisModel | None = Field(None, alias='reviewsAnalysisModel')
    title_id: str | None = Field(None, alias='titleID')

class HeaderDetail(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | None = None
    synopsis: str | None = None
    amazon_rating: AmazonRating | None = Field(None, alias='amazonRating')
    audio_tracks: list[str] | None = Field(None, alias='audioTracks')
    catalog_id: str | None = Field(None, alias='catalogId')
    contributors: Contributors | None = None
    enhanced_subtitles: list[EnhancedSubtitle] | None = Field(None, alias='enhancedSubtitles')
    entity_type: str | None = Field(None, alias='entityType')
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
    parent_title: str | None = Field(None, alias='parentTitle')
    playback_tracks: list[Any] | None = Field(None, alias='playbackTracks')
    rating_badge: RatingBadge | None = Field(None, alias='ratingBadge')
    release_date: str | None = Field(None, alias='releaseDate')
    release_year: int | None = Field(None, alias='releaseYear')
    reviews: Reviews | None = None
    runtime: str | None = None
    season_number: int | None = Field(None, alias='seasonNumber')
    studios: list[str] | None = None
    subtitles: list[str] | None = None
    title_type: str | None = Field(None, alias='titleType')
    duration: int | None = None

class Detail(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    detail: dict[str, Any] | None = None
    header_detail: dict[str, HeaderDetail] | None = Field(None, alias='headerDetail')
    btf_more_details: dict[str, Any] | None = Field(None, alias='btfMoreDetails')

class DvMessage(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    attrs: dict[str, Any] | None = None
    string: str | None = None

class FocusMessage(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    dv_message: DvMessage | None = Field(None, alias='dvMessage')
    icon: str | None = None
    icon_type: str | None = Field(None, alias='iconType')

class HighValueMessage(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    dv_message: DvMessage | None = Field(None, alias='dvMessage')
    icon: str | None = None
    icon_type: str | None = Field(None, alias='iconType')

class InformationalMessage(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    dv_message: DvMessage | None = Field(None, alias='dvMessage')

class ProviderLogo(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    alt_text: str | None = Field(None, alias='altText')
    image: str | None = None
    link: str | None = None

class TitleMetadataBadge(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    dv_message: DvMessage | None = Field(None, alias='dvMessage')
    entry_type: str | None = Field(None, alias='entryType')
    level: str | None = None

class Messages(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    entitlement_type: str | None = Field(None, alias='entitlementType')
    focus_message: FocusMessage | None = Field(None, alias='focusMessage')
    high_value_message: HighValueMessage | None = Field(None, alias='highValueMessage')
    informational_messages: list[InformationalMessage] | None = Field(None, alias='informationalMessages')
    provider_logo: ProviderLogo | None = Field(None, alias='providerLogo')
    title_metadata_badge: TitleMetadataBadge | None = Field(None, alias='titleMetadataBadge')

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

class Subscription(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    app_fallback_url: str | None = Field(None, alias='appFallbackUrl')
    app_subscription_url: str | None = Field(None, alias='appSubscriptionUrl')
    benefit_id: str | None = Field(None, alias='benefitId')
    display_messages: list[Any] | None = Field(None, alias='displayMessages')
    label: str | None = None
    problems: list[Any] | None = None
    ref_marker: str | None = Field(None, alias='refMarker')
    s_type: str | None = Field(None, alias='sType')
    signup_link: str | None = Field(None, alias='signupLink')
    channel_link: str | None = Field(None, alias='channelLink')

class Payload1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    payload_type: str | None = Field(None, alias='payloadType')
    transaction: Transaction | None = None
    subscription: Subscription | None = None

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

class TransactionDetail(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    component_payload: ComponentPayload | None = Field(None, alias='componentPayload')
    component_primitive: str | None = Field(None, alias='componentPrimitive')

class Tags(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    logo_entity_tag: str | None = Field(None, alias='LOGO_ENTITY_TAG')
    logo_height: str | None = Field(None, alias='LOGO_HEIGHT')
    logo_width: str | None = Field(None, alias='LOGO_WIDTH')

class LogoComponent(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    tags: Tags | None = None
    url: str | None = None

class ComponentPayload1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    text_component: TextComponent | None = Field(None, alias='textComponent')
    logo_component: LogoComponent | None = Field(None, alias='logoComponent')

class Header(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    component_payload: ComponentPayload1 | None = Field(None, alias='componentPayload')
    component_primitive: str | None = Field(None, alias='componentPrimitive')

class Tags1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    text_theme: str | None = Field(None, alias='TEXT_THEME')

class TextComponent2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    tags: Tags1 | None = None
    text: str | None = None
    text_type: str | None = Field(None, alias='textType')

class ComponentPayload2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    text_component: TextComponent2 | None = Field(None, alias='textComponent')

class MotivatorMessaging(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    component_payload: ComponentPayload2 | None = Field(None, alias='componentPayload')
    component_primitive: str | None = Field(None, alias='componentPrimitive')

class Components(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    transaction_detail: TransactionDetail | None = Field(None, alias='TRANSACTION_DETAIL')
    header: Header | None = Field(None, alias='HEADER')
    motivator_messaging: MotivatorMessaging | None = Field(None, alias='MOTIVATOR_MESSAGING')

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

class Subscription1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    app_fallback_url: str | None = Field(None, alias='appFallbackUrl')
    app_subscription_url: str | None = Field(None, alias='appSubscriptionUrl')
    benefit_id: str | None = Field(None, alias='benefitId')
    display_messages: list[Any] | None = Field(None, alias='displayMessages')
    label: str | None = None
    problems: list[Any] | None = None
    ref_marker: str | None = Field(None, alias='refMarker')
    s_type: str | None = Field(None, alias='sType')
    signup_link: str | None = Field(None, alias='signupLink')

class Payload2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    payload_type: str | None = Field(None, alias='payloadType')
    transaction: Transaction1 | None = None
    subscription: Subscription1 | None = None

class Action2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    action_type: str | None = Field(None, alias='actionType')
    is_selected: bool | None = Field(None, alias='isSelected')
    payload: Payload2 | None = None
    presentation: Presentation | None = None

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

class Tags2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    brand_glow: str | None = Field(None, alias='BRAND_GLOW')
    text_theme: str | None = Field(None, alias='TEXT_THEME')

class TextComponent3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    tags: Tags2 | None = None
    text: str | None = None
    text_type: str | None = Field(None, alias='textType')

class Tags3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    brand_glow: str | None = Field(None, alias='BRAND_GLOW')
    logo_entity_tag: str | None = Field(None, alias='LOGO_ENTITY_TAG')
    logo_height: str | None = Field(None, alias='LOGO_HEIGHT')
    logo_width: str | None = Field(None, alias='LOGO_WIDTH')

class LogoComponent1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    tags: Tags3 | None = None
    url: str | None = None

class ComponentPayload4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    text_component: TextComponent3 | None = Field(None, alias='textComponent')
    logo_component: LogoComponent1 | None = Field(None, alias='logoComponent')

class Banner(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    component_payload: ComponentPayload4 | None = Field(None, alias='componentPayload')
    component_primitive: str | None = Field(None, alias='componentPrimitive')

class IconTextListItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    icon: str | None = None
    tags: dict[str, Any] | None = None
    text: str | None = None
    text_type: str | None = Field(None, alias='textType')

class IconTextListComponent(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    icon_text_list: list[IconTextListItem] | None = Field(None, alias='iconTextList')

class ComponentPayload5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    icon_text_list_component: IconTextListComponent | None = Field(None, alias='iconTextListComponent')

class MotivatorMessaging1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    component_payload: ComponentPayload5 | None = Field(None, alias='componentPayload')
    component_primitive: str | None = Field(None, alias='componentPrimitive')

class TextComponent4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    tags: dict[str, Any] | None = None
    text: str | None = None
    text_type: str | None = Field(None, alias='textType')

class Tags4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    alt_text: str | None = Field(None, alias='ALT_TEXT')

class ImageListItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    tags: Tags4 | None = None
    url: str | None = None

class ImageListComponent(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    image_list: list[ImageListItem] | None = Field(None, alias='imageList')

class ComponentPayload7(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    text_component: TextComponent4 | None = Field(None, alias='textComponent')
    image_list_component: ImageListComponent | None = Field(None, alias='imageListComponent')

class ComponentListItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    component_payload: ComponentPayload7 | None = Field(None, alias='componentPayload')
    component_primitive: str | None = Field(None, alias='componentPrimitive')

class MixedComponent(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    component_list: list[ComponentListItem] | None = Field(None, alias='componentList')

class ComponentPayload6(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    mixed_component: MixedComponent | None = Field(None, alias='mixedComponent')

class RelatedBenefits(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    component_payload: ComponentPayload6 | None = Field(None, alias='componentPayload')
    component_primitive: str | None = Field(None, alias='componentPrimitive')

class Components1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    transaction_detail: TransactionDetail1 | None = Field(None, alias='TRANSACTION_DETAIL')
    banner: Banner | None = Field(None, alias='BANNER')
    motivator_messaging: MotivatorMessaging1 | None = Field(None, alias='MOTIVATOR_MESSAGING')
    related_benefits: RelatedBenefits | None = Field(None, alias='RELATED_BENEFITS')

class CardOption(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    actions: list[Action2] | None = None
    card_type: str | None = Field(None, alias='cardType')
    components: Components1 | None = None

class Playback(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    benefit_id: str | None = Field(None, alias='benefitId')
    correlation_id: str | None = Field(None, alias='correlationId')
    expiry_time: int | None = Field(None, alias='expiryTime')
    fallback_url: str | None = Field(None, alias='fallbackURL')
    is_trailer: bool | None = Field(None, alias='isTrailer')
    label: str | None = None
    minutes_remaining: int | None = Field(None, alias='minutesRemaining')
    playback_envelope: str | None = Field(None, alias='playbackEnvelope')
    playback_id: str | None = Field(None, alias='playbackID')
    playback_status: str | None = Field(None, alias='playbackStatus')
    playback_url: str | None = Field(None, alias='playbackURL')
    player_ref_marker: str | None = Field(None, alias='playerRefMarker')
    player_ui_spec: str | None = Field(None, alias='playerUISpec')
    ref_marker: str | None = Field(None, alias='refMarker')
    resume_time: int | None = Field(None, alias='resumeTime')
    run_time: int | None = Field(None, alias='runTime')
    video_material_type: str | None = Field(None, alias='videoMaterialType')

class Payload(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    expanding_card: ExpandingCard | None = Field(None, alias='expandingCard')
    payload_type: str | None = Field(None, alias='payloadType')
    card_options: list[CardOption] | None = Field(None, alias='cardOptions')
    playback: Playback | None = None

class Presentation2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    primary_label: str | None = Field(None, alias='primaryLabel')
    ref_marker: str | None = Field(None, alias='refMarker')
    icon: str | None = None

class PrimaryAction(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    action_type: str | None = Field(None, alias='actionType')
    is_selected: bool | None = Field(None, alias='isSelected')
    payload: Payload | None = None
    presentation: Presentation2 | None = None

class ReactionAction(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    csrf_token: str | None = Field(None, alias='csrfToken')
    reaction: str | None = None
    sign_in_url: str | None = Field(None, alias='signInUrl')

class Playback1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    benefit_id: str | None = Field(None, alias='benefitId')
    correlation_id: str | None = Field(None, alias='correlationId')
    expiry_time: int | None = Field(None, alias='expiryTime')
    fallback_url: str | None = Field(None, alias='fallbackURL')
    is_trailer: bool | None = Field(None, alias='isTrailer')
    label: str | None = None
    playback_envelope: str | None = Field(None, alias='playbackEnvelope')
    playback_id: str | None = Field(None, alias='playbackID')
    playback_status: str | None = Field(None, alias='playbackStatus')
    playback_url: str | None = Field(None, alias='playbackURL')
    player_ref_marker: str | None = Field(None, alias='playerRefMarker')
    ref_marker: str | None = Field(None, alias='refMarker')
    resume_time: int | None = Field(None, alias='resumeTime')
    run_time: int | None = Field(None, alias='runTime')
    video_material_type: str | None = Field(None, alias='videoMaterialType')

class Payload3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    payload_type: str | None = Field(None, alias='payloadType')
    playback: Playback1 | None = None

class Presentation3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    icon: str | None = None
    primary_label: str | None = Field(None, alias='primaryLabel')
    ref_marker: str | None = Field(None, alias='refMarker')

class SecondaryAction(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    action_type: str | None = Field(None, alias='actionType')
    is_selected: bool | None = Field(None, alias='isSelected')
    payload: Payload3 | None = None
    presentation: Presentation3 | None = None

class Atf1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    messages: Messages | None = None
    primary_actions: list[PrimaryAction] | None = Field(None, alias='primaryActions')
    reaction_action: ReactionAction | None = Field(None, alias='reactionAction')
    secondary_actions: list[SecondaryAction] | None = Field(None, alias='secondaryActions')
    view_ref_marker: str | None = Field(None, alias='viewRefMarker')

class Action(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    btf: dict[str, Any] | None = None
    atf: dict[str, Atf1] | None = None

class Refund(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    fragments: dict[str, Any] | None = None
    refunding: Any | None = None

class Imdb(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    max_score: str | None = Field(None, alias='maxScore')
    score: int | float | None = None
    score_formatted: str | None = Field(None, alias='scoreFormatted')

class Content1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    href: str | None = None

class Attrs(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    content: Content1 | None = None

class Content(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    attrs: Attrs | None = None
    string: str | None = None

class Link(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    aria_label: str | None = Field(None, alias='ariaLabel')
    href: str | None = None

class Image(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    alt: str | None = None
    link: Link | None = None
    path: str | None = None

class Title(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    attrs: dict[str, Any] | None = None
    string: str | None = None

class AtfBottom(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__type: str | None = Field(None, alias='__type')
    content: Content | None = None
    image: Image | None = None
    title: Title | None = None

class Creative(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    atf_bottom: AtfBottom | None = Field(None, alias='atfBottom')

class Banner1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    crow: dict[str, Any] | None = None
    ui: Any | None = None

class Notification(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    alerts: list[Any] | None = None
    warnings: list[Any] | None = None

class Season(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    season_id: str | None = Field(None, alias='seasonId')
    season_link: str | None = Field(None, alias='seasonLink')
    display_name: str | None = Field(None, alias='displayName')
    season_selector_icon: str | None = Field(None, alias='seasonSelectorIcon')
    sequence_number: int | None = Field(None, alias='sequenceNumber')
    is_selected: bool | None = Field(None, alias='isSelected')

class Self(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    asins: list[str] | None = None
    compact_gti: str | None = Field(None, alias='compactGTI')
    gti: str | None = None
    is_launched: bool | None = Field(None, alias='isLaunched')
    link: str | None = None
    sequence_number: int | None = Field(None, alias='sequenceNumber')
    title_type: str | None = Field(None, alias='titleType')

class Query(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    signin: str | None = None
    return_url: str | None = Field(None, alias='returnUrl')
    ref_: str | None = None

class Endpoint(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    partial_url: str | None = Field(None, alias='partialURL')
    query: Query | None = None

class Text(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    attrs: dict[str, Any] | None = None
    string: str | None = None

class Watchlist(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    ajax_enabled: bool | None = Field(None, alias='ajaxEnabled')
    endpoint: Endpoint | None = None
    format_code: str | None = Field(None, alias='formatCode')
    tag: str | None = None
    text: Text | None = None

class Restriction(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_pin_setup_required: bool | None = Field(None, alias='isPinSetupRequired')
    is_playback_pin_required: bool | None = Field(None, alias='isPlaybackPinRequired')
    is_purchase_pin_required: bool | None = Field(None, alias='isPurchasePinRequired')

class Features1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    activate_auto_playing_in_hovers: str | None = Field(None, alias='activateAutoPlayingInHovers')
    offer_clarity_enabled: str | None = Field(None, alias='offerClarityEnabled')
    is_reviews_submission_enabled: str | None = Field(None, alias='isReviewsSubmissionEnabled')
    disable_hover: str | None = Field(None, alias='disableHover')
    is_autoplay_setting_enabled: str | None = Field(None, alias='isAutoplaySettingEnabled')
    is_record_season_enabled: str | None = Field(None, alias='isRecordSeasonEnabled')
    is_detail_page_header_widget_enabled: str | None = Field(None, alias='isDetailPageHeaderWidgetEnabled')
    disable_player_for_google_bot: str | None = Field(None, alias='disablePlayerForGoogleBot')
    disable_whisper_cache_in_draper: str | None = Field(None, alias='disableWhisperCacheInDraper')
    is_detail_page_header_widget_refresh_enabled: str | None = Field(None, alias='isDetailPageHeaderWidgetRefreshEnabled')
    panorama_treatment: str | None = Field(None, alias='panoramaTreatment')
    disable_enrich_item_metadata: str | None = Field(None, alias='disableEnrichItemMetadata')
    disable_marin_tracking: str | None = Field(None, alias='disableMarinTracking')
    is_stream_selector_modal_enabled: str | None = Field(None, alias='isStreamSelectorModalEnabled')
    is_swm_enabled: str | None = Field(None, alias='isSWMEnabled')
    is_spider_noir: str | None = Field(None, alias='isSpiderNoir')
    disable_explore_tab: str | None = Field(None, alias='disableExploreTab')

class Btf(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    decoration_scheme: str | None = Field(None, alias='decorationScheme')
    dynamic_features: list[str] | None = Field(None, alias='dynamicFeatures')
    feature_scheme: str | None = Field(None, alias='featureScheme')
    widget_scheme: str | None = Field(None, alias='widgetScheme')

class Atf2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    decoration_scheme: str | None = Field(None, alias='decorationScheme')
    dynamic_features: list[str] | None = Field(None, alias='dynamicFeatures')
    feature_scheme: str | None = Field(None, alias='featureScheme')
    widget_scheme: str | None = Field(None, alias='widgetScheme')

class SwiftParameters(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    btf: Btf | None = Field(None, alias='BTF')
    atf: Atf2 | None = Field(None, alias='ATF')

class PageContext(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    app: str | None = None
    download_launch_type: str | None = Field(None, alias='downloadLaunchType')
    enable_hover: bool | None = Field(None, alias='enableHover')
    features: Features1 | None = None
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
    sub_page_type: str | None = Field(None, alias='subPageType')
    swift_parameters: SwiftParameters | None = Field(None, alias='swiftParameters')

class Url(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    href: str | None = None

class Attrs1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: Url | None = None

class HelpText(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    attrs: Attrs1 | None = None
    string: str | None = None

class CopyLinkButton(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    localized_copy_link: str | None = Field(None, alias='localizedCopyLink')
    localized_link_copied: str | None = Field(None, alias='localizedLinkCopied')
    ref_tag: str | None = Field(None, alias='refTag')
    url: str | None = None

class Email(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    aria_text: str | None = Field(None, alias='ariaText')
    localized_text: str | None = Field(None, alias='localizedText')
    reftag: str | None = None
    target: str | None = None
    url: str | None = None

class Facebook(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    aria_text: str | None = Field(None, alias='ariaText')
    height: int | None = None
    localized_text: str | None = Field(None, alias='localizedText')
    reftag: str | None = None
    target: str | None = None
    url: str | None = None
    width: int | None = None

class WhatsApp(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    aria_text: str | None = Field(None, alias='ariaText')
    height: int | None = None
    localized_text: str | None = Field(None, alias='localizedText')
    reftag: str | None = None
    target: str | None = None
    url: str | None = None
    width: int | None = None

class XCorp(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    aria_text: str | None = Field(None, alias='ariaText')
    height: int | None = None
    localized_text: str | None = Field(None, alias='localizedText')
    reftag: str | None = None
    target: str | None = None
    url: str | None = None
    width: int | None = None

class ShareButtons(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    email: Email | None = Field(None, alias='Email')
    facebook: Facebook | None = Field(None, alias='Facebook')
    whats_app: WhatsApp | None = Field(None, alias='WhatsApp')
    x_corp: XCorp | None = Field(None, alias='XCorp')

class ShareWidgetModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    copy_link_button: CopyLinkButton | None = Field(None, alias='copyLinkButton')
    is_creator: bool | None = Field(None, alias='isCreator')
    localized_share: str | None = Field(None, alias='localizedShare')
    share_buttons: ShareButtons | None = Field(None, alias='shareButtons')

class Attrs2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: Url | None = None

class TermsText(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    attrs: Attrs2 | None = None
    string: str | None = None

class Attrs3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: Url | None = None

class WriteReviewText(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    attrs: Attrs3 | None = None
    string: str | None = None

class BottomBar(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    feedback_sign_in_url: str | None = Field(None, alias='feedbackSignInUrl')
    help_text: HelpText | None = Field(None, alias='helpText')
    share_widget_model: ShareWidgetModel | None = Field(None, alias='shareWidgetModel')
    terms_text: TermsText | None = Field(None, alias='termsText')
    write_review_text: WriteReviewText | None = Field(None, alias='writeReviewText')

class DraperTrackingEvents(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    removed_from_watchlist_notification: str | None = Field(None, alias='removedFromWatchlistNotification')
    resume: str | None = None
    default_impression: str | None = Field(None, alias='defaultImpression')
    add_to_watchlist: str | None = Field(None, alias='addToWatchlist')
    first_quartile: str | None = Field(None, alias='firstQuartile')
    pause: str | None = None
    accept_invitation: str | None = Field(None, alias='acceptInvitation')
    skip: str | None = None
    mute: str | None = None
    expand: str | None = None
    playback_blocked: str | None = Field(None, alias='playbackBlocked')
    unmute: str | None = None
    complete: str | None = None
    error: str | None = None
    third_quartile: str | None = Field(None, alias='thirdQuartile')
    midpoint: str | None = None
    added_to_watchlist_notification: str | None = Field(None, alias='addedToWatchlistNotification')
    close: str | None = None
    rewind: str | None = None

class TextMap(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    enter_fullscreen: str | None = Field(None, alias='enterFullscreen')
    exit_fullscreen: str | None = Field(None, alias='exitFullscreen')
    mute_button: str | None = Field(None, alias='muteButton')
    unmute_button: str | None = Field(None, alias='unmuteButton')

class AutoplayTrailerHero(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    asset_id: str | None = Field(None, alias='assetId')
    draper_tracking_events: DraperTrackingEvents | None = Field(None, alias='draperTrackingEvents')
    is_trailer_autoplay_enabled: bool | None = Field(None, alias='isTrailerAutoplayEnabled')
    playback_envelope: str | None = Field(None, alias='playbackEnvelope')
    playback_id: str | None = Field(None, alias='playbackId')
    ref_marker: str | None = Field(None, alias='refMarker')
    text_map: TextMap | None = Field(None, alias='textMap')

class MaturityRating(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__type: str | None = Field(None, alias='__type')
    description: str | None = None
    display_text: str | None = Field(None, alias='displayText')
    id: str | None = None
    country_code: str | None = Field(None, alias='countryCode')

class Metadata1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    episode_count: str | None = Field(None, alias='episodeCount')
    maturity_rating: MaturityRating | None = Field(None, alias='maturityRating')
    moods: list[str] | None = None

class State(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    features: Features | None = None
    page_title_id: str | None = Field(None, alias='pageTitleId')
    detail: Detail | None = None
    action: Action | None = None
    refund: Refund | None = None
    imdb: dict[str, Imdb] | None = None
    buy_box: dict[str, Any] | None = Field(None, alias='buyBox')
    buybox_title_id: dict[str, str] | None = Field(None, alias='buyboxTitleId')
    creative: dict[str, Creative] | None = None
    banner: Banner1 | None = None
    age_verification_banner: dict[str, Any] | None = Field(None, alias='ageVerificationBanner')
    notification: dict[str, Notification] | None = None
    seasons: dict[str, list[Season]] | None = None
    self: dict[str, Self] | None = None
    watchlist: dict[str, Watchlist] | None = None
    restriction: dict[str, Restriction] | None = None
    extras: dict[str, Any] | None = None
    tokens: dict[str, Any] | None = None
    page_link: dict[str, Any] | None = Field(None, alias='pageLink')
    episode_list: dict[str, Any] | None = Field(None, alias='episodeList')
    containers: dict[str, Any] | None = None
    recordings: dict[str, Any] | None = None
    bundles_content: dict[str, Any] | None = Field(None, alias='bundlesContent')
    other_formats: dict[str, Any] | None = Field(None, alias='otherFormats')
    page_context: PageContext | None = Field(None, alias='pageContext')
    bottom_bar: BottomBar | None = Field(None, alias='bottomBar')
    autoplay_hero: dict[str, Any] | None = Field(None, alias='autoplayHero')
    autoplay_trailer_hero: dict[str, AutoplayTrailerHero] | None = Field(None, alias='autoplayTrailerHero')
    playback_integration: dict[str, Any] | None = Field(None, alias='playbackIntegration')
    coming_soon: dict[str, bool] | None = Field(None, alias='comingSoon')
    metadata: dict[str, Metadata1] | None = None
    widgets: dict[str, dict[str, Any]] | None = None
    bottom_menu: dict[str, Any] | None = Field(None, alias='bottomMenu')
    recording_metadata: dict[str, Any] | None = Field(None, alias='recordingMetadata')

class Strings(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    dv_dp_wp_create_ineligible_swm: str | None = Field(None, alias='DV_DP_WP_CREATE_INELIGIBLE_SWM')
    dv_web_one_season: str | None = Field(None, alias='DV_WEB_ONE_SEASON')
    dv_web_dp_eu_cancel_accidental_purchase: str | None = Field(None, alias='DV_WEB_DP_EU_CANCEL_ACCIDENTAL_PURCHASE')
    dv_dp_wp_unsupported_chat_heading: str | None = Field(None, alias='DV_DP_WP_UNSUPPORTED_CHAT_HEADING')
    dv_comma_separator: str | None = Field(None, alias='DV_comma_separator')
    dv_web_sports_record_success_upcoming: str | None = Field(None, alias='DV_WEB_SPORTS_RECORD_SUCCESS_UPCOMING')
    dv_dp_aria_audio_description: str | None = Field(None, alias='DV_DP_ARIA_audio_description')
    dv_dp_dv_gcpc_window_title: str | None = Field(None, alias='DV_DP_DV_GCPC_window_title')
    dv_dp_wp_end: str | None = Field(None, alias='DV_DP_WP_END')
    dv_web_dp_eu_cancel_purch_modal_submit: str | None = Field(None, alias='DV_WEB_DP_EU_CANCEL_PURCH_MODAL_SUBMIT')
    dv_dp_select_season: str | None = Field(None, alias='DV_DP_select_season')
    dv_web_sports_record_success_ended: str | None = Field(None, alias='DV_WEB_SPORTS_RECORD_SUCCESS_ENDED')
    dv_dp_aria_hdr10_plus: str | None = Field(None, alias='DV_DP_ARIA_hdr10_plus')
    dv_dp_you_multiple_orders_for_this_title: str | None = Field(None, alias='DV_DP_you_multiple_orders_for_this_title')
    dv_web_sports_record_league_success_ended: str | None = Field(None, alias='DV_WEB_SPORTS_RECORD_LEAGUE_SUCCESS_ENDED')
    dv_dp_wl_remove_movie: str | None = Field(None, alias='DV_DP_WL_removeMovie')
    dv_ab_cancel_accidental_purchase: str | None = Field(None, alias='DV_AB_CANCEL_ACCIDENTAL_PURCHASE')
    dv_dp_gc_balance_update_failed: str | None = Field(None, alias='DV_DP_GC_balance_update_failed')
    avod_dp_gc_promotion_message: str | None = Field(None, alias='AVOD_DP_GC_promotion_message')
    dv_dp_only_playback_available_in_gen4_message: str | None = Field(None, alias='DV_DP_only_playback_available_in_gen4_message')
    dv_web_linear_program_record_start_success: str | None = Field(None, alias='DV_WEB_LINEAR_PROGRAM_RECORD_START_SUCCESS')
    assoc_mshop_getlink_close: str | None = Field(None, alias='assoc-mshop-getlink-close')
    dv_tw_title_genres: str | None = Field(None, alias='DV_TW_title_genres')
    dv_incompatible_systems_banner_body_update_os: str | None = Field(None, alias='DV_INCOMPATIBLE_SYSTEMS_BANNER_BODY_UPDATE_OS')
    dv_web_playback_watch_in_app: str | None = Field(None, alias='DV_WEB_PLAYBACK_WATCH_IN_APP')
    dv_incompatible_systems_banner_body: str | None = Field(None, alias='DV_INCOMPATIBLE_SYSTEMS_BANNER_BODY')
    dv_web_recording_scheduled: str | None = Field(None, alias='DV_WEB_RECORDING_SCHEDULED')
    assoc_mshop_getlink_share_copy: str | None = Field(None, alias='assoc-mshop-getlink-share-copy')
    dv_web_dp_eu_choose_order_to_cancel: str | None = Field(None, alias='DV_WEB_DP_EU_choose_order_to_cancel')
    dv_dp_none_available: str | None = Field(None, alias='DV_DP_none_available')
    dv_dp_aria_dolby_atmos: str | None = Field(None, alias='DV_DP_ARIA_dolby_atmos')
    dv_dp_wp_unsupported_browser_heading: str | None = Field(None, alias='DV_DP_WP_UNSUPPORTED_BROWSER_HEADING')
    dv_dp_wp_unsupported_chat: str | None = Field(None, alias='DV_DP_WP_UNSUPPORTED_CHAT')
    dv_web_playback_app_benefits: str | None = Field(None, alias='DV_WEB_PLAYBACK_APP_BENEFITS')
    dv_dp_wp_error: str | None = Field(None, alias='DV_DP_WP_ERROR')
    dv_dp_wp_stream_ended: str | None = Field(None, alias='DV_DP_WP_STREAM_ENDED')
    dv_dp_wl_remove_tv: str | None = Field(None, alias='DV_DP_WL_removeTv')
    dv_dp_aria_release_year: str | None = Field(None, alias='DV_DP_ARIA_release_year')
    dv_web_recording_now: str | None = Field(None, alias='DV_WEB_RECORDING_NOW')
    assoc_mshop_getlink_share_ingress_normal: str | None = Field(None, alias='assoc-mshop-getlink-share-ingress-normal')
    dv_incompatible_systems_banner_heading_unsupported_browser: str | None = Field(None, alias='DV_INCOMPATIBLE_SYSTEMS_BANNER_HEADING_UNSUPPORTED_BROWSER')
    dv_dp_wp_join_ineligible_tvod: str | None = Field(None, alias='DV_DP_WP_JOIN_INELIGIBLE_TVOD')
    dv_dp_wp_join_ineligible_svod_tvod: str | None = Field(None, alias='DV_DP_WP_JOIN_INELIGIBLE_SVOD_TVOD')
    avod_dp_e_error_ok: str | None = Field(None, alias='AVOD_DP_E_error_ok')
    dv_dp_tr_dislike_toast: str | None = Field(None, alias='DV_DP_TR_dislike_toast')
    dv_web_live_not_supported_body: str | None = Field(None, alias='DV_WEB_LIVE_NOT_SUPPORTED_BODY')
    dv_web_sports_cancel_record_league_success: str | None = Field(None, alias='DV_WEB_SPORTS_CANCEL_RECORD_LEAGUE_SUCCESS')
    dv_dp_tr_liked_aria: str | None = Field(None, alias='DV_DP_TR_liked_aria')
    dv_tw_title_producers: str | None = Field(None, alias='DV_TW_title_producers')
    dv_dp_wp_unsupported_browser: str | None = Field(None, alias='DV_DP_WP_UNSUPPORTED_BROWSER')
    dv_incompatible_systems_banner_heading_update_os: str | None = Field(None, alias='DV_INCOMPATIBLE_SYSTEMS_BANNER_HEADING_UPDATE_OS')
    dv_dp_ub_gc_popup_apply: str | None = Field(None, alias='DV_DP_UB_GC_popup_apply')
    dv_dp_wp_banned_specific_chat: str | None = Field(None, alias='DV_DP_WP_BANNED_SPECIFIC_CHAT')
    dv_incompatible_systems_banner_heading_update_browser: str | None = Field(None, alias='DV_INCOMPATIBLE_SYSTEMS_BANNER_HEADING_UPDATE_BROWSER')
    dv_dp_wp_create_ineligible: str | None = Field(None, alias='DV_DP_WP_CREATE_INELIGIBLE')
    dv_dp_aria_watch_title: str | None = Field(None, alias='DV_DP_ARIA_watch_title')
    dv_web_playback_watch_in_pv_app: str | None = Field(None, alias='DV_WEB_PLAYBACK_WATCH_IN_PV_APP')
    dv_dp_wp_join_ineligible: str | None = Field(None, alias='DV_DP_WP_JOIN_INELIGIBLE')
    dv_dp_aria_dolby_vision: str | None = Field(None, alias='DV_DP_ARIA_dolby_vision')
    dv_dp_wp_join_ineligible_heading: str | None = Field(None, alias='DV_DP_WP_JOIN_INELIGIBLE_HEADING')
    dv_tw_title_studio: str | None = Field(None, alias='DV_TW_title_studio')
    assoc_mshop_getlink_share_trackingid: str | None = Field(None, alias='assoc-mshop-getlink-share-trackingid')
    dv_cr_review_submission_processing: str | None = Field(None, alias='DV_CR_review_submission_processing')
    dv_web_linear_program_record_error: str | None = Field(None, alias='DV_WEB_LINEAR_PROGRAM_RECORD_ERROR')
    dv_dp_aria_dolby_51: str | None = Field(None, alias='DV_DP_ARIA_dolby_51')
    dv_web_dp_eu_cancel_purch_modal_header: str | None = Field(None, alias='DV_WEB_DP_EU_CANCEL_PURCH_MODAL_HEADER')
    dv_dp_wp_safari_mac_unsupported_body: str | None = Field(None, alias='DV_DP_WP_SAFARI_MAC_UNSUPPORTED_BODY')
    dv_dp_gc_widget_heading: str | None = Field(None, alias='DV_DP_GC_widget_heading')
    dv_dp_tr_err_msg: str | None = Field(None, alias='DV_DP_TR_err_msg')
    dv_tw_title_languages: str | None = Field(None, alias='DV_TW_title_languages')
    avod_dp_e_error_text: str | None = Field(None, alias='AVOD_DP_E_error_text')
    dv_dp_player_timeout_heading: str | None = Field(None, alias='DV_DP_PLAYER_TIMEOUT_HEADING')
    dv_web_watchlist_label: str | None = Field(None, alias='DV_WEB_WATCHLIST_LABEL')
    avod_dp_season_selector: str | None = Field(None, alias='AVOD_DP_season_selector')
    dv_dp_atf_cast: str | None = Field(None, alias='DV_DP_ATF_CAST')
    dv_rbb_cancel_purch_modal_submit: str | None = Field(None, alias='DV_RBB_CANCEL_PURCH_MODAL_SUBMIT')
    dv_dp_aria_season_selector: str | None = Field(None, alias='DV_DP_ARIA_season_selector')
    dv_cr_review_submission_success: str | None = Field(None, alias='DV_CR_review_submission_success')
    dv_tw_title_content_descriptors: str | None = Field(None, alias='DV_TW_title_content_descriptors')
    dv_dp_wp_create_ineligible_svod_tvod: str | None = Field(None, alias='DV_DP_WP_CREATE_INELIGIBLE_SVOD_TVOD')
    dv_mwtw_title_main: str | None = Field(None, alias='DV_MWTW_TITLE_MAIN')
    dv_tw_title_subtitles: str | None = Field(None, alias='DV_TW_title_subtitles')
    dv_dp_aria_star_rating: str | None = Field(None, alias='DV_DP_ARIA_star_rating')
    dv_dot_separator: str | None = Field(None, alias='DV_dot_separator')
    dv_tw_title_directors: str | None = Field(None, alias='DV_TW_title_directors')
    dv_dp_unavailable_page_message: str | None = Field(None, alias='DV_DP_unavailable_page_message')
    dv_dp_player_timeout_body: str | None = Field(None, alias='DV_DP_PLAYER_TIMEOUT_BODY')
    avod_wl_error_msg: str | None = Field(None, alias='AVOD_WL_error_msg')
    dv_dp_minutes_remaining: str | None = Field(None, alias='DV_DP_minutes_remaining')
    dv_mwtw_title: str | None = Field(None, alias='DV_MWTW_TITLE')
    dv_web_playback_watch_here: str | None = Field(None, alias='DV_WEB_PLAYBACK_WATCH_HERE')
    dv_rbb_cancel_purch_modal_header: str | None = Field(None, alias='DV_RBB_CANCEL_PURCH_MODAL_HEADER')
    dv_dp_wp_create_ineligible_tvod: str | None = Field(None, alias='DV_DP_WP_CREATE_INELIGIBLE_TVOD')
    avod_dp_gc_toc_learn_more: str | None = Field(None, alias='AVOD_DP_GC_toc_learn_more')
    dv_dp_tr_dislike_btn: str | None = Field(None, alias='DV_DP_TR_dislike_btn')
    dv_web_sports_cancel_record_success: str | None = Field(None, alias='DV_WEB_SPORTS_CANCEL_RECORD_SUCCESS')
    dv_dp_gc_balance_type_heading: str | None = Field(None, alias='DV_DP_GC_balance_type_heading')
    dv_tw_title_cast: str | None = Field(None, alias='DV_TW_title_cast')
    dv_dp_wl_add_movie: str | None = Field(None, alias='DV_DP_WL_addMovie')
    dv_incompatible_systems_banner_body_unsupported_browser: str | None = Field(None, alias='DV_INCOMPATIBLE_SYSTEMS_BANNER_BODY_UNSUPPORTED_BROWSER')
    dv_web_watchlist_csrf_problem: str | None = Field(None, alias='DV_WEB_WATCHLIST_CSRF_PROBLEM')
    dv_web_settings_head_subtitles: str | None = Field(None, alias='DV_WEB_SETTINGS_HEAD_SUBTITLES')
    pv_le_ip_watchlist_and_record: str | None = Field(None, alias='PV_LE_IP_WATCHLIST_AND_RECORD')
    dv_dp_aria_pse_badge: str | None = Field(None, alias='DV_DP_ARIA_pse_badge')
    dv_web_sports_record: str | None = Field(None, alias='DV_WEB_SPORTS_RECORD')
    dv_web_seasons_count: str | None = Field(None, alias='DV_WEB_SEASONS_COUNT')
    dv_dp_aria_imdb_rating: str | None = Field(None, alias='DV_DP_ARIA_imdb_rating')
    avod_dp_redeem_gift_card_or_promotion: str | None = Field(None, alias='AVOD_DP_redeem_gift_card_or_promotion')
    dv_dp_atf_more_icon_label: str | None = Field(None, alias='DV_DP_ATF_MORE_ICON_LABEL')
    dv_dp_wp_create_ineligible_heading: str | None = Field(None, alias='DV_DP_WP_CREATE_INELIGIBLE_HEADING')
    dv_dp_ub_gc_success_message: str | None = Field(None, alias='DV_DP_UB_GC_success_message')
    dv_dp_aria_suitable_for: str | None = Field(None, alias='DV_DP_ARIA_suitable_for')
    dv_dp_wp_geo_restriction_heading: str | None = Field(None, alias='DV_DP_WP_GEO_RESTRICTION_HEADING')
    dv_incompatible_systems_banner_body_update_browser: str | None = Field(None, alias='DV_INCOMPATIBLE_SYSTEMS_BANNER_BODY_UPDATE_BROWSER')
    dv_dp_tr_like_btn: str | None = Field(None, alias='DV_DP_TR_like_btn')
    dv_dp_wp_geo_restriction: str | None = Field(None, alias='DV_DP_WP_GEO_RESTRICTION')
    dv_tw_title_cast_and_creators: str | None = Field(None, alias='DV_TW_title_cast_and_creators')
    dv_dp_wp_end_heading: str | None = Field(None, alias='DV_DP_WP_END_HEADING')
    dv_dp_wp_safari_mac_unsupported_heading: str | None = Field(None, alias='DV_DP_WP_SAFARI_MAC_UNSUPPORTED_HEADING')
    dv_web_recording_indicator: str | None = Field(None, alias='DV_WEB_RECORDING_INDICATOR')
    dv_dp_gc_balances_explanation: str | None = Field(None, alias='DV_DP_GC_balances_explanation')
    assoc_mshop_getlink_share_ineligible_title: str | None = Field(None, alias='assoc-mshop-getlink-share-ineligible-title')
    dv_dp_gc_wrong_code: str | None = Field(None, alias='DV_DP_GC_wrong_code')
    dv_dp_choose_order_to_cancel: str | None = Field(None, alias='DV_DP_choose_order_to_cancel')
    dv_web_linear_program_record_cancel_success: str | None = Field(None, alias='DV_WEB_LINEAR_PROGRAM_RECORD_CANCEL_SUCCESS')
    dv_dp_wp_banned_specific_chat_heading: str | None = Field(None, alias='DV_DP_WP_BANNED_SPECIFIC_CHAT_HEADING')
    dv_dp_aria_regulatory_rating: str | None = Field(None, alias='DV_DP_ARIA_regulatory_rating')
    dv_dp_wp_create_ineligible_svod_tvod_swm: str | None = Field(None, alias='DV_DP_WP_CREATE_INELIGIBLE_SVOD_TVOD_SWM')
    dv_dp_alt_channel_logo: str | None = Field(None, alias='DV_DP_ALT_channel_logo')
    dv_dp_ub_gc_enter_code: str | None = Field(None, alias='DV_DP_UB_GC_enter_code')
    dv_dp_gc_code_input_placeholder: str | None = Field(None, alias='DV_DP_GC_code_input_placeholder')
    dv_dp_gc_balance_amount_heading: str | None = Field(None, alias='DV_DP_GC_balance_amount_heading')
    dv_web_sports_record_league_success_upcoming: str | None = Field(None, alias='DV_WEB_SPORTS_RECORD_LEAGUE_SUCCESS_UPCOMING')
    assoc_mshop_getlink_share_storeid: str | None = Field(None, alias='assoc-mshop-getlink-share-storeid')
    dv_dp_tr_dislike_aria: str | None = Field(None, alias='DV_DP_TR_dislike_aria')
    dv_tw_amr_nr_text: str | None = Field(None, alias='DV_TW_amr_nr_text')
    assoc_mshop_getlink_share_ingress: str | None = Field(None, alias='assoc-mshop-getlink-share-ingress')
    dv_brand_av: str | None = Field(None, alias='DV_brand_av')
    dv_dp_aria_runtime: str | None = Field(None, alias='DV_DP_ARIA_runtime')
    dv_incompatible_systems_banner_heading: str | None = Field(None, alias='DV_INCOMPATIBLE_SYSTEMS_BANNER_HEADING')
    dv_dp_wp_error_heading: str | None = Field(None, alias='DV_DP_WP_ERROR_HEADING')
    dv_dp_more_info: str | None = Field(None, alias='DV_DP_more_info')
    dv_dp_tr_like_toast: str | None = Field(None, alias='DV_DP_TR_like_toast')
    dv_dp_tr_like_aria: str | None = Field(None, alias='DV_DP_TR_like_aria')
    dv_dp_unavailable_live_page_message: str | None = Field(None, alias='DV_DP_unavailable_live_page_message')
    dv_web_sports_cancel_record: str | None = Field(None, alias='DV_WEB_SPORTS_CANCEL_RECORD')
    dv_dp_tr_disliked_aria: str | None = Field(None, alias='DV_DP_TR_disliked_aria')
    dv_dp_wl_add_tv: str | None = Field(None, alias='DV_DP_WL_addTv')

class ResiliencyMetadata(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_degraded_response: bool | None = Field(None, alias='isDegradedResponse')
    is_no_content_response: bool | None = Field(None, alias='isNoContentResponse')
    is_partial_response: bool | None = Field(None, alias='isPartialResponse')

class Atf(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    home_region: str | None = Field(None, alias='homeRegion')
    state: State | None = None
    strings: Strings | None = None
    resiliency_metadata: ResiliencyMetadata | None = Field(None, alias='resiliencyMetadata')

class Features2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_elcano: bool | None = Field(None, alias='isElcano')

class Images1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    packshot: str | None = None
    covershot: str | None = None

class RatingsHistogram1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    five_star: FiveStar | None = Field(None, alias='fiveStar')
    four_star: FourStar | None = Field(None, alias='fourStar')
    one_star: OneStar | None = Field(None, alias='oneStar')
    three_star: ThreeStar | None = Field(None, alias='threeStar')
    two_star: TwoStar | None = Field(None, alias='twoStar')

class ReviewsAnalysisModel1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    ratings_histogram: RatingsHistogram1 | None = Field(None, alias='ratingsHistogram')
    review_rating_info: ReviewRatingInfo | None = Field(None, alias='reviewRatingInfo')

class Reviews1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    all_reviews_link: str | None = Field(None, alias='allReviewsLink')
    create_review_link: str | None = Field(None, alias='createReviewLink')
    locale_language: str | None = Field(None, alias='localeLanguage')
    review_submission_token: str | None = Field(None, alias='reviewSubmissionToken')
    reviews_analysis_model: ReviewsAnalysisModel1 | None = Field(None, alias='reviewsAnalysisModel')
    title_id: str | None = Field(None, alias='titleID')

class Detail2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | None = None
    synopsis: str | None = None
    audio_tracks: list[str] | None = Field(None, alias='audioTracks')
    duration: int | None = None
    entity_type: str | None = Field(None, alias='entityType')
    episode_number: int | None = Field(None, alias='episodeNumber')
    is_ad: bool | None = Field(None, alias='isAd')
    is_closed_caption: bool | None = Field(None, alias='isClosedCaption')
    is_dolby51: bool | None = Field(None, alias='isDolby51')
    is_dolby_atmos: bool | None = Field(None, alias='isDolbyAtmos')
    is_dolby_vision: bool | None = Field(None, alias='isDolbyVision')
    is_hdr: bool | None = Field(None, alias='isHdr')
    is_hdr10_plus: bool | None = Field(None, alias='isHdr10Plus')
    is_prime: bool | None = Field(None, alias='isPrime')
    is_pse: bool | None = Field(None, alias='isPse')
    is_uhd: bool | None = Field(None, alias='isUhd')
    is_x_ray: bool | None = Field(None, alias='isXRay')
    playback_tracks: list[Any] | None = Field(None, alias='playbackTracks')
    release_date: str | None = Field(None, alias='releaseDate')
    release_year: int | None = Field(None, alias='releaseYear')
    runtime: str | None = None
    subtitles: list[str] | None = None
    title_type: str | None = Field(None, alias='titleType')
    images: Images1 | None = None
    amazon_rating: AmazonRating | None = Field(None, alias='amazonRating')
    explore_panel_url: str | None = Field(None, alias='explorePanelURL')
    explore_tab_name: str | None = Field(None, alias='exploreTabName')
    parent_title: str | None = Field(None, alias='parentTitle')
    rating_badge: RatingBadge | None = Field(None, alias='ratingBadge')
    reviews: Reviews1 | None = None
    season_number: int | None = Field(None, alias='seasonNumber')

class Contributors1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    cast: list[CastItem] | None = None
    directors: list[Director] | None = None
    producers: list[Producer] | None = None

class Images2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    covershot: str | None = None
    heroshot: str | None = None
    packshot: str | None = None
    title_logo: str | None = Field(None, alias='titleLogo')
    titleshot: str | None = None
    provider_logo: str | None = Field(None, alias='providerLogo')

class RatingsHistogram2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    five_star: FiveStar | None = Field(None, alias='fiveStar')
    four_star: FourStar | None = Field(None, alias='fourStar')
    one_star: OneStar | None = Field(None, alias='oneStar')
    three_star: ThreeStar | None = Field(None, alias='threeStar')
    two_star: TwoStar | None = Field(None, alias='twoStar')

class ReviewsAnalysisModel2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    ratings_histogram: RatingsHistogram2 | None = Field(None, alias='ratingsHistogram')
    review_rating_info: ReviewRatingInfo | None = Field(None, alias='reviewRatingInfo')

class Reviews2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    all_reviews_link: str | None = Field(None, alias='allReviewsLink')
    create_review_link: str | None = Field(None, alias='createReviewLink')
    locale_language: str | None = Field(None, alias='localeLanguage')
    review_submission_token: str | None = Field(None, alias='reviewSubmissionToken')
    reviews_analysis_model: ReviewsAnalysisModel2 | None = Field(None, alias='reviewsAnalysisModel')
    title_id: str | None = Field(None, alias='titleID')

class BtfMoreDetails(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | None = None
    synopsis: str | None = None
    amazon_rating: AmazonRating | None = Field(None, alias='amazonRating')
    audio_tracks: list[str] | None = Field(None, alias='audioTracks')
    catalog_id: str | None = Field(None, alias='catalogId')
    contributors: Contributors1 | None = None
    enhanced_subtitles: list[EnhancedSubtitle] | None = Field(None, alias='enhancedSubtitles')
    entity_type: str | None = Field(None, alias='entityType')
    explore_panel_url: str | None = Field(None, alias='explorePanelURL')
    explore_tab_name: str | None = Field(None, alias='exploreTabName')
    genres: list[Genre] | None = None
    images: Images2 | None = None
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
    parent_title: str | None = Field(None, alias='parentTitle')
    playback_tracks: list[Any] | None = Field(None, alias='playbackTracks')
    rating_badge: RatingBadge | None = Field(None, alias='ratingBadge')
    release_date: str | None = Field(None, alias='releaseDate')
    release_year: int | None = Field(None, alias='releaseYear')
    reviews: Reviews2 | None = None
    runtime: str | None = None
    season_number: int | None = Field(None, alias='seasonNumber')
    studios: list[str] | None = None
    subtitles: list[str] | None = None
    title_type: str | None = Field(None, alias='titleType')
    duration: int | None = None

class Detail1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    detail: dict[str, Detail2] | None = None
    header_detail: dict[str, Any] | None = Field(None, alias='headerDetail')
    btf_more_details: dict[str, BtfMoreDetails] | None = Field(None, alias='btfMoreDetails')

class FocusMessage1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    dv_message: DvMessage | None = Field(None, alias='dvMessage')
    icon: str | None = None
    icon_type: str | None = Field(None, alias='iconType')

class Messages1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    entitlement_type: str | None = Field(None, alias='entitlementType')
    focus_message: FocusMessage1 | None = Field(None, alias='focusMessage')

class Transaction2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    asin: str | None = None
    csrf_token: str | None = Field(None, alias='csrfToken')
    csrf_token_workflow: str | None = Field(None, alias='csrfTokenWorkflow')
    display_messages: list[Any] | None = Field(None, alias='displayMessages')
    label: str | None = None
    offer_token: str | None = Field(None, alias='offerToken')
    purchase_data: PurchaseData | None = Field(None, alias='purchaseData')
    ref_marker: str | None = Field(None, alias='refMarker')

class Subscription2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    app_fallback_url: str | None = Field(None, alias='appFallbackUrl')
    app_subscription_url: str | None = Field(None, alias='appSubscriptionUrl')
    benefit_id: str | None = Field(None, alias='benefitId')
    channel_link: str | None = Field(None, alias='channelLink')
    display_messages: list[Any] | None = Field(None, alias='displayMessages')
    label: str | None = None
    problems: list[Any] | None = None
    ref_marker: str | None = Field(None, alias='refMarker')
    s_type: str | None = Field(None, alias='sType')
    signup_link: str | None = Field(None, alias='signupLink')

class Payload5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    payload_type: str | None = Field(None, alias='payloadType')
    transaction: Transaction2 | None = None
    subscription: Subscription2 | None = None

class Action4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    action_type: str | None = Field(None, alias='actionType')
    is_selected: bool | None = Field(None, alias='isSelected')
    payload: Payload5 | None = None
    presentation: Presentation3 | None = None

class ComponentPayload8(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    text_component: TextComponent4 | None = Field(None, alias='textComponent')

class TransactionDetail2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    component_payload: ComponentPayload8 | None = Field(None, alias='componentPayload')
    component_primitive: str | None = Field(None, alias='componentPrimitive')

class Tags5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    logo_entity_tag: str | None = Field(None, alias='LOGO_ENTITY_TAG')
    logo_height: str | None = Field(None, alias='LOGO_HEIGHT')
    logo_width: str | None = Field(None, alias='LOGO_WIDTH')

class LogoComponent2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    tags: Tags5 | None = None
    url: str | None = None

class ComponentPayload9(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    text_component: TextComponent4 | None = Field(None, alias='textComponent')
    logo_component: LogoComponent2 | None = Field(None, alias='logoComponent')

class Header1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    component_payload: ComponentPayload9 | None = Field(None, alias='componentPayload')
    component_primitive: str | None = Field(None, alias='componentPrimitive')

class Components2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    transaction_detail: TransactionDetail2 | None = Field(None, alias='TRANSACTION_DETAIL')
    header: Header1 | None = Field(None, alias='HEADER')

class ExpandingCard1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    actions: list[Action4] | None = None
    card_type: str | None = Field(None, alias='cardType')
    components: Components2 | None = None

class Transaction3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    asin: str | None = None
    csrf_token: str | None = Field(None, alias='csrfToken')
    csrf_token_workflow: str | None = Field(None, alias='csrfTokenWorkflow')
    display_messages: list[Any] | None = Field(None, alias='displayMessages')
    label: str | None = None
    offer_token: str | None = Field(None, alias='offerToken')
    purchase_data: PurchaseData | None = Field(None, alias='purchaseData')
    ref_marker: str | None = Field(None, alias='refMarker')

class Subscription3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    app_fallback_url: str | None = Field(None, alias='appFallbackUrl')
    app_subscription_url: str | None = Field(None, alias='appSubscriptionUrl')
    benefit_id: str | None = Field(None, alias='benefitId')
    display_messages: list[Any] | None = Field(None, alias='displayMessages')
    label: str | None = None
    problems: list[Any] | None = None
    ref_marker: str | None = Field(None, alias='refMarker')
    s_type: str | None = Field(None, alias='sType')
    signup_link: str | None = Field(None, alias='signupLink')

class Payload6(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    payload_type: str | None = Field(None, alias='payloadType')
    transaction: Transaction3 | None = None
    subscription: Subscription3 | None = None

class Action5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    action_type: str | None = Field(None, alias='actionType')
    is_selected: bool | None = Field(None, alias='isSelected')
    payload: Payload6 | None = None
    presentation: Presentation3 | None = None

class TextComponentCollection1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    text_list: list[TextListItem] | None = Field(None, alias='textList')

class ComponentPayload10(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    text_component_collection: TextComponentCollection1 | None = Field(None, alias='textComponentCollection')

class TransactionDetail3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    component_payload: ComponentPayload10 | None = Field(None, alias='componentPayload')
    component_primitive: str | None = Field(None, alias='componentPrimitive')

class Tags6(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    brand_glow: str | None = Field(None, alias='BRAND_GLOW')
    text_theme: str | None = Field(None, alias='TEXT_THEME')

class TextComponent7(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    tags: Tags6 | None = None
    text: str | None = None
    text_type: str | None = Field(None, alias='textType')

class Tags7(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    brand_glow: str | None = Field(None, alias='BRAND_GLOW')
    logo_entity_tag: str | None = Field(None, alias='LOGO_ENTITY_TAG')
    logo_height: str | None = Field(None, alias='LOGO_HEIGHT')
    logo_width: str | None = Field(None, alias='LOGO_WIDTH')

class LogoComponent3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    tags: Tags7 | None = None
    url: str | None = None

class ComponentPayload11(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    text_component: TextComponent7 | None = Field(None, alias='textComponent')
    logo_component: LogoComponent3 | None = Field(None, alias='logoComponent')

class Banner2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    component_payload: ComponentPayload11 | None = Field(None, alias='componentPayload')
    component_primitive: str | None = Field(None, alias='componentPrimitive')

class TextComponent8(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    tags: dict[str, Any] | None = None
    text: str | None = None
    text_type: str | None = Field(None, alias='textType')

class Tags8(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    alt_text: str | None = Field(None, alias='ALT_TEXT')

class ImageListItem1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    tags: Tags8 | None = None
    url: str | None = None

class ImageListComponent1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    image_list: list[ImageListItem1] | None = Field(None, alias='imageList')

class ComponentPayload13(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    text_component: TextComponent8 | None = Field(None, alias='textComponent')
    image_list_component: ImageListComponent1 | None = Field(None, alias='imageListComponent')

class ComponentListItem1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    component_payload: ComponentPayload13 | None = Field(None, alias='componentPayload')
    component_primitive: str | None = Field(None, alias='componentPrimitive')

class MixedComponent1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    component_list: list[ComponentListItem1] | None = Field(None, alias='componentList')

class ComponentPayload12(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    mixed_component: MixedComponent1 | None = Field(None, alias='mixedComponent')

class RelatedBenefits1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    component_payload: ComponentPayload12 | None = Field(None, alias='componentPayload')
    component_primitive: str | None = Field(None, alias='componentPrimitive')

class Components3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    transaction_detail: TransactionDetail3 | None = Field(None, alias='TRANSACTION_DETAIL')
    banner: Banner2 | None = Field(None, alias='BANNER')
    related_benefits: RelatedBenefits1 | None = Field(None, alias='RELATED_BENEFITS')

class CardOption1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    actions: list[Action5] | None = None
    card_type: str | None = Field(None, alias='cardType')
    components: Components3 | None = None

class Playback2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    benefit_id: str | None = Field(None, alias='benefitId')
    correlation_id: str | None = Field(None, alias='correlationId')
    expiry_time: int | None = Field(None, alias='expiryTime')
    fallback_url: str | None = Field(None, alias='fallbackURL')
    is_trailer: bool | None = Field(None, alias='isTrailer')
    label: str | None = None
    minutes_remaining: int | None = Field(None, alias='minutesRemaining')
    playback_envelope: str | None = Field(None, alias='playbackEnvelope')
    playback_id: str | None = Field(None, alias='playbackID')
    playback_status: str | None = Field(None, alias='playbackStatus')
    playback_url: str | None = Field(None, alias='playbackURL')
    player_ref_marker: str | None = Field(None, alias='playerRefMarker')
    player_ui_spec: str | None = Field(None, alias='playerUISpec')
    ref_marker: str | None = Field(None, alias='refMarker')
    resume_time: int | None = Field(None, alias='resumeTime')
    run_time: int | None = Field(None, alias='runTime')
    video_material_type: str | None = Field(None, alias='videoMaterialType')

class Payload4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    expanding_card: ExpandingCard1 | None = Field(None, alias='expandingCard')
    payload_type: str | None = Field(None, alias='payloadType')
    card_options: list[CardOption1] | None = Field(None, alias='cardOptions')
    playback: Playback2 | None = None

class Presentation6(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    primary_label: str | None = Field(None, alias='primaryLabel')
    ref_marker: str | None = Field(None, alias='refMarker')
    icon: str | None = None

class PrimaryAction1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    action_type: str | None = Field(None, alias='actionType')
    is_selected: bool | None = Field(None, alias='isSelected')
    payload: Payload4 | None = None
    presentation: Presentation6 | None = None

class Btf2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    messages: Messages1 | None = None
    primary_actions: list[PrimaryAction1] | None = Field(None, alias='primaryActions')
    secondary_actions: list[Any] | None = Field(None, alias='secondaryActions')
    view_ref_marker: str | None = Field(None, alias='viewRefMarker')

class Action3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    btf: dict[str, Btf2] | None = None
    atf: dict[str, Any] | None = None

class Banner3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    crow: dict[str, Any] | None = None
    ui: Any | None = None

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

class EpisodeList(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    header: str | None = None
    total_card_size: int | None = Field(None, alias='totalCardSize')
    card_title_ids: list[str] | None = Field(None, alias='cardTitleIds')
    actions: Actions | None = None

class CustomerReviewsText(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    attrs: dict[str, Any] | None = None
    string: str | None = None

class CustomerReviews(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    count: int | None = None
    count_formatted: str | None = Field(None, alias='countFormatted')
    customer_reviews_text: CustomerReviewsText | None = Field(None, alias='customerReviewsText')
    link: str | None = None
    value: int | float | None = None

class FocusMessage2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    icon: str | None = None
    message: str | None = None

class GlanceMessage(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    icon: str | None = None
    message: str | None = None

class HighValueMessage1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    icon: str | None = None
    message: str | None = None

class ProviderLogo1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    image_url: str | None = Field(None, alias='imageUrl')
    logo_scalar_horizontal: str | None = Field(None, alias='logoScalarHorizontal')
    message: str | None = None
    logo_scalar_stacked: str | None = Field(None, alias='logoScalarStacked')

class TitleMetadataBadge1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    entry_type: str | None = Field(None, alias='entryType')
    level: str | None = None
    message: str | None = None

class EntitlementCues(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    buybox_message: dict[str, Any] | None = Field(None, alias='buyboxMessage')
    compact_focus_message: dict[str, Any] | None = Field(None, alias='compactFocusMessage')
    content_source_logo: dict[str, Any] | None = Field(None, alias='contentSourceLogo')
    entitlement_type: str | None = Field(None, alias='entitlementType')
    focus_message: FocusMessage2 | None = Field(None, alias='focusMessage')
    glance_message: GlanceMessage | None = Field(None, alias='glanceMessage')
    high_value_message: HighValueMessage1 | None = Field(None, alias='highValueMessage')
    high_value_messages: list[Any] | None = Field(None, alias='highValueMessages')
    informational_message: dict[str, Any] | None = Field(None, alias='informationalMessage')
    informational_messages: list[Any] | None = Field(None, alias='informationalMessages')
    product_promotion_message: dict[str, Any] | None = Field(None, alias='productPromotionMessage')
    product_summary_message: dict[str, Any] | None = Field(None, alias='productSummaryMessage')
    provider_logo: ProviderLogo1 | None = Field(None, alias='providerLogo')
    title_metadata_badge: TitleMetadataBadge1 | None = Field(None, alias='titleMetadataBadge')

class HoverInfo(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    can_hover: bool | None = Field(None, alias='canHover')

class Cover(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | None = None

class Hero(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | None = None

class Poster2x3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | None = None

class TitleLogo(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | None = None

class Images3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    cover: Cover | None = None
    hero: Hero | None = None
    poster2x3: Poster2x3 | None = None
    title_logo: TitleLogo | None = Field(None, alias='titleLogo')

class ItemAnalytics(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    ref_marker: str | None = Field(None, alias='refMarker')

class Link1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    analytics: dict[str, Any] | None = None
    metadata: dict[str, Any] | None = None
    url: str | None = None

class MaturityRatingBadge(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__type: str | None = Field(None, alias='__type')
    description: str | None = None
    display_text: str | None = Field(None, alias='displayText')
    id: str | None = None
    country_code: str | None = Field(None, alias='countryCode')

class Endpoint1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    partial_url: str | None = Field(None, alias='partialURL')
    query: Query | None = None

class Action6(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    ajax_enabled: bool | None = Field(None, alias='ajaxEnabled')
    endpoint: Endpoint1 | None = None
    format_code: str | None = Field(None, alias='formatCode')
    tag: str | None = None
    text: Text | None = None

class Item(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__type: str | None = Field(None, alias='__type')
    action: Action6 | None = None
    item_type: str | None = Field(None, alias='itemType')
    text: str | None = None

class OverflowMenu(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    items: list[Item] | None = None
    title: str | None = None

class Endpoint2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    partial_url: str | None = Field(None, alias='partialURL')
    query: Query | None = None

class WatchlistAction(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    ajax_enabled: bool | None = Field(None, alias='ajaxEnabled')
    endpoint: Endpoint2 | None = None
    format_code: str | None = Field(None, alias='formatCode')
    tag: str | None = None
    text: Text | None = None

class CategorizedGenres(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    primary_genre: str | None = Field(None, alias='primaryGenre')
    secondary_genres: list[str] | None = Field(None, alias='secondaryGenres')

class Entity(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    buy_box_actions: list[Any] | None = Field(None, alias='buyBoxActions')
    customer_reviews: CustomerReviews | None = Field(None, alias='customerReviews')
    degradations: list[Any] | None = None
    display_title: str | None = Field(None, alias='displayTitle')
    entitlement_cues: EntitlementCues | None = Field(None, alias='entitlementCues')
    entity_type: str | None = Field(None, alias='entityType')
    hover_info: HoverInfo | None = Field(None, alias='hoverInfo')
    images: Images3 | None = None
    impression_id: str | None = Field(None, alias='impressionId')
    is_closed_caption: bool | None = Field(None, alias='isClosedCaption')
    item_analytics: ItemAnalytics | None = Field(None, alias='itemAnalytics')
    link: Link1 | None = None
    maturity_rating_badge: MaturityRatingBadge | None = Field(None, alias='maturityRatingBadge')
    overflow_menu: OverflowMenu | None = Field(None, alias='overflowMenu')
    playback_actions: list[Any] | None = Field(None, alias='playbackActions')
    ref_marker: str | None = Field(None, alias='refMarker')
    release_year: str | None = Field(None, alias='releaseYear')
    synopsis: str | None = None
    title: str | None = None
    title_id: str | None = Field(None, alias='titleID')
    watchlist_action: WatchlistAction | None = Field(None, alias='watchlistAction')
    widget_type: str | None = Field(None, alias='widgetType')
    runtime: str | None = None
    categorized_genres: CategorizedGenres | None = Field(None, alias='categorizedGenres')

class EntitlementCues1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    entitled_carousel: str | None = Field(None, alias='entitledCarousel')
    offer_type: str | None = Field(None, alias='offerType')

class Container(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    container_type: str | None = Field(None, alias='containerType')
    entities: list[Entity] | None = None
    entitlement_cues: EntitlementCues1 | None = Field(None, alias='entitlementCues')
    estimated_total: int | None = Field(None, alias='estimatedTotal')
    impression_data: str | None = Field(None, alias='impressionData')
    inline_container_update_actions: list[Any] | None = Field(None, alias='inlineContainerUpdateActions')
    is_continue_watching: bool | None = Field(None, alias='isContinueWatching')
    journey_ingress_context: str | None = Field(None, alias='journeyIngressContext')
    pagination_service_token: str | None = Field(None, alias='paginationServiceToken')
    pagination_start_index: int | None = Field(None, alias='paginationStartIndex')
    pagination_target_id: str | None = Field(None, alias='paginationTargetId')
    strings: dict[str, Any] | None = None
    text: str | None = None
    title: str | None = None
    web_uid: str | None = Field(None, alias='webUid')
    not_expandable: bool | None = Field(None, alias='notExpandable')

class Action7(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    format: str | None = None
    link: str | None = None
    text: Text | None = None
    title_id: str | None = Field(None, alias='titleID')

class OtherFormats(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    actions: list[Action7] | None = None

class Features3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    activate_auto_playing_in_hovers: str | None = Field(None, alias='activateAutoPlayingInHovers')
    offer_clarity_enabled: str | None = Field(None, alias='offerClarityEnabled')
    is_reviews_submission_enabled: str | None = Field(None, alias='isReviewsSubmissionEnabled')
    disable_hover: str | None = Field(None, alias='disableHover')
    is_autoplay_setting_enabled: str | None = Field(None, alias='isAutoplaySettingEnabled')
    is_record_season_enabled: str | None = Field(None, alias='isRecordSeasonEnabled')
    is_detail_page_header_widget_enabled: str | None = Field(None, alias='isDetailPageHeaderWidgetEnabled')
    disable_player_for_google_bot: str | None = Field(None, alias='disablePlayerForGoogleBot')
    disable_whisper_cache_in_draper: str | None = Field(None, alias='disableWhisperCacheInDraper')
    is_detail_page_header_widget_refresh_enabled: str | None = Field(None, alias='isDetailPageHeaderWidgetRefreshEnabled')
    panorama_treatment: str | None = Field(None, alias='panoramaTreatment')
    disable_enrich_item_metadata: str | None = Field(None, alias='disableEnrichItemMetadata')
    disable_marin_tracking: str | None = Field(None, alias='disableMarinTracking')
    is_stream_selector_modal_enabled: str | None = Field(None, alias='isStreamSelectorModalEnabled')
    is_swm_enabled: str | None = Field(None, alias='isSWMEnabled')
    is_spider_noir: str | None = Field(None, alias='isSpiderNoir')
    disable_explore_tab: str | None = Field(None, alias='disableExploreTab')

class Btf3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    decoration_scheme: str | None = Field(None, alias='decorationScheme')
    dynamic_features: list[str] | None = Field(None, alias='dynamicFeatures')
    feature_scheme: str | None = Field(None, alias='featureScheme')
    widget_scheme: str | None = Field(None, alias='widgetScheme')

class Atf3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    decoration_scheme: str | None = Field(None, alias='decorationScheme')
    dynamic_features: list[str] | None = Field(None, alias='dynamicFeatures')
    feature_scheme: str | None = Field(None, alias='featureScheme')
    widget_scheme: str | None = Field(None, alias='widgetScheme')

class SwiftParameters1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    btf: Btf3 | None = Field(None, alias='BTF')
    atf: Atf3 | None = Field(None, alias='ATF')

class PageContext1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    app: str | None = None
    download_launch_type: str | None = Field(None, alias='downloadLaunchType')
    enable_hover: bool | None = Field(None, alias='enableHover')
    features: Features3 | None = None
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
    sub_page_type: str | None = Field(None, alias='subPageType')
    swift_parameters: SwiftParameters1 | None = Field(None, alias='swiftParameters')

class Metadata2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    content_descriptors: list[str] | None = Field(None, alias='contentDescriptors')
    content_warnings: list[str] | None = Field(None, alias='contentWarnings')
    maturity_rating: MaturityRating | None = Field(None, alias='maturityRating')
    traits: list[Any] | None = None

class Attrs4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: Url | None = None

class TermsText1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    attrs: Attrs4 | None = None
    string: str | None = None

class Attrs5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: Url | None = None

class HelpText1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    attrs: Attrs5 | None = None
    string: str | None = None

class BottomMenu(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    feedback_sign_in_url: str | None = Field(None, alias='feedbackSignInUrl')
    help_text: HelpText1 | None = Field(None, alias='helpText')

class State1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    features: Features2 | None = None
    page_title_id: str | None = Field(None, alias='pageTitleId')
    detail: Detail1 | None = None
    action: Action3 | None = None
    refund: Refund | None = None
    imdb: dict[str, Any] | None = None
    buy_box: dict[str, Any] | None = Field(None, alias='buyBox')
    buybox_title_id: dict[str, Any] | None = Field(None, alias='buyboxTitleId')
    creative: dict[str, Any] | None = None
    banner: Banner3 | None = None
    age_verification_banner: dict[str, Any] | None = Field(None, alias='ageVerificationBanner')
    notification: dict[str, Any] | None = None
    seasons: dict[str, Any] | None = None
    self: dict[str, Self] | None = None
    watchlist: dict[str, Any] | None = None
    restriction: dict[str, Any] | None = None
    extras: dict[str, Any] | None = None
    tokens: dict[str, Any] | None = None
    page_link: dict[str, Any] | None = Field(None, alias='pageLink')
    episode_list: EpisodeList | None = Field(None, alias='episodeList')
    containers: dict[str, list[Container]] | None = None
    recordings: dict[str, Any] | None = None
    bundles_content: dict[str, Any] | None = Field(None, alias='bundlesContent')
    other_formats: dict[str, OtherFormats] | None = Field(None, alias='otherFormats')
    page_context: PageContext1 | None = Field(None, alias='pageContext')
    autoplay_hero: dict[str, Any] | None = Field(None, alias='autoplayHero')
    autoplay_trailer_hero: dict[str, Any] | None = Field(None, alias='autoplayTrailerHero')
    playback_integration: dict[str, Any] | None = Field(None, alias='playbackIntegration')
    coming_soon: dict[str, Any] | None = Field(None, alias='comingSoon')
    metadata: dict[str, Metadata2] | None = None
    widgets: dict[str, dict[str, Any]] | None = None
    terms_text: TermsText1 | None = Field(None, alias='termsText')
    bottom_menu: BottomMenu | None = Field(None, alias='bottomMenu')
    recording_metadata: dict[str, Any] | None = Field(None, alias='recordingMetadata')

class Strings1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    dv_cr_review_submission_failure: str | None = Field(None, alias='DV_CR_review_submission_failure')
    dv_web_one_season: str | None = Field(None, alias='DV_WEB_ONE_SEASON')
    dv_web_dp_eu_cancel_accidental_purchase: str | None = Field(None, alias='DV_WEB_DP_EU_CANCEL_ACCIDENTAL_PURCHASE')
    dv_web_aria_previous_title: str | None = Field(None, alias='DV_WEB_ARIA_PREVIOUS_TITLE')
    dv_web_watchlist_tooltip: str | None = Field(None, alias='DV_WEB_WATCHLIST_TOOLTIP')
    dv_comma_separator: str | None = Field(None, alias='DV_comma_separator')
    dv_dp_tab_related: str | None = Field(None, alias='DV_DP_TAB_related')
    dv_web_sports_record_success_upcoming: str | None = Field(None, alias='DV_WEB_SPORTS_RECORD_SUCCESS_UPCOMING')
    dv_dp_aria_audio_description: str | None = Field(None, alias='DV_DP_ARIA_audio_description')
    dv_dp_dv_gcpc_window_title: str | None = Field(None, alias='DV_DP_DV_GCPC_window_title')
    dv_web_dp_eu_cancel_purch_modal_submit: str | None = Field(None, alias='DV_WEB_DP_EU_CANCEL_PURCH_MODAL_SUBMIT')
    dv_cr_reviews_explanation_header: str | None = Field(None, alias='DV_CR_reviews_explanation_header')
    dv_web_sports_record_success_ended: str | None = Field(None, alias='DV_WEB_SPORTS_RECORD_SUCCESS_ENDED')
    dv_dp_aria_hdr10_plus: str | None = Field(None, alias='DV_DP_ARIA_hdr10_plus')
    dv_dp_you_multiple_orders_for_this_title: str | None = Field(None, alias='DV_DP_you_multiple_orders_for_this_title')
    dv_web_sports_record_league_success_ended: str | None = Field(None, alias='DV_WEB_SPORTS_RECORD_LEAGUE_SUCCESS_ENDED')
    dv_ab_cancel_accidental_purchase: str | None = Field(None, alias='DV_AB_CANCEL_ACCIDENTAL_PURCHASE')
    dv_web_watchlist_add: str | None = Field(None, alias='DV_WEB_WATCHLIST_ADD')
    dv_web_feedback_select_option_dropdown_menu: str | None = Field(None, alias='DV_WEB_FEEDBACK_select_option_dropdown_menu')
    dv_cr_write_review_label_other: str | None = Field(None, alias='DV_CR_write_review_label_other')
    dv_dp_gc_balance_update_failed: str | None = Field(None, alias='DV_DP_GC_balance_update_failed')
    avod_dp_gc_promotion_message: str | None = Field(None, alias='AVOD_DP_GC_promotion_message')
    dv_web_linear_program_record_start_success: str | None = Field(None, alias='DV_WEB_LINEAR_PROGRAM_RECORD_START_SUCCESS')
    dv_dp_help_support: str | None = Field(None, alias='DV_DP_Help_Support')
    dv_tw_title_genres: str | None = Field(None, alias='DV_TW_title_genres')
    dv_web_recording_scheduled: str | None = Field(None, alias='DV_WEB_RECORDING_SCHEDULED')
    dv_web_dp_eu_choose_order_to_cancel: str | None = Field(None, alias='DV_WEB_DP_EU_choose_order_to_cancel')
    dv_dp_el_bonus_title_template: str | None = Field(None, alias='DV_DP_EL_bonus_title_template')
    dv_dp_none_available: str | None = Field(None, alias='DV_DP_none_available')
    dv_dp_aria_dolby_atmos: str | None = Field(None, alias='DV_DP_ARIA_dolby_atmos')
    dv_dp_cl_other_formats_title: str | None = Field(None, alias='DV_DP_CL_other_formats_title')
    dv_dp_aria_release_year: str | None = Field(None, alias='DV_DP_ARIA_release_year')
    dv_web_recording_now: str | None = Field(None, alias='DV_WEB_RECORDING_NOW')
    avod_dp_e_error_ok: str | None = Field(None, alias='AVOD_DP_E_error_ok')
    dv_web_sports_cancel_record_league_success: str | None = Field(None, alias='DV_WEB_SPORTS_CANCEL_RECORD_LEAGUE_SUCCESS')
    dv_tw_title_producers: str | None = Field(None, alias='DV_TW_title_producers')
    dv_dp_aria_alt_star_rating: str | None = Field(None, alias='DV_DP_ARIA_alt_star_rating')
    dv_web_feedback_dropdown_prompt: str | None = Field(None, alias='DV_WEB_FEEDBACK_dropdown_prompt')
    dv_dp_ub_gc_popup_apply: str | None = Field(None, alias='DV_DP_UB_GC_popup_apply')
    dv_web_aria_next_n_titles: str | None = Field(None, alias='DV_WEB_ARIA_NEXT_N_TITLES')
    dv_dp_aria_watch_title: str | None = Field(None, alias='DV_DP_ARIA_watch_title')
    dv_cr_read_reviews_label: str | None = Field(None, alias='DV_CR_read_reviews_label')
    dv_dp_aria_dolby_vision: str | None = Field(None, alias='DV_DP_ARIA_dolby_vision')
    dv_web_more_details: str | None = Field(None, alias='DV_WEB_MORE_DETAILS')
    dv_tw_title_studio: str | None = Field(None, alias='DV_TW_title_studio')
    dv_dp_tab_details: str | None = Field(None, alias='DV_DP_TAB_details')
    dv_web_linear_program_record_error: str | None = Field(None, alias='DV_WEB_LINEAR_PROGRAM_RECORD_ERROR')
    avod_dp_episode_title: str | None = Field(None, alias='AVOD_DP_episode_title')
    dv_web_aria_previous_n_titles: str | None = Field(None, alias='DV_WEB_ARIA_PREVIOUS_N_TITLES')
    dv_dp_aria_dolby_51: str | None = Field(None, alias='DV_DP_ARIA_dolby_51')
    dv_web_dp_eu_cancel_purch_modal_header: str | None = Field(None, alias='DV_WEB_DP_EU_CANCEL_PURCH_MODAL_HEADER')
    dv_dp_gc_widget_heading: str | None = Field(None, alias='DV_DP_GC_widget_heading')
    dv_tw_title_languages: str | None = Field(None, alias='DV_TW_title_languages')
    avod_dp_e_error_text: str | None = Field(None, alias='AVOD_DP_E_error_text')
    dv_web_overflow_menu_tooltip: str | None = Field(None, alias='DV_WEB_OVERFLOW_MENU_TOOLTIP')
    dv_rbb_cancel_purch_modal_submit: str | None = Field(None, alias='DV_RBB_CANCEL_PURCH_MODAL_SUBMIT')
    dv_tw_title_content_descriptors: str | None = Field(None, alias='DV_TW_title_content_descriptors')
    dv_web_feedback_submit_button: str | None = Field(None, alias='DV_WEB_FEEDBACK_submit_button')
    dv_cr_reviews_explanation_text: str | None = Field(None, alias='DV_CR_reviews_explanation_text')
    dv_mwtw_title_main: str | None = Field(None, alias='DV_MWTW_TITLE_MAIN')
    dv_tw_title_subtitles: str | None = Field(None, alias='DV_TW_title_subtitles')
    dv_dp_aria_star_rating: str | None = Field(None, alias='DV_DP_ARIA_star_rating')
    dv_cr_reviews_header: str | None = Field(None, alias='DV_CR_reviews_header')
    dv_web_feedback_your_devices: str | None = Field(None, alias='DV_WEB_FEEDBACK_your_devices')
    dv_dot_separator: str | None = Field(None, alias='DV_dot_separator')
    dv_tw_title_directors: str | None = Field(None, alias='DV_TW_title_directors')
    dv_dp_aria_next_tab: str | None = Field(None, alias='DV_DP_ARIA_next_tab')
    dv_dp_minutes_remaining: str | None = Field(None, alias='DV_DP_minutes_remaining')
    dv_aw_purchase_options: str | None = Field(None, alias='DV_AW_PURCHASE_OPTIONS')
    dv_mwtw_title: str | None = Field(None, alias='DV_MWTW_TITLE')
    dv_rbb_cancel_purch_modal_header: str | None = Field(None, alias='DV_RBB_CANCEL_PURCH_MODAL_HEADER')
    avod_dp_gc_toc_learn_more: str | None = Field(None, alias='AVOD_DP_GC_toc_learn_more')
    dv_dp_tab_recordings: str | None = Field(None, alias='DV_DP_TAB_recordings')
    dv_web_sports_cancel_record_success: str | None = Field(None, alias='DV_WEB_SPORTS_CANCEL_RECORD_SUCCESS')
    dv_dp_gc_balance_type_heading: str | None = Field(None, alias='DV_DP_GC_balance_type_heading')
    dv_tw_title_cast: str | None = Field(None, alias='DV_TW_title_cast')
    dv_cr_write_review_label: str | None = Field(None, alias='DV_CR_write_review_label')
    dv_web_watchlist_csrf_problem: str | None = Field(None, alias='DV_WEB_WATCHLIST_CSRF_PROBLEM')
    dv_web_settings_head_subtitles: str | None = Field(None, alias='DV_WEB_SETTINGS_HEAD_SUBTITLES')
    dv_web_feedback_select_related_device: str | None = Field(None, alias='DV_WEB_FEEDBACK_select_related_device')
    dv_dp_aria_pse_badge: str | None = Field(None, alias='DV_DP_ARIA_pse_badge')
    dv_web_details_tooltip: str | None = Field(None, alias='DV_WEB_DETAILS_TOOLTIP')
    dv_web_sports_record: str | None = Field(None, alias='DV_WEB_SPORTS_RECORD')
    dv_web_seasons_count: str | None = Field(None, alias='DV_WEB_SEASONS_COUNT')
    dv_dp_aria_imdb_rating: str | None = Field(None, alias='DV_DP_ARIA_imdb_rating')
    dv_dp_episode_sort: str | None = Field(None, alias='DV_DP_EPISODE_SORT')
    avod_dp_redeem_gift_card_or_promotion: str | None = Field(None, alias='AVOD_DP_redeem_gift_card_or_promotion')
    dv_dp_ub_gc_success_message: str | None = Field(None, alias='DV_DP_UB_GC_success_message')
    dv_web_watchlist_remove: str | None = Field(None, alias='DV_WEB_WATCHLIST_REMOVE')
    dv_dp_aria_suitable_for: str | None = Field(None, alias='DV_DP_ARIA_suitable_for')
    dv_tw_title_cast_and_creators: str | None = Field(None, alias='DV_TW_title_cast_and_creators')
    dv_web_recording_indicator: str | None = Field(None, alias='DV_WEB_RECORDING_INDICATOR')
    dv_dp_gc_balances_explanation: str | None = Field(None, alias='DV_DP_GC_balances_explanation')
    dv_dp_gc_wrong_code: str | None = Field(None, alias='DV_DP_GC_wrong_code')
    dv_web_feedback_feedback: str | None = Field(None, alias='DV_WEB_FEEDBACK_feedback')
    dv_dp_choose_order_to_cancel: str | None = Field(None, alias='DV_DP_choose_order_to_cancel')
    dv_web_linear_program_record_cancel_success: str | None = Field(None, alias='DV_WEB_LINEAR_PROGRAM_RECORD_CANCEL_SUCCESS')
    dv_dp_aria_regulatory_rating: str | None = Field(None, alias='DV_DP_ARIA_regulatory_rating')
    dv_dp_ub_gc_enter_code: str | None = Field(None, alias='DV_DP_UB_GC_enter_code')
    dv_dp_tab_explore: str | None = Field(None, alias='DV_DP_TAB_explore')
    dv_dp_episode_range_selector: str | None = Field(None, alias='DV_DP_EPISODE_RANGE_SELECTOR')
    dv_dp_tab_extras: str | None = Field(None, alias='DV_DP_TAB_extras')
    dv_dp_gc_code_input_placeholder: str | None = Field(None, alias='DV_DP_GC_code_input_placeholder')
    dv_dp_gc_balance_amount_heading: str | None = Field(None, alias='DV_DP_GC_balance_amount_heading')
    dv_web_sports_record_league_success_upcoming: str | None = Field(None, alias='DV_WEB_SPORTS_RECORD_LEAGUE_SUCCESS_UPCOMING')
    dv_web_feedback_no_device_website: str | None = Field(None, alias='DV_WEB_FEEDBACK_no_device_website')
    dv_dp_el_episode_title: str | None = Field(None, alias='DV_DP_EL_episode_title')
    dv_tw_amr_nr_text: str | None = Field(None, alias='DV_TW_amr_nr_text')
    dv_web_feedback__send_us_feedback: str | None = Field(None, alias='DV_WEB_FEEDBACK__send_us_feedback')
    dv_brand_av: str | None = Field(None, alias='DV_brand_av')
    dv_dp_tab_episodes: str | None = Field(None, alias='DV_DP_TAB_episodes')
    dv_dp_aria_runtime: str | None = Field(None, alias='DV_DP_ARIA_runtime')
    dv_web_aria_next_title: str | None = Field(None, alias='DV_WEB_ARIA_NEXT_TITLE')
    dv_dp_more_info: str | None = Field(None, alias='DV_DP_more_info')
    dv_web_sports_cancel_record: str | None = Field(None, alias='DV_WEB_SPORTS_CANCEL_RECORD')

class Btf1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    home_region: str | None = Field(None, alias='homeRegion')
    state: State1 | None = None
    strings: Strings1 | None = None

class CustomerState(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_robotic: bool | None = Field(None, alias='isRobotic')

class FeatureSwitches(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    show_floating_join_prime_button: bool | None = Field(None, alias='showFloatingJoinPrimeButton')

class Metadata3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability: Availability | None = None

class Image1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    alt_text: str | None = Field(None, alias='altText')
    url: str | None = None

class Branding(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    image: Image1 | None = None
    label: str | None = None
    ref_marker: str | None = Field(None, alias='refMarker')
    url: str | None = None

class NavSection(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    desktop: str | None = None
    mobile: str | None = None

class SubNode(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__type: str | None = Field(None, alias='__type')
    id: str | None = None
    label: str | None = None
    ref_marker: str | None = Field(None, alias='refMarker')
    url: str | None = None

class SubMenuItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    id: str | None = None
    sub_nodes: list[SubNode] | None = Field(None, alias='subNodes')
    label: str | None = None

class NavigationNode(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__type: str | None = Field(None, alias='__type')
    id: str | None = None
    label: str | None = None
    nav_section: NavSection | None = Field(None, alias='navSection')
    ref_marker: str | None = Field(None, alias='refMarker')
    sub_menu: list[SubMenuItem] | None = Field(None, alias='subMenu')
    url: str | None = None
    coachmark_text: str | None = Field(None, alias='coachmarkText')
    enrich_nav: str | None = Field(None, alias='enrichNav')
    icon: str | None = None

class Query3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    ie: str | None = None
    ref_: str | None = None

class SubmitSearchDestructuredEndpoint(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    partial_url: str | None = Field(None, alias='partialURL')
    query: Query3 | None = None

class SearchBar(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    clear_search_label: str | None = Field(None, alias='clearSearchLabel')
    close_search_alt_text: str | None = Field(None, alias='closeSearchAltText')
    is_search_suggestions_disabled: bool | None = Field(None, alias='isSearchSuggestionsDisabled')
    is_search_suggestions_enhanced: bool | None = Field(None, alias='isSearchSuggestionsEnhanced')
    search_bar_placeholder_label: str | None = Field(None, alias='searchBarPlaceholderLabel')
    search_icon_alt_text: str | None = Field(None, alias='searchIconAltText')
    submit_search_destructured_endpoint: SubmitSearchDestructuredEndpoint | None = Field(None, alias='submitSearchDestructuredEndpoint')
    submit_search_endpoint: str | None = Field(None, alias='submitSearchEndpoint')

class Nav(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    aria_label: str | None = Field(None, alias='ariaLabel')
    branding: Branding | None = None
    collapsed_nav_browse_label: str | None = Field(None, alias='collapsedNavBrowseLabel')
    label: str | None = None
    navigation_nodes: list[NavigationNode] | None = Field(None, alias='navigationNodes')
    search_bar: SearchBar | None = Field(None, alias='searchBar')

class SitewideNavigationBar1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    customer_state: CustomerState | None = Field(None, alias='customerState')
    feature_switches: FeatureSwitches | None = Field(None, alias='featureSwitches')
    is_sticky: bool | None = Field(None, alias='isSticky')
    metadata: Metadata3 | None = None
    nav: Nav | None = None
    hz_page_type: str | None = Field(None, alias='hzPageType')
    hz_sub_page_type: str | None = Field(None, alias='hzSubPageType')
    is_roadblocked: bool | None = Field(None, alias='isRoadblocked')

class SitewideInlineScriptsTop1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    hide_footer_gap: bool | None = Field(None, alias='hideFooterGap')

class SitewideInlineScriptsBottom1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    hide_footer_gap: bool | None = Field(None, alias='hideFooterGap')

class Metadata4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability: Availability | None = None

class SitewideConditional(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    degradations: list[Any] | None = None
    features: dict[str, Any] | None = None
    metadata: Metadata4 | None = None
    page_type: str | None = Field(None, alias='pageType')
    sub_page_type: str | None = Field(None, alias='subPageType')
    privacy_prefs_csrf_token: str | None = Field(None, alias='privacyPrefsCsrfToken')

class SitewideAlexa(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    device_config_id: str | None = Field(None, alias='deviceConfigId')
    iframe_origin: str | None = Field(None, alias='iframeOrigin')

class Sitewide(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    sitewide_navigation_bar: SitewideNavigationBar1 | None = Field(None, alias='sitewide-navigation-bar')
    sitewide_inline_scripts_top: SitewideInlineScriptsTop1 | None = Field(None, alias='sitewide-inline-scripts-top')
    sitewide_inline_scripts_bottom: SitewideInlineScriptsBottom1 | None = Field(None, alias='sitewide-inline-scripts-bottom')
    sitewide_conditional: SitewideConditional | None = Field(None, alias='sitewide-conditional')
    sitewide_alexa: SitewideAlexa | None = Field(None, alias='sitewide-alexa')

class Body(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    routing_type: str | None = Field(None, alias='routingType')
    page_classes: list[str] | None = Field(None, alias='pageClasses')
    pangaea_banner: PangaeaBanner | None = Field(None, alias='pangaeaBanner')
    atf: Atf | None = None
    btf: Btf1 | None = None
    sitewide: Sitewide | None = None

class QueryParameters(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    dv_web_app_client_version: list[str] | None = Field(None, alias='dvWebAppClientVersion')

class Contingencies(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_testing: bool | None = Field(None, alias='isTesting')
    values: dict[str, Any] | None = None

class RequestContext(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    customer_id: Any | None = Field(None, alias='customerID')
    user_agent: str | None = Field(None, alias='userAgent')
    is_internal: bool | None = Field(None, alias='isInternal')
    path: str | None = None
    query_parameters: QueryParameters | None = Field(None, alias='queryParameters')
    request_id: str | None = Field(None, alias='requestID')
    session_id: str | None = Field(None, alias='sessionID')
    traffic_policies: str | None = Field(None, alias='trafficPolicies')
    domain: str | None = None
    marketplace_id: str | None = Field(None, alias='marketplaceID')
    customer_ip_address: IPv4Address | None = Field(None, alias='customerIPAddress')
    original_uri: str | None = Field(None, alias='originalURI')
    os_locale: str | None = Field(None, alias='osLocale')
    record_territory: str | None = Field(None, alias='recordTerritory')
    current_territory: str | None = Field(None, alias='currentTerritory')
    geo_token: str | None = Field(None, alias='geoToken')
    cookie_timezone: Any | None = Field(None, alias='cookieTimezone')
    app_name: Any | None = Field(None, alias='appName')
    device_id: Any | None = Field(None, alias='deviceID')
    contingencies: Contingencies | None = None
    is_test: bool | None = Field(None, alias='isTest')
    mocks: Any | None = None
    service_overrides: Any | None = Field(None, alias='serviceOverrides')
    weblab_overrides: dict[str, Any] | None = Field(None, alias='weblabOverrides')
    server_name: str | None = Field(None, alias='serverName')
    resiliency_token: Any | None = Field(None, alias='resiliencyToken')
    is_locale_rtl: bool | None = Field(None, alias='isLocaleRTL')
    identity_context: str | None = Field(None, alias='identityContext')
    locale: str | None = None

class Weblab(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    weblab_name: str | None = Field(None, alias='weblabName')
    treatment_name: str | None = Field(None, alias='treatmentName')

class ClickstreamData(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    page_type: str | None = Field(None, alias='pageType')
    sub_page_type: str | None = Field(None, alias='subPageType')
    request_id: str | None = Field(None, alias='requestId')
    page_type_id: str | None = Field(None, alias='pageTypeId')
    ref_marker: Any | None = Field(None, alias='refMarker')
    action: Any | None = None
    hit_type: Any | None = Field(None, alias='hitType')
    a9_search_fields: Any | None = Field(None, alias='A9SearchFields')
    additional_data: Any | None = Field(None, alias='additionalData')
    weblabs: list[Weblab] | None = Field(None, alias='Weblabs')
    site_variant: str | None = Field(None, alias='siteVariant')

class Profile(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    age_group: str | None = Field(None, alias='ageGroup')
    is_child: bool | None = Field(None, alias='isChild')

class FeaturePivots(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    dv_web_feedback_widget_scheme_1382103: bool | None = Field(None, alias='DV_WEB_FEEDBACK_WIDGET_SCHEME_1382103')
    dv_web_linear_age_restriction_sign_in_explore_scheme_1445266: bool | None = Field(None, alias='DV_WEB_LINEAR_AGE_RESTRICTION_SIGN_IN_EXPLORE_SCHEME_1445266')
    is_agent_self_declaration_enabled: bool | None = Field(None, alias='isAgentSelfDeclarationEnabled')
    dv_web_scores_and_gameclock_1279604: bool | None = Field(None, alias='DV_WEB_SCORES_AND_GAMECLOCK_1279604')
    dv_web_dp_enable_drm_support_for_desktop_1437352: bool | None = Field(None, alias='DV_WEB_DP_ENABLE_DRM_SUPPORT_FOR_DESKTOP_1437352')
    dv_web_linear_vmvpd_explore_scheme_1407946: bool | None = Field(None, alias='DV_WEB_LINEAR_VMVPD_EXPLORE_SCHEME_1407946')
    dv_web_linear_search_1434133: bool | None = Field(None, alias='DV_WEB_LINEAR_SEARCH_1434133')
    is_crw_redesign_enabled: bool | None = Field(None, alias='isCrwRedesignEnabled')
    is_telemetry_sdk_migration_weblab_on: bool | None = Field(None, alias='isTelemetrySDKMigrationWeblabOn')
    is_deprecate_dcs_telemetry_weblab_on: bool | None = Field(None, alias='isDeprecateDCSTelemetryWeblabOn')
    dv_windows_app_pwa_back_to_legacy_1316821: bool | None = Field(None, alias='DV_WINDOWS_APP_PWA_BACK_TO_LEGACY_1316821')
    pv_web_sterling_sponsored_label_1438224: bool | None = Field(None, alias='PV_WEB_STERLING_SPONSORED_LABEL_1438224')
    dv_web_linear_station_taps_view_upgrade_1358041: bool | None = Field(None, alias='DV_WEB_LINEAR_STATION_TAPS_VIEW_UPGRADE_1358041')
    dv_web_tr_persist_1434722: bool | None = Field(None, alias='DV_WEB_TR_PERSIST_1434722')
    handshake_token: str | None = Field(None, alias='handshakeToken')
    dv_web_xiaomi_deeplink_with_https_1303012: bool | None = Field(None, alias='DV_WEB_XIAOMI_DEEPLINK_WITH_HTTPS_1303012')
    pause_refreshes_during_playback: bool | None = Field(None, alias='pauseRefreshesDuringPlayback')
    dv_web_linear_station_favoriting_1356611: bool | None = Field(None, alias='DV_WEB_LINEAR_STATION_FAVORITING_1356611')
    is_profile_age_restricted_enabled: bool | None = Field(None, alias='isProfileAgeRestrictedEnabled')
    is_page_load_clickstream_exp_weblab_on: bool | None = Field(None, alias='isPageLoadClickstreamExpWeblabOn')
    dv_web_service_worker_1293503: bool | None = Field(None, alias='DV_WEB_SERVICE_WORKER_1293503')
    pause_downloads_during_playback: bool | None = Field(None, alias='pauseDownloadsDuringPlayback')
    dv_web_dp_panorama_immersive_cx_autoplay_1222621: bool | None = Field(None, alias='DV_WEB_DP_PANORAMA_IMMERSIVE_CX_AUTOPLAY_1222621')
    super_draper_safari_minimum_bitrate: Any | None = Field(None, alias='superDraperSafariMinimumBitrate')
    is_seamless_expansion_enabled: bool | None = Field(None, alias='isSeamlessExpansionEnabled')
    dv_web_enable_pvcom_for_cmp_customers_signed_in_1405793: bool | None = Field(None, alias='DV_WEB_ENABLE_PVCOM_FOR_CMP_CUSTOMERS_SIGNED_IN_1405793')
    dv_web_ref_marker_as_query_param_1380642: bool | None = Field(None, alias='DV_WEB_REF_MARKER_AS_QUERY_PARAM_1380642')
    dv_web_fox_followup_1298275: bool | None = Field(None, alias='DV_WEB_FOX_FOLLOWUP_1298275')
    is_profile_level_parental_controls_enabled: bool | None = Field(None, alias='isProfileLevelParentalControlsEnabled')
    is_exposed_to_immersive_cx_experiment: bool | None = Field(None, alias='isExposedToImmersiveCXExperiment')
    dv_web_live_events_music_kahuna_1400248: str | None = Field(None, alias='DV_WEB_LIVE_EVENTS_MUSIC_KAHUNA_1400248')
    dv_web_dp_enable_whisper_cache_for_unrec_customers_1440503: bool | None = Field(None, alias='DV_WEB_DP_ENABLE_WHISPER_CACHE_FOR_UNREC_CUSTOMERS_1440503')
    telemetry_client_launch_web_treatment: str | None = Field(None, alias='telemetryClientLaunchWebTreatment')
    is_runway_post_transition_enabled: bool | None = Field(None, alias='isRunwayPostTransitionEnabled')
    dv_web_live_events_music_kahuna_test_1411910: bool | None = Field(None, alias='DV_WEB_LIVE_EVENTS_MUSIC_KAHUNA_TEST_1411910')
    is_less_aggressive_play_button_spinner: bool | None = Field(None, alias='isLessAggressivePlayButtonSpinner')
    dv_web_enable_pvcom_for_cmp_customers_1365035: bool | None = Field(None, alias='DV_WEB_ENABLE_PVCOM_FOR_CMP_CUSTOMERS_1365035')
    is_runway_transition_initiation_enabled: bool | None = Field(None, alias='isRunwayTransitionInitiationEnabled')
    pv_web_common_sense_media_kids_profile_1422829: bool | None = Field(None, alias='PV_WEB_COMMON_SENSE_MEDIA_KIDS_PROFILE_1422829')
    dv_web_dp_enable_drm_support_1433238: bool | None = Field(None, alias='DV_WEB_DP_ENABLE_DRM_SUPPORT_1433238')
    pv_linear_carousel_bearded_web_1433664: bool | None = Field(None, alias='PV_LINEAR_CAROUSEL_BEARDED_WEB_1433664')
    dv_web_live_autoplay_1290319: str | None = Field(None, alias='DV_WEB_LIVE_AUTOPLAY_1290319')
    dv_web_enable_linear_station_in_all_carousels_1272039: bool | None = Field(None, alias='DV_WEB_ENABLE_LINEAR_STATION_IN_ALL_CAROUSELS_1272039')
    dv_web_minidetails_expandable_synopsis_1336752: bool | None = Field(None, alias='DV_WEB_MINIDETAILS_EXPANDABLE_SYNOPSIS_1336752')
    is_page_resiliency_launched: bool | None = Field(None, alias='isPageResiliencyLaunched')
    is_pvcom_enabled_for_signed_in_cmp_customer: bool | None = Field(None, alias='isPVCOMEnabledForSignedInCMPCustomer')
    dv_web_linear_vmvpd_recording_card_1405557: bool | None = Field(None, alias='DV_WEB_LINEAR_VMVPD_RECORDING_CARD_1405557')
    dv_web_title_rating_experiment_1374850: str | None = Field(None, alias='DV_WEB_TITLE_RATING_EXPERIMENT_1374850')
    pv_web_lighthouse_1438707: bool | str | None = Field(None, alias='PV_WEB_LIGHTHOUSE_1438707')
    dv_web_rt_designation_icons_1459085: bool | None = Field(None, alias='DV_WEB_RT_DESIGNATION_ICONS_1459085')
    client_side_xdsso_cap_disabled: bool | None = Field(None, alias='clientSideXdssoCapDisabled')
    dv_web_linear_provider_logo_on_linear_carousel_1453031: bool | None = Field(None, alias='DV_WEB_LINEAR_PROVIDER_LOGO_ON_LINEAR_CAROUSEL_1453031')
    dv_web_linear_recents_recommended_carousel_1454985: bool | None = Field(None, alias='DV_WEB_LINEAR_RECENTS_RECOMMENDED_CAROUSEL_1454985')
    dv_web_linear_search_explore_scheme_1459604: bool | None = Field(None, alias='DV_WEB_LINEAR_SEARCH_EXPLORE_SCHEME_1459604')
    pv_web_prefetching_1461638: bool | None = Field(None, alias='PV_WEB_PREFETCHING_1461638')
    dv_web_player_optimisation_1464673: str | None = Field(None, alias='DV_WEB_PLAYER_OPTIMISATION_1464673')
    dv_web_multi_hvm_supported_1454411: bool | None = Field(None, alias='DV_WEB_MULTI_HVM_SUPPORTED_1454411')

class Resiliency(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    resiliency_version: str | None = Field(None, alias='resiliencyVersion')

class GlobalStore(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    request_context: RequestContext | None = Field(None, alias='RequestContext')
    clickstream_data: ClickstreamData | None = Field(None, alias='ClickstreamData')
    site_variant: str | None = Field(None, alias='SiteVariant')
    profile: Profile | None = Field(None, alias='Profile')
    home_region: str | None = Field(None, alias='HomeRegion')
    feature_pivots: FeaturePivots | None = Field(None, alias='FeaturePivots')
    resiliency: Resiliency | None = Field(None, alias='Resiliency')
    cross_domain_sso_url: Any | None = Field(None, alias='CrossDomainSSOUrl')
    player_context: dict[str, Any] | None = Field(None, alias='PlayerContext')

class Config(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    delay_loading_indicator: bool | None = Field(None, alias='delayLoadingIndicator')
    csn_deny_list: list[str] | None = Field(None, alias='csnDenyList')
    disable_downloads_sync: bool | None = Field(None, alias='disableDownloadsSync')
    client_ttl_mins: int | None = Field(None, alias='clientTTLMins')
    force_fake_navigation_api: bool | None = Field(None, alias='forceFakeNavigationAPI')

class DetailModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    head: Head | None = None
    body: Body | None = None
    global_store: GlobalStore | None = Field(None, alias='globalStore')
    config: Config | None = None
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
