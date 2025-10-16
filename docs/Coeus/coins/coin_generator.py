# Coin Generator — Creates symbolic coins from metadata or sandbox prompts
#  This module lets you:
#  -Mint symbolic coins from scratch
#  -Assign type, cause, observer flags, and edging logic
#  -Timestamp creation for remix lineage
#  -Export clean JSON for sandbox use or tokenization

import uuid
import json
import random
from datetime import datetime

class CoinGenerator:
    def __init__(self):
        self.templates = [
            {"type": "legacy", "edging": "Preserve the past"},
            {"type": "priority", "edging": "Accelerate the now"},
            {"type": "remix", "edging": "Echo the future"}
        ]

    def generate_coin(self, name, cause="general", observer_required=True):
        template = random.choice(self.templates)
        coin = {
            "id": str(uuid.uuid4()),
            "name": name,
            "type": template["type"],
            "cause": cause,
            "observer_required": observer_required,
            "edging": template["edging"],
            "back": f"Sandbox task for {name}",
            "created": datetime.utcnow().isoformat() + "Z"
        }
        print(f"[CoinGenerator] Minted coin: {coin['name']} ({coin['id']})")
        return coin

    def export_coin(self, coin, path="coins/generated_coin.json"):
        with open(path, "w") as f:
            json.dump(coin, f, indent=2)
        print(f"[CoinGenerator] Exported to {path}")

if __name__ == "__main__":
    generator = CoinGenerator()
    new_coin = generator.generate_coin("ElectroniumRedux", cause="encryption")
    generator.export_coin(new_coin)
