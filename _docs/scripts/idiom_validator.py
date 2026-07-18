"""
Idiom Dashboard Generator
-------------------------
Reads idiom_manifest.json, applies validator logic, and generates
Markdown + HTML dashboards showing mythmatical alignment scores.
"""

import json
from pathlib import Path
from idiom_validator import validate_idiom

def load_manifest(path="docs/registries/idiom_manifest.json"):
    with open(path, "r") as f:
        return json.load(f)

def generate_markdown(manifest, out_path="docs/charts/idiom_dashboard.md"):
    lines = []
    lines.append("# Mythmatical Idiom Dashboard\n")
    lines.append(f"**Protocol:** {manifest['protocol']}\n")

    for entry in manifest["entries"]:
        score = validate_idiom(entry)
        lines.append(f"## {entry['idiom']}")
        lines.append(f"- Forci: {entry['forci']}")
        lines.append(f"- Flui: {entry['flui']}")
        lines.append(f"- Freqi: {entry['freqi']}")
        lines.append(f"- Interpretation: {entry['interpretation']}")
        lines.append(f"- Alignment Score: {score}")
        lines.append("")
    Path(out_path).write_text("\n".join(lines))
    print(f"Markdown dashboard written to {out_path}")

def generate_html(manifest, out_path="docs/charts/idiom_dashboard.html"):
    html = []
    html.append("<html><head><title>Mythmatical Idiom Dashboard</title>")
    html.append("<style>body{font-family:Arial;margin:40px;} table{border-collapse:collapse;width:100%;} th,td{border:1px solid #ccc;padding:8px;text-align:left;} th{background:#f4f4f4;}</style>")
    html.append("</head><body>")
    html.append("<h1>Mythmatical Idiom Dashboard</h1>")
    html.append(f"<p><em>Protocol: {manifest['protocol']}</em></p>")

    html.append("<table>")
    html.append("<tr><th>Idiom</th><th>Forci</th><th>Flui</th><th>Freqi</th><th>Interpretation</th><th>Score</th></tr>")
    for entry in manifest["entries"]:
        score = validate_idiom(entry)
        html.append(f"<tr><td>{entry['idiom']}</td><td>{entry['forci']}</td><td>{entry['flui']}</td><td>{entry['freqi']}</td><td>{entry['interpretation']}</td><td>{score}</td></tr>")
    html.append("</table>")

    html.append("</body></html>")
    Path(out_path).write_text("\n".join(html))
    print(f"HTML dashboard written to {out_path}")

if __name__ == "__main__":
    manifest = load_manifest()
    generate_markdown(manifest)
    generate_html(manifest)
