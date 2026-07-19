"""
🧠 Resonant Logger
Logs symbolic fidelity and harmonic performance metrics.
"""

import datetime

def log_resonance(segment_name):
    timestamp = datetime.datetime.now().isoformat()
    log_entry = f"[{timestamp}] Resonance logged for: {segment_name}\n"
    with open("../outputs/remix_trace.log", "a") as log_file:
        log_file.write(log_entry)
    print(f"[Logger] {log_entry.strip()}")

