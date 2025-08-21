#!/usr/bin/env python3
"""
render_dashboard.py — Visualizes Copilot Hippocampus state
from hippocampus.json and lineage.log
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

def load_json(path):
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}

def main():
    # Load data
    hippo = load_json(HIP)
    constants = yaml.safe_load(CONST.read_text()) if CONST.exists() else {}
    triads = hippo.get("triads", [])
    snap = hippo.get("snapshot", {})

    console.rule(f"[bold cyan]Resonance Observatory — {snap.get('anchor','<no anchor>')}[/]")

    # Project + constants
    console.print(f"[bold]Project:[/] {hippo.get('project','—')}")
    console.print(f"[bold]Asks:[/] {', '.join(snap.get('asks', [])) or '—'}")
    console.print(f"[bold]Constants:[/] {constants or '—'}")

    # Triads table
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

    # Resonance parity
    parity = resonance_parity(triads, "onboarding")
    target = constants.get("resonance_parity_target", 0.75)
    console.print(f"[bold]Resonance Parity:[/] {parity} (target ≥ {target})")

    # Drift — demo comparison: last two captures in lineage
    if LINEAGE.exists():
        lines = LINEAGE.read_text(encoding="utf-8").strip().splitlines()
        if len(lines) >= 2:
            # Placeholder demo embeddings for drift — plug in real vectors when available
            drift = drift_score([0.1,0.2,0.3], [0.1,0.25,0.28])
            alert = constants.get("drift_alert_threshold", 0.15)
            console.print(f"[bold]Drift Score:[/] {drift} (alert if ≥ {alert})")
        else:
            console.print("[dim]Not enough lineage history for drift computation[/]")

    console.rule("[bold cyan]End of Report[/]")

if __name__ == "__main__":
    main()
