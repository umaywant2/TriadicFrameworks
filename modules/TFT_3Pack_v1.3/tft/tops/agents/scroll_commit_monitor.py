"""
entft Scroll Commit Monitor
Purpose: Watch scroll directories for updates and auto-trigger flame hooks
Author: Nawder Loswin & Copilot
Date: 2025-10-04
"""

import os
import time
import hashlib
from pathlib import Path
from badge_logic_engine import trigger_flame_hook
from mightthor_agent_interface import generate_trace

# 🔍 Watch Path
SCROLL_DIR = Path("docs/_rituals")

# 🧠 Track File Hashes
file_hashes = {}

def hash_file(path):
    try:
        with open(path, "rb") as f:
            return hashlib.md5(f.read()).hexdigest()
    except Exception:
        return None

def monitor_scrolls(interval=10):
    print("[ScrollMonitor] 🔁 Monitoring scroll commits...")
    while True:
        for scroll in SCROLL_DIR.glob("*.md"):
            current_hash = hash_file(scroll)
            if scroll.name not in file_hashes:
                file_hashes[scroll.name] = current_hash
            elif file_hashes[scroll.name] != current_hash:
                print(f"[ScrollMonitor] ✏️ Scroll Updated: {scroll.name}")
                file_hashes[scroll.name] = current_hash
                flame_event = {
                    "scroll": scroll.name,
                    "glyph": extract_glyph(scroll.name),
                    "action": "updated",
                    "manifest": True
                }
                trigger_flame_hook(flame_event)
                generate_trace(
                    scroll_name=scroll.name,
                    glyph_id=flame_event["glyph"],
                    contributor="AutoMonitor",
                    action="updated",
                    echo="Scroll updated and flame hook triggered"
                )
        time.sleep(interval)

def extract_glyph(scroll_name):
    # Simple mapping for demo purposes
    if "cascade" in scroll_name:
        return "glyph:cascade-001"
    elif "wildflower" in scroll_name:
        return "glyph:wildflower-002"
    elif "grove" in scroll_name:
        return "glyph:grovebloom-003"
    elif "bloomfall" in scroll_name:
        return "glyph:bloomfall-004"
    return "glyph:unknown"

if __name__ == "__main__":
    monitor_scrolls()
