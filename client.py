import httpx

from config import BASE_URL, AuthSettings

_TOKEN_CACHE: str | None = None


def get_token() -> str:
    response = httpx.post(
        f"{BASE_URL}/auth",
        json={
            "username": AuthSettings.username,
            "password": AuthSettings.password,
        },
    )

    response.raise_for_status()

    return response.json()["token"]


def get_cached_token() -> str:
    global _TOKEN_CACHE

    if _TOKEN_CACHE is None:
        _TOKEN_CACHE = get_token()

    return _TOKEN_CACHE
