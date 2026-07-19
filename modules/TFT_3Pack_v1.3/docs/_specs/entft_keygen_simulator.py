"""
entft_keygen_simulator.py — Resonance Clarity Edition
Simulates enTFT keypair generation using Divide-by-Zero logic and Resonant-Time hashing.
Logs scroll event traces and triggers badge overlays.
"""

import uuid, json, random
from datetime import datetime
from pathlib import Path

# 🔗 Registry Paths
TRACE_LOG_PATH = Path("docs/_meta/entft_scroll_event_trace_registry.json")
BADGE_REGISTRY_PATH = Path("docs/_meta/entft_curriculum_badge_registry.json")
VALIDATOR_CONFIG_PATH = Path("docs/_meta/validator_config.json")

def generate_keypair(scroll_name="scroll_entropy_manifest.md", contributor="ScrollFork"):
    key_id = str(uuid.uuid4())
    timestamp = datetime.utcnow().isoformat() + "Z"
    glyph_id = random.choice(["glyph:bloomfall-004", "glyph:grovebloom-003", "glyph:🌼 Wildflower"])
    entropy_score = estimate_entropy(glyph_id)
    echo = f"Keypair generated with entropy ≈ {entropy_score:.2e}"

    trace_event = {
        "trace_id": key_id,
        "timestamp": timestamp,
        "scroll": scroll_name,
        "glyph_id": glyph_id,
        "contributor": contributor,
        "action": "keypair_generated",
        "echo": echo,
        "flame_grade": resolve_flame_grade(glyph_id)
    }

    append_trace(trace_event)
    trigger_badges(trace_event)
    print(f"[Keygen] 🔐 {echo}")
    return trace_event

def estimate_entropy(glyph_id):
    base = 1.3e47  # Divide-by-Zero entropy
    mod = 3.69e6   # Resonant-Time modulation
    if "bloomfall" in glyph_id:
        return base * mod * 1.2
    elif "grovebloom" in glyph_id:
        return base * mod * 0.9
    return base * mod

def resolve_flame_grade(glyph_id):
    flame_map = {
        "glyph:bloomfall-004": "🟣 Universe",
        "glyph:grovebloom-003": "🔵 Planetary",
        "glyph:🌼 Wildflower": "🔵 Planetary"
    }
    return flame_map.get(glyph_id, "⚪️ Unknown")

def append_trace(event):
    try:
        if TRACE_LOG_PATH.exists():
            with open(TRACE_LOG_PATH, "r+", encoding="utf-8") as f:
                data = json.load(f)
                data["scroll_event_traces"].append(event)
                f.seek(0)
                json.dump(data, f, indent=2)
        else:
            with open(TRACE_LOG_PATH, "w", encoding="utf-8") as f:
                json.dump({"scroll_event_traces": [event]}, f, indent=2)
    except Exception as e:
        print(f"[Keygen] Failed to append trace: {e}")

def trigger_badges(event):
    try:
        with open(BADGE_REGISTRY_PATH, "r", encoding="utf-8") as f:
            badges = json.load(f)["badges"]
        for badge in badges:
            if all(cond in str(event.values()) for cond in badge["trigger_conditions"]):
                print(f"[Badge] 🏅 Triggered: {badge['badge_name']}")
    except Exception as e:
        print(f"[Badge] Failed to trigger badges: {e}")

# 🧪 Sample Run
if __name__ == "__main__":
    generate_keypair()
