"""
🧶 CoConsciousness — Braid Timeline Visualiser

Reads memory/braid_records.md and shows:
- Chronological run history
- Coherence and Resilience trends
- Badges earned over time

Keeps code simple so devs can hack visuals as they like.
"""

import os
from datetime import datetime
import matplotlib.pyplot as plt

BRAID_FILE = os.path.join(os.path.dirname(__file__), "..", "memory", "braid_records.md")

def parse_braid_records():
    records = []
    if not os.path.exists(BRAID_FILE):
        return records
    with open(BRAID_FILE, "r", encoding="utf-8") as f:
        for line in f:
            if not line.startswith("- "):
                continue
            try:
                parts = line.strip("- \n").split("|")
                ts = datetime.fromisoformat(parts[0].strip().rstrip("Z"))
                c = float(parts[1].strip().split("=")[1])
                r = float(parts[2].strip().split("=")[1])
                intent = parts[3].strip().split("=")[1]
                badges = [b.strip() for b in parts[4].strip().split("=")[1].split(",")]
                records.append({"ts": ts, "C": c, "R": r, "intent": intent, "badges": badges})
            except Exception as e:
                print(f"[!] Could not parse line: {line.strip()} ({e})")
    return records

def plot_timeline(records):
    if not records:
        print("No braid records to plot.")
        return
    
    times = [rec["ts"] for rec in records]
    coherence_vals = [rec["C"] for rec in records]
    resilience_vals = [rec["R"] for rec in records]

    plt.figure(figsize=(10, 5))
    plt.plot(times, coherence_vals, marker="o", label="Coherence %")
    plt.plot(times, resilience_vals, marker="s", label="Resilience %", alpha=0.7)
    plt.axhline(0.70, color="green", linestyle="--", alpha=0.5, label="Coherence target")
    plt.axhline(0.85, color="blue", linestyle="--", alpha=0.5, label="Resilience target")

    plt.title("🧶 CoConsciousness — Braid Timeline")
    plt.xlabel("Run timestamp")
    plt.ylabel("Score")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    data = parse_braid_records()
    plot_timeline(data)
