import json
from datetime import datetime

def log_audit_entry(contributor, theme, paper, action, details, notes, log_path="badge_trigger_audit_log.md"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M %Z")
    entry = f"""
### 🧹 Rollback
- **Timestamp:** {timestamp}  
- **Contributor:** {contributor}  
- **Theme:** {theme}  
- **Paper:** {paper}  
- **Action:** {action}  
- **Details:** {details}  
- **Notes:** {notes}
"""
    with open(log_path, "a") as f:
        f.write(entry + "\n")

def rollback_glyph(theme, paper, contributor="Nawder Loswin",
                   manifest_path="badge_trigger_echo_manifest.json",
                   svg_path="badge_trigger_echo_map.svg",
                   log_path="badge_trigger_audit_log.md"):

    with open(manifest_path, "r") as f:
        manifest = json.load(f)

    entry = next((e for e in manifest["echoed_glyphs"] if e["theme"] == theme and e["paper"] == paper), None)
    if not entry:
        print(f"⚠️ No glyph found for {paper} in {theme}.")
        return

    with open(svg_path, "r") as f:
        svg = f.read()

    marker_comment = f"<!-- {theme} – {paper} -->"
    svg = svg.replace(marker_comment, "")
    svg = svg.replace(f"<text x=\"300\" y=\"130\">{entry['status']}</text>", "")

    with open(svg_path, "w") as f:
        f.write(svg)

    manifest["echoed_glyphs"] = [e for e in manifest["echoed_glyphs"] if not (e["theme"] == theme and e["paper"] == paper)]

    with open(manifest_path, "w") as f:
        json.dump(manifest, f, indent=2)

    log_audit_entry(
        contributor=contributor,
        theme=theme,
        paper=paper,
        action="Glyph rollback",
        details="Removed SVG marker and manifest entry.",
        notes="Triggered by validation mismatch. Preparing for re-echo with updated resonance protocol.",
        log_path=log_path
    )

    print(f"🧹 Glyph and manifest entry removed for {paper} in {theme}. Audit log updated.")

# Example usage
if __name__ == "__main__":
    rollback_glyph("Quantum & Particle Vision", "Entropy’s Harmonic")
