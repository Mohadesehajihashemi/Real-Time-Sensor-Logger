import random
import time
import pymongo
from pymongo import MongoClient
from pymongo.errors import ConnectionError

# Configuration
MONGO_URI = "mongodb://localhost:27017/"
DB_NAME = "sensor_data"
COLLECTION_NAME = "readings"
SLEEP_INTERVAL = 5  # Seconds between logs

# Initialize MongoDB client
try:
    client = MongoClient(MONGO_URI)
    db = client[DB_NAME]
    collection = db[COLLECTION_NAME]
    # Test connection
    client.admin.command("ping")
    print("Connected to MongoDB successfully!")
except ConnectionError as e:
    print(f"Failed to connect to MongoDB: {e}")
    exit(1)

def log_sensor_data():
    """Log random sensor data to MongoDB continuously."""
    while True:
        data = {
            "temperature": round(random.uniform(20, 30), 2),  # Temperature in °C
            "humidity": round(random.uniform(40, 60), 2),     # Humidity in %
            "pressure": round(random.uniform(980, 1020), 2),  # Pressure in hPa
            "light": round(random.uniform(0, 1000), 2),       # Light in lux
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        }
        try:
            collection.insert_one(data)
            print(f"Logged: {data}")
        except Exception as e:
            print(f"Error logging data: {e}")
        time.sleep(SLEEP_INTERVAL)

if __name__ == "__main__":
    log_sensor_data()
