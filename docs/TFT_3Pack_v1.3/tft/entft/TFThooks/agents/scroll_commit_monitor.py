"""
entft Scroll Commit Monitor — Resonance Clarity Edition
Purpose: Watch scroll directories for updates and auto-trigger flame hooks
Author: Nawder Loswin & Copilot
Date: 2025-10-20
"""

import os, time, hashlib
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
                trigger_flame_hook(scroll.name)
                generate_trace(scroll.name)
                file_hashes[scroll.name] = current_hash
        time.sleep(interval)
