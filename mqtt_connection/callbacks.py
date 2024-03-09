from dotenv import dotenv_values
from generative.gemini import gemini
from datetime import datetime
from mqtt_publisher.publisher import publish

config = dotenv_values(".env")
REQ_TOPIC = config["REQ_TOPIC"]


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print(f"[{datetime.now().strftime('%Y-%m-%d - %H:%M:%S')}] {client._client_id.decode()} connected to broker sucessfully")
        client.subscribe(REQ_TOPIC)
        
    else:
        print(f"Connection failed with code {rc}")
        
def on_subscribe(client, userdata, mid, granted_qos):
    print(f"[{datetime.now().strftime('%Y-%m-%d - %H:%M:%S')}] {client._client_id.decode()} subscribed to topic with mid {mid} and QOS {granted_qos} on {REQ_TOPIC}")
    
def on_message(client, userdata, message):
    print(f"[{datetime.now().strftime('%Y-%m-%d - %H:%M:%S')}] Received a message on topic {message.topic}")
    res = gemini.generate_response(message.payload.decode())
    publish(res)
    
    