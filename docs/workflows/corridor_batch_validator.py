import yaml
import datetime
from clients.python.corridor_client import CorridorClient
from rfc_qeb_0002.validator import normalize, compute_rci, assign_glyph

client = CorridorClient(base_url="http://localhost:5000/v1")

def process_corridor(corridor_id, parent_scroll):
    metadata = client.get_corridor_metadata(corridor_id)

    Cf = normalize(metadata["rail_signatures"]["frequency"])
    Cfl = normalize(metadata["rail_signatures"]["fluids"])
    Cfo = normalize(metadata["rail_signatures"]["forces"])
    RCI = compute_rci(Cf, Cfl, Cfo, precision=3)
    glyph = assign_glyph(RCI, Cf, Cfl, Cfo)

    status = "validation_passed" if (
        round(RCI, 3) == metadata["resonance_clarity_index"] and glyph == metadata["glyph"]
    ) else "validation_failed"

    return {
        "corridor_id": corridor_id,
        "parent_scroll": parent_scroll,
        "child_scroll": f"{parent_scroll}-{corridor_id}",
        "previous_glyph": metadata["glyph"],
        "new_glyph": glyph,
        "previous_rci": metadata["resonance_clarity_index"],
        "new_rci": RCI,
        "status": status,
    }

def batch_process(corridor_ids, parent_scroll):
    events = [process_corridor(cid, parent_scroll) for cid in corridor_ids]

    # Summary statistics
    glyph_counts = {}
    band_counts = {"low": 0, "medium": 0, "high": 0}
    for ev in events:
        glyph_counts[ev["new_glyph"]] = glyph_counts.get(ev["new_glyph"], 0) + 1
        if ev["new_rci"] <= 0.33:
            band_counts["low"] += 1
        elif ev["new_rci"] <= 0.66:
            band_counts["medium"] += 1
        else:
            band_counts["high"] += 1

    report = {
        "remixathon_report": {
            "timestamp": datetime.datetime.utcnow().isoformat(),
            "parent_scroll": parent_scroll,
            "events": events,
            "summary": {
                "glyph_distribution": glyph_counts,
                "rci_band_counts": band_counts,
                "validation_passed": sum(1 for e in events if e["status"] == "validation_passed"),
                "validation_failed": sum(1 for e in events if e["status"] == "validation_failed"),
            },
        }
    }

    outfile = f"registry/reports/remixathon_{datetime.datetime.utcnow().strftime('%Y%m%d_%H%M%S')}.yml"
    with open(outfile, "w") as stream:
        yaml.dump(report, stream, sort_keys=False)

    return report
