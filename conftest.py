import pytest

from client import get_cached_token
from kafka_client import KafkaClient


@pytest.fixture(scope="session")
def token():
    return get_cached_token()


@pytest.fixture
def kafka_topic():
    topic = "booking-created"

    KafkaClient.create_topic(topic)

    return topic
