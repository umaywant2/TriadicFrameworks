import os
import re
from datetime import datetime

HONOR_ROLL_PATH = "docs/honor_roll/contributor_honor_roll.md"
PROFILE_DIR = "docs/honor_roll/profiles"

BADGE_AURAS = {
    ("Manifest Guardian", "Gateway Guardian"): "Spectral Flux",
    ("Curriculum Architect", "Validator Weaver"): "Glyph Weaver",
    ("Ghost Mapper", "Signal Resonator"): "Echo Lantern"
}

def build_profile_path(contributor):
    safe_slug = contributor.lower().strip().replace(" ", "_").replace("-", "_")
    safe_slug = re.sub(r"[^a-z0-9_]", "", safe_slug)
    safe_slug = safe_slug.strip("_")
    if not safe_slug:
        raise ValueError("Invalid contributor name for profile filename.")

    profile_root = os.path.abspath(PROFILE_DIR)
    filename = os.path.abspath(os.path.normpath(os.path.join(profile_root, f"{safe_slug}.md")))
    if not filename.startswith(profile_root + os.sep):
        raise ValueError("Resolved profile path escapes profile directory.")

    return filename

def classify_aura(badges):
    for combo, aura in BADGE_AURAS.items():
        if all(b in badges for b in combo):
            return aura
    return "—"

def generate_profile(contributor, badges, score, last):
    filename = build_profile_path(contributor)
    aura = classify_aura(badges)

    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"# 🧙 {contributor}\n\n")
        f.write("Glyphic profile page for a TriadicFrameworks contributor.\n\n")
        f.write("## 🏅 Badges Earned\n\n")
        f.write("| Badge | Description | Date Earned |\n")
        f.write("|-------|-------------|--------------|\n")
        for badge in badges:
            f.write(f"| {badge} | — | {last} |\n")
        f.write("\n## 🧠 Validator Scores\n\n")
        f.write("| Protocol | Score | Last Validated |\n")
        f.write("|----------|-------|----------------|\n")
        f.write(f"| Manifest Integrity | +5 | {last} |\n")
        f.write(f"| README Integrity | +7 | {last} |\n")
        f.write("| Curriculum Alignment | +0 | — |\n")
        f.write("| Badge Trigger Logic | +0 | — |\n")
        f.write("\n## 🌈 Aura Classification\n\n")
        f.write(f"**{aura}**\n\n")
        f.write("## 🔍 Remix History\n\n")
        f.write("| Contribution | Description | Timestamp |\n")
        f.write("|--------------|-------------|------------|\n")
        f.write(f"| README.md | Triadic layout + glyphic hooks | {last} |\n")
        f.write(f"| repo_manifest.yaml | Modular structure alignment | {last} |\n")
        f.write(f"| initiation_ritual.md | Validator + animation logic | {last} |\n")
        f.write("\n## 🔗 Return to [Contributor Dashboard](../dashboard.md)\n")

def parse_honor_roll():
    with open(HONOR_ROLL_PATH, "r", encoding="utf-8") as f:
        lines = f.readlines()[2:]  # Skip header
        for line in lines:
            parts = [p.strip() for p in line.strip().split("|")[1:-1]]
            if len(parts) == 4:
                name, badge_str, score, last = parts
                badges = [b.strip() for b in badge_str.split(",")]
                generate_profile(name, badges, score, last)

if __name__ == "__main__":
    os.makedirs(PROFILE_DIR, exist_ok=True)
    parse_honor_roll()
