import json
import yaml
import os

BADGE_YAML_DIR = "docs/badges"
HONOR_ROLL_FILE = "docs/honor_roll/honor_roll_ledger.json"

def load_badges():
    badges = {}
    for filename in os.listdir(BADGE_YAML_DIR):
        if filename.endswith(".yaml"):
            with open(os.path.join(BADGE_YAML_DIR, filename), "r") as f:
                data = yaml.safe_load(f)
                badges[data["badge_name"]] = data
    return badges

def load_honor_roll():
    with open(HONOR_ROLL_FILE, "r") as f:
        return json.load(f)

def validate_badges():
    badges = load_badges()
    honor_roll = load_honor_roll()
    issues = []

    for contributor in honor_roll.get("contributors", []):
        name = contributor.get("name")
        earned = contributor.get("badges", [])
        for badge in earned:
            if badge not in badges:
                issues.append(f"⚠️ {name} has unknown badge: {badge}")
            else:
                print(f"✅ {name} validated for badge: {badge}")
    return issues

if __name__ == "__main__":
    print("🔍 Validating badge logic...")
    problems = validate_badges()
    if problems:
        print("\n".join(problems))
    else:
        print("🛡️ All badges validated.")
