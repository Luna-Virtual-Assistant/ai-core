from config import REQ_TOPIC, RES_TOPIC

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print(f"Client connect to broker sucessfully")
        client.subscribe(REQ_TOPIC)
        
    else:
        print(f"Connection failed with code {rc}")
        
def on_subscribe(client, userdata, mid, granted_qos):
    print(f'Client subscribed to topic with mid {mid} and QOS {granted_qos} on {REQ_TOPIC}')
    
def on_message(client, userdata, message):
    print(f"Received message '{message.payload.decode()}' on topic '{message.topic}' with QOS {message.qos}")