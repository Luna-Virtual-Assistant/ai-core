import paho.mqtt.client as mqtt
from dotenv import dotenv_values

config = dotenv_values(".env")

mqtt_client = mqtt.Client(config["PUBLISHER_NAME"])
mqtt_client.connect(host=config["HOST"], port=int(config["PORT"]))

def publish(text: str):
    print(f"Publishing {text}")
    mqtt_client.publish(topic=config["RES_TOPIC"], payload=text)