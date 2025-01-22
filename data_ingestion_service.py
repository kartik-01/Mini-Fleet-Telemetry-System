import paho.mqtt.client as mqtt
from kafka import KafkaProducer
import json

# MQTT settings
mqtt_broker = "localhost"
mqtt_topic = "vehicle/telemetry"

# Kafka settings
kafka_broker = "localhost:9092"
kafka_topic = "vehicle_telemetry"

# Initialize Kafka producer
producer = KafkaProducer(
    bootstrap_servers=[kafka_broker],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# MQTT on_message callback
def on_message(client, userdata, message):
    msg = json.loads(message.payload.decode())
    print(f"Received MQTT message: {msg}")
    # Produce message to Kafka
    producer.send(kafka_topic, value=msg)
    print(f"Produced message to Kafka: {msg}")

# Set up MQTT client
client = mqtt.Client()
client.on_message = on_message
client.connect(mqtt_broker)
client.subscribe(mqtt_topic)

# Start MQTT loop
print("Starting MQTT to Kafka bridge...")
client.loop_forever()
