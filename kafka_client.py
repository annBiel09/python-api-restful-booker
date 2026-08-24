import json

from confluent_kafka import Consumer, Producer

KAFKA_BOOTSTRAP_SERVERS = "localhost:9092"


class KafkaClient:
    @staticmethod
    def create_producer() -> Producer:
        return Producer({"bootstrap.servers": KAFKA_BOOTSTRAP_SERVERS})

    @staticmethod
    def create_consumer(group_id: str) -> Consumer:
        return Consumer(
            {
                "bootstrap.servers": KAFKA_BOOTSTRAP_SERVERS,
                "group.id": group_id,
                "auto.offset.reset": "earliest",
                "enable.auto.commit": False,
            }
        )

    @staticmethod
    def serialize_message(message: dict) -> bytes:
        return json.dumps(message).encode("utf-8")
