# TODO: Validate
"""Helpers the parsed models are read out of a response with.

A response is read as the JSON it was served as rather than through a model of
the whole of it, since the whole of it is far larger than the parts that are
kept.
"""

from __future__ import annotations

from datetime import datetime
from typing import Any

IMAGE_PREFERENCE = ("covershot", "packshot", "titleshot", "heroshot")
"""Which of a title's images stands for it, most wanted first."""

RELEASE_DATE_FORMAT = "%b %d, %Y"
"""How a release date is written, e.g. `Jan 22, 1985`."""


# TODO: Validate
def mapping(value: Any) -> dict[str, Any]:  # noqa: ANN401 - Any JSON value.
    """Return `value` when it is an object, and an empty one when it is not."""
    return value if isinstance(value, dict) else {}


# TODO: Validate
def sequence(value: Any) -> list[Any]:  # noqa: ANN401 - Any JSON value.
    """Return `value` when it is a list, and an empty one when it is not."""
    return value if isinstance(value, list) else []


# TODO: Validate
def text_or_none(value: Any) -> str | None:  # noqa: ANN401 - Any JSON value.
    """Return `value` as text, with a missing or empty value as None."""
    if value is None:
        return None
    text = str(value)
    return text or None


# TODO: Validate
def number_or_none(value: Any) -> float | None:  # noqa: ANN401 - Any JSON value.
    """Return `value` when it is a number, and None when it is not."""
    if isinstance(value, bool) or not isinstance(value, int | float):
        return None
    return value


# TODO: Validate
def texts(values: Any) -> list[str]:  # noqa: ANN401 - Any JSON value.
    """Return a list of values as the text each one is written as."""
    return [str(value) for value in sequence(values) if value is not None]


# TODO: Validate
def build_url(path: str) -> str:
    """Return the Prime Video address `path` is served at."""
    return f"https://www.primevideo.com/{path.lstrip('/')}"


# TODO: Validate
def amazon_url(path: str) -> str:
    """Return the Amazon address `path` is served at."""
    return f"https://www.amazon.com/{path.lstrip('/')}"


# TODO: Validate
def detail_url(link_id: str | None) -> str | None:
    """Return the address of the detail page written with `link_id`."""
    if not link_id:
        return None
    return build_url(f"detail/{link_id}")


# TODO: Validate
def link_id_from_href(href: Any) -> str | None:  # noqa: ANN401 - Any JSON value.
    """Return the id a link to a title carries, which is how its URL names it."""
    if not isinstance(href, str) or not href:
        return None
    return href.split("?", 1)[0].rstrip("/").rsplit("/", 1)[-1] or None


# TODO: Validate
def release_date(written_date: Any) -> str | None:  # noqa: ANN401 - Any JSON value.
    """Return a release date as an ISO date, or None when it is not one."""
    if not isinstance(written_date, str) or not written_date:
        return None
    try:
        # DTZ007 - A release date carries no timezone.
        parsed_date = datetime.strptime(written_date, RELEASE_DATE_FORMAT)  # noqa: DTZ007
    except ValueError:
        return None
    return parsed_date.date().isoformat()


# TODO: Validate
def pick_image(images: Any) -> str | None:  # noqa: ANN401 - Any JSON value.
    """Return the image that stands for a title, most wanted first."""
    named_images = mapping(images)
    for name in IMAGE_PREFERENCE:
        if image_url := text_or_none(named_images.get(name)):
            return image_url
    return None


# TODO: Validate
def named_urls(images: Any, names: dict[str, str]) -> dict[str, Any]:  # noqa: ANN401
    """Return the images a title carries, keyed by what each one is called."""
    named_images = mapping(images)
    return {name: text_or_none(named_images.get(key)) for name, key in names.items()}


# TODO: Validate
def episode_pages(actions: dict[str, Any]) -> list[dict[str, Any]]:
    """Return the pages an episode list is split over, as its actions list them.

    A page other than the selected one is downloaded with its token through the
    detail widgets endpoint.
    """
    pages: list[dict[str, Any]] = []
    for listed_page in sequence(actions.get("episodePages")):
        page = mapping(listed_page)
        pages.append(
            {
                "token": text_or_none(page.get("token")),
                "text": text_or_none(mapping(page.get("text")).get("string")),
                "is_selected": bool(page.get("isSelected")),
            },
        )
    return pages


# TODO: Validate
def episode(
    episode_key: str,
    detail: Any,  # noqa: ANN401 - Any JSON value.
    compact_gti: Any,  # noqa: ANN401 - Any JSON value.
    action: Any,  # noqa: ANN401 - Any JSON value.
    *,
    available: bool,
) -> dict[str, Any]:
    """Return one episode, as the page that lists it gives it."""
    episode_detail = mapping(detail)
    link_id = text_or_none(compact_gti)
    return {
        "key": episode_key,
        "link_id": link_id,
        "url": detail_url(link_id),
        "title": text_or_none(episode_detail.get("title")),
        "episode_number": number_or_none(episode_detail.get("episodeNumber")),
        "synopsis": text_or_none(episode_detail.get("synopsis")),
        "duration": number_or_none(episode_detail.get("duration")),
        "runtime": text_or_none(episode_detail.get("runtime")),
        "release_date": release_date(episode_detail.get("releaseDate")),
        "image_url": pick_image(episode_detail.get("images")),
        "is_available": available,
        "subscription_ids": offer_subscription_ids(action),
        "purchasable": offer_purchasable(action),
    }


# TODO: Validate
def action_cards(action: Any) -> list[Any]:  # noqa: ANN401 - Any JSON value.
    """Return every card an action offers a way to watch a title on."""
    cards: list[Any] = []
    for listed_action in sequence(mapping(action).get("primaryActions")):
        payload = mapping(mapping(listed_action).get("payload"))
        if card := payload.get("expandingCard"):
            cards.append(card)
        cards += sequence(payload.get("cardOptions"))
    return cards


# TODO: Validate
def offer_payloads(action: Any) -> list[dict[str, Any]]:  # noqa: ANN401 - Any JSON value.
    payloads = [
        mapping(mapping(option).get("payload"))
        for card in action_cards(action)
        for option in sequence(mapping(card).get("actions"))
        if mapping(option).get("payload")
    ]
    payloads += [
        mapping(mapping(listed_action).get("payload"))
        for listed_key in ("primaryActions", "secondaryActions")
        for listed_action in sequence(mapping(action).get(listed_key))
        if mapping(listed_action).get("payload")
    ]
    return payloads


# TODO: Validate
def offer_subscription_ids(action: Any) -> list[str]:  # noqa: ANN401 - Any JSON value.
    found = {
        str(subscription_id)
        for payload in offer_payloads(action)
        for holder in (payload.get("subscription"), payload.get("playback"))
        if (subscription_id := mapping(holder).get("benefitId"))
    }
    return sorted(found)


# TODO: Validate
def offer_purchasable(action: Any) -> bool:  # noqa: ANN401 - Any JSON value.
    return any(payload.get("transaction") for payload in offer_payloads(action))
