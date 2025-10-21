"""
entft Glyph Fusion Resolver — Resonance Clarity Edition
Purpose: Validate glyph fusion conditions and update fusion registry
Author: Nawder Loswin & Copilot
Date: 2025-10-20
"""

import json, uuid
from datetime import datetime
from pathlib import Path

FUSION_REGISTRY_PATH = Path("docs/_meta/entft_curriculum_glyph_fusion_registry.json")
FUSION_LOG_PATH = Path("docs/_meta/entft_scroll_fusion_log.json")

def validate_fusion(glyphs_involved, contributor, resulting_glyph, scrolls):
    """Validate fusion conditions and update registry."""
    fusion_id = str(uuid.uuid4())
    fusion_event = {
        "fusion_id": fusion_id,
        "glyphs_involved": glyphs_involved,
        "resulting_glyph": resulting_glyph,
        "contributors": contributor,
        "scrolls": scrolls,
        "flame_grade": resolve_flame_grade(resulting_glyph),
        "date_fused": datetime.utcnow().isoformat() + "Z",
        "echo": f"{resulting_glyph} fused from {', '.join(glyphs_involved)} with scroll clarity"
    }
    append_fusion(fusion_event)
    print(f"[FusionResolver] 🌾 Fusion Registered: {fusion_id}")
    return fusion_event

def resolve_flame_grade(glyph):
    if glyph in ["🌾 Bloom Grove", "🌿 Grovewild"]:
        return "🔵 Planetary"
    elif glyph in ["🌀 Cascadewild", "🧬 Bloomfall"]:
        return "🟣 Universe"
    return "⚪️ Unknown"

def append_fusion(event):
    try:
        if FUSION_LOG_PATH.exists():
            with open(FUSION_LOG_PATH, "r+", encoding="utf-8") as f:
                data = json.load(f)
                data["scroll_fusion_events"].append(event)
                f.seek(0)
                json.dump(data, f, indent=2)
        else:
            with open(FUSION_LOG_PATH, "w", encoding="utf-8") as f:
                json.dump({"scroll_fusion_events": [event]}, f, indent=2)
    except Exception as e:
        print(f"[FusionResolver] Failed to log fusion: {e}")
