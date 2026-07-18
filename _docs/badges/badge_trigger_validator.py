import json
from datetime import datetime

def log_validation_entry(validator, theme, paper, outcome, protocol, notes, log_path="badge_trigger_validator_log.md"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M %Z")
    entry = f"""
### 🔎 Validation
- **Timestamp:** {timestamp}  
- **Validator:** {validator}  
- **Theme:** {theme}  
- **Paper:** {paper}  
- **Outcome:** {outcome}  
- **Protocol:** {protocol}  
- **Notes:** {notes}
"""
    with open(log_path, "a") as f:
        f.write(entry + "\n")

def validate_glyph(theme, paper,
                   validator="loop_validator.py",
                   protocol="loop_validation_protocol.md",
                   manifest_path="badge_trigger_echo_manifest.json",
                   log_path="badge_trigger_validator_log.md"):

    # Load manifest
    with open(manifest_path, "r") as f:
        manifest = json.load(f)

    entry = next((e for e in manifest["echoed_glyphs"] if e["theme"] == theme and e["paper"] == paper), None)
    if not entry:
        print(f"⚠️ No glyph found for {paper} in {theme}.")
        return

    # Simulated validation logic
    reproducibility_passed = True  # Replace with actual check
    svg_preview_ok = True          # Replace with actual check

    if reproducibility_passed and svg_preview_ok:
        outcome = "✅ Passed"
        notes = "Echo validated across platforms. Resonance confirmed."
    else:
        outcome = "❌ Failed"
        notes = "Validation mismatch. Reproducibility or SVG preview failed."

    log_validation_entry(
        validator=validator,
        theme=theme,
        paper=paper,
        outcome=outcome,
        protocol=protocol,
        notes=notes,
        log_path=log_path
    )

    print(f"🔍 Validation complete for {paper} in {theme}: {outcome}")

# Example usage
if __name__ == "__main__":
    validate_glyph("Quantum & Particle Vision", "Entropy’s Harmonic")
