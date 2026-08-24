import json
import uuid

from kafka_client import KafkaClient

TOPIC = "booking-created"


def test_publish_and_consume_message():
    message = {
        "bookingid": 123,
        "firstname": "Anna",
    }

    consumer = KafkaClient.create_consumer(group_id=f"test-{uuid.uuid4().hex}")
    consumer.subscribe([TOPIC])

    producer = KafkaClient.create_producer()

    producer.produce(
        TOPIC,
        value=KafkaClient.serialize_message(message),
    )
    producer.flush()

    received = None

    for _ in range(10):
        received = consumer.poll(timeout=1.0)
        if received is not None:
            break

    assert received is not None
    assert not received.error()

    received_message = json.loads(received.value().decode("utf-8"))

    assert received_message == message

    consumer.close()
