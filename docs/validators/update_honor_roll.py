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

import os
from datetime import datetime

HONOR_ROLL_PATH = "docs/honor_roll/contributor_honor_roll.md"
README_PATH = "README.md"
BADGE = "🧭 Gateway Guardian"
SCORE = "+7"

def get_contributor():
    return os.getenv("GITHUB_ACTOR", "unknown")

def read_honor_roll():
    with open(HONOR_ROLL_PATH, "r", encoding="utf-8") as f:
        return f.readlines()

def update_honor_roll(contributor):
    timestamp = datetime.utcnow().strftime("%Y-%m-%d")
    entry_line = f"| {contributor} | {BADGE} | {SCORE} | {timestamp} |\n"
    lines = read_honor_roll()

    if entry_line not in lines:
        with open(HONOR_ROLL_PATH, "a", encoding="utf-8") as f:
            f.write(entry_line)

def readme_was_edited():
    try:
        with open(".git/HEAD", "r") as head:
            ref = head.read().strip().split(" ")[-1]
        with open(f".git/{ref}", "r") as commit_file:
            commit_hash = commit_file.read().strip()
        diff = os.popen(f"git diff-tree --no-commit-id --name-only -r {commit_hash}").read()
        return README_PATH in diff
    except:
        return False

if __name__ == "__main__":
    contributor = get_contributor()
    if readme_was_edited():
        update_honor_roll(contributor)
