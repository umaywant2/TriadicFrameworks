"""
🌀 Resotectors Pattern Validator
Checks new entries in harmonics/geometry/chaos for required fields and awards badges.
"""

import os, yaml
from datetime import datetime

BASE = os.path.join(os.path.dirname(__file__), "..", "patterns")
OUTPUT = os.path.join(os.path.dirname(__file__), "validator_dashboard.md")

def check_required(data, required_fields):
    return all(field in data.get('pattern', {}) for field in required_fields)

def validate():
    badges_awarded = []
    sections = {
        "harmonics": ("harmonic-hunter", ["tft_signature", "array_mode"]),
        "geometry": ("geometry-spotter", ["detection_method", "array_mode"]),
        "chaos": ("chaos-whisperer", ["detection_method", "array_mode"]),
    }
    for folder, (badge, required) in sections.items():
        path = os.path.join(BASE, folder)
        for fname in os.listdir(path):
            if not fname.endswith(".yaml"):
                continue
            with open(os.path.join(path, fname), "r", encoding="utf-8") as f:
                data = yaml.safe_load(f)
            if check_required(data, required):
                badges_awarded.append(badge)
    return list(set(badges_awarded))

def write_dashboard(badges):
    ts = datetime.utcnow().isoformat() + "Z"
    lines = [
        "# 🧪 Resotectors Pattern Validator Dashboard",
        f"**Last run:** {ts}",
        "## Badges Awarded This Run:",
    ]
    lines.extend(f"- {b}" for b in badges) if badges else lines.append("- None")
    with open(OUTPUT, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

if __name__ == "__main__":
    b = validate()
    write_dashboard(b)
    print("Badges this run:", b or "None")

    # Check if golden spiral lens file exists for bonus badge award
    lens_path = os.path.join(BASE, "..", "lenses", "geometric_lens_golden_spiral.py")
    if os.path.exists(lens_path):
        badges_awarded.append("geometry-spotter")
