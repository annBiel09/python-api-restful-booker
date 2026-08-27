import json

import paho.mqtt.client as mqtt

MQTT_BROKER = "localhost"
MQTT_PORT = 1883


class MqttClient:
    @staticmethod
    def create_client() -> mqtt.Client:
        return mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2)

    @staticmethod
    def serialize_message(message: dict) -> str:
        return json.dumps(message)
