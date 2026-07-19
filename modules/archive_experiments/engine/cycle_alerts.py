import yaml, uuid, datetime

def generate_alert(scroll_id, from_stage, to_stage, status, contributors):
    alert = {
        "alert": {
            "id": str(uuid.uuid4()),
            "timestamp": datetime.datetime.utcnow().isoformat(),
            "scroll_id": scroll_id,
            "from_stage": from_stage,
            "to_stage": to_stage,
            "status": status,
            "contributor_targets": contributors,
            "message": f"Scroll {scroll_id} transitioned {from_stage} → {to_stage} ({status})",
            "checksum": str(uuid.uuid4())[:8]  # placeholder checksum
        }
    }

    outfile = f"registry/alerts/{scroll_id}_alert.yml"
    with open(outfile, "w") as stream:
        yaml.dump(alert, stream, sort_keys=False)

    return alert

# Example usage
# generate_alert("scroll-010", "remix", "export", "validation_passed", ["user42","user17"])
