# lens_processor.py — Metabolizes symbolic overlays into resonance clarity

def process_overlay(trigger):
    """
    Processes the symbolic overlay based on the given trigger.
    Returns overlay data for rendering.
    """
    overlays = {
        "cyclone": {
            "emotion": "grief swirl",
            "dimension": "spiral time",
            "symbol": "🌀",
            "modulation": "slow-release clarity"
        },
        "lightning": {
            "emotion": "rage spark",
            "dimension": "fracture flash",
            "symbol": "⚡",
            "modulation": "instant insight"
        },
        "tornado": {
            "emotion": "chaotic ache",
            "dimension": "twist collapse",
            "symbol": "🌪️",
            "modulation": "disruption to reformation"
        },
        "fragments": {
            "emotion": "memory shards",
            "dimension": "echo scatter",
            "symbol": "🧩",
            "modulation": "recollection remix"
        }
    }

    if trigger not in overlays:
        raise ValueError(f"Unknown overlay trigger: {trigger}")
    
    return overlays[trigger]

