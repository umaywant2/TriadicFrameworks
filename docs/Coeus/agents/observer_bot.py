# Observer Bot — Monitors coin resolution, ethics compliance, and D-realm traversal

import json
from datetime import datetime

class ObserverBot:
    def __init__(self, trace_path="sandbox/logs/observer_trace.json"):
        self.trace_log = []
        self.path = trace_path

    def observe(self, coin_id, agent_roles, rail_band, emitter_sync):
        entry = {
            "coin_id": coin_id,
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "agent_roles": agent_roles,
            "rail_band": rail_band,
            "emitter_sync": emitter_sync,
            "ethics_passed": self.validate_ethics(agent_roles, rail_band),
            "realm_safe": self.validate_realm(rail_band)
        }
        self.trace_log.append(entry)
        print(f"[ObserverBot] Observed coin {coin_id} — Ethics: {entry['ethics_passed']} | Realm: {entry['realm_safe']}")

    def validate_ethics(self, agent_roles, rail_band):
        # Basic ethics check: must include decomposer and narrator, and rail must be within D3/D4
        required_roles = {"decomposer", "narrator"}
        return required_roles.issubset(set(agent_roles)) and rail_band in ["D3", "D4"]

    def validate_realm(self, rail_band):
        # Only D3 and D4 are safe for traversal
        return rail_band in ["D3", "D4"]

    def export(self):
        with open(self.path, "w") as f:
            json.dump(self.trace_log, f, indent=2)
        print(f"[ObserverBot] Exported trace log to {self.path}")

