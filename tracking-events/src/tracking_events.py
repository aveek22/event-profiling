"""Generate tracking events."""

import json
from confluent_kafka import Producer
import generate_events

producer_config = {
    "bootstrap.servers": "localhost:9092"
}
producer = Producer(producer_config)

for i in range(1, 10):
    (key, event) = generate_events.create()
    producer.produce(topic= "tracking.events.raw.v1", key = key, value= json.dumps(event))
    # print(event)

producer.flush()