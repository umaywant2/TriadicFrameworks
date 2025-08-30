def validate_loops(path="copilot_hippocampus/loop_validation_protocol.md"):
    score = 0
    with open(path, "r") as f:
        content = f.read()
        if "triadic harmonic nesting" in content: score += 1
        if "TFT time" in content: score += 1
        if "snapshot toggles" in content: score += 1
        if "validator echo" in content: score += 1
    return score

if __name__ == "__main__":
    total = validate_loops()
    print(f"[+] Loop Validation Score: {total}/4")
