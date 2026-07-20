from validators.token_trigger import is_mint_ready

class TokenMinter:
    def __init__(self, ledger_path="tokens/token_ledger.json"):
        with open(ledger_path, "r") as f:
            self.ledger = json.load(f)
        self.ledger_path = ledger_path

    def mint_token(self, coin, minted_by="professor_bot"):
        ready, message = is_mint_ready(coin)
        if not ready:
            print(f"[TokenMinter] Mint failed: {message}")
            return

        token = {
            "token_id": f"tok-{coin['id'][:8]}",
            "name": coin["name"],
            "glyph": coin["glyph"],
            "score": coin["score"],
            "class": coin["class"],
            "cause": coin["cause"],
            "remix_lineage": coin["remix_lineage"],
            "minted_by": minted_by,
            "timestamp": datetime.utcnow().isoformat() + "Z"
        }
        self.ledger.append(token)
        print(f"[TokenMinter] Minted token: {token['name']} ({token['token_id']})")

    def export(self):
        with open(self.ledger_path, "w") as f:
            json.dump(self.ledger, f, indent=2)
        print(f"[TokenMinter] Exported updated token ledger to {self.ledger_path}")
