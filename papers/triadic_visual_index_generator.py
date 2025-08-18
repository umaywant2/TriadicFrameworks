import json
import markdown
from xml.etree.ElementTree import Element, SubElement, tostring
from pathlib import Path

def load_glyphmap_index(path):
    with open(path, 'r') as f:
        return json.load(f)

def parse_theme_manifest(path):
    with open(path, 'r') as f:
        md = markdown.markdown(f.read())
        # Simplified parser: extract theme blocks and tiers
        return extract_themes(md)

def extract_themes(md_content):
    # Placeholder: parse HTML from markdown to extract theme mappings
    return {
        "Quantum": {"tier": "I", "color": "#00FFFF"},
        "Planetary": {"tier": "II", "color": "#FFD700"},
        "Health": {"tier": "III", "color": "#FF69B4"},
    }

def generate_svg(glyph_data, theme_data):
    svg = Element('svg', xmlns="http://www.w3.org/2000/svg", width="1200", height="800")
    for glyph, props in glyph_data.items():
        theme = props.get("theme")
        coords = props.get("coords", [0, 0])
        color = theme_data.get(theme, {}).get("color", "#CCCCCC")
        SubElement(svg, 'circle', cx=str(coords[0]), cy=str(coords[1]), r="10", fill=color)
        SubElement(svg, 'text', x=str(coords[0]+12), y=str(coords[1]), fill="#333", font_size="12").text = glyph
    return tostring(svg).decode()

def save_svg(output_path, svg_content):
    with open(output_path, 'w') as f:
        f.write(svg_content)

if __name__ == "__main__":
    glyph_data = load_glyphmap_index("badge_trigger_glyphmap_index.json")
    theme_data = parse_theme_manifest("badge_trigger_theme_manifest.md")
    svg_content = generate_svg(glyph_data, theme_data)
    save_svg("triadic_visual_index.svg", svg_content)
    print("✅ Visual index generated and saved.")
