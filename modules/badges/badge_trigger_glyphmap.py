import pandas as pd
from pathlib import Path

# Load logs
theme_manifest = Path("badge_trigger_theme_manifest.md").read_text()
validator_log = Path("badge_trigger_validator_log.md").read_text()

# Placeholder parser
def parse_glyphmap_data(manifest, log):
    # Replace with actual parsing logic
    return pd.DataFrame([
        {"Theme": "Elemental & Spectrum", "Glyph": "🜁", "Aura": "validated"},
        {"Theme": "Cognitive & Symbolic", "Glyph": "🧠", "Aura": "validated"},
        {"Theme": "Music & Symbolic Extensions", "Glyph": "🎶", "Aura": "validated"},
        {"Theme": "Quantum & Particle Vision", "Glyph": "⚛️", "Aura": "partial"},
        {"Theme": "Planetary & Temporal Mapping", "Glyph": "🪐", "Aura": "partial"},
        {"Theme": "Health & Ultrasound", "Glyph": "🩺", "Aura": "partial"},
        {"Theme": "Engineering & Firmware", "Glyph": "🔧", "Aura": "partial"},
        {"Theme": "Energy & Wireless Power", "Glyph": "⚡", "Aura": "partial"},
    ])

# Generate SVG
df = parse_glyphmap_data(theme_manifest, validator_log)
svg = '<svg width="800" height="500" xmlns="http://www.w3.org/2000/svg">\n'
svg += '<style>.glyph{font:bold 24px serif;} .theme{font:14px sans-serif;fill:#333;} .halo{stroke-width:6;stroke-opacity:0.5;} .validated{stroke:#4CAF50;} .partial{stroke:#FFC107;} .unvalidated{stroke:#F44336;}</style>\n'

for i, row in df.iterrows():
    y = 60 + i * 50
    svg += f'<g transform="translate(100,{y})">\n'
    svg += f'  <text x="0" y="0" class="glyph">{row["Glyph"]}</text>\n'
    svg += f'  <circle cx="10" cy="-10" r="25" class="halo {row["Aura"]}"/>\n'
    svg += f'  <text x="40" y="0" class="theme">{row["Theme"]}</text>\n'
    svg += '</g>\n'

# Legend
svg += '<rect x="600" y="30" width="20" height="20" class="validated"/><text x="630" y="45" class="theme">Validated</text>\n'
svg += '<rect x="600" y="60" width="20" height="20" class="partial"/><text x="630" y="75" class="theme">Partial</text>\n'
svg += '<rect x="600" y="90" width="20" height="20" class="unvalidated"/><text x="630" y="105" class="theme">Unvalidated</text>\n'
svg += '</svg>'

Path("badge_trigger_glyphmap.svg").write_text(svg)
print("Glyphmap constellation updated.")
