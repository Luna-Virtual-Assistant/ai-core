from datetime import datetime
import json
from mqtt_publisher.publisher import publish
import os
from dotenv import load_dotenv
from factory import AIFactory

load_dotenv(override=True)
ai = AIFactory().get_ai('gemini')

REQ_TOPIC = os.getenv("REQ_TOPIC")

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
    print(f"[{datetime.now().strftime('%Y-%m-%d - %H:%M:%S')}] Message payload: {message.payload.decode()}")
    res = ai.generate_response(message.payload.decode())
    data = {
        "command": message.payload.decode(),
        "response": res
    }
    stringfied_response = json.dumps(data)
    publish(text=stringfied_response, topic='/history')
    publish(res)
    