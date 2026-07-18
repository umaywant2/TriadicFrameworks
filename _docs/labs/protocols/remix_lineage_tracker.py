import json
from datetime import datetime

def log_remix(contributor, fold_id, remix_id, badge):
    entry = {
        "contributor": contributor,
        "fold": fold_id,
        "remix": remix_id,
        "badge": badge,
        "timestamp": datetime.utcnow().isoformat()
    }

    with open("honor_roll/honor_roll_ledger.json", "r+") as file:
        data = json.load(file)
        data.append(entry)
        file.seek(0)
        json.dump(data, file, indent=2)

    print(f"Remix logged for {contributor} with badge {badge}.")
