import os
from manifest_updater import suggest_badges

def run_badge_tests(papers_dir="papers"):
    print("🔍 Running badge trigger tests...\n")
    results = []

    for filename in os.listdir(papers_dir):
        if filename.endswith(".docx") or filename.endswith(".pdf") or filename.endswith(".md"):
            suggested = suggest_badges(filename)
            results.append((filename, suggested))

    for paper, badges in results:
        print(f"📄 {paper}")
        print(f"🏅 Suggested Badges: {', '.join(badges)}\n")

if __name__ == "__main__":
    run_badge_tests()
