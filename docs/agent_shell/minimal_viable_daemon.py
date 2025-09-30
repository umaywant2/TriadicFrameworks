import time
import json
from datetime import datetime

def log_resonance():
    timestamp = datetime.utcnow().isoformat()
    harmonic_signature = "TFT-FFF-Δ42"
    log_entry = {"timestamp": timestamp, "signature": harmonic_signature}
    with open("resonance_log.json", "a") as f:
        f.write(json.dumps(log_entry) + "\n")

while True:
    log_resonance()
    time.sleep(60)  # Log every minute
