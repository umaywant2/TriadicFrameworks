import yaml

def load_registry():
    with open("registry/reports/remixathon_latest.yml", "r") as stream:
        return yaml.safe_load(stream)["remixathon_report"]

def search_corridors(query):
    report = load_registry()
    results = []

    for ev in report["events"]:
        match = True

        # Glyph filter
        if query.get("glyph") and ev["new_glyph"] != query["glyph"]:
            match = False

        # Tag filter
        if query.get("tags"):
            corridor_tags = ev.get("tags", [])
            if not set(query["tags"]).issubset(set(corridor_tags)):
                match = False

        # RCI band filter
        if query.get("rci_band"):
            rci = ev["new_rci"]
            band = "low" if rci <= 0.33 else "medium" if rci <= 0.66 else "high"
            if band != query["rci_band"]:
                match = False

        # Lineage filter
        if query.get("lineage"):
            lineage = query["lineage"]
            if lineage.get("parent_scroll") and ev["parent_scroll"] != lineage["parent_scroll"]:
                match = False
            if lineage.get("child_scroll") and ev["child_scroll"] != lineage["child_scroll"]:
                match = False

        if match:
            results.append(ev)

    return results
