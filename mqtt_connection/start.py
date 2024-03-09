import time

from .mqtt_client_connection import MqttClientConnection
from dotenv import dotenv_values

config = dotenv_values(".env")

def start():
    mqtt_client = MqttClientConnection(
        broker_ip=config["HOST"],
        port=int(config["PORT"]),
        client_name=config["CLIENT_NAME"],
        keep_alive=int(config["KEEP_ALIVE"])
    )
    mqtt_client.start_connection()
    
    while True: 
        try:
            time.sleep(0.001)
        except KeyboardInterrupt:
            mqtt_client.end_connection()
            break