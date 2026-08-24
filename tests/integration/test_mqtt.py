import json
import threading

from mqtt_client import MQTT_BROKER, MQTT_PORT, MqttClient

TOPIC = "device/status"


def test_publish_and_receive_message():
    message = {
        "device_id": "mat-123",
        "status": "active",
    }

    received_messages = []
    message_received = threading.Event()

    subscriber = MqttClient.create_client()

    def on_message(client, userdata, msg):
        received_messages.append(json.loads(msg.payload.decode("utf-8")))
        message_received.set()

    subscriber.on_message = on_message

    subscriber.connect(MQTT_BROKER, MQTT_PORT)
    subscriber.subscribe(TOPIC)
    subscriber.loop_start()

    publisher = MqttClient.create_client()
    publisher.connect(MQTT_BROKER, MQTT_PORT)

    publisher.publish(
        TOPIC,
        MqttClient.serialize_message(message),
    )

    assert message_received.wait(timeout=5)
    assert received_messages[0] == message

    subscriber.loop_stop()
    subscriber.disconnect()
    publisher.disconnect()
