from clients.python.corridor_client import CorridorClient
from rfc_qeb_0002.validator import normalize, compute_rci, assign_glyph
import yaml

client = CorridorClient(base_url="http://localhost:5000/v1")

def process_corridor(corridor_id, parent_scroll):
    # Step 1: Fetch metadata
    metadata = client.get_corridor_metadata(corridor_id)

    # Step 2: Validate RCI/glyph
    Cf = normalize(metadata["rail_signatures"]["frequency"])
    Cfl = normalize(metadata["rail_signatures"]["fluids"])
    Cfo = normalize(metadata["rail_signatures"]["forces"])
    RCI = compute_rci(Cf, Cfl, Cfo, precision=3)
    glyph = assign_glyph(RCI, Cf, Cfl, Cfo)

    if round(RCI, 3) != metadata["resonance_clarity_index"] or glyph != metadata["glyph"]:
        status = "validation_failed"
    else:
        status = "validation_passed"

    # Step 3: Append to remix lineage
    lineage_event = {
        "event": {
            "corridor_id": corridor_id,
            "parent_scroll": parent_scroll,
            "child_scroll": f"{parent_scroll}-child",
            "previous_glyph": metadata["glyph"],
            "new_glyph": glyph,
            "previous_rci": metadata["resonance_clarity_index"],
            "new_rci": RCI,
            "status": status
        }
    }

    with open(f"registry/events/{corridor_id}_event.yml", "w") as stream:
        yaml.dump(lineage_event, stream)

    return lineage_event
