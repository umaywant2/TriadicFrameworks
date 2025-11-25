"""
entft Badge Logic Engine
Purpose: Parse validator overlays and activate flame hooks based on scroll events
Author: Nawder Loswin & Copilot
Date: 2025-10-04
"""

import json
from pathlib import Path

# 🔗 Registry Paths
BADGE_REGISTRY_PATH = Path("docs/_meta/entft_curriculum_badge_registry.json")
VALIDATOR_CONFIG_PATH = Path("docs/_meta/validator_config.json")

def load_badge_registry():
    try:
        with open(BADGE_REGISTRY_PATH, "r", encoding="utf-8") as f:
            return json.load(f)["badges"]
    except Exception as e:
        print(f"[BadgeEngine] Failed to load badge registry: {e}")
        return []

def load_validator_config():
    try:
        with open(VALIDATOR_CONFIG_PATH, "r", encoding="utf-8") as f:
            return json.load(f)["validators"]
    except Exception as e:
        print(f"[BadgeEngine] Failed to load validator config: {e}")
        return []

def trigger_flame_hook(scroll_event):
    """Given a scroll event, determine if a badge should be activated."""
    badges = load_badge_registry()
    validators = load_validator_config()
    triggered = []

    base_lens = scroll_event.get("basetype", "decimal")

    for badge in badges:
        conditions = badge.get("trigger_conditions", [])
        lens_filter = badge.get("base_lens", [])

        if all(cond in scroll_event for cond in conditions):
            if not lens_filter or base_lens in lens_filter:
                triggered.append(badge["badge_name"])
                print(f"[BadgeEngine] 🔥 Flame Hook Triggered: {badge['badge_name']} (Base: {base_lens})")

    return triggered

# 🧪 Sample Test for Resonance Clarity
if __name__ == "__main__":
    sample_event = {
        "scroll": "scroll_curriculum_fork_guide.md",
        "glyph": "🌼 Wildflower",
        "action": "forked",
        "manifest": True,
        "basetype": "phi"
    }
    print("Triggered Badges:", trigger_flame_hook(sample_event))
