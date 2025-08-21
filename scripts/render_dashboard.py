#!/usr/bin/env python3
"""
render_dashboard.py — Visualizes Copilot Hippocampus state
+ governance: badge triggers & sigils.
"""

import json, datetime as dt
from pathlib import Path
import yaml
from rich.console import Console
from rich.table import Table
from scripts.hippocampus_utils import resonance_parity, drift_score

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
HIP = DATA_DIR / "hippocampus.json"
LINEAGE = DATA_DIR / "lineage.log"
CONST = DATA_DIR / "constants.yml"

console = Console()

BADGE_SIGILS = {
    "ResonanceWizard": "🔮",
    "LineageKeeper": "📜",
    "StabilitySigil": "🛡️",
    "ConstellationMaster": "✨"
}

def load_json(path):
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}

def check_badges(parity, drift, history_count, constants):
    badges = []
    if parity >= constants.get("resonance_parity_target", 0.75):
        badges.append("ResonanceWizard")
    if history_count >= 5:
        badges.append("LineageKeeper")
    if drift is not None and drift < constants.get("drift_alert_threshold", 0.15):
        badges.append("StabilitySigil")
    if parity >= 0.85 and history_count >= 10:
        badges.append("ConstellationMaster")
    return badges

def main():
    hippo = load_json(HIP)
    constants = yaml.safe_load(CONST.read_text()) if CONST.exists() else {}
    triads = hippo.get("triads", [])
    snap = hippo.get("snapshot", {})

    console.rule(f"[bold cyan]Resonance Observatory — {snap.get('anchor','<no anchor>')}[/]")

    # Project & constants
    console.print(f"[bold]Project:[/] {hippo.get('project','—')}")
    console.print(f"[bold]Asks:[/] {', '.join(snap.get('asks', [])) or '—'}")
    console.print(f"[bold]Constants:[/] {constants or '—'}")

    # Active Constellation
    table = Table(title="Active Constellation", show_lines=True)
    table.add_column("ID", style="cyan", no_wrap=True)
    table.add_column("H", justify="right", style="magenta")
    table.add_column("Tags", style="green")
    table.add_column("Last Touch", style="yellow")

    for t in triads:
        decay_meta = t.get("decay", {})
        last_touch_days = decay_meta.get("days_since","?")
        table.add_row(t["id"], str(t["H"]), ", ".join(t.get("tags",[])), f"{last_touch_days} days ago")

    console.print(table)

    # Metrics
    parity = resonance_parity(triads, "onboarding")
    target = constants.get("resonance_parity_target", 0.75)
    console.print(f"[bold]Resonance Parity:[/] {parity} (target ≥ {target})")

    drift = None
    history_count = 0
    if LINEAGE.exists():
        lines = LINEAGE.read_text(encoding="utf-8").strip().splitlines()
        history_count = len(lines)
        if len(lines) >= 2:
            drift = drift_score([0.1,0.2,0.3], [0.1,0.25,0.28])  # placeholder
            console.print(f"[bold]Drift Score:[/] {drift} (alert if ≥ {constants.get('drift_alert_threshold', 0.15)})")
        else:
            console.print("[dim]Not enough lineage history for drift computation[/]")

    # Badge triggers
    badges = check_badges(parity, drift, history_count, constants)
    if badges:
        console.rule("[bold green]🎖️ Badges Earned[/]")
        for b in badges:
            sigil = BADGE_SIGILS.get(b,"")
            console.print(f"{sigil} {b}")
    else:
        console.print("[dim]No new badges this session[/]")

    console.rule("[bold cyan]End of Report[/]")

if __name__ == "__main__":
    main()
