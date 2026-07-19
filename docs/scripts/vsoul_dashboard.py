"""
vSoul Discovery Dashboard
-------------------------
Generates a Markdown or HTML dashboard of vSoul listings
filtered by clarity, rights, and amenities.
Part of RFC-014: vSoul Market Protocol
"""

import json
from typing import List, Dict, Any

def load_listings(path: str = "docs/registries/vsoul_listings.json") -> List[Dict[str, Any]]:
    with open(path, "r") as f:
        return json.load(f)

def generate_markdown(listings: List[Dict[str, Any]]) -> str:
    lines = []
    lines.append("| Listing ID | Partition | Clarity | Rights | Amenities | Audits |")
    lines.append("|------------|-----------|---------|--------|-----------|--------|")
    for l in listings:
        rights = ", ".join(l["rights_guarantees"])
        amenities = ", ".join(l["amenities"])
        audits = ", ".join(l["audit_refs"])
        lines.append(
            f"| {l['listing_id']} | {l['partition']} | {l['resonance_profile']['clarity_score']} "
            f"| {rights} | {amenities} | {audits} |"
        )
    return "\n".join(lines)

def generate_html(listings: List[Dict[str, Any]]) -> str:
    rows = []
    for l in listings:
        rights = ", ".join(l["rights_guarantees"])
        amenities = ", ".join(l["amenities"])
        audits = ", ".join(l["audit_refs"])
        rows.append(
            f"<tr><td>{l['listing_id']}</td><td>{l['partition']}</td>"
            f"<td>{l['resonance_profile']['clarity_score']}</td>"
            f"<td>{rights}</td><td>{amenities}</td><td>{audits}</td></tr>"
        )
    return (
        "<table border='1'>"
        "<tr><th>Listing ID</th><th>Partition</th><th>Clarity</th>"
        "<th>Rights</th><th>Amenities</th><th>Audits</th></tr>"
        + "".join(rows) + "</table>"
    )

if __name__ == "__main__":
    listings = load_listings()
    md = generate_markdown(listings)
    html = generate_html(listings)

    # Write outputs
    with open("docs/charts/vsoul_dashboard.md", "w") as f:
        f.write(md)
    with open("docs/charts/vsoul_dashboard.html", "w") as f:
        f.write(html)

    print("vSoul dashboards generated: vsoul_dashboard.md and vsoul_dashboard.html")
