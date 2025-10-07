```python
"""
TFTincryption Glyph Reawakening Monitor
Purpose: Auto-log glyph reactivation when dormant glyphs reappear in scroll edits
Author: Nawder Loswin & Copilot
Date: 2025-10-04
"""

import json
import uuid
from datetime import datetime
from pathlib import Path

REAWAKEN_LOG_PATH = Path("docs/_meta/tftincryption_scroll_glyph_reawakening_log.json")
GLYPH_REGISTRY_PATH = Path("docs/_meta/tftincryption_glyph_degree_registry.json")

def detect_reawakening(scroll_name, glyph_id, contributor):
    """
    Detect if a dormant glyph has reappeared in a scroll.
    """
    if is_dormant(glyph_id):
        event = {
            "reawakening_id": str(uuid.uuid4()),
            "glyph_id": glyph_id,
            "symbol": resolve_symbol(glyph_id),
            "reawakened_by": contributor,
            "scroll": scroll_name,
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "reason": f"{glyph_id} reactivated in {scroll_name} by {contributor}",
            "flame_grade": resolve_flame_grade(glyph_id)
        }
        append_reawakening(event)
        print(f"[ReawakeningMonitor] 🌅 Glyph Reawakened: {glyph_id}")
        return event
    return None

def is_dormant(glyph_id):
    try:
        with open(GLYPH_REGISTRY_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)["glyph_degrees"]
            for glyph in data:
                if glyph["glyph_id"] == glyph_id:
                    return len(glyph["modules_used"]) <= 1
    except Exception:
        return False
    return False

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

def append_reawakening(event):
    try:
        if REAWAKEN_LOG_PATH.exists():
            with open(REAWAKEN_LOG_PATH, "r+", encoding="utf-8") as f:
                data = json.load(f)
                data["glyph_reawakening_log"].append(event)
                f.seek(0)
                json.dump(data, f, indent=2)
        else:
            with open(REAWAKEN_LOG_PATH, "w", encoding="utf-8") as f:
                json.dump({"glyph_reawakening_log": [event]}, f, indent=2)
    except Exception as e:
        print(f"[ReawakeningMonitor] Failed to log reawakening: {e}")

# 🧪 Sample Test
if __name__ == "__main__":
    detect_reawakening(
        scroll_name="scroll_codex.md",
        glyph_id="glyph:cascade-001",
        contributor="Nawder Loswin"
    )
