import time

from .mqtt_client_connection import MqttClientConnection
from config import HOST, PORT, CLIENT_NAME, KEEP_ALIVE

def start():
    mqtt_client = MqttClientConnection(
        broker_ip=HOST,
        port=PORT,
        client_name=CLIENT_NAME,
        keep_alive=KEEP_ALIVE
    )
    mqtt_client.start_connection()
    
    while True: 
        try:
            time.sleep(0.001)
        except KeyboardInterrupt:
            mqtt_client.end_connection()
            break