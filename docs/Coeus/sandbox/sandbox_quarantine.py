# Sandbox Quarantine — Isolates unstable or flagged coins during tournaments

import json
import time

class SandboxQuarantine:
    def __init__(self):
        self.quarantine_log = []

    def isolate(self, coin_id, reason):
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
        entry = {
            "coin_id": coin_id,
            "reason": reason,
            "timestamp": timestamp
        }
        self.quarantine_log.append(entry)
        print(f"[Quarantine] Isolated {coin_id} → {reason}")

    def export_log(self, path="sandbox/quarantine_log.json"):
        with open(path, "w") as f:
            json.dump(self.quarantine_log, f, indent=2)
        print(f"[Quarantine] Exported log to {path}")

