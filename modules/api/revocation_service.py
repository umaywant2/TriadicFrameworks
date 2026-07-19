import datetime, uuid

def revoke_signature(scroll_id, contributor_id, signature, reason):
    event = {
        "revocation_event": {
            "id": str(uuid.uuid4()),
            "scroll_id": scroll_id,
            "contributor_id": contributor_id,
            "revoked_signature": signature,
            "reason": reason,
            "timestamp": datetime.datetime.utcnow().isoformat(),
            "replacement_signature": None,
            "status": "revoked",
            "checksum": str(uuid.uuid4())[:8]
        }
    }
    return event

def resign_signature(event, new_signature):
    event["revocation_event"]["replacement_signature"] = new_signature
    event["revocation_event"]["status"] = "re-signed"
    return event
