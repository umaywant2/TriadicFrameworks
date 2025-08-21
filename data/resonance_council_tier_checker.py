import json

# Load badge trigger log
with open("badge_trigger_glyphmap_index_trigger_log.json", "r") as f:
    data = json.load(f)

# Aggregate contributor stats
contributors = {}

for entry in data.get("triggers", []):
    name = entry.get("contributor")
    role = entry.get("role")
    badge = entry.get("badge")
    lab = entry.get("lab")

    if name not in contributors:
        contributors[name] = {"badges": set(), "validated_labs": set(), "remixes": 0}

    contributors[name]["badges"].add(badge)
    if role == "validator" and lab:
        contributors[name]["validated_labs"].add(lab)
    if role == "remixer":
        contributors[name]["remixes"] += 1

# Assign tiers
def assign_tier(stats):
    badges = len(stats["badges"])
    labs = len(stats["validated_labs"])
    remixes = stats["remixes"]

    if badges >= 10 and labs >= 3 and remixes >= 1:
        return "🥇 Gold"
    elif badges >= 5 and labs >= 1:
        return "🥈 Silver"
    elif badges >= 1:
        return "🥉 Bronze"
    else:
        return "🔍 Observer"

# Output council roster
with open("resonance_council_roster.md", "w") as f:
    f.write("# 🏛️ Resonance Council Roster\n\n")
    f.write("| Name | Badges | Validated Labs | Remixes | Tier |\n")
    f.write("|------|--------|----------------|---------|------|\n")
    for name, stats in contributors.items():
        tier = assign_tier(stats)
        f.write(f"| {name} | {len(stats['badges'])} | {len(stats['validated_labs'])} | {stats['remixes']} | {tier} |\n")
