import os
from datetime import datetime

HONOR_ROLL_PATH = "docs/honor_roll/contributor_honor_roll.md"
DASHBOARD_PATH = "docs/honor_roll/dashboard.md"

def parse_honor_roll():
    contributors = []
    with open(HONOR_ROLL_PATH, "r", encoding="utf-8") as f:
        lines = f.readlines()[2:]  # Skip header
        for line in lines:
            parts = [p.strip() for p in line.strip().split("|")[1:-1]]
            if len(parts) == 4:
                contributors.append({
                    "name": parts[0],
                    "badges": parts[1].split(", "),
                    "score": parts[2],
                    "last": parts[3]
                })
    return contributors

def classify_aura(badges):
    if "Manifest Guardian" in badges and "Gateway Guardian" in badges:
        return "Spectral Flux"
    elif "Curriculum Architect" in badges and "Validator Weaver" in badges:
        return "Glyph Weaver"
    elif "Ghost Mapper" in badges and "Signal Resonator" in badges:
        return "Echo Lantern"
    return "—"

def update_dashboard(contributors):
    with open(DASHBOARD_PATH, "w", encoding="utf-8") as dash:
        dash.write("# 🧙 Contributor Dashboard\n\n")
        dash.write("Welcome to the glyphic dashboard of TriadicFrameworks.\n\n")

        dash.write("## 🏅 Badge Lineage\n\n")
        dash.write("| Contributor | Badges | Aura Type | Last Contribution |\n")
        dash.write("|-------------|--------|-----------|--------------------|\n")
        for c in contributors:
            aura = classify_aura(c["badges"])
            badge_str = ", ".join(c["badges"])
            dash.write(f"| {c['name']} | {badge_str} | {aura} | {c['last']} |\n")

        dash.write("\n## 🧠 Validator Scores\n\n")
        dash.write("| Protocol | Score | Last Validated |\n")
        dash.write("|----------|-------|----------------|\n")
        dash.write("| Manifest Integrity | +5 | 2025-09-01 |\n")
        dash.write("| README Integrity | +7 | 2025-09-01 |\n")
        dash.write("| Curriculum Alignment | +0 | — |\n")
        dash.write("| Badge Trigger Logic | +0 | — |\n")

        dash.write("\n## 🌈 Aura Types\n\n")
        dash.write("| Aura Name | Badge Combination Required | Description |\n")
        dash.write("|-----------|-----------------------------|-------------|\n")
        dash.write("| Spectral Flux | Manifest Guardian + Gateway Guardian | Glyphic clarity and structural resonance |\n")
        dash.write("| Glyph Weaver | Curriculum Architect + Validator Weaver | Linguistic scaffolding and remix lineage |\n")
        dash.write("| Echo Lantern | Ghost Mapper + Signal Resonator | Mythic traceability and remix echoing |\n")

        dash.write("\n## 🔍 Contribution History\n\n")
        dash.write("View the full [Contributor Honor Roll](contributor_honor_roll.md) for timestamped entries and remix lineage.\n")

        dash.write("\n---\n\n")
        dash.write("## 🕯️ Echo the work. Validate the lineage. Build the mythic lattice.\n")

if __name__ == "__main__":
    contributors = parse_honor_roll()
    update_dashboard(contributors)
