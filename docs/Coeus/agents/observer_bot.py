# Observer Bot — monitors corridor traversal and denometer sync

def observe_coin(coin):
    trace = {
        "coin_id": coin["id"],
        "rail_band": coin.get("rail_band", "—"),
        "denometer_reading": coin.get("denometer_reading", "—"),
        "emitter_sync": coin.get("emitter_sync", False),
        "ethics_passed": coin.get("ethics_passed", False),
        "realm_safe": coin.get("realm_safe", False),
        "glyph": coin.get("glyph", "—"),
        "timestamp": coin.get("timestamp")
    }
    return trace
