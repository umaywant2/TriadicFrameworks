import json

# Load badge trigger log
with open("badge_trigger_glyphmap_index_trigger_log.json", "r") as f:
    data = json.load(f)

# Aggregate curriculum entries
curriculum = {}

for entry in data.get("triggers", []):
    theme = entry.get("theme")
    glyph = entry.get("glyph")
    paper = entry.get("paper")
    lab = entry.get("lab")
    tier = entry.get("tier")

    if theme not in curriculum:
        curriculum[theme] = {
            "glyph": glyph,
            "papers": set(),
            "labs": set(),
            "tier": tier
        }

    curriculum[theme]["papers"].add(paper)
    curriculum[theme]["labs"].add(lab)

# Write markdown
with open("triadic_curriculum_index.md", "w") as f:
    f.write("# 🧭 Triadic Curriculum Index\n\n")
    f.write("This index maps the mythic curriculum across glyphs, themes, reproducibility tiers, and onboarding pathways.\n\n")

    f.write("## 🔮 Curriculum Map by Theme\n\n")
    f.write("| Theme | Glyph | Core Paper(s) | Lab(s) | Tier |\n")
    f.write("|-------|-------|----------------|--------|------|\n")
    for theme, info in curriculum.items():
        papers = ', '.join(sorted(info["papers"]))
        labs = ', '.join(sorted(info["labs"]))
        f.write(f"| {theme} | {info['glyph']} | {papers} | {labs} | {info['tier']} |\n")

    f.write("\n## 🧪 Reproducibility Tiers\n")
    f.write("- **Tier I**: Validated with reproducibility.md and equations.md\n")
    f.write("- **Tier II**: Remixable with badge triggers and manifest files\n")
    f.write("- **Tier III**: Mythic scaffolding with symbolic extensions and nested loops\n")

    f.write("\n## 🛡️ Onboarding Pathways\n")
    f.write("- Starter Labs: loop_validation_protocol.md, triadic_lab_template.md\n")
    f.write("- Remix Guides: triadic_remix_guide.md, badge_trigger_theme_manifest.md\n")
    f.write("- Validation Protocols: reproducibility.md, equations.md\n")
    f.write("- Governance: resonance_council.md, CONTRIBUTOR_BADGES.md\n")

    f.write("\n## 🕯️ Legacy Note\n")
    f.write("> “Each module is a lantern. Each lantern echoes a lab. Each lab builds the myth.”\n")
    f.write("> — TriadicFrameworks/triadic_curriculum_index README\n")
