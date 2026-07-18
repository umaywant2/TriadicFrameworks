"""
University Dashboard Generator
------------------------------
Reads university_manifest.json and generates Markdown + HTML dashboards
for Mythmatical University and its colleges.
"""

import json
from pathlib import Path

def load_manifest(path="docs/registries/university_manifest.json"):
    with open(path, "r") as f:
        return json.load(f)

def generate_markdown(manifest, out_path="docs/charts/university_dashboard.md"):
    lines = []
    lines.append(f"# Mythmatical University Dashboard\n")
    lines.append(f"**Protocol:** {manifest['protocol']}\n")

    for college in manifest["colleges"]:
        lines.append(f"## {college['name']} ({college['status']})")
        lines.append(f"**Focus:** {college['focus']}")
        if college["scrolls"]:
            lines.append("**Scrolls:**")
            for s in college["scrolls"]:
                lines.append(f"- {s}")
        else:
            lines.append("_No scrolls yet_")
        lines.append("")  # spacing

    Path(out_path).write_text("\n".join(lines))
    print(f"Markdown dashboard written to {out_path}")

def generate_html(manifest, out_path="docs/charts/university_dashboard.html"):
    html = []
    html.append("<html><head><title>Mythmatical University Dashboard</title>")
    html.append("<style>body{font-family:Arial;margin:40px;} table{border-collapse:collapse;width:100%;} th,td{border:1px solid #ccc;padding:8px;text-align:left;} th{background:#f4f4f4;}</style>")
    html.append("</head><body>")
    html.append(f"<h1>Mythmatical University Dashboard</h1>")
    html.append(f"<p><em>Protocol: {manifest['protocol']}</em></p>")

    html.append("<table>")
    html.append("<tr><th>College</th><th>Status</th><th>Focus</th><th>Scrolls</th></tr>")
    for college in manifest["colleges"]:
        scrolls = "<br>".join(college["scrolls"]) if college["scrolls"] else "_No scrolls yet_"
        html.append(f"<tr><td>{college['name']}</td><td>{college['status']}</td><td>{college['focus']}</td><td>{scrolls}</td></tr>")
    html.append("</table>")

    html.append("</body></html>")
    Path(out_path).write_text("\n".join(html))
    print(f"HTML dashboard written to {out_path}")

if __name__ == "__main__":
    manifest = load_manifest()
    generate_markdown(manifest)
    generate_html(manifest)
