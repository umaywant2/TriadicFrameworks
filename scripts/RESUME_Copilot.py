#!/usr/bin/env python3
"""
RESUME_Copilot.py — Toggle script for Capture ↔ Playback,
with harmonic scoring + Active Constellation generator.
"""

from pathlib import Path
import webbrowser, json, datetime as dt, sys, yaml
from scripts.hippocampus_utils import make_triad, resonance_parity

ROOT = Path(__file__).resolve().parents[1]
SNAPSHOT_DIR = ROOT / "snapshots"
DATA_DIR = ROOT / "data"
SCRIPTS_DIR = ROOT / "scripts"

HOT = SNAPSHOT_DIR / "LAST_CHAT_CONTEXT.md"
HIP = DATA_DIR / "hippocampus.json"
LINEAGE = DATA_DIR / "lineage.log"
CONST = DATA_DIR / "constants.yml"

def open_and_delete(path: Path):
    webbrowser.open(path.as_uri())
    path.unlink(missing_ok=True)

def write_lineage(event, meta=None):
    LINEAGE.write_text(
        (LINEAGE.read_text() if LINEAGE.exists() else "")
        + json.dumps({"ts": dt.datetime.utcnow().isoformat()+"Z",
                      "event": event, "meta": meta or {}}, ensure_ascii=False)
        + "\n",
        encoding="utf-8"
    )

def capture_mode():
    constants = yaml.safe_load(CONST.read_text()) if CONST.exists() else {}
    anchor = input("Anchor (e.g., TFT Project 1 — Resonance tier mapping): ").strip()
    goals = [g.strip() for g in input("Goals (comma-separated): ").split(",") if g.strip()]
    today = dt.datetime.utcnow()

    # ⚠️ In real build: ingest data, embeddings, validator inputs
    triads = []
    triads.append(make_triad(
        a="OnboardingV3",
        b="ResonanceParity",
        c="ValidatorMatrix",
        roles=("goal","metric","scaffold"),
        harmonics={"similarity":0.83,"authority":0.90,"relevance":0.88,"validator":0.92},
        decay_meta={"days_since":2, "half_life_days":constants.get("half_life_days", 21)},
        provenance={"source":"md","path":"/docs/onboarding_v3.md","line":"12-58"},
        tags=["onboarding","v3"]
    ))
    triads.append(make_triad(
        a="BadgeSystem",
        b="ContributorHonorRoll",
        c="ValidatorMatrix",
        roles=("artifact","artifact","scaffold"),
        harmonics={"similarity":0.79,"authority":0.85,"relevance":0.81,"validator":0.90},
        decay_meta={"days_since":5, "half_life_days":constants.get("half_life_days", 21)},
        provenance={"source":"md","path":"/docs/badges.md","line":"3-40"},
        tags=["governance","recognition"]
    ))

    # Rank top-K
    top_k = constants.get("top_k", 7)
    triads_sorted = sorted(triads, key=lambda t: t["H"], reverse=True)[:top_k]

    # Compute parity
    parity = resonance_parity(triads_sorted, "onboarding")

    # Write hippocampus.json
    hippocampus = {
        "version":"0.1",
        "project":"TFT Project 1",
        "snapshot":{"anchor":anchor,"asks":goals,"constants":constants},
        "triads": triads_sorted
    }
    HIP.write_text(json.dumps(hippocampus, indent=2, ensure_ascii=False), encoding="utf-8")

    # Write human-readable snapshot
    md = f"""# RESUME_Copilot snapshot

**Anchor:** {anchor}  
**Asks:** {", ".join(goals) or "—"}  
**Constants:** {constants}  
**Resonance parity:** {parity}

## Active Constellation (Top-{top_k} Triads)
"""
    for t in triads_sorted:
        md += f"- **{t['id']}** — H={t['H']} — tags: {', '.join(t['tags'])}\n"

    md += f"""

**Instructions to Copilot:**  
- Apply anchor and asks.  
- Assume constants unless overridden.  
- Use Active Constellation triads as preload context.

> Provenance: {today.isoformat()}Z
"""
    SNAPSHOT_DIR.mkdir(exist_ok=True)
    HOT.write_text(md, encoding="utf-8")

    write_lineage("capture", {"anchor": anchor, "goals": goals})
    print(f"Wrote {HOT.name} and {HIP.name}")

def playback_mode():
    open_and_delete(HOT)
    write_lineage("playback_opened", {"file": str(HOT)})

def main():
    if HOT.exists():
        playback_mode()
    else:
        capture_mode()

if __name__ == "__main__":
    sys.exit(main())
