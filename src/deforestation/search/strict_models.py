from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import ConfigDict
from datetime import timedelta
from ipaddress import IPv4Address
from typing import Any
from pydantic import BaseModel, Field

class PageMetadata(BaseModel):
    model_config = ConfigDict(defer_build=True)
    page_type: str = Field(..., alias='pageType')
    sub_page_type: str = Field(..., alias='subPageType')

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
    page_metadata: PageMetadata = Field(..., alias='pageMetadata')
    sitewide_head: SitewideHead = Field(..., alias='sitewideHead')
    title: str

class FocusMessage(BaseModel):
    model_config = ConfigDict(defer_build=True)
    icon: str | None = None
    message: str

class GlanceMessage(BaseModel):
    model_config = ConfigDict(defer_build=True)
    icon: str | None = None
    message: str

class HighValueMessage(BaseModel):
    model_config = ConfigDict(defer_build=True)
    message: str
    icon: str | None = None

class ProviderLogo(BaseModel):
    model_config = ConfigDict(defer_build=True)
    image_url: str | None = Field(None, alias='imageUrl')
    message: str | None = None
    logo_scalar_horizontal: str | None = Field(None, alias='logoScalarHorizontal')

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
    focus_message: FocusMessage = Field(..., alias='focusMessage')
    glance_message: GlanceMessage = Field(..., alias='glanceMessage')
    high_value_message: HighValueMessage = Field(..., alias='highValueMessage')
    high_value_messages: list[None] = Field(..., alias='highValueMessages')
    informational_message: dict[str, Any] = Field(..., alias='informationalMessage')
    informational_messages: list[None] = Field(..., alias='informationalMessages')
    product_promotion_message: dict[str, Any] = Field(..., alias='productPromotionMessage')
    product_summary_message: dict[str, Any] = Field(..., alias='productSummaryMessage')
    provider_logo: ProviderLogo = Field(..., alias='providerLogo')
    title_metadata_badge: TitleMetadataBadge = Field(..., alias='titleMetadataBadge')

class HoverInfo(BaseModel):
    model_config = ConfigDict(defer_build=True)
    can_hover: bool = Field(..., alias='canHover')

class Cover(BaseModel):
    model_config = ConfigDict(defer_build=True)
    url: str

class Images(BaseModel):
    model_config = ConfigDict(defer_build=True)
    cover: Cover

class ItemAnalytics(BaseModel):
    model_config = ConfigDict(defer_build=True)
    is_prime_customer: str = Field(..., alias='isPrimeCustomer')
    page_type_id_source: str | None = Field(None, alias='pageTypeIdSource')
    ref_marker: str = Field(..., alias='refMarker')
    page_type_id: str | None = Field(None, alias='pageTypeId')
    a9_search_fields: str = Field(..., alias='A9SearchFields')
    pvs3: str | None = None

class Link(BaseModel):
    model_config = ConfigDict(defer_build=True)
    analytics: dict[str, Any]
    metadata: dict[str, Any]
    url: str

class LiveInfo(BaseModel):
    model_config = ConfigDict(defer_build=True)
    status: str
    time_badge: str = Field(..., alias='timeBadge')
    venue: str | None = None

class MaturityRatingBadge(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field__type: str = Field(..., alias='__type')
    description: str
    display_text: str = Field(..., alias='displayText')
    id: str
    country_code: str | None = Field(None, alias='countryCode')

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

class Action(BaseModel):
    model_config = ConfigDict(defer_build=True)
    ajax_enabled: bool = Field(..., alias='ajaxEnabled')
    endpoint: Endpoint
    format_code: str = Field(..., alias='formatCode')
    tag: str
    text: Text

class Item(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field__type: str = Field(..., alias='__type')
    action: Action
    item_type: str = Field(..., alias='itemType')
    text: str

class OverflowMenu(BaseModel):
    model_config = ConfigDict(defer_build=True)
    items: list[Item]
    title: str

class Endpoint1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    partial_url: str = Field(..., alias='partialURL')
    query: Query

class WatchlistAction(BaseModel):
    model_config = ConfigDict(defer_build=True)
    ajax_enabled: bool = Field(..., alias='ajaxEnabled')
    endpoint: Endpoint1
    format_code: str = Field(..., alias='formatCode')
    tag: str
    text: Text

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

class Entity(BaseModel):
    model_config = ConfigDict(defer_build=True)
    buy_box_actions: list[None] = Field(..., alias='buyBoxActions')
    degradations: list[None]
    display_title: str = Field(..., alias='displayTitle')
    entitlement_cues: EntitlementCues = Field(..., alias='entitlementCues')
    entity_type: str = Field(..., alias='entityType')
    hover_info: HoverInfo = Field(..., alias='hoverInfo')
    images: Images
    impression_id: str = Field(..., alias='impressionId')
    is_closed_caption: bool = Field(..., alias='isClosedCaption')
    item_analytics: ItemAnalytics = Field(..., alias='itemAnalytics')
    link: Link
    live_info: LiveInfo | None = Field(None, alias='liveInfo')
    maturity_rating_badge: MaturityRatingBadge | None = Field(None, alias='maturityRatingBadge')
    overflow_menu: OverflowMenu = Field(..., alias='overflowMenu')
    playback_actions: list[None] = Field(..., alias='playbackActions')
    ref_marker: str = Field(..., alias='refMarker')
    synopsis: str
    title: str
    title_id: str = Field(..., alias='titleID')
    watchlist_action: WatchlistAction = Field(..., alias='watchlistAction')
    widget_type: str = Field(..., alias='widgetType')
    release_year: str | None = Field(None, alias='releaseYear')
    runtime: str | None = None
    customer_reviews: CustomerReviews | None = Field(None, alias='customerReviews')

class EntitlementCues1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    entitled_carousel: str = Field(..., alias='entitledCarousel')
    offer_type: str = Field(..., alias='offerType')

class Action1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    analytics: dict[str, Any]
    label: str
    metadata: dict[str, Any]
    target: str
    url: str

class Badge(BaseModel):
    model_config = ConfigDict(defer_build=True)
    badge_text: str = Field(..., alias='badgeText')
    badge_type: str = Field(..., alias='badgeType')

class Container(BaseModel):
    model_config = ConfigDict(defer_build=True)
    container_type: str = Field(..., alias='containerType')
    entities: list[Entity]
    entitlement_cues: EntitlementCues1 | None = Field(None, alias='entitlementCues')
    estimated_total: int | None = Field(None, alias='estimatedTotal')
    impression_data: str | None = Field(None, alias='impressionData')
    inline_container_update_actions: list[None] = Field(..., alias='inlineContainerUpdateActions')
    is_continue_watching: bool = Field(..., alias='isContinueWatching')
    strings: dict[str, Any]
    text: str | None = None
    title: str
    web_uid: timedelta | str = Field(..., alias='webUid', union_mode='left_to_right')
    action: Action1 | None = None
    badges: list[Badge] | None = None

class FeatureSwitches(BaseModel):
    model_config = ConfigDict(defer_build=True)
    use_post_for_enrichment: bool = Field(..., alias='usePostForEnrichment')
    disable_win_app_max_containers_limit: bool = Field(..., alias='disableWinAppMaxContainersLimit')
    is_pagination_limited_on_m_shop: bool = Field(..., alias='isPaginationLimitedOnMShop')
    no_index_paramount_parent_id_pages: bool = Field(..., alias='noIndexParamountParentIdPages')
    disable_hover: bool = Field(..., alias='disableHover')
    should_always_show_maturity_rating: bool = Field(..., alias='shouldAlwaysShowMaturityRating')
    is_mobile_web_streaming_enabled: bool = Field(..., alias='isMobileWebStreamingEnabled')
    is_hover_ssm_on: bool = Field(..., alias='isHoverSsmOn')
    disable_enrich_item_metadata: bool = Field(..., alias='disableEnrichItemMetadata')
    disable_storefront_tvod_checkout: bool = Field(..., alias='disableStorefrontTvodCheckout')

class Availability(BaseModel):
    model_config = ConfigDict(defer_build=True)
    description: str
    severity: str

class Metadata(BaseModel):
    model_config = ConfigDict(defer_build=True)
    availability: Availability

class PageMetadata1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    hide_page_title: bool = Field(..., alias='hidePageTitle')
    should_generate_json_ld: bool = Field(..., alias='shouldGenerateJsonLD')

class Strings(BaseModel):
    model_config = ConfigDict(defer_build=True)
    dv_web_aria_label_filter_item: str = Field(..., alias='DV_WEB_ARIA_LABEL_FILTER_ITEM')
    dv_web_aria_previous_title: str = Field(..., alias='DV_WEB_ARIA_PREVIOUS_TITLE')
    dv_web_pwa_first_launch_modal_learn_more: str = Field(..., alias='DV_WEB_PWA_First_LAUNCH_MODAL_LEARN_MORE')
    dv_web_watchlist_tooltip: str = Field(..., alias='DV_WEB_WATCHLIST_TOOLTIP')
    dv_comma_separator: str = Field(..., alias='DV_comma_separator')
    dv_web_sports_record_success_upcoming: str = Field(..., alias='DV_WEB_SPORTS_RECORD_SUCCESS_UPCOMING')
    dv_web_sports_record_success_ended: str = Field(..., alias='DV_WEB_SPORTS_RECORD_SUCCESS_ENDED')
    dv_web_pv_api_link_fallback_failure_retry_link: str = Field(..., alias='DV_WEB_PV_API_LINK_FALLBACK_FAILURE_RETRY_LINK')
    dv_web_sports_record_league_success_ended: str = Field(..., alias='DV_WEB_SPORTS_RECORD_LEAGUE_SUCCESS_ENDED')
    dv_web_watchlist_add: str = Field(..., alias='DV_WEB_WATCHLIST_ADD')
    dv_web_linear_program_record_start_success: str = Field(..., alias='DV_WEB_LINEAR_PROGRAM_RECORD_START_SUCCESS')
    dv_web_epg_card_on_now: str = Field(..., alias='DV_WEB_EPG_CARD_ON_NOW')
    dv_web_recording_scheduled: str = Field(..., alias='DV_WEB_RECORDING_SCHEDULED')
    dv_web_pwa_first_launch_modal_sign_in_now: str = Field(..., alias='DV_WEB_PWA_First_LAUNCH_MODAL_SIGN_IN_NOW')
    dv_web_aria_more_details: str = Field(..., alias='DV_WEB_ARIA_MORE_DETAILS')
    dv_dp_aria_release_year: str = Field(..., alias='DV_DP_ARIA_release_year')
    dv_web_recording_now: str = Field(..., alias='DV_WEB_RECORDING_NOW')
    dv_web_added_to_favorites: str = Field(..., alias='DV_WEB_ADDED_TO_FAVORITES')
    dv_web_sports_cancel_record_league_success: str = Field(..., alias='DV_WEB_SPORTS_CANCEL_RECORD_LEAGUE_SUCCESS')
    dv_dp_tr_liked_aria: str = Field(..., alias='DV_DP_TR_liked_aria')
    dv_web_aria_next_n_titles: str = Field(..., alias='DV_WEB_ARIA_NEXT_N_TITLES')
    dv_web_pv_api_link_fallback_failure_title: str = Field(..., alias='DV_WEB_PV_API_LINK_FALLBACK_FAILURE_TITLE')
    dv_web_aria_current_title_index: str = Field(..., alias='DV_WEB_ARIA_CURRENT_TITLE_INDEX')
    dv_web_favorites_filter_fallback_heading: str = Field(..., alias='DV_WEB_FAVORITES_FILTER_FALLBACK_HEADING')
    dv_web_linear_program_cancel_record_tooltip: str = Field(..., alias='DV_WEB_LINEAR_PROGRAM_CANCEL_RECORD_TOOLTIP')
    dv_web_more_details: str = Field(..., alias='DV_WEB_MORE_DETAILS')
    dv_web_linear_program_record_error: str = Field(..., alias='DV_WEB_LINEAR_PROGRAM_RECORD_ERROR')
    dv_web_aria_previous_title_index: str = Field(..., alias='DV_WEB_ARIA_PREVIOUS_TITLE_INDEX')
    dv_web_aria_previous_n_titles: str = Field(..., alias='DV_WEB_ARIA_PREVIOUS_N_TITLES')
    dv_web_removed_from_favorites: str = Field(..., alias='DV_WEB_REMOVED_FROM_FAVORITES')
    dv_web_overflow_menu_tooltip: str = Field(..., alias='DV_WEB_OVERFLOW_MENU_TOOLTIP')
    av_lrc_start_over: str = Field(..., alias='AV_LRC_START_OVER')
    dv_web_sports_record_league: str = Field(..., alias='DV_WEB_SPORTS_RECORD_LEAGUE')
    dv_web_draper_player_mute_button: str = Field(..., alias='DV_WEB_DRAPER_PLAYER_MUTE_BUTTON')
    dv_web_add_to_favorites: str = Field(..., alias='DV_WEB_ADD_TO_FAVORITES')
    dv_web_favorites_filter_fallback_body: str = Field(..., alias='DV_WEB_FAVORITES_FILTER_FALLBACK_BODY')
    dv_web_draper_player_unmute_button: str = Field(..., alias='DV_WEB_DRAPER_PLAYER_UNMUTE_BUTTON')
    dv_dp_tr_dislike_btn: str = Field(..., alias='DV_DP_TR_dislike_btn')
    dv_web_pwa_post_auth_modal_go_to_downloads: str = Field(..., alias='DV_WEB_PWA_POST_AUTH_MODAL_GO_TO_DOWNLOADS')
    dv_web_sports_cancel_record_success: str = Field(..., alias='DV_WEB_SPORTS_CANCEL_RECORD_SUCCESS')
    dv_web_pv_api_link_fallback_failure_message: str = Field(..., alias='DV_WEB_PV_API_LINK_FALLBACK_FAILURE_MESSAGE')
    dv_web_watchlist_csrf_problem: str = Field(..., alias='DV_WEB_WATCHLIST_CSRF_PROBLEM')
    dv_web_pwa_first_launch_modal_content: str = Field(..., alias='DV_WEB_PWA_First_LAUNCH_MODAL_CONTENT')
    dv_web_pwa_post_auth_modal_content: str = Field(..., alias='DV_WEB_PWA_POST_AUTH_MODAL_CONTENT')
    dv_web_undo_like: str = Field(..., alias='DV_WEB_Undo_like')
    dv_web_pv_api_link_fallback_success_message: str = Field(..., alias='DV_WEB_PV_API_LINK_FALLBACK_SUCCESS_MESSAGE')
    dv_web_details_tooltip: str = Field(..., alias='DV_WEB_DETAILS_TOOLTIP')
    dv_web_undo_remove_from_container: str = Field(..., alias='DV_WEB_UNDO_REMOVE_FROM_CONTAINER')
    dv_web_sports_record: str = Field(..., alias='DV_WEB_SPORTS_RECORD')
    dv_web_pwa_first_launch_modal_heading: str = Field(..., alias='DV_WEB_PWA_First_LAUNCH_MODAL_HEADING')
    dv_web_watchlist_remove: str = Field(..., alias='DV_WEB_WATCHLIST_REMOVE')
    dv_web_pwa_post_auth_modal_start_watching: str = Field(..., alias='DV_WEB_PWA_POST_AUTH_MODAL_START_WATCHING')
    dv_dp_tr_like_btn: str = Field(..., alias='DV_DP_TR_like_btn')
    dv_web_channel_name_logo_label: str = Field(..., alias='DV_WEB_CHANNEL_NAME_LOGO_LABEL')
    dv_web_remove_from_favorites: str = Field(..., alias='DV_WEB_REMOVE_FROM_FAVORITES')
    dv_web_sports_cancel_record_league: str = Field(..., alias='DV_WEB_SPORTS_CANCEL_RECORD_LEAGUE')
    dv_web_recording_indicator: str = Field(..., alias='DV_WEB_RECORDING_INDICATOR')
    dv_web_linear_program_record_cancel_success: str = Field(..., alias='DV_WEB_LINEAR_PROGRAM_RECORD_CANCEL_SUCCESS')
    dv_web_linear_program_record_tooltip: str = Field(..., alias='DV_WEB_LINEAR_PROGRAM_RECORD_TOOLTIP')
    dv_web_sports_recording_aria: str = Field(..., alias='DV_WEB_SPORTS_RECORDING_ARIA')
    dv_dp_aria_regulatory_rating: str = Field(..., alias='DV_DP_ARIA_regulatory_rating')
    dv_web_pwa_post_auth_modal_heading: str = Field(..., alias='DV_WEB_PWA_POST_AUTH_MODAL_HEADING')
    dv_web_linear_program_start_over_tooltip: str = Field(..., alias='DV_WEB_LINEAR_PROGRAM_START_OVER_TOOLTIP')
    dv_web_sports_record_league_success_upcoming: str = Field(..., alias='DV_WEB_SPORTS_RECORD_LEAGUE_SUCCESS_UPCOMING')
    dv_dp_tr_dislike_aria: str = Field(..., alias='DV_DP_TR_dislike_aria')
    dv_dp_aria_runtime: str = Field(..., alias='DV_DP_ARIA_runtime')
    dv_web_aria_next_title: str = Field(..., alias='DV_WEB_ARIA_NEXT_TITLE')
    dv_web_aria_next_title_index: str = Field(..., alias='DV_WEB_ARIA_NEXT_TITLE_INDEX')
    dv_dp_tr_like_aria: str = Field(..., alias='DV_DP_TR_like_aria')
    dv_web_watch_live: str = Field(..., alias='DV_WEB_WATCH_LIVE')
    dv_web_sports_cancel_record: str = Field(..., alias='DV_WEB_SPORTS_CANCEL_RECORD')
    dv_dp_tr_disliked_aria: str = Field(..., alias='DV_DP_TR_disliked_aria')

class SwiftPageParameters(BaseModel):
    model_config = ConfigDict(defer_build=True)
    page_id: str = Field(..., alias='pageId')
    page_type: str = Field(..., alias='pageType')

class RequestFeatureSwitches(BaseModel):
    model_config = ConfigDict(defer_build=True)
    horizontal_pagination: bool = Field(..., alias='HorizontalPagination')

class CustomerState(BaseModel):
    model_config = ConfigDict(defer_build=True)
    is_robotic: bool = Field(..., alias='isRobotic')

class FeatureSwitches1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    show_floating_join_prime_button: bool = Field(..., alias='showFloatingJoinPrimeButton')

class Metadata1(BaseModel):
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

class Query2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    ie: str
    ref_: str

class SubmitSearchDestructuredEndpoint(BaseModel):
    model_config = ConfigDict(defer_build=True)
    partial_url: str = Field(..., alias='partialURL')
    query: Query2

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
    feature_switches: FeatureSwitches1 = Field(..., alias='featureSwitches')
    is_sticky: bool = Field(..., alias='isSticky')
    metadata: Metadata1
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

class Metadata2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    availability: Availability

class SitewideConditional(BaseModel):
    model_config = ConfigDict(defer_build=True)
    degradations: list[None]
    features: dict[str, Any]
    metadata: Metadata2
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
    containers: list[Container]
    feature_switches: FeatureSwitches = Field(..., alias='featureSwitches')
    has_failed: bool = Field(..., alias='hasFailed')
    is_trailer_autoplay_enabled: bool = Field(..., alias='isTrailerAutoplayEnabled')
    metadata: Metadata
    page_metadata: PageMetadata1 = Field(..., alias='pageMetadata')
    phrase: str
    playback_launch_type: str = Field(..., alias='playbackLaunchType')
    strings: Strings
    swift_page_parameters: SwiftPageParameters = Field(..., alias='swiftPageParameters')
    hz_page_type: str = Field(..., alias='hzPageType')
    hz_sub_page_type: str = Field(..., alias='hzSubPageType')
    home_region: str = Field(..., alias='homeRegion')
    request_feature_switches: RequestFeatureSwitches = Field(..., alias='requestFeatureSwitches')
    enable_vertical_performant_render: bool = Field(..., alias='enableVerticalPerformantRender')
    sitewide: Sitewide

class QueryParameters(BaseModel):
    model_config = ConfigDict(defer_build=True)
    phrase: list[str]
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
    page_type_id: None = Field(..., alias='pageTypeId')
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
    dv_web_tr_persist_1434722: bool = Field(..., alias='DV_WEB_TR_PERSIST_1434722')
    dv_web_linear_station_taps_view_upgrade_1358041: bool = Field(..., alias='DV_WEB_LINEAR_STATION_TAPS_VIEW_UPGRADE_1358041')
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
    telemetry_client_launch_web_treatment: str = Field(..., alias='telemetryClientLaunchWebTreatment')
    is_runway_post_transition_enabled: bool = Field(..., alias='isRunwayPostTransitionEnabled')
    dv_web_dp_enable_whisper_cache_for_unrec_customers_1440503: bool = Field(..., alias='DV_WEB_DP_ENABLE_WHISPER_CACHE_FOR_UNREC_CUSTOMERS_1440503')
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

class SearchModel(BaseModel):
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
