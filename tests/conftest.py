import pytest
from get_around import build_client_automatically

from deforestation import Deforestation


@pytest.fixture(scope="session")
def client() -> Deforestation:
    return Deforestation(build_client_automatically())
