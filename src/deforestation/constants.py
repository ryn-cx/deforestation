# TODO: Validate
"""Constants."""

from pathlib import Path

FILES_PATH = Path(__file__).parent / "_files"

DEFAULT_HOST = "www.amazon.com"

MARKETPLACES = {
    "US": "www.amazon.com",
    "UK": "www.amazon.co.uk",
    "DE": "www.amazon.de",
    "JP": "www.amazon.co.jp",
    "ROW": "www.primevideo.com",
}
"""Hosts the web player is served from, one per marketplace.

Every marketplace runs the same app against a different catalog, so the host is
the only thing that changes between them. `ROW` is the rest of the world, where
the catalog is decided by where the request comes from rather than by the host.
"""

CLIENT_VERSION = "1.0.127846.0"
"""Version the web player sends as `dvWebAppClientVersion`.

The parameter is what makes a page return its data instead of its HTML. Any
value has been accepted so far, but the real one is sent to stay unremarkable.
"""

WEB_PATH = "gp/video"
"""Prefix every page and API endpoint lives under."""

REGION_WEB_PATHS = {
    "NA": "region/na",
    "EU": "region/eu",
    "FE": "region/fe",
}
"""Prefixes the rest of the world marketplace serves its pages under.

`www.primevideo.com` is the app's own site rather than a section of Amazon's, so
its pages sit under the region they were resolved for instead of under
`WEB_PATH`. Asking for one without a region is answered with a redirect to the
same page carrying the region the request was resolved to, which is decided by
where it came from, so the region is named up front instead of being followed.
"""
