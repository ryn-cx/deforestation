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

class FiveStar(BaseModel):
    model_config = ConfigDict(defer_build=True)
    hover_text: str = Field(..., alias='hoverText')
    percentage: int
    percentage_display: str = Field(..., alias='percentageDisplay')
    rating_display_label: str = Field(..., alias='ratingDisplayLabel')
    url: str

class FourStar(BaseModel):
    model_config = ConfigDict(defer_build=True)
    hover_text: str = Field(..., alias='hoverText')
    percentage: int
    percentage_display: str = Field(..., alias='percentageDisplay')
    rating_display_label: str = Field(..., alias='ratingDisplayLabel')
    url: str

class OneStar(BaseModel):
    model_config = ConfigDict(defer_build=True)
    hover_text: str = Field(..., alias='hoverText')
    percentage: int
    percentage_display: str = Field(..., alias='percentageDisplay')
    rating_display_label: str = Field(..., alias='ratingDisplayLabel')
    url: str

class ThreeStar(BaseModel):
    model_config = ConfigDict(defer_build=True)
    hover_text: str = Field(..., alias='hoverText')
    percentage: int
    percentage_display: str = Field(..., alias='percentageDisplay')
    rating_display_label: str = Field(..., alias='ratingDisplayLabel')
    url: str

class TwoStar(BaseModel):
    model_config = ConfigDict(defer_build=True)
    hover_text: str = Field(..., alias='hoverText')
    percentage: int
    percentage_display: str = Field(..., alias='percentageDisplay')
    rating_display_label: str = Field(..., alias='ratingDisplayLabel')
    url: str

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
    review_rating_info: ReviewRatingInfo = Field(..., alias='reviewRatingInfo')

class Reviews(BaseModel):
    model_config = ConfigDict(defer_build=True)
    all_reviews_link: str = Field(..., alias='allReviewsLink')
    create_review_link: str = Field(..., alias='createReviewLink')
    locale_language: str = Field(..., alias='localeLanguage')
    review_submission_token: str = Field(..., alias='reviewSubmissionToken')
    reviews_analysis_model: ReviewsAnalysisModel = Field(..., alias='reviewsAnalysisModel')
    title_id: str = Field(..., alias='titleID')

class B005C8Db7E(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str
    synopsis: str
    amazon_rating: AmazonRating = Field(..., alias='amazonRating')
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
    parent_title: str = Field(..., alias='parentTitle')
    playback_tracks: list[None] = Field(..., alias='playbackTracks')
    rating_badge: RatingBadge = Field(..., alias='ratingBadge')
    release_date: str = Field(..., alias='releaseDate')
    release_year: int = Field(..., alias='releaseYear')
    reviews: Reviews
    runtime: str
    season_number: int = Field(..., alias='seasonNumber')
    studios: list[str]
    subtitles: list[str]
    title_type: str = Field(..., alias='titleType')

class Contributors1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    cast: list[CastItem]
    directors: list[Director]
    producers: list[Producer]

class RatingBadge1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field__type: str = Field(..., alias='__type')
    country_code: str = Field(..., alias='countryCode')
    description: str
    display_text: str = Field(..., alias='displayText')
    id: str

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
    review_rating_info: ReviewRatingInfo = Field(..., alias='reviewRatingInfo')

class Reviews1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    all_reviews_link: str = Field(..., alias='allReviewsLink')
    create_review_link: str = Field(..., alias='createReviewLink')
    locale_language: str = Field(..., alias='localeLanguage')
    review_submission_token: str = Field(..., alias='reviewSubmissionToken')
    reviews_analysis_model: ReviewsAnalysisModel1 = Field(..., alias='reviewsAnalysisModel')
    title_id: str = Field(..., alias='titleID')

class B001T5Bzao(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str
    synopsis: str
    amazon_rating: AmazonRating = Field(..., alias='amazonRating')
    audio_tracks: list[str] = Field(..., alias='audioTracks')
    catalog_id: str = Field(..., alias='catalogId')
    contributors: Contributors1
    duration: int
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
    playback_tracks: list[None] = Field(..., alias='playbackTracks')
    rating_badge: RatingBadge1 = Field(..., alias='ratingBadge')
    release_date: str = Field(..., alias='releaseDate')
    release_year: int = Field(..., alias='releaseYear')
    reviews: Reviews1
    runtime: str
    studios: list[str]
    subtitles: list[str]
    title_type: str = Field(..., alias='titleType')

class Contributors2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    cast: list[CastItem]
    directors: list[Director]
    producers: list[None]

class RatingBadge2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field__type: str = Field(..., alias='__type')
    description: str
    display_text: str = Field(..., alias='displayText')
    id: str

class FiveStar2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    percentage: int
    percentage_display: str = Field(..., alias='percentageDisplay')
    rating_display_label: str = Field(..., alias='ratingDisplayLabel')

class FourStar2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    percentage: int
    percentage_display: str = Field(..., alias='percentageDisplay')
    rating_display_label: str = Field(..., alias='ratingDisplayLabel')

class OneStar2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    percentage: int
    percentage_display: str = Field(..., alias='percentageDisplay')
    rating_display_label: str = Field(..., alias='ratingDisplayLabel')

class ThreeStar2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    percentage: int
    percentage_display: str = Field(..., alias='percentageDisplay')
    rating_display_label: str = Field(..., alias='ratingDisplayLabel')

class TwoStar2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    percentage: int
    percentage_display: str = Field(..., alias='percentageDisplay')
    rating_display_label: str = Field(..., alias='ratingDisplayLabel')

class RatingsHistogram2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    five_star: FiveStar2 = Field(..., alias='fiveStar')
    four_star: FourStar2 = Field(..., alias='fourStar')
    one_star: OneStar2 = Field(..., alias='oneStar')
    three_star: ThreeStar2 = Field(..., alias='threeStar')
    two_star: TwoStar2 = Field(..., alias='twoStar')

class ReviewsAnalysisModel2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    ratings_histogram: RatingsHistogram2 = Field(..., alias='ratingsHistogram')

class Reviews2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    all_reviews_link: str = Field(..., alias='allReviewsLink')
    create_review_link: str = Field(..., alias='createReviewLink')
    locale_language: str = Field(..., alias='localeLanguage')
    review_submission_token: str = Field(..., alias='reviewSubmissionToken')
    reviews_analysis_model: ReviewsAnalysisModel2 = Field(..., alias='reviewsAnalysisModel')
    title_id: str = Field(..., alias='titleID')

class B0Chf9Mzxz(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str
    synopsis: str
    audio_tracks: list[str] = Field(..., alias='audioTracks')
    catalog_id: str = Field(..., alias='catalogId')
    contributors: Contributors2
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
    parent_title: str = Field(..., alias='parentTitle')
    playback_tracks: list[None] = Field(..., alias='playbackTracks')
    rating_badge: RatingBadge2 = Field(..., alias='ratingBadge')
    release_date: str = Field(..., alias='releaseDate')
    release_year: int = Field(..., alias='releaseYear')
    reviews: Reviews2
    runtime: str
    season_number: int = Field(..., alias='seasonNumber')
    studios: list[str]
    subtitles: list[str]
    title_type: str = Field(..., alias='titleType')

class HeaderDetail(BaseModel):
    model_config = ConfigDict(defer_build=True)
    b005_c8_db7_e: B005C8Db7E | None = Field(None, alias='B005C8DB7E')
    b001_t5_bzao: B001T5Bzao | None = Field(None, alias='B001T5BZAO')
    b0_chf9_mzxz: B0Chf9Mzxz | None = Field(None, alias='B0CHF9MZXZ')

class Detail(BaseModel):
    model_config = ConfigDict(defer_build=True)
    detail: dict[str, Any]
    header_detail: HeaderDetail = Field(..., alias='headerDetail')
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

class TransactionDetail(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class ComponentPayload1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_component: TextComponent = Field(..., alias='textComponent')

class Header(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload1 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class Components(BaseModel):
    model_config = ConfigDict(defer_build=True)
    transaction_detail: TransactionDetail = Field(..., alias='TRANSACTION_DETAIL')
    header: Header = Field(..., alias='HEADER')

class ExpandingCard(BaseModel):
    model_config = ConfigDict(defer_build=True)
    actions: list[Action1]
    card_type: str = Field(..., alias='cardType')
    components: Components

class Payload(BaseModel):
    model_config = ConfigDict(defer_build=True)
    expanding_card: ExpandingCard = Field(..., alias='expandingCard')
    payload_type: str = Field(..., alias='payloadType')

class PrimaryAction(BaseModel):
    model_config = ConfigDict(defer_build=True)
    action_type: str = Field(..., alias='actionType')
    is_selected: bool = Field(..., alias='isSelected')
    payload: Payload

class ReactionAction(BaseModel):
    model_config = ConfigDict(defer_build=True)
    csrf_token: str = Field(..., alias='csrfToken')
    reaction: str
    sign_in_url: str = Field(..., alias='signInUrl')

class B005C8Db7E1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    messages: Messages
    primary_actions: list[PrimaryAction] = Field(..., alias='primaryActions')
    reaction_action: ReactionAction = Field(..., alias='reactionAction')
    secondary_actions: list[None] = Field(..., alias='secondaryActions')
    view_ref_marker: str = Field(..., alias='viewRefMarker')

class FocusMessage1(BaseModel):
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

class Messages1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    entitlement_type: str = Field(..., alias='entitlementType')
    focus_message: FocusMessage1 = Field(..., alias='focusMessage')
    high_value_message: HighValueMessage = Field(..., alias='highValueMessage')
    informational_messages: list[InformationalMessage] = Field(..., alias='informationalMessages')

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

class Payload3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    payload_type: str = Field(..., alias='payloadType')
    transaction: Transaction1

class Action2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    action_type: str = Field(..., alias='actionType')
    is_selected: bool = Field(..., alias='isSelected')
    payload: Payload3
    presentation: Presentation

class ComponentPayload2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_component: TextComponent = Field(..., alias='textComponent')

class TransactionDetail1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload2 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class ComponentPayload3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_component: TextComponent = Field(..., alias='textComponent')

class Header1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload3 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class Tags(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_theme: str = Field(..., alias='TEXT_THEME')

class TextComponent4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    tags: Tags
    text: str
    text_type: str = Field(..., alias='textType')

class ComponentPayload4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_component: TextComponent4 = Field(..., alias='textComponent')

class MotivatorMessaging(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload4 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class Components1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    transaction_detail: TransactionDetail1 = Field(..., alias='TRANSACTION_DETAIL')
    header: Header1 = Field(..., alias='HEADER')
    motivator_messaging: MotivatorMessaging | None = Field(None, alias='MOTIVATOR_MESSAGING')

class ExpandingCard1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    actions: list[Action2]
    card_type: str = Field(..., alias='cardType')
    components: Components1

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

class Payload4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    payload_type: str = Field(..., alias='payloadType')
    transaction: Transaction2

class Action3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    action_type: str = Field(..., alias='actionType')
    is_selected: bool = Field(..., alias='isSelected')
    payload: Payload4
    presentation: Presentation

class TextListItem(BaseModel):
    model_config = ConfigDict(defer_build=True)
    tags: dict[str, Any]
    text: str
    text_type: str = Field(..., alias='textType')

class TextComponentCollection(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_list: list[TextListItem] = Field(..., alias='textList')

class ComponentPayload5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_component_collection: TextComponentCollection = Field(..., alias='textComponentCollection')

class TransactionDetail2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload5 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class Tags1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    brand_glow: str = Field(..., alias='BRAND_GLOW')
    text_theme: str = Field(..., alias='TEXT_THEME')

class TextComponent5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    tags: Tags1
    text: str
    text_type: str = Field(..., alias='textType')

class ComponentPayload6(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_component: TextComponent5 = Field(..., alias='textComponent')

class Banner(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload6 = Field(..., alias='componentPayload')
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

class ComponentPayload7(BaseModel):
    model_config = ConfigDict(defer_build=True)
    icon_text_list_component: IconTextListComponent = Field(..., alias='iconTextListComponent')

class MotivatorMessaging1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload7 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class Components2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    transaction_detail: TransactionDetail2 = Field(..., alias='TRANSACTION_DETAIL')
    banner: Banner = Field(..., alias='BANNER')
    motivator_messaging: MotivatorMessaging1 | None = Field(None, alias='MOTIVATOR_MESSAGING')

class CardOption(BaseModel):
    model_config = ConfigDict(defer_build=True)
    actions: list[Action3]
    card_type: str = Field(..., alias='cardType')
    components: Components2

class Payload2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    expanding_card: ExpandingCard1 | None = Field(None, alias='expandingCard')
    payload_type: str = Field(..., alias='payloadType')
    card_options: list[CardOption] | None = Field(None, alias='cardOptions')

class Presentation3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    primary_label: str = Field(..., alias='primaryLabel')
    ref_marker: str = Field(..., alias='refMarker')

class PrimaryAction1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    action_type: str = Field(..., alias='actionType')
    is_selected: bool = Field(..., alias='isSelected')
    payload: Payload2
    presentation: Presentation3 | None = None

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

class Payload5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    payload_type: str = Field(..., alias='payloadType')
    playback: Playback

class Presentation4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    icon: str
    primary_label: str = Field(..., alias='primaryLabel')
    ref_marker: str = Field(..., alias='refMarker')

class SecondaryAction(BaseModel):
    model_config = ConfigDict(defer_build=True)
    action_type: str = Field(..., alias='actionType')
    is_selected: bool = Field(..., alias='isSelected')
    payload: Payload5
    presentation: Presentation4

class B001T5Bzao1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    messages: Messages1
    primary_actions: list[PrimaryAction1] = Field(..., alias='primaryActions')
    reaction_action: ReactionAction = Field(..., alias='reactionAction')
    secondary_actions: list[SecondaryAction] = Field(..., alias='secondaryActions')
    view_ref_marker: str = Field(..., alias='viewRefMarker')

class FocusMessage2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    dv_message: DvMessage = Field(..., alias='dvMessage')
    icon: str
    icon_type: str = Field(..., alias='iconType')

class HighValueMessage1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    dv_message: DvMessage = Field(..., alias='dvMessage')
    icon: str

class InformationalMessage1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    dv_message: DvMessage = Field(..., alias='dvMessage')

class ProviderLogo(BaseModel):
    model_config = ConfigDict(defer_build=True)
    alt_text: str = Field(..., alias='altText')
    image: str
    link: str

class Messages2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    entitlement_type: str = Field(..., alias='entitlementType')
    focus_message: FocusMessage2 = Field(..., alias='focusMessage')
    high_value_message: HighValueMessage1 = Field(..., alias='highValueMessage')
    informational_messages: list[InformationalMessage1] = Field(..., alias='informationalMessages')
    provider_logo: ProviderLogo = Field(..., alias='providerLogo')

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

class Payload7(BaseModel):
    model_config = ConfigDict(defer_build=True)
    payload_type: str = Field(..., alias='payloadType')
    subscription: Subscription

class Presentation5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    primary_label: str = Field(..., alias='primaryLabel')
    ref_marker: str = Field(..., alias='refMarker')

class Action4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    action_type: str = Field(..., alias='actionType')
    is_selected: bool = Field(..., alias='isSelected')
    payload: Payload7
    presentation: Presentation5

class TextComponent6(BaseModel):
    model_config = ConfigDict(defer_build=True)
    tags: dict[str, Any]
    text: str
    text_type: str = Field(..., alias='textType')

class ComponentPayload8(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_component: TextComponent6 = Field(..., alias='textComponent')

class TransactionDetail3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload8 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class Tags2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    logo_entity_tag: str = Field(..., alias='LOGO_ENTITY_TAG')
    logo_height: str = Field(..., alias='LOGO_HEIGHT')
    logo_width: str = Field(..., alias='LOGO_WIDTH')

class LogoComponent(BaseModel):
    model_config = ConfigDict(defer_build=True)
    tags: Tags2
    url: str

class ComponentPayload9(BaseModel):
    model_config = ConfigDict(defer_build=True)
    logo_component: LogoComponent = Field(..., alias='logoComponent')

class Header2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload9 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class Components3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    transaction_detail: TransactionDetail3 = Field(..., alias='TRANSACTION_DETAIL')
    header: Header2 = Field(..., alias='HEADER')

class ExpandingCard2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    actions: list[Action4]
    card_type: str = Field(..., alias='cardType')
    components: Components3

class Payload6(BaseModel):
    model_config = ConfigDict(defer_build=True)
    expanding_card: ExpandingCard2 = Field(..., alias='expandingCard')
    payload_type: str = Field(..., alias='payloadType')

class PrimaryAction2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    action_type: str = Field(..., alias='actionType')
    is_selected: bool = Field(..., alias='isSelected')
    payload: Payload6

class B0Chf9Mzxz1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    messages: Messages2
    primary_actions: list[PrimaryAction2] = Field(..., alias='primaryActions')
    reaction_action: ReactionAction = Field(..., alias='reactionAction')
    secondary_actions: list[None] = Field(..., alias='secondaryActions')
    view_ref_marker: str = Field(..., alias='viewRefMarker')

class Atf1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    b005_c8_db7_e: B005C8Db7E1 | None = Field(None, alias='B005C8DB7E')
    b001_t5_bzao: B001T5Bzao1 | None = Field(None, alias='B001T5BZAO')
    b0_chf9_mzxz: B0Chf9Mzxz1 | None = Field(None, alias='B0CHF9MZXZ')

class Action(BaseModel):
    model_config = ConfigDict(defer_build=True)
    btf: dict[str, Any]
    atf: Atf1

class Refund(BaseModel):
    model_config = ConfigDict(defer_build=True)
    fragments: dict[str, Any]
    refunding: None

class B005C8Db7E2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    max_score: str = Field(..., alias='maxScore')
    score: float
    score_formatted: str = Field(..., alias='scoreFormatted')

class B001T5Bzao2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    max_score: str = Field(..., alias='maxScore')
    score: float
    score_formatted: str = Field(..., alias='scoreFormatted')

class B0Chf9Mzxz2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    max_score: str = Field(..., alias='maxScore')
    score: float
    score_formatted: str = Field(..., alias='scoreFormatted')

class Imdb(BaseModel):
    model_config = ConfigDict(defer_build=True)
    b005_c8_db7_e: B005C8Db7E2 | None = Field(None, alias='B005C8DB7E')
    b001_t5_bzao: B001T5Bzao2 | None = Field(None, alias='B001T5BZAO')
    b0_chf9_mzxz: B0Chf9Mzxz2 | None = Field(None, alias='B0CHF9MZXZ')

class BuyboxTitleId(BaseModel):
    model_config = ConfigDict(defer_build=True)
    b005_c8_db7_e: str | None = Field(None, alias='B005C8DB7E')
    b001_t5_bzao: str | None = Field(None, alias='B001T5BZAO')
    b0_chf9_mzxz: str | None = Field(None, alias='B0CHF9MZXZ')

class Creative(BaseModel):
    model_config = ConfigDict(defer_build=True)
    b005_c8_db7_e: dict[str, Any] | None = Field(None, alias='B005C8DB7E')
    b001_t5_bzao: dict[str, Any] | None = Field(None, alias='B001T5BZAO')
    b0_chf9_mzxz: dict[str, Any] | None = Field(None, alias='B0CHF9MZXZ')

class Banner1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    crow: dict[str, Any]
    ui: None

class B005C8Db7E3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    alerts: list[None]
    warnings: list[None]

class B001T5Bzao3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    alerts: list[None]
    warnings: list[None]

class B0Chf9Mzxz3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    alerts: list[None]
    warnings: list[None]

class Notification(BaseModel):
    model_config = ConfigDict(defer_build=True)
    b005_c8_db7_e: B005C8Db7E3 | None = Field(None, alias='B005C8DB7E')
    b001_t5_bzao: B001T5Bzao3 | None = Field(None, alias='B001T5BZAO')
    b0_chf9_mzxz: B0Chf9Mzxz3 | None = Field(None, alias='B0CHF9MZXZ')

class B005C8Db7EItem(BaseModel):
    model_config = ConfigDict(defer_build=True)
    season_id: str = Field(..., alias='seasonId')
    season_link: str = Field(..., alias='seasonLink')
    display_name: str = Field(..., alias='displayName')
    season_selector_icon: str = Field(..., alias='seasonSelectorIcon')
    sequence_number: int = Field(..., alias='sequenceNumber')
    is_selected: bool = Field(..., alias='isSelected')

class B0Chf9MzxzItem(BaseModel):
    model_config = ConfigDict(defer_build=True)
    season_id: str = Field(..., alias='seasonId')
    season_link: str = Field(..., alias='seasonLink')
    display_name: str = Field(..., alias='displayName')
    season_selector_icon: str = Field(..., alias='seasonSelectorIcon')
    sequence_number: int = Field(..., alias='sequenceNumber')
    is_selected: bool = Field(..., alias='isSelected')

class Seasons(BaseModel):
    model_config = ConfigDict(defer_build=True)
    b005_c8_db7_e: list[B005C8Db7EItem] | None = Field(None, alias='B005C8DB7E')
    b0_chf9_mzxz: list[B0Chf9MzxzItem] | None = Field(None, alias='B0CHF9MZXZ')

class B005C8Db7E4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    asins: list[str]
    compact_gti: str = Field(..., alias='compactGTI')
    gti: str
    is_launched: bool = Field(..., alias='isLaunched')
    link: str
    sequence_number: int = Field(..., alias='sequenceNumber')
    title_type: str = Field(..., alias='titleType')

class B005C8Dbii(BaseModel):
    model_config = ConfigDict(defer_build=True)
    asins: list[str]
    compact_gti: str = Field(..., alias='compactGTI')
    gti: str
    is_launched: bool = Field(..., alias='isLaunched')
    link: str
    sequence_number: int = Field(..., alias='sequenceNumber')
    title_type: str = Field(..., alias='titleType')

class B001T5Bzao4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    asins: list[str]
    compact_gti: str = Field(..., alias='compactGTI')
    gti: str
    is_launched: bool = Field(..., alias='isLaunched')
    link: str
    title_type: str = Field(..., alias='titleType')

class B0Chf9Mzxz4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    asins: list[str]
    compact_gti: str = Field(..., alias='compactGTI')
    gti: str
    is_launched: bool = Field(..., alias='isLaunched')
    link: str
    sequence_number: int = Field(..., alias='sequenceNumber')
    title_type: str = Field(..., alias='titleType')

class B0Cjp8Rbmq(BaseModel):
    model_config = ConfigDict(defer_build=True)
    asins: list[str]
    compact_gti: str = Field(..., alias='compactGTI')
    gti: str
    is_launched: bool = Field(..., alias='isLaunched')
    link: str
    sequence_number: int = Field(..., alias='sequenceNumber')
    title_type: str = Field(..., alias='titleType')

class Self(BaseModel):
    model_config = ConfigDict(defer_build=True)
    b005_c8_db7_e: B005C8Db7E4 | None = Field(None, alias='B005C8DB7E')
    b005_c8_dbii: B005C8Dbii | None = Field(None, alias='B005C8DBII')
    b001_t5_bzao: B001T5Bzao4 | None = Field(None, alias='B001T5BZAO')
    b0_chf9_mzxz: B0Chf9Mzxz4 | None = Field(None, alias='B0CHF9MZXZ')
    b0_cjp8_rbmq: B0Cjp8Rbmq | None = Field(None, alias='B0CJP8RBMQ')

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

class B005C8Db7E5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    ajax_enabled: bool = Field(..., alias='ajaxEnabled')
    endpoint: Endpoint
    format_code: str = Field(..., alias='formatCode')
    tag: str
    text: Text

class Endpoint1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    partial_url: str = Field(..., alias='partialURL')
    query: Query

class B001T5Bzao5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    ajax_enabled: bool = Field(..., alias='ajaxEnabled')
    endpoint: Endpoint1
    format_code: str = Field(..., alias='formatCode')
    tag: str
    text: Text

class Endpoint2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    partial_url: str = Field(..., alias='partialURL')
    query: Query

class B0Chf9Mzxz5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    ajax_enabled: bool = Field(..., alias='ajaxEnabled')
    endpoint: Endpoint2
    format_code: str = Field(..., alias='formatCode')
    tag: str
    text: Text

class Watchlist(BaseModel):
    model_config = ConfigDict(defer_build=True)
    b005_c8_db7_e: B005C8Db7E5 | None = Field(None, alias='B005C8DB7E')
    b001_t5_bzao: B001T5Bzao5 | None = Field(None, alias='B001T5BZAO')
    b0_chf9_mzxz: B0Chf9Mzxz5 | None = Field(None, alias='B0CHF9MZXZ')

class B005C8Db7E6(BaseModel):
    model_config = ConfigDict(defer_build=True)
    is_pin_setup_required: bool = Field(..., alias='isPinSetupRequired')
    is_playback_pin_required: bool = Field(..., alias='isPlaybackPinRequired')
    is_purchase_pin_required: bool = Field(..., alias='isPurchasePinRequired')

class B001T5Bzao6(BaseModel):
    model_config = ConfigDict(defer_build=True)
    is_pin_setup_required: bool = Field(..., alias='isPinSetupRequired')
    is_playback_pin_required: bool = Field(..., alias='isPlaybackPinRequired')
    is_purchase_pin_required: bool = Field(..., alias='isPurchasePinRequired')

class B0Chf9Mzxz6(BaseModel):
    model_config = ConfigDict(defer_build=True)
    is_pin_setup_required: bool = Field(..., alias='isPinSetupRequired')
    is_playback_pin_required: bool = Field(..., alias='isPlaybackPinRequired')
    is_purchase_pin_required: bool = Field(..., alias='isPurchasePinRequired')

class Restriction(BaseModel):
    model_config = ConfigDict(defer_build=True)
    b005_c8_db7_e: B005C8Db7E6 | None = Field(None, alias='B005C8DB7E')
    b001_t5_bzao: B001T5Bzao6 | None = Field(None, alias='B001T5BZAO')
    b0_chf9_mzxz: B0Chf9Mzxz6 | None = Field(None, alias='B0CHF9MZXZ')

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

class B001T5Bzao7(BaseModel):
    model_config = ConfigDict(defer_build=True)
    asset_id: str = Field(..., alias='assetId')
    draper_tracking_events: DraperTrackingEvents = Field(..., alias='draperTrackingEvents')
    is_trailer_autoplay_enabled: bool = Field(..., alias='isTrailerAutoplayEnabled')
    playback_envelope: str = Field(..., alias='playbackEnvelope')
    playback_id: str = Field(..., alias='playbackId')
    ref_marker: str = Field(..., alias='refMarker')
    text_map: TextMap = Field(..., alias='textMap')

class AutoplayTrailerHero(BaseModel):
    model_config = ConfigDict(defer_build=True)
    b001_t5_bzao: B001T5Bzao7 | None = Field(None, alias='B001T5BZAO')

class ComingSoon(BaseModel):
    model_config = ConfigDict(defer_build=True)
    b005_c8_db7_e: bool | None = Field(None, alias='B005C8DB7E')
    b001_t5_bzao: bool | None = Field(None, alias='B001T5BZAO')
    b0_chf9_mzxz: bool | None = Field(None, alias='B0CHF9MZXZ')

class MaturityRating(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field__type: str = Field(..., alias='__type')
    description: str
    display_text: str = Field(..., alias='displayText')
    id: str

class B005C8Db7E7(BaseModel):
    model_config = ConfigDict(defer_build=True)
    episode_count: str = Field(..., alias='episodeCount')
    maturity_rating: MaturityRating = Field(..., alias='maturityRating')
    moods: list[str]

class MaturityRating1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field__type: str = Field(..., alias='__type')
    country_code: str = Field(..., alias='countryCode')
    description: str
    display_text: str = Field(..., alias='displayText')
    id: str

class B001T5Bzao8(BaseModel):
    model_config = ConfigDict(defer_build=True)
    maturity_rating: MaturityRating1 = Field(..., alias='maturityRating')
    moods: list[str]

class MaturityRating2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field__type: str = Field(..., alias='__type')
    description: str
    display_text: str = Field(..., alias='displayText')
    id: str

class B0Chf9Mzxz7(BaseModel):
    model_config = ConfigDict(defer_build=True)
    episode_count: str = Field(..., alias='episodeCount')
    maturity_rating: MaturityRating2 = Field(..., alias='maturityRating')
    moods: list[str]

class Metadata1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    b005_c8_db7_e: B005C8Db7E7 | None = Field(None, alias='B005C8DB7E')
    b001_t5_bzao: B001T5Bzao8 | None = Field(None, alias='B001T5BZAO')
    b0_chf9_mzxz: B0Chf9Mzxz7 | None = Field(None, alias='B0CHF9MZXZ')

class Widgets(BaseModel):
    model_config = ConfigDict(defer_build=True)
    b005_c8_db7_e: dict[str, Any] | None = Field(None, alias='B005C8DB7E')
    b001_t5_bzao: dict[str, Any] | None = Field(None, alias='B001T5BZAO')
    b0_chf9_mzxz: dict[str, Any] | None = Field(None, alias='B0CHF9MZXZ')

class State(BaseModel):
    model_config = ConfigDict(defer_build=True)
    features: Features
    page_title_id: str = Field(..., alias='pageTitleId')
    detail: Detail
    action: Action
    refund: Refund
    imdb: Imdb
    buy_box: dict[str, Any] = Field(..., alias='buyBox')
    buybox_title_id: BuyboxTitleId = Field(..., alias='buyboxTitleId')
    creative: Creative
    banner: Banner1
    age_verification_banner: dict[str, Any] = Field(..., alias='ageVerificationBanner')
    notification: Notification
    seasons: Seasons
    self: Self
    watchlist: Watchlist
    restriction: Restriction
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
    autoplay_trailer_hero: AutoplayTrailerHero = Field(..., alias='autoplayTrailerHero')
    playback_integration: dict[str, Any] = Field(..., alias='playbackIntegration')
    coming_soon: ComingSoon = Field(..., alias='comingSoon')
    metadata: Metadata1
    widgets: Widgets
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

class Images3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    packshot: str
    covershot: str

class B005C8Dbii1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str
    synopsis: str
    audio_tracks: list[str] = Field(..., alias='audioTracks')
    duration: int
    entity_type: str = Field(..., alias='entityType')
    episode_number: int = Field(..., alias='episodeNumber')
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
    images: Images3

class B005C8E538(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str
    synopsis: str
    audio_tracks: list[str] = Field(..., alias='audioTracks')
    duration: int
    entity_type: str = Field(..., alias='entityType')
    episode_number: int = Field(..., alias='episodeNumber')
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
    images: Images3

class B005C8E70Y(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str
    synopsis: str
    audio_tracks: list[str] = Field(..., alias='audioTracks')
    duration: int
    entity_type: str = Field(..., alias='entityType')
    episode_number: int = Field(..., alias='episodeNumber')
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
    images: Images3

class B005G0R6Xi(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str
    synopsis: str
    audio_tracks: list[str] = Field(..., alias='audioTracks')
    duration: int
    entity_type: str = Field(..., alias='entityType')
    episode_number: int = Field(..., alias='episodeNumber')
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
    images: Images3

class B005C8Egx2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str
    synopsis: str
    audio_tracks: list[str] = Field(..., alias='audioTracks')
    duration: int
    entity_type: str = Field(..., alias='entityType')
    episode_number: int = Field(..., alias='episodeNumber')
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
    images: Images3

class B005C8Ei62(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str
    synopsis: str
    audio_tracks: list[str] = Field(..., alias='audioTracks')
    duration: int
    entity_type: str = Field(..., alias='entityType')
    episode_number: int = Field(..., alias='episodeNumber')
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
    images: Images3

class B005C8Ec7M(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str
    synopsis: str
    audio_tracks: list[str] = Field(..., alias='audioTracks')
    duration: int
    entity_type: str = Field(..., alias='entityType')
    episode_number: int = Field(..., alias='episodeNumber')
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
    images: Images3

class B005C8Egeg(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str
    synopsis: str
    audio_tracks: list[str] = Field(..., alias='audioTracks')
    duration: int
    entity_type: str = Field(..., alias='entityType')
    episode_number: int = Field(..., alias='episodeNumber')
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
    images: Images3

class B005C8Elci(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str
    synopsis: str
    audio_tracks: list[str] = Field(..., alias='audioTracks')
    duration: int
    entity_type: str = Field(..., alias='entityType')
    episode_number: int = Field(..., alias='episodeNumber')
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
    images: Images3

class B005C8Ed30(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str
    synopsis: str
    audio_tracks: list[str] = Field(..., alias='audioTracks')
    duration: int
    entity_type: str = Field(..., alias='entityType')
    episode_number: int = Field(..., alias='episodeNumber')
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
    images: Images3

class B005C8Dike(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str
    synopsis: str
    audio_tracks: list[str] = Field(..., alias='audioTracks')
    duration: int
    entity_type: str = Field(..., alias='entityType')
    episode_number: int = Field(..., alias='episodeNumber')
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
    images: Images3

class B005C8Ecls(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str
    synopsis: str
    audio_tracks: list[str] = Field(..., alias='audioTracks')
    duration: int
    entity_type: str = Field(..., alias='entityType')
    episode_number: int = Field(..., alias='episodeNumber')
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
    images: Images3

class B005C8Dtto(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str
    synopsis: str
    audio_tracks: list[str] = Field(..., alias='audioTracks')
    duration: int
    entity_type: str = Field(..., alias='entityType')
    episode_number: int = Field(..., alias='episodeNumber')
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
    images: Images3

class B005C8E91Q(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str
    synopsis: str
    audio_tracks: list[str] = Field(..., alias='audioTracks')
    duration: int
    entity_type: str = Field(..., alias='entityType')
    episode_number: int = Field(..., alias='episodeNumber')
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
    images: Images3

class B005C8Dkvg(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str
    synopsis: str
    audio_tracks: list[str] = Field(..., alias='audioTracks')
    duration: int
    entity_type: str = Field(..., alias='entityType')
    episode_number: int = Field(..., alias='episodeNumber')
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
    images: Images3

class B005C8Ei5S(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str
    synopsis: str
    audio_tracks: list[str] = Field(..., alias='audioTracks')
    duration: int
    entity_type: str = Field(..., alias='entityType')
    episode_number: int = Field(..., alias='episodeNumber')
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
    images: Images3

class B005C8Eiui(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str
    synopsis: str
    audio_tracks: list[str] = Field(..., alias='audioTracks')
    duration: int
    entity_type: str = Field(..., alias='entityType')
    episode_number: int = Field(..., alias='episodeNumber')
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
    images: Images3

class B005C8Emmm(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str
    synopsis: str
    audio_tracks: list[str] = Field(..., alias='audioTracks')
    duration: int
    entity_type: str = Field(..., alias='entityType')
    episode_number: int = Field(..., alias='episodeNumber')
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
    images: Images3

class B005C8Eh2W(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str
    synopsis: str
    audio_tracks: list[str] = Field(..., alias='audioTracks')
    duration: int
    entity_type: str = Field(..., alias='entityType')
    episode_number: int = Field(..., alias='episodeNumber')
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
    images: Images3

class B005C8Ebws(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str
    synopsis: str
    audio_tracks: list[str] = Field(..., alias='audioTracks')
    duration: int
    entity_type: str = Field(..., alias='entityType')
    episode_number: int = Field(..., alias='episodeNumber')
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
    images: Images3

class B005C8Ds0Y(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str
    synopsis: str
    audio_tracks: list[str] = Field(..., alias='audioTracks')
    duration: int
    entity_type: str = Field(..., alias='entityType')
    episode_number: int = Field(..., alias='episodeNumber')
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
    images: Images3

class B005C8E5A6(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str
    synopsis: str
    audio_tracks: list[str] = Field(..., alias='audioTracks')
    duration: int
    entity_type: str = Field(..., alias='entityType')
    episode_number: int = Field(..., alias='episodeNumber')
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
    images: Images3

class B005C8Ef8I(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str
    synopsis: str
    audio_tracks: list[str] = Field(..., alias='audioTracks')
    duration: int
    entity_type: str = Field(..., alias='entityType')
    episode_number: int = Field(..., alias='episodeNumber')
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
    images: Images3

class B005C8Ek9M(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str
    synopsis: str
    audio_tracks: list[str] = Field(..., alias='audioTracks')
    duration: int
    entity_type: str = Field(..., alias='entityType')
    episode_number: int = Field(..., alias='episodeNumber')
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
    images: Images3

class FiveStar3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    hover_text: str = Field(..., alias='hoverText')
    percentage: int
    percentage_display: str = Field(..., alias='percentageDisplay')
    rating_display_label: str = Field(..., alias='ratingDisplayLabel')
    url: str

class FourStar3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    hover_text: str = Field(..., alias='hoverText')
    percentage: int
    percentage_display: str = Field(..., alias='percentageDisplay')
    rating_display_label: str = Field(..., alias='ratingDisplayLabel')
    url: str

class OneStar3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    hover_text: str = Field(..., alias='hoverText')
    percentage: int
    percentage_display: str = Field(..., alias='percentageDisplay')
    rating_display_label: str = Field(..., alias='ratingDisplayLabel')
    url: str

class ThreeStar3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    hover_text: str = Field(..., alias='hoverText')
    percentage: int
    percentage_display: str = Field(..., alias='percentageDisplay')
    rating_display_label: str = Field(..., alias='ratingDisplayLabel')
    url: str

class TwoStar3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    hover_text: str = Field(..., alias='hoverText')
    percentage: int
    percentage_display: str = Field(..., alias='percentageDisplay')
    rating_display_label: str = Field(..., alias='ratingDisplayLabel')
    url: str

class RatingsHistogram3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    five_star: FiveStar3 = Field(..., alias='fiveStar')
    four_star: FourStar3 = Field(..., alias='fourStar')
    one_star: OneStar3 = Field(..., alias='oneStar')
    three_star: ThreeStar3 = Field(..., alias='threeStar')
    two_star: TwoStar3 = Field(..., alias='twoStar')

class ReviewsAnalysisModel3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    ratings_histogram: RatingsHistogram3 = Field(..., alias='ratingsHistogram')
    review_rating_info: ReviewRatingInfo = Field(..., alias='reviewRatingInfo')

class Reviews3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    all_reviews_link: str = Field(..., alias='allReviewsLink')
    create_review_link: str = Field(..., alias='createReviewLink')
    locale_language: str = Field(..., alias='localeLanguage')
    review_submission_token: str = Field(..., alias='reviewSubmissionToken')
    reviews_analysis_model: ReviewsAnalysisModel3 = Field(..., alias='reviewsAnalysisModel')
    title_id: str = Field(..., alias='titleID')

class B005C8Db7E8(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str
    synopsis: str
    amazon_rating: AmazonRating = Field(..., alias='amazonRating')
    audio_tracks: list[None] = Field(..., alias='audioTracks')
    entity_type: str = Field(..., alias='entityType')
    explore_panel_url: str = Field(..., alias='explorePanelURL')
    explore_tab_name: str = Field(..., alias='exploreTabName')
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
    parent_title: str = Field(..., alias='parentTitle')
    playback_tracks: list[None] = Field(..., alias='playbackTracks')
    rating_badge: RatingBadge2 = Field(..., alias='ratingBadge')
    release_date: str = Field(..., alias='releaseDate')
    release_year: int = Field(..., alias='releaseYear')
    reviews: Reviews3
    runtime: str
    season_number: int = Field(..., alias='seasonNumber')
    subtitles: list[None]
    title_type: str = Field(..., alias='titleType')
    images: Images3

class RatingBadge4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field__type: str = Field(..., alias='__type')
    country_code: str = Field(..., alias='countryCode')
    description: str
    display_text: str = Field(..., alias='displayText')
    id: str

class RatingsHistogram4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    five_star: FiveStar3 = Field(..., alias='fiveStar')
    four_star: FourStar3 = Field(..., alias='fourStar')
    one_star: OneStar3 = Field(..., alias='oneStar')
    three_star: ThreeStar3 = Field(..., alias='threeStar')
    two_star: TwoStar3 = Field(..., alias='twoStar')

class ReviewsAnalysisModel4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    ratings_histogram: RatingsHistogram4 = Field(..., alias='ratingsHistogram')
    review_rating_info: ReviewRatingInfo = Field(..., alias='reviewRatingInfo')

class Reviews4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    all_reviews_link: str = Field(..., alias='allReviewsLink')
    create_review_link: str = Field(..., alias='createReviewLink')
    locale_language: str = Field(..., alias='localeLanguage')
    review_submission_token: str = Field(..., alias='reviewSubmissionToken')
    reviews_analysis_model: ReviewsAnalysisModel4 = Field(..., alias='reviewsAnalysisModel')
    title_id: str = Field(..., alias='titleID')

class B001T5Bzao9(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str
    synopsis: str
    amazon_rating: AmazonRating = Field(..., alias='amazonRating')
    audio_tracks: list[str] = Field(..., alias='audioTracks')
    duration: int
    entity_type: str = Field(..., alias='entityType')
    explore_panel_url: str = Field(..., alias='explorePanelURL')
    explore_tab_name: str = Field(..., alias='exploreTabName')
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
    rating_badge: RatingBadge4 = Field(..., alias='ratingBadge')
    release_date: str = Field(..., alias='releaseDate')
    release_year: int = Field(..., alias='releaseYear')
    reviews: Reviews4
    runtime: str
    subtitles: list[str]
    title_type: str = Field(..., alias='titleType')
    images: Images3

class B0Cjp8Rbmq1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str
    synopsis: str
    audio_tracks: list[str] = Field(..., alias='audioTracks')
    duration: int
    entity_type: str = Field(..., alias='entityType')
    episode_number: int = Field(..., alias='episodeNumber')
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
    images: Images3

class B0Ck832Gg5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str
    synopsis: str
    audio_tracks: list[str] = Field(..., alias='audioTracks')
    duration: int
    entity_type: str = Field(..., alias='entityType')
    episode_number: int = Field(..., alias='episodeNumber')
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
    images: Images3

class B0Chsjdg3Y(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str
    synopsis: str
    audio_tracks: list[str] = Field(..., alias='audioTracks')
    duration: int
    entity_type: str = Field(..., alias='entityType')
    episode_number: int = Field(..., alias='episodeNumber')
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
    images: Images3

class B0Cgpsngts(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str
    synopsis: str
    audio_tracks: list[str] = Field(..., alias='audioTracks')
    duration: int
    entity_type: str = Field(..., alias='entityType')
    episode_number: int = Field(..., alias='episodeNumber')
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
    images: Images3

class B0Chjln6Gs(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str
    synopsis: str
    audio_tracks: list[str] = Field(..., alias='audioTracks')
    duration: int
    entity_type: str = Field(..., alias='entityType')
    episode_number: int = Field(..., alias='episodeNumber')
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
    images: Images3

class B0Chpmk42L(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str
    synopsis: str
    audio_tracks: list[str] = Field(..., alias='audioTracks')
    duration: int
    entity_type: str = Field(..., alias='entityType')
    episode_number: int = Field(..., alias='episodeNumber')
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
    images: Images3

class B0Cjcmt4Xn(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str
    synopsis: str
    audio_tracks: list[str] = Field(..., alias='audioTracks')
    duration: int
    entity_type: str = Field(..., alias='entityType')
    episode_number: int = Field(..., alias='episodeNumber')
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
    images: Images3

class B0Cgx6W4Gk(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str
    synopsis: str
    audio_tracks: list[str] = Field(..., alias='audioTracks')
    duration: int
    entity_type: str = Field(..., alias='entityType')
    episode_number: int = Field(..., alias='episodeNumber')
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
    images: Images3

class B0Ch4Tmyh2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str
    synopsis: str
    audio_tracks: list[str] = Field(..., alias='audioTracks')
    duration: int
    entity_type: str = Field(..., alias='entityType')
    episode_number: int = Field(..., alias='episodeNumber')
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
    images: Images3

class B0Cjqd32Q6(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str
    synopsis: str
    audio_tracks: list[str] = Field(..., alias='audioTracks')
    duration: int
    entity_type: str = Field(..., alias='entityType')
    episode_number: int = Field(..., alias='episodeNumber')
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
    images: Images3

class B0Cj658T6K(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str
    synopsis: str
    audio_tracks: list[str] = Field(..., alias='audioTracks')
    duration: int
    entity_type: str = Field(..., alias='entityType')
    episode_number: int = Field(..., alias='episodeNumber')
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
    images: Images3

class B0Cjq1Pt9T(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str
    synopsis: str
    audio_tracks: list[str] = Field(..., alias='audioTracks')
    duration: int
    entity_type: str = Field(..., alias='entityType')
    episode_number: int = Field(..., alias='episodeNumber')
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
    images: Images3

class RatingBadge5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field__type: str = Field(..., alias='__type')
    description: str
    display_text: str = Field(..., alias='displayText')
    id: str

class FiveStar5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    percentage: int
    percentage_display: str = Field(..., alias='percentageDisplay')
    rating_display_label: str = Field(..., alias='ratingDisplayLabel')

class FourStar5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    percentage: int
    percentage_display: str = Field(..., alias='percentageDisplay')
    rating_display_label: str = Field(..., alias='ratingDisplayLabel')

class OneStar5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    percentage: int
    percentage_display: str = Field(..., alias='percentageDisplay')
    rating_display_label: str = Field(..., alias='ratingDisplayLabel')

class ThreeStar5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    percentage: int
    percentage_display: str = Field(..., alias='percentageDisplay')
    rating_display_label: str = Field(..., alias='ratingDisplayLabel')

class TwoStar5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    percentage: int
    percentage_display: str = Field(..., alias='percentageDisplay')
    rating_display_label: str = Field(..., alias='ratingDisplayLabel')

class RatingsHistogram5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    five_star: FiveStar5 = Field(..., alias='fiveStar')
    four_star: FourStar5 = Field(..., alias='fourStar')
    one_star: OneStar5 = Field(..., alias='oneStar')
    three_star: ThreeStar5 = Field(..., alias='threeStar')
    two_star: TwoStar5 = Field(..., alias='twoStar')

class ReviewsAnalysisModel5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    ratings_histogram: RatingsHistogram5 = Field(..., alias='ratingsHistogram')

class Reviews5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    all_reviews_link: str = Field(..., alias='allReviewsLink')
    create_review_link: str = Field(..., alias='createReviewLink')
    locale_language: str = Field(..., alias='localeLanguage')
    review_submission_token: str = Field(..., alias='reviewSubmissionToken')
    reviews_analysis_model: ReviewsAnalysisModel5 = Field(..., alias='reviewsAnalysisModel')
    title_id: str = Field(..., alias='titleID')

class B0Chf9Mzxz8(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str
    synopsis: str
    audio_tracks: list[None] = Field(..., alias='audioTracks')
    entity_type: str = Field(..., alias='entityType')
    explore_tab_name: str = Field(..., alias='exploreTabName')
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
    parent_title: str = Field(..., alias='parentTitle')
    playback_tracks: list[None] = Field(..., alias='playbackTracks')
    rating_badge: RatingBadge5 = Field(..., alias='ratingBadge')
    release_date: str = Field(..., alias='releaseDate')
    release_year: int = Field(..., alias='releaseYear')
    reviews: Reviews5
    runtime: str
    season_number: int = Field(..., alias='seasonNumber')
    subtitles: list[None]
    title_type: str = Field(..., alias='titleType')
    images: Images3

class Detail2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    b005_c8_dbii: B005C8Dbii1 | None = Field(None, alias='B005C8DBII')
    b005_c8_e538: B005C8E538 | None = Field(None, alias='B005C8E538')
    b005_c8_e70_y: B005C8E70Y | None = Field(None, alias='B005C8E70Y')
    b005_g0_r6_xi: B005G0R6Xi | None = Field(None, alias='B005G0R6XI')
    b005_c8_egx2: B005C8Egx2 | None = Field(None, alias='B005C8EGX2')
    b005_c8_ei62: B005C8Ei62 | None = Field(None, alias='B005C8EI62')
    b005_c8_ec7_m: B005C8Ec7M | None = Field(None, alias='B005C8EC7M')
    b005_c8_egeg: B005C8Egeg | None = Field(None, alias='B005C8EGEG')
    b005_c8_elci: B005C8Elci | None = Field(None, alias='B005C8ELCI')
    b005_c8_ed30: B005C8Ed30 | None = Field(None, alias='B005C8ED30')
    b005_c8_dike: B005C8Dike | None = Field(None, alias='B005C8DIKE')
    b005_c8_ecls: B005C8Ecls | None = Field(None, alias='B005C8ECLS')
    b005_c8_dtto: B005C8Dtto | None = Field(None, alias='B005C8DTTO')
    b005_c8_e91_q: B005C8E91Q | None = Field(None, alias='B005C8E91Q')
    b005_c8_dkvg: B005C8Dkvg | None = Field(None, alias='B005C8DKVG')
    b005_c8_ei5_s: B005C8Ei5S | None = Field(None, alias='B005C8EI5S')
    b005_c8_eiui: B005C8Eiui | None = Field(None, alias='B005C8EIUI')
    b005_c8_emmm: B005C8Emmm | None = Field(None, alias='B005C8EMMM')
    b005_c8_eh2_w: B005C8Eh2W | None = Field(None, alias='B005C8EH2W')
    b005_c8_ebws: B005C8Ebws | None = Field(None, alias='B005C8EBWS')
    b005_c8_ds0_y: B005C8Ds0Y | None = Field(None, alias='B005C8DS0Y')
    b005_c8_e5_a6: B005C8E5A6 | None = Field(None, alias='B005C8E5A6')
    b005_c8_ef8_i: B005C8Ef8I | None = Field(None, alias='B005C8EF8I')
    b005_c8_ek9_m: B005C8Ek9M | None = Field(None, alias='B005C8EK9M')
    b005_c8_db7_e: B005C8Db7E8 | None = Field(None, alias='B005C8DB7E')
    b001_t5_bzao: B001T5Bzao9 | None = Field(None, alias='B001T5BZAO')
    b0_cjp8_rbmq: B0Cjp8Rbmq1 | None = Field(None, alias='B0CJP8RBMQ')
    b0_ck832_gg5: B0Ck832Gg5 | None = Field(None, alias='B0CK832GG5')
    b0_chsjdg3_y: B0Chsjdg3Y | None = Field(None, alias='B0CHSJDG3Y')
    b0_cgpsngts: B0Cgpsngts | None = Field(None, alias='B0CGPSNGTS')
    b0_chjln6_gs: B0Chjln6Gs | None = Field(None, alias='B0CHJLN6GS')
    b0_chpmk42_l: B0Chpmk42L | None = Field(None, alias='B0CHPMK42L')
    b0_cjcmt4_xn: B0Cjcmt4Xn | None = Field(None, alias='B0CJCMT4XN')
    b0_cgx6_w4_gk: B0Cgx6W4Gk | None = Field(None, alias='B0CGX6W4GK')
    b0_ch4_tmyh2: B0Ch4Tmyh2 | None = Field(None, alias='B0CH4TMYH2')
    b0_cjqd32_q6: B0Cjqd32Q6 | None = Field(None, alias='B0CJQD32Q6')
    b0_cj658_t6_k: B0Cj658T6K | None = Field(None, alias='B0CJ658T6K')
    b0_cjq1_pt9_t: B0Cjq1Pt9T | None = Field(None, alias='B0CJQ1PT9T')
    b0_chf9_mzxz: B0Chf9Mzxz8 | None = Field(None, alias='B0CHF9MZXZ')

class Contributors3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    cast: list[CastItem]
    directors: list[Director]
    producers: list[Producer]

class Images42(BaseModel):
    model_config = ConfigDict(defer_build=True)
    covershot: str
    heroshot: str
    packshot: str
    title_logo: str = Field(..., alias='titleLogo')
    titleshot: str

class FiveStar6(BaseModel):
    model_config = ConfigDict(defer_build=True)
    hover_text: str = Field(..., alias='hoverText')
    percentage: int
    percentage_display: str = Field(..., alias='percentageDisplay')
    rating_display_label: str = Field(..., alias='ratingDisplayLabel')
    url: str

class FourStar6(BaseModel):
    model_config = ConfigDict(defer_build=True)
    hover_text: str = Field(..., alias='hoverText')
    percentage: int
    percentage_display: str = Field(..., alias='percentageDisplay')
    rating_display_label: str = Field(..., alias='ratingDisplayLabel')
    url: str

class OneStar6(BaseModel):
    model_config = ConfigDict(defer_build=True)
    hover_text: str = Field(..., alias='hoverText')
    percentage: int
    percentage_display: str = Field(..., alias='percentageDisplay')
    rating_display_label: str = Field(..., alias='ratingDisplayLabel')
    url: str

class ThreeStar6(BaseModel):
    model_config = ConfigDict(defer_build=True)
    hover_text: str = Field(..., alias='hoverText')
    percentage: int
    percentage_display: str = Field(..., alias='percentageDisplay')
    rating_display_label: str = Field(..., alias='ratingDisplayLabel')
    url: str

class TwoStar6(BaseModel):
    model_config = ConfigDict(defer_build=True)
    hover_text: str = Field(..., alias='hoverText')
    percentage: int
    percentage_display: str = Field(..., alias='percentageDisplay')
    rating_display_label: str = Field(..., alias='ratingDisplayLabel')
    url: str

class RatingsHistogram6(BaseModel):
    model_config = ConfigDict(defer_build=True)
    five_star: FiveStar6 = Field(..., alias='fiveStar')
    four_star: FourStar6 = Field(..., alias='fourStar')
    one_star: OneStar6 = Field(..., alias='oneStar')
    three_star: ThreeStar6 = Field(..., alias='threeStar')
    two_star: TwoStar6 = Field(..., alias='twoStar')

class ReviewsAnalysisModel6(BaseModel):
    model_config = ConfigDict(defer_build=True)
    ratings_histogram: RatingsHistogram6 = Field(..., alias='ratingsHistogram')
    review_rating_info: ReviewRatingInfo = Field(..., alias='reviewRatingInfo')

class Reviews6(BaseModel):
    model_config = ConfigDict(defer_build=True)
    all_reviews_link: str = Field(..., alias='allReviewsLink')
    create_review_link: str = Field(..., alias='createReviewLink')
    locale_language: str = Field(..., alias='localeLanguage')
    review_submission_token: str = Field(..., alias='reviewSubmissionToken')
    reviews_analysis_model: ReviewsAnalysisModel6 = Field(..., alias='reviewsAnalysisModel')
    title_id: str = Field(..., alias='titleID')

class B005C8Db7E9(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str
    synopsis: str
    amazon_rating: AmazonRating = Field(..., alias='amazonRating')
    audio_tracks: list[None] = Field(..., alias='audioTracks')
    catalog_id: str = Field(..., alias='catalogId')
    contributors: Contributors3
    enhanced_subtitles: list[None] = Field(..., alias='enhancedSubtitles')
    entity_type: str = Field(..., alias='entityType')
    explore_panel_url: str = Field(..., alias='explorePanelURL')
    explore_tab_name: str = Field(..., alias='exploreTabName')
    genres: list[Genre]
    images: Images42
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
    parent_title: str = Field(..., alias='parentTitle')
    playback_tracks: list[None] = Field(..., alias='playbackTracks')
    rating_badge: RatingBadge5 = Field(..., alias='ratingBadge')
    release_date: str = Field(..., alias='releaseDate')
    release_year: int = Field(..., alias='releaseYear')
    reviews: Reviews6
    runtime: str
    season_number: int = Field(..., alias='seasonNumber')
    studios: list[str]
    subtitles: list[None]
    title_type: str = Field(..., alias='titleType')

class Contributors4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    cast: list[CastItem]
    directors: list[Director]
    producers: list[Producer]

class RatingBadge7(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field__type: str = Field(..., alias='__type')
    country_code: str = Field(..., alias='countryCode')
    description: str
    display_text: str = Field(..., alias='displayText')
    id: str

class RatingsHistogram7(BaseModel):
    model_config = ConfigDict(defer_build=True)
    five_star: FiveStar6 = Field(..., alias='fiveStar')
    four_star: FourStar6 = Field(..., alias='fourStar')
    one_star: OneStar6 = Field(..., alias='oneStar')
    three_star: ThreeStar6 = Field(..., alias='threeStar')
    two_star: TwoStar6 = Field(..., alias='twoStar')

class ReviewsAnalysisModel7(BaseModel):
    model_config = ConfigDict(defer_build=True)
    ratings_histogram: RatingsHistogram7 = Field(..., alias='ratingsHistogram')
    review_rating_info: ReviewRatingInfo = Field(..., alias='reviewRatingInfo')

class Reviews7(BaseModel):
    model_config = ConfigDict(defer_build=True)
    all_reviews_link: str = Field(..., alias='allReviewsLink')
    create_review_link: str = Field(..., alias='createReviewLink')
    locale_language: str = Field(..., alias='localeLanguage')
    review_submission_token: str = Field(..., alias='reviewSubmissionToken')
    reviews_analysis_model: ReviewsAnalysisModel7 = Field(..., alias='reviewsAnalysisModel')
    title_id: str = Field(..., alias='titleID')

class B001T5Bzao10(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str
    synopsis: str
    amazon_rating: AmazonRating = Field(..., alias='amazonRating')
    audio_tracks: list[str] = Field(..., alias='audioTracks')
    catalog_id: str = Field(..., alias='catalogId')
    contributors: Contributors4
    duration: int
    enhanced_subtitles: list[EnhancedSubtitle] = Field(..., alias='enhancedSubtitles')
    entity_type: str = Field(..., alias='entityType')
    explore_panel_url: str = Field(..., alias='explorePanelURL')
    explore_tab_name: str = Field(..., alias='exploreTabName')
    genres: list[Genre]
    images: Images42
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
    rating_badge: RatingBadge7 = Field(..., alias='ratingBadge')
    release_date: str = Field(..., alias='releaseDate')
    release_year: int = Field(..., alias='releaseYear')
    reviews: Reviews7
    runtime: str
    studios: list[str]
    subtitles: list[str]
    title_type: str = Field(..., alias='titleType')

class Contributors5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    cast: list[CastItem]
    directors: list[Director]
    producers: list[None]

class RatingBadge8(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field__type: str = Field(..., alias='__type')
    description: str
    display_text: str = Field(..., alias='displayText')
    id: str

class FiveStar8(BaseModel):
    model_config = ConfigDict(defer_build=True)
    percentage: int
    percentage_display: str = Field(..., alias='percentageDisplay')
    rating_display_label: str = Field(..., alias='ratingDisplayLabel')

class FourStar8(BaseModel):
    model_config = ConfigDict(defer_build=True)
    percentage: int
    percentage_display: str = Field(..., alias='percentageDisplay')
    rating_display_label: str = Field(..., alias='ratingDisplayLabel')

class OneStar8(BaseModel):
    model_config = ConfigDict(defer_build=True)
    percentage: int
    percentage_display: str = Field(..., alias='percentageDisplay')
    rating_display_label: str = Field(..., alias='ratingDisplayLabel')

class ThreeStar8(BaseModel):
    model_config = ConfigDict(defer_build=True)
    percentage: int
    percentage_display: str = Field(..., alias='percentageDisplay')
    rating_display_label: str = Field(..., alias='ratingDisplayLabel')

class TwoStar8(BaseModel):
    model_config = ConfigDict(defer_build=True)
    percentage: int
    percentage_display: str = Field(..., alias='percentageDisplay')
    rating_display_label: str = Field(..., alias='ratingDisplayLabel')

class RatingsHistogram8(BaseModel):
    model_config = ConfigDict(defer_build=True)
    five_star: FiveStar8 = Field(..., alias='fiveStar')
    four_star: FourStar8 = Field(..., alias='fourStar')
    one_star: OneStar8 = Field(..., alias='oneStar')
    three_star: ThreeStar8 = Field(..., alias='threeStar')
    two_star: TwoStar8 = Field(..., alias='twoStar')

class ReviewsAnalysisModel8(BaseModel):
    model_config = ConfigDict(defer_build=True)
    ratings_histogram: RatingsHistogram8 = Field(..., alias='ratingsHistogram')

class Reviews8(BaseModel):
    model_config = ConfigDict(defer_build=True)
    all_reviews_link: str = Field(..., alias='allReviewsLink')
    create_review_link: str = Field(..., alias='createReviewLink')
    locale_language: str = Field(..., alias='localeLanguage')
    review_submission_token: str = Field(..., alias='reviewSubmissionToken')
    reviews_analysis_model: ReviewsAnalysisModel8 = Field(..., alias='reviewsAnalysisModel')
    title_id: str = Field(..., alias='titleID')

class B0Chf9Mzxz9(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str
    synopsis: str
    audio_tracks: list[None] = Field(..., alias='audioTracks')
    catalog_id: str = Field(..., alias='catalogId')
    contributors: Contributors5
    enhanced_subtitles: list[None] = Field(..., alias='enhancedSubtitles')
    entity_type: str = Field(..., alias='entityType')
    explore_tab_name: str = Field(..., alias='exploreTabName')
    genres: list[Genre]
    images: Images42
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
    parent_title: str = Field(..., alias='parentTitle')
    playback_tracks: list[None] = Field(..., alias='playbackTracks')
    rating_badge: RatingBadge8 = Field(..., alias='ratingBadge')
    release_date: str = Field(..., alias='releaseDate')
    release_year: int = Field(..., alias='releaseYear')
    reviews: Reviews8
    runtime: str
    season_number: int = Field(..., alias='seasonNumber')
    studios: list[str]
    subtitles: list[None]
    title_type: str = Field(..., alias='titleType')

class BtfMoreDetails(BaseModel):
    model_config = ConfigDict(defer_build=True)
    b005_c8_db7_e: B005C8Db7E9 | None = Field(None, alias='B005C8DB7E')
    b001_t5_bzao: B001T5Bzao10 | None = Field(None, alias='B001T5BZAO')
    b0_chf9_mzxz: B0Chf9Mzxz9 | None = Field(None, alias='B0CHF9MZXZ')

class Detail1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    detail: Detail2
    header_detail: dict[str, Any] = Field(..., alias='headerDetail')
    btf_more_details: BtfMoreDetails = Field(..., alias='btfMoreDetails')

class FocusMessage3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    dv_message: DvMessage = Field(..., alias='dvMessage')
    icon: str
    icon_type: str = Field(..., alias='iconType')

class Messages3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    entitlement_type: str = Field(..., alias='entitlementType')
    focus_message: FocusMessage3 = Field(..., alias='focusMessage')

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

class Payload9(BaseModel):
    model_config = ConfigDict(defer_build=True)
    payload_type: str = Field(..., alias='payloadType')
    transaction: Transaction3

class Presentation6(BaseModel):
    model_config = ConfigDict(defer_build=True)
    icon: str
    primary_label: str = Field(..., alias='primaryLabel')
    ref_marker: str = Field(..., alias='refMarker')

class Action6(BaseModel):
    model_config = ConfigDict(defer_build=True)
    action_type: str = Field(..., alias='actionType')
    is_selected: bool = Field(..., alias='isSelected')
    payload: Payload9
    presentation: Presentation6

class ComponentPayload10(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_component: TextComponent6 = Field(..., alias='textComponent')

class TransactionDetail4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload10 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class ComponentPayload11(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_component: TextComponent6 = Field(..., alias='textComponent')

class Header3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload11 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class Components4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    transaction_detail: TransactionDetail4 = Field(..., alias='TRANSACTION_DETAIL')
    header: Header3 = Field(..., alias='HEADER')

class ExpandingCard3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    actions: list[Action6]
    card_type: str = Field(..., alias='cardType')
    components: Components4

class Transaction4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    asin: str
    csrf_token: str = Field(..., alias='csrfToken')
    csrf_token_workflow: str = Field(..., alias='csrfTokenWorkflow')
    display_messages: list[None] = Field(..., alias='displayMessages')
    label: str
    offer_token: str = Field(..., alias='offerToken')
    purchase_data: PurchaseData = Field(..., alias='purchaseData')
    ref_marker: str = Field(..., alias='refMarker')

class Payload10(BaseModel):
    model_config = ConfigDict(defer_build=True)
    payload_type: str = Field(..., alias='payloadType')
    transaction: Transaction4

class Action7(BaseModel):
    model_config = ConfigDict(defer_build=True)
    action_type: str = Field(..., alias='actionType')
    is_selected: bool = Field(..., alias='isSelected')
    payload: Payload10
    presentation: Presentation6

class TextComponentCollection1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_list: list[TextListItem] = Field(..., alias='textList')

class ComponentPayload12(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_component_collection: TextComponentCollection1 = Field(..., alias='textComponentCollection')

class TransactionDetail5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload12 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class Tags3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    brand_glow: str = Field(..., alias='BRAND_GLOW')
    text_theme: str = Field(..., alias='TEXT_THEME')

class TextComponent9(BaseModel):
    model_config = ConfigDict(defer_build=True)
    tags: Tags3
    text: str
    text_type: str = Field(..., alias='textType')

class ComponentPayload13(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_component: TextComponent9 = Field(..., alias='textComponent')

class Banner2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload13 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class Components5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    transaction_detail: TransactionDetail5 = Field(..., alias='TRANSACTION_DETAIL')
    banner: Banner2 = Field(..., alias='BANNER')

class CardOption1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    actions: list[Action7]
    card_type: str = Field(..., alias='cardType')
    components: Components5

class Payload8(BaseModel):
    model_config = ConfigDict(defer_build=True)
    expanding_card: ExpandingCard3 | None = Field(None, alias='expandingCard')
    payload_type: str = Field(..., alias='payloadType')
    card_options: list[CardOption1] | None = Field(None, alias='cardOptions')

class Presentation8(BaseModel):
    model_config = ConfigDict(defer_build=True)
    primary_label: str = Field(..., alias='primaryLabel')
    ref_marker: str = Field(..., alias='refMarker')

class PrimaryAction3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    action_type: str = Field(..., alias='actionType')
    is_selected: bool = Field(..., alias='isSelected')
    payload: Payload8
    presentation: Presentation8 | None = None

class B005C8Dbii2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    messages: Messages3
    primary_actions: list[PrimaryAction3] = Field(..., alias='primaryActions')
    secondary_actions: list[None] = Field(..., alias='secondaryActions')
    view_ref_marker: str = Field(..., alias='viewRefMarker')

class FocusMessage4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    dv_message: DvMessage = Field(..., alias='dvMessage')
    icon: str
    icon_type: str = Field(..., alias='iconType')

class Messages4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    entitlement_type: str = Field(..., alias='entitlementType')
    focus_message: FocusMessage4 = Field(..., alias='focusMessage')

class Transaction5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    asin: str
    csrf_token: str = Field(..., alias='csrfToken')
    csrf_token_workflow: str = Field(..., alias='csrfTokenWorkflow')
    display_messages: list[None] = Field(..., alias='displayMessages')
    label: str
    offer_token: str = Field(..., alias='offerToken')
    purchase_data: PurchaseData = Field(..., alias='purchaseData')
    ref_marker: str = Field(..., alias='refMarker')

class Payload12(BaseModel):
    model_config = ConfigDict(defer_build=True)
    payload_type: str = Field(..., alias='payloadType')
    transaction: Transaction5

class Presentation9(BaseModel):
    model_config = ConfigDict(defer_build=True)
    icon: str
    primary_label: str = Field(..., alias='primaryLabel')
    ref_marker: str = Field(..., alias='refMarker')

class Action8(BaseModel):
    model_config = ConfigDict(defer_build=True)
    action_type: str = Field(..., alias='actionType')
    is_selected: bool = Field(..., alias='isSelected')
    payload: Payload12
    presentation: Presentation9

class TextComponent10(BaseModel):
    model_config = ConfigDict(defer_build=True)
    tags: dict[str, Any]
    text: str
    text_type: str = Field(..., alias='textType')

class ComponentPayload14(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_component: TextComponent10 = Field(..., alias='textComponent')

class TransactionDetail6(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload14 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class ComponentPayload15(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_component: TextComponent10 = Field(..., alias='textComponent')

class Header4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload15 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class Components6(BaseModel):
    model_config = ConfigDict(defer_build=True)
    transaction_detail: TransactionDetail6 = Field(..., alias='TRANSACTION_DETAIL')
    header: Header4 = Field(..., alias='HEADER')

class ExpandingCard4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    actions: list[Action8]
    card_type: str = Field(..., alias='cardType')
    components: Components6

class Transaction6(BaseModel):
    model_config = ConfigDict(defer_build=True)
    asin: str
    csrf_token: str = Field(..., alias='csrfToken')
    csrf_token_workflow: str = Field(..., alias='csrfTokenWorkflow')
    display_messages: list[None] = Field(..., alias='displayMessages')
    label: str
    offer_token: str = Field(..., alias='offerToken')
    purchase_data: PurchaseData = Field(..., alias='purchaseData')
    ref_marker: str = Field(..., alias='refMarker')

class Payload13(BaseModel):
    model_config = ConfigDict(defer_build=True)
    payload_type: str = Field(..., alias='payloadType')
    transaction: Transaction6

class Action9(BaseModel):
    model_config = ConfigDict(defer_build=True)
    action_type: str = Field(..., alias='actionType')
    is_selected: bool = Field(..., alias='isSelected')
    payload: Payload13
    presentation: Presentation9

class TextComponentCollection2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_list: list[TextListItem] = Field(..., alias='textList')

class ComponentPayload16(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_component_collection: TextComponentCollection2 = Field(..., alias='textComponentCollection')

class TransactionDetail7(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload16 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class TextComponent12(BaseModel):
    model_config = ConfigDict(defer_build=True)
    tags: Tags3
    text: str
    text_type: str = Field(..., alias='textType')

class ComponentPayload17(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_component: TextComponent12 = Field(..., alias='textComponent')

class Banner3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload17 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class Components7(BaseModel):
    model_config = ConfigDict(defer_build=True)
    transaction_detail: TransactionDetail7 = Field(..., alias='TRANSACTION_DETAIL')
    banner: Banner3 = Field(..., alias='BANNER')

class CardOption2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    actions: list[Action9]
    card_type: str = Field(..., alias='cardType')
    components: Components7

class Payload11(BaseModel):
    model_config = ConfigDict(defer_build=True)
    expanding_card: ExpandingCard4 | None = Field(None, alias='expandingCard')
    payload_type: str = Field(..., alias='payloadType')
    card_options: list[CardOption2] | None = Field(None, alias='cardOptions')

class Presentation11(BaseModel):
    model_config = ConfigDict(defer_build=True)
    primary_label: str = Field(..., alias='primaryLabel')
    ref_marker: str = Field(..., alias='refMarker')

class PrimaryAction4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    action_type: str = Field(..., alias='actionType')
    is_selected: bool = Field(..., alias='isSelected')
    payload: Payload11
    presentation: Presentation11 | None = None

class B005C8E5381(BaseModel):
    model_config = ConfigDict(defer_build=True)
    messages: Messages4
    primary_actions: list[PrimaryAction4] = Field(..., alias='primaryActions')
    secondary_actions: list[None] = Field(..., alias='secondaryActions')
    view_ref_marker: str = Field(..., alias='viewRefMarker')

class FocusMessage5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    dv_message: DvMessage = Field(..., alias='dvMessage')
    icon: str
    icon_type: str = Field(..., alias='iconType')

class Messages5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    entitlement_type: str = Field(..., alias='entitlementType')
    focus_message: FocusMessage5 = Field(..., alias='focusMessage')

class Transaction7(BaseModel):
    model_config = ConfigDict(defer_build=True)
    asin: str
    csrf_token: str = Field(..., alias='csrfToken')
    csrf_token_workflow: str = Field(..., alias='csrfTokenWorkflow')
    display_messages: list[None] = Field(..., alias='displayMessages')
    label: str
    offer_token: str = Field(..., alias='offerToken')
    purchase_data: PurchaseData = Field(..., alias='purchaseData')
    ref_marker: str = Field(..., alias='refMarker')

class Payload15(BaseModel):
    model_config = ConfigDict(defer_build=True)
    payload_type: str = Field(..., alias='payloadType')
    transaction: Transaction7

class Presentation12(BaseModel):
    model_config = ConfigDict(defer_build=True)
    icon: str
    primary_label: str = Field(..., alias='primaryLabel')
    ref_marker: str = Field(..., alias='refMarker')

class Action10(BaseModel):
    model_config = ConfigDict(defer_build=True)
    action_type: str = Field(..., alias='actionType')
    is_selected: bool = Field(..., alias='isSelected')
    payload: Payload15
    presentation: Presentation12

class TextComponent13(BaseModel):
    model_config = ConfigDict(defer_build=True)
    tags: dict[str, Any]
    text: str
    text_type: str = Field(..., alias='textType')

class ComponentPayload18(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_component: TextComponent13 = Field(..., alias='textComponent')

class TransactionDetail8(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload18 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class ComponentPayload19(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_component: TextComponent13 = Field(..., alias='textComponent')

class Header5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload19 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class Components8(BaseModel):
    model_config = ConfigDict(defer_build=True)
    transaction_detail: TransactionDetail8 = Field(..., alias='TRANSACTION_DETAIL')
    header: Header5 = Field(..., alias='HEADER')

class ExpandingCard5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    actions: list[Action10]
    card_type: str = Field(..., alias='cardType')
    components: Components8

class Transaction8(BaseModel):
    model_config = ConfigDict(defer_build=True)
    asin: str
    csrf_token: str = Field(..., alias='csrfToken')
    csrf_token_workflow: str = Field(..., alias='csrfTokenWorkflow')
    display_messages: list[None] = Field(..., alias='displayMessages')
    label: str
    offer_token: str = Field(..., alias='offerToken')
    purchase_data: PurchaseData = Field(..., alias='purchaseData')
    ref_marker: str = Field(..., alias='refMarker')

class Payload16(BaseModel):
    model_config = ConfigDict(defer_build=True)
    payload_type: str = Field(..., alias='payloadType')
    transaction: Transaction8

class Action11(BaseModel):
    model_config = ConfigDict(defer_build=True)
    action_type: str = Field(..., alias='actionType')
    is_selected: bool = Field(..., alias='isSelected')
    payload: Payload16
    presentation: Presentation12

class TextComponentCollection3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_list: list[TextListItem] = Field(..., alias='textList')

class ComponentPayload20(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_component_collection: TextComponentCollection3 = Field(..., alias='textComponentCollection')

class TransactionDetail9(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload20 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class TextComponent15(BaseModel):
    model_config = ConfigDict(defer_build=True)
    tags: Tags3
    text: str
    text_type: str = Field(..., alias='textType')

class ComponentPayload21(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_component: TextComponent15 = Field(..., alias='textComponent')

class Banner4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload21 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class Components9(BaseModel):
    model_config = ConfigDict(defer_build=True)
    transaction_detail: TransactionDetail9 = Field(..., alias='TRANSACTION_DETAIL')
    banner: Banner4 = Field(..., alias='BANNER')

class CardOption3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    actions: list[Action11]
    card_type: str = Field(..., alias='cardType')
    components: Components9

class Payload14(BaseModel):
    model_config = ConfigDict(defer_build=True)
    expanding_card: ExpandingCard5 | None = Field(None, alias='expandingCard')
    payload_type: str = Field(..., alias='payloadType')
    card_options: list[CardOption3] | None = Field(None, alias='cardOptions')

class Presentation14(BaseModel):
    model_config = ConfigDict(defer_build=True)
    primary_label: str = Field(..., alias='primaryLabel')
    ref_marker: str = Field(..., alias='refMarker')

class PrimaryAction5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    action_type: str = Field(..., alias='actionType')
    is_selected: bool = Field(..., alias='isSelected')
    payload: Payload14
    presentation: Presentation14 | None = None

class B005C8E70Y1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    messages: Messages5
    primary_actions: list[PrimaryAction5] = Field(..., alias='primaryActions')
    secondary_actions: list[None] = Field(..., alias='secondaryActions')
    view_ref_marker: str = Field(..., alias='viewRefMarker')

class FocusMessage6(BaseModel):
    model_config = ConfigDict(defer_build=True)
    dv_message: DvMessage = Field(..., alias='dvMessage')
    icon: str
    icon_type: str = Field(..., alias='iconType')

class Messages6(BaseModel):
    model_config = ConfigDict(defer_build=True)
    entitlement_type: str = Field(..., alias='entitlementType')
    focus_message: FocusMessage6 = Field(..., alias='focusMessage')

class Transaction9(BaseModel):
    model_config = ConfigDict(defer_build=True)
    asin: str
    csrf_token: str = Field(..., alias='csrfToken')
    csrf_token_workflow: str = Field(..., alias='csrfTokenWorkflow')
    display_messages: list[None] = Field(..., alias='displayMessages')
    label: str
    offer_token: str = Field(..., alias='offerToken')
    purchase_data: PurchaseData = Field(..., alias='purchaseData')
    ref_marker: str = Field(..., alias='refMarker')

class Payload18(BaseModel):
    model_config = ConfigDict(defer_build=True)
    payload_type: str = Field(..., alias='payloadType')
    transaction: Transaction9

class Presentation15(BaseModel):
    model_config = ConfigDict(defer_build=True)
    icon: str
    primary_label: str = Field(..., alias='primaryLabel')
    ref_marker: str = Field(..., alias='refMarker')

class Action12(BaseModel):
    model_config = ConfigDict(defer_build=True)
    action_type: str = Field(..., alias='actionType')
    is_selected: bool = Field(..., alias='isSelected')
    payload: Payload18
    presentation: Presentation15

class TextComponent16(BaseModel):
    model_config = ConfigDict(defer_build=True)
    tags: dict[str, Any]
    text: str
    text_type: str = Field(..., alias='textType')

class ComponentPayload22(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_component: TextComponent16 = Field(..., alias='textComponent')

class TransactionDetail10(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload22 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class ComponentPayload23(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_component: TextComponent16 = Field(..., alias='textComponent')

class Header6(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload23 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class Components10(BaseModel):
    model_config = ConfigDict(defer_build=True)
    transaction_detail: TransactionDetail10 = Field(..., alias='TRANSACTION_DETAIL')
    header: Header6 = Field(..., alias='HEADER')

class ExpandingCard6(BaseModel):
    model_config = ConfigDict(defer_build=True)
    actions: list[Action12]
    card_type: str = Field(..., alias='cardType')
    components: Components10

class Transaction10(BaseModel):
    model_config = ConfigDict(defer_build=True)
    asin: str
    csrf_token: str = Field(..., alias='csrfToken')
    csrf_token_workflow: str = Field(..., alias='csrfTokenWorkflow')
    display_messages: list[None] = Field(..., alias='displayMessages')
    label: str
    offer_token: str = Field(..., alias='offerToken')
    purchase_data: PurchaseData = Field(..., alias='purchaseData')
    ref_marker: str = Field(..., alias='refMarker')

class Payload19(BaseModel):
    model_config = ConfigDict(defer_build=True)
    payload_type: str = Field(..., alias='payloadType')
    transaction: Transaction10

class Action13(BaseModel):
    model_config = ConfigDict(defer_build=True)
    action_type: str = Field(..., alias='actionType')
    is_selected: bool = Field(..., alias='isSelected')
    payload: Payload19
    presentation: Presentation15

class TextComponentCollection4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_list: list[TextListItem] = Field(..., alias='textList')

class ComponentPayload24(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_component_collection: TextComponentCollection4 = Field(..., alias='textComponentCollection')

class TransactionDetail11(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload24 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class TextComponent18(BaseModel):
    model_config = ConfigDict(defer_build=True)
    tags: Tags3
    text: str
    text_type: str = Field(..., alias='textType')

class ComponentPayload25(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_component: TextComponent18 = Field(..., alias='textComponent')

class Banner5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload25 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class Components11(BaseModel):
    model_config = ConfigDict(defer_build=True)
    transaction_detail: TransactionDetail11 = Field(..., alias='TRANSACTION_DETAIL')
    banner: Banner5 = Field(..., alias='BANNER')

class CardOption4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    actions: list[Action13]
    card_type: str = Field(..., alias='cardType')
    components: Components11

class Payload17(BaseModel):
    model_config = ConfigDict(defer_build=True)
    expanding_card: ExpandingCard6 | None = Field(None, alias='expandingCard')
    payload_type: str = Field(..., alias='payloadType')
    card_options: list[CardOption4] | None = Field(None, alias='cardOptions')

class Presentation17(BaseModel):
    model_config = ConfigDict(defer_build=True)
    primary_label: str = Field(..., alias='primaryLabel')
    ref_marker: str = Field(..., alias='refMarker')

class PrimaryAction6(BaseModel):
    model_config = ConfigDict(defer_build=True)
    action_type: str = Field(..., alias='actionType')
    is_selected: bool = Field(..., alias='isSelected')
    payload: Payload17
    presentation: Presentation17 | None = None

class B005G0R6Xi1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    messages: Messages6
    primary_actions: list[PrimaryAction6] = Field(..., alias='primaryActions')
    secondary_actions: list[None] = Field(..., alias='secondaryActions')
    view_ref_marker: str = Field(..., alias='viewRefMarker')

class FocusMessage7(BaseModel):
    model_config = ConfigDict(defer_build=True)
    dv_message: DvMessage = Field(..., alias='dvMessage')
    icon: str
    icon_type: str = Field(..., alias='iconType')

class Messages7(BaseModel):
    model_config = ConfigDict(defer_build=True)
    entitlement_type: str = Field(..., alias='entitlementType')
    focus_message: FocusMessage7 = Field(..., alias='focusMessage')

class Transaction11(BaseModel):
    model_config = ConfigDict(defer_build=True)
    asin: str
    csrf_token: str = Field(..., alias='csrfToken')
    csrf_token_workflow: str = Field(..., alias='csrfTokenWorkflow')
    display_messages: list[None] = Field(..., alias='displayMessages')
    label: str
    offer_token: str = Field(..., alias='offerToken')
    purchase_data: PurchaseData = Field(..., alias='purchaseData')
    ref_marker: str = Field(..., alias='refMarker')

class Payload21(BaseModel):
    model_config = ConfigDict(defer_build=True)
    payload_type: str = Field(..., alias='payloadType')
    transaction: Transaction11

class Presentation18(BaseModel):
    model_config = ConfigDict(defer_build=True)
    icon: str
    primary_label: str = Field(..., alias='primaryLabel')
    ref_marker: str = Field(..., alias='refMarker')

class Action14(BaseModel):
    model_config = ConfigDict(defer_build=True)
    action_type: str = Field(..., alias='actionType')
    is_selected: bool = Field(..., alias='isSelected')
    payload: Payload21
    presentation: Presentation18

class TextComponent19(BaseModel):
    model_config = ConfigDict(defer_build=True)
    tags: dict[str, Any]
    text: str
    text_type: str = Field(..., alias='textType')

class ComponentPayload26(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_component: TextComponent19 = Field(..., alias='textComponent')

class TransactionDetail12(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload26 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class ComponentPayload27(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_component: TextComponent19 = Field(..., alias='textComponent')

class Header7(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload27 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class Components12(BaseModel):
    model_config = ConfigDict(defer_build=True)
    transaction_detail: TransactionDetail12 = Field(..., alias='TRANSACTION_DETAIL')
    header: Header7 = Field(..., alias='HEADER')

class ExpandingCard7(BaseModel):
    model_config = ConfigDict(defer_build=True)
    actions: list[Action14]
    card_type: str = Field(..., alias='cardType')
    components: Components12

class Transaction12(BaseModel):
    model_config = ConfigDict(defer_build=True)
    asin: str
    csrf_token: str = Field(..., alias='csrfToken')
    csrf_token_workflow: str = Field(..., alias='csrfTokenWorkflow')
    display_messages: list[None] = Field(..., alias='displayMessages')
    label: str
    offer_token: str = Field(..., alias='offerToken')
    purchase_data: PurchaseData = Field(..., alias='purchaseData')
    ref_marker: str = Field(..., alias='refMarker')

class Payload22(BaseModel):
    model_config = ConfigDict(defer_build=True)
    payload_type: str = Field(..., alias='payloadType')
    transaction: Transaction12

class Action15(BaseModel):
    model_config = ConfigDict(defer_build=True)
    action_type: str = Field(..., alias='actionType')
    is_selected: bool = Field(..., alias='isSelected')
    payload: Payload22
    presentation: Presentation18

class TextComponentCollection5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_list: list[TextListItem] = Field(..., alias='textList')

class ComponentPayload28(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_component_collection: TextComponentCollection5 = Field(..., alias='textComponentCollection')

class TransactionDetail13(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload28 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class TextComponent21(BaseModel):
    model_config = ConfigDict(defer_build=True)
    tags: Tags3
    text: str
    text_type: str = Field(..., alias='textType')

class ComponentPayload29(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_component: TextComponent21 = Field(..., alias='textComponent')

class Banner6(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload29 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class Components13(BaseModel):
    model_config = ConfigDict(defer_build=True)
    transaction_detail: TransactionDetail13 = Field(..., alias='TRANSACTION_DETAIL')
    banner: Banner6 = Field(..., alias='BANNER')

class CardOption5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    actions: list[Action15]
    card_type: str = Field(..., alias='cardType')
    components: Components13

class Payload20(BaseModel):
    model_config = ConfigDict(defer_build=True)
    expanding_card: ExpandingCard7 | None = Field(None, alias='expandingCard')
    payload_type: str = Field(..., alias='payloadType')
    card_options: list[CardOption5] | None = Field(None, alias='cardOptions')

class Presentation20(BaseModel):
    model_config = ConfigDict(defer_build=True)
    primary_label: str = Field(..., alias='primaryLabel')
    ref_marker: str = Field(..., alias='refMarker')

class PrimaryAction7(BaseModel):
    model_config = ConfigDict(defer_build=True)
    action_type: str = Field(..., alias='actionType')
    is_selected: bool = Field(..., alias='isSelected')
    payload: Payload20
    presentation: Presentation20 | None = None

class B005C8Egx21(BaseModel):
    model_config = ConfigDict(defer_build=True)
    messages: Messages7
    primary_actions: list[PrimaryAction7] = Field(..., alias='primaryActions')
    secondary_actions: list[None] = Field(..., alias='secondaryActions')
    view_ref_marker: str = Field(..., alias='viewRefMarker')

class FocusMessage8(BaseModel):
    model_config = ConfigDict(defer_build=True)
    dv_message: DvMessage = Field(..., alias='dvMessage')
    icon: str
    icon_type: str = Field(..., alias='iconType')

class Messages8(BaseModel):
    model_config = ConfigDict(defer_build=True)
    entitlement_type: str = Field(..., alias='entitlementType')
    focus_message: FocusMessage8 = Field(..., alias='focusMessage')

class Transaction13(BaseModel):
    model_config = ConfigDict(defer_build=True)
    asin: str
    csrf_token: str = Field(..., alias='csrfToken')
    csrf_token_workflow: str = Field(..., alias='csrfTokenWorkflow')
    display_messages: list[None] = Field(..., alias='displayMessages')
    label: str
    offer_token: str = Field(..., alias='offerToken')
    purchase_data: PurchaseData = Field(..., alias='purchaseData')
    ref_marker: str = Field(..., alias='refMarker')

class Payload24(BaseModel):
    model_config = ConfigDict(defer_build=True)
    payload_type: str = Field(..., alias='payloadType')
    transaction: Transaction13

class Presentation21(BaseModel):
    model_config = ConfigDict(defer_build=True)
    icon: str
    primary_label: str = Field(..., alias='primaryLabel')
    ref_marker: str = Field(..., alias='refMarker')

class Action16(BaseModel):
    model_config = ConfigDict(defer_build=True)
    action_type: str = Field(..., alias='actionType')
    is_selected: bool = Field(..., alias='isSelected')
    payload: Payload24
    presentation: Presentation21

class TextComponent22(BaseModel):
    model_config = ConfigDict(defer_build=True)
    tags: dict[str, Any]
    text: str
    text_type: str = Field(..., alias='textType')

class ComponentPayload30(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_component: TextComponent22 = Field(..., alias='textComponent')

class TransactionDetail14(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload30 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class ComponentPayload31(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_component: TextComponent22 = Field(..., alias='textComponent')

class Header8(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload31 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class Components14(BaseModel):
    model_config = ConfigDict(defer_build=True)
    transaction_detail: TransactionDetail14 = Field(..., alias='TRANSACTION_DETAIL')
    header: Header8 = Field(..., alias='HEADER')

class ExpandingCard8(BaseModel):
    model_config = ConfigDict(defer_build=True)
    actions: list[Action16]
    card_type: str = Field(..., alias='cardType')
    components: Components14

class Transaction14(BaseModel):
    model_config = ConfigDict(defer_build=True)
    asin: str
    csrf_token: str = Field(..., alias='csrfToken')
    csrf_token_workflow: str = Field(..., alias='csrfTokenWorkflow')
    display_messages: list[None] = Field(..., alias='displayMessages')
    label: str
    offer_token: str = Field(..., alias='offerToken')
    purchase_data: PurchaseData = Field(..., alias='purchaseData')
    ref_marker: str = Field(..., alias='refMarker')

class Payload25(BaseModel):
    model_config = ConfigDict(defer_build=True)
    payload_type: str = Field(..., alias='payloadType')
    transaction: Transaction14

class Action17(BaseModel):
    model_config = ConfigDict(defer_build=True)
    action_type: str = Field(..., alias='actionType')
    is_selected: bool = Field(..., alias='isSelected')
    payload: Payload25
    presentation: Presentation21

class TextComponentCollection6(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_list: list[TextListItem] = Field(..., alias='textList')

class ComponentPayload32(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_component_collection: TextComponentCollection6 = Field(..., alias='textComponentCollection')

class TransactionDetail15(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload32 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class TextComponent24(BaseModel):
    model_config = ConfigDict(defer_build=True)
    tags: Tags3
    text: str
    text_type: str = Field(..., alias='textType')

class ComponentPayload33(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_component: TextComponent24 = Field(..., alias='textComponent')

class Banner7(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload33 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class Components15(BaseModel):
    model_config = ConfigDict(defer_build=True)
    transaction_detail: TransactionDetail15 = Field(..., alias='TRANSACTION_DETAIL')
    banner: Banner7 = Field(..., alias='BANNER')

class CardOption6(BaseModel):
    model_config = ConfigDict(defer_build=True)
    actions: list[Action17]
    card_type: str = Field(..., alias='cardType')
    components: Components15

class Payload23(BaseModel):
    model_config = ConfigDict(defer_build=True)
    expanding_card: ExpandingCard8 | None = Field(None, alias='expandingCard')
    payload_type: str = Field(..., alias='payloadType')
    card_options: list[CardOption6] | None = Field(None, alias='cardOptions')

class Presentation23(BaseModel):
    model_config = ConfigDict(defer_build=True)
    primary_label: str = Field(..., alias='primaryLabel')
    ref_marker: str = Field(..., alias='refMarker')

class PrimaryAction8(BaseModel):
    model_config = ConfigDict(defer_build=True)
    action_type: str = Field(..., alias='actionType')
    is_selected: bool = Field(..., alias='isSelected')
    payload: Payload23
    presentation: Presentation23 | None = None

class B005C8Ei621(BaseModel):
    model_config = ConfigDict(defer_build=True)
    messages: Messages8
    primary_actions: list[PrimaryAction8] = Field(..., alias='primaryActions')
    secondary_actions: list[None] = Field(..., alias='secondaryActions')
    view_ref_marker: str = Field(..., alias='viewRefMarker')

class FocusMessage9(BaseModel):
    model_config = ConfigDict(defer_build=True)
    dv_message: DvMessage = Field(..., alias='dvMessage')
    icon: str
    icon_type: str = Field(..., alias='iconType')

class Messages9(BaseModel):
    model_config = ConfigDict(defer_build=True)
    entitlement_type: str = Field(..., alias='entitlementType')
    focus_message: FocusMessage9 = Field(..., alias='focusMessage')

class Transaction15(BaseModel):
    model_config = ConfigDict(defer_build=True)
    asin: str
    csrf_token: str = Field(..., alias='csrfToken')
    csrf_token_workflow: str = Field(..., alias='csrfTokenWorkflow')
    display_messages: list[None] = Field(..., alias='displayMessages')
    label: str
    offer_token: str = Field(..., alias='offerToken')
    purchase_data: PurchaseData = Field(..., alias='purchaseData')
    ref_marker: str = Field(..., alias='refMarker')

class Payload27(BaseModel):
    model_config = ConfigDict(defer_build=True)
    payload_type: str = Field(..., alias='payloadType')
    transaction: Transaction15

class Presentation24(BaseModel):
    model_config = ConfigDict(defer_build=True)
    icon: str
    primary_label: str = Field(..., alias='primaryLabel')
    ref_marker: str = Field(..., alias='refMarker')

class Action18(BaseModel):
    model_config = ConfigDict(defer_build=True)
    action_type: str = Field(..., alias='actionType')
    is_selected: bool = Field(..., alias='isSelected')
    payload: Payload27
    presentation: Presentation24

class TextComponent25(BaseModel):
    model_config = ConfigDict(defer_build=True)
    tags: dict[str, Any]
    text: str
    text_type: str = Field(..., alias='textType')

class ComponentPayload34(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_component: TextComponent25 = Field(..., alias='textComponent')

class TransactionDetail16(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload34 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class ComponentPayload35(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_component: TextComponent25 = Field(..., alias='textComponent')

class Header9(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload35 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class Components16(BaseModel):
    model_config = ConfigDict(defer_build=True)
    transaction_detail: TransactionDetail16 = Field(..., alias='TRANSACTION_DETAIL')
    header: Header9 = Field(..., alias='HEADER')

class ExpandingCard9(BaseModel):
    model_config = ConfigDict(defer_build=True)
    actions: list[Action18]
    card_type: str = Field(..., alias='cardType')
    components: Components16

class Transaction16(BaseModel):
    model_config = ConfigDict(defer_build=True)
    asin: str
    csrf_token: str = Field(..., alias='csrfToken')
    csrf_token_workflow: str = Field(..., alias='csrfTokenWorkflow')
    display_messages: list[None] = Field(..., alias='displayMessages')
    label: str
    offer_token: str = Field(..., alias='offerToken')
    purchase_data: PurchaseData = Field(..., alias='purchaseData')
    ref_marker: str = Field(..., alias='refMarker')

class Payload28(BaseModel):
    model_config = ConfigDict(defer_build=True)
    payload_type: str = Field(..., alias='payloadType')
    transaction: Transaction16

class Action19(BaseModel):
    model_config = ConfigDict(defer_build=True)
    action_type: str = Field(..., alias='actionType')
    is_selected: bool = Field(..., alias='isSelected')
    payload: Payload28
    presentation: Presentation24

class TextComponentCollection7(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_list: list[TextListItem] = Field(..., alias='textList')

class ComponentPayload36(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_component_collection: TextComponentCollection7 = Field(..., alias='textComponentCollection')

class TransactionDetail17(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload36 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class TextComponent27(BaseModel):
    model_config = ConfigDict(defer_build=True)
    tags: Tags3
    text: str
    text_type: str = Field(..., alias='textType')

class ComponentPayload37(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_component: TextComponent27 = Field(..., alias='textComponent')

class Banner8(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload37 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class Components17(BaseModel):
    model_config = ConfigDict(defer_build=True)
    transaction_detail: TransactionDetail17 = Field(..., alias='TRANSACTION_DETAIL')
    banner: Banner8 = Field(..., alias='BANNER')

class CardOption7(BaseModel):
    model_config = ConfigDict(defer_build=True)
    actions: list[Action19]
    card_type: str = Field(..., alias='cardType')
    components: Components17

class Payload26(BaseModel):
    model_config = ConfigDict(defer_build=True)
    expanding_card: ExpandingCard9 | None = Field(None, alias='expandingCard')
    payload_type: str = Field(..., alias='payloadType')
    card_options: list[CardOption7] | None = Field(None, alias='cardOptions')

class Presentation26(BaseModel):
    model_config = ConfigDict(defer_build=True)
    primary_label: str = Field(..., alias='primaryLabel')
    ref_marker: str = Field(..., alias='refMarker')

class PrimaryAction9(BaseModel):
    model_config = ConfigDict(defer_build=True)
    action_type: str = Field(..., alias='actionType')
    is_selected: bool = Field(..., alias='isSelected')
    payload: Payload26
    presentation: Presentation26 | None = None

class B005C8Ec7M1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    messages: Messages9
    primary_actions: list[PrimaryAction9] = Field(..., alias='primaryActions')
    secondary_actions: list[None] = Field(..., alias='secondaryActions')
    view_ref_marker: str = Field(..., alias='viewRefMarker')

class FocusMessage10(BaseModel):
    model_config = ConfigDict(defer_build=True)
    dv_message: DvMessage = Field(..., alias='dvMessage')
    icon: str
    icon_type: str = Field(..., alias='iconType')

class Messages10(BaseModel):
    model_config = ConfigDict(defer_build=True)
    entitlement_type: str = Field(..., alias='entitlementType')
    focus_message: FocusMessage10 = Field(..., alias='focusMessage')

class Transaction17(BaseModel):
    model_config = ConfigDict(defer_build=True)
    asin: str
    csrf_token: str = Field(..., alias='csrfToken')
    csrf_token_workflow: str = Field(..., alias='csrfTokenWorkflow')
    display_messages: list[None] = Field(..., alias='displayMessages')
    label: str
    offer_token: str = Field(..., alias='offerToken')
    purchase_data: PurchaseData = Field(..., alias='purchaseData')
    ref_marker: str = Field(..., alias='refMarker')

class Payload30(BaseModel):
    model_config = ConfigDict(defer_build=True)
    payload_type: str = Field(..., alias='payloadType')
    transaction: Transaction17

class Presentation27(BaseModel):
    model_config = ConfigDict(defer_build=True)
    icon: str
    primary_label: str = Field(..., alias='primaryLabel')
    ref_marker: str = Field(..., alias='refMarker')

class Action20(BaseModel):
    model_config = ConfigDict(defer_build=True)
    action_type: str = Field(..., alias='actionType')
    is_selected: bool = Field(..., alias='isSelected')
    payload: Payload30
    presentation: Presentation27

class TextComponent28(BaseModel):
    model_config = ConfigDict(defer_build=True)
    tags: dict[str, Any]
    text: str
    text_type: str = Field(..., alias='textType')

class ComponentPayload38(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_component: TextComponent28 = Field(..., alias='textComponent')

class TransactionDetail18(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload38 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class ComponentPayload39(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_component: TextComponent28 = Field(..., alias='textComponent')

class Header10(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload39 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class Components18(BaseModel):
    model_config = ConfigDict(defer_build=True)
    transaction_detail: TransactionDetail18 = Field(..., alias='TRANSACTION_DETAIL')
    header: Header10 = Field(..., alias='HEADER')

class ExpandingCard10(BaseModel):
    model_config = ConfigDict(defer_build=True)
    actions: list[Action20]
    card_type: str = Field(..., alias='cardType')
    components: Components18

class Transaction18(BaseModel):
    model_config = ConfigDict(defer_build=True)
    asin: str
    csrf_token: str = Field(..., alias='csrfToken')
    csrf_token_workflow: str = Field(..., alias='csrfTokenWorkflow')
    display_messages: list[None] = Field(..., alias='displayMessages')
    label: str
    offer_token: str = Field(..., alias='offerToken')
    purchase_data: PurchaseData = Field(..., alias='purchaseData')
    ref_marker: str = Field(..., alias='refMarker')

class Payload31(BaseModel):
    model_config = ConfigDict(defer_build=True)
    payload_type: str = Field(..., alias='payloadType')
    transaction: Transaction18

class Action21(BaseModel):
    model_config = ConfigDict(defer_build=True)
    action_type: str = Field(..., alias='actionType')
    is_selected: bool = Field(..., alias='isSelected')
    payload: Payload31
    presentation: Presentation27

class TextComponentCollection8(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_list: list[TextListItem] = Field(..., alias='textList')

class ComponentPayload40(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_component_collection: TextComponentCollection8 = Field(..., alias='textComponentCollection')

class TransactionDetail19(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload40 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class TextComponent30(BaseModel):
    model_config = ConfigDict(defer_build=True)
    tags: Tags3
    text: str
    text_type: str = Field(..., alias='textType')

class ComponentPayload41(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_component: TextComponent30 = Field(..., alias='textComponent')

class Banner9(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload41 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class Components19(BaseModel):
    model_config = ConfigDict(defer_build=True)
    transaction_detail: TransactionDetail19 = Field(..., alias='TRANSACTION_DETAIL')
    banner: Banner9 = Field(..., alias='BANNER')

class CardOption8(BaseModel):
    model_config = ConfigDict(defer_build=True)
    actions: list[Action21]
    card_type: str = Field(..., alias='cardType')
    components: Components19

class Payload29(BaseModel):
    model_config = ConfigDict(defer_build=True)
    expanding_card: ExpandingCard10 | None = Field(None, alias='expandingCard')
    payload_type: str = Field(..., alias='payloadType')
    card_options: list[CardOption8] | None = Field(None, alias='cardOptions')

class Presentation29(BaseModel):
    model_config = ConfigDict(defer_build=True)
    primary_label: str = Field(..., alias='primaryLabel')
    ref_marker: str = Field(..., alias='refMarker')

class PrimaryAction10(BaseModel):
    model_config = ConfigDict(defer_build=True)
    action_type: str = Field(..., alias='actionType')
    is_selected: bool = Field(..., alias='isSelected')
    payload: Payload29
    presentation: Presentation29 | None = None

class B005C8Egeg1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    messages: Messages10
    primary_actions: list[PrimaryAction10] = Field(..., alias='primaryActions')
    secondary_actions: list[None] = Field(..., alias='secondaryActions')
    view_ref_marker: str = Field(..., alias='viewRefMarker')

class FocusMessage11(BaseModel):
    model_config = ConfigDict(defer_build=True)
    dv_message: DvMessage = Field(..., alias='dvMessage')
    icon: str
    icon_type: str = Field(..., alias='iconType')

class Messages11(BaseModel):
    model_config = ConfigDict(defer_build=True)
    entitlement_type: str = Field(..., alias='entitlementType')
    focus_message: FocusMessage11 = Field(..., alias='focusMessage')

class Transaction19(BaseModel):
    model_config = ConfigDict(defer_build=True)
    asin: str
    csrf_token: str = Field(..., alias='csrfToken')
    csrf_token_workflow: str = Field(..., alias='csrfTokenWorkflow')
    display_messages: list[None] = Field(..., alias='displayMessages')
    label: str
    offer_token: str = Field(..., alias='offerToken')
    purchase_data: PurchaseData = Field(..., alias='purchaseData')
    ref_marker: str = Field(..., alias='refMarker')

class Payload33(BaseModel):
    model_config = ConfigDict(defer_build=True)
    payload_type: str = Field(..., alias='payloadType')
    transaction: Transaction19

class Presentation30(BaseModel):
    model_config = ConfigDict(defer_build=True)
    icon: str
    primary_label: str = Field(..., alias='primaryLabel')
    ref_marker: str = Field(..., alias='refMarker')

class Action22(BaseModel):
    model_config = ConfigDict(defer_build=True)
    action_type: str = Field(..., alias='actionType')
    is_selected: bool = Field(..., alias='isSelected')
    payload: Payload33
    presentation: Presentation30

class TextComponent31(BaseModel):
    model_config = ConfigDict(defer_build=True)
    tags: dict[str, Any]
    text: str
    text_type: str = Field(..., alias='textType')

class ComponentPayload42(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_component: TextComponent31 = Field(..., alias='textComponent')

class TransactionDetail20(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload42 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class ComponentPayload43(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_component: TextComponent31 = Field(..., alias='textComponent')

class Header11(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload43 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class Components20(BaseModel):
    model_config = ConfigDict(defer_build=True)
    transaction_detail: TransactionDetail20 = Field(..., alias='TRANSACTION_DETAIL')
    header: Header11 = Field(..., alias='HEADER')

class ExpandingCard11(BaseModel):
    model_config = ConfigDict(defer_build=True)
    actions: list[Action22]
    card_type: str = Field(..., alias='cardType')
    components: Components20

class Transaction20(BaseModel):
    model_config = ConfigDict(defer_build=True)
    asin: str
    csrf_token: str = Field(..., alias='csrfToken')
    csrf_token_workflow: str = Field(..., alias='csrfTokenWorkflow')
    display_messages: list[None] = Field(..., alias='displayMessages')
    label: str
    offer_token: str = Field(..., alias='offerToken')
    purchase_data: PurchaseData = Field(..., alias='purchaseData')
    ref_marker: str = Field(..., alias='refMarker')

class Payload34(BaseModel):
    model_config = ConfigDict(defer_build=True)
    payload_type: str = Field(..., alias='payloadType')
    transaction: Transaction20

class Action23(BaseModel):
    model_config = ConfigDict(defer_build=True)
    action_type: str = Field(..., alias='actionType')
    is_selected: bool = Field(..., alias='isSelected')
    payload: Payload34
    presentation: Presentation30

class TextComponentCollection9(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_list: list[TextListItem] = Field(..., alias='textList')

class ComponentPayload44(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_component_collection: TextComponentCollection9 = Field(..., alias='textComponentCollection')

class TransactionDetail21(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload44 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class TextComponent33(BaseModel):
    model_config = ConfigDict(defer_build=True)
    tags: Tags3
    text: str
    text_type: str = Field(..., alias='textType')

class ComponentPayload45(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_component: TextComponent33 = Field(..., alias='textComponent')

class Banner10(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload45 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class Components21(BaseModel):
    model_config = ConfigDict(defer_build=True)
    transaction_detail: TransactionDetail21 = Field(..., alias='TRANSACTION_DETAIL')
    banner: Banner10 = Field(..., alias='BANNER')

class CardOption9(BaseModel):
    model_config = ConfigDict(defer_build=True)
    actions: list[Action23]
    card_type: str = Field(..., alias='cardType')
    components: Components21

class Payload32(BaseModel):
    model_config = ConfigDict(defer_build=True)
    expanding_card: ExpandingCard11 | None = Field(None, alias='expandingCard')
    payload_type: str = Field(..., alias='payloadType')
    card_options: list[CardOption9] | None = Field(None, alias='cardOptions')

class Presentation32(BaseModel):
    model_config = ConfigDict(defer_build=True)
    primary_label: str = Field(..., alias='primaryLabel')
    ref_marker: str = Field(..., alias='refMarker')

class PrimaryAction11(BaseModel):
    model_config = ConfigDict(defer_build=True)
    action_type: str = Field(..., alias='actionType')
    is_selected: bool = Field(..., alias='isSelected')
    payload: Payload32
    presentation: Presentation32 | None = None

class B005C8Elci1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    messages: Messages11
    primary_actions: list[PrimaryAction11] = Field(..., alias='primaryActions')
    secondary_actions: list[None] = Field(..., alias='secondaryActions')
    view_ref_marker: str = Field(..., alias='viewRefMarker')

class FocusMessage12(BaseModel):
    model_config = ConfigDict(defer_build=True)
    dv_message: DvMessage = Field(..., alias='dvMessage')
    icon: str
    icon_type: str = Field(..., alias='iconType')

class Messages12(BaseModel):
    model_config = ConfigDict(defer_build=True)
    entitlement_type: str = Field(..., alias='entitlementType')
    focus_message: FocusMessage12 = Field(..., alias='focusMessage')

class Transaction21(BaseModel):
    model_config = ConfigDict(defer_build=True)
    asin: str
    csrf_token: str = Field(..., alias='csrfToken')
    csrf_token_workflow: str = Field(..., alias='csrfTokenWorkflow')
    display_messages: list[None] = Field(..., alias='displayMessages')
    label: str
    offer_token: str = Field(..., alias='offerToken')
    purchase_data: PurchaseData = Field(..., alias='purchaseData')
    ref_marker: str = Field(..., alias='refMarker')

class Payload36(BaseModel):
    model_config = ConfigDict(defer_build=True)
    payload_type: str = Field(..., alias='payloadType')
    transaction: Transaction21

class Presentation33(BaseModel):
    model_config = ConfigDict(defer_build=True)
    icon: str
    primary_label: str = Field(..., alias='primaryLabel')
    ref_marker: str = Field(..., alias='refMarker')

class Action24(BaseModel):
    model_config = ConfigDict(defer_build=True)
    action_type: str = Field(..., alias='actionType')
    is_selected: bool = Field(..., alias='isSelected')
    payload: Payload36
    presentation: Presentation33

class TextComponent34(BaseModel):
    model_config = ConfigDict(defer_build=True)
    tags: dict[str, Any]
    text: str
    text_type: str = Field(..., alias='textType')

class ComponentPayload46(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_component: TextComponent34 = Field(..., alias='textComponent')

class TransactionDetail22(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload46 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class ComponentPayload47(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_component: TextComponent34 = Field(..., alias='textComponent')

class Header12(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload47 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class Components22(BaseModel):
    model_config = ConfigDict(defer_build=True)
    transaction_detail: TransactionDetail22 = Field(..., alias='TRANSACTION_DETAIL')
    header: Header12 = Field(..., alias='HEADER')

class ExpandingCard12(BaseModel):
    model_config = ConfigDict(defer_build=True)
    actions: list[Action24]
    card_type: str = Field(..., alias='cardType')
    components: Components22

class Transaction22(BaseModel):
    model_config = ConfigDict(defer_build=True)
    asin: str
    csrf_token: str = Field(..., alias='csrfToken')
    csrf_token_workflow: str = Field(..., alias='csrfTokenWorkflow')
    display_messages: list[None] = Field(..., alias='displayMessages')
    label: str
    offer_token: str = Field(..., alias='offerToken')
    purchase_data: PurchaseData = Field(..., alias='purchaseData')
    ref_marker: str = Field(..., alias='refMarker')

class Payload37(BaseModel):
    model_config = ConfigDict(defer_build=True)
    payload_type: str = Field(..., alias='payloadType')
    transaction: Transaction22

class Action25(BaseModel):
    model_config = ConfigDict(defer_build=True)
    action_type: str = Field(..., alias='actionType')
    is_selected: bool = Field(..., alias='isSelected')
    payload: Payload37
    presentation: Presentation33

class TextComponentCollection10(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_list: list[TextListItem] = Field(..., alias='textList')

class ComponentPayload48(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_component_collection: TextComponentCollection10 = Field(..., alias='textComponentCollection')

class TransactionDetail23(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload48 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class TextComponent36(BaseModel):
    model_config = ConfigDict(defer_build=True)
    tags: Tags3
    text: str
    text_type: str = Field(..., alias='textType')

class ComponentPayload49(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_component: TextComponent36 = Field(..., alias='textComponent')

class Banner11(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload49 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class Components23(BaseModel):
    model_config = ConfigDict(defer_build=True)
    transaction_detail: TransactionDetail23 = Field(..., alias='TRANSACTION_DETAIL')
    banner: Banner11 = Field(..., alias='BANNER')

class CardOption10(BaseModel):
    model_config = ConfigDict(defer_build=True)
    actions: list[Action25]
    card_type: str = Field(..., alias='cardType')
    components: Components23

class Payload35(BaseModel):
    model_config = ConfigDict(defer_build=True)
    expanding_card: ExpandingCard12 | None = Field(None, alias='expandingCard')
    payload_type: str = Field(..., alias='payloadType')
    card_options: list[CardOption10] | None = Field(None, alias='cardOptions')

class Presentation35(BaseModel):
    model_config = ConfigDict(defer_build=True)
    primary_label: str = Field(..., alias='primaryLabel')
    ref_marker: str = Field(..., alias='refMarker')

class PrimaryAction12(BaseModel):
    model_config = ConfigDict(defer_build=True)
    action_type: str = Field(..., alias='actionType')
    is_selected: bool = Field(..., alias='isSelected')
    payload: Payload35
    presentation: Presentation35 | None = None

class B005C8Ed301(BaseModel):
    model_config = ConfigDict(defer_build=True)
    messages: Messages12
    primary_actions: list[PrimaryAction12] = Field(..., alias='primaryActions')
    secondary_actions: list[None] = Field(..., alias='secondaryActions')
    view_ref_marker: str = Field(..., alias='viewRefMarker')

class FocusMessage13(BaseModel):
    model_config = ConfigDict(defer_build=True)
    dv_message: DvMessage = Field(..., alias='dvMessage')
    icon: str
    icon_type: str = Field(..., alias='iconType')

class Messages13(BaseModel):
    model_config = ConfigDict(defer_build=True)
    entitlement_type: str = Field(..., alias='entitlementType')
    focus_message: FocusMessage13 = Field(..., alias='focusMessage')

class Transaction23(BaseModel):
    model_config = ConfigDict(defer_build=True)
    asin: str
    csrf_token: str = Field(..., alias='csrfToken')
    csrf_token_workflow: str = Field(..., alias='csrfTokenWorkflow')
    display_messages: list[None] = Field(..., alias='displayMessages')
    label: str
    offer_token: str = Field(..., alias='offerToken')
    purchase_data: PurchaseData = Field(..., alias='purchaseData')
    ref_marker: str = Field(..., alias='refMarker')

class Payload39(BaseModel):
    model_config = ConfigDict(defer_build=True)
    payload_type: str = Field(..., alias='payloadType')
    transaction: Transaction23

class Presentation36(BaseModel):
    model_config = ConfigDict(defer_build=True)
    icon: str
    primary_label: str = Field(..., alias='primaryLabel')
    ref_marker: str = Field(..., alias='refMarker')

class Action26(BaseModel):
    model_config = ConfigDict(defer_build=True)
    action_type: str = Field(..., alias='actionType')
    is_selected: bool = Field(..., alias='isSelected')
    payload: Payload39
    presentation: Presentation36

class TextComponent37(BaseModel):
    model_config = ConfigDict(defer_build=True)
    tags: dict[str, Any]
    text: str
    text_type: str = Field(..., alias='textType')

class ComponentPayload50(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_component: TextComponent37 = Field(..., alias='textComponent')

class TransactionDetail24(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload50 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class ComponentPayload51(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_component: TextComponent37 = Field(..., alias='textComponent')

class Header13(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload51 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class Components24(BaseModel):
    model_config = ConfigDict(defer_build=True)
    transaction_detail: TransactionDetail24 = Field(..., alias='TRANSACTION_DETAIL')
    header: Header13 = Field(..., alias='HEADER')

class ExpandingCard13(BaseModel):
    model_config = ConfigDict(defer_build=True)
    actions: list[Action26]
    card_type: str = Field(..., alias='cardType')
    components: Components24

class Transaction24(BaseModel):
    model_config = ConfigDict(defer_build=True)
    asin: str
    csrf_token: str = Field(..., alias='csrfToken')
    csrf_token_workflow: str = Field(..., alias='csrfTokenWorkflow')
    display_messages: list[None] = Field(..., alias='displayMessages')
    label: str
    offer_token: str = Field(..., alias='offerToken')
    purchase_data: PurchaseData = Field(..., alias='purchaseData')
    ref_marker: str = Field(..., alias='refMarker')

class Payload40(BaseModel):
    model_config = ConfigDict(defer_build=True)
    payload_type: str = Field(..., alias='payloadType')
    transaction: Transaction24

class Action27(BaseModel):
    model_config = ConfigDict(defer_build=True)
    action_type: str = Field(..., alias='actionType')
    is_selected: bool = Field(..., alias='isSelected')
    payload: Payload40
    presentation: Presentation36

class TextComponentCollection11(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_list: list[TextListItem] = Field(..., alias='textList')

class ComponentPayload52(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_component_collection: TextComponentCollection11 = Field(..., alias='textComponentCollection')

class TransactionDetail25(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload52 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class TextComponent39(BaseModel):
    model_config = ConfigDict(defer_build=True)
    tags: Tags3
    text: str
    text_type: str = Field(..., alias='textType')

class ComponentPayload53(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_component: TextComponent39 = Field(..., alias='textComponent')

class Banner12(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload53 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class Components25(BaseModel):
    model_config = ConfigDict(defer_build=True)
    transaction_detail: TransactionDetail25 = Field(..., alias='TRANSACTION_DETAIL')
    banner: Banner12 = Field(..., alias='BANNER')

class CardOption11(BaseModel):
    model_config = ConfigDict(defer_build=True)
    actions: list[Action27]
    card_type: str = Field(..., alias='cardType')
    components: Components25

class Payload38(BaseModel):
    model_config = ConfigDict(defer_build=True)
    expanding_card: ExpandingCard13 | None = Field(None, alias='expandingCard')
    payload_type: str = Field(..., alias='payloadType')
    card_options: list[CardOption11] | None = Field(None, alias='cardOptions')

class Presentation38(BaseModel):
    model_config = ConfigDict(defer_build=True)
    primary_label: str = Field(..., alias='primaryLabel')
    ref_marker: str = Field(..., alias='refMarker')

class PrimaryAction13(BaseModel):
    model_config = ConfigDict(defer_build=True)
    action_type: str = Field(..., alias='actionType')
    is_selected: bool = Field(..., alias='isSelected')
    payload: Payload38
    presentation: Presentation38 | None = None

class B005C8Dike1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    messages: Messages13
    primary_actions: list[PrimaryAction13] = Field(..., alias='primaryActions')
    secondary_actions: list[None] = Field(..., alias='secondaryActions')
    view_ref_marker: str = Field(..., alias='viewRefMarker')

class FocusMessage14(BaseModel):
    model_config = ConfigDict(defer_build=True)
    dv_message: DvMessage = Field(..., alias='dvMessage')
    icon: str
    icon_type: str = Field(..., alias='iconType')

class Messages14(BaseModel):
    model_config = ConfigDict(defer_build=True)
    entitlement_type: str = Field(..., alias='entitlementType')
    focus_message: FocusMessage14 = Field(..., alias='focusMessage')

class Transaction25(BaseModel):
    model_config = ConfigDict(defer_build=True)
    asin: str
    csrf_token: str = Field(..., alias='csrfToken')
    csrf_token_workflow: str = Field(..., alias='csrfTokenWorkflow')
    display_messages: list[None] = Field(..., alias='displayMessages')
    label: str
    offer_token: str = Field(..., alias='offerToken')
    purchase_data: PurchaseData = Field(..., alias='purchaseData')
    ref_marker: str = Field(..., alias='refMarker')

class Payload42(BaseModel):
    model_config = ConfigDict(defer_build=True)
    payload_type: str = Field(..., alias='payloadType')
    transaction: Transaction25

class Presentation39(BaseModel):
    model_config = ConfigDict(defer_build=True)
    icon: str
    primary_label: str = Field(..., alias='primaryLabel')
    ref_marker: str = Field(..., alias='refMarker')

class Action28(BaseModel):
    model_config = ConfigDict(defer_build=True)
    action_type: str = Field(..., alias='actionType')
    is_selected: bool = Field(..., alias='isSelected')
    payload: Payload42
    presentation: Presentation39

class TextComponent40(BaseModel):
    model_config = ConfigDict(defer_build=True)
    tags: dict[str, Any]
    text: str
    text_type: str = Field(..., alias='textType')

class ComponentPayload54(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_component: TextComponent40 = Field(..., alias='textComponent')

class TransactionDetail26(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload54 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class ComponentPayload55(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_component: TextComponent40 = Field(..., alias='textComponent')

class Header14(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload55 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class Components26(BaseModel):
    model_config = ConfigDict(defer_build=True)
    transaction_detail: TransactionDetail26 = Field(..., alias='TRANSACTION_DETAIL')
    header: Header14 = Field(..., alias='HEADER')

class ExpandingCard14(BaseModel):
    model_config = ConfigDict(defer_build=True)
    actions: list[Action28]
    card_type: str = Field(..., alias='cardType')
    components: Components26

class Transaction26(BaseModel):
    model_config = ConfigDict(defer_build=True)
    asin: str
    csrf_token: str = Field(..., alias='csrfToken')
    csrf_token_workflow: str = Field(..., alias='csrfTokenWorkflow')
    display_messages: list[None] = Field(..., alias='displayMessages')
    label: str
    offer_token: str = Field(..., alias='offerToken')
    purchase_data: PurchaseData = Field(..., alias='purchaseData')
    ref_marker: str = Field(..., alias='refMarker')

class Payload43(BaseModel):
    model_config = ConfigDict(defer_build=True)
    payload_type: str = Field(..., alias='payloadType')
    transaction: Transaction26

class Action29(BaseModel):
    model_config = ConfigDict(defer_build=True)
    action_type: str = Field(..., alias='actionType')
    is_selected: bool = Field(..., alias='isSelected')
    payload: Payload43
    presentation: Presentation39

class TextComponentCollection12(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_list: list[TextListItem] = Field(..., alias='textList')

class ComponentPayload56(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_component_collection: TextComponentCollection12 = Field(..., alias='textComponentCollection')

class TransactionDetail27(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload56 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class TextComponent42(BaseModel):
    model_config = ConfigDict(defer_build=True)
    tags: Tags3
    text: str
    text_type: str = Field(..., alias='textType')

class ComponentPayload57(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_component: TextComponent42 = Field(..., alias='textComponent')

class Banner13(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload57 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class Components27(BaseModel):
    model_config = ConfigDict(defer_build=True)
    transaction_detail: TransactionDetail27 = Field(..., alias='TRANSACTION_DETAIL')
    banner: Banner13 = Field(..., alias='BANNER')

class CardOption12(BaseModel):
    model_config = ConfigDict(defer_build=True)
    actions: list[Action29]
    card_type: str = Field(..., alias='cardType')
    components: Components27

class Payload41(BaseModel):
    model_config = ConfigDict(defer_build=True)
    expanding_card: ExpandingCard14 | None = Field(None, alias='expandingCard')
    payload_type: str = Field(..., alias='payloadType')
    card_options: list[CardOption12] | None = Field(None, alias='cardOptions')

class Presentation41(BaseModel):
    model_config = ConfigDict(defer_build=True)
    primary_label: str = Field(..., alias='primaryLabel')
    ref_marker: str = Field(..., alias='refMarker')

class PrimaryAction14(BaseModel):
    model_config = ConfigDict(defer_build=True)
    action_type: str = Field(..., alias='actionType')
    is_selected: bool = Field(..., alias='isSelected')
    payload: Payload41
    presentation: Presentation41 | None = None

class B005C8Ecls1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    messages: Messages14
    primary_actions: list[PrimaryAction14] = Field(..., alias='primaryActions')
    secondary_actions: list[None] = Field(..., alias='secondaryActions')
    view_ref_marker: str = Field(..., alias='viewRefMarker')

class FocusMessage15(BaseModel):
    model_config = ConfigDict(defer_build=True)
    dv_message: DvMessage = Field(..., alias='dvMessage')
    icon: str
    icon_type: str = Field(..., alias='iconType')

class Messages15(BaseModel):
    model_config = ConfigDict(defer_build=True)
    entitlement_type: str = Field(..., alias='entitlementType')
    focus_message: FocusMessage15 = Field(..., alias='focusMessage')

class Transaction27(BaseModel):
    model_config = ConfigDict(defer_build=True)
    asin: str
    csrf_token: str = Field(..., alias='csrfToken')
    csrf_token_workflow: str = Field(..., alias='csrfTokenWorkflow')
    display_messages: list[None] = Field(..., alias='displayMessages')
    label: str
    offer_token: str = Field(..., alias='offerToken')
    purchase_data: PurchaseData = Field(..., alias='purchaseData')
    ref_marker: str = Field(..., alias='refMarker')

class Payload45(BaseModel):
    model_config = ConfigDict(defer_build=True)
    payload_type: str = Field(..., alias='payloadType')
    transaction: Transaction27

class Presentation42(BaseModel):
    model_config = ConfigDict(defer_build=True)
    icon: str
    primary_label: str = Field(..., alias='primaryLabel')
    ref_marker: str = Field(..., alias='refMarker')

class Action30(BaseModel):
    model_config = ConfigDict(defer_build=True)
    action_type: str = Field(..., alias='actionType')
    is_selected: bool = Field(..., alias='isSelected')
    payload: Payload45
    presentation: Presentation42

class TextComponent43(BaseModel):
    model_config = ConfigDict(defer_build=True)
    tags: dict[str, Any]
    text: str
    text_type: str = Field(..., alias='textType')

class ComponentPayload58(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_component: TextComponent43 = Field(..., alias='textComponent')

class TransactionDetail28(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload58 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class ComponentPayload59(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_component: TextComponent43 = Field(..., alias='textComponent')

class Header15(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload59 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class Components28(BaseModel):
    model_config = ConfigDict(defer_build=True)
    transaction_detail: TransactionDetail28 = Field(..., alias='TRANSACTION_DETAIL')
    header: Header15 = Field(..., alias='HEADER')

class ExpandingCard15(BaseModel):
    model_config = ConfigDict(defer_build=True)
    actions: list[Action30]
    card_type: str = Field(..., alias='cardType')
    components: Components28

class Transaction28(BaseModel):
    model_config = ConfigDict(defer_build=True)
    asin: str
    csrf_token: str = Field(..., alias='csrfToken')
    csrf_token_workflow: str = Field(..., alias='csrfTokenWorkflow')
    display_messages: list[None] = Field(..., alias='displayMessages')
    label: str
    offer_token: str = Field(..., alias='offerToken')
    purchase_data: PurchaseData = Field(..., alias='purchaseData')
    ref_marker: str = Field(..., alias='refMarker')

class Payload46(BaseModel):
    model_config = ConfigDict(defer_build=True)
    payload_type: str = Field(..., alias='payloadType')
    transaction: Transaction28

class Action31(BaseModel):
    model_config = ConfigDict(defer_build=True)
    action_type: str = Field(..., alias='actionType')
    is_selected: bool = Field(..., alias='isSelected')
    payload: Payload46
    presentation: Presentation42

class TextComponentCollection13(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_list: list[TextListItem] = Field(..., alias='textList')

class ComponentPayload60(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_component_collection: TextComponentCollection13 = Field(..., alias='textComponentCollection')

class TransactionDetail29(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload60 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class TextComponent45(BaseModel):
    model_config = ConfigDict(defer_build=True)
    tags: Tags3
    text: str
    text_type: str = Field(..., alias='textType')

class ComponentPayload61(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_component: TextComponent45 = Field(..., alias='textComponent')

class Banner14(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload61 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class Components29(BaseModel):
    model_config = ConfigDict(defer_build=True)
    transaction_detail: TransactionDetail29 = Field(..., alias='TRANSACTION_DETAIL')
    banner: Banner14 = Field(..., alias='BANNER')

class CardOption13(BaseModel):
    model_config = ConfigDict(defer_build=True)
    actions: list[Action31]
    card_type: str = Field(..., alias='cardType')
    components: Components29

class Payload44(BaseModel):
    model_config = ConfigDict(defer_build=True)
    expanding_card: ExpandingCard15 | None = Field(None, alias='expandingCard')
    payload_type: str = Field(..., alias='payloadType')
    card_options: list[CardOption13] | None = Field(None, alias='cardOptions')

class Presentation44(BaseModel):
    model_config = ConfigDict(defer_build=True)
    primary_label: str = Field(..., alias='primaryLabel')
    ref_marker: str = Field(..., alias='refMarker')

class PrimaryAction15(BaseModel):
    model_config = ConfigDict(defer_build=True)
    action_type: str = Field(..., alias='actionType')
    is_selected: bool = Field(..., alias='isSelected')
    payload: Payload44
    presentation: Presentation44 | None = None

class B005C8Dtto1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    messages: Messages15
    primary_actions: list[PrimaryAction15] = Field(..., alias='primaryActions')
    secondary_actions: list[None] = Field(..., alias='secondaryActions')
    view_ref_marker: str = Field(..., alias='viewRefMarker')

class FocusMessage16(BaseModel):
    model_config = ConfigDict(defer_build=True)
    dv_message: DvMessage = Field(..., alias='dvMessage')
    icon: str
    icon_type: str = Field(..., alias='iconType')

class Messages16(BaseModel):
    model_config = ConfigDict(defer_build=True)
    entitlement_type: str = Field(..., alias='entitlementType')
    focus_message: FocusMessage16 = Field(..., alias='focusMessage')

class Transaction29(BaseModel):
    model_config = ConfigDict(defer_build=True)
    asin: str
    csrf_token: str = Field(..., alias='csrfToken')
    csrf_token_workflow: str = Field(..., alias='csrfTokenWorkflow')
    display_messages: list[None] = Field(..., alias='displayMessages')
    label: str
    offer_token: str = Field(..., alias='offerToken')
    purchase_data: PurchaseData = Field(..., alias='purchaseData')
    ref_marker: str = Field(..., alias='refMarker')

class Payload48(BaseModel):
    model_config = ConfigDict(defer_build=True)
    payload_type: str = Field(..., alias='payloadType')
    transaction: Transaction29

class Presentation45(BaseModel):
    model_config = ConfigDict(defer_build=True)
    icon: str
    primary_label: str = Field(..., alias='primaryLabel')
    ref_marker: str = Field(..., alias='refMarker')

class Action32(BaseModel):
    model_config = ConfigDict(defer_build=True)
    action_type: str = Field(..., alias='actionType')
    is_selected: bool = Field(..., alias='isSelected')
    payload: Payload48
    presentation: Presentation45

class TextComponent46(BaseModel):
    model_config = ConfigDict(defer_build=True)
    tags: dict[str, Any]
    text: str
    text_type: str = Field(..., alias='textType')

class ComponentPayload62(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_component: TextComponent46 = Field(..., alias='textComponent')

class TransactionDetail30(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload62 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class ComponentPayload63(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_component: TextComponent46 = Field(..., alias='textComponent')

class Header16(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload63 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class Components30(BaseModel):
    model_config = ConfigDict(defer_build=True)
    transaction_detail: TransactionDetail30 = Field(..., alias='TRANSACTION_DETAIL')
    header: Header16 = Field(..., alias='HEADER')

class ExpandingCard16(BaseModel):
    model_config = ConfigDict(defer_build=True)
    actions: list[Action32]
    card_type: str = Field(..., alias='cardType')
    components: Components30

class Transaction30(BaseModel):
    model_config = ConfigDict(defer_build=True)
    asin: str
    csrf_token: str = Field(..., alias='csrfToken')
    csrf_token_workflow: str = Field(..., alias='csrfTokenWorkflow')
    display_messages: list[None] = Field(..., alias='displayMessages')
    label: str
    offer_token: str = Field(..., alias='offerToken')
    purchase_data: PurchaseData = Field(..., alias='purchaseData')
    ref_marker: str = Field(..., alias='refMarker')

class Payload49(BaseModel):
    model_config = ConfigDict(defer_build=True)
    payload_type: str = Field(..., alias='payloadType')
    transaction: Transaction30

class Action33(BaseModel):
    model_config = ConfigDict(defer_build=True)
    action_type: str = Field(..., alias='actionType')
    is_selected: bool = Field(..., alias='isSelected')
    payload: Payload49
    presentation: Presentation45

class TextComponentCollection14(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_list: list[TextListItem] = Field(..., alias='textList')

class ComponentPayload64(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_component_collection: TextComponentCollection14 = Field(..., alias='textComponentCollection')

class TransactionDetail31(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload64 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class TextComponent48(BaseModel):
    model_config = ConfigDict(defer_build=True)
    tags: Tags3
    text: str
    text_type: str = Field(..., alias='textType')

class ComponentPayload65(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_component: TextComponent48 = Field(..., alias='textComponent')

class Banner15(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload65 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class Components31(BaseModel):
    model_config = ConfigDict(defer_build=True)
    transaction_detail: TransactionDetail31 = Field(..., alias='TRANSACTION_DETAIL')
    banner: Banner15 = Field(..., alias='BANNER')

class CardOption14(BaseModel):
    model_config = ConfigDict(defer_build=True)
    actions: list[Action33]
    card_type: str = Field(..., alias='cardType')
    components: Components31

class Payload47(BaseModel):
    model_config = ConfigDict(defer_build=True)
    expanding_card: ExpandingCard16 | None = Field(None, alias='expandingCard')
    payload_type: str = Field(..., alias='payloadType')
    card_options: list[CardOption14] | None = Field(None, alias='cardOptions')

class Presentation47(BaseModel):
    model_config = ConfigDict(defer_build=True)
    primary_label: str = Field(..., alias='primaryLabel')
    ref_marker: str = Field(..., alias='refMarker')

class PrimaryAction16(BaseModel):
    model_config = ConfigDict(defer_build=True)
    action_type: str = Field(..., alias='actionType')
    is_selected: bool = Field(..., alias='isSelected')
    payload: Payload47
    presentation: Presentation47 | None = None

class B005C8E91Q1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    messages: Messages16
    primary_actions: list[PrimaryAction16] = Field(..., alias='primaryActions')
    secondary_actions: list[None] = Field(..., alias='secondaryActions')
    view_ref_marker: str = Field(..., alias='viewRefMarker')

class FocusMessage17(BaseModel):
    model_config = ConfigDict(defer_build=True)
    dv_message: DvMessage = Field(..., alias='dvMessage')
    icon: str
    icon_type: str = Field(..., alias='iconType')

class Messages17(BaseModel):
    model_config = ConfigDict(defer_build=True)
    entitlement_type: str = Field(..., alias='entitlementType')
    focus_message: FocusMessage17 = Field(..., alias='focusMessage')

class Transaction31(BaseModel):
    model_config = ConfigDict(defer_build=True)
    asin: str
    csrf_token: str = Field(..., alias='csrfToken')
    csrf_token_workflow: str = Field(..., alias='csrfTokenWorkflow')
    display_messages: list[None] = Field(..., alias='displayMessages')
    label: str
    offer_token: str = Field(..., alias='offerToken')
    purchase_data: PurchaseData = Field(..., alias='purchaseData')
    ref_marker: str = Field(..., alias='refMarker')

class Payload51(BaseModel):
    model_config = ConfigDict(defer_build=True)
    payload_type: str = Field(..., alias='payloadType')
    transaction: Transaction31

class Presentation48(BaseModel):
    model_config = ConfigDict(defer_build=True)
    icon: str
    primary_label: str = Field(..., alias='primaryLabel')
    ref_marker: str = Field(..., alias='refMarker')

class Action34(BaseModel):
    model_config = ConfigDict(defer_build=True)
    action_type: str = Field(..., alias='actionType')
    is_selected: bool = Field(..., alias='isSelected')
    payload: Payload51
    presentation: Presentation48

class TextComponent49(BaseModel):
    model_config = ConfigDict(defer_build=True)
    tags: dict[str, Any]
    text: str
    text_type: str = Field(..., alias='textType')

class ComponentPayload66(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_component: TextComponent49 = Field(..., alias='textComponent')

class TransactionDetail32(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload66 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class ComponentPayload67(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_component: TextComponent49 = Field(..., alias='textComponent')

class Header17(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload67 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class Components32(BaseModel):
    model_config = ConfigDict(defer_build=True)
    transaction_detail: TransactionDetail32 = Field(..., alias='TRANSACTION_DETAIL')
    header: Header17 = Field(..., alias='HEADER')

class ExpandingCard17(BaseModel):
    model_config = ConfigDict(defer_build=True)
    actions: list[Action34]
    card_type: str = Field(..., alias='cardType')
    components: Components32

class Transaction32(BaseModel):
    model_config = ConfigDict(defer_build=True)
    asin: str
    csrf_token: str = Field(..., alias='csrfToken')
    csrf_token_workflow: str = Field(..., alias='csrfTokenWorkflow')
    display_messages: list[None] = Field(..., alias='displayMessages')
    label: str
    offer_token: str = Field(..., alias='offerToken')
    purchase_data: PurchaseData = Field(..., alias='purchaseData')
    ref_marker: str = Field(..., alias='refMarker')

class Payload52(BaseModel):
    model_config = ConfigDict(defer_build=True)
    payload_type: str = Field(..., alias='payloadType')
    transaction: Transaction32

class Action35(BaseModel):
    model_config = ConfigDict(defer_build=True)
    action_type: str = Field(..., alias='actionType')
    is_selected: bool = Field(..., alias='isSelected')
    payload: Payload52
    presentation: Presentation48

class TextComponentCollection15(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_list: list[TextListItem] = Field(..., alias='textList')

class ComponentPayload68(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_component_collection: TextComponentCollection15 = Field(..., alias='textComponentCollection')

class TransactionDetail33(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload68 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class TextComponent51(BaseModel):
    model_config = ConfigDict(defer_build=True)
    tags: Tags3
    text: str
    text_type: str = Field(..., alias='textType')

class ComponentPayload69(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_component: TextComponent51 = Field(..., alias='textComponent')

class Banner16(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload69 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class Components33(BaseModel):
    model_config = ConfigDict(defer_build=True)
    transaction_detail: TransactionDetail33 = Field(..., alias='TRANSACTION_DETAIL')
    banner: Banner16 = Field(..., alias='BANNER')

class CardOption15(BaseModel):
    model_config = ConfigDict(defer_build=True)
    actions: list[Action35]
    card_type: str = Field(..., alias='cardType')
    components: Components33

class Payload50(BaseModel):
    model_config = ConfigDict(defer_build=True)
    expanding_card: ExpandingCard17 | None = Field(None, alias='expandingCard')
    payload_type: str = Field(..., alias='payloadType')
    card_options: list[CardOption15] | None = Field(None, alias='cardOptions')

class Presentation50(BaseModel):
    model_config = ConfigDict(defer_build=True)
    primary_label: str = Field(..., alias='primaryLabel')
    ref_marker: str = Field(..., alias='refMarker')

class PrimaryAction17(BaseModel):
    model_config = ConfigDict(defer_build=True)
    action_type: str = Field(..., alias='actionType')
    is_selected: bool = Field(..., alias='isSelected')
    payload: Payload50
    presentation: Presentation50 | None = None

class B005C8Dkvg1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    messages: Messages17
    primary_actions: list[PrimaryAction17] = Field(..., alias='primaryActions')
    secondary_actions: list[None] = Field(..., alias='secondaryActions')
    view_ref_marker: str = Field(..., alias='viewRefMarker')

class FocusMessage18(BaseModel):
    model_config = ConfigDict(defer_build=True)
    dv_message: DvMessage = Field(..., alias='dvMessage')
    icon: str
    icon_type: str = Field(..., alias='iconType')

class Messages18(BaseModel):
    model_config = ConfigDict(defer_build=True)
    entitlement_type: str = Field(..., alias='entitlementType')
    focus_message: FocusMessage18 = Field(..., alias='focusMessage')

class Transaction33(BaseModel):
    model_config = ConfigDict(defer_build=True)
    asin: str
    csrf_token: str = Field(..., alias='csrfToken')
    csrf_token_workflow: str = Field(..., alias='csrfTokenWorkflow')
    display_messages: list[None] = Field(..., alias='displayMessages')
    label: str
    offer_token: str = Field(..., alias='offerToken')
    purchase_data: PurchaseData = Field(..., alias='purchaseData')
    ref_marker: str = Field(..., alias='refMarker')

class Payload54(BaseModel):
    model_config = ConfigDict(defer_build=True)
    payload_type: str = Field(..., alias='payloadType')
    transaction: Transaction33

class Presentation51(BaseModel):
    model_config = ConfigDict(defer_build=True)
    icon: str
    primary_label: str = Field(..., alias='primaryLabel')
    ref_marker: str = Field(..., alias='refMarker')

class Action36(BaseModel):
    model_config = ConfigDict(defer_build=True)
    action_type: str = Field(..., alias='actionType')
    is_selected: bool = Field(..., alias='isSelected')
    payload: Payload54
    presentation: Presentation51

class TextComponent52(BaseModel):
    model_config = ConfigDict(defer_build=True)
    tags: dict[str, Any]
    text: str
    text_type: str = Field(..., alias='textType')

class ComponentPayload70(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_component: TextComponent52 = Field(..., alias='textComponent')

class TransactionDetail34(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload70 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class ComponentPayload71(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_component: TextComponent52 = Field(..., alias='textComponent')

class Header18(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload71 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class Components34(BaseModel):
    model_config = ConfigDict(defer_build=True)
    transaction_detail: TransactionDetail34 = Field(..., alias='TRANSACTION_DETAIL')
    header: Header18 = Field(..., alias='HEADER')

class ExpandingCard18(BaseModel):
    model_config = ConfigDict(defer_build=True)
    actions: list[Action36]
    card_type: str = Field(..., alias='cardType')
    components: Components34

class Transaction34(BaseModel):
    model_config = ConfigDict(defer_build=True)
    asin: str
    csrf_token: str = Field(..., alias='csrfToken')
    csrf_token_workflow: str = Field(..., alias='csrfTokenWorkflow')
    display_messages: list[None] = Field(..., alias='displayMessages')
    label: str
    offer_token: str = Field(..., alias='offerToken')
    purchase_data: PurchaseData = Field(..., alias='purchaseData')
    ref_marker: str = Field(..., alias='refMarker')

class Payload55(BaseModel):
    model_config = ConfigDict(defer_build=True)
    payload_type: str = Field(..., alias='payloadType')
    transaction: Transaction34

class Action37(BaseModel):
    model_config = ConfigDict(defer_build=True)
    action_type: str = Field(..., alias='actionType')
    is_selected: bool = Field(..., alias='isSelected')
    payload: Payload55
    presentation: Presentation51

class TextComponentCollection16(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_list: list[TextListItem] = Field(..., alias='textList')

class ComponentPayload72(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_component_collection: TextComponentCollection16 = Field(..., alias='textComponentCollection')

class TransactionDetail35(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload72 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class TextComponent54(BaseModel):
    model_config = ConfigDict(defer_build=True)
    tags: Tags3
    text: str
    text_type: str = Field(..., alias='textType')

class ComponentPayload73(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_component: TextComponent54 = Field(..., alias='textComponent')

class Banner17(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload73 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class Components35(BaseModel):
    model_config = ConfigDict(defer_build=True)
    transaction_detail: TransactionDetail35 = Field(..., alias='TRANSACTION_DETAIL')
    banner: Banner17 = Field(..., alias='BANNER')

class CardOption16(BaseModel):
    model_config = ConfigDict(defer_build=True)
    actions: list[Action37]
    card_type: str = Field(..., alias='cardType')
    components: Components35

class Payload53(BaseModel):
    model_config = ConfigDict(defer_build=True)
    expanding_card: ExpandingCard18 | None = Field(None, alias='expandingCard')
    payload_type: str = Field(..., alias='payloadType')
    card_options: list[CardOption16] | None = Field(None, alias='cardOptions')

class Presentation53(BaseModel):
    model_config = ConfigDict(defer_build=True)
    primary_label: str = Field(..., alias='primaryLabel')
    ref_marker: str = Field(..., alias='refMarker')

class PrimaryAction18(BaseModel):
    model_config = ConfigDict(defer_build=True)
    action_type: str = Field(..., alias='actionType')
    is_selected: bool = Field(..., alias='isSelected')
    payload: Payload53
    presentation: Presentation53 | None = None

class B005C8Ei5S1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    messages: Messages18
    primary_actions: list[PrimaryAction18] = Field(..., alias='primaryActions')
    secondary_actions: list[None] = Field(..., alias='secondaryActions')
    view_ref_marker: str = Field(..., alias='viewRefMarker')

class FocusMessage19(BaseModel):
    model_config = ConfigDict(defer_build=True)
    dv_message: DvMessage = Field(..., alias='dvMessage')
    icon: str
    icon_type: str = Field(..., alias='iconType')

class Messages19(BaseModel):
    model_config = ConfigDict(defer_build=True)
    entitlement_type: str = Field(..., alias='entitlementType')
    focus_message: FocusMessage19 = Field(..., alias='focusMessage')

class Transaction35(BaseModel):
    model_config = ConfigDict(defer_build=True)
    asin: str
    csrf_token: str = Field(..., alias='csrfToken')
    csrf_token_workflow: str = Field(..., alias='csrfTokenWorkflow')
    display_messages: list[None] = Field(..., alias='displayMessages')
    label: str
    offer_token: str = Field(..., alias='offerToken')
    purchase_data: PurchaseData = Field(..., alias='purchaseData')
    ref_marker: str = Field(..., alias='refMarker')

class Payload57(BaseModel):
    model_config = ConfigDict(defer_build=True)
    payload_type: str = Field(..., alias='payloadType')
    transaction: Transaction35

class Presentation54(BaseModel):
    model_config = ConfigDict(defer_build=True)
    icon: str
    primary_label: str = Field(..., alias='primaryLabel')
    ref_marker: str = Field(..., alias='refMarker')

class Action38(BaseModel):
    model_config = ConfigDict(defer_build=True)
    action_type: str = Field(..., alias='actionType')
    is_selected: bool = Field(..., alias='isSelected')
    payload: Payload57
    presentation: Presentation54

class TextComponent55(BaseModel):
    model_config = ConfigDict(defer_build=True)
    tags: dict[str, Any]
    text: str
    text_type: str = Field(..., alias='textType')

class ComponentPayload74(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_component: TextComponent55 = Field(..., alias='textComponent')

class TransactionDetail36(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload74 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class ComponentPayload75(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_component: TextComponent55 = Field(..., alias='textComponent')

class Header19(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload75 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class Components36(BaseModel):
    model_config = ConfigDict(defer_build=True)
    transaction_detail: TransactionDetail36 = Field(..., alias='TRANSACTION_DETAIL')
    header: Header19 = Field(..., alias='HEADER')

class ExpandingCard19(BaseModel):
    model_config = ConfigDict(defer_build=True)
    actions: list[Action38]
    card_type: str = Field(..., alias='cardType')
    components: Components36

class Transaction36(BaseModel):
    model_config = ConfigDict(defer_build=True)
    asin: str
    csrf_token: str = Field(..., alias='csrfToken')
    csrf_token_workflow: str = Field(..., alias='csrfTokenWorkflow')
    display_messages: list[None] = Field(..., alias='displayMessages')
    label: str
    offer_token: str = Field(..., alias='offerToken')
    purchase_data: PurchaseData = Field(..., alias='purchaseData')
    ref_marker: str = Field(..., alias='refMarker')

class Payload58(BaseModel):
    model_config = ConfigDict(defer_build=True)
    payload_type: str = Field(..., alias='payloadType')
    transaction: Transaction36

class Action39(BaseModel):
    model_config = ConfigDict(defer_build=True)
    action_type: str = Field(..., alias='actionType')
    is_selected: bool = Field(..., alias='isSelected')
    payload: Payload58
    presentation: Presentation54

class TextComponentCollection17(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_list: list[TextListItem] = Field(..., alias='textList')

class ComponentPayload76(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_component_collection: TextComponentCollection17 = Field(..., alias='textComponentCollection')

class TransactionDetail37(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload76 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class TextComponent57(BaseModel):
    model_config = ConfigDict(defer_build=True)
    tags: Tags3
    text: str
    text_type: str = Field(..., alias='textType')

class ComponentPayload77(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_component: TextComponent57 = Field(..., alias='textComponent')

class Banner18(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload77 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class Components37(BaseModel):
    model_config = ConfigDict(defer_build=True)
    transaction_detail: TransactionDetail37 = Field(..., alias='TRANSACTION_DETAIL')
    banner: Banner18 = Field(..., alias='BANNER')

class CardOption17(BaseModel):
    model_config = ConfigDict(defer_build=True)
    actions: list[Action39]
    card_type: str = Field(..., alias='cardType')
    components: Components37

class Payload56(BaseModel):
    model_config = ConfigDict(defer_build=True)
    expanding_card: ExpandingCard19 | None = Field(None, alias='expandingCard')
    payload_type: str = Field(..., alias='payloadType')
    card_options: list[CardOption17] | None = Field(None, alias='cardOptions')

class Presentation56(BaseModel):
    model_config = ConfigDict(defer_build=True)
    primary_label: str = Field(..., alias='primaryLabel')
    ref_marker: str = Field(..., alias='refMarker')

class PrimaryAction19(BaseModel):
    model_config = ConfigDict(defer_build=True)
    action_type: str = Field(..., alias='actionType')
    is_selected: bool = Field(..., alias='isSelected')
    payload: Payload56
    presentation: Presentation56 | None = None

class B005C8Eiui1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    messages: Messages19
    primary_actions: list[PrimaryAction19] = Field(..., alias='primaryActions')
    secondary_actions: list[None] = Field(..., alias='secondaryActions')
    view_ref_marker: str = Field(..., alias='viewRefMarker')

class FocusMessage20(BaseModel):
    model_config = ConfigDict(defer_build=True)
    dv_message: DvMessage = Field(..., alias='dvMessage')
    icon: str
    icon_type: str = Field(..., alias='iconType')

class Messages20(BaseModel):
    model_config = ConfigDict(defer_build=True)
    entitlement_type: str = Field(..., alias='entitlementType')
    focus_message: FocusMessage20 = Field(..., alias='focusMessage')

class Transaction37(BaseModel):
    model_config = ConfigDict(defer_build=True)
    asin: str
    csrf_token: str = Field(..., alias='csrfToken')
    csrf_token_workflow: str = Field(..., alias='csrfTokenWorkflow')
    display_messages: list[None] = Field(..., alias='displayMessages')
    label: str
    offer_token: str = Field(..., alias='offerToken')
    purchase_data: PurchaseData = Field(..., alias='purchaseData')
    ref_marker: str = Field(..., alias='refMarker')

class Payload60(BaseModel):
    model_config = ConfigDict(defer_build=True)
    payload_type: str = Field(..., alias='payloadType')
    transaction: Transaction37

class Presentation57(BaseModel):
    model_config = ConfigDict(defer_build=True)
    icon: str
    primary_label: str = Field(..., alias='primaryLabel')
    ref_marker: str = Field(..., alias='refMarker')

class Action40(BaseModel):
    model_config = ConfigDict(defer_build=True)
    action_type: str = Field(..., alias='actionType')
    is_selected: bool = Field(..., alias='isSelected')
    payload: Payload60
    presentation: Presentation57

class TextComponent58(BaseModel):
    model_config = ConfigDict(defer_build=True)
    tags: dict[str, Any]
    text: str
    text_type: str = Field(..., alias='textType')

class ComponentPayload78(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_component: TextComponent58 = Field(..., alias='textComponent')

class TransactionDetail38(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload78 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class ComponentPayload79(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_component: TextComponent58 = Field(..., alias='textComponent')

class Header20(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload79 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class Components38(BaseModel):
    model_config = ConfigDict(defer_build=True)
    transaction_detail: TransactionDetail38 = Field(..., alias='TRANSACTION_DETAIL')
    header: Header20 = Field(..., alias='HEADER')

class ExpandingCard20(BaseModel):
    model_config = ConfigDict(defer_build=True)
    actions: list[Action40]
    card_type: str = Field(..., alias='cardType')
    components: Components38

class Transaction38(BaseModel):
    model_config = ConfigDict(defer_build=True)
    asin: str
    csrf_token: str = Field(..., alias='csrfToken')
    csrf_token_workflow: str = Field(..., alias='csrfTokenWorkflow')
    display_messages: list[None] = Field(..., alias='displayMessages')
    label: str
    offer_token: str = Field(..., alias='offerToken')
    purchase_data: PurchaseData = Field(..., alias='purchaseData')
    ref_marker: str = Field(..., alias='refMarker')

class Payload61(BaseModel):
    model_config = ConfigDict(defer_build=True)
    payload_type: str = Field(..., alias='payloadType')
    transaction: Transaction38

class Action41(BaseModel):
    model_config = ConfigDict(defer_build=True)
    action_type: str = Field(..., alias='actionType')
    is_selected: bool = Field(..., alias='isSelected')
    payload: Payload61
    presentation: Presentation57

class TextComponentCollection18(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_list: list[TextListItem] = Field(..., alias='textList')

class ComponentPayload80(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_component_collection: TextComponentCollection18 = Field(..., alias='textComponentCollection')

class TransactionDetail39(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload80 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class TextComponent60(BaseModel):
    model_config = ConfigDict(defer_build=True)
    tags: Tags3
    text: str
    text_type: str = Field(..., alias='textType')

class ComponentPayload81(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_component: TextComponent60 = Field(..., alias='textComponent')

class Banner19(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload81 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class Components39(BaseModel):
    model_config = ConfigDict(defer_build=True)
    transaction_detail: TransactionDetail39 = Field(..., alias='TRANSACTION_DETAIL')
    banner: Banner19 = Field(..., alias='BANNER')

class CardOption18(BaseModel):
    model_config = ConfigDict(defer_build=True)
    actions: list[Action41]
    card_type: str = Field(..., alias='cardType')
    components: Components39

class Payload59(BaseModel):
    model_config = ConfigDict(defer_build=True)
    expanding_card: ExpandingCard20 | None = Field(None, alias='expandingCard')
    payload_type: str = Field(..., alias='payloadType')
    card_options: list[CardOption18] | None = Field(None, alias='cardOptions')

class Presentation59(BaseModel):
    model_config = ConfigDict(defer_build=True)
    primary_label: str = Field(..., alias='primaryLabel')
    ref_marker: str = Field(..., alias='refMarker')

class PrimaryAction20(BaseModel):
    model_config = ConfigDict(defer_build=True)
    action_type: str = Field(..., alias='actionType')
    is_selected: bool = Field(..., alias='isSelected')
    payload: Payload59
    presentation: Presentation59 | None = None

class B005C8Emmm1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    messages: Messages20
    primary_actions: list[PrimaryAction20] = Field(..., alias='primaryActions')
    secondary_actions: list[None] = Field(..., alias='secondaryActions')
    view_ref_marker: str = Field(..., alias='viewRefMarker')

class FocusMessage21(BaseModel):
    model_config = ConfigDict(defer_build=True)
    dv_message: DvMessage = Field(..., alias='dvMessage')
    icon: str
    icon_type: str = Field(..., alias='iconType')

class Messages21(BaseModel):
    model_config = ConfigDict(defer_build=True)
    entitlement_type: str = Field(..., alias='entitlementType')
    focus_message: FocusMessage21 = Field(..., alias='focusMessage')

class Transaction39(BaseModel):
    model_config = ConfigDict(defer_build=True)
    asin: str
    csrf_token: str = Field(..., alias='csrfToken')
    csrf_token_workflow: str = Field(..., alias='csrfTokenWorkflow')
    display_messages: list[None] = Field(..., alias='displayMessages')
    label: str
    offer_token: str = Field(..., alias='offerToken')
    purchase_data: PurchaseData = Field(..., alias='purchaseData')
    ref_marker: str = Field(..., alias='refMarker')

class Payload63(BaseModel):
    model_config = ConfigDict(defer_build=True)
    payload_type: str = Field(..., alias='payloadType')
    transaction: Transaction39

class Presentation60(BaseModel):
    model_config = ConfigDict(defer_build=True)
    icon: str
    primary_label: str = Field(..., alias='primaryLabel')
    ref_marker: str = Field(..., alias='refMarker')

class Action42(BaseModel):
    model_config = ConfigDict(defer_build=True)
    action_type: str = Field(..., alias='actionType')
    is_selected: bool = Field(..., alias='isSelected')
    payload: Payload63
    presentation: Presentation60

class TextComponent61(BaseModel):
    model_config = ConfigDict(defer_build=True)
    tags: dict[str, Any]
    text: str
    text_type: str = Field(..., alias='textType')

class ComponentPayload82(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_component: TextComponent61 = Field(..., alias='textComponent')

class TransactionDetail40(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload82 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class ComponentPayload83(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_component: TextComponent61 = Field(..., alias='textComponent')

class Header21(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload83 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class Components40(BaseModel):
    model_config = ConfigDict(defer_build=True)
    transaction_detail: TransactionDetail40 = Field(..., alias='TRANSACTION_DETAIL')
    header: Header21 = Field(..., alias='HEADER')

class ExpandingCard21(BaseModel):
    model_config = ConfigDict(defer_build=True)
    actions: list[Action42]
    card_type: str = Field(..., alias='cardType')
    components: Components40

class Transaction40(BaseModel):
    model_config = ConfigDict(defer_build=True)
    asin: str
    csrf_token: str = Field(..., alias='csrfToken')
    csrf_token_workflow: str = Field(..., alias='csrfTokenWorkflow')
    display_messages: list[None] = Field(..., alias='displayMessages')
    label: str
    offer_token: str = Field(..., alias='offerToken')
    purchase_data: PurchaseData = Field(..., alias='purchaseData')
    ref_marker: str = Field(..., alias='refMarker')

class Payload64(BaseModel):
    model_config = ConfigDict(defer_build=True)
    payload_type: str = Field(..., alias='payloadType')
    transaction: Transaction40

class Action43(BaseModel):
    model_config = ConfigDict(defer_build=True)
    action_type: str = Field(..., alias='actionType')
    is_selected: bool = Field(..., alias='isSelected')
    payload: Payload64
    presentation: Presentation60

class TextComponentCollection19(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_list: list[TextListItem] = Field(..., alias='textList')

class ComponentPayload84(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_component_collection: TextComponentCollection19 = Field(..., alias='textComponentCollection')

class TransactionDetail41(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload84 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class TextComponent63(BaseModel):
    model_config = ConfigDict(defer_build=True)
    tags: Tags3
    text: str
    text_type: str = Field(..., alias='textType')

class ComponentPayload85(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_component: TextComponent63 = Field(..., alias='textComponent')

class Banner20(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload85 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class Components41(BaseModel):
    model_config = ConfigDict(defer_build=True)
    transaction_detail: TransactionDetail41 = Field(..., alias='TRANSACTION_DETAIL')
    banner: Banner20 = Field(..., alias='BANNER')

class CardOption19(BaseModel):
    model_config = ConfigDict(defer_build=True)
    actions: list[Action43]
    card_type: str = Field(..., alias='cardType')
    components: Components41

class Payload62(BaseModel):
    model_config = ConfigDict(defer_build=True)
    expanding_card: ExpandingCard21 | None = Field(None, alias='expandingCard')
    payload_type: str = Field(..., alias='payloadType')
    card_options: list[CardOption19] | None = Field(None, alias='cardOptions')

class Presentation62(BaseModel):
    model_config = ConfigDict(defer_build=True)
    primary_label: str = Field(..., alias='primaryLabel')
    ref_marker: str = Field(..., alias='refMarker')

class PrimaryAction21(BaseModel):
    model_config = ConfigDict(defer_build=True)
    action_type: str = Field(..., alias='actionType')
    is_selected: bool = Field(..., alias='isSelected')
    payload: Payload62
    presentation: Presentation62 | None = None

class B005C8Eh2W1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    messages: Messages21
    primary_actions: list[PrimaryAction21] = Field(..., alias='primaryActions')
    secondary_actions: list[None] = Field(..., alias='secondaryActions')
    view_ref_marker: str = Field(..., alias='viewRefMarker')

class FocusMessage22(BaseModel):
    model_config = ConfigDict(defer_build=True)
    dv_message: DvMessage = Field(..., alias='dvMessage')
    icon: str
    icon_type: str = Field(..., alias='iconType')

class Messages22(BaseModel):
    model_config = ConfigDict(defer_build=True)
    entitlement_type: str = Field(..., alias='entitlementType')
    focus_message: FocusMessage22 = Field(..., alias='focusMessage')

class Transaction41(BaseModel):
    model_config = ConfigDict(defer_build=True)
    asin: str
    csrf_token: str = Field(..., alias='csrfToken')
    csrf_token_workflow: str = Field(..., alias='csrfTokenWorkflow')
    display_messages: list[None] = Field(..., alias='displayMessages')
    label: str
    offer_token: str = Field(..., alias='offerToken')
    purchase_data: PurchaseData = Field(..., alias='purchaseData')
    ref_marker: str = Field(..., alias='refMarker')

class Payload66(BaseModel):
    model_config = ConfigDict(defer_build=True)
    payload_type: str = Field(..., alias='payloadType')
    transaction: Transaction41

class Presentation63(BaseModel):
    model_config = ConfigDict(defer_build=True)
    icon: str
    primary_label: str = Field(..., alias='primaryLabel')
    ref_marker: str = Field(..., alias='refMarker')

class Action44(BaseModel):
    model_config = ConfigDict(defer_build=True)
    action_type: str = Field(..., alias='actionType')
    is_selected: bool = Field(..., alias='isSelected')
    payload: Payload66
    presentation: Presentation63

class TextComponent64(BaseModel):
    model_config = ConfigDict(defer_build=True)
    tags: dict[str, Any]
    text: str
    text_type: str = Field(..., alias='textType')

class ComponentPayload86(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_component: TextComponent64 = Field(..., alias='textComponent')

class TransactionDetail42(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload86 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class ComponentPayload87(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_component: TextComponent64 = Field(..., alias='textComponent')

class Header22(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload87 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class Components42(BaseModel):
    model_config = ConfigDict(defer_build=True)
    transaction_detail: TransactionDetail42 = Field(..., alias='TRANSACTION_DETAIL')
    header: Header22 = Field(..., alias='HEADER')

class ExpandingCard22(BaseModel):
    model_config = ConfigDict(defer_build=True)
    actions: list[Action44]
    card_type: str = Field(..., alias='cardType')
    components: Components42

class Transaction42(BaseModel):
    model_config = ConfigDict(defer_build=True)
    asin: str
    csrf_token: str = Field(..., alias='csrfToken')
    csrf_token_workflow: str = Field(..., alias='csrfTokenWorkflow')
    display_messages: list[None] = Field(..., alias='displayMessages')
    label: str
    offer_token: str = Field(..., alias='offerToken')
    purchase_data: PurchaseData = Field(..., alias='purchaseData')
    ref_marker: str = Field(..., alias='refMarker')

class Payload67(BaseModel):
    model_config = ConfigDict(defer_build=True)
    payload_type: str = Field(..., alias='payloadType')
    transaction: Transaction42

class Action45(BaseModel):
    model_config = ConfigDict(defer_build=True)
    action_type: str = Field(..., alias='actionType')
    is_selected: bool = Field(..., alias='isSelected')
    payload: Payload67
    presentation: Presentation63

class TextComponentCollection20(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_list: list[TextListItem] = Field(..., alias='textList')

class ComponentPayload88(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_component_collection: TextComponentCollection20 = Field(..., alias='textComponentCollection')

class TransactionDetail43(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload88 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class TextComponent66(BaseModel):
    model_config = ConfigDict(defer_build=True)
    tags: Tags3
    text: str
    text_type: str = Field(..., alias='textType')

class ComponentPayload89(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_component: TextComponent66 = Field(..., alias='textComponent')

class Banner21(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload89 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class Components43(BaseModel):
    model_config = ConfigDict(defer_build=True)
    transaction_detail: TransactionDetail43 = Field(..., alias='TRANSACTION_DETAIL')
    banner: Banner21 = Field(..., alias='BANNER')

class CardOption20(BaseModel):
    model_config = ConfigDict(defer_build=True)
    actions: list[Action45]
    card_type: str = Field(..., alias='cardType')
    components: Components43

class Payload65(BaseModel):
    model_config = ConfigDict(defer_build=True)
    expanding_card: ExpandingCard22 | None = Field(None, alias='expandingCard')
    payload_type: str = Field(..., alias='payloadType')
    card_options: list[CardOption20] | None = Field(None, alias='cardOptions')

class Presentation65(BaseModel):
    model_config = ConfigDict(defer_build=True)
    primary_label: str = Field(..., alias='primaryLabel')
    ref_marker: str = Field(..., alias='refMarker')

class PrimaryAction22(BaseModel):
    model_config = ConfigDict(defer_build=True)
    action_type: str = Field(..., alias='actionType')
    is_selected: bool = Field(..., alias='isSelected')
    payload: Payload65
    presentation: Presentation65 | None = None

class B005C8Ebws1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    messages: Messages22
    primary_actions: list[PrimaryAction22] = Field(..., alias='primaryActions')
    secondary_actions: list[None] = Field(..., alias='secondaryActions')
    view_ref_marker: str = Field(..., alias='viewRefMarker')

class FocusMessage23(BaseModel):
    model_config = ConfigDict(defer_build=True)
    dv_message: DvMessage = Field(..., alias='dvMessage')
    icon: str
    icon_type: str = Field(..., alias='iconType')

class Messages23(BaseModel):
    model_config = ConfigDict(defer_build=True)
    entitlement_type: str = Field(..., alias='entitlementType')
    focus_message: FocusMessage23 = Field(..., alias='focusMessage')

class Transaction43(BaseModel):
    model_config = ConfigDict(defer_build=True)
    asin: str
    csrf_token: str = Field(..., alias='csrfToken')
    csrf_token_workflow: str = Field(..., alias='csrfTokenWorkflow')
    display_messages: list[None] = Field(..., alias='displayMessages')
    label: str
    offer_token: str = Field(..., alias='offerToken')
    purchase_data: PurchaseData = Field(..., alias='purchaseData')
    ref_marker: str = Field(..., alias='refMarker')

class Payload69(BaseModel):
    model_config = ConfigDict(defer_build=True)
    payload_type: str = Field(..., alias='payloadType')
    transaction: Transaction43

class Presentation66(BaseModel):
    model_config = ConfigDict(defer_build=True)
    icon: str
    primary_label: str = Field(..., alias='primaryLabel')
    ref_marker: str = Field(..., alias='refMarker')

class Action46(BaseModel):
    model_config = ConfigDict(defer_build=True)
    action_type: str = Field(..., alias='actionType')
    is_selected: bool = Field(..., alias='isSelected')
    payload: Payload69
    presentation: Presentation66

class TextComponent67(BaseModel):
    model_config = ConfigDict(defer_build=True)
    tags: dict[str, Any]
    text: str
    text_type: str = Field(..., alias='textType')

class ComponentPayload90(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_component: TextComponent67 = Field(..., alias='textComponent')

class TransactionDetail44(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload90 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class ComponentPayload91(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_component: TextComponent67 = Field(..., alias='textComponent')

class Header23(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload91 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class Components44(BaseModel):
    model_config = ConfigDict(defer_build=True)
    transaction_detail: TransactionDetail44 = Field(..., alias='TRANSACTION_DETAIL')
    header: Header23 = Field(..., alias='HEADER')

class ExpandingCard23(BaseModel):
    model_config = ConfigDict(defer_build=True)
    actions: list[Action46]
    card_type: str = Field(..., alias='cardType')
    components: Components44

class Transaction44(BaseModel):
    model_config = ConfigDict(defer_build=True)
    asin: str
    csrf_token: str = Field(..., alias='csrfToken')
    csrf_token_workflow: str = Field(..., alias='csrfTokenWorkflow')
    display_messages: list[None] = Field(..., alias='displayMessages')
    label: str
    offer_token: str = Field(..., alias='offerToken')
    purchase_data: PurchaseData = Field(..., alias='purchaseData')
    ref_marker: str = Field(..., alias='refMarker')

class Payload70(BaseModel):
    model_config = ConfigDict(defer_build=True)
    payload_type: str = Field(..., alias='payloadType')
    transaction: Transaction44

class Action47(BaseModel):
    model_config = ConfigDict(defer_build=True)
    action_type: str = Field(..., alias='actionType')
    is_selected: bool = Field(..., alias='isSelected')
    payload: Payload70
    presentation: Presentation66

class TextComponentCollection21(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_list: list[TextListItem] = Field(..., alias='textList')

class ComponentPayload92(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_component_collection: TextComponentCollection21 = Field(..., alias='textComponentCollection')

class TransactionDetail45(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload92 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class TextComponent69(BaseModel):
    model_config = ConfigDict(defer_build=True)
    tags: Tags3
    text: str
    text_type: str = Field(..., alias='textType')

class ComponentPayload93(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_component: TextComponent69 = Field(..., alias='textComponent')

class Banner22(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload93 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class Components45(BaseModel):
    model_config = ConfigDict(defer_build=True)
    transaction_detail: TransactionDetail45 = Field(..., alias='TRANSACTION_DETAIL')
    banner: Banner22 = Field(..., alias='BANNER')

class CardOption21(BaseModel):
    model_config = ConfigDict(defer_build=True)
    actions: list[Action47]
    card_type: str = Field(..., alias='cardType')
    components: Components45

class Payload68(BaseModel):
    model_config = ConfigDict(defer_build=True)
    expanding_card: ExpandingCard23 | None = Field(None, alias='expandingCard')
    payload_type: str = Field(..., alias='payloadType')
    card_options: list[CardOption21] | None = Field(None, alias='cardOptions')

class Presentation68(BaseModel):
    model_config = ConfigDict(defer_build=True)
    primary_label: str = Field(..., alias='primaryLabel')
    ref_marker: str = Field(..., alias='refMarker')

class PrimaryAction23(BaseModel):
    model_config = ConfigDict(defer_build=True)
    action_type: str = Field(..., alias='actionType')
    is_selected: bool = Field(..., alias='isSelected')
    payload: Payload68
    presentation: Presentation68 | None = None

class B005C8Ds0Y1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    messages: Messages23
    primary_actions: list[PrimaryAction23] = Field(..., alias='primaryActions')
    secondary_actions: list[None] = Field(..., alias='secondaryActions')
    view_ref_marker: str = Field(..., alias='viewRefMarker')

class FocusMessage24(BaseModel):
    model_config = ConfigDict(defer_build=True)
    dv_message: DvMessage = Field(..., alias='dvMessage')
    icon: str
    icon_type: str = Field(..., alias='iconType')

class Messages24(BaseModel):
    model_config = ConfigDict(defer_build=True)
    entitlement_type: str = Field(..., alias='entitlementType')
    focus_message: FocusMessage24 = Field(..., alias='focusMessage')

class Transaction45(BaseModel):
    model_config = ConfigDict(defer_build=True)
    asin: str
    csrf_token: str = Field(..., alias='csrfToken')
    csrf_token_workflow: str = Field(..., alias='csrfTokenWorkflow')
    display_messages: list[None] = Field(..., alias='displayMessages')
    label: str
    offer_token: str = Field(..., alias='offerToken')
    purchase_data: PurchaseData = Field(..., alias='purchaseData')
    ref_marker: str = Field(..., alias='refMarker')

class Payload72(BaseModel):
    model_config = ConfigDict(defer_build=True)
    payload_type: str = Field(..., alias='payloadType')
    transaction: Transaction45

class Presentation69(BaseModel):
    model_config = ConfigDict(defer_build=True)
    icon: str
    primary_label: str = Field(..., alias='primaryLabel')
    ref_marker: str = Field(..., alias='refMarker')

class Action48(BaseModel):
    model_config = ConfigDict(defer_build=True)
    action_type: str = Field(..., alias='actionType')
    is_selected: bool = Field(..., alias='isSelected')
    payload: Payload72
    presentation: Presentation69

class TextComponent70(BaseModel):
    model_config = ConfigDict(defer_build=True)
    tags: dict[str, Any]
    text: str
    text_type: str = Field(..., alias='textType')

class ComponentPayload94(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_component: TextComponent70 = Field(..., alias='textComponent')

class TransactionDetail46(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload94 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class ComponentPayload95(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_component: TextComponent70 = Field(..., alias='textComponent')

class Header24(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload95 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class Components46(BaseModel):
    model_config = ConfigDict(defer_build=True)
    transaction_detail: TransactionDetail46 = Field(..., alias='TRANSACTION_DETAIL')
    header: Header24 = Field(..., alias='HEADER')

class ExpandingCard24(BaseModel):
    model_config = ConfigDict(defer_build=True)
    actions: list[Action48]
    card_type: str = Field(..., alias='cardType')
    components: Components46

class Transaction46(BaseModel):
    model_config = ConfigDict(defer_build=True)
    asin: str
    csrf_token: str = Field(..., alias='csrfToken')
    csrf_token_workflow: str = Field(..., alias='csrfTokenWorkflow')
    display_messages: list[None] = Field(..., alias='displayMessages')
    label: str
    offer_token: str = Field(..., alias='offerToken')
    purchase_data: PurchaseData = Field(..., alias='purchaseData')
    ref_marker: str = Field(..., alias='refMarker')

class Payload73(BaseModel):
    model_config = ConfigDict(defer_build=True)
    payload_type: str = Field(..., alias='payloadType')
    transaction: Transaction46

class Action49(BaseModel):
    model_config = ConfigDict(defer_build=True)
    action_type: str = Field(..., alias='actionType')
    is_selected: bool = Field(..., alias='isSelected')
    payload: Payload73
    presentation: Presentation69

class TextComponentCollection22(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_list: list[TextListItem] = Field(..., alias='textList')

class ComponentPayload96(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_component_collection: TextComponentCollection22 = Field(..., alias='textComponentCollection')

class TransactionDetail47(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload96 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class TextComponent72(BaseModel):
    model_config = ConfigDict(defer_build=True)
    tags: Tags3
    text: str
    text_type: str = Field(..., alias='textType')

class ComponentPayload97(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_component: TextComponent72 = Field(..., alias='textComponent')

class Banner23(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload97 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class Components47(BaseModel):
    model_config = ConfigDict(defer_build=True)
    transaction_detail: TransactionDetail47 = Field(..., alias='TRANSACTION_DETAIL')
    banner: Banner23 = Field(..., alias='BANNER')

class CardOption22(BaseModel):
    model_config = ConfigDict(defer_build=True)
    actions: list[Action49]
    card_type: str = Field(..., alias='cardType')
    components: Components47

class Payload71(BaseModel):
    model_config = ConfigDict(defer_build=True)
    expanding_card: ExpandingCard24 | None = Field(None, alias='expandingCard')
    payload_type: str = Field(..., alias='payloadType')
    card_options: list[CardOption22] | None = Field(None, alias='cardOptions')

class Presentation71(BaseModel):
    model_config = ConfigDict(defer_build=True)
    primary_label: str = Field(..., alias='primaryLabel')
    ref_marker: str = Field(..., alias='refMarker')

class PrimaryAction24(BaseModel):
    model_config = ConfigDict(defer_build=True)
    action_type: str = Field(..., alias='actionType')
    is_selected: bool = Field(..., alias='isSelected')
    payload: Payload71
    presentation: Presentation71 | None = None

class B005C8E5A61(BaseModel):
    model_config = ConfigDict(defer_build=True)
    messages: Messages24
    primary_actions: list[PrimaryAction24] = Field(..., alias='primaryActions')
    secondary_actions: list[None] = Field(..., alias='secondaryActions')
    view_ref_marker: str = Field(..., alias='viewRefMarker')

class FocusMessage25(BaseModel):
    model_config = ConfigDict(defer_build=True)
    dv_message: DvMessage = Field(..., alias='dvMessage')
    icon: str
    icon_type: str = Field(..., alias='iconType')

class Messages25(BaseModel):
    model_config = ConfigDict(defer_build=True)
    entitlement_type: str = Field(..., alias='entitlementType')
    focus_message: FocusMessage25 = Field(..., alias='focusMessage')

class Transaction47(BaseModel):
    model_config = ConfigDict(defer_build=True)
    asin: str
    csrf_token: str = Field(..., alias='csrfToken')
    csrf_token_workflow: str = Field(..., alias='csrfTokenWorkflow')
    display_messages: list[None] = Field(..., alias='displayMessages')
    label: str
    offer_token: str = Field(..., alias='offerToken')
    purchase_data: PurchaseData = Field(..., alias='purchaseData')
    ref_marker: str = Field(..., alias='refMarker')

class Payload75(BaseModel):
    model_config = ConfigDict(defer_build=True)
    payload_type: str = Field(..., alias='payloadType')
    transaction: Transaction47

class Presentation72(BaseModel):
    model_config = ConfigDict(defer_build=True)
    icon: str
    primary_label: str = Field(..., alias='primaryLabel')
    ref_marker: str = Field(..., alias='refMarker')

class Action50(BaseModel):
    model_config = ConfigDict(defer_build=True)
    action_type: str = Field(..., alias='actionType')
    is_selected: bool = Field(..., alias='isSelected')
    payload: Payload75
    presentation: Presentation72

class TextComponent73(BaseModel):
    model_config = ConfigDict(defer_build=True)
    tags: dict[str, Any]
    text: str
    text_type: str = Field(..., alias='textType')

class ComponentPayload98(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_component: TextComponent73 = Field(..., alias='textComponent')

class TransactionDetail48(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload98 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class ComponentPayload99(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_component: TextComponent73 = Field(..., alias='textComponent')

class Header25(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload99 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class Components48(BaseModel):
    model_config = ConfigDict(defer_build=True)
    transaction_detail: TransactionDetail48 = Field(..., alias='TRANSACTION_DETAIL')
    header: Header25 = Field(..., alias='HEADER')

class ExpandingCard25(BaseModel):
    model_config = ConfigDict(defer_build=True)
    actions: list[Action50]
    card_type: str = Field(..., alias='cardType')
    components: Components48

class Transaction48(BaseModel):
    model_config = ConfigDict(defer_build=True)
    asin: str
    csrf_token: str = Field(..., alias='csrfToken')
    csrf_token_workflow: str = Field(..., alias='csrfTokenWorkflow')
    display_messages: list[None] = Field(..., alias='displayMessages')
    label: str
    offer_token: str = Field(..., alias='offerToken')
    purchase_data: PurchaseData = Field(..., alias='purchaseData')
    ref_marker: str = Field(..., alias='refMarker')

class Payload76(BaseModel):
    model_config = ConfigDict(defer_build=True)
    payload_type: str = Field(..., alias='payloadType')
    transaction: Transaction48

class Action51(BaseModel):
    model_config = ConfigDict(defer_build=True)
    action_type: str = Field(..., alias='actionType')
    is_selected: bool = Field(..., alias='isSelected')
    payload: Payload76
    presentation: Presentation72

class TextComponentCollection23(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_list: list[TextListItem] = Field(..., alias='textList')

class ComponentPayload100(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_component_collection: TextComponentCollection23 = Field(..., alias='textComponentCollection')

class TransactionDetail49(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload100 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class TextComponent75(BaseModel):
    model_config = ConfigDict(defer_build=True)
    tags: Tags3
    text: str
    text_type: str = Field(..., alias='textType')

class ComponentPayload101(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_component: TextComponent75 = Field(..., alias='textComponent')

class Banner24(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload101 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class Components49(BaseModel):
    model_config = ConfigDict(defer_build=True)
    transaction_detail: TransactionDetail49 = Field(..., alias='TRANSACTION_DETAIL')
    banner: Banner24 = Field(..., alias='BANNER')

class CardOption23(BaseModel):
    model_config = ConfigDict(defer_build=True)
    actions: list[Action51]
    card_type: str = Field(..., alias='cardType')
    components: Components49

class Payload74(BaseModel):
    model_config = ConfigDict(defer_build=True)
    expanding_card: ExpandingCard25 | None = Field(None, alias='expandingCard')
    payload_type: str = Field(..., alias='payloadType')
    card_options: list[CardOption23] | None = Field(None, alias='cardOptions')

class Presentation74(BaseModel):
    model_config = ConfigDict(defer_build=True)
    primary_label: str = Field(..., alias='primaryLabel')
    ref_marker: str = Field(..., alias='refMarker')

class PrimaryAction25(BaseModel):
    model_config = ConfigDict(defer_build=True)
    action_type: str = Field(..., alias='actionType')
    is_selected: bool = Field(..., alias='isSelected')
    payload: Payload74
    presentation: Presentation74 | None = None

class B005C8Ef8I1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    messages: Messages25
    primary_actions: list[PrimaryAction25] = Field(..., alias='primaryActions')
    secondary_actions: list[None] = Field(..., alias='secondaryActions')
    view_ref_marker: str = Field(..., alias='viewRefMarker')

class FocusMessage26(BaseModel):
    model_config = ConfigDict(defer_build=True)
    dv_message: DvMessage = Field(..., alias='dvMessage')
    icon: str
    icon_type: str = Field(..., alias='iconType')

class Messages26(BaseModel):
    model_config = ConfigDict(defer_build=True)
    entitlement_type: str = Field(..., alias='entitlementType')
    focus_message: FocusMessage26 = Field(..., alias='focusMessage')

class Transaction49(BaseModel):
    model_config = ConfigDict(defer_build=True)
    asin: str
    csrf_token: str = Field(..., alias='csrfToken')
    csrf_token_workflow: str = Field(..., alias='csrfTokenWorkflow')
    display_messages: list[None] = Field(..., alias='displayMessages')
    label: str
    offer_token: str = Field(..., alias='offerToken')
    purchase_data: PurchaseData = Field(..., alias='purchaseData')
    ref_marker: str = Field(..., alias='refMarker')

class Payload78(BaseModel):
    model_config = ConfigDict(defer_build=True)
    payload_type: str = Field(..., alias='payloadType')
    transaction: Transaction49

class Presentation75(BaseModel):
    model_config = ConfigDict(defer_build=True)
    icon: str
    primary_label: str = Field(..., alias='primaryLabel')
    ref_marker: str = Field(..., alias='refMarker')

class Action52(BaseModel):
    model_config = ConfigDict(defer_build=True)
    action_type: str = Field(..., alias='actionType')
    is_selected: bool = Field(..., alias='isSelected')
    payload: Payload78
    presentation: Presentation75

class TextComponent76(BaseModel):
    model_config = ConfigDict(defer_build=True)
    tags: dict[str, Any]
    text: str
    text_type: str = Field(..., alias='textType')

class ComponentPayload102(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_component: TextComponent76 = Field(..., alias='textComponent')

class TransactionDetail50(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload102 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class ComponentPayload103(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_component: TextComponent76 = Field(..., alias='textComponent')

class Header26(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload103 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class Components50(BaseModel):
    model_config = ConfigDict(defer_build=True)
    transaction_detail: TransactionDetail50 = Field(..., alias='TRANSACTION_DETAIL')
    header: Header26 = Field(..., alias='HEADER')

class ExpandingCard26(BaseModel):
    model_config = ConfigDict(defer_build=True)
    actions: list[Action52]
    card_type: str = Field(..., alias='cardType')
    components: Components50

class Transaction50(BaseModel):
    model_config = ConfigDict(defer_build=True)
    asin: str
    csrf_token: str = Field(..., alias='csrfToken')
    csrf_token_workflow: str = Field(..., alias='csrfTokenWorkflow')
    display_messages: list[None] = Field(..., alias='displayMessages')
    label: str
    offer_token: str = Field(..., alias='offerToken')
    purchase_data: PurchaseData = Field(..., alias='purchaseData')
    ref_marker: str = Field(..., alias='refMarker')

class Payload79(BaseModel):
    model_config = ConfigDict(defer_build=True)
    payload_type: str = Field(..., alias='payloadType')
    transaction: Transaction50

class Action53(BaseModel):
    model_config = ConfigDict(defer_build=True)
    action_type: str = Field(..., alias='actionType')
    is_selected: bool = Field(..., alias='isSelected')
    payload: Payload79
    presentation: Presentation75

class TextComponentCollection24(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_list: list[TextListItem] = Field(..., alias='textList')

class ComponentPayload104(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_component_collection: TextComponentCollection24 = Field(..., alias='textComponentCollection')

class TransactionDetail51(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload104 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class TextComponent78(BaseModel):
    model_config = ConfigDict(defer_build=True)
    tags: Tags3
    text: str
    text_type: str = Field(..., alias='textType')

class ComponentPayload105(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_component: TextComponent78 = Field(..., alias='textComponent')

class Banner25(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload105 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class Components51(BaseModel):
    model_config = ConfigDict(defer_build=True)
    transaction_detail: TransactionDetail51 = Field(..., alias='TRANSACTION_DETAIL')
    banner: Banner25 = Field(..., alias='BANNER')

class CardOption24(BaseModel):
    model_config = ConfigDict(defer_build=True)
    actions: list[Action53]
    card_type: str = Field(..., alias='cardType')
    components: Components51

class Payload77(BaseModel):
    model_config = ConfigDict(defer_build=True)
    expanding_card: ExpandingCard26 | None = Field(None, alias='expandingCard')
    payload_type: str = Field(..., alias='payloadType')
    card_options: list[CardOption24] | None = Field(None, alias='cardOptions')

class Presentation77(BaseModel):
    model_config = ConfigDict(defer_build=True)
    primary_label: str = Field(..., alias='primaryLabel')
    ref_marker: str = Field(..., alias='refMarker')

class PrimaryAction26(BaseModel):
    model_config = ConfigDict(defer_build=True)
    action_type: str = Field(..., alias='actionType')
    is_selected: bool = Field(..., alias='isSelected')
    payload: Payload77
    presentation: Presentation77 | None = None

class B005C8Ek9M1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    messages: Messages26
    primary_actions: list[PrimaryAction26] = Field(..., alias='primaryActions')
    secondary_actions: list[None] = Field(..., alias='secondaryActions')
    view_ref_marker: str = Field(..., alias='viewRefMarker')

class FocusMessage27(BaseModel):
    model_config = ConfigDict(defer_build=True)
    dv_message: DvMessage = Field(..., alias='dvMessage')
    icon: str
    icon_type: str = Field(..., alias='iconType')

class Messages27(BaseModel):
    model_config = ConfigDict(defer_build=True)
    entitlement_type: str = Field(..., alias='entitlementType')
    focus_message: FocusMessage27 = Field(..., alias='focusMessage')

class Payload81(BaseModel):
    model_config = ConfigDict(defer_build=True)
    payload_type: str = Field(..., alias='payloadType')
    subscription: Subscription

class Action54(BaseModel):
    model_config = ConfigDict(defer_build=True)
    action_type: str = Field(..., alias='actionType')
    is_selected: bool = Field(..., alias='isSelected')
    payload: Payload81
    presentation: Presentation77

class TextComponent79(BaseModel):
    model_config = ConfigDict(defer_build=True)
    tags: dict[str, Any]
    text: str
    text_type: str = Field(..., alias='textType')

class ComponentPayload106(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_component: TextComponent79 = Field(..., alias='textComponent')

class TransactionDetail52(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload106 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class Tags27(BaseModel):
    model_config = ConfigDict(defer_build=True)
    logo_entity_tag: str = Field(..., alias='LOGO_ENTITY_TAG')
    logo_height: str = Field(..., alias='LOGO_HEIGHT')
    logo_width: str = Field(..., alias='LOGO_WIDTH')

class LogoComponent1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    tags: Tags27
    url: str

class ComponentPayload107(BaseModel):
    model_config = ConfigDict(defer_build=True)
    logo_component: LogoComponent1 = Field(..., alias='logoComponent')

class Header27(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload107 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class Components52(BaseModel):
    model_config = ConfigDict(defer_build=True)
    transaction_detail: TransactionDetail52 = Field(..., alias='TRANSACTION_DETAIL')
    header: Header27 = Field(..., alias='HEADER')

class ExpandingCard27(BaseModel):
    model_config = ConfigDict(defer_build=True)
    actions: list[Action54]
    card_type: str = Field(..., alias='cardType')
    components: Components52

class Payload80(BaseModel):
    model_config = ConfigDict(defer_build=True)
    expanding_card: ExpandingCard27 = Field(..., alias='expandingCard')
    payload_type: str = Field(..., alias='payloadType')

class PrimaryAction27(BaseModel):
    model_config = ConfigDict(defer_build=True)
    action_type: str = Field(..., alias='actionType')
    is_selected: bool = Field(..., alias='isSelected')
    payload: Payload80

class B0Cjp8Rbmq2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    messages: Messages27
    primary_actions: list[PrimaryAction27] = Field(..., alias='primaryActions')
    secondary_actions: list[None] = Field(..., alias='secondaryActions')
    view_ref_marker: str = Field(..., alias='viewRefMarker')

class FocusMessage28(BaseModel):
    model_config = ConfigDict(defer_build=True)
    dv_message: DvMessage = Field(..., alias='dvMessage')
    icon: str
    icon_type: str = Field(..., alias='iconType')

class Messages28(BaseModel):
    model_config = ConfigDict(defer_build=True)
    entitlement_type: str = Field(..., alias='entitlementType')
    focus_message: FocusMessage28 = Field(..., alias='focusMessage')

class Payload83(BaseModel):
    model_config = ConfigDict(defer_build=True)
    payload_type: str = Field(..., alias='payloadType')
    subscription: Subscription

class Action55(BaseModel):
    model_config = ConfigDict(defer_build=True)
    action_type: str = Field(..., alias='actionType')
    is_selected: bool = Field(..., alias='isSelected')
    payload: Payload83
    presentation: Presentation77

class ComponentPayload108(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_component: TextComponent79 = Field(..., alias='textComponent')

class TransactionDetail53(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload108 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class LogoComponent2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    tags: Tags27
    url: str

class ComponentPayload109(BaseModel):
    model_config = ConfigDict(defer_build=True)
    logo_component: LogoComponent2 = Field(..., alias='logoComponent')

class Header28(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload109 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class Components53(BaseModel):
    model_config = ConfigDict(defer_build=True)
    transaction_detail: TransactionDetail53 = Field(..., alias='TRANSACTION_DETAIL')
    header: Header28 = Field(..., alias='HEADER')

class ExpandingCard28(BaseModel):
    model_config = ConfigDict(defer_build=True)
    actions: list[Action55]
    card_type: str = Field(..., alias='cardType')
    components: Components53

class Payload82(BaseModel):
    model_config = ConfigDict(defer_build=True)
    expanding_card: ExpandingCard28 = Field(..., alias='expandingCard')
    payload_type: str = Field(..., alias='payloadType')

class PrimaryAction28(BaseModel):
    model_config = ConfigDict(defer_build=True)
    action_type: str = Field(..., alias='actionType')
    is_selected: bool = Field(..., alias='isSelected')
    payload: Payload82

class B0Ck832Gg51(BaseModel):
    model_config = ConfigDict(defer_build=True)
    messages: Messages28
    primary_actions: list[PrimaryAction28] = Field(..., alias='primaryActions')
    secondary_actions: list[None] = Field(..., alias='secondaryActions')
    view_ref_marker: str = Field(..., alias='viewRefMarker')

class FocusMessage29(BaseModel):
    model_config = ConfigDict(defer_build=True)
    dv_message: DvMessage = Field(..., alias='dvMessage')
    icon: str
    icon_type: str = Field(..., alias='iconType')

class Messages29(BaseModel):
    model_config = ConfigDict(defer_build=True)
    entitlement_type: str = Field(..., alias='entitlementType')
    focus_message: FocusMessage29 = Field(..., alias='focusMessage')

class Payload85(BaseModel):
    model_config = ConfigDict(defer_build=True)
    payload_type: str = Field(..., alias='payloadType')
    subscription: Subscription

class Action56(BaseModel):
    model_config = ConfigDict(defer_build=True)
    action_type: str = Field(..., alias='actionType')
    is_selected: bool = Field(..., alias='isSelected')
    payload: Payload85
    presentation: Presentation77

class ComponentPayload110(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_component: TextComponent79 = Field(..., alias='textComponent')

class TransactionDetail54(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload110 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class LogoComponent3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    tags: Tags27
    url: str

class ComponentPayload111(BaseModel):
    model_config = ConfigDict(defer_build=True)
    logo_component: LogoComponent3 = Field(..., alias='logoComponent')

class Header29(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload111 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class Components54(BaseModel):
    model_config = ConfigDict(defer_build=True)
    transaction_detail: TransactionDetail54 = Field(..., alias='TRANSACTION_DETAIL')
    header: Header29 = Field(..., alias='HEADER')

class ExpandingCard29(BaseModel):
    model_config = ConfigDict(defer_build=True)
    actions: list[Action56]
    card_type: str = Field(..., alias='cardType')
    components: Components54

class Payload84(BaseModel):
    model_config = ConfigDict(defer_build=True)
    expanding_card: ExpandingCard29 = Field(..., alias='expandingCard')
    payload_type: str = Field(..., alias='payloadType')

class PrimaryAction29(BaseModel):
    model_config = ConfigDict(defer_build=True)
    action_type: str = Field(..., alias='actionType')
    is_selected: bool = Field(..., alias='isSelected')
    payload: Payload84

class B0Chsjdg3Y1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    messages: Messages29
    primary_actions: list[PrimaryAction29] = Field(..., alias='primaryActions')
    secondary_actions: list[None] = Field(..., alias='secondaryActions')
    view_ref_marker: str = Field(..., alias='viewRefMarker')

class FocusMessage30(BaseModel):
    model_config = ConfigDict(defer_build=True)
    dv_message: DvMessage = Field(..., alias='dvMessage')
    icon: str
    icon_type: str = Field(..., alias='iconType')

class Messages30(BaseModel):
    model_config = ConfigDict(defer_build=True)
    entitlement_type: str = Field(..., alias='entitlementType')
    focus_message: FocusMessage30 = Field(..., alias='focusMessage')

class Payload87(BaseModel):
    model_config = ConfigDict(defer_build=True)
    payload_type: str = Field(..., alias='payloadType')
    subscription: Subscription

class Action57(BaseModel):
    model_config = ConfigDict(defer_build=True)
    action_type: str = Field(..., alias='actionType')
    is_selected: bool = Field(..., alias='isSelected')
    payload: Payload87
    presentation: Presentation77

class ComponentPayload112(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_component: TextComponent79 = Field(..., alias='textComponent')

class TransactionDetail55(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload112 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class LogoComponent4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    tags: Tags27
    url: str

class ComponentPayload113(BaseModel):
    model_config = ConfigDict(defer_build=True)
    logo_component: LogoComponent4 = Field(..., alias='logoComponent')

class Header30(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload113 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class Components55(BaseModel):
    model_config = ConfigDict(defer_build=True)
    transaction_detail: TransactionDetail55 = Field(..., alias='TRANSACTION_DETAIL')
    header: Header30 = Field(..., alias='HEADER')

class ExpandingCard30(BaseModel):
    model_config = ConfigDict(defer_build=True)
    actions: list[Action57]
    card_type: str = Field(..., alias='cardType')
    components: Components55

class Payload86(BaseModel):
    model_config = ConfigDict(defer_build=True)
    expanding_card: ExpandingCard30 = Field(..., alias='expandingCard')
    payload_type: str = Field(..., alias='payloadType')

class PrimaryAction30(BaseModel):
    model_config = ConfigDict(defer_build=True)
    action_type: str = Field(..., alias='actionType')
    is_selected: bool = Field(..., alias='isSelected')
    payload: Payload86

class B0Cgpsngts1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    messages: Messages30
    primary_actions: list[PrimaryAction30] = Field(..., alias='primaryActions')
    secondary_actions: list[None] = Field(..., alias='secondaryActions')
    view_ref_marker: str = Field(..., alias='viewRefMarker')

class FocusMessage31(BaseModel):
    model_config = ConfigDict(defer_build=True)
    dv_message: DvMessage = Field(..., alias='dvMessage')
    icon: str
    icon_type: str = Field(..., alias='iconType')

class Messages31(BaseModel):
    model_config = ConfigDict(defer_build=True)
    entitlement_type: str = Field(..., alias='entitlementType')
    focus_message: FocusMessage31 = Field(..., alias='focusMessage')

class Payload89(BaseModel):
    model_config = ConfigDict(defer_build=True)
    payload_type: str = Field(..., alias='payloadType')
    subscription: Subscription

class Action58(BaseModel):
    model_config = ConfigDict(defer_build=True)
    action_type: str = Field(..., alias='actionType')
    is_selected: bool = Field(..., alias='isSelected')
    payload: Payload89
    presentation: Presentation77

class ComponentPayload114(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_component: TextComponent79 = Field(..., alias='textComponent')

class TransactionDetail56(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload114 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class LogoComponent5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    tags: Tags27
    url: str

class ComponentPayload115(BaseModel):
    model_config = ConfigDict(defer_build=True)
    logo_component: LogoComponent5 = Field(..., alias='logoComponent')

class Header31(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload115 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class Components56(BaseModel):
    model_config = ConfigDict(defer_build=True)
    transaction_detail: TransactionDetail56 = Field(..., alias='TRANSACTION_DETAIL')
    header: Header31 = Field(..., alias='HEADER')

class ExpandingCard31(BaseModel):
    model_config = ConfigDict(defer_build=True)
    actions: list[Action58]
    card_type: str = Field(..., alias='cardType')
    components: Components56

class Payload88(BaseModel):
    model_config = ConfigDict(defer_build=True)
    expanding_card: ExpandingCard31 = Field(..., alias='expandingCard')
    payload_type: str = Field(..., alias='payloadType')

class PrimaryAction31(BaseModel):
    model_config = ConfigDict(defer_build=True)
    action_type: str = Field(..., alias='actionType')
    is_selected: bool = Field(..., alias='isSelected')
    payload: Payload88

class B0Chjln6Gs1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    messages: Messages31
    primary_actions: list[PrimaryAction31] = Field(..., alias='primaryActions')
    secondary_actions: list[None] = Field(..., alias='secondaryActions')
    view_ref_marker: str = Field(..., alias='viewRefMarker')

class FocusMessage32(BaseModel):
    model_config = ConfigDict(defer_build=True)
    dv_message: DvMessage = Field(..., alias='dvMessage')
    icon: str
    icon_type: str = Field(..., alias='iconType')

class Messages32(BaseModel):
    model_config = ConfigDict(defer_build=True)
    entitlement_type: str = Field(..., alias='entitlementType')
    focus_message: FocusMessage32 = Field(..., alias='focusMessage')

class Payload91(BaseModel):
    model_config = ConfigDict(defer_build=True)
    payload_type: str = Field(..., alias='payloadType')
    subscription: Subscription

class Action59(BaseModel):
    model_config = ConfigDict(defer_build=True)
    action_type: str = Field(..., alias='actionType')
    is_selected: bool = Field(..., alias='isSelected')
    payload: Payload91
    presentation: Presentation77

class ComponentPayload116(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_component: TextComponent79 = Field(..., alias='textComponent')

class TransactionDetail57(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload116 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class LogoComponent6(BaseModel):
    model_config = ConfigDict(defer_build=True)
    tags: Tags27
    url: str

class ComponentPayload117(BaseModel):
    model_config = ConfigDict(defer_build=True)
    logo_component: LogoComponent6 = Field(..., alias='logoComponent')

class Header32(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload117 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class Components57(BaseModel):
    model_config = ConfigDict(defer_build=True)
    transaction_detail: TransactionDetail57 = Field(..., alias='TRANSACTION_DETAIL')
    header: Header32 = Field(..., alias='HEADER')

class ExpandingCard32(BaseModel):
    model_config = ConfigDict(defer_build=True)
    actions: list[Action59]
    card_type: str = Field(..., alias='cardType')
    components: Components57

class Payload90(BaseModel):
    model_config = ConfigDict(defer_build=True)
    expanding_card: ExpandingCard32 = Field(..., alias='expandingCard')
    payload_type: str = Field(..., alias='payloadType')

class PrimaryAction32(BaseModel):
    model_config = ConfigDict(defer_build=True)
    action_type: str = Field(..., alias='actionType')
    is_selected: bool = Field(..., alias='isSelected')
    payload: Payload90

class B0Chpmk42L1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    messages: Messages32
    primary_actions: list[PrimaryAction32] = Field(..., alias='primaryActions')
    secondary_actions: list[None] = Field(..., alias='secondaryActions')
    view_ref_marker: str = Field(..., alias='viewRefMarker')

class FocusMessage33(BaseModel):
    model_config = ConfigDict(defer_build=True)
    dv_message: DvMessage = Field(..., alias='dvMessage')
    icon: str
    icon_type: str = Field(..., alias='iconType')

class Messages33(BaseModel):
    model_config = ConfigDict(defer_build=True)
    entitlement_type: str = Field(..., alias='entitlementType')
    focus_message: FocusMessage33 = Field(..., alias='focusMessage')

class Payload93(BaseModel):
    model_config = ConfigDict(defer_build=True)
    payload_type: str = Field(..., alias='payloadType')
    subscription: Subscription

class Action60(BaseModel):
    model_config = ConfigDict(defer_build=True)
    action_type: str = Field(..., alias='actionType')
    is_selected: bool = Field(..., alias='isSelected')
    payload: Payload93
    presentation: Presentation77

class ComponentPayload118(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_component: TextComponent79 = Field(..., alias='textComponent')

class TransactionDetail58(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload118 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class LogoComponent7(BaseModel):
    model_config = ConfigDict(defer_build=True)
    tags: Tags27
    url: str

class ComponentPayload119(BaseModel):
    model_config = ConfigDict(defer_build=True)
    logo_component: LogoComponent7 = Field(..., alias='logoComponent')

class Header33(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload119 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class Components58(BaseModel):
    model_config = ConfigDict(defer_build=True)
    transaction_detail: TransactionDetail58 = Field(..., alias='TRANSACTION_DETAIL')
    header: Header33 = Field(..., alias='HEADER')

class ExpandingCard33(BaseModel):
    model_config = ConfigDict(defer_build=True)
    actions: list[Action60]
    card_type: str = Field(..., alias='cardType')
    components: Components58

class Payload92(BaseModel):
    model_config = ConfigDict(defer_build=True)
    expanding_card: ExpandingCard33 = Field(..., alias='expandingCard')
    payload_type: str = Field(..., alias='payloadType')

class PrimaryAction33(BaseModel):
    model_config = ConfigDict(defer_build=True)
    action_type: str = Field(..., alias='actionType')
    is_selected: bool = Field(..., alias='isSelected')
    payload: Payload92

class B0Cjcmt4Xn1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    messages: Messages33
    primary_actions: list[PrimaryAction33] = Field(..., alias='primaryActions')
    secondary_actions: list[None] = Field(..., alias='secondaryActions')
    view_ref_marker: str = Field(..., alias='viewRefMarker')

class FocusMessage34(BaseModel):
    model_config = ConfigDict(defer_build=True)
    dv_message: DvMessage = Field(..., alias='dvMessage')
    icon: str
    icon_type: str = Field(..., alias='iconType')

class Messages34(BaseModel):
    model_config = ConfigDict(defer_build=True)
    entitlement_type: str = Field(..., alias='entitlementType')
    focus_message: FocusMessage34 = Field(..., alias='focusMessage')

class Payload95(BaseModel):
    model_config = ConfigDict(defer_build=True)
    payload_type: str = Field(..., alias='payloadType')
    subscription: Subscription

class Action61(BaseModel):
    model_config = ConfigDict(defer_build=True)
    action_type: str = Field(..., alias='actionType')
    is_selected: bool = Field(..., alias='isSelected')
    payload: Payload95
    presentation: Presentation77

class ComponentPayload120(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_component: TextComponent79 = Field(..., alias='textComponent')

class TransactionDetail59(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload120 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class LogoComponent8(BaseModel):
    model_config = ConfigDict(defer_build=True)
    tags: Tags27
    url: str

class ComponentPayload121(BaseModel):
    model_config = ConfigDict(defer_build=True)
    logo_component: LogoComponent8 = Field(..., alias='logoComponent')

class Header34(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload121 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class Components59(BaseModel):
    model_config = ConfigDict(defer_build=True)
    transaction_detail: TransactionDetail59 = Field(..., alias='TRANSACTION_DETAIL')
    header: Header34 = Field(..., alias='HEADER')

class ExpandingCard34(BaseModel):
    model_config = ConfigDict(defer_build=True)
    actions: list[Action61]
    card_type: str = Field(..., alias='cardType')
    components: Components59

class Payload94(BaseModel):
    model_config = ConfigDict(defer_build=True)
    expanding_card: ExpandingCard34 = Field(..., alias='expandingCard')
    payload_type: str = Field(..., alias='payloadType')

class PrimaryAction34(BaseModel):
    model_config = ConfigDict(defer_build=True)
    action_type: str = Field(..., alias='actionType')
    is_selected: bool = Field(..., alias='isSelected')
    payload: Payload94

class B0Cgx6W4Gk1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    messages: Messages34
    primary_actions: list[PrimaryAction34] = Field(..., alias='primaryActions')
    secondary_actions: list[None] = Field(..., alias='secondaryActions')
    view_ref_marker: str = Field(..., alias='viewRefMarker')

class FocusMessage35(BaseModel):
    model_config = ConfigDict(defer_build=True)
    dv_message: DvMessage = Field(..., alias='dvMessage')
    icon: str
    icon_type: str = Field(..., alias='iconType')

class Messages35(BaseModel):
    model_config = ConfigDict(defer_build=True)
    entitlement_type: str = Field(..., alias='entitlementType')
    focus_message: FocusMessage35 = Field(..., alias='focusMessage')

class Payload97(BaseModel):
    model_config = ConfigDict(defer_build=True)
    payload_type: str = Field(..., alias='payloadType')
    subscription: Subscription

class Action62(BaseModel):
    model_config = ConfigDict(defer_build=True)
    action_type: str = Field(..., alias='actionType')
    is_selected: bool = Field(..., alias='isSelected')
    payload: Payload97
    presentation: Presentation77

class ComponentPayload122(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_component: TextComponent79 = Field(..., alias='textComponent')

class TransactionDetail60(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload122 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class LogoComponent9(BaseModel):
    model_config = ConfigDict(defer_build=True)
    tags: Tags27
    url: str

class ComponentPayload123(BaseModel):
    model_config = ConfigDict(defer_build=True)
    logo_component: LogoComponent9 = Field(..., alias='logoComponent')

class Header35(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload123 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class Components60(BaseModel):
    model_config = ConfigDict(defer_build=True)
    transaction_detail: TransactionDetail60 = Field(..., alias='TRANSACTION_DETAIL')
    header: Header35 = Field(..., alias='HEADER')

class ExpandingCard35(BaseModel):
    model_config = ConfigDict(defer_build=True)
    actions: list[Action62]
    card_type: str = Field(..., alias='cardType')
    components: Components60

class Payload96(BaseModel):
    model_config = ConfigDict(defer_build=True)
    expanding_card: ExpandingCard35 = Field(..., alias='expandingCard')
    payload_type: str = Field(..., alias='payloadType')

class PrimaryAction35(BaseModel):
    model_config = ConfigDict(defer_build=True)
    action_type: str = Field(..., alias='actionType')
    is_selected: bool = Field(..., alias='isSelected')
    payload: Payload96

class B0Ch4Tmyh21(BaseModel):
    model_config = ConfigDict(defer_build=True)
    messages: Messages35
    primary_actions: list[PrimaryAction35] = Field(..., alias='primaryActions')
    secondary_actions: list[None] = Field(..., alias='secondaryActions')
    view_ref_marker: str = Field(..., alias='viewRefMarker')

class FocusMessage36(BaseModel):
    model_config = ConfigDict(defer_build=True)
    dv_message: DvMessage = Field(..., alias='dvMessage')
    icon: str
    icon_type: str = Field(..., alias='iconType')

class Messages36(BaseModel):
    model_config = ConfigDict(defer_build=True)
    entitlement_type: str = Field(..., alias='entitlementType')
    focus_message: FocusMessage36 = Field(..., alias='focusMessage')

class Payload99(BaseModel):
    model_config = ConfigDict(defer_build=True)
    payload_type: str = Field(..., alias='payloadType')
    subscription: Subscription

class Action63(BaseModel):
    model_config = ConfigDict(defer_build=True)
    action_type: str = Field(..., alias='actionType')
    is_selected: bool = Field(..., alias='isSelected')
    payload: Payload99
    presentation: Presentation77

class ComponentPayload124(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_component: TextComponent79 = Field(..., alias='textComponent')

class TransactionDetail61(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload124 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class LogoComponent10(BaseModel):
    model_config = ConfigDict(defer_build=True)
    tags: Tags27
    url: str

class ComponentPayload125(BaseModel):
    model_config = ConfigDict(defer_build=True)
    logo_component: LogoComponent10 = Field(..., alias='logoComponent')

class Header36(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload125 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class Components61(BaseModel):
    model_config = ConfigDict(defer_build=True)
    transaction_detail: TransactionDetail61 = Field(..., alias='TRANSACTION_DETAIL')
    header: Header36 = Field(..., alias='HEADER')

class ExpandingCard36(BaseModel):
    model_config = ConfigDict(defer_build=True)
    actions: list[Action63]
    card_type: str = Field(..., alias='cardType')
    components: Components61

class Payload98(BaseModel):
    model_config = ConfigDict(defer_build=True)
    expanding_card: ExpandingCard36 = Field(..., alias='expandingCard')
    payload_type: str = Field(..., alias='payloadType')

class PrimaryAction36(BaseModel):
    model_config = ConfigDict(defer_build=True)
    action_type: str = Field(..., alias='actionType')
    is_selected: bool = Field(..., alias='isSelected')
    payload: Payload98

class B0Cjqd32Q61(BaseModel):
    model_config = ConfigDict(defer_build=True)
    messages: Messages36
    primary_actions: list[PrimaryAction36] = Field(..., alias='primaryActions')
    secondary_actions: list[None] = Field(..., alias='secondaryActions')
    view_ref_marker: str = Field(..., alias='viewRefMarker')

class FocusMessage37(BaseModel):
    model_config = ConfigDict(defer_build=True)
    dv_message: DvMessage = Field(..., alias='dvMessage')
    icon: str
    icon_type: str = Field(..., alias='iconType')

class Messages37(BaseModel):
    model_config = ConfigDict(defer_build=True)
    entitlement_type: str = Field(..., alias='entitlementType')
    focus_message: FocusMessage37 = Field(..., alias='focusMessage')

class Payload101(BaseModel):
    model_config = ConfigDict(defer_build=True)
    payload_type: str = Field(..., alias='payloadType')
    subscription: Subscription

class Action64(BaseModel):
    model_config = ConfigDict(defer_build=True)
    action_type: str = Field(..., alias='actionType')
    is_selected: bool = Field(..., alias='isSelected')
    payload: Payload101
    presentation: Presentation77

class ComponentPayload126(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_component: TextComponent79 = Field(..., alias='textComponent')

class TransactionDetail62(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload126 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class LogoComponent11(BaseModel):
    model_config = ConfigDict(defer_build=True)
    tags: Tags27
    url: str

class ComponentPayload127(BaseModel):
    model_config = ConfigDict(defer_build=True)
    logo_component: LogoComponent11 = Field(..., alias='logoComponent')

class Header37(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload127 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class Components62(BaseModel):
    model_config = ConfigDict(defer_build=True)
    transaction_detail: TransactionDetail62 = Field(..., alias='TRANSACTION_DETAIL')
    header: Header37 = Field(..., alias='HEADER')

class ExpandingCard37(BaseModel):
    model_config = ConfigDict(defer_build=True)
    actions: list[Action64]
    card_type: str = Field(..., alias='cardType')
    components: Components62

class Payload100(BaseModel):
    model_config = ConfigDict(defer_build=True)
    expanding_card: ExpandingCard37 = Field(..., alias='expandingCard')
    payload_type: str = Field(..., alias='payloadType')

class PrimaryAction37(BaseModel):
    model_config = ConfigDict(defer_build=True)
    action_type: str = Field(..., alias='actionType')
    is_selected: bool = Field(..., alias='isSelected')
    payload: Payload100

class B0Cj658T6K1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    messages: Messages37
    primary_actions: list[PrimaryAction37] = Field(..., alias='primaryActions')
    secondary_actions: list[None] = Field(..., alias='secondaryActions')
    view_ref_marker: str = Field(..., alias='viewRefMarker')

class FocusMessage38(BaseModel):
    model_config = ConfigDict(defer_build=True)
    dv_message: DvMessage = Field(..., alias='dvMessage')
    icon: str
    icon_type: str = Field(..., alias='iconType')

class Messages38(BaseModel):
    model_config = ConfigDict(defer_build=True)
    entitlement_type: str = Field(..., alias='entitlementType')
    focus_message: FocusMessage38 = Field(..., alias='focusMessage')

class Payload103(BaseModel):
    model_config = ConfigDict(defer_build=True)
    payload_type: str = Field(..., alias='payloadType')
    subscription: Subscription

class Action65(BaseModel):
    model_config = ConfigDict(defer_build=True)
    action_type: str = Field(..., alias='actionType')
    is_selected: bool = Field(..., alias='isSelected')
    payload: Payload103
    presentation: Presentation77

class ComponentPayload128(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text_component: TextComponent79 = Field(..., alias='textComponent')

class TransactionDetail63(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload128 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class LogoComponent12(BaseModel):
    model_config = ConfigDict(defer_build=True)
    tags: Tags27
    url: str

class ComponentPayload129(BaseModel):
    model_config = ConfigDict(defer_build=True)
    logo_component: LogoComponent12 = Field(..., alias='logoComponent')

class Header38(BaseModel):
    model_config = ConfigDict(defer_build=True)
    component_payload: ComponentPayload129 = Field(..., alias='componentPayload')
    component_primitive: str = Field(..., alias='componentPrimitive')

class Components63(BaseModel):
    model_config = ConfigDict(defer_build=True)
    transaction_detail: TransactionDetail63 = Field(..., alias='TRANSACTION_DETAIL')
    header: Header38 = Field(..., alias='HEADER')

class ExpandingCard38(BaseModel):
    model_config = ConfigDict(defer_build=True)
    actions: list[Action65]
    card_type: str = Field(..., alias='cardType')
    components: Components63

class Payload102(BaseModel):
    model_config = ConfigDict(defer_build=True)
    expanding_card: ExpandingCard38 = Field(..., alias='expandingCard')
    payload_type: str = Field(..., alias='payloadType')

class PrimaryAction38(BaseModel):
    model_config = ConfigDict(defer_build=True)
    action_type: str = Field(..., alias='actionType')
    is_selected: bool = Field(..., alias='isSelected')
    payload: Payload102

class B0Cjq1Pt9T1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    messages: Messages38
    primary_actions: list[PrimaryAction38] = Field(..., alias='primaryActions')
    secondary_actions: list[None] = Field(..., alias='secondaryActions')
    view_ref_marker: str = Field(..., alias='viewRefMarker')

class Btf2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    b005_c8_dbii: B005C8Dbii2 | None = Field(None, alias='B005C8DBII')
    b005_c8_e538: B005C8E5381 | None = Field(None, alias='B005C8E538')
    b005_c8_e70_y: B005C8E70Y1 | None = Field(None, alias='B005C8E70Y')
    b005_g0_r6_xi: B005G0R6Xi1 | None = Field(None, alias='B005G0R6XI')
    b005_c8_egx2: B005C8Egx21 | None = Field(None, alias='B005C8EGX2')
    b005_c8_ei62: B005C8Ei621 | None = Field(None, alias='B005C8EI62')
    b005_c8_ec7_m: B005C8Ec7M1 | None = Field(None, alias='B005C8EC7M')
    b005_c8_egeg: B005C8Egeg1 | None = Field(None, alias='B005C8EGEG')
    b005_c8_elci: B005C8Elci1 | None = Field(None, alias='B005C8ELCI')
    b005_c8_ed30: B005C8Ed301 | None = Field(None, alias='B005C8ED30')
    b005_c8_dike: B005C8Dike1 | None = Field(None, alias='B005C8DIKE')
    b005_c8_ecls: B005C8Ecls1 | None = Field(None, alias='B005C8ECLS')
    b005_c8_dtto: B005C8Dtto1 | None = Field(None, alias='B005C8DTTO')
    b005_c8_e91_q: B005C8E91Q1 | None = Field(None, alias='B005C8E91Q')
    b005_c8_dkvg: B005C8Dkvg1 | None = Field(None, alias='B005C8DKVG')
    b005_c8_ei5_s: B005C8Ei5S1 | None = Field(None, alias='B005C8EI5S')
    b005_c8_eiui: B005C8Eiui1 | None = Field(None, alias='B005C8EIUI')
    b005_c8_emmm: B005C8Emmm1 | None = Field(None, alias='B005C8EMMM')
    b005_c8_eh2_w: B005C8Eh2W1 | None = Field(None, alias='B005C8EH2W')
    b005_c8_ebws: B005C8Ebws1 | None = Field(None, alias='B005C8EBWS')
    b005_c8_ds0_y: B005C8Ds0Y1 | None = Field(None, alias='B005C8DS0Y')
    b005_c8_e5_a6: B005C8E5A61 | None = Field(None, alias='B005C8E5A6')
    b005_c8_ef8_i: B005C8Ef8I1 | None = Field(None, alias='B005C8EF8I')
    b005_c8_ek9_m: B005C8Ek9M1 | None = Field(None, alias='B005C8EK9M')
    b0_cjp8_rbmq: B0Cjp8Rbmq2 | None = Field(None, alias='B0CJP8RBMQ')
    b0_ck832_gg5: B0Ck832Gg51 | None = Field(None, alias='B0CK832GG5')
    b0_chsjdg3_y: B0Chsjdg3Y1 | None = Field(None, alias='B0CHSJDG3Y')
    b0_cgpsngts: B0Cgpsngts1 | None = Field(None, alias='B0CGPSNGTS')
    b0_chjln6_gs: B0Chjln6Gs1 | None = Field(None, alias='B0CHJLN6GS')
    b0_chpmk42_l: B0Chpmk42L1 | None = Field(None, alias='B0CHPMK42L')
    b0_cjcmt4_xn: B0Cjcmt4Xn1 | None = Field(None, alias='B0CJCMT4XN')
    b0_cgx6_w4_gk: B0Cgx6W4Gk1 | None = Field(None, alias='B0CGX6W4GK')
    b0_ch4_tmyh2: B0Ch4Tmyh21 | None = Field(None, alias='B0CH4TMYH2')
    b0_cjqd32_q6: B0Cjqd32Q61 | None = Field(None, alias='B0CJQD32Q6')
    b0_cj658_t6_k: B0Cj658T6K1 | None = Field(None, alias='B0CJ658T6K')
    b0_cjq1_pt9_t: B0Cjq1Pt9T1 | None = Field(None, alias='B0CJQ1PT9T')

class Action5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    btf: Btf2
    atf: dict[str, Any]

class Banner26(BaseModel):
    model_config = ConfigDict(defer_build=True)
    crow: dict[str, Any]
    ui: None

class Amzn1DvGti8ca9f71eF00061b3339819b8b550587b(BaseModel):
    model_config = ConfigDict(defer_build=True)
    asins: list[str]
    compact_gti: str = Field(..., alias='compactGTI')
    gti: str
    is_launched: bool = Field(..., alias='isLaunched')
    link: str
    sequence_number: int = Field(..., alias='sequenceNumber')
    title_type: str = Field(..., alias='titleType')

class B005C8Dbii3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    asins: list[str]
    compact_gti: str = Field(..., alias='compactGTI')
    gti: str
    is_launched: bool = Field(..., alias='isLaunched')
    link: str
    sequence_number: int = Field(..., alias='sequenceNumber')
    title_type: str = Field(..., alias='titleType')

class Amzn1DvGtiB6a9f76558690c96D76dA11fa169d6d7(BaseModel):
    model_config = ConfigDict(defer_build=True)
    asins: list[str]
    compact_gti: str = Field(..., alias='compactGTI')
    gti: str
    is_launched: bool = Field(..., alias='isLaunched')
    link: str
    sequence_number: int = Field(..., alias='sequenceNumber')
    title_type: str = Field(..., alias='titleType')

class B005C8E5382(BaseModel):
    model_config = ConfigDict(defer_build=True)
    asins: list[str]
    compact_gti: str = Field(..., alias='compactGTI')
    gti: str
    is_launched: bool = Field(..., alias='isLaunched')
    link: str
    sequence_number: int = Field(..., alias='sequenceNumber')
    title_type: str = Field(..., alias='titleType')

class Amzn1DvGtiC4a9f6faE70c0e699a947cdf3c7d6631(BaseModel):
    model_config = ConfigDict(defer_build=True)
    asins: list[str]
    compact_gti: str = Field(..., alias='compactGTI')
    gti: str
    is_launched: bool = Field(..., alias='isLaunched')
    link: str
    sequence_number: int = Field(..., alias='sequenceNumber')
    title_type: str = Field(..., alias='titleType')

class B005C8E70Y2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    asins: list[str]
    compact_gti: str = Field(..., alias='compactGTI')
    gti: str
    is_launched: bool = Field(..., alias='isLaunched')
    link: str
    sequence_number: int = Field(..., alias='sequenceNumber')
    title_type: str = Field(..., alias='titleType')

class Amzn1DvGtiAaa9f7ae63feE366767c20b5eadfeab8(BaseModel):
    model_config = ConfigDict(defer_build=True)
    asins: list[str]
    compact_gti: str = Field(..., alias='compactGTI')
    gti: str
    is_launched: bool = Field(..., alias='isLaunched')
    link: str
    sequence_number: int = Field(..., alias='sequenceNumber')
    title_type: str = Field(..., alias='titleType')

class B005G0R6Xi2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    asins: list[str]
    compact_gti: str = Field(..., alias='compactGTI')
    gti: str
    is_launched: bool = Field(..., alias='isLaunched')
    link: str
    sequence_number: int = Field(..., alias='sequenceNumber')
    title_type: str = Field(..., alias='titleType')

class Amzn1DvGti5aa9f7359f5910b02c3c1018f15c5796(BaseModel):
    model_config = ConfigDict(defer_build=True)
    asins: list[str]
    compact_gti: str = Field(..., alias='compactGTI')
    gti: str
    is_launched: bool = Field(..., alias='isLaunched')
    link: str
    sequence_number: int = Field(..., alias='sequenceNumber')
    title_type: str = Field(..., alias='titleType')

class B005C8Egx22(BaseModel):
    model_config = ConfigDict(defer_build=True)
    asins: list[str]
    compact_gti: str = Field(..., alias='compactGTI')
    gti: str
    is_launched: bool = Field(..., alias='isLaunched')
    link: str
    sequence_number: int = Field(..., alias='sequenceNumber')
    title_type: str = Field(..., alias='titleType')

class Amzn1DvGti5aa9f76fD62eF01089786ac8844b3ca7(BaseModel):
    model_config = ConfigDict(defer_build=True)
    asins: list[str]
    compact_gti: str = Field(..., alias='compactGTI')
    gti: str
    is_launched: bool = Field(..., alias='isLaunched')
    link: str
    sequence_number: int = Field(..., alias='sequenceNumber')
    title_type: str = Field(..., alias='titleType')

class B005C8Ei622(BaseModel):
    model_config = ConfigDict(defer_build=True)
    asins: list[str]
    compact_gti: str = Field(..., alias='compactGTI')
    gti: str
    is_launched: bool = Field(..., alias='isLaunched')
    link: str
    sequence_number: int = Field(..., alias='sequenceNumber')
    title_type: str = Field(..., alias='titleType')

class Amzn1DvGti38a9f74fD09070edD2527b3ddefdbb00(BaseModel):
    model_config = ConfigDict(defer_build=True)
    asins: list[str]
    compact_gti: str = Field(..., alias='compactGTI')
    gti: str
    is_launched: bool = Field(..., alias='isLaunched')
    link: str
    sequence_number: int = Field(..., alias='sequenceNumber')
    title_type: str = Field(..., alias='titleType')

class B005C8Ec7M2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    asins: list[str]
    compact_gti: str = Field(..., alias='compactGTI')
    gti: str
    is_launched: bool = Field(..., alias='isLaunched')
    link: str
    sequence_number: int = Field(..., alias='sequenceNumber')
    title_type: str = Field(..., alias='titleType')

class Amzn1DvGti50a9f76c6010D5b7834009d70dee5ab2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    asins: list[str]
    compact_gti: str = Field(..., alias='compactGTI')
    gti: str
    is_launched: bool = Field(..., alias='isLaunched')
    link: str
    sequence_number: int = Field(..., alias='sequenceNumber')
    title_type: str = Field(..., alias='titleType')

class B005C8Egeg2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    asins: list[str]
    compact_gti: str = Field(..., alias='compactGTI')
    gti: str
    is_launched: bool = Field(..., alias='isLaunched')
    link: str
    sequence_number: int = Field(..., alias='sequenceNumber')
    title_type: str = Field(..., alias='titleType')

class Amzn1DvGti38a9f7b30846E9dc0c32F086787b0d77(BaseModel):
    model_config = ConfigDict(defer_build=True)
    asins: list[str]
    compact_gti: str = Field(..., alias='compactGTI')
    gti: str
    is_launched: bool = Field(..., alias='isLaunched')
    link: str
    sequence_number: int = Field(..., alias='sequenceNumber')
    title_type: str = Field(..., alias='titleType')

class B005C8Elci2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    asins: list[str]
    compact_gti: str = Field(..., alias='compactGTI')
    gti: str
    is_launched: bool = Field(..., alias='isLaunched')
    link: str
    sequence_number: int = Field(..., alias='sequenceNumber')
    title_type: str = Field(..., alias='titleType')

class Amzn1DvGtiF0a9f6f7C7609037Ec5eD9e41cc1445a(BaseModel):
    model_config = ConfigDict(defer_build=True)
    asins: list[str]
    compact_gti: str = Field(..., alias='compactGTI')
    gti: str
    is_launched: bool = Field(..., alias='isLaunched')
    link: str
    sequence_number: int = Field(..., alias='sequenceNumber')
    title_type: str = Field(..., alias='titleType')

class B005C8Ed302(BaseModel):
    model_config = ConfigDict(defer_build=True)
    asins: list[str]
    compact_gti: str = Field(..., alias='compactGTI')
    gti: str
    is_launched: bool = Field(..., alias='isLaunched')
    link: str
    sequence_number: int = Field(..., alias='sequenceNumber')
    title_type: str = Field(..., alias='titleType')

class Amzn1DvGti94a9f7330d654faeB307Af5e31bfd133(BaseModel):
    model_config = ConfigDict(defer_build=True)
    asins: list[str]
    compact_gti: str = Field(..., alias='compactGTI')
    gti: str
    is_launched: bool = Field(..., alias='isLaunched')
    link: str
    sequence_number: int = Field(..., alias='sequenceNumber')
    title_type: str = Field(..., alias='titleType')

class B005C8Dike2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    asins: list[str]
    compact_gti: str = Field(..., alias='compactGTI')
    gti: str
    is_launched: bool = Field(..., alias='isLaunched')
    link: str
    sequence_number: int = Field(..., alias='sequenceNumber')
    title_type: str = Field(..., alias='titleType')

class Amzn1DvGti7ea9f73d49f6Ee30F08e7615e67cc2e0(BaseModel):
    model_config = ConfigDict(defer_build=True)
    asins: list[str]
    compact_gti: str = Field(..., alias='compactGTI')
    gti: str
    is_launched: bool = Field(..., alias='isLaunched')
    link: str
    sequence_number: int = Field(..., alias='sequenceNumber')
    title_type: str = Field(..., alias='titleType')

class B005C8Ecls2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    asins: list[str]
    compact_gti: str = Field(..., alias='compactGTI')
    gti: str
    is_launched: bool = Field(..., alias='isLaunched')
    link: str
    sequence_number: int = Field(..., alias='sequenceNumber')
    title_type: str = Field(..., alias='titleType')

class Amzn1DvGtiFaa9f72dD08f348538a81dc7d58c8322(BaseModel):
    model_config = ConfigDict(defer_build=True)
    asins: list[str]
    compact_gti: str = Field(..., alias='compactGTI')
    gti: str
    is_launched: bool = Field(..., alias='isLaunched')
    link: str
    sequence_number: int = Field(..., alias='sequenceNumber')
    title_type: str = Field(..., alias='titleType')

class B005C8Dtto2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    asins: list[str]
    compact_gti: str = Field(..., alias='compactGTI')
    gti: str
    is_launched: bool = Field(..., alias='isLaunched')
    link: str
    sequence_number: int = Field(..., alias='sequenceNumber')
    title_type: str = Field(..., alias='titleType')

class Amzn1DvGtiD6a9f72146c8670cAc5097fbe1817840(BaseModel):
    model_config = ConfigDict(defer_build=True)
    asins: list[str]
    compact_gti: str = Field(..., alias='compactGTI')
    gti: str
    is_launched: bool = Field(..., alias='isLaunched')
    link: str
    sequence_number: int = Field(..., alias='sequenceNumber')
    title_type: str = Field(..., alias='titleType')

class B005C8E91Q2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    asins: list[str]
    compact_gti: str = Field(..., alias='compactGTI')
    gti: str
    is_launched: bool = Field(..., alias='isLaunched')
    link: str
    sequence_number: int = Field(..., alias='sequenceNumber')
    title_type: str = Field(..., alias='titleType')

class Amzn1DvGti04a9f75cB19d77e1Fd861874ab829fe1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    asins: list[str]
    compact_gti: str = Field(..., alias='compactGTI')
    gti: str
    is_launched: bool = Field(..., alias='isLaunched')
    link: str
    sequence_number: int = Field(..., alias='sequenceNumber')
    title_type: str = Field(..., alias='titleType')

class B005C8Dkvg2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    asins: list[str]
    compact_gti: str = Field(..., alias='compactGTI')
    gti: str
    is_launched: bool = Field(..., alias='isLaunched')
    link: str
    sequence_number: int = Field(..., alias='sequenceNumber')
    title_type: str = Field(..., alias='titleType')

class Amzn1DvGti32a9f7586b150034B3ee2483e4cf8ef0(BaseModel):
    model_config = ConfigDict(defer_build=True)
    asins: list[str]
    compact_gti: str = Field(..., alias='compactGTI')
    gti: str
    is_launched: bool = Field(..., alias='isLaunched')
    link: str
    sequence_number: int = Field(..., alias='sequenceNumber')
    title_type: str = Field(..., alias='titleType')

class B005C8Ei5S2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    asins: list[str]
    compact_gti: str = Field(..., alias='compactGTI')
    gti: str
    is_launched: bool = Field(..., alias='isLaunched')
    link: str
    sequence_number: int = Field(..., alias='sequenceNumber')
    title_type: str = Field(..., alias='titleType')

class Amzn1DvGti88a9f7572a26850dC5fb445796019594(BaseModel):
    model_config = ConfigDict(defer_build=True)
    asins: list[str]
    compact_gti: str = Field(..., alias='compactGTI')
    gti: str
    is_launched: bool = Field(..., alias='isLaunched')
    link: str
    sequence_number: int = Field(..., alias='sequenceNumber')
    title_type: str = Field(..., alias='titleType')

class B005C8Eiui2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    asins: list[str]
    compact_gti: str = Field(..., alias='compactGTI')
    gti: str
    is_launched: bool = Field(..., alias='isLaunched')
    link: str
    sequence_number: int = Field(..., alias='sequenceNumber')
    title_type: str = Field(..., alias='titleType')

class Amzn1DvGti96a9f7a206fd7ad08f2a1384d42a5fa0(BaseModel):
    model_config = ConfigDict(defer_build=True)
    asins: list[str]
    compact_gti: str = Field(..., alias='compactGTI')
    gti: str
    is_launched: bool = Field(..., alias='isLaunched')
    link: str
    sequence_number: int = Field(..., alias='sequenceNumber')
    title_type: str = Field(..., alias='titleType')

class B005C8Emmm2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    asins: list[str]
    compact_gti: str = Field(..., alias='compactGTI')
    gti: str
    is_launched: bool = Field(..., alias='isLaunched')
    link: str
    sequence_number: int = Field(..., alias='sequenceNumber')
    title_type: str = Field(..., alias='titleType')

class Amzn1DvGtiD0a9f7861862Bd0a30beD2d7c61debda(BaseModel):
    model_config = ConfigDict(defer_build=True)
    asins: list[str]
    compact_gti: str = Field(..., alias='compactGTI')
    gti: str
    is_launched: bool = Field(..., alias='isLaunched')
    link: str
    sequence_number: int = Field(..., alias='sequenceNumber')
    title_type: str = Field(..., alias='titleType')

class B005C8Eh2W2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    asins: list[str]
    compact_gti: str = Field(..., alias='compactGTI')
    gti: str
    is_launched: bool = Field(..., alias='isLaunched')
    link: str
    sequence_number: int = Field(..., alias='sequenceNumber')
    title_type: str = Field(..., alias='titleType')

class Amzn1DvGti42a9f768Ec3523d241ae4e7d048f3568(BaseModel):
    model_config = ConfigDict(defer_build=True)
    asins: list[str]
    compact_gti: str = Field(..., alias='compactGTI')
    gti: str
    is_launched: bool = Field(..., alias='isLaunched')
    link: str
    sequence_number: int = Field(..., alias='sequenceNumber')
    title_type: str = Field(..., alias='titleType')

class B005C8Ebws2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    asins: list[str]
    compact_gti: str = Field(..., alias='compactGTI')
    gti: str
    is_launched: bool = Field(..., alias='isLaunched')
    link: str
    sequence_number: int = Field(..., alias='sequenceNumber')
    title_type: str = Field(..., alias='titleType')

class Amzn1DvGtiF4a9f7b0E9f3851c8709A9fdda3de7b9(BaseModel):
    model_config = ConfigDict(defer_build=True)
    asins: list[str]
    compact_gti: str = Field(..., alias='compactGTI')
    gti: str
    is_launched: bool = Field(..., alias='isLaunched')
    link: str
    sequence_number: int = Field(..., alias='sequenceNumber')
    title_type: str = Field(..., alias='titleType')

class B005C8Ds0Y2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    asins: list[str]
    compact_gti: str = Field(..., alias='compactGTI')
    gti: str
    is_launched: bool = Field(..., alias='isLaunched')
    link: str
    sequence_number: int = Field(..., alias='sequenceNumber')
    title_type: str = Field(..., alias='titleType')

class Amzn1DvGti44a9f70aE1c43f1182c15a219359627c(BaseModel):
    model_config = ConfigDict(defer_build=True)
    asins: list[str]
    compact_gti: str = Field(..., alias='compactGTI')
    gti: str
    is_launched: bool = Field(..., alias='isLaunched')
    link: str
    sequence_number: int = Field(..., alias='sequenceNumber')
    title_type: str = Field(..., alias='titleType')

class B005C8E5A62(BaseModel):
    model_config = ConfigDict(defer_build=True)
    asins: list[str]
    compact_gti: str = Field(..., alias='compactGTI')
    gti: str
    is_launched: bool = Field(..., alias='isLaunched')
    link: str
    sequence_number: int = Field(..., alias='sequenceNumber')
    title_type: str = Field(..., alias='titleType')

class Amzn1DvGtiC8a9f75165aa4e636836897328709e07(BaseModel):
    model_config = ConfigDict(defer_build=True)
    asins: list[str]
    compact_gti: str = Field(..., alias='compactGTI')
    gti: str
    is_launched: bool = Field(..., alias='isLaunched')
    link: str
    sequence_number: int = Field(..., alias='sequenceNumber')
    title_type: str = Field(..., alias='titleType')

class B005C8Ef8I2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    asins: list[str]
    compact_gti: str = Field(..., alias='compactGTI')
    gti: str
    is_launched: bool = Field(..., alias='isLaunched')
    link: str
    sequence_number: int = Field(..., alias='sequenceNumber')
    title_type: str = Field(..., alias='titleType')

class Amzn1DvGti76a9f761FddaDd36AfbcB029a965b322(BaseModel):
    model_config = ConfigDict(defer_build=True)
    asins: list[str]
    compact_gti: str = Field(..., alias='compactGTI')
    gti: str
    is_launched: bool = Field(..., alias='isLaunched')
    link: str
    sequence_number: int = Field(..., alias='sequenceNumber')
    title_type: str = Field(..., alias='titleType')

class B005C8Ek9M2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    asins: list[str]
    compact_gti: str = Field(..., alias='compactGTI')
    gti: str
    is_launched: bool = Field(..., alias='isLaunched')
    link: str
    sequence_number: int = Field(..., alias='sequenceNumber')
    title_type: str = Field(..., alias='titleType')

class Amzn1DvGti97a2765847704c94Bda803fa1245f0be(BaseModel):
    model_config = ConfigDict(defer_build=True)
    asins: list[str]
    compact_gti: str = Field(..., alias='compactGTI')
    gti: str
    is_launched: bool = Field(..., alias='isLaunched')
    link: str
    sequence_number: int = Field(..., alias='sequenceNumber')
    title_type: str = Field(..., alias='titleType')

class B0Cjp8Rbmq3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    asins: list[str]
    compact_gti: str = Field(..., alias='compactGTI')
    gti: str
    is_launched: bool = Field(..., alias='isLaunched')
    link: str
    sequence_number: int = Field(..., alias='sequenceNumber')
    title_type: str = Field(..., alias='titleType')

class Amzn1DvGtiC28e3a6099ca45399248Ef3cc2a04f75(BaseModel):
    model_config = ConfigDict(defer_build=True)
    asins: list[str]
    compact_gti: str = Field(..., alias='compactGTI')
    gti: str
    is_launched: bool = Field(..., alias='isLaunched')
    link: str
    sequence_number: int = Field(..., alias='sequenceNumber')
    title_type: str = Field(..., alias='titleType')

class B0Ck832Gg52(BaseModel):
    model_config = ConfigDict(defer_build=True)
    asins: list[str]
    compact_gti: str = Field(..., alias='compactGTI')
    gti: str
    is_launched: bool = Field(..., alias='isLaunched')
    link: str
    sequence_number: int = Field(..., alias='sequenceNumber')
    title_type: str = Field(..., alias='titleType')

class Amzn1DvGti34eed07b985c4f0fA1e21faa9fa77c70(BaseModel):
    model_config = ConfigDict(defer_build=True)
    asins: list[str]
    compact_gti: str = Field(..., alias='compactGTI')
    gti: str
    is_launched: bool = Field(..., alias='isLaunched')
    link: str
    sequence_number: int = Field(..., alias='sequenceNumber')
    title_type: str = Field(..., alias='titleType')

class B0Chsjdg3Y2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    asins: list[str]
    compact_gti: str = Field(..., alias='compactGTI')
    gti: str
    is_launched: bool = Field(..., alias='isLaunched')
    link: str
    sequence_number: int = Field(..., alias='sequenceNumber')
    title_type: str = Field(..., alias='titleType')

class Amzn1DvGti2d4f68232a774bf385a2E75a87852fc2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    asins: list[str]
    compact_gti: str = Field(..., alias='compactGTI')
    gti: str
    is_launched: bool = Field(..., alias='isLaunched')
    link: str
    sequence_number: int = Field(..., alias='sequenceNumber')
    title_type: str = Field(..., alias='titleType')

class B0Cgpsngts2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    asins: list[str]
    compact_gti: str = Field(..., alias='compactGTI')
    gti: str
    is_launched: bool = Field(..., alias='isLaunched')
    link: str
    sequence_number: int = Field(..., alias='sequenceNumber')
    title_type: str = Field(..., alias='titleType')

class Amzn1DvGti967ee13668434c8f8d3e88e2191b32a9(BaseModel):
    model_config = ConfigDict(defer_build=True)
    asins: list[str]
    compact_gti: str = Field(..., alias='compactGTI')
    gti: str
    is_launched: bool = Field(..., alias='isLaunched')
    link: str
    sequence_number: int = Field(..., alias='sequenceNumber')
    title_type: str = Field(..., alias='titleType')

class B0Chjln6Gs2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    asins: list[str]
    compact_gti: str = Field(..., alias='compactGTI')
    gti: str
    is_launched: bool = Field(..., alias='isLaunched')
    link: str
    sequence_number: int = Field(..., alias='sequenceNumber')
    title_type: str = Field(..., alias='titleType')

class Amzn1DvGti35c8dc98E6ad4af1Bc99289ea71be7e2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    asins: list[str]
    compact_gti: str = Field(..., alias='compactGTI')
    gti: str
    is_launched: bool = Field(..., alias='isLaunched')
    link: str
    sequence_number: int = Field(..., alias='sequenceNumber')
    title_type: str = Field(..., alias='titleType')

class B0Chpmk42L2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    asins: list[str]
    compact_gti: str = Field(..., alias='compactGTI')
    gti: str
    is_launched: bool = Field(..., alias='isLaunched')
    link: str
    sequence_number: int = Field(..., alias='sequenceNumber')
    title_type: str = Field(..., alias='titleType')

class Amzn1DvGti1fcd5cf358d545b89ce874d19866fa5e(BaseModel):
    model_config = ConfigDict(defer_build=True)
    asins: list[str]
    compact_gti: str = Field(..., alias='compactGTI')
    gti: str
    is_launched: bool = Field(..., alias='isLaunched')
    link: str
    sequence_number: int = Field(..., alias='sequenceNumber')
    title_type: str = Field(..., alias='titleType')

class B0Cjcmt4Xn2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    asins: list[str]
    compact_gti: str = Field(..., alias='compactGTI')
    gti: str
    is_launched: bool = Field(..., alias='isLaunched')
    link: str
    sequence_number: int = Field(..., alias='sequenceNumber')
    title_type: str = Field(..., alias='titleType')

class Amzn1DvGti949955796c92495eBcf274b7f0980acc(BaseModel):
    model_config = ConfigDict(defer_build=True)
    asins: list[str]
    compact_gti: str = Field(..., alias='compactGTI')
    gti: str
    is_launched: bool = Field(..., alias='isLaunched')
    link: str
    sequence_number: int = Field(..., alias='sequenceNumber')
    title_type: str = Field(..., alias='titleType')

class B0Cgx6W4Gk2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    asins: list[str]
    compact_gti: str = Field(..., alias='compactGTI')
    gti: str
    is_launched: bool = Field(..., alias='isLaunched')
    link: str
    sequence_number: int = Field(..., alias='sequenceNumber')
    title_type: str = Field(..., alias='titleType')

class Amzn1DvGti0e5e58fb4e8646499c8c3a13d7725d25(BaseModel):
    model_config = ConfigDict(defer_build=True)
    asins: list[str]
    compact_gti: str = Field(..., alias='compactGTI')
    gti: str
    is_launched: bool = Field(..., alias='isLaunched')
    link: str
    sequence_number: int = Field(..., alias='sequenceNumber')
    title_type: str = Field(..., alias='titleType')

class B0Ch4Tmyh22(BaseModel):
    model_config = ConfigDict(defer_build=True)
    asins: list[str]
    compact_gti: str = Field(..., alias='compactGTI')
    gti: str
    is_launched: bool = Field(..., alias='isLaunched')
    link: str
    sequence_number: int = Field(..., alias='sequenceNumber')
    title_type: str = Field(..., alias='titleType')

class Amzn1DvGtiAc594480D6b948c3A3c369b4a69ce14a(BaseModel):
    model_config = ConfigDict(defer_build=True)
    asins: list[str]
    compact_gti: str = Field(..., alias='compactGTI')
    gti: str
    is_launched: bool = Field(..., alias='isLaunched')
    link: str
    sequence_number: int = Field(..., alias='sequenceNumber')
    title_type: str = Field(..., alias='titleType')

class B0Cjqd32Q62(BaseModel):
    model_config = ConfigDict(defer_build=True)
    asins: list[str]
    compact_gti: str = Field(..., alias='compactGTI')
    gti: str
    is_launched: bool = Field(..., alias='isLaunched')
    link: str
    sequence_number: int = Field(..., alias='sequenceNumber')
    title_type: str = Field(..., alias='titleType')

class Amzn1DvGti5806cfcf58a347deA96019642dbb297b(BaseModel):
    model_config = ConfigDict(defer_build=True)
    asins: list[str]
    compact_gti: str = Field(..., alias='compactGTI')
    gti: str
    is_launched: bool = Field(..., alias='isLaunched')
    link: str
    sequence_number: int = Field(..., alias='sequenceNumber')
    title_type: str = Field(..., alias='titleType')

class B0Cj658T6K2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    asins: list[str]
    compact_gti: str = Field(..., alias='compactGTI')
    gti: str
    is_launched: bool = Field(..., alias='isLaunched')
    link: str
    sequence_number: int = Field(..., alias='sequenceNumber')
    title_type: str = Field(..., alias='titleType')

class Amzn1DvGti3cf8dc4e533b4c69A131Ec0c79871752(BaseModel):
    model_config = ConfigDict(defer_build=True)
    asins: list[str]
    compact_gti: str = Field(..., alias='compactGTI')
    gti: str
    is_launched: bool = Field(..., alias='isLaunched')
    link: str
    sequence_number: int = Field(..., alias='sequenceNumber')
    title_type: str = Field(..., alias='titleType')

class B0Cjq1Pt9T2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    asins: list[str]
    compact_gti: str = Field(..., alias='compactGTI')
    gti: str
    is_launched: bool = Field(..., alias='isLaunched')
    link: str
    sequence_number: int = Field(..., alias='sequenceNumber')
    title_type: str = Field(..., alias='titleType')

class Self1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    amzn1_dv_gti_8ca9f71e_f000_61b3_3398_19b8b550587b: Amzn1DvGti8ca9f71eF00061b3339819b8b550587b | None = Field(None, alias='amzn1.dv.gti.8ca9f71e-f000-61b3-3398-19b8b550587b')
    b005_c8_dbii: B005C8Dbii3 | None = Field(None, alias='B005C8DBII')
    amzn1_dv_gti_b6a9f765_5869_0c96_d76d_a11fa169d6d7: Amzn1DvGtiB6a9f76558690c96D76dA11fa169d6d7 | None = Field(None, alias='amzn1.dv.gti.b6a9f765-5869-0c96-d76d-a11fa169d6d7')
    b005_c8_e538: B005C8E5382 | None = Field(None, alias='B005C8E538')
    amzn1_dv_gti_c4a9f6fa_e70c_0e69_9a94_7cdf3c7d6631: Amzn1DvGtiC4a9f6faE70c0e699a947cdf3c7d6631 | None = Field(None, alias='amzn1.dv.gti.c4a9f6fa-e70c-0e69-9a94-7cdf3c7d6631')
    b005_c8_e70_y: B005C8E70Y2 | None = Field(None, alias='B005C8E70Y')
    amzn1_dv_gti_aaa9f7ae_63fe_e366_767c_20b5eadfeab8: Amzn1DvGtiAaa9f7ae63feE366767c20b5eadfeab8 | None = Field(None, alias='amzn1.dv.gti.aaa9f7ae-63fe-e366-767c-20b5eadfeab8')
    b005_g0_r6_xi: B005G0R6Xi2 | None = Field(None, alias='B005G0R6XI')
    amzn1_dv_gti_5aa9f735_9f59_10b0_2c3c_1018f15c5796: Amzn1DvGti5aa9f7359f5910b02c3c1018f15c5796 | None = Field(None, alias='amzn1.dv.gti.5aa9f735-9f59-10b0-2c3c-1018f15c5796')
    b005_c8_egx2: B005C8Egx22 | None = Field(None, alias='B005C8EGX2')
    amzn1_dv_gti_5aa9f76f_d62e_f010_8978_6ac8844b3ca7: Amzn1DvGti5aa9f76fD62eF01089786ac8844b3ca7 | None = Field(None, alias='amzn1.dv.gti.5aa9f76f-d62e-f010-8978-6ac8844b3ca7')
    b005_c8_ei62: B005C8Ei622 | None = Field(None, alias='B005C8EI62')
    amzn1_dv_gti_38a9f74f_d090_70ed_d252_7b3ddefdbb00: Amzn1DvGti38a9f74fD09070edD2527b3ddefdbb00 | None = Field(None, alias='amzn1.dv.gti.38a9f74f-d090-70ed-d252-7b3ddefdbb00')
    b005_c8_ec7_m: B005C8Ec7M2 | None = Field(None, alias='B005C8EC7M')
    amzn1_dv_gti_50a9f76c_6010_d5b7_8340_09d70dee5ab2: Amzn1DvGti50a9f76c6010D5b7834009d70dee5ab2 | None = Field(None, alias='amzn1.dv.gti.50a9f76c-6010-d5b7-8340-09d70dee5ab2')
    b005_c8_egeg: B005C8Egeg2 | None = Field(None, alias='B005C8EGEG')
    amzn1_dv_gti_38a9f7b3_0846_e9dc_0c32_f086787b0d77: Amzn1DvGti38a9f7b30846E9dc0c32F086787b0d77 | None = Field(None, alias='amzn1.dv.gti.38a9f7b3-0846-e9dc-0c32-f086787b0d77')
    b005_c8_elci: B005C8Elci2 | None = Field(None, alias='B005C8ELCI')
    amzn1_dv_gti_f0a9f6f7_c760_9037_ec5e_d9e41cc1445a: Amzn1DvGtiF0a9f6f7C7609037Ec5eD9e41cc1445a | None = Field(None, alias='amzn1.dv.gti.f0a9f6f7-c760-9037-ec5e-d9e41cc1445a')
    b005_c8_ed30: B005C8Ed302 | None = Field(None, alias='B005C8ED30')
    amzn1_dv_gti_94a9f733_0d65_4fae_b307_af5e31bfd133: Amzn1DvGti94a9f7330d654faeB307Af5e31bfd133 | None = Field(None, alias='amzn1.dv.gti.94a9f733-0d65-4fae-b307-af5e31bfd133')
    b005_c8_dike: B005C8Dike2 | None = Field(None, alias='B005C8DIKE')
    amzn1_dv_gti_7ea9f73d_49f6_ee30_f08e_7615e67cc2e0: Amzn1DvGti7ea9f73d49f6Ee30F08e7615e67cc2e0 | None = Field(None, alias='amzn1.dv.gti.7ea9f73d-49f6-ee30-f08e-7615e67cc2e0')
    b005_c8_ecls: B005C8Ecls2 | None = Field(None, alias='B005C8ECLS')
    amzn1_dv_gti_faa9f72d_d08f_3485_38a8_1dc7d58c8322: Amzn1DvGtiFaa9f72dD08f348538a81dc7d58c8322 | None = Field(None, alias='amzn1.dv.gti.faa9f72d-d08f-3485-38a8-1dc7d58c8322')
    b005_c8_dtto: B005C8Dtto2 | None = Field(None, alias='B005C8DTTO')
    amzn1_dv_gti_d6a9f721_46c8_670c_ac50_97fbe1817840: Amzn1DvGtiD6a9f72146c8670cAc5097fbe1817840 | None = Field(None, alias='amzn1.dv.gti.d6a9f721-46c8-670c-ac50-97fbe1817840')
    b005_c8_e91_q: B005C8E91Q2 | None = Field(None, alias='B005C8E91Q')
    amzn1_dv_gti_04a9f75c_b19d_77e1_fd86_1874ab829fe1: Amzn1DvGti04a9f75cB19d77e1Fd861874ab829fe1 | None = Field(None, alias='amzn1.dv.gti.04a9f75c-b19d-77e1-fd86-1874ab829fe1')
    b005_c8_dkvg: B005C8Dkvg2 | None = Field(None, alias='B005C8DKVG')
    amzn1_dv_gti_32a9f758_6b15_0034_b3ee_2483e4cf8ef0: Amzn1DvGti32a9f7586b150034B3ee2483e4cf8ef0 | None = Field(None, alias='amzn1.dv.gti.32a9f758-6b15-0034-b3ee-2483e4cf8ef0')
    b005_c8_ei5_s: B005C8Ei5S2 | None = Field(None, alias='B005C8EI5S')
    amzn1_dv_gti_88a9f757_2a26_850d_c5fb_445796019594: Amzn1DvGti88a9f7572a26850dC5fb445796019594 | None = Field(None, alias='amzn1.dv.gti.88a9f757-2a26-850d-c5fb-445796019594')
    b005_c8_eiui: B005C8Eiui2 | None = Field(None, alias='B005C8EIUI')
    amzn1_dv_gti_96a9f7a2_06fd_7ad0_8f2a_1384d42a5fa0: Amzn1DvGti96a9f7a206fd7ad08f2a1384d42a5fa0 | None = Field(None, alias='amzn1.dv.gti.96a9f7a2-06fd-7ad0-8f2a-1384d42a5fa0')
    b005_c8_emmm: B005C8Emmm2 | None = Field(None, alias='B005C8EMMM')
    amzn1_dv_gti_d0a9f786_1862_bd0a_30be_d2d7c61debda: Amzn1DvGtiD0a9f7861862Bd0a30beD2d7c61debda | None = Field(None, alias='amzn1.dv.gti.d0a9f786-1862-bd0a-30be-d2d7c61debda')
    b005_c8_eh2_w: B005C8Eh2W2 | None = Field(None, alias='B005C8EH2W')
    amzn1_dv_gti_42a9f768_ec35_23d2_41ae_4e7d048f3568: Amzn1DvGti42a9f768Ec3523d241ae4e7d048f3568 | None = Field(None, alias='amzn1.dv.gti.42a9f768-ec35-23d2-41ae-4e7d048f3568')
    b005_c8_ebws: B005C8Ebws2 | None = Field(None, alias='B005C8EBWS')
    amzn1_dv_gti_f4a9f7b0_e9f3_851c_8709_a9fdda3de7b9: Amzn1DvGtiF4a9f7b0E9f3851c8709A9fdda3de7b9 | None = Field(None, alias='amzn1.dv.gti.f4a9f7b0-e9f3-851c-8709-a9fdda3de7b9')
    b005_c8_ds0_y: B005C8Ds0Y2 | None = Field(None, alias='B005C8DS0Y')
    amzn1_dv_gti_44a9f70a_e1c4_3f11_82c1_5a219359627c: Amzn1DvGti44a9f70aE1c43f1182c15a219359627c | None = Field(None, alias='amzn1.dv.gti.44a9f70a-e1c4-3f11-82c1-5a219359627c')
    b005_c8_e5_a6: B005C8E5A62 | None = Field(None, alias='B005C8E5A6')
    amzn1_dv_gti_c8a9f751_65aa_4e63_6836_897328709e07: Amzn1DvGtiC8a9f75165aa4e636836897328709e07 | None = Field(None, alias='amzn1.dv.gti.c8a9f751-65aa-4e63-6836-897328709e07')
    b005_c8_ef8_i: B005C8Ef8I2 | None = Field(None, alias='B005C8EF8I')
    amzn1_dv_gti_76a9f761_fdda_dd36_afbc_b029a965b322: Amzn1DvGti76a9f761FddaDd36AfbcB029a965b322 | None = Field(None, alias='amzn1.dv.gti.76a9f761-fdda-dd36-afbc-b029a965b322')
    b005_c8_ek9_m: B005C8Ek9M2 | None = Field(None, alias='B005C8EK9M')
    amzn1_dv_gti_97a27658_4770_4c94_bda8_03fa1245f0be: Amzn1DvGti97a2765847704c94Bda803fa1245f0be | None = Field(None, alias='amzn1.dv.gti.97a27658-4770-4c94-bda8-03fa1245f0be')
    b0_cjp8_rbmq: B0Cjp8Rbmq3 | None = Field(None, alias='B0CJP8RBMQ')
    amzn1_dv_gti_c28e3a60_99ca_4539_9248_ef3cc2a04f75: Amzn1DvGtiC28e3a6099ca45399248Ef3cc2a04f75 | None = Field(None, alias='amzn1.dv.gti.c28e3a60-99ca-4539-9248-ef3cc2a04f75')
    b0_ck832_gg5: B0Ck832Gg52 | None = Field(None, alias='B0CK832GG5')
    amzn1_dv_gti_34eed07b_985c_4f0f_a1e2_1faa9fa77c70: Amzn1DvGti34eed07b985c4f0fA1e21faa9fa77c70 | None = Field(None, alias='amzn1.dv.gti.34eed07b-985c-4f0f-a1e2-1faa9fa77c70')
    b0_chsjdg3_y: B0Chsjdg3Y2 | None = Field(None, alias='B0CHSJDG3Y')
    amzn1_dv_gti_2d4f6823_2a77_4bf3_85a2_e75a87852fc2: Amzn1DvGti2d4f68232a774bf385a2E75a87852fc2 | None = Field(None, alias='amzn1.dv.gti.2d4f6823-2a77-4bf3-85a2-e75a87852fc2')
    b0_cgpsngts: B0Cgpsngts2 | None = Field(None, alias='B0CGPSNGTS')
    amzn1_dv_gti_967ee136_6843_4c8f_8d3e_88e2191b32a9: Amzn1DvGti967ee13668434c8f8d3e88e2191b32a9 | None = Field(None, alias='amzn1.dv.gti.967ee136-6843-4c8f-8d3e-88e2191b32a9')
    b0_chjln6_gs: B0Chjln6Gs2 | None = Field(None, alias='B0CHJLN6GS')
    amzn1_dv_gti_35c8dc98_e6ad_4af1_bc99_289ea71be7e2: Amzn1DvGti35c8dc98E6ad4af1Bc99289ea71be7e2 | None = Field(None, alias='amzn1.dv.gti.35c8dc98-e6ad-4af1-bc99-289ea71be7e2')
    b0_chpmk42_l: B0Chpmk42L2 | None = Field(None, alias='B0CHPMK42L')
    amzn1_dv_gti_1fcd5cf3_58d5_45b8_9ce8_74d19866fa5e: Amzn1DvGti1fcd5cf358d545b89ce874d19866fa5e | None = Field(None, alias='amzn1.dv.gti.1fcd5cf3-58d5-45b8-9ce8-74d19866fa5e')
    b0_cjcmt4_xn: B0Cjcmt4Xn2 | None = Field(None, alias='B0CJCMT4XN')
    amzn1_dv_gti_94995579_6c92_495e_bcf2_74b7f0980acc: Amzn1DvGti949955796c92495eBcf274b7f0980acc | None = Field(None, alias='amzn1.dv.gti.94995579-6c92-495e-bcf2-74b7f0980acc')
    b0_cgx6_w4_gk: B0Cgx6W4Gk2 | None = Field(None, alias='B0CGX6W4GK')
    amzn1_dv_gti_0e5e58fb_4e86_4649_9c8c_3a13d7725d25: Amzn1DvGti0e5e58fb4e8646499c8c3a13d7725d25 | None = Field(None, alias='amzn1.dv.gti.0e5e58fb-4e86-4649-9c8c-3a13d7725d25')
    b0_ch4_tmyh2: B0Ch4Tmyh22 | None = Field(None, alias='B0CH4TMYH2')
    amzn1_dv_gti_ac594480_d6b9_48c3_a3c3_69b4a69ce14a: Amzn1DvGtiAc594480D6b948c3A3c369b4a69ce14a | None = Field(None, alias='amzn1.dv.gti.ac594480-d6b9-48c3-a3c3-69b4a69ce14a')
    b0_cjqd32_q6: B0Cjqd32Q62 | None = Field(None, alias='B0CJQD32Q6')
    amzn1_dv_gti_5806cfcf_58a3_47de_a960_19642dbb297b: Amzn1DvGti5806cfcf58a347deA96019642dbb297b | None = Field(None, alias='amzn1.dv.gti.5806cfcf-58a3-47de-a960-19642dbb297b')
    b0_cj658_t6_k: B0Cj658T6K2 | None = Field(None, alias='B0CJ658T6K')
    amzn1_dv_gti_3cf8dc4e_533b_4c69_a131_ec0c79871752: Amzn1DvGti3cf8dc4e533b4c69A131Ec0c79871752 | None = Field(None, alias='amzn1.dv.gti.3cf8dc4e-533b-4c69-a131-ec0c79871752')
    b0_cjq1_pt9_t: B0Cjq1Pt9T2 | None = Field(None, alias='B0CJQ1PT9T')

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

class FocusMessage39(BaseModel):
    model_config = ConfigDict(defer_build=True)
    icon: str
    message: str

class GlanceMessage(BaseModel):
    model_config = ConfigDict(defer_build=True)
    icon: str | None = None
    message: str

class HighValueMessage2(BaseModel):
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
    entitlement_type: str = Field(..., alias='entitlementType')
    focus_message: FocusMessage39 = Field(..., alias='focusMessage')
    glance_message: GlanceMessage = Field(..., alias='glanceMessage')
    high_value_message: HighValueMessage2 = Field(..., alias='highValueMessage')
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

class Images45(BaseModel):
    model_config = ConfigDict(defer_build=True)
    cover: Cover

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

class Endpoint3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    partial_url: str = Field(..., alias='partialURL')
    query: Query

class Action66(BaseModel):
    model_config = ConfigDict(defer_build=True)
    ajax_enabled: bool = Field(..., alias='ajaxEnabled')
    endpoint: Endpoint3
    format_code: str = Field(..., alias='formatCode')
    tag: str
    text: Text

class Item(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field__type: str = Field(..., alias='__type')
    action: Action66
    item_type: str = Field(..., alias='itemType')
    text: str

class OverflowMenu(BaseModel):
    model_config = ConfigDict(defer_build=True)
    items: list[Item]
    title: str

class Endpoint4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    partial_url: str = Field(..., alias='partialURL')
    query: Query

class WatchlistAction(BaseModel):
    model_config = ConfigDict(defer_build=True)
    ajax_enabled: bool = Field(..., alias='ajaxEnabled')
    endpoint: Endpoint4
    format_code: str = Field(..., alias='formatCode')
    tag: str
    text: Text

class Entity(BaseModel):
    model_config = ConfigDict(defer_build=True)
    buy_box_actions: list[None] = Field(..., alias='buyBoxActions')
    customer_reviews: CustomerReviews | None = Field(None, alias='customerReviews')
    degradations: list[None]
    display_title: str = Field(..., alias='displayTitle')
    entitlement_cues: EntitlementCues = Field(..., alias='entitlementCues')
    entity_type: str = Field(..., alias='entityType')
    hover_info: HoverInfo = Field(..., alias='hoverInfo')
    images: Images45
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

class EntitlementCues1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    entitled_carousel: str = Field(..., alias='entitledCarousel')
    offer_type: str = Field(..., alias='offerType')

class B005C8Db7EItem1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    container_type: str = Field(..., alias='containerType')
    entities: list[Entity]
    entitlement_cues: EntitlementCues1 = Field(..., alias='entitlementCues')
    estimated_total: int = Field(..., alias='estimatedTotal')
    impression_data: str = Field(..., alias='impressionData')
    inline_container_update_actions: list[None] = Field(..., alias='inlineContainerUpdateActions')
    is_continue_watching: bool = Field(..., alias='isContinueWatching')
    journey_ingress_context: str = Field(..., alias='journeyIngressContext')
    pagination_service_token: str = Field(..., alias='paginationServiceToken')
    pagination_start_index: int = Field(..., alias='paginationStartIndex')
    pagination_target_id: str = Field(..., alias='paginationTargetId')
    strings: dict[str, Any]
    text: str
    title: str
    web_uid: str = Field(..., alias='webUid')

class CategorizedGenres(BaseModel):
    model_config = ConfigDict(defer_build=True)
    primary_genre: str = Field(..., alias='primaryGenre')
    secondary_genres: list[str] | None = Field(None, alias='secondaryGenres')

class CustomerReviews1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    count: int
    count_formatted: str = Field(..., alias='countFormatted')
    customer_reviews_text: CustomerReviewsText = Field(..., alias='customerReviewsText')
    link: str
    value: int | float

class FocusMessage40(BaseModel):
    model_config = ConfigDict(defer_build=True)
    icon: str | None = None
    message: str

class ProviderLogo2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    image_url: str | None = Field(None, alias='imageUrl')
    message: str | None = None
    logo_scalar_horizontal: str | None = Field(None, alias='logoScalarHorizontal')

class EntitlementCues2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    buybox_message: dict[str, Any] = Field(..., alias='buyboxMessage')
    compact_focus_message: dict[str, Any] = Field(..., alias='compactFocusMessage')
    content_source_logo: dict[str, Any] = Field(..., alias='contentSourceLogo')
    entitlement_type: str | None = Field(None, alias='entitlementType')
    focus_message: FocusMessage40 = Field(..., alias='focusMessage')
    glance_message: GlanceMessage = Field(..., alias='glanceMessage')
    high_value_message: HighValueMessage2 = Field(..., alias='highValueMessage')
    high_value_messages: list[None] = Field(..., alias='highValueMessages')
    informational_message: dict[str, Any] = Field(..., alias='informationalMessage')
    informational_messages: list[None] = Field(..., alias='informationalMessages')
    product_promotion_message: dict[str, Any] = Field(..., alias='productPromotionMessage')
    product_summary_message: dict[str, Any] = Field(..., alias='productSummaryMessage')
    provider_logo: ProviderLogo2 = Field(..., alias='providerLogo')
    title_metadata_badge: TitleMetadataBadge = Field(..., alias='titleMetadataBadge')

class Hero(BaseModel):
    model_config = ConfigDict(defer_build=True)
    url: str

class Poster2x3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    url: str

class Images46(BaseModel):
    model_config = ConfigDict(defer_build=True)
    hero: Hero | None = None
    poster2x3: Poster2x3 | None = None
    cover: Cover | None = None

class Endpoint5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    partial_url: str = Field(..., alias='partialURL')
    query: Query

class Action67(BaseModel):
    model_config = ConfigDict(defer_build=True)
    ajax_enabled: bool = Field(..., alias='ajaxEnabled')
    endpoint: Endpoint5
    format_code: str = Field(..., alias='formatCode')
    tag: str
    text: Text

class Item1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field__type: str = Field(..., alias='__type')
    action: Action67
    item_type: str = Field(..., alias='itemType')
    text: str

class OverflowMenu1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    items: list[Item1]
    title: str

class Endpoint6(BaseModel):
    model_config = ConfigDict(defer_build=True)
    partial_url: str = Field(..., alias='partialURL')
    query: Query

class WatchlistAction1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    ajax_enabled: bool = Field(..., alias='ajaxEnabled')
    endpoint: Endpoint6
    format_code: str = Field(..., alias='formatCode')
    tag: str
    text: Text

class Entity1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    buy_box_actions: list[None] = Field(..., alias='buyBoxActions')
    categorized_genres: CategorizedGenres | None = Field(None, alias='categorizedGenres')
    customer_reviews: CustomerReviews1 | None = Field(None, alias='customerReviews')
    degradations: list[None]
    display_title: str = Field(..., alias='displayTitle')
    entitlement_cues: EntitlementCues2 = Field(..., alias='entitlementCues')
    entity_type: str = Field(..., alias='entityType')
    hover_info: HoverInfo = Field(..., alias='hoverInfo')
    images: Images46
    impression_id: str = Field(..., alias='impressionId')
    is_closed_caption: bool = Field(..., alias='isClosedCaption')
    item_analytics: ItemAnalytics = Field(..., alias='itemAnalytics')
    link: Link
    maturity_rating_badge: MaturityRatingBadge = Field(..., alias='maturityRatingBadge')
    overflow_menu: OverflowMenu1 = Field(..., alias='overflowMenu')
    playback_actions: list[None] = Field(..., alias='playbackActions')
    ref_marker: str = Field(..., alias='refMarker')
    release_year: str = Field(..., alias='releaseYear')
    synopsis: str
    title: str
    title_id: str = Field(..., alias='titleID')
    watchlist_action: WatchlistAction1 = Field(..., alias='watchlistAction')
    widget_type: str = Field(..., alias='widgetType')
    runtime: str | None = None

class EntitlementCues3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    entitled_carousel: str = Field(..., alias='entitledCarousel')
    offer_type: str = Field(..., alias='offerType')

class B001T5BzaoItem(BaseModel):
    model_config = ConfigDict(defer_build=True)
    container_type: str = Field(..., alias='containerType')
    entities: list[Entity1]
    entitlement_cues: EntitlementCues3 = Field(..., alias='entitlementCues')
    estimated_total: int = Field(..., alias='estimatedTotal')
    impression_data: str = Field(..., alias='impressionData')
    inline_container_update_actions: list[None] = Field(..., alias='inlineContainerUpdateActions')
    is_continue_watching: bool = Field(..., alias='isContinueWatching')
    not_expandable: bool | None = Field(None, alias='notExpandable')
    strings: dict[str, Any]
    text: str
    title: str
    web_uid: str = Field(..., alias='webUid')
    journey_ingress_context: str | None = Field(None, alias='journeyIngressContext')
    pagination_service_token: str | None = Field(None, alias='paginationServiceToken')
    pagination_start_index: int | None = Field(None, alias='paginationStartIndex')
    pagination_target_id: str | None = Field(None, alias='paginationTargetId')

class CustomerReviews2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    count: int
    count_formatted: str = Field(..., alias='countFormatted')
    customer_reviews_text: CustomerReviewsText = Field(..., alias='customerReviewsText')
    link: str
    value: int | float

class HighValueMessage4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    message: str
    icon: str | None = None

class ProviderLogo3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    image_url: str | None = Field(None, alias='imageUrl')
    logo_scalar_horizontal: str | None = Field(None, alias='logoScalarHorizontal')
    message: str | None = None

class EntitlementCues4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    buybox_message: dict[str, Any] = Field(..., alias='buyboxMessage')
    compact_focus_message: dict[str, Any] = Field(..., alias='compactFocusMessage')
    content_source_logo: dict[str, Any] = Field(..., alias='contentSourceLogo')
    entitlement_type: str | None = Field(None, alias='entitlementType')
    focus_message: FocusMessage40 = Field(..., alias='focusMessage')
    glance_message: GlanceMessage = Field(..., alias='glanceMessage')
    high_value_message: HighValueMessage4 = Field(..., alias='highValueMessage')
    high_value_messages: list[None] = Field(..., alias='highValueMessages')
    informational_message: dict[str, Any] = Field(..., alias='informationalMessage')
    informational_messages: list[None] = Field(..., alias='informationalMessages')
    product_promotion_message: dict[str, Any] = Field(..., alias='productPromotionMessage')
    product_summary_message: dict[str, Any] = Field(..., alias='productSummaryMessage')
    provider_logo: ProviderLogo3 = Field(..., alias='providerLogo')
    title_metadata_badge: TitleMetadataBadge = Field(..., alias='titleMetadataBadge')

class Images47(BaseModel):
    model_config = ConfigDict(defer_build=True)
    cover: Cover

class Endpoint7(BaseModel):
    model_config = ConfigDict(defer_build=True)
    partial_url: str = Field(..., alias='partialURL')
    query: Query

class Action68(BaseModel):
    model_config = ConfigDict(defer_build=True)
    ajax_enabled: bool = Field(..., alias='ajaxEnabled')
    endpoint: Endpoint7
    format_code: str = Field(..., alias='formatCode')
    tag: str
    text: Text

class Item2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field__type: str = Field(..., alias='__type')
    action: Action68
    item_type: str = Field(..., alias='itemType')
    text: str

class OverflowMenu2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    items: list[Item2]
    title: str

class Endpoint8(BaseModel):
    model_config = ConfigDict(defer_build=True)
    partial_url: str = Field(..., alias='partialURL')
    query: Query

class WatchlistAction2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    ajax_enabled: bool = Field(..., alias='ajaxEnabled')
    endpoint: Endpoint8
    format_code: str = Field(..., alias='formatCode')
    tag: str
    text: Text

class Entity2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    buy_box_actions: list[None] = Field(..., alias='buyBoxActions')
    customer_reviews: CustomerReviews2 | None = Field(None, alias='customerReviews')
    degradations: list[None]
    display_title: str = Field(..., alias='displayTitle')
    entitlement_cues: EntitlementCues4 = Field(..., alias='entitlementCues')
    entity_type: str = Field(..., alias='entityType')
    hover_info: HoverInfo = Field(..., alias='hoverInfo')
    images: Images47
    impression_id: str = Field(..., alias='impressionId')
    is_closed_caption: bool = Field(..., alias='isClosedCaption')
    item_analytics: ItemAnalytics = Field(..., alias='itemAnalytics')
    link: Link
    maturity_rating_badge: MaturityRatingBadge = Field(..., alias='maturityRatingBadge')
    overflow_menu: OverflowMenu2 = Field(..., alias='overflowMenu')
    playback_actions: list[None] = Field(..., alias='playbackActions')
    ref_marker: str = Field(..., alias='refMarker')
    release_year: str = Field(..., alias='releaseYear')
    runtime: str | None = None
    synopsis: str
    title: str
    title_id: str = Field(..., alias='titleID')
    watchlist_action: WatchlistAction2 = Field(..., alias='watchlistAction')
    widget_type: str = Field(..., alias='widgetType')

class EntitlementCues5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    entitled_carousel: str = Field(..., alias='entitledCarousel')
    offer_type: str = Field(..., alias='offerType')

class B0Chf9MzxzItem1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    container_type: str = Field(..., alias='containerType')
    entities: list[Entity2]
    entitlement_cues: EntitlementCues5 = Field(..., alias='entitlementCues')
    estimated_total: int = Field(..., alias='estimatedTotal')
    impression_data: str = Field(..., alias='impressionData')
    inline_container_update_actions: list[None] = Field(..., alias='inlineContainerUpdateActions')
    is_continue_watching: bool = Field(..., alias='isContinueWatching')
    journey_ingress_context: str = Field(..., alias='journeyIngressContext')
    pagination_service_token: str = Field(..., alias='paginationServiceToken')
    pagination_start_index: int = Field(..., alias='paginationStartIndex')
    pagination_target_id: str = Field(..., alias='paginationTargetId')
    strings: dict[str, Any]
    text: str
    title: str
    web_uid: str = Field(..., alias='webUid')

class Containers(BaseModel):
    model_config = ConfigDict(defer_build=True)
    b005_c8_db7_e: list[B005C8Db7EItem1] | None = Field(None, alias='B005C8DB7E')
    b001_t5_bzao: list[B001T5BzaoItem] | None = Field(None, alias='B001T5BZAO')
    b0_chf9_mzxz: list[B0Chf9MzxzItem1] | None = Field(None, alias='B0CHF9MZXZ')

class Action69(BaseModel):
    model_config = ConfigDict(defer_build=True)
    format: str
    link: str
    text: Text
    title_id: str = Field(..., alias='titleID')

class B001T5Bzao11(BaseModel):
    model_config = ConfigDict(defer_build=True)
    actions: list[Action69]

class OtherFormats(BaseModel):
    model_config = ConfigDict(defer_build=True)
    b001_t5_bzao: B001T5Bzao11 | None = Field(None, alias='B001T5BZAO')

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

class B005C8Db7E10(BaseModel):
    model_config = ConfigDict(defer_build=True)
    content_descriptors: list[None] = Field(..., alias='contentDescriptors')
    content_warnings: list[str] = Field(..., alias='contentWarnings')
    maturity_rating: MaturityRating2 = Field(..., alias='maturityRating')

class B005C8Dbii4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    maturity_rating: MaturityRating2 = Field(..., alias='maturityRating')
    traits: list[None]

class B005C8E5383(BaseModel):
    model_config = ConfigDict(defer_build=True)
    maturity_rating: MaturityRating2 = Field(..., alias='maturityRating')
    traits: list[None]

class B005C8E70Y3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    maturity_rating: MaturityRating2 = Field(..., alias='maturityRating')
    traits: list[None]

class B005G0R6Xi3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    maturity_rating: MaturityRating2 = Field(..., alias='maturityRating')
    traits: list[None]

class B005C8Egx23(BaseModel):
    model_config = ConfigDict(defer_build=True)
    maturity_rating: MaturityRating2 = Field(..., alias='maturityRating')
    traits: list[None]

class B005C8Ei623(BaseModel):
    model_config = ConfigDict(defer_build=True)
    maturity_rating: MaturityRating2 = Field(..., alias='maturityRating')
    traits: list[None]

class B005C8Ec7M3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    maturity_rating: MaturityRating2 = Field(..., alias='maturityRating')
    traits: list[None]

class B005C8Egeg3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    maturity_rating: MaturityRating2 = Field(..., alias='maturityRating')
    traits: list[None]

class B005C8Elci3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    maturity_rating: MaturityRating2 = Field(..., alias='maturityRating')
    traits: list[None]

class B005C8Ed303(BaseModel):
    model_config = ConfigDict(defer_build=True)
    maturity_rating: MaturityRating2 = Field(..., alias='maturityRating')
    traits: list[None]

class B005C8Dike3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    maturity_rating: MaturityRating2 = Field(..., alias='maturityRating')
    traits: list[None]

class B005C8Ecls3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    maturity_rating: MaturityRating2 = Field(..., alias='maturityRating')
    traits: list[None]

class B005C8Dtto3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    maturity_rating: MaturityRating2 = Field(..., alias='maturityRating')
    traits: list[None]

class B005C8E91Q3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    maturity_rating: MaturityRating2 = Field(..., alias='maturityRating')
    traits: list[None]

class B005C8Dkvg3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    maturity_rating: MaturityRating2 = Field(..., alias='maturityRating')
    traits: list[None]

class B005C8Ei5S3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    maturity_rating: MaturityRating2 = Field(..., alias='maturityRating')
    traits: list[None]

class B005C8Eiui3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    maturity_rating: MaturityRating2 = Field(..., alias='maturityRating')
    traits: list[None]

class B005C8Emmm3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    maturity_rating: MaturityRating2 = Field(..., alias='maturityRating')
    traits: list[None]

class B005C8Eh2W3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    maturity_rating: MaturityRating2 = Field(..., alias='maturityRating')
    traits: list[None]

class B005C8Ebws3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    maturity_rating: MaturityRating2 = Field(..., alias='maturityRating')
    traits: list[None]

class B005C8Ds0Y3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    maturity_rating: MaturityRating2 = Field(..., alias='maturityRating')
    traits: list[None]

class B005C8E5A63(BaseModel):
    model_config = ConfigDict(defer_build=True)
    maturity_rating: MaturityRating2 = Field(..., alias='maturityRating')
    traits: list[None]

class B005C8Ef8I3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    maturity_rating: MaturityRating2 = Field(..., alias='maturityRating')
    traits: list[None]

class B005C8Ek9M3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    maturity_rating: MaturityRating2 = Field(..., alias='maturityRating')
    traits: list[None]

class MaturityRating28(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field__type: str = Field(..., alias='__type')
    country_code: str = Field(..., alias='countryCode')
    description: str
    display_text: str = Field(..., alias='displayText')
    id: str

class B001T5Bzao12(BaseModel):
    model_config = ConfigDict(defer_build=True)
    content_descriptors: list[None] = Field(..., alias='contentDescriptors')
    content_warnings: list[str] = Field(..., alias='contentWarnings')
    maturity_rating: MaturityRating28 = Field(..., alias='maturityRating')

class MaturityRating29(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field__type: str = Field(..., alias='__type')
    description: str
    display_text: str = Field(..., alias='displayText')
    id: str

class B0Chf9Mzxz10(BaseModel):
    model_config = ConfigDict(defer_build=True)
    content_descriptors: list[str] = Field(..., alias='contentDescriptors')
    content_warnings: list[str] = Field(..., alias='contentWarnings')
    maturity_rating: MaturityRating29 = Field(..., alias='maturityRating')

class B0Cjp8Rbmq4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    maturity_rating: MaturityRating29 = Field(..., alias='maturityRating')
    traits: list[None]

class B0Ck832Gg53(BaseModel):
    model_config = ConfigDict(defer_build=True)
    maturity_rating: MaturityRating29 = Field(..., alias='maturityRating')
    traits: list[None]

class B0Chsjdg3Y3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    maturity_rating: MaturityRating29 = Field(..., alias='maturityRating')
    traits: list[None]

class B0Cgpsngts3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    maturity_rating: MaturityRating29 = Field(..., alias='maturityRating')
    traits: list[None]

class B0Chjln6Gs3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    maturity_rating: MaturityRating29 = Field(..., alias='maturityRating')
    traits: list[None]

class B0Chpmk42L3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    maturity_rating: MaturityRating29 = Field(..., alias='maturityRating')
    traits: list[None]

class B0Cjcmt4Xn3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    maturity_rating: MaturityRating29 = Field(..., alias='maturityRating')
    traits: list[None]

class B0Cgx6W4Gk3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    maturity_rating: MaturityRating29 = Field(..., alias='maturityRating')
    traits: list[None]

class B0Ch4Tmyh23(BaseModel):
    model_config = ConfigDict(defer_build=True)
    maturity_rating: MaturityRating29 = Field(..., alias='maturityRating')
    traits: list[None]

class B0Cjqd32Q63(BaseModel):
    model_config = ConfigDict(defer_build=True)
    maturity_rating: MaturityRating29 = Field(..., alias='maturityRating')
    traits: list[None]

class B0Cj658T6K3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    maturity_rating: MaturityRating29 = Field(..., alias='maturityRating')
    traits: list[None]

class B0Cjq1Pt9T3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    maturity_rating: MaturityRating29 = Field(..., alias='maturityRating')
    traits: list[None]

class Metadata2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    b005_c8_db7_e: B005C8Db7E10 | None = Field(None, alias='B005C8DB7E')
    b005_c8_dbii: B005C8Dbii4 | None = Field(None, alias='B005C8DBII')
    b005_c8_e538: B005C8E5383 | None = Field(None, alias='B005C8E538')
    b005_c8_e70_y: B005C8E70Y3 | None = Field(None, alias='B005C8E70Y')
    b005_g0_r6_xi: B005G0R6Xi3 | None = Field(None, alias='B005G0R6XI')
    b005_c8_egx2: B005C8Egx23 | None = Field(None, alias='B005C8EGX2')
    b005_c8_ei62: B005C8Ei623 | None = Field(None, alias='B005C8EI62')
    b005_c8_ec7_m: B005C8Ec7M3 | None = Field(None, alias='B005C8EC7M')
    b005_c8_egeg: B005C8Egeg3 | None = Field(None, alias='B005C8EGEG')
    b005_c8_elci: B005C8Elci3 | None = Field(None, alias='B005C8ELCI')
    b005_c8_ed30: B005C8Ed303 | None = Field(None, alias='B005C8ED30')
    b005_c8_dike: B005C8Dike3 | None = Field(None, alias='B005C8DIKE')
    b005_c8_ecls: B005C8Ecls3 | None = Field(None, alias='B005C8ECLS')
    b005_c8_dtto: B005C8Dtto3 | None = Field(None, alias='B005C8DTTO')
    b005_c8_e91_q: B005C8E91Q3 | None = Field(None, alias='B005C8E91Q')
    b005_c8_dkvg: B005C8Dkvg3 | None = Field(None, alias='B005C8DKVG')
    b005_c8_ei5_s: B005C8Ei5S3 | None = Field(None, alias='B005C8EI5S')
    b005_c8_eiui: B005C8Eiui3 | None = Field(None, alias='B005C8EIUI')
    b005_c8_emmm: B005C8Emmm3 | None = Field(None, alias='B005C8EMMM')
    b005_c8_eh2_w: B005C8Eh2W3 | None = Field(None, alias='B005C8EH2W')
    b005_c8_ebws: B005C8Ebws3 | None = Field(None, alias='B005C8EBWS')
    b005_c8_ds0_y: B005C8Ds0Y3 | None = Field(None, alias='B005C8DS0Y')
    b005_c8_e5_a6: B005C8E5A63 | None = Field(None, alias='B005C8E5A6')
    b005_c8_ef8_i: B005C8Ef8I3 | None = Field(None, alias='B005C8EF8I')
    b005_c8_ek9_m: B005C8Ek9M3 | None = Field(None, alias='B005C8EK9M')
    b001_t5_bzao: B001T5Bzao12 | None = Field(None, alias='B001T5BZAO')
    b0_chf9_mzxz: B0Chf9Mzxz10 | None = Field(None, alias='B0CHF9MZXZ')
    b0_cjp8_rbmq: B0Cjp8Rbmq4 | None = Field(None, alias='B0CJP8RBMQ')
    b0_ck832_gg5: B0Ck832Gg53 | None = Field(None, alias='B0CK832GG5')
    b0_chsjdg3_y: B0Chsjdg3Y3 | None = Field(None, alias='B0CHSJDG3Y')
    b0_cgpsngts: B0Cgpsngts3 | None = Field(None, alias='B0CGPSNGTS')
    b0_chjln6_gs: B0Chjln6Gs3 | None = Field(None, alias='B0CHJLN6GS')
    b0_chpmk42_l: B0Chpmk42L3 | None = Field(None, alias='B0CHPMK42L')
    b0_cjcmt4_xn: B0Cjcmt4Xn3 | None = Field(None, alias='B0CJCMT4XN')
    b0_cgx6_w4_gk: B0Cgx6W4Gk3 | None = Field(None, alias='B0CGX6W4GK')
    b0_ch4_tmyh2: B0Ch4Tmyh23 | None = Field(None, alias='B0CH4TMYH2')
    b0_cjqd32_q6: B0Cjqd32Q63 | None = Field(None, alias='B0CJQD32Q6')
    b0_cj658_t6_k: B0Cj658T6K3 | None = Field(None, alias='B0CJ658T6K')
    b0_cjq1_pt9_t: B0Cjq1Pt9T3 | None = Field(None, alias='B0CJQ1PT9T')

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
    action: Action5
    refund: Refund
    imdb: dict[str, Any]
    buy_box: dict[str, Any] = Field(..., alias='buyBox')
    buybox_title_id: dict[str, Any] = Field(..., alias='buyboxTitleId')
    creative: dict[str, Any]
    banner: Banner26
    age_verification_banner: dict[str, Any] = Field(..., alias='ageVerificationBanner')
    notification: dict[str, Any]
    seasons: dict[str, Any]
    self: Self1
    watchlist: dict[str, Any]
    restriction: dict[str, Any]
    extras: dict[str, Any]
    tokens: dict[str, Any]
    page_link: dict[str, Any] = Field(..., alias='pageLink')
    episode_list: EpisodeList = Field(..., alias='episodeList')
    containers: Containers
    recordings: dict[str, Any]
    bundles_content: dict[str, Any] = Field(..., alias='bundlesContent')
    other_formats: OtherFormats = Field(..., alias='otherFormats')
    page_context: PageContext1 = Field(..., alias='pageContext')
    autoplay_hero: dict[str, Any] = Field(..., alias='autoplayHero')
    autoplay_trailer_hero: dict[str, Any] = Field(..., alias='autoplayTrailerHero')
    playback_integration: dict[str, Any] = Field(..., alias='playbackIntegration')
    coming_soon: dict[str, Any] = Field(..., alias='comingSoon')
    metadata: Metadata2
    widgets: Widgets
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

class Query9(BaseModel):
    model_config = ConfigDict(defer_build=True)
    ie: str
    ref_: str

class SubmitSearchDestructuredEndpoint(BaseModel):
    model_config = ConfigDict(defer_build=True)
    partial_url: str = Field(..., alias='partialURL')
    query: Query9

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
