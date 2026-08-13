import httpx

HTTP_TIMEOUT = 10.0


class HttpClient:
    @staticmethod
    def get(url: str) -> httpx.Response:
        response = httpx.get(url, timeout=HTTP_TIMEOUT)
        response.raise_for_status()
        return response

    @staticmethod
    def post(url: str, payload: dict) -> httpx.Response:
        response = httpx.post(
            url,
            json=payload,
            timeout=HTTP_TIMEOUT,
        )
        response.raise_for_status()
        return response
