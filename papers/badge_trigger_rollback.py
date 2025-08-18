import json

def rollback_glyph(theme, paper, manifest_path="badge_trigger_echo_manifest.json", svg_path="badge_trigger_echo_map.svg"):
    # Load manifest
    with open(manifest_path, "r") as f:
        manifest = json.load(f)

    # Find entry
    entry = next((e for e in manifest["echoed_glyphs"] if e["theme"] == theme and e["paper"] == paper), None)
    if not entry:
        print(f"⚠️ No glyph found for {paper} in {theme}.")
        return

    # Remove SVG marker
    with open(svg_path, "r") as f:
        svg = f.read()

    marker_comment = f"<!-- {theme} – {paper} -->"
    svg = svg.replace(marker_comment, "")  # Remove comment
    svg = svg.replace(f"<text x=\"300\" y=\"130\">{entry['status']}</text>", "")  # Remove glyph

    with open(svg_path, "w") as f:
        f.write(svg)

    # Remove from manifest
    manifest["echoed_glyphs"] = [e for e in manifest["echoed_glyphs"] if not (e["theme"] == theme and e["paper"] == paper)]

    with open(manifest_path, "w") as f:
        json.dump(manifest, f, indent=2)

    print(f"🧹 Glyph and manifest entry removed for {paper} in {theme}.")

# Example usage
if __name__ == "__main__":
    rollback_glyph("Quantum & Particle Vision", "Entropy’s Harmonic")
