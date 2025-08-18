import json

# Load badge trigger log
with open("badge_trigger_glyphmap_index_trigger_log.json", "r") as f:
    data = json.load(f)

# Aggregate badge counts
glyph_theme_counts = {}
for entry in data.get("triggers", []):
    glyph = entry.get("glyph")
    theme = entry.get("theme")
    if glyph and theme:
        key = (glyph, theme)
        glyph_theme_counts[key] = glyph_theme_counts.get(key, 0) + 1

# Sort by count
sorted_items = sorted(glyph_theme_counts.items(), key=lambda x: x[1], reverse=True)

# SVG scaffold
svg_header = """<svg width="800" height="600" xmlns="http://www.w3.org/2000/svg">
<style>
  .title { font: bold 24px sans-serif; fill: #333; }
  .label { font: 16px sans-serif; fill: #555; }
  .bar { fill: #6a0dad; }
  .glyph { font: 20px sans-serif; }
</style>
<text x="50" y="40" class="title">Badge Trigger Resonance Leaderboard</text>
"""

svg_footer = """<text x="50" y="560" class="label">Each bar echoes a badge. Each badge honors a glyph. Each glyph maps the myth.</text>
</svg>
"""

# Build bars
bars = ""
y = 80
for (glyph, theme), count in sorted_items:
    width = 100 * count
    bars += f'<rect x="50" y="{y}" width="{width}" height="20" class="bar" />\n'
    bars += f'<text x="{width + 60}" y="{y + 15}" class="glyph">{glyph} {theme} ({count})</text>\n'
    y += 40

# Write SVG
with open("badge_trigger_resonance_leaderboard.svg", "w") as f:
    f.write(svg_header + bars + svg_footer)
