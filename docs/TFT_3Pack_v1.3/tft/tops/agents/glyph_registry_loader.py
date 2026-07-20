"""
entft Glyph Registry Loader
Purpose: Load and validate glyph references from canonical registry
Author: Nawder Loswin & Copilot
Date: 2025-10-04
"""

import json
from pathlib import Path

# 🔗 Registry Path
GLYPH_REGISTRY_PATH = Path("docs/_meta/entft_scroll_glyph_reference.md")

# 🧠 Canonical Glyphs (fallback if registry not parsed)
CANONICAL_GLYPHS = {
    "glyph:cascade-001": "🍂 Cascade",
    "glyph:wildflower-002": "🌼 Wildflower",
    "glyph:grovebloom-003": "🌴 Grove Bloom",
    "glyph:bloomfall-004": "🍁 Bloomfall"
}

def load_glyph_registry():
    """
    Parses glyph reference scroll and returns structured glyph metadata.
    """
    glyphs = {}
    try:
        with open(GLYPH_REGISTRY_PATH, "r", encoding="utf-8") as f:
            lines = f.readlines()
            for line in lines:
                if line.startswith("| ") and "glyph:" in line:
                    parts = line.strip().split("|")
                    glyph_id = parts[2].strip()
                    symbol = parts[1].strip()
                    role = parts[3].strip()
                    modules = parts[4].strip()
                    degree = parts[5].strip()
                    contributor = parts[6].strip()
                    glyphs[glyph_id] = {
                        "symbol": symbol,
                        "role": role,
                        "modules": modules,
                        "degree": degree,
                        "contributor": contributor
                    }
    except Exception as e:
        print(f"[GlyphLoader] Failed to load registry: {e}")
        glyphs = CANONICAL_GLYPHS
    return glyphs

def validate_glyph(glyph_id):
    """
    Validates glyph ID against registry.
    """
    registry = load_glyph_registry()
    return glyph_id in registry

if __name__ == "__main__":
    registry = load_glyph_registry()
    for gid, meta in registry.items():
        print(f"{gid}: {meta['symbol']} used in {meta['modules']} by {meta['contributor']}")
