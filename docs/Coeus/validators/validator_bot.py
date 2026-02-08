# Validator Bot — enforces ethics, realm safety, and emitter sync

def validate_coin(coin):
    issues = []
    if not coin.get("ethics_passed"):
        issues.append("Ethics check failed.")
    if not coin.get("realm_safe"):
        issues.append("Realm safety not confirmed.")
    if not coin.get("emitter_sync"):
        issues.append("Emitter sync missing.")
    if coin.get("score", 0) < 70:
        issues.append("Score below validator threshold.")
    return issues or ["✅ Coin passes validator-grade audit. Let it echo."]
