import paho.mqtt.client as mqtt
import json
import time
import random
import uuid

def generate_telemetry(vehicle_id):
    return {
        "vehicle_id": vehicle_id,
        "timestamp": int(time.time()),
        "speed": round(random.uniform(0, 120), 2),
        "battery_level": round(random.uniform(0, 100), 2),
        "latitude": round(random.uniform(30, 50), 6),  
        "longitude": round(random.uniform(-120, -70), 6), 
        "heading": round(random.uniform(0, 359), 2),
        "acceleration": round(random.uniform(-5, 5), 2),
        "tire_pressure": {
            "front_left": round(random.uniform(30, 35), 1),
            "front_right": round(random.uniform(30, 35), 1),
            "rear_left": round(random.uniform(30, 35), 1),
            "rear_right": round(random.uniform(30, 35), 1)
        },
        "engine_temperature": round(random.uniform(90, 110), 1),
        "outside_temperature": round(random.uniform(-10, 40), 1),
        "windshield_wiper_status": random.choice(["off", "low", "medium", "high"]),
        "lights_status": random.choice(["off", "on", "auto"]),
        "autopilot_engaged": random.choice([True, False])
    }

# MQTT setup
broker = "localhost"
port = 1883
topic = "vehicle/telemetry"

client = mqtt.Client()
client.connect(broker, port, 60)

# Generate 10 unique vehicle IDs
vehicle_ids = [f"VEH-{uuid.uuid4().hex[:8].upper()}" for _ in range(10)]

try:
    while True:
        for vehicle_id in vehicle_ids:
            telemetry = generate_telemetry(vehicle_id)
            client.publish(topic, json.dumps(telemetry))
            print(f"Published: {telemetry}")
        time.sleep(1)  # Simulate data to be being sent out every second
except KeyboardInterrupt:
    print("Simulation stopped.")
    client.disconnect()
