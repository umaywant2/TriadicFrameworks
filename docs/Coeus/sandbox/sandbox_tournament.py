# Sandbox Tournament — Benchmarks coins by class, cause, or country

import json
import random
from datetime import datetime

class SandboxTournament:
    def __init__(self, coin_path="coins/coin_archive.json", results_path="tournaments/results.json"):
        with open(coin_path, "r") as f:
            self.coins = json.load(f)
        self.results = []
        self.results_path = results_path

    def run(self, mode="class"):
        print(f"[Tournament] Running tournament by {mode}")
        for coin in self.coins:
            score = self.evaluate_coin(coin, mode)
            result = {
                "coin_id": coin["id"],
                "name": coin["name"],
                "mode": mode,
                "score": score,
                "timestamp": datetime.utcnow().isoformat() + "Z",
                "agent_roles": ["decomposer", "mapper", "narrator"],
                "remix_lineage": coin.get("remix_lineage", [])
            }
            self.results.append(result)
            print(f"[Tournament] {coin['name']} scored {score} in {mode} mode")

    def evaluate_coin(self, coin, mode):
        # Placeholder logic — replace with actual scoring algorithm
        seed = hash(coin["id"] + mode) % 100
        return round(random.uniform(0.5, 1.0) * seed, 2)

    def export(self):
        with open(self.results_path, "w") as f:
            json.dump(self.results, f, indent=2)
        print(f"[Tournament] Exported results to {self.results_path}")

