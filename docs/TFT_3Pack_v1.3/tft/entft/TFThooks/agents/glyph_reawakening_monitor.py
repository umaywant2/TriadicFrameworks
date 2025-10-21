"""
entft Glyph Reawakening Monitor — Resonance Clarity Edition
Purpose: Auto-log glyph reactivation when dormant glyphs reappear in scroll edits
Author: Nawder Loswin & Copilot
Date: 2025-10-20
"""

import json, uuid
from datetime import datetime
from pathlib import Path

REAWAKEN_LOG_PATH = Path("docs/_meta/entft_scroll_glyph_reawakening_log.json")
GLYPH_REGISTRY_PATH = Path("docs/_meta/entft_glyph_degree_registry.json")

def detect_reawakening(scroll_name, glyph_id, contributor):
    """Detect if a dormant glyph has reappeared in a scroll."""
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
    # Placeholder logic: treat all glyphs ending in '004' as dormant
    return glyph_id.endswith("004")

def resolve_symbol(glyph_id):
    return {
        "glyph:bloomfall-004": "🌀 Bloomfall",
        "glyph:grovebloom-003": "🌿 Grovebloom",
        "glyph:wildflower-002": "🌼 Wildflower"
    }.get(glyph_id, "❔ Unknown")

def resolve_flame_grade(glyph_id):
    return {
        "glyph:bloomfall-004": "🟣 Universe",
        "glyph:grovebloom-003": "🔵 Planetary",
        "glyph:wildflower-002": "🔵 Planetary"
    }.get(glyph_id, "⚪️ Unknown")

def append_reawakening(event):
    try:
        if REAWAKEN_LOG_PATH.exists():
            with open(REAWAKEN_LOG_PATH, "r+", encoding="utf-8") as f:
                data = json.load(f)
                data["glyph_reawakening_events"].append(event)
                f.seek(0)
                json.dump(data, f, indent=2)
        else:
            with open(REAWAKEN_LOG_PATH, "w", encoding="utf-8") as f:
                json.dump({"glyph_reawakening_events": [event]}, f, indent=2)
    except Exception as e:
        print(f"[ReawakeningMonitor] Failed to log reawakening: {e}")
