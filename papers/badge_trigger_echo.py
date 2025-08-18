import json
import re
from datetime import datetime

def load_manifest(manifest_path="badge_trigger_echo_manifest.json"):
    try:
        with open(manifest_path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {"echoed_glyphs": []}

def glyph_already_echoed(manifest, theme, paper):
    return any(entry["theme"] == theme and entry["paper"] == paper for entry in manifest["echoed_glyphs"])

def append_glyph_to_svg(svg_path, theme, paper, status, manifest_path):
    manifest = load_manifest(manifest_path)
    if glyph_already_echoed(manifest, theme, paper):
        print(f"⚠️ Glyph for {paper} in {theme} already echoed. Skipping.")
        return

    with open(svg_path, "r") as f:
        svg = f.read()

    marker = f"<text x=\"300\" y=\"130\">{status}</text> <!-- {theme} – {paper} -->\n"
    insert_point = svg.find("</svg>")
    updated_svg = svg[:insert_point] + marker + svg[insert_point:]

    with open(svg_path, "w") as f:
        f.write(updated_svg)

    # Update manifest
    manifest["echoed_glyphs"].append({
        "theme": theme,
        "paper": paper,
        "status": status,
        "timestamp": datetime.now().isoformat(),
        "svg_id": f"glyph_{len(manifest['echoed_glyphs']) + 1:03}"
    })

    with open(manifest_path, "w") as f:
        json.dump(manifest, f, indent=2)

    print(f"🎨 Glyph echoed and manifest updated for {paper} in {theme}.")

# Example usage
if __name__ == "__main__":
    append_glyph_to_svg(
        svg_path="badge_trigger_echo_map.svg",
        theme="Quantum & Particle Vision",
        paper="Entropy’s Harmonic",
        status="✅",
        manifest_path="badge_trigger_echo_manifest.json"
    )
