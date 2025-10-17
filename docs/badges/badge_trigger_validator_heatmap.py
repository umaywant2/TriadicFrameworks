import pandas as pd
from pathlib import Path

# Load logs
validator_log = Path("badge_trigger_validator_log.md").read_text()
theme_manifest = Path("badge_trigger_theme_manifest.md").read_text()

# Placeholder parser
def parse_heatmap_data(log, manifest):
    # Replace with actual parsing logic
    return pd.DataFrame([
        {"Theme": "Elemental & Spectrum", "Validated": [True, True, True, False]},
        {"Theme": "Cognitive & Symbolic", "Validated": [True, True, True, False]},
        {"Theme": "Music & Symbolic Extensions", "Validated": [True, True]},
        {"Theme": "Quantum & Particle Vision", "Validated": [True, False, False]},
        {"Theme": "Planetary & Temporal Mapping", "Validated": [True, True, False]},
        {"Theme": "Health & Ultrasound", "Validated": [True, False]},
        {"Theme": "Engineering & Firmware", "Validated": [True, True, False]},
        {"Theme": "Energy & Wireless Power", "Validated": [True, True, False]},
    ])

# Generate SVG
df = parse_heatmap_data(validator_log, theme_manifest)
svg = '<svg width="800" height="500" xmlns="http://www.w3.org/2000/svg">\n'
svg += '<style>.theme{font:bold 14px sans-serif;} .validated{fill:#4CAF50;} .unvalidated{fill:#F44336;} .label{fill:#000;}</style>\n'

y_base = 30
x_base = 250
x_step = 30

for i, row in df.iterrows():
    svg += f'<text x="20" y="{y_base + i*50}" class="theme">{row["Theme"]}</text>\n'
    for j, val in enumerate(row["Validated"]):
        color_class = "validated" if val else "unvalidated"
        x = x_base + j * x_step
        y = y_base - 5 + i * 50
        svg += f'<circle cx="{x}" cy="{y}" r="10" class="{color_class}"/>\n'

# Legend
svg += '<rect x="600" y="30" width="20" height="20" class="validated"/><text x="630" y="45" class="label">Validated</text>\n'
svg += '<rect x="600" y="60" width="20" height="20" class="unvalidated"/><text x="630" y="75" class="label">Unvalidated</text>\n'
svg += '</svg>'

Path("badge_trigger_validator_heatmap.svg").write_text(svg)
print("Validator heatmap updated.")
