from faker import Faker

from mqtt_client import MQTT_BROKER, MQTT_PORT, MqttClient

TOPIC = "booking/events"

fake = Faker()


def create_booking_event() -> dict:
    return {
        "event": "booking_created",
        "booking_id": fake.random_int(min=1, max=10000),
        "firstname": fake.first_name(),
    }


def simulate_booking_created(message: dict):
    client = MqttClient.create_client()

    client.connect(MQTT_BROKER, MQTT_PORT)

    client.publish(
        TOPIC,
        MqttClient.serialize_message(message),
    )

    print(f"Published message: {message}")

    client.disconnect()


if __name__ == "__main__":
    message = create_booking_event()

    simulate_booking_created(message)
