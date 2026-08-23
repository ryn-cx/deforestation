# TODO: Validate
import pytest
from get_around import build_client_automatically

from deforestation import Deforestation


# TODO: Validate
@pytest.fixture(scope="session")
def client() -> Deforestation:
    return Deforestation(build_client_automatically())
