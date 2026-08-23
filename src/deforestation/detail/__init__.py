# TODO: Validate
"""Contains the Detail class."""

from __future__ import annotations

from logging import NullHandler, getLogger

from deforestation.base_api_endpoint import BaseEndpoint
from deforestation.detail.models import DetailModel, model_validate_json
from deforestation.exceptions import ResourceNotFoundError, TitleNotFoundError

logger = getLogger(__name__)
logger.addHandler(NullHandler())


# TODO: Validate
class Detail(BaseEndpoint):
    """Manage the title detail file.

    A movie, a series, a season and an episode are all asked for the same way,
    but only a movie and a season are a page: an episode id lands on its
    season's page and a series id lands on one of its seasons, so the page says
    which title it settled on.

    Pages are asked for by ASIN (`B005C8DB7E`), which is what the site links to.

    Source: https://www.amazon.com/gp/video/detail/{title_id}

    Example request:
        - GET /gp/video/detail/{title_id}?
            - dvWebAppClientVersion=1.0.127846.0
            - HTTP/2
        - Host: www.amazon.com
        - User-Agent: __REDACTED__
        - Accept: application/json
        - Accept-Language: en-US
        - Accept-Encoding: gzip, deflate, br, zstd
        - Referer: https://www.amazon.com/
        - x-requested-with: WebAppSPA
        - Sec-Fetch-Dest: empty
        - Sec-Fetch-Mode: cors
        - Sec-Fetch-Site: same-origin
        - Connection: keep-alive
    """

    # TODO: Validate
    def __call__(self, title_id: str) -> DetailModel:
        """Look the title up and return the model it is read into."""
        log_id = self.get_log_id(self.__call__, locals())
        return self.load(self.download(title_id), log_id)

    # TODO: Validate
    def download(self, title_id: str) -> str:
        """Download the title detail file."""
        log_id = self.get_log_id(self.download, locals())
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
    def load(self, data: str, log_id: str = "") -> DetailModel:
        """Read a downloaded title detail file into its model."""
        return model_validate_json(data, log_id or type(self).__name__)
