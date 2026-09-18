# TODO: Validate
"""Helpers the parsed models are read out of a response with.

A response is read as the JSON it was served as rather than through a model of
the whole of it, since the whole of it is far larger than the parts that are
kept.
"""

from __future__ import annotations

import re
from datetime import datetime
from typing import Any

PRIME_BENEFIT_ID = "Prime"
"""The benefit a title included with Prime is offered under."""

IMAGE_PREFERENCE = ("covershot", "packshot", "titleshot", "heroshot")
"""Which of a title's images stands for it, most wanted first."""

RELEASE_DATE_FORMAT = "%b %d, %Y"
"""How a release date is written, e.g. `Jan 22, 1985`."""

BENEFIT_ID_IN_LOGO = re.compile(r"/benefit-id/[^/]+/([^/]+)/logos/")
"""Where the benefit a title is offered under is written into its provider logo."""


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
def title_card(entity: Any) -> dict[str, Any]:  # noqa: ANN401 - Any JSON value.
    """Return one title as a row of titles lists it.

    A search result and a title recommended on a detail page are written the
    same way, so both are read into the same card.
    """
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
        "benefit_id": benefit_id(listed_title),
    }


# TODO: Validate
def benefit_id(entity: Any) -> str | None:  # noqa: ANN401 - Any JSON value.
    """Return the benefit a title is offered under, read off its provider logo."""
    cues = mapping(mapping(entity).get("entitlementCues"))
    logo_url = mapping(cues.get("providerLogo")).get("imageUrl")
    if not logo_url:
        return None
    found = BENEFIT_ID_IN_LOGO.search(str(logo_url))
    return found[1] if found else None


# TODO: Validate
def title_row(container: Any) -> dict[str, Any]:  # noqa: ANN401 - Any JSON value.
    """Return one row of titles, such as what customers also watched."""
    row = mapping(container)
    return {
        "title": text_or_none(row.get("title")),
        "container_type": text_or_none(row.get("containerType")),
        "titles": [title_card(entity) for entity in sequence(row.get("entities"))],
    }
