import json
import os
import random
import time
from datetime import datetime

OUTPUT_PATH = "data/raw_events"

os.makedirs(OUTPUT_PATH, exist_ok=True)

event_types = [
    "login",
    "purchase",
    "logout",
    "search"
]

NUM_EVENTS = 20

for i in range(NUM_EVENTS):

    event = {
        "event_id": random.randint(1000, 9999),
        "user_id": random.randint(1, 100),
        "event_type": random.choice(event_types),
        "amount": round(random.uniform(10, 500), 2),
        "timestamp": datetime.now().isoformat()
    }

    filename = f"{OUTPUT_PATH}/event_{i}.json"

    with open(filename, "w") as f:
        json.dump(event, f)

    print(f"Generated {i+1}/{NUM_EVENTS}")

    time.sleep(2)

print("Finished generating events")