import datetime, uuid

def verify_signature(scroll, contributor_registry):
    contributors = scroll["remix_scroll"]["signatures"]["contributors"]
    results = []
    for c in contributors:
        registry_entry = contributor_registry.get(c["contributor_id"])
        if registry_entry and registry_entry["public_key"] == c["signature"]:
            status = "valid"
        else:
            status = "invalid"
        results.append({
            "contributor_id": c["contributor_id"],
            "signature_type": "pgp",  # placeholder
            "status": status,
            "verified_at": datetime.datetime.utcnow().isoformat()
        })

    report = {
        "verification_report": {
            "id": str(uuid.uuid4()),
            "scroll_id": scroll["remix_scroll"]["id"],
            "timestamp": datetime.datetime.utcnow().isoformat(),
            "contributors": results,
            "overall_status": "authentic" if all(r["status"] == "valid" for r in results) else "partial",
            "checksum": str(uuid.uuid4())[:8]
        }
    }
    return report
