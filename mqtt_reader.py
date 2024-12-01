import asyncio
from gmqtt import Client as MQTTClient

BROKER_HOST = 'localhost'
BROKER_PORT = 1884
TOPIC = '/events'

# when a message is received from the broker.
def on_message(client, topic, payload, qos, properties):
    print(f"Received message on topic '{topic}': {payload.decode()}")
    
async def main():
    client = MQTTClient("MQTT_Reader_Client")

    client.on_message = on_message
    
    # Connect to the broker
    await client.connect(BROKER_HOST, BROKER_PORT)

    # Subscribe to the topic
    client.subscribe(TOPIC)
    print(f"Subscribed to topic '{TOPIC}'")
    # Run the event loop
    try:
        await asyncio.Future()
    except asyncio.CancelledError:
        pass

if __name__ == "__main__":
    asyncio.run(main())

