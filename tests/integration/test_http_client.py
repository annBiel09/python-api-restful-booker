from unittest.mock import patch

import httpx
import pytest

from http_client import HttpClient


def test_post_returns_successful_response():
    with patch("http_client.httpx.post") as mock_post:
        mock_post.return_value = httpx.Response(
            200,
            json={"status": "ok"},
            request=httpx.Request(
                "POST",
                "https://example.com",
            ),
        )

        response = HttpClient.post(
            "https://example.com",
            {"test": "data"},
        )

        assert response.status_code == 200
        assert response.json() == {"status": "ok"}


def test_post_raises_for_500_response():
    with patch("http_client.httpx.post") as mock_post:
        mock_post.return_value = httpx.Response(
            500,
            request=httpx.Request(
                "POST",
                "https://example.com",
            ),
        )

        with pytest.raises(httpx.HTTPStatusError):
            HttpClient.post(
                "https://example.com",
                {"test": "data"},
            )


def test_post_raises_for_timeout():
    with patch("http_client.httpx.post") as mock_post:
        mock_post.side_effect = httpx.TimeoutException("Request timed out")

        with pytest.raises(httpx.TimeoutException):
            HttpClient.post(
                "https://example.com",
                {"test": "data"},
            )
