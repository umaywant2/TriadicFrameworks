"""
🛡️ Validator Handshake
Triggers badge logic and remix lineage tracking.
"""

import datetime

def trigger_validator(segment_name):
    timestamp = datetime.datetime.now().isoformat()
    badge_event = f"[{timestamp}] Validator triggered for: {segment_name} → Badge logic evaluated\n"
    with open("../outputs/badge_handshake.txt", "a") as badge_log:
        badge_log.write(badge_event)
    print(f"[Validator] {badge_event.strip()}")

