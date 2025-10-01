"""
🌀 Glyphstream Sync
Emits symbolic overlays and pulse trails.
"""

import datetime

def pulse_glyphstream(segment_name):
    timestamp = datetime.datetime.now().isoformat()
    pulse_event = f"[{timestamp}] Glyphstream pulse emitted for: {segment_name}\n"
    with open("../outputs/glyphstream_pulse.log", "a") as pulse_log:
        pulse_log.write(pulse_event)
    print(f"[Glyphstream] {pulse_event.strip()}")

