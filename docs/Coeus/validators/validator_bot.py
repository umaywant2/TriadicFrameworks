# Validator Bot — Enforces ethics, audits remix lineage, and approves coin/token status

import json
from datetime import datetime

class ValidatorBot:
    def __init__(self, archive_path="coins/coin_archive.json", ledger_path="tokens/token_ledger.json"):
        with open(archive_path, "r") as f:
            self.coins = json.load(f)
        with open(ledger_path, "r") as f:
            self.tokens = json.load(f)

    def audit_coin(self, coin_id):
        coin = next((c for c in self.coins if c["id"] == coin_id), None)
        if not coin:
            print(f"[ValidatorBot] Coin {coin_id} not found.")
            return None

        lineage_ok = self.validate_lineage(coin)
        ethics_ok = self.validate_ethics(coin)

        print(f"[ValidatorBot] Audit for {coin['name']} → Ethics: {ethics_ok} | Lineage: {lineage_ok}")
        return ethics_ok and lineage_ok

    def validate_lineage(self, coin):
        lineage = coin.get("remix_lineage", [])
        return all(parent_id in [c["id"] for c in self.coins] for parent_id in lineage)

    def validate_ethics(self, coin):
        # Basic ethics check: must include glyph and validated status
        return coin.get("glyph") is not None and coin.get("status") in ["validated", "approved"]

    def approve_token(self, token_id):
        token = next((t for t in self.tokens if t["token_id"] == token_id), None)
        if not token:
            print(f"[ValidatorBot] Token {token_id} not found.")
            return

        token["status"] = "approved"
        token["approved_at"] = datetime.utcnow().isoformat() + "Z"
        print(f"[ValidatorBot] Token {token_id} approved.")

    def export(self, archive_path="coins/coin_archive.json", ledger_path="tokens/token_ledger.json"):
        with open(archive_path, "w") as f:
            json.dump(self.coins, f, indent=2)
        with open(ledger_path, "w") as f:
            json.dump(self.tokens, f, indent=2)
        print(f"[ValidatorBot] Exported updated coin and token data.")

