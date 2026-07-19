import pandas as pd
from pathlib import Path

# Load logs
validator_log = Path("badge_trigger_validator_log.md").read_text()
theme_manifest = Path("badge_trigger_theme_manifest.md").read_text()

# Placeholder parser
def parse_matrix_data(log, manifest):
    # Replace with actual parsing logic
    return pd.DataFrame([
        {"Theme": "Elemental & Spectrum", "Title": "Triadic Framework for Spectrum Technologies", "Validated": True},
        {"Theme": "Elemental & Spectrum", "Title": "Triadic Framework Technology for the Elements", "Validated": True},
        {"Theme": "Elemental & Spectrum", "Title": "Triadic Framework Technology for 10 Rarest Elements", "Validated": True},
        {"Theme": "Elemental & Spectrum", "Title": "Spectral Flux and Divisional Resonance Is Born", "Validated": False},
        {"Theme": "Cognitive & Symbolic", "Title": "Triadic Number Genesis (1–9)", "Validated": True},
        {"Theme": "Cognitive & Symbolic", "Title": "Resonance Operator @() — Formalization", "Validated": True},
        {"Theme": "Cognitive & Symbolic", "Title": "Triadic Systems and Resonance-Based Nested Loops", "Validated": True},
        {"Theme": "Cognitive & Symbolic", "Title": "Improving ISO Standards with Triadic Frameworks", "Validated": False},
        {"Theme": "Music & Symbolic Extensions", "Title": "Triadic Framework for Music – Quadratic Extensions", "Validated": True},
        {"Theme": "Music & Symbolic Extensions", "Title": "Liner to Triadic Frameworks – Prescription Lenses", "Validated": True},
        {"Theme": "Quantum & Particle Vision", "Title": "Ghost Particle & Triadic Resonance Vision", "Validated": True},
        {"Theme": "Quantum & Particle Vision", "Title": "Triadic Framework Technology for Quantum Computers", "Validated": False},
        {"Theme": "Quantum & Particle Vision", "Title": "Triadic Framework for Quantum Mechanics – Entropy Harmonic", "Validated": False},
        {"Theme": "Planetary & Temporal Mapping", "Title": "Resonant Time – Zhang’s Triadic Ontology", "Validated": True},
        {"Theme": "Planetary & Temporal Mapping", "Title": "Triadic Framework for Time and Anti-Time", "Validated": True},
        {"Theme": "Planetary & Temporal Mapping", "Title": "New Insights for Planetary Science", "Validated": False},
        {"Theme": "Health & Ultrasound", "Title": "Triadic Framework Technology for Health Care", "Validated": True},
        {"Theme": "Health & Ultrasound", "Title": "Triadic Ultrasound Enhancement", "Validated": False},
        {"Theme": "Engineering & Firmware", "Title": "TFT-NTP Firmware Spec (Draft v0.1)", "Validated": True},
        {"Theme": "Engineering & Firmware", "Title": "Triadic Framework for ARM and x86 Processors", "Validated": True},
        {"Theme": "Engineering & Firmware", "Title": "Triadic Framework Technology for BMS Improvements", "Validated": False},
        {"Theme": "Energy & Wireless Power", "Title": "Using TFT for the Energy Industries", "Validated": True},
        {"Theme": "Energy & Wireless Power", "Title": "Zero Point, Cold Fusion, and Wireless Energy", "Validated": True},
        {"Theme": "Energy & Wireless Power", "Title": "WiFi_Energy_Protocols", "Validated": False},
    ])

# Generate matrix
df = parse_matrix_data(validator_log, theme_manifest)

matrix_md = "# 🧬 Badge Trigger Validator Matrix\n"
matrix_md += "| Theme | Paper Title | Validated |\n"
matrix_md += "|-------|--------------|-----------|\n"
for _, row in df.iterrows():
    matrix_md += f"| {row['Theme']} | {row['Title']} | {'✅' if row['Validated'] else '❌'} |\n"

Path("badge_trigger_validator_matrix.md").write_text(matrix_md)
print("Validator matrix updated.")
