import datetime, uuid

def add_signature(scroll, contributor_id, signature):
    sig_entry = {
        "contributor_id": contributor_id,
        "signature": signature,
        "timestamp": datetime.datetime.utcnow().isoformat()
    }
    if "signatures" not in scroll["remix_scroll"]:
        scroll["remix_scroll"]["signatures"] = {"contributors": []}
    scroll["remix_scroll"]["signatures"]["contributors"].append(sig_entry)
    return scroll

# Example usage
# scroll = {...}  # remix scroll artifact
# scroll = add_signature(scroll, "user42", "pgp-signature-placeholder")
# scroll = add_signature(scroll, "user17", "ecdsa-signature-placeholder")
