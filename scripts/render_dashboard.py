#!/usr/bin/env python3
"""
render_dashboard.py — Resonance Observatory
Now with HTML export for GitHub Pages/docs sharing.
"""

import json
from pathlib import Path
import yaml
from datetime import datetime as dt
from scripts.hippocampus_utils import resonance_parity, drift_score

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
DOCS_DIR = ROOT / "docs"
HIP = DATA_DIR / "hippocampus.json"
LINEAGE = DATA_DIR / "lineage.log"
CONST = DATA_DIR / "constants.yml"

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

def render_html(hippo, constants, triads, parity, drift, history_count, badges):
    ts = dt.utcnow().strftime("%Y-%m-%d %H:%M:%SZ")
    rows = "\n".join(
        f"<tr><td>{t['id']}</td><td>{t['H']}</td>"
        f"<td>{', '.join(t.get('tags',[]))}</td>"
        f"<td>{t.get('decay',{}).get('days_since','?')} days ago</td></tr>"
        for t in triads
    )
    badge_html = "".join(
        f"<li>{BADGE_SIGILS.get(b,'')} {b}</li>" for b in badges
    ) or "<li><em>No new badges this session</em></li>"

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Resonance Observatory — {hippo.get('project','')}</title>
<style>
body {{ font-family: sans-serif; padding: 1rem; }}
table {{ border-collapse: collapse; width: 100%; }}
td, th {{ border: 1px solid #ccc; padding: 0.5rem; }}
th {{ background: #eee; }}
</style>
</head>
<body>
<h1>Resonance Observatory</h1>
<p><strong>Project:</strong> {hippo.get('project','—')}</p>
<p><strong>Anchor:</strong> {hippo.get('snapshot',{}).get('anchor','—')}</p>
<p><strong>Asks:</strong> {', '.join(hippo.get('snapshot',{}).get('asks', [])) or '—'}</p>
<p><strong>Constants:</strong> {constants}</p>
<h2>Active Constellation</h2>
<table>
<tr><th>ID</th><th>H</th><th>Tags</th><th>Last Touch</th></tr>
{rows}
</table>
<h2>Metrics</h2>
<ul>
<li><strong>Resonance Parity:</strong> {parity}</li>
<li><strong>Drift Score:</strong> {drift if drift is not None else '—'}</li>
<li><strong>History Count:</strong> {history_count}</li>
</ul>
<h2>Badges Earned</h2>
<ul>
{badge_html}
</ul>
<p><em>Generated {ts} UTC</em></p>
</body>
</html>"""
    out_path = DOCS_DIR / "resonance_observatory.html"
    DOCS_DIR.mkdir(exist_ok=True)
    out_path.write_text(html, encoding="utf-8")
    print(f"[+] HTML report written to {out_path}")

def main():
    hippo = load_json(HIP)
    constants = yaml.safe_load(CONST.read_text()) if CONST.exists() else {}
    triads = hippo.get("triads", [])
    parity = resonance_parity(triads, "onboarding")
    drift = None
    history_count = 0
    if LINEAGE.exists():
        lines = LINEAGE.read_text(encoding="utf-8").strip().splitlines()
        history_count = len(lines)
        if len(lines) >= 2:
            drift = drift_score([0.1,0.2,0.3],[0.1,0.25,0.28]) # placeholder
    badges = check_badges(parity, drift, history_count, constants)
    render_html(hippo, constants, triads, parity, drift, history_count, badges)

if __name__ == "__main__":
    main()
