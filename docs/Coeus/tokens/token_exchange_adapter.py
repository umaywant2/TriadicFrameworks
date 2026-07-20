# Token Exchange Adapter — Simulates token swap and validator approval

import json
import uuid
from datetime import datetime

class TokenExchangeAdapter:
    def __init__(self):
        self.exchange_log = []

    def swap(self, token_a, token_b):
        tx_id = str(uuid.uuid4())
        timestamp = datetime.utcnow().isoformat() + "Z"
        record = {
            "tx_id": tx_id,
            "from": token_a["id"],
            "to": token_b["id"],
            "timestamp": timestamp
        }
        self.exchange_log.append(record)
        print(f"[ExchangeAdapter] Swapped {token_a['name']} → {token_b['name']}")

    def export_log(self, path="tokens/exchange_log.json"):
        with open(path, "w") as f:
            json.dump(self.exchange_log, f, indent=2)
        print(f"[ExchangeAdapter] Exported log to {path}")

