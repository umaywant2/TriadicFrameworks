import os

ROOT = "docs"
SPINE = os.path.join(ROOT, "spine")

# Known atlas/heatmap SVGs to stack
SVG_FILES = [
    "triad_purity_heatmap.svg",
    "consistency_map.svg",
    "consistency_map_heatmap.svg",
]

def read_svg_body(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            text = f.read()
    except:
        return None

    # crude extraction: strip outer <svg ...>...</svg>
    start = text.find("<svg")
    if start == -1:
        return None
    start = text.find(">", start)
    end = text.rfind("</svg>")
    if start == -1 or end == -1:
        return None
    inner = text[start + 1:end].strip()
    return inner

def main():
    print("\n=== TriadicFrameworks Multi‑Atlas SVG Composite Generator ===\n")

    os.makedirs(SPINE, exist_ok=True)
    atlas_paths = []
    for name in SVG_FILES:
        p = os.path.join(SPINE, name)
        if os.path.isfile(p):
            atlas_paths.append(p)
            print(f"✔ found atlas: {name}")
        else:
            print(f"⚠ missing atlas: {name}")

    if not atlas_paths:
        print("\n⚠ No atlas SVGs found in /docs/spine — nothing to composite.\n")
        return

    # Assume each atlas is roughly same width; stack vertically with offsets
    bodies = []
    y_offset = 0
    gap = 20  # vertical gap between atlases

    # Simple fixed width/height; we’ll expand height as we stack
    width = 1200
    total_height = 0

    for p in atlas_paths:
        inner = read_svg_body(p)
        if inner is None:
            print(f"⚠ could not parse {os.path.basename(p)} — skipped")
            continue

        # Wrap each atlas in a <g> with translate
        bodies.append(f'<g transform="translate(0,{y_offset})">\n{inner}\n</g>\n')
        # crude height increment: assume 400px per atlas
        y_offset += 400 + gap
        total_height = y_offset

    if not bodies:
        print("\n⚠ No parsable atlas SVGs — composite not created.\n")
        return

    out_path = os.path.join(SPINE, "multi_atlas_composite.svg")
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{total_height}">
<rect x="0" y="0" width="{width}" height="{total_height}" fill="#ffffff"/>
{''.join(bodies)}
</svg>
"""

    with open(out_path, "w", encoding="utf-8") as f:
        f.write(svg)

    print(f"\n✔ Created {out_path}")
    print("\n✨ Multi‑atlas SVG composite generated.\n")

if __name__ == "__main__":
    main()
