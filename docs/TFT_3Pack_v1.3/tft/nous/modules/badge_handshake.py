import json
from datetime import datetime

def issue_badge(initiator, recipient, badge_type, glyph, corridor, notes):
    handshake = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "initiator": initiator,
        "recipient": recipient,
        "badge_type": badge_type,
        "glyph": glyph,
        "corridor": corridor,
        "notes": notes,
        "status": "handshake_complete"
    }
    return handshake

def save_handshake(handshake, path="../outputs/badge_handshake.txt"):
    with open(path, "a") as file:
        file.write(json.dumps(handshake) + "\n")

if __name__ == "__main__":
    badge = issue_badge(
        initiator="professor_bot",
        recipient="validator_bot",
        badge_type="remix_trust",
        glyph="🪙",
        corridor="Remix Economy",
        notes="Scroll lineage confirmed. Remix rights honored."
    )
    save_handshake(badge)
    print("🪙 Badge handshake complete.")

