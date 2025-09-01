import os
from datetime import datetime

HONOR_ROLL_PATH = "docs/honor_roll/contributor_honor_roll.md"
BADGE = "🛡️ Manifest Guardian"
SCORE = "+5"

def get_contributor():
    return os.getenv("GITHUB_ACTOR", "unknown")

def update_honor_roll(contributor):
    timestamp = datetime.utcnow().strftime("%Y-%m-%d")
    entry = f"| {contributor} | {BADGE} | {SCORE} | {timestamp} |\n"

    with open(HONOR_ROLL_PATH, "r+") as f:
        lines = f.readlines()
        if entry not in lines:
            f.write(entry)

if __name__ == "__main__":
    contributor = get_contributor()
    update_honor_roll(contributor)
