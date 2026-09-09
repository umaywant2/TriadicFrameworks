import os
import json

ROOT = "docs"
SPINE = os.path.join(ROOT, "spine")

SVG_FILES = {
    "Triad‑Purity Heatmap": "triad_purity_heatmap.svg",
    "Consistency Map SVG": "consistency_map.svg",
    "Consistency Heatmap": "consistency_map_heatmap.svg",
    "Multi‑Atlas Composite": "multi_atlas_composite.svg",
    "Full Canon Graph SVG": "full_canon_graph_svg.svg",
    "Domain Graph SVG": "domain_graph_svg.svg",
}

HTML_FILES = {
    "Consistency Map HTML": "consistency_map.html",
    "Consistency Atlas": "consistency_atlas.html",
    "Structural Observatory": "structural_observatory.html",
    "Canon Purity Dashboard": "canon_purity_dashboard.html",
    "Tools Status Dashboard": "tools_status_dashboard.html",
}

JSON_FILES = {
    "Structural Fingerprint": "structural_fingerprint.json",
    "Canon Health Time‑Series": "canon_health_timeseries.json",
}

def read_file(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except:
        return None

def safe_json(path):
    text = read_file(path)
    if text is None:
        return None
    try:
        return json.loads(text)
    except:
        return None

def summarize_structural_fingerprint(data):
    if not isinstance(data, dict):
        return "Could not parse structural fingerprint."
    modules = len(data)
    with_triads = sum(1 for m in data.values() if m.get("blocks", {}).get("has_triads"))
    with_deps = sum(1 for m in data.values() if m.get("blocks", {}).get("has_dependencies"))
    return (
        f"Modules fingerprinted: {modules}. "
        f"Modules with triads: {with_triads}. "
        f"Modules with dependencies: {with_deps}."
    )

def summarize_timeseries(data):
    if not isinstance(data, list) or not data:
        return "No time‑series snapshots recorded yet."
    latest = data[-1]
    ts = latest.get("timestamp", "unknown")
    totals = latest.get("totals", {})
    scores = latest.get("scores", {})
    return (
        f"Latest snapshot: {ts}. "
        f"Modules: {totals.get('modules', 0)}, "
        f"Schema OK: {totals.get('schema_ok', 0)}, "
        f"Triads OK: {totals.get('triads_ok', 0)}, "
        f"Dependencies OK: {totals.get('dependencies_ok', 0)}. "
        f"Avg consistency score: {scores.get('average_consistency_score', 0):.2f}, "
        f"Max score: {scores.get('max_consistency_score', 0)}."
    )

def main():
    print("\n=== TriadicFrameworks Everything‑Composite Generator ===\n")

    os.makedirs(SPINE, exist_ok=True)
    sections = []

    # SVG section
    svg_blocks = []
    for label, fname in SVG_FILES.items():
        p = os.path.join(SPINE, fname)
        if os.path.isfile(p):
            svg_blocks.append(
                f"<h2>{label}</h2>\n"
                f"<object type=\"image/svg+xml\" data=\"{fname}\" "
                f"style=\"width:100%;border:1px solid #ddd;\"></object>\n"
            )
            print(f"✔ found SVG: {fname}")
        else:
            svg_blocks.append(f"<h2>{label}</h2>\n<p>Missing: {fname}</p>\n")
            print(f"⚠ missing SVG: {fname}")
    sections.append("<section>\n<h1>SVG Atlases, Heatmaps & Graphs</h1>\n" + "".join(svg_blocks) + "\n</section>")

    # HTML dashboards section
    html_blocks = []
    for label, fname in HTML_FILES.items():
        p = os.path.join(SPINE, fname)
        if os.path.isfile(p):
            html_blocks.append(f"<li><a href=\"{fname}\" target=\"_blank\">{label}</a></li>")
            print(f"✔ found HTML: {fname}")
        else:
            html_blocks.append(f"<li>{label} — missing ({fname})</li>")
            print(f"⚠ missing HTML: {fname}")
    sections.append("<section>\n<h1>HTML Dashboards & Observatories</h1>\n<ul>\n" + "\n".join(html_blocks) + "\n</ul>\n</section>")

    # JSON analytics section
    json_blocks = []
    for label, fname in JSON_FILES.items():
        p = os.path.join(SPINE, fname)
        if os.path.isfile(p):
            data = safe_json(p)
            if label == "Structural Fingerprint" and data is not None:
                summary = summarize_structural_fingerprint(data)
            elif label == "Canon Health Time‑Series" and data is not None:
                summary = summarize_timeseries(data)
            else:
                summary = "Could not parse JSON."
            json_blocks.append(
                f"<h2>{label}</h2>\n"
                f"<p>File: {fname}</p>\n"
                f"<p>{summary}</p>\n"
            )
            print(f"✔ found JSON: {fname}")
        else:
            json_blocks.append(f"<h2>{label}</h2>\n<p>Missing: {fname}</p>\n")
            print(f"⚠ missing JSON: {fname}")
    sections.append("<section>\n<h1>JSON Analytics & Health Metrics</h1>\n" + "".join(json_blocks) + "\n</section>")

    html = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>TriadicFrameworks Everything‑Composite Observatory</title>
<style>
body {{ font-family: system-ui; margin: 2rem; }}
h1 {{ margin-top: 2rem; }}
section {{ margin-bottom: 2rem; }}
object {{ margin-bottom: 1rem; }}
ul {{ list-style: disc; margin-left: 1.5rem; }}
</style>
</head>
<body>
<h1>Everything‑Composite Observatory</h1>
<p>
This observatory aggregates all major canon instruments: triad‑purity heatmaps, consistency maps, atlases, multi‑atlas composites,
full‑canon graphs, dashboards, structural fingerprints, and canon‑health time‑series metrics.
</p>
{''.join(sections)}
</body>
</html>
"""

    out = os.path.join(SPINE, "everything_composite.html")
    with open(out, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"\n✔ Created {out}")
    print("\n✨ Everything‑composite observatory generated.\n")

if __name__ == "__main__":
    main()
