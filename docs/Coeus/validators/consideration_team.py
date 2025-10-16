# Consideration Team — Reviews remix requests and coin ethics

import json
from datetime import datetime

class ConsiderationTeam:
    def __init__(self, queue_path="validators/pending_remix.json"):
        with open(queue_path, "r") as f:
            self.queue = json.load(f)

    def review(self, remix_id):
        remix = next((r for r in self.queue if r["id"] == remix_id), None)
        if not remix:
            print(f"[ConsiderationTeam] Remix {remix_id} not found.")
            return None

        print(f"[ConsiderationTeam] Reviewing remix: {remix['name']}")
        return remix

    def approve(self, remix_id):
        remix = self.review(remix_id)
        if remix:
            remix["status"] = "approved"
            remix["approved_at"] = datetime.utcnow().isoformat() + "Z"
            print(f"[ConsiderationTeam] Approved remix {remix_id}")

    def flag(self, remix_id, reason):
        remix = self.review(remix_id)
        if remix:
            remix["status"] = "flagged"
            remix["flag_reason"] = reason
            remix["flagged_at"] = datetime.utcnow().isoformat() + "Z"
            print(f"[ConsiderationTeam] Flagged remix {remix_id} → {reason}")

    def export(self, path="validators/pending_remix.json"):
        with open(path, "w") as f:
            json.dump(self.queue, f, indent=2)
        print(f"[ConsiderationTeam] Exported queue to {path}")

