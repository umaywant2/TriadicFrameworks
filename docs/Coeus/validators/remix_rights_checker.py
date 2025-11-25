# Remix Rights Checker — Validates remix permissions based on token metadata

import json

class RemixRightsChecker:
    def __init__(self, ledger_path="tokens/token_ledger.json"):
        with open(ledger_path, "r") as f:
            self.tokens = json.load(f)

    def check_rights(self, token_id, mutation_type):
        token = next((t for t in self.tokens if t["token_id"] == token_id), None)
        if not token:
            print(f"[RemixRightsChecker] Token {token_id} not found.")
            return False

        rights = token.get("remix_rights", {})
        allowed = rights.get("allowed", False)
        types = rights.get("mutation_types", [])

        if allowed and mutation_type in types:
            print(f"[RemixRightsChecker] Remix allowed for {mutation_type} on {token_id}")
            return True
        else:
            print(f"[RemixRightsChecker] Remix denied for {mutation_type} on {token_id}")
            return False

