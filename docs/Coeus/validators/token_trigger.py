# Token Trigger — checks if coin meets minting criteria

def is_mint_ready(coin):
    if not coin.get("ethics_passed"):
        return False, "Ethics check failed."
    if not coin.get("realm_safe"):
        return False, "Realm safety not confirmed."
    if not coin.get("emitter_sync"):
        return False, "Emitter sync missing."
    if coin.get("score", 0) < 80:
        return False, "Score below mint threshold."
    if not coin.get("remix_lineage") and coin.get("mutation_type"):
        return False, "Mutation declared but lineage missing."
    return True, "✅ Coin is mint-ready. Let it echo."
