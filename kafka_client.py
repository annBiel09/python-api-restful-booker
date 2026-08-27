import json

from confluent_kafka import Consumer, KafkaError, KafkaException, Producer
from confluent_kafka.admin import AdminClient, NewTopic

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
                "auto.offset.reset": "latest",
                "enable.auto.commit": False,
            }
        )

    @staticmethod
    def create_topic(topic: str) -> None:
        admin_client = AdminClient({"bootstrap.servers": KAFKA_BOOTSTRAP_SERVERS})

        futures = admin_client.create_topics(
            [
                NewTopic(
                    topic,
                    num_partitions=1,
                    replication_factor=1,
                )
            ]
        )

        for future in futures.values():
            try:
                future.result()
            except KafkaException as error:
                if error.args[0].code() != KafkaError.TOPIC_ALREADY_EXISTS:
                    raise

    @staticmethod
    def serialize_message(message: dict) -> bytes:
        return json.dumps(message).encode("utf-8")
