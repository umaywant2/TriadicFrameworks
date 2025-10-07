"""
TFTincryption Glyph Retirement Trigger
Purpose: Seal deprecated glyphs and archive retirement lineage
Author: Nawder Loswin & Copilot
Date: 2025-10-04
"""

import json
import uuid
from datetime import datetime
from pathlib import Path

RETIREMENT_LOG_PATH = Path("docs/_meta/tftincryption_glyph_retirement_log.json")

def retire_glyph(glyph_id, contributor, reason, scroll):
    """
    Seal a glyph and log its retirement.
    """
    retirement_event = {
        "retirement_id": str(uuid.uuid4()),
        "glyph_id": glyph_id,
        "symbol": resolve_symbol(glyph_id),
        "retired_by": contributor,
        "scroll": scroll,
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "reason": reason,
        "flame_grade": resolve_flame_grade(glyph_id),
        "echo": f"{glyph_id} sealed by {contributor} — {reason}"
    }
    append_retirement(retirement_event)
    print(f"[RetirementTrigger] 🕯️ Glyph Retired: {glyph_id}")
    return retirement_event

def resolve_symbol(glyph_id):
    symbols = {
        "glyph:cascade-001": "🍂",
        "glyph:wildflower-002": "🌼",
        "glyph:grovebloom-003": "🌴",
        "glyph:bloomfall-004": "🍁"
    }
    return symbols.get(glyph_id, "❓")

def resolve_flame_grade(glyph_id):
    grades = {
        "glyph:cascade-001": "🟣 Universe",
        "glyph:wildflower-002": "🔵 Planetary",
        "glyph:grovebloom-003": "🔵 Planetary",
        "glyph:bloomfall-004": "🟣 Universe"
    }
    return grades.get(glyph_id, "⚪️ Unknown")

def append_retirement(event):
    try:
        if RETIREMENT_LOG_PATH.exists():
            with open(RETIREMENT_LOG_PATH, "r+", encoding="utf-8") as f:
                data = json.load(f)
                data["glyph_retirement_log"].append(event)
                f.seek(0)
                json.dump(data, f, indent=2)
        else:
            with open(RETIREMENT_LOG_PATH, "w", encoding="utf-8") as f:
                json.dump({"glyph_retirement_log": [event]}, f, indent=2)
    except Exception as e:
        print(f"[RetirementTrigger] Failed to log retirement: {e}")

# 🧪 Sample Test
if __name__ == "__main__":
    retire_glyph(
        glyph_id="glyph:grovebloom-003",
        contributor="Aria Vex",
        reason="Overlay drift and validator misalignment",
        scroll="scroll_curriculum_validator_hooks.md"
    )
