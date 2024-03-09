import paho.mqtt.client as mqtt
from dotenv import dotenv_values
from datetime import datetime

config = dotenv_values(".env")

mqtt_client = mqtt.Client(config["PUBLISHER_NAME"])
mqtt_client.connect(host=config["HOST"], port=int(config["PORT"]))

def publish(text: str):
    print(f"[{datetime.now().strftime('%Y-%m-%d - %H:%M:%S')}] publishing to {config['RES_TOPIC']}")
    mqtt_client.publish(topic=config["RES_TOPIC"], payload=text)