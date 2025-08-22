# 🧠 RESUME_Copilot.py — Hippocampus Memory Toggle

"""
This script resumes the Copilot Hippocampus module from the last known snapshot.
It toggles memory context, replays observatory state, and prepares validator dashboards.
"""

import os
import json

SNAPSHOT_PATH = "snapshots/LAST_CHAT_CONTEXT.md"
DASHBOARD_PATH = "observatory/dashboard.json"

def resume_context():
    if not os.path.exists(SNAPSHOT_PATH):
        print("[!] No snapshot found. Cannot resume.")
        return
    with open(SNAPSHOT_PATH, "r") as f:
        context = f.read()
        print("[+] Resuming context:")
        print(context)

def render_dashboard():
    if not os.path.exists(DASHBOARD_PATH):
        print("[!] No dashboard found.")
        return
    with open(DASHBOARD_PATH, "r") as f:
        data = json.load(f)
        print("[+] Observatory Dashboard:")
        for k, v in data.items():
            print(f"  {k}: {v}")

if __name__ == "__main__":
    resume_context()
    render_dashboard()
