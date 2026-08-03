import pytest

from client import get_cached_token


@pytest.fixture(scope="session")
def token():
    return get_cached_token()
