import json
import threading

from event_emulator import (
    TOPIC,
    create_booking_event,
    simulate_booking_created,
)
from mqtt_client import MQTT_BROKER, MQTT_PORT, MqttClient


def test_booking_event_emulator():
    message = create_booking_event()

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

    simulate_booking_created(message)

    assert message_received.wait(timeout=5)
    assert received_messages[0] == message

    subscriber.loop_stop()
    subscriber.disconnect()
