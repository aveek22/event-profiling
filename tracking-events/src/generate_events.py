"""Generate raw events"""

import random
import uuid

APP_IDS = ["google", "apple", "netflix", "meta"]
EVENT_TYPES = [
    "pageview",
    "click",
    "video_start"
]
ACCOUNT_IDS = [
    "account_id_1",
    "account_id_2",
    "account_id_3"
]

SESSION_IDS = [
    "session_id_1",
    "session_id_2",
    "session_id_3",
    "session_id_4",
    "session_id_5",
]

def create():
    """Generates a raw tracking event."""
    event_id = str(uuid.uuid4())
    event = {
        "event_id": event_id,
        "event_type": random.choice(EVENT_TYPES),
        "account_id": random.choice(ACCOUNT_IDS),
        "session_id": random.choice(SESSION_IDS)
    }

    return event_id, event