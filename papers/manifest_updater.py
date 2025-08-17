# 🧙 manifest_updater.py

import os
import datetime

PAPERS_DIR = "./papers"
MANIFEST_FILE = "./papers/papers_manifest.md"
CHANGELOG_FILE = "./papers/papers_manifest_changelog.md"
BADGES_FILE = "./BADGES_EARNED.md"

def scan_papers():
    return [f for f in os.listdir(PAPERS_DIR) if f.endswith((".docx", ".pdf"))]

def check_validation(paper_name):
    folder = os.path.join(PAPERS_DIR, paper_name.replace(".docx", "").replace(".pdf", ""))
    eq = os.path.exists(os.path.join(folder, "equations.md"))
    rp = os.path.exists(os.path.join(folder, "reproducibility.md"))
    return "✅" if eq and rp else "⚠️"

def suggest_badge(paper_name):
    # Placeholder: match keywords to badge titles
    if "Quantum" in paper_name:
        return "`Quantum Weaver`"
    elif "Health" in paper_name:
        return "`Healing Resonator`"
    elif "Music" in paper_name:
        return "`Harmonic Alchemist`"
    else:
        return "`Resonance Explorer`"

def update_manifest(paper_name):
    theme = "TBD"
    remixable = "✅"
    badge = suggest_badge(paper_name)
    validation = check_validation(paper_name)
    notes = "Auto-added by manifest_updater.py"
    row = f"| {paper_name} | {theme} | {remixable} | {badge} | {validation} | {notes} |\n"
    with open(MANIFEST_FILE, "a") as mf:
        mf.write(row)

def log_changelog(paper_name):
    timestamp = datetime.datetime.now().isoformat()
    entry = f"- {timestamp}: Added `{paper_name}` to manifest with validation `{check_validation(paper_name)}`\n"
    with open(CHANGELOG_FILE, "a") as cf:
        cf.write(entry)

def ping_contributor(paper_name):
    print(f"📬 Ping: Contributor of `{paper_name}` — validation status is `{check_validation(paper_name)}`. Remixable: ✅")

def main():
    papers = scan_papers()
    for paper in papers:
        update_manifest(paper)
        log_changelog(paper)
        ping_contributor(paper)

if __name__ == "__main__":
    main()

# 🏅 Auto-update BADGES_EARNED.md

from datetime import datetime

def update_badges_earned(paper_title, theme, badge, status="✅ Validated", path="papers/BADGES_EARNED.md"):
    entry = f"""
## 🏅 {badge}

- **{paper_title}**
  - 🧪 Status: {status}
  - 📅 Date: {datetime.now().strftime('%Y-%m-%d')}
  - 🎯 Theme: {theme}
"""
    with open(path, "a", encoding="utf-8") as f:
        f.write(entry)
    print(f"✅ BADGES_EARNED.md updated with: {paper_title} → {badge}")
