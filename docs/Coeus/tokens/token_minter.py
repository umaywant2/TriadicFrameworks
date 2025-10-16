# Token Minter — Converts validated coins into sovereign tokens

import json
from datetime import datetime
import uuid

class TokenMinter:
    def __init__(self, coin_path="coins/coin_archive.json", token_path="tokens/token_ledger.json"):
        with open(coin_path, "r") as f:
            self.coins = json.load(f)
        with open(token_path, "r") as f:
            self.tokens = json.load(f)
        self.token_path = token_path

    def mint(self, coin_id, shares=100, remix_rights=None):
        coin = next((c for c in self.coins if c["id"] == coin_id), None)
        if not coin:
            print(f"[TokenMinter] Coin {coin_id} not found.")
            return

        if coin["status"] not in ["validated", "approved"]:
            print(f"[TokenMinter] Coin {coin_id} not eligible for tokenization.")
            return

        token = {
            "token_id": f"tkn-{str(uuid.uuid4())[:8]}",
            "coin_id": coin["id"],
            "name": coin["name"],
            "creator": coin["creator"],
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "status": "validated",
            "exchange_ready": True,
            "derivative_shares": shares,
            "glyph": coin.get("glyph", "🧠"),
            "remix_rights": remix_rights or {
                "allowed": True,
                "mutation_types": ["emotional", "dimensional"]
            }
        }

        self.tokens.append(token)
        print(f"[TokenMinter] Minted token {token['token_id']} from coin {coin['name']}")

    def export(self):
        with open(self.token_path, "w") as f:
            json.dump(self.tokens, f, indent=2)
        print(f"[TokenMinter] Exported updated token ledger to {self.token_path}")

