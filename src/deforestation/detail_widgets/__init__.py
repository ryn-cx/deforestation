# TODO: Validate
"""Contains the DetailWidgets class."""

from __future__ import annotations

import json
from logging import NullHandler, getLogger
from typing import Any, override
from urllib.parse import quote

from deforestation.base_api_endpoint import BaseEndpoint
from deforestation.detail_widgets.models import DetailWidgetsModel

logger = getLogger(__name__)
logger.addHandler(NullHandler())

EPISODE_LIST = "EpisodeList"
"""Widget that holds one page of a season's episodes."""


class DetailWidgets(BaseEndpoint[DetailWidgetsModel]):
    """Manage the detail widgets file.

    A detail page is built out of widgets, and this refetches one of them
    without refetching the page. It is what the site calls when a control on an
    open page changes what that widget should show.

    The one that matters here is `EpisodeList`. A season's page only ever
    carries the first 24 of its episodes, and the rest are reached a page at a
    time through the tokens the page lists in
    `body.btf.state.episodeList.actions.episodePages`. Every page of a season is
    listed there from the start, so paging through does not have to be a walk:
    the tokens for all of them are known after the first request.

    Episodes come back as `widgets.episodeList.episodes`, a list rather than the
    title keyed map the detail page uses, each naming its own title in
    `titleID`.

    Source: the episode page buttons on https://www.amazon.com/gp/video/detail/{title_id}

    Example request:
        - GET /gp/video/api/getDetailWidgets?
            - titleID={title_id}&
            - widgets=[{"widgetType":"EpisodeList","widgetToken":"{token}"}]
            - HTTP/2
        - Host: www.amazon.com
        - User-Agent: __REDACTED__
        - Accept: application/json
        - Accept-Language: en-US
        - Accept-Encoding: gzip, deflate, br, zstd
        - Referer: https://www.amazon.com/
        - x-requested-with: XMLHttpRequest
        - Sec-Fetch-Dest: empty
        - Sec-Fetch-Mode: cors
        - Sec-Fetch-Site: same-origin
        - Connection: keep-alive
    """

    _response_model = DetailWidgetsModel

    # TODO: Validate
    @override
    def download(
        self,
        title_id: str,
        widget_token: str,
        widget_type: str = EPISODE_LIST,
    ) -> dict[str, Any]:
        log_id = self.get_log_id(self.download, locals())
        # The token is escaped inside the JSON and then escaped again as part of
        # it, which is what the site sends. The token survives being escaped
        # only once as well, but there is no reason to send something else.
        widgets = json.dumps(
            [{"widgetType": widget_type, "widgetToken": quote(widget_token, safe="")}],
            separators=(",", ":"),
        )
        return self._client.download_api(
            operation="getDetailWidgets",
            params={"titleID": title_id, "widgets": widgets},
            log_id=log_id,
        )

    # TODO: Validate
    @override
    def download_and_parse(
        self,
        title_id: str,
        widget_token: str,
        widget_type: str = EPISODE_LIST,
    ) -> DetailWidgetsModel:
        return self.parse(self.download(title_id, widget_token, widget_type))
