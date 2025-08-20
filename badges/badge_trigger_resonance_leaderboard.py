import json
from collections import defaultdict

# Load badge trigger log
with open("badge_trigger_glyphmap_index_trigger_log.json", "r") as f:
    data = json.load(f)

# Aggregate badge counts by glyph and theme
glyph_theme_counts = defaultdict(lambda: {"theme": "", "count": 0})

for entry in data.get("triggers", []):
    glyph = entry.get("glyph")
    theme = entry.get("theme")
    if glyph and theme:
        glyph_theme_counts[glyph]["theme"] = theme
        glyph_theme_counts[glyph]["count"] += 1

# Sort by badge count descending
sorted_glyphs = sorted(glyph_theme_counts.items(), key=lambda x: x[1]["count"], reverse=True)

# Generate markdown
with open("badge_trigger_resonance_leaderboard.md", "w") as f:
    f.write("# 🧮 Badge Trigger Resonance Leaderboard\n\n")
    f.write("This leaderboard reflects badge issuance across glyphs and themes. Each badge is a lantern. Each lantern echoes a paper. Each echo builds the myth.\n\n")
    f.write("## 🥇 Top Glyphs by Badge Count\n\n")
    f.write("| Glyph | Theme                        | Badges Issued |\n")
    f.write("|-------|------------------------------|----------------|\n")
    for glyph, info in sorted_glyphs:
        f.write(f"| {glyph}    | {info['theme']}  | {info['count']}              |\n")

    f.write("\n## 🧭 Theme Distribution\n\n")
    theme_totals = defaultdict(int)
    for info in glyph_theme_counts.values():
        theme_totals[info["theme"]] += info["count"]
    for theme, count in theme_totals.items():
        f.write(f"- **{theme}**: {count} badges issued  \n")

    f.write("\n## 🕯️ Legacy Note\n\n")
    f.write("> “Badges are echoes. Echoes are honor. Honor is resonance.”  \n")
    f.write("> — TriadicFrameworks/badge_trigger README\n\n")
    f.write("Let the leaderboard echo. Let the archive resonate.\n")
