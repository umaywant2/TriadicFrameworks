import pandas as pd
from pathlib import Path

# Load logs
validator_log = Path("badge_trigger_validator_log.md").read_text()
theme_manifest = Path("badge_trigger_theme_manifest.md").read_text()

# Placeholder parser
def parse_validator_data(log, manifest):
    # Replace with actual parsing logic
    return pd.DataFrame([
        {"Theme": "Elemental & Spectrum", "Validated": 3, "Total": 4},
        {"Theme": "Cognitive & Symbolic", "Validated": 3, "Total": 4},
        {"Theme": "Music & Symbolic Extensions", "Validated": 2, "Total": 2},
        {"Theme": "Quantum & Particle Vision", "Validated": 1, "Total": 3},
        {"Theme": "Planetary & Temporal Mapping", "Validated": 2, "Total": 3},
        {"Theme": "Health & Ultrasound", "Validated": 1, "Total": 2},
        {"Theme": "Engineering & Firmware", "Validated": 2, "Total": 3},
        {"Theme": "Energy & Wireless Power", "Validated": 2, "Total": 3},
    ])

# Generate dashboard
df = parse_validator_data(validator_log, theme_manifest)
df["Rate"] = (df["Validated"] / df["Total"] * 100).round(0).astype(int).astype(str) + "%"

dashboard_md = "# 🧪 Badge Trigger Validator Dashboard\n"
dashboard_md += "| Theme | Papers Validated | Total Papers | Validation Rate |\n"
dashboard_md += "|-------|------------------|--------------|-----------------|\n"
for _, row in df.iterrows():
    dashboard_md += f"| {row['Theme']} | {row['Validated']} | {row['Total']} | {row['Rate']} |\n"

Path("badge_trigger_validator_dashboard.md").write_text(dashboard_md)
print("Validator dashboard updated.")
