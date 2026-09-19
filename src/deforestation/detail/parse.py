# TODO: Validate
"""Read the essentials of a title out of its detail page."""

from __future__ import annotations

import re
from typing import Any

from deforestation.parsing import (
    action_cards,
    detail_url,
    episode,
    episode_pages,
    link_id_from_href,
    mapping,
    named_urls,
    number_or_none,
    offer_subscription_ids,
    pick_image,
    release_date,
    sequence,
    text_or_none,
    texts,
)

PRIME_SUBSCRIPTION_ID = "Prime"
"""The benefit a title included with Prime is offered under."""

SUBSCRIPTION_ID_IN_LOGO = re.compile(r"/benefit-id/[^/]+/([^/]+)/logos/")
"""Where the benefit a title is offered under is written into its provider logo."""

IMAGE_NAMES = {
    "covershot": "covershot",
    "packshot": "packshot",
    "titleshot": "titleshot",
    "heroshot": "heroshot",
    "title_logo": "titleLogo",
}
"""The images a title carries, keyed by what each one is called."""

CONTRIBUTOR_ROLES = ("cast", "directors", "producers")
"""The roles a title credits people in."""

CHANNEL_NAME_PREFIXES = ("Watch with ", "Start your free trial to ", "Subscribe to ")
"""What a channel's own name is written after in the label it is offered under."""

LABEL_LINE_BREAK = "{lineBreak}"
"""What splits the two lines of an offer's label."""


# TODO: Validate
def parse_detail(page: Any) -> dict[str, Any]:  # noqa: ANN401 - Any JSON value.
    """Return the essentials of a detail page, as the parsed model reads them."""
    body = mapping(mapping(page).get("body"))
    atf_state = mapping(mapping(body.get("atf")).get("state"))
    btf_state = mapping(mapping(body.get("btf")).get("state"))
    page_id = str(atf_state.get("pageTitleId"))
    header = mapping(mapping(atf_state.get("detail")).get("headerDetail")).get(page_id)
    seasons = _seasons(atf_state, page_id)
    link_id = _link_id(atf_state, page_id)
    offer_cards = _offer_cards(atf_state, page_id)

    return {
        "page_id": page_id,
        "link_id": link_id,
        "title_key": _title_key(seasons, link_id),
        "url": detail_url(link_id),
        **_header_fields(mapping(header)),
        "imdb_rating": _imdb_rating(atf_state, page_id),
        "moods": _moods(atf_state, page_id),
        "included_with_prime": _included_with_prime(offer_cards),
        "free_with_ads": _free_with_ads(atf_state, page_id),
        "purchasable": _purchasable(offer_cards),
        "unavailable_message": _unavailable_message(atf_state, page_id, offer_cards),
        "channels": _channels(offer_cards),
        "seasons": seasons,
        "episode_count": _episode_count(btf_state),
        "episodes": _episodes(btf_state),
        "episode_pages": _episode_pages(btf_state),
        "containers": _containers(btf_state, page_id),
    }


# TODO: Validate
def _link_id(atf_state: dict[str, Any], page_id: str) -> str | None:
    """Return the id of this title that a link to it is written with."""
    page_self = mapping(mapping(atf_state.get("self")).get(page_id))
    return text_or_none(page_self.get("compactGTI"))


# TODO: Validate
def _title_key(seasons: list[dict[str, Any]], link_id: str | None) -> str | None:
    """Return the key the title this page is for is stored under.

    A series has no page of its own, so its first season stands for the whole
    series and a series reached through any of its seasons is the one title.
    """
    if not seasons:
        return link_id
    first_season = min(seasons, key=lambda season: season["season_number"] or 0)
    return first_season["key"]


# TODO: Validate
def _header_fields(header: dict[str, Any]) -> dict[str, Any]:
    """Return what the page says about the title itself."""
    rating_badge = mapping(header.get("ratingBadge"))
    amazon_rating = mapping(header.get("amazonRating"))
    contributors = mapping(header.get("contributors"))
    return {
        "title": text_or_none(header.get("title")),
        "parent_title": text_or_none(header.get("parentTitle")),
        "synopsis": text_or_none(header.get("synopsis")),
        "entity_type": text_or_none(header.get("entityType")),
        "title_type": text_or_none(header.get("titleType")),
        "season_number": number_or_none(header.get("seasonNumber")),
        "release_date": release_date(header.get("releaseDate")),
        "release_year": number_or_none(header.get("releaseYear")),
        "duration": number_or_none(header.get("duration")),
        "runtime": text_or_none(header.get("runtime")),
        "image_url": pick_image(header.get("images")),
        "images": named_urls(header.get("images"), IMAGE_NAMES),
        "genres": [
            str(mapping(genre)["text"])
            for genre in sequence(header.get("genres"))
            if mapping(genre).get("text")
        ],
        "studios": texts(header.get("studios")),
        **{role: _contributor_names(contributors, role) for role in CONTRIBUTOR_ROLES},
        "audio_tracks": texts(header.get("audioTracks")),
        "subtitles": texts(header.get("subtitles")),
        "maturity_rating": text_or_none(rating_badge.get("displayText")),
        "amazon_rating": number_or_none(amazon_rating.get("value")),
        "amazon_rating_count": number_or_none(amazon_rating.get("count")),
    }


# TODO: Validate
def _contributor_names(contributors: dict[str, Any], role: str) -> list[str]:
    """Return the names of everyone credited in one role."""
    return [
        str(mapping(person)["name"])
        for person in sequence(contributors.get(role))
        if mapping(person).get("name")
    ]


# TODO: Validate
def _imdb_rating(atf_state: dict[str, Any], page_id: str) -> float | None:
    """Return the IMDb score of the title, out of ten."""
    imdb = mapping(mapping(atf_state.get("imdb")).get(page_id))
    return number_or_none(imdb.get("score"))


# TODO: Validate
def _moods(atf_state: dict[str, Any], page_id: str) -> list[str]:
    """Return the moods the title is filed under, e.g. `Exciting`."""
    metadata = mapping(mapping(atf_state.get("metadata")).get(page_id))
    return texts(metadata.get("moods"))


# TODO: Validate
def _seasons(atf_state: dict[str, Any], page_id: str) -> list[dict[str, Any]]:
    """Return every season of the series this page is a season of."""
    listed_seasons = sequence(mapping(atf_state.get("seasons")).get(page_id))
    entries: list[dict[str, Any]] = []
    for listed_season in listed_seasons:
        season = mapping(listed_season)
        # Keyed by the id its own page is addressed by rather than by the id the
        # listing names it with, so a season is the same season whichever way in
        # it was found.
        key = link_id_from_href(season.get("seasonLink"))
        entries.append(
            {
                "key": key,
                "name": text_or_none(season.get("displayName")),
                "season_number": number_or_none(season.get("sequenceNumber")),
                "url": detail_url(key),
                "is_selected": bool(season.get("isSelected")),
            },
        )
    return entries


# TODO: Validate
def _episode_count(btf_state: dict[str, Any]) -> float | None:
    """Return how many episodes the season has, across all of its pages."""
    episode_list = mapping(btf_state.get("episodeList"))
    return number_or_none(episode_list.get("totalCardSize"))


# TODO: Validate
def _episode_pages(btf_state: dict[str, Any]) -> list[dict[str, Any]]:
    """Return every page the season's episode list is split over."""
    actions = mapping(mapping(btf_state.get("episodeList")).get("actions"))
    return episode_pages(actions)


# TODO: Validate
def _episodes(btf_state: dict[str, Any]) -> list[dict[str, Any]]:
    """Return the episodes the season's own page carries."""
    episode_list = mapping(btf_state.get("episodeList"))
    episode_details = mapping(mapping(btf_state.get("detail")).get("detail"))
    link_ids = mapping(btf_state.get("self"))
    return [
        episode(
            str(episode_key),
            episode_details[episode_key],
            mapping(link_ids.get(episode_key)).get("compactGTI"),
            _episode_action(btf_state, str(episode_key)),
            available=_episode_available(btf_state, str(episode_key)),
        )
        for episode_key in sequence(episode_list.get("cardTitleIds"))
        if episode_key in episode_details
    ]


# TODO: Validate
def _episode_action(btf_state: dict[str, Any], episode_key: str) -> Any:  # noqa: ANN401 - Any JSON value.
    return mapping(mapping(btf_state.get("action")).get("btf")).get(episode_key)


# TODO: Validate
def _episode_available(btf_state: dict[str, Any], episode_key: str) -> bool:
    """Report whether the episode is offered a way to watch it."""
    episode_action = _episode_action(btf_state, episode_key)
    if not episode_action:
        return True
    return any(mapping(card).get("actions") for card in action_cards(episode_action))


# TODO: Validate
def _atf_action(atf_state: dict[str, Any], page_id: str) -> Any:  # noqa: ANN401 - Any JSON value.
    return mapping(mapping(atf_state.get("action")).get("atf")).get(page_id)


# TODO: Validate
def _offer_cards(atf_state: dict[str, Any], page_id: str) -> list[Any]:
    """Return every card the page offers a way to watch the title on."""
    return action_cards(_atf_action(atf_state, page_id))


# TODO: Validate
def _free_with_ads(atf_state: dict[str, Any], page_id: str) -> bool:
    return "freewithads" in offer_subscription_ids(_atf_action(atf_state, page_id))


# TODO: Validate
def _offer_payloads(offer_cards: list[Any]) -> list[dict[str, Any]]:
    """Return everything the page says about how the title can be watched."""
    return [
        mapping(mapping(option).get("payload"))
        for card in offer_cards
        for option in sequence(mapping(card).get("actions"))
        if mapping(option).get("payload")
    ]


# TODO: Validate
def _included_with_prime(offer_cards: list[Any]) -> bool:
    """Report whether a Prime subscription is enough to watch this title."""
    return any(
        mapping(payload.get("subscription")).get("benefitId") == PRIME_SUBSCRIPTION_ID
        for payload in _offer_payloads(offer_cards)
    )


# TODO: Validate
def _purchasable(offer_cards: list[Any]) -> bool:
    """Report whether the title can be bought or rented."""
    return any(payload.get("transaction") for payload in _offer_payloads(offer_cards))


# TODO: Validate
def _unavailable_message(
    atf_state: dict[str, Any],
    page_id: str,
    offer_cards: list[Any],
) -> str | None:
    """Return why the title cannot be watched, when nothing offers it."""
    if _offer_payloads(offer_cards):
        return None
    action = _atf_action(atf_state, page_id)
    for listed_action in sequence(mapping(action).get("primaryActions")):
        primary_action = mapping(listed_action)
        if primary_action.get("actionType") != "MESSAGE":
            continue
        message = mapping(mapping(primary_action.get("payload")).get("message"))
        if written_message := mapping(message.get("message")).get("string"):
            return text_or_none(written_message)
    return None


# TODO: Validate
def _channels(offer_cards: list[Any]) -> list[dict[str, Any]]:
    """Return every Amazon Channel this title can be watched with.

    A channel is offered more than once when it offers the title in more than
    one way, and the offer the page leads with is the one that names it.
    """
    channels: dict[str, dict[str, Any]] = {}
    for card in offer_cards:
        for option in sequence(mapping(card).get("actions")):
            payload = mapping(mapping(option).get("payload"))
            subscription = mapping(payload.get("subscription"))
            if not subscription:
                continue
            subscription_id = str(subscription.get("benefitId"))
            if subscription_id == PRIME_SUBSCRIPTION_ID:
                continue
            logo_url = _card_logo_url(card)
            if channel := channels.get(subscription_id):
                channel["logo_url"] = channel["logo_url"] or logo_url
                continue
            channels[subscription_id] = {
                "subscription_id": subscription_id,
                "name": _card_heading(card) or _channel_name(subscription.get("label")),
                "logo_url": logo_url,
            }
    return list(channels.values())


# TODO: Validate
def _card_payloads(card: Any) -> list[dict[str, Any]]:  # noqa: ANN401 - Any JSON.
    """Return what every component of a card holds."""
    components = mapping(mapping(card).get("components"))
    return [
        mapping(mapping(component).get("componentPayload"))
        for component in components.values()
        if mapping(component).get("componentPayload")
    ]


# TODO: Validate
def _card_logo_url(card: Any) -> str | None:  # noqa: ANN401 - Any JSON value.
    """Return the logo of what the card offers."""
    for payload in _card_payloads(card):
        if logo_url := mapping(payload.get("logoComponent")).get("url"):
            return str(logo_url)
    return None


# TODO: Validate
def _card_texts(card: Any) -> list[dict[str, Any]]:  # noqa: ANN401 - Any JSON value.
    """Return every piece of text a card is written with."""
    written_texts: list[dict[str, Any]] = []
    for payload in _card_payloads(card):
        collection = mapping(payload.get("textComponentCollection"))
        written_texts += [
            mapping(text) for text in sequence(collection.get("textList"))
        ]
        if text_component := payload.get("textComponent"):
            written_texts.append(mapping(text_component))
    return written_texts


# TODO: Validate
def _card_heading(card: Any) -> str | None:  # noqa: ANN401 - Any JSON value.
    """Return what the card writes the name of what it offers as.

    The button on the card is labelled with what pressing it does rather than
    with the channel, so more than one channel is offered under the same label.
    """
    for text in _card_texts(card):
        if text.get("textType") == "HEADING" and text.get("text"):
            return str(text["text"]).strip()
    return None


# TODO: Validate
def _channel_name(label: Any) -> str | None:  # noqa: ANN401 - Any JSON value.
    """Return the channel's own name, as the label it is offered under writes it."""
    if not label:
        return None
    name = str(label).split(LABEL_LINE_BREAK, 1)[0].strip()
    for prefix in CHANNEL_NAME_PREFIXES:
        name = name.removeprefix(prefix)
    return name or None


# TODO: Validate
def _containers(btf_state: dict[str, Any], page_id: str) -> list[dict[str, Any]]:
    """Return the rows of other titles the page carries."""
    listed_containers = sequence(mapping(btf_state.get("containers")).get(page_id))
    return [_title_row(container) for container in listed_containers]


# TODO: Validate
def _title_card(entity: Any) -> dict[str, Any]:  # noqa: ANN401 - Any JSON value.
    """Return one title as a row of titles lists it."""
    listed_title = mapping(entity)
    link_id = link_id_from_href(mapping(listed_title.get("link")).get("url"))
    cover = mapping(mapping(listed_title.get("images")).get("cover"))
    maturity_rating_badge = mapping(listed_title.get("maturityRatingBadge"))
    return {
        "title_id": text_or_none(listed_title.get("titleID")),
        "link_id": link_id,
        "url": detail_url(link_id),
        "title": text_or_none(listed_title.get("title")),
        "synopsis": text_or_none(listed_title.get("synopsis")),
        "entity_type": text_or_none(listed_title.get("entityType")),
        "release_year": text_or_none(listed_title.get("releaseYear")),
        "runtime": text_or_none(listed_title.get("runtime")),
        "image_url": text_or_none(cover.get("url")),
        "maturity_rating": text_or_none(maturity_rating_badge.get("displayText")),
        "subscription_id": _subscription_id(listed_title),
    }


# TODO: Validate
def _subscription_id(entity: Any) -> str | None:  # noqa: ANN401 - Any JSON value.
    """Return the benefit a title is offered under, read off its provider logo."""
    cues = mapping(mapping(entity).get("entitlementCues"))
    logo_url = mapping(cues.get("providerLogo")).get("imageUrl")
    if not logo_url:
        return None
    found = SUBSCRIPTION_ID_IN_LOGO.search(str(logo_url))
    return found[1] if found else None


# TODO: Validate
def _title_row(container: Any) -> dict[str, Any]:  # noqa: ANN401 - Any JSON value.
    """Return one row of titles, such as what customers also watched."""
    row = mapping(container)
    return {
        "title": text_or_none(row.get("title")),
        "container_type": text_or_none(row.get("containerType")),
        "titles": [_title_card(entity) for entity in sequence(row.get("entities"))],
    }
