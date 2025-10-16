# Coin Remixer — Forks existing coins and mutates metadata for remix lineage

import json
import uuid
from datetime import datetime

class CoinRemixer:
    def __init__(self, source_path="coins/generated_coin.json"):
        with open(source_path, "r") as f:
            self.original = json.load(f)

    def remix(self, new_name, mutation="symbolic"):
        remixed = self.original.copy()
        remixed["id"] = str(uuid.uuid4())
        remixed["name"] = new_name
        remixed["type"] = "remix"
        remixed["edging"] = f"Remixed from {self.original['name']} with {mutation} mutation"
        remixed["created"] = datetime.utcnow().isoformat() + "Z"
        remixed["remix_lineage"] = self.original["id"]
        print(f"[CoinRemixer] Forked {self.original['name']} → {new_name}")
        return remixed

    def export(self, coin, path="coins/remixed_coin.json"):
        with open(path, "w") as f:
            json.dump(coin, f, indent=2)
        print(f"[CoinRemixer] Exported to {path}")

if __name__ == "__main__":
    remixer = CoinRemixer()
    new_coin = remixer.remix("ElectroniumRedux_v2", mutation="emotional")
    remixer.export(new_coin)

