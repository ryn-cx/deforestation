from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from datetime import timedelta
from ipaddress import IPv4Address
from typing import Any
from pydantic import BaseModel, ConfigDict, Field

class PageMetadata(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    page_type: str | None = Field(None, alias='pageType')
    sub_page_type: str | None = Field(None, alias='subPageType')

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
    page_metadata: PageMetadata | None = Field(None, alias='pageMetadata')
    sitewide_head: SitewideHead | None = Field(None, alias='sitewideHead')
    title: str | None = None

class FocusMessage(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    icon: str | None = None
    message: str | None = None

class GlanceMessage(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    icon: str | None = None
    message: str | None = None

class HighValueMessage(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    message: str | None = None
    icon: str | None = None

class ProviderLogo(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    image_url: str | None = Field(None, alias='imageUrl')
    message: str | None = None
    logo_scalar_horizontal: str | None = Field(None, alias='logoScalarHorizontal')

class TitleMetadataBadge(BaseModel):
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
    focus_message: FocusMessage | None = Field(None, alias='focusMessage')
    glance_message: GlanceMessage | None = Field(None, alias='glanceMessage')
    high_value_message: HighValueMessage | None = Field(None, alias='highValueMessage')
    high_value_messages: list[Any] | None = Field(None, alias='highValueMessages')
    informational_message: dict[str, Any] | None = Field(None, alias='informationalMessage')
    informational_messages: list[Any] | None = Field(None, alias='informationalMessages')
    product_promotion_message: dict[str, Any] | None = Field(None, alias='productPromotionMessage')
    product_summary_message: dict[str, Any] | None = Field(None, alias='productSummaryMessage')
    provider_logo: ProviderLogo | None = Field(None, alias='providerLogo')
    title_metadata_badge: TitleMetadataBadge | None = Field(None, alias='titleMetadataBadge')

class HoverInfo(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    can_hover: bool | None = Field(None, alias='canHover')

class Cover(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | None = None

class Images(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    cover: Cover | None = None

class ItemAnalytics(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_prime_customer: str | None = Field(None, alias='isPrimeCustomer')
    page_type_id_source: str | None = Field(None, alias='pageTypeIdSource')
    ref_marker: str | None = Field(None, alias='refMarker')
    page_type_id: str | None = Field(None, alias='pageTypeId')
    a9_search_fields: str | None = Field(None, alias='A9SearchFields')
    pvs3: str | None = None

class Link(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    analytics: dict[str, Any] | None = None
    metadata: dict[str, Any] | None = None
    url: str | None = None

class LiveInfo(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    status: str | None = None
    time_badge: str | None = Field(None, alias='timeBadge')
    venue: str | None = None

class MaturityRatingBadge(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__type: str | None = Field(None, alias='__type')
    description: str | None = None
    display_text: str | None = Field(None, alias='displayText')
    id: str | None = None
    country_code: str | None = Field(None, alias='countryCode')

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

class Action(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    ajax_enabled: bool | None = Field(None, alias='ajaxEnabled')
    endpoint: Endpoint | None = None
    format_code: str | None = Field(None, alias='formatCode')
    tag: str | None = None
    text: Text | None = None

class Item(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field__type: str | None = Field(None, alias='__type')
    action: Action | None = None
    item_type: str | None = Field(None, alias='itemType')
    text: str | None = None

class OverflowMenu(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    items: list[Item] | None = None
    title: str | None = None

class Endpoint1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    partial_url: str | None = Field(None, alias='partialURL')
    query: Query | None = None

class WatchlistAction(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    ajax_enabled: bool | None = Field(None, alias='ajaxEnabled')
    endpoint: Endpoint1 | None = None
    format_code: str | None = Field(None, alias='formatCode')
    tag: str | None = None
    text: Text | None = None

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

class Entity(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    buy_box_actions: list[Any] | None = Field(None, alias='buyBoxActions')
    degradations: list[Any] | None = None
    display_title: str | None = Field(None, alias='displayTitle')
    entitlement_cues: EntitlementCues | None = Field(None, alias='entitlementCues')
    entity_type: str | None = Field(None, alias='entityType')
    hover_info: HoverInfo | None = Field(None, alias='hoverInfo')
    images: Images | None = None
    impression_id: str | None = Field(None, alias='impressionId')
    is_closed_caption: bool | None = Field(None, alias='isClosedCaption')
    item_analytics: ItemAnalytics | None = Field(None, alias='itemAnalytics')
    link: Link | None = None
    live_info: LiveInfo | None = Field(None, alias='liveInfo')
    maturity_rating_badge: MaturityRatingBadge | None = Field(None, alias='maturityRatingBadge')
    overflow_menu: OverflowMenu | None = Field(None, alias='overflowMenu')
    playback_actions: list[Any] | None = Field(None, alias='playbackActions')
    ref_marker: str | None = Field(None, alias='refMarker')
    synopsis: str | None = None
    title: str | None = None
    title_id: str | None = Field(None, alias='titleID')
    watchlist_action: WatchlistAction | None = Field(None, alias='watchlistAction')
    widget_type: str | None = Field(None, alias='widgetType')
    release_year: str | None = Field(None, alias='releaseYear')
    runtime: str | None = None
    customer_reviews: CustomerReviews | None = Field(None, alias='customerReviews')

class EntitlementCues1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    entitled_carousel: str | None = Field(None, alias='entitledCarousel')
    offer_type: str | None = Field(None, alias='offerType')

class Action1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    analytics: dict[str, Any] | None = None
    label: str | None = None
    metadata: dict[str, Any] | None = None
    target: str | None = None
    url: str | None = None

class Badge(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    badge_text: str | None = Field(None, alias='badgeText')
    badge_type: str | None = Field(None, alias='badgeType')

class Container(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    container_type: str | None = Field(None, alias='containerType')
    entities: list[Entity] | None = None
    entitlement_cues: EntitlementCues1 | None = Field(None, alias='entitlementCues')
    estimated_total: int | None = Field(None, alias='estimatedTotal')
    impression_data: str | None = Field(None, alias='impressionData')
    inline_container_update_actions: list[Any] | None = Field(None, alias='inlineContainerUpdateActions')
    is_continue_watching: bool | None = Field(None, alias='isContinueWatching')
    strings: dict[str, Any] | None = None
    text: str | None = None
    title: str | None = None
    web_uid: timedelta | str | None = Field(None, alias='webUid', union_mode='left_to_right')
    action: Action1 | None = None
    badges: list[Badge] | None = None

class FeatureSwitches(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    use_post_for_enrichment: bool | None = Field(None, alias='usePostForEnrichment')
    disable_win_app_max_containers_limit: bool | None = Field(None, alias='disableWinAppMaxContainersLimit')
    is_pagination_limited_on_m_shop: bool | None = Field(None, alias='isPaginationLimitedOnMShop')
    no_index_paramount_parent_id_pages: bool | None = Field(None, alias='noIndexParamountParentIdPages')
    disable_hover: bool | None = Field(None, alias='disableHover')
    should_always_show_maturity_rating: bool | None = Field(None, alias='shouldAlwaysShowMaturityRating')
    is_mobile_web_streaming_enabled: bool | None = Field(None, alias='isMobileWebStreamingEnabled')
    is_hover_ssm_on: bool | None = Field(None, alias='isHoverSsmOn')
    disable_enrich_item_metadata: bool | None = Field(None, alias='disableEnrichItemMetadata')
    disable_storefront_tvod_checkout: bool | None = Field(None, alias='disableStorefrontTvodCheckout')

class Availability(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    description: str | None = None
    severity: str | None = None

class Metadata(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability: Availability | None = None

class PageMetadata1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    hide_page_title: bool | None = Field(None, alias='hidePageTitle')
    should_generate_json_ld: bool | None = Field(None, alias='shouldGenerateJsonLD')

class Strings(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    dv_web_aria_label_filter_item: str | None = Field(None, alias='DV_WEB_ARIA_LABEL_FILTER_ITEM')
    dv_web_aria_previous_title: str | None = Field(None, alias='DV_WEB_ARIA_PREVIOUS_TITLE')
    dv_web_pwa_first_launch_modal_learn_more: str | None = Field(None, alias='DV_WEB_PWA_First_LAUNCH_MODAL_LEARN_MORE')
    dv_web_watchlist_tooltip: str | None = Field(None, alias='DV_WEB_WATCHLIST_TOOLTIP')
    dv_comma_separator: str | None = Field(None, alias='DV_comma_separator')
    dv_web_sports_record_success_upcoming: str | None = Field(None, alias='DV_WEB_SPORTS_RECORD_SUCCESS_UPCOMING')
    dv_web_sports_record_success_ended: str | None = Field(None, alias='DV_WEB_SPORTS_RECORD_SUCCESS_ENDED')
    dv_web_pv_api_link_fallback_failure_retry_link: str | None = Field(None, alias='DV_WEB_PV_API_LINK_FALLBACK_FAILURE_RETRY_LINK')
    dv_web_sports_record_league_success_ended: str | None = Field(None, alias='DV_WEB_SPORTS_RECORD_LEAGUE_SUCCESS_ENDED')
    dv_web_watchlist_add: str | None = Field(None, alias='DV_WEB_WATCHLIST_ADD')
    dv_web_linear_program_record_start_success: str | None = Field(None, alias='DV_WEB_LINEAR_PROGRAM_RECORD_START_SUCCESS')
    dv_web_epg_card_on_now: str | None = Field(None, alias='DV_WEB_EPG_CARD_ON_NOW')
    dv_web_recording_scheduled: str | None = Field(None, alias='DV_WEB_RECORDING_SCHEDULED')
    dv_web_pwa_first_launch_modal_sign_in_now: str | None = Field(None, alias='DV_WEB_PWA_First_LAUNCH_MODAL_SIGN_IN_NOW')
    dv_web_aria_more_details: str | None = Field(None, alias='DV_WEB_ARIA_MORE_DETAILS')
    dv_dp_aria_release_year: str | None = Field(None, alias='DV_DP_ARIA_release_year')
    dv_web_recording_now: str | None = Field(None, alias='DV_WEB_RECORDING_NOW')
    dv_web_added_to_favorites: str | None = Field(None, alias='DV_WEB_ADDED_TO_FAVORITES')
    dv_web_sports_cancel_record_league_success: str | None = Field(None, alias='DV_WEB_SPORTS_CANCEL_RECORD_LEAGUE_SUCCESS')
    dv_dp_tr_liked_aria: str | None = Field(None, alias='DV_DP_TR_liked_aria')
    dv_web_aria_next_n_titles: str | None = Field(None, alias='DV_WEB_ARIA_NEXT_N_TITLES')
    dv_web_pv_api_link_fallback_failure_title: str | None = Field(None, alias='DV_WEB_PV_API_LINK_FALLBACK_FAILURE_TITLE')
    dv_web_aria_current_title_index: str | None = Field(None, alias='DV_WEB_ARIA_CURRENT_TITLE_INDEX')
    dv_web_favorites_filter_fallback_heading: str | None = Field(None, alias='DV_WEB_FAVORITES_FILTER_FALLBACK_HEADING')
    dv_web_linear_program_cancel_record_tooltip: str | None = Field(None, alias='DV_WEB_LINEAR_PROGRAM_CANCEL_RECORD_TOOLTIP')
    dv_web_more_details: str | None = Field(None, alias='DV_WEB_MORE_DETAILS')
    dv_web_linear_program_record_error: str | None = Field(None, alias='DV_WEB_LINEAR_PROGRAM_RECORD_ERROR')
    dv_web_aria_previous_title_index: str | None = Field(None, alias='DV_WEB_ARIA_PREVIOUS_TITLE_INDEX')
    dv_web_aria_previous_n_titles: str | None = Field(None, alias='DV_WEB_ARIA_PREVIOUS_N_TITLES')
    dv_web_removed_from_favorites: str | None = Field(None, alias='DV_WEB_REMOVED_FROM_FAVORITES')
    dv_web_overflow_menu_tooltip: str | None = Field(None, alias='DV_WEB_OVERFLOW_MENU_TOOLTIP')
    av_lrc_start_over: str | None = Field(None, alias='AV_LRC_START_OVER')
    dv_web_sports_record_league: str | None = Field(None, alias='DV_WEB_SPORTS_RECORD_LEAGUE')
    dv_web_draper_player_mute_button: str | None = Field(None, alias='DV_WEB_DRAPER_PLAYER_MUTE_BUTTON')
    dv_web_add_to_favorites: str | None = Field(None, alias='DV_WEB_ADD_TO_FAVORITES')
    dv_web_favorites_filter_fallback_body: str | None = Field(None, alias='DV_WEB_FAVORITES_FILTER_FALLBACK_BODY')
    dv_web_draper_player_unmute_button: str | None = Field(None, alias='DV_WEB_DRAPER_PLAYER_UNMUTE_BUTTON')
    dv_dp_tr_dislike_btn: str | None = Field(None, alias='DV_DP_TR_dislike_btn')
    dv_web_pwa_post_auth_modal_go_to_downloads: str | None = Field(None, alias='DV_WEB_PWA_POST_AUTH_MODAL_GO_TO_DOWNLOADS')
    dv_web_sports_cancel_record_success: str | None = Field(None, alias='DV_WEB_SPORTS_CANCEL_RECORD_SUCCESS')
    dv_web_pv_api_link_fallback_failure_message: str | None = Field(None, alias='DV_WEB_PV_API_LINK_FALLBACK_FAILURE_MESSAGE')
    dv_web_watchlist_csrf_problem: str | None = Field(None, alias='DV_WEB_WATCHLIST_CSRF_PROBLEM')
    dv_web_pwa_first_launch_modal_content: str | None = Field(None, alias='DV_WEB_PWA_First_LAUNCH_MODAL_CONTENT')
    dv_web_pwa_post_auth_modal_content: str | None = Field(None, alias='DV_WEB_PWA_POST_AUTH_MODAL_CONTENT')
    dv_web_undo_like: str | None = Field(None, alias='DV_WEB_Undo_like')
    dv_web_pv_api_link_fallback_success_message: str | None = Field(None, alias='DV_WEB_PV_API_LINK_FALLBACK_SUCCESS_MESSAGE')
    dv_web_details_tooltip: str | None = Field(None, alias='DV_WEB_DETAILS_TOOLTIP')
    dv_web_undo_remove_from_container: str | None = Field(None, alias='DV_WEB_UNDO_REMOVE_FROM_CONTAINER')
    dv_web_sports_record: str | None = Field(None, alias='DV_WEB_SPORTS_RECORD')
    dv_web_pwa_first_launch_modal_heading: str | None = Field(None, alias='DV_WEB_PWA_First_LAUNCH_MODAL_HEADING')
    dv_web_watchlist_remove: str | None = Field(None, alias='DV_WEB_WATCHLIST_REMOVE')
    dv_web_pwa_post_auth_modal_start_watching: str | None = Field(None, alias='DV_WEB_PWA_POST_AUTH_MODAL_START_WATCHING')
    dv_dp_tr_like_btn: str | None = Field(None, alias='DV_DP_TR_like_btn')
    dv_web_channel_name_logo_label: str | None = Field(None, alias='DV_WEB_CHANNEL_NAME_LOGO_LABEL')
    dv_web_remove_from_favorites: str | None = Field(None, alias='DV_WEB_REMOVE_FROM_FAVORITES')
    dv_web_sports_cancel_record_league: str | None = Field(None, alias='DV_WEB_SPORTS_CANCEL_RECORD_LEAGUE')
    dv_web_recording_indicator: str | None = Field(None, alias='DV_WEB_RECORDING_INDICATOR')
    dv_web_linear_program_record_cancel_success: str | None = Field(None, alias='DV_WEB_LINEAR_PROGRAM_RECORD_CANCEL_SUCCESS')
    dv_web_linear_program_record_tooltip: str | None = Field(None, alias='DV_WEB_LINEAR_PROGRAM_RECORD_TOOLTIP')
    dv_web_sports_recording_aria: str | None = Field(None, alias='DV_WEB_SPORTS_RECORDING_ARIA')
    dv_dp_aria_regulatory_rating: str | None = Field(None, alias='DV_DP_ARIA_regulatory_rating')
    dv_web_pwa_post_auth_modal_heading: str | None = Field(None, alias='DV_WEB_PWA_POST_AUTH_MODAL_HEADING')
    dv_web_linear_program_start_over_tooltip: str | None = Field(None, alias='DV_WEB_LINEAR_PROGRAM_START_OVER_TOOLTIP')
    dv_web_sports_record_league_success_upcoming: str | None = Field(None, alias='DV_WEB_SPORTS_RECORD_LEAGUE_SUCCESS_UPCOMING')
    dv_dp_tr_dislike_aria: str | None = Field(None, alias='DV_DP_TR_dislike_aria')
    dv_dp_aria_runtime: str | None = Field(None, alias='DV_DP_ARIA_runtime')
    dv_web_aria_next_title: str | None = Field(None, alias='DV_WEB_ARIA_NEXT_TITLE')
    dv_web_aria_next_title_index: str | None = Field(None, alias='DV_WEB_ARIA_NEXT_TITLE_INDEX')
    dv_dp_tr_like_aria: str | None = Field(None, alias='DV_DP_TR_like_aria')
    dv_web_watch_live: str | None = Field(None, alias='DV_WEB_WATCH_LIVE')
    dv_web_sports_cancel_record: str | None = Field(None, alias='DV_WEB_SPORTS_CANCEL_RECORD')
    dv_dp_tr_disliked_aria: str | None = Field(None, alias='DV_DP_TR_disliked_aria')

class SwiftPageParameters(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    page_id: str | None = Field(None, alias='pageId')
    page_type: str | None = Field(None, alias='pageType')

class RequestFeatureSwitches(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    horizontal_pagination: bool | None = Field(None, alias='HorizontalPagination')

class CustomerState(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_robotic: bool | None = Field(None, alias='isRobotic')

class FeatureSwitches1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    show_floating_join_prime_button: bool | None = Field(None, alias='showFloatingJoinPrimeButton')

class Metadata1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability: Availability | None = None

class Image(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    alt_text: str | None = Field(None, alias='altText')
    url: str | None = None

class Branding(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    image: Image | None = None
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

class Query2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    ie: str | None = None
    ref_: str | None = None

class SubmitSearchDestructuredEndpoint(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    partial_url: str | None = Field(None, alias='partialURL')
    query: Query2 | None = None

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
    feature_switches: FeatureSwitches1 | None = Field(None, alias='featureSwitches')
    is_sticky: bool | None = Field(None, alias='isSticky')
    metadata: Metadata1 | None = None
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

class Metadata2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability: Availability | None = None

class SitewideConditional(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    degradations: list[Any] | None = None
    features: dict[str, Any] | None = None
    metadata: Metadata2 | None = None
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
    containers: list[Container] | None = None
    feature_switches: FeatureSwitches | None = Field(None, alias='featureSwitches')
    has_failed: bool | None = Field(None, alias='hasFailed')
    is_trailer_autoplay_enabled: bool | None = Field(None, alias='isTrailerAutoplayEnabled')
    metadata: Metadata | None = None
    page_metadata: PageMetadata1 | None = Field(None, alias='pageMetadata')
    phrase: str | None = None
    playback_launch_type: str | None = Field(None, alias='playbackLaunchType')
    strings: Strings | None = None
    swift_page_parameters: SwiftPageParameters | None = Field(None, alias='swiftPageParameters')
    hz_page_type: str | None = Field(None, alias='hzPageType')
    hz_sub_page_type: str | None = Field(None, alias='hzSubPageType')
    home_region: str | None = Field(None, alias='homeRegion')
    request_feature_switches: RequestFeatureSwitches | None = Field(None, alias='requestFeatureSwitches')
    enable_vertical_performant_render: bool | None = Field(None, alias='enableVerticalPerformantRender')
    sitewide: Sitewide | None = None

class QueryParameters(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    phrase: list[str] | None = None
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
    page_type_id: Any | None = Field(None, alias='pageTypeId')
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
    dv_web_tr_persist_1434722: bool | None = Field(None, alias='DV_WEB_TR_PERSIST_1434722')
    dv_web_linear_station_taps_view_upgrade_1358041: bool | None = Field(None, alias='DV_WEB_LINEAR_STATION_TAPS_VIEW_UPGRADE_1358041')
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
    telemetry_client_launch_web_treatment: str | None = Field(None, alias='telemetryClientLaunchWebTreatment')
    is_runway_post_transition_enabled: bool | None = Field(None, alias='isRunwayPostTransitionEnabled')
    dv_web_dp_enable_whisper_cache_for_unrec_customers_1440503: bool | None = Field(None, alias='DV_WEB_DP_ENABLE_WHISPER_CACHE_FOR_UNREC_CUSTOMERS_1440503')
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
    pv_web_lighthouse_1438707: bool | None = Field(None, alias='PV_WEB_LIGHTHOUSE_1438707')

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

class Config(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    delay_loading_indicator: bool | None = Field(None, alias='delayLoadingIndicator')
    csn_deny_list: list[str] | None = Field(None, alias='csnDenyList')
    disable_downloads_sync: bool | None = Field(None, alias='disableDownloadsSync')
    client_ttl_mins: int | None = Field(None, alias='clientTTLMins')
    force_fake_navigation_api: bool | None = Field(None, alias='forceFakeNavigationAPI')

class SearchModel(BaseModel):
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
