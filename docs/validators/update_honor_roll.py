# 🏅 Honor Roll Updater
# Echoes contributor achievements into symbolic honor roll

import json

def update_honor_roll(contributor_id, badge_name, honor_roll_path):
    try:
        with open(honor_roll_path, 'r') as f:
            honor_roll = json.load(f)
    except FileNotFoundError:
        honor_roll = []

    honor_roll.append({
        "contributor_id": contributor_id,
        "badge": badge_name,
        "timestamp": "2025-09-26T04:55:00Z"
    })

    with open(honor_roll_path, 'w') as f:
        json.dump(honor_roll, f, indent=2)

    print(f"✅ Honor roll updated for {contributor_id} → {badge_name}")
