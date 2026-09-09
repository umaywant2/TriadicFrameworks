import os
import json

ROOT = "docs"
SPINE = os.path.join(ROOT, "spine")

SVG_FILES = {
    "Triad‑Purity Heatmap": "triad_purity_heatmap.svg",
    "Consistency Map SVG": "consistency_map.svg",
    "Consistency Heatmap": "consistency_map_heatmap.svg",
    "Multi‑Atlas Composite": "multi_atlas_composite.svg",
}

HTML_FILES = {
    "Consistency Map HTML": "consistency_map.html",
    "Consistency Atlas": "consistency_atlas.html",
}

JSON_FILES = {
    "Structural Fingerprint": "structural_fingerprint.json",
}

def read_file(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except:
        return None

def main():
    print("\n=== TriadicFrameworks Structural Observatory Generator ===\n")

    os.makedirs(SPINE, exist_ok=True)

    sections = []

    # SVG section
    svg_blocks = []
    for label, fname in SVG_FILES.items():
        p = os.path.join(SPINE, fname)
        if os.path.isfile(p):
            svg_blocks.append(f"<h2>{label}</h2>\n<object type=\"image/svg+xml\" data=\"{fname}\" style=\"width:100%;border:1px solid #ddd;\"></object>\n")
            print(f"✔ found SVG: {fname}")
        else:
            svg_blocks.append(f"<h2>{label}</h2>\n<p>Missing: {fname}</p>\n")
            print(f"⚠ missing SVG: {fname}")
    sections.append("<section>\n<h1>SVG Atlases & Heatmaps</h1>\n" + "".join(svg_blocks) + "\n</section>")

    # HTML section (linked)
    html_blocks = []
    for label, fname in HTML_FILES.items():
        p = os.path.join(SPINE, fname)
        if os.path.isfile(p):
            html_blocks.append(f"<li><a href=\"{fname}\" target=\"_blank\">{label}</a></li>")
            print(f"✔ found HTML: {fname}")
        else:
            html_blocks.append(f"<li>{label} — missing ({fname})</li>")
            print(f"⚠ missing HTML: {fname}")
    sections.append("<section>\n<h1>HTML Dashboards</h1>\n<ul>\n" + "\n".join(html_blocks) + "\n</ul>\n</section>")

    # JSON fingerprint summary
    json_blocks = []
    for label, fname in JSON_FILES.items():
        p = os.path.join(SPINE, fname)
        if os.path.isfile(p):
            text = read_file(p)
            try:
                data = json.loads(text)
                module_count = len(data)
                json_blocks.append(f"<h2>{label}</h2>\n<p>File: {fname}</p>\n<p>Modules fingerprinted: {module_count}</p>\n")
                print(f"✔ found JSON: {fname} ({module_count} modules)")
            except:
                json_blocks.append(f"<h2>{label}</h2>\n<p>File: {fname}</p>\n<p>Could not parse JSON.</p>\n")
                print(f"⚠ JSON parse error: {fname}")
        else:
            json_blocks.append(f"<h2>{label}</h2>\n<p>Missing: {fname}</p>\n")
            print(f"⚠ missing JSON: {fname}")
    sections.append("<section>\n<h1>Structural Fingerprint</h1>\n" + "".join(json_blocks) + "\n</section>")

    html = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>TriadicFrameworks Structural Observatory</title>
<style>
body {{ font-family: system-ui; margin: 2rem; }}
h1 {{ margin-top: 2rem; }}
section {{ margin-bottom: 2rem; }}
object {{ margin-bottom: 1rem; }}
</style>
</head>
<body>
<h1>Structural Observatory</h1>
<p>This observatory aggregates canon‑wide structural instruments: triad‑purity, consistency maps, atlases, composites, and fingerprints.</p>
{''.join(sections)}
</body>
</html>
"""

    out = os.path.join(SPINE, "structural_observatory.html")
    with open(out, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"\n✔ Created {out}")
    print("\n✨ Structural observatory generated.\n")

if __name__ == "__main__":
    main()
