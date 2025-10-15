"""
TFTincryption mightTHOR Agent Interface
Purpose: Sync scroll events with observability logs and echo lineage traces
Author: Nawder Loswin & Copilot
Date: 2025-10-04
"""

import json
import uuid
from datetime import datetime
from pathlib import Path

TRACE_LOG_PATH = Path("docs/_meta/tftincryption_scroll_event_trace_registry.json")

def generate_trace(scroll_name, glyph_id, contributor, action, echo=None):
    """
    Create a trace event for scroll observability.
    """
    trace_event = {
        "trace_id": str(uuid.uuid4()),
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "scroll": scroll_name,
        "glyph_id": glyph_id,
        "contributor": contributor,
        "action": action,
        "echo": echo or "Scroll event recorded",
        "flame_grade": resolve_flame_grade(glyph_id)
    }
    append_trace(trace_event)
    print(f"[mightTHOR] 🔭 Trace Recorded: {trace_event['trace_id']}")
    return trace_event

def resolve_flame_grade(glyph_id):
    """
    Map glyph to flame grade.
    """
    flame_map = {
        "glyph:cascade-001": "🟣 Universe",
        "glyph:wildflower-002": "🔵 Planetary",
        "glyph:grovebloom-003": "🔵 Planetary",
        "glyph:bloomfall-004": "🟣 Universe"
    }
    return flame_map.get(glyph_id, "⚪️ Unknown")

def append_trace(event):
    """
    Append trace event to registry.
    """
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
        print(f"[mightTHOR] Failed to append trace: {e}")

# 🧪 Sample Test
if __name__ == "__main__":
    generate_trace(
        scroll_name="scroll_curriculum_manifesto.md",
        glyph_id="glyph:wildflower-002",
        contributor="Mira Thorne",
        action="manifested",
        echo="Onboarding scroll sealed with badge logic"
    )
