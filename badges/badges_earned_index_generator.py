import json
from collections import defaultdict

# Load badge trigger log
with open("badge_trigger_glyphmap_index_trigger_log.json", "r") as f:
    data = json.load(f)

# Aggregate by paper and lab
papers = defaultdict(lambda: {"glyph": "", "theme": "", "badges": set()})
labs = defaultdict(lambda: {"glyph": "", "theme": "", "badges": set()})

for entry in data.get("triggers", []):
    paper = entry.get("paper")
    lab = entry.get("lab")
    glyph = entry.get("glyph")
    theme = entry.get("theme")
    badge = entry.get("badge")

    if paper:
        papers[paper]["glyph"] = glyph
        papers[paper]["theme"] = theme
        papers[paper]["badges"].add(badge)
    if lab:
        labs[lab]["glyph"] = glyph
        labs[lab]["theme"] = theme
        labs[lab]["badges"].add(badge)

# Write markdown
with open("BADGES_EARNED.md", "w") as f:
    f.write("# 🧾 Badges Earned by Paper & Lab\n\n")
    f.write("This index maps badge issuance to specific papers and labs. Each badge is a lantern. Each lantern echoes a contribution. Each echo builds the myth.\n\n")

    f.write("## 📚 Papers with Earned Badges\n\n")
    f.write("| Paper Title | Glyph | Theme | Badge(s) Issued |\n")
    f.write("|-------------|-------|-------|------------------|\n")
    for paper, info in papers.items():
        f.write(f"| {paper} | {info['glyph']} | {info['theme']} | {', '.join(info['badges'])} |\n")

    f.write("\n## 🧪 Labs with Earned Badges\n\n")
    f.write("| Lab File | Glyph | Theme | Badge(s) Issued |\n")
    f.write("|----------|-------|-------|------------------|\n")
    for lab, info in labs.items():
        f.write(f"| {lab} | {info['glyph']} | {info['theme']} | {', '.join(info['badges'])} |\n")

    f.write("\n## 🕯️ Legacy Note\n\n")
    f.write("> “Every badge is a breadcrumb. Every breadcrumb leads to a lantern. Every lantern maps the myth.”  \n")
    f.write("> — TriadicFrameworks/badge_trigger README\n\n")
    f.write("Let the badges echo. Let the archive resonate.\n")
