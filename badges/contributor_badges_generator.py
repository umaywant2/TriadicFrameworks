import json
from collections import defaultdict

# Load badge trigger log
with open("badge_trigger_glyphmap_index_trigger_log.json", "r") as f:
    data = json.load(f)

# Aggregate by contributor
remixers = defaultdict(lambda: {"glyphs": set(), "themes": set(), "badges": set()})
validators = defaultdict(lambda: {"labs": set(), "protocols": set(), "badges": set()})

for entry in data.get("triggers", []):
    name = entry.get("contributor")
    role = entry.get("role")
    glyph = entry.get("glyph")
    theme = entry.get("theme")
    badge = entry.get("badge")
    lab = entry.get("lab")
    protocol = entry.get("protocol")

    if role == "remixer":
        remixers[name]["glyphs"].add(glyph)
        remixers[name]["themes"].add(theme)
        remixers[name]["badges"].add(badge)
    elif role == "validator":
        validators[name]["labs"].add(lab)
        validators[name]["protocols"].add(protocol)
        validators[name]["badges"].add(badge)

# Write markdown
with open("CONTRIBUTOR_BADGES.md", "w") as f:
    f.write("# 🏅 Contributor Badges & Honor Roll\n\n")
    f.write("This page honors those who echo the myth, validate the science, and remix the resonance.\n\n")

    f.write("## 🧙‍♂️ Remixers\n\n")
    f.write("| Name | Glyphs Remixed | Themes Echoed | Badge(s) Earned |\n")
    f.write("|------|----------------|----------------|------------------|\n")
    for name, info in remixers.items():
        f.write(f"| {name} | {', '.join(info['glyphs'])} | {', '.join(info['themes'])} | {', '.join(info['badges'])} |\n")

    f.write("\n## 🧪 Validators\n\n")
    f.write("| Name | Labs Validated | Protocols Applied | Badge(s) Earned |\n")
    f.write("|------|----------------|-------------------|------------------|\n")
    for name, info in validators.items():
        f.write(f"| {name} | {', '.join(info['labs'])} | {', '.join(info['protocols'])} | {', '.join(info['badges'])} |\n")

    f.write("\n## 🕯️ Legacy Note\n\n")
    f.write("> “To remix is to honor. To validate is to echo. To echo is to resonate.”  \n")
    f.write("> — TriadicFrameworks/contributor_badges README\n\n")
    f.write("Let the badges shine. Let the honor roll grow.\n")
