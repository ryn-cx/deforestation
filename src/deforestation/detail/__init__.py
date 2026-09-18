# TODO: Validate

from __future__ import annotations

import json
import re
from logging import NullHandler, getLogger

from deforestation.base_api_endpoint import BaseEndpoint
from deforestation.detail.models import (
    ParsedDetailModel,
    model_validate_json,
)
from deforestation.detail.parse import parse_detail
from deforestation.exceptions import (
    RedirectedError,
    ResourceNotFoundError,
    TitleNotFoundError,
)

logger = getLogger(__name__)
logger.addHandler(NullHandler())

TITLE_ID_IN_LOCATION = re.compile(r"/(?:dp|gp/video/detail)/([A-Z0-9]{10,})")


# TODO: Validate
class Detail(BaseEndpoint):
    # TODO: Validate
    def __call__(self, title_id: str) -> ParsedDetailModel:
        log_id = self.get_log_id(self.__call__, locals())
        return self.load(self.download(title_id), log_id)

    # TODO: Validate
    def download(self, title_id: str) -> str:

        log_id = self.get_log_id(self.download, locals())
        try:
            return self._download(title_id, log_id)
        except RedirectedError as err:
            landing_title_id = self._title_id(err.location)
            logger.debug("%s is served as %s.", title_id, landing_title_id)
            return self._download(landing_title_id, log_id)

    # TODO: Validate
    @staticmethod
    def _title_id(location: str) -> str:
        if found := TITLE_ID_IN_LOCATION.search(location):
            return found[1]
        msg = f"Could not get title_id from {location}"
        raise ValueError(msg)

    # TODO: Validate
    def _download(self, title_id: str, log_id: str) -> str:
        try:
            return self._client.download(
                endpoint=f"detail/{title_id}",
                params={"dvWebAppClientVersion": self._client.client_version},
                headers={"x-requested-with": "WebAppSPA"},
                log_id=log_id,
            )
        except ResourceNotFoundError as err:
            raise TitleNotFoundError(
                title_id,
                err.status_code,
                err.response,
            ) from err

    # TODO: Validate
    def load(self, data: str, log_id: str = "") -> ParsedDetailModel:
        return model_validate_json(
            parse_detail(json.loads(data)),
            log_id or self.default_log_id,
        )
