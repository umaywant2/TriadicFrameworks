def validate_resume(path="copilot_hippocampus/RESUME_Copilot.py"):
    score = 0
    with open(path, "r") as f:
        content = f.read()
        if "SNAPSHOT_PATH" in content: score += 1
        if "resume_context()" in content: score += 1
        if "render_dashboard()" in content: score += 1
        if "Observatory Dashboard" in content: score += 1
    return score

if __name__ == "__main__":
    total = validate_resume()
    print(f"[+] Resume Script Score: {total}/4")
