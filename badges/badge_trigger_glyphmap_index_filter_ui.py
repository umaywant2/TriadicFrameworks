import pandas as pd
import json
from pathlib import Path

# Load logs
theme_manifest = Path("badge_trigger_theme_manifest.md").read_text()
validator_log = Path("badge_trigger_validator_log.md").read_text()

# Placeholder parser
def parse_flat_data(manifest, log):
    return pd.DataFrame([
        {"Glyph": "🜁", "Theme": "Elemental & Spectrum", "Paper Title": "Spectral Flux and Divisional Resonance Is Born", "Validated": False},
        {"Glyph": "🧠", "Theme": "Cognitive & Symbolic", "Paper Title": "Improving ISO Standards with Triadic Frameworks", "Validated": False},
        {"Glyph": "🎶", "Theme": "Music & Symbolic Extensions", "Paper Title": "Triadic Framework for Music – With Quadratic Extensions", "Validated": True},
        {"Glyph": "⚛️", "Theme": "Quantum & Particle Vision", "Paper Title": "Triadic Framework Technology for Quantum Computers", "Validated": False},
        {"Glyph": "🪐", "Theme": "Planetary & Temporal Mapping", "Paper Title": "Resonant Time – Operationalizing Zhang’s Triadic Ontology", "Validated": True},
        {"Glyph": "🩺", "Theme": "Health & Ultrasound", "Paper Title": "Triadic Ultrasound Enhancement", "Validated": False},
        {"Glyph": "🔧", "Theme": "Engineering & Firmware", "Paper Title": "Triadic Framework for ARM and x86 Processors", "Validated": True},
        {"Glyph": "⚡", "Theme": "Energy & Wireless Power", "Paper Title": "WiFi_Energy_Protocols", "Validated": False}
    ])

# UI prompt
def run_ui():
    df = parse_flat_data(theme_manifest, validator_log)
    print("\n🔮 Badge Trigger Glyphmap Filter UI")
    print("Select filters (leave blank to skip):")

    glyph = input("Glyph (e.g. 🜁, ⚛️): ").strip() or None
    theme = input("Theme (e.g. Quantum & Particle Vision): ").strip() or None
    val_input = input("Validated only? (y/n): ").strip().lower()
    validated = True if val_input == "y" else False if val_input == "n" else None
    format = input("Export format (csv/json): ").strip().lower() or "csv"

    # Apply filters
    if glyph:
        df = df[df["Glyph"] == glyph]
    if theme:
        df = df[df["Theme"] == theme]
    if validated is not None:
        df = df[df["Validated"] == validated]

    # Export
    if format == "csv":
        df.to_csv("badge_trigger_glyphmap_index_filtered.csv", index=False)
        print("✅ Filtered CSV saved.")
    elif format == "json":
        Path("badge_trigger_glyphmap_index_filtered.json").write_text(json.dumps(df.to_dict(orient="records"), indent=2))
        print("✅ Filtered JSON saved.")
    else:
        print("⚠️ Unknown format.")

# Run
if __name__ == "__main__":
    run_ui()
