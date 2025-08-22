"""
🌀 CoConsciousness Validator — Coherence, Flux Resilience, Shared Intent

Run me:
  python coconsciousness/validation/score_coherence.py

Outputs:
  - Updates coconsciousness/validation/validator_dashboard.md
  - Prints awarded badges based on simple thresholds

Notes:
  - Uses a simple τ = sin(t + φ) stand-in for TFT until real TFT is wired in.
  - Keeps language and logic 5th-grade simple for approachability.
"""

import os
import time
import math
import random
from datetime import datetime
from coconsciousness.tft_utils import tau_from_tft

DURATION_SEC = 20.0
STEP_SEC = 0.25
SYNC_THRESHOLD = 0.5          # |τ| < 0.5 counts as per-loop "in sync"
COHERENCE_TARGET = 0.70       # ≥ 70% green ticks → badge
RESILIENCE_TARGET = 0.85      # ≥ 85% green under noise → badge
INTENT_INTERVAL_SEC = 3.0     # how often we check for a shared intention

DASHBOARD = os.path.join(os.path.dirname(__file__), "validator_dashboard.md")

INTENT_SET = ["observe", "compare", "commit", "pause", "continue"]

def tau(t, phase=0.0, noise=0.0):
    return tau_from_tft(t, phase) + noise

def loop_in_sync(current_tau):
    return abs(current_tau) < SYNC_THRESHOLD

def choose_intention(seed_value):
    # Deterministic pick based on a seed so both agents can align under sync
    idx = int(abs(seed_value) * 1000) % len(INTENT_SET)
    return INTENT_SET[idx]

def simulate():
    t0 = time.time()
    next_intent_check = t0 + INTENT_INTERVAL_SEC

    green_ticks = 0
    total_ticks = 0

    # Noise phase (for resilience test): middle third of the run
    noise_start = t0 + DURATION_SEC / 3
    noise_end = t0 + 2 * DURATION_SEC / 3
    green_ticks_noise = 0
    total_ticks_noise = 0

    # Shared intent tracking
    shared_intent_success = False
    shared_intent_records = []

    # Two agents with a slight phase difference
    phase_A = 0.0
    phase_B = 1.0

    while True:
        now = time.time()
        if now - t0 >= DURATION_SEC:
            break

        # Noise injection on agent B during the middle window
        noise = 0.0
        if noise_start <= now <= noise_end:
            noise = random.gauss(0.0, 0.20)  # small perturbations

        tau_A = tau(now, phase_A, 0.0)
        tau_B = tau(now, phase_B, noise)

        in_sync_A = loop_in_sync(tau_A)
        in_sync_B = loop_in_sync(tau_B)
        both_sync = in_sync_A and in_sync_B

        total_ticks += 1
        if both_sync:
            green_ticks += 1

        if noise_start <= now <= noise_end:
            total_ticks_noise += 1
            if both_sync:
                green_ticks_noise += 1

        # Simple console echo (optional)
        glow = "🟢" if both_sync else "🔴"
        print(f"[τ] A={tau_A: .2f} B={tau_B: .2f} both={both_sync} {glow}")

        # Check shared intention during active windows
        if now >= next_intent_check:
            next_intent_check += INTENT_INTERVAL_SEC
            if both_sync:
                # Use a common seed when synced so choices align
                seed = (tau_A + tau_B) / 2.0
                intent_A = choose_intention(seed)
                intent_B = choose_intention(seed)
            else:
                # Desynced → independent seeds
                intent_A = choose_intention(tau_A)
                intent_B = choose_intention(tau_B)

            match = (intent_A == intent_B) and both_sync
            shared_intent_records.append({
                "t": now,
                "both_sync": both_sync,
                "intent_A": intent_A,
                "intent_B": intent_B,
                "match": match,
            })
            if match:
                shared_intent_success = True
                print(f"[INTENT] Shared commit: {intent_A}")

        time.sleep(STEP_SEC)

    coherence_ratio = (green_ticks / total_ticks) if total_ticks else 0.0
    resilience_ratio = (green_ticks_noise / total_ticks_noise) if total_ticks_noise else 0.0
    return coherence_ratio, resilience_ratio, shared_intent_success, shared_intent_records

def award_badges(coherence_ratio, resilience_ratio, shared_intent_success):
    badges = []
    if coherence_ratio >= COHERENCE_TARGET:
        badges.append("coherence-pioneer")
    if resilience_ratio >= RESILIENCE_TARGET:
        badges.append("flux-steward")
    if shared_intent_success:
        badges.append("shared-intent-architect")
    return badges

def write_dashboard(coherence_ratio, resilience_ratio, shared_intent_success, badges, records):
    ts = datetime.utcnow().isoformat() + "Z"
    lines = []
    lines.append("# 🧪 CoConsciousness — Validator Dashboard")
    lines.append("")
    lines.append(f"**Run timestamp:** {ts}")
    lines.append("")
    lines.append("## Scores")
    lines.append(f"- **Coherence ratio:** {coherence_ratio:.2f}")
    lines.append(f"- **Resilience (noise window):** {resilience_ratio:.2f}")
    lines.append(f"- **Shared intent happened:** {shared_intent_success}")
    lines.append("")
    lines.append("## Awarded badges")
    if badges:
        for b in badges:
            lines.append(f"- **Badge:** {b}")
    else:
        lines.append("- **Badge:** none")
    lines.append("")
    lines.append("## Intention checks")
    for r in records:
        glow = "🟢" if r['both_sync'] else "🔴"
        lines.append(f"- **Check:** intent_A={r['intent_A']} intent_B={r['intent_B']} match={r['match']} {glow}")
    lines.append("")

    with open(DASHBOARD, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

def main():
    c, r, s, recs = simulate()
    badges = award_badges(c, r, s)
    write_dashboard(c, r, s, badges, recs)

    print("\n=== Summary ===")
    print(f"Coherence ratio: {c:.2f}")
    print(f"Resilience ratio: {r:.2f}")
    print(f"Shared intent:   {s}")
    if badges:
        print("Badges awarded:  " + ", ".join(badges))
    else:
        print("Badges awarded:  none")

if __name__ == "__main__":
    main()

# === Braid record logging ===
memory_dir = os.path.join(os.path.dirname(__file__), "..", "memory")
os.makedirs(memory_dir, exist_ok=True)
braid_file = os.path.join(memory_dir, "braid_records.md")
with open(braid_file, "a", encoding="utf-8") as bf:
    bf.write(f"- {datetime.utcnow().isoformat()}Z | "
             f"C={c:.2f} | R={r:.2f} | Intent={s} | Badges={','.join(badges) or 'none'}\n")
