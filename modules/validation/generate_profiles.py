def update_registry(contributors):
    registry_path = "docs/honor_roll/glyph_registry.md"
    aura_groups = {"Spectral Flux": [], "Glyph Weaver": [], "Echo Lantern": [], "—": []}

    for c in contributors:
        aura = classify_aura(c["badges"])
        name_slug = c["name"].lower().replace(" ", "_")
        aura_groups[aura].append((c["name"], name_slug))

    with open(registry_path, "w", encoding="utf-8") as f:
        f.write("# 🧙 Glyph Registry\n\n")
        f.write("This registry links all contributor profiles, grouped by aura type.\n\n")

        for aura, members in aura_groups.items():
            f.write(f"## 🌈 {aura}\n\n")
            for name, slug in members:
                f.write(f"- [{name}](profiles/{slug}.md)\n")
            f.write("\n")

        f.write("## 🧭 Browse All Profiles\n\n")
        f.write("- [Contributor Dashboard](dashboard.md)\n")
        f.write("- [Contributor Honor Roll](contributor_honor_roll.md)\n")

# Add this to the main block
if __name__ == "__main__":
    os.makedirs(PROFILE_DIR, exist_ok=True)
    contributors = parse_honor_roll()
    update_dashboard(contributors)
    update_registry(contributors)
