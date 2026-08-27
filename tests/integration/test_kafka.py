import json
import time
import uuid

from faker import Faker

from kafka_client import KafkaClient

fake = Faker()


def test_publish_and_consume_message(kafka_topic):
    message = {
        "bookingid": fake.random_int(min=1, max=10000),
        "firstname": fake.first_name(),
    }

    consumer = KafkaClient.create_consumer(group_id=f"test-{uuid.uuid4().hex}")
    consumer.subscribe([kafka_topic])

    timeout = time.time() + 10

    while not consumer.assignment() and time.time() < timeout:
        consumer.poll(timeout=1.0)

    assert consumer.assignment()

    producer = KafkaClient.create_producer()

    producer.produce(
        kafka_topic,
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
