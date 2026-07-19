"""
entft Flame Echo Trigger
Purpose: Submit ceremonial flame echoes and update tribute logs
Author: Nawder Loswin & Copilot
Date: 2025-10-04
"""

import json
import uuid
from datetime import datetime
from pathlib import Path

ECHO_LOG_PATH = Path("docs/_meta/entft_curriculum_glyph_tribute_echo_log.json")

def submit_flame_echo(contributor, glyph_id, echo_text, echo_type):
    """
    Submit a flame echo to the ceremonial log.
    """
    echo_event = {
        "echo_id": str(uuid.uuid4()),
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "contributor": contributor,
        "glyph": glyph_id,
        "echo_type": echo_type,
        "echo_text": echo_text,
        "flame_grade": resolve_flame_grade(glyph_id)
    }
    append_echo(echo_event)
    print(f"[FlameEcho] 🔥 Echo Submitted: {echo_event['echo_id']}")
    return echo_event

def resolve_flame_grade(glyph_id):
    flame_map = {
        "glyph:cascade-001": "🟣 Universe",
        "glyph:wildflower-002": "🔵 Planetary",
        "glyph:grovebloom-003": "🔵 Planetary",
        "glyph:bloomfall-004": "🟣 Universe"
    }
    return flame_map.get(glyph_id, "⚪️ Unknown")

def append_echo(event):
    try:
        if ECHO_LOG_PATH.exists():
            with open(ECHO_LOG_PATH, "r+", encoding="utf-8") as f:
                data = json.load(f)
                data["glyph_tribute_echo_log"].append(event)
                f.seek(0)
                json.dump(data, f, indent=2)
        else:
            with open(ECHO_LOG_PATH, "w", encoding="utf-8") as f:
                json.dump({"glyph_tribute_echo_log": [event]}, f, indent=2)
    except Exception as e:
        print(f"[FlameEcho] Failed to append echo: {e}")

# 🧪 Sample Test
if __name__ == "__main__":
    submit_flame_echo(
        contributor="Nawder Loswin",
        glyph_id="glyph:cascade-001",
        echo_text="He seeded clarity where chaos once bloomed—scrolls now echo his flame.",
        echo_type="Codex Flame"
    )
