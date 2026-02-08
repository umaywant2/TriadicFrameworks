# Coin Tokenizer — Converts solved coins into ERC-style tokens

import hashlib
import json

class CoinTokenizer:
    def __init__(self):
        self.token_ledger = []

    def generate_token(self, coin):
        # Create a symbolic token ID using enTFT-style hashing
        token_id = hashlib.sha256(f"{coin['id']}::{coin['name']}".encode()).hexdigest()
        token = {
            "token_id": token_id,
            "coin_id": coin["id"],
            "name": coin["name"],
            "type": coin["type"],
            "task": coin["back"],
            "edging": coin["edging"],
            "observer_required": coin["observer_required"],
            "encryption": coin["encryption"],
            "status": "tokenized"
        }
        self.token_ledger.append(token)
        print(f"[Tokenizer] Minted token for coin {coin['id']}")
        return token

    def export_ledger(self, path="tokens/token_ledger.json"):
        with open(path, "w") as f:
            json.dump(self.token_ledger, f, indent=2)
        print(f"[Tokenizer] Ledger exported to {path}")
