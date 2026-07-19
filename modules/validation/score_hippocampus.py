# 🧠 Hippocampus Validator Scoring Script

def validate_makefile(path="docs/Hippocampus/Makefile.md"):
    score = 0
    with open(path, "r") as f:
        content = f.read()
        if "Reference Info" in content: score += 1
        if "🎯 Resume ritual" in content: score += 1
        if "📜 Capture context" in content: score += 1
        if "🔄 Playback memory" in content: score += 1
        if "🔭 Render dashboard" in content: score += 1
        if "🧹 Clear snapshot" in content: score += 1
    return score

if __name__ == "__main__":
    total = validate_makefile()
    print(f"[+] Hippocampus Makefile Score: {total}/6")
