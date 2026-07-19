# Sandbox Metrics — Logs coin resolution stats for tournaments and dashboards

import time
import json

class SandboxMetrics:
    def __init__(self):
        self.metrics = []

    def log_resolution(self, coin_id, agent_name, outcome):
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
        entry = {
            "coin_id": coin_id,
            "agent": agent_name,
            "outcome": outcome,
            "resonant_timestamp": timestamp
        }
        self.metrics.append(entry)
        print(f"[Metrics] Logged resolution for {coin_id} by {agent_name}")

    def export_metrics(self, path="sandbox/metrics.json"):
        with open(path, "w") as f:
            json.dump(self.metrics, f, indent=2)
        print(f"[Metrics] Exported to {path}")

