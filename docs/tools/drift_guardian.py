import os
import json
import argparse
import requests

EXPECTED_CANON_REF = "/docs/spine/spine.json"

EXPECTED_INHERIT = {
    "canon": True,
    "session_context": True,
    "triad_alias_resolution": True
}

EXPECTED_RTT = {
    "layer": 1,
    "source": "https://www.triadicframeworks.org/_ideas/Resonance-Time_Theory.html"
}

EXPECTED_AI_INIT = {
    "load_spine_first": True,
    "load_canon_first": True,
    "apply_session_context": True,
    "triad_validation": True
}

# ---------------------------------------------------------
# DRIFT SCORING
# ---------------------------------------------------------
def score_drift(errors):
    count = len(errors)
    if count == 0: return 0
    if count <= 2: return 1
    if count <= 4: return 2
    if count <= 7: return 3
    return 4

def drift_label(score):
    return {
        0: "Pure",
        1: "Low Drift",
        2: "Moderate Drift",
        3: "High Drift",
        4: "Critical Drift"
    }[score]

def drift_color(score):
    return {
        0: "🟩",
        1: "🟨",
        2: "🟧",
        3: "🟥",
        4: "⬛"
    }[score]

# ---------------------------------------------------------
# VALIDATION
# ---------------------------------------------------------
def validate_module_json(data):
    module = data.get("module", {})
    errors = []

    if module.get("canon_ref") != EXPECTED_CANON_REF:
        errors.append("canon_ref mismatch")

    inherit = module.get("inherit", {})
    for key, expected in EXPECTED_INHERIT.items():
        if inherit.get(key) != expected:
            errors.append(f"inherit.{key} mismatch")

    rtt = module.get("rtt", {})
    for key, expected in EXPECTED_RTT.items():
        if rtt.get(key) != expected:
            errors.append(f"rtt.{key} mismatch")

    ai = module.get("ai", {}).get("initialization", {})
    for key, expected in EXPECTED_AI_INIT.items():
        if ai.get(key) != expected:
            errors.append(f"ai.initialization.{key} mismatch")

    return errors

# ---------------------------------------------------------
# GITHUB API HELPERS
# ---------------------------------------------------------
def github_get(url, token):
    return requests.get(url, headers={"Authorization": f"token {token}"}).json()

def github_post(url, token, payload):
    return requests.post(url, headers={"Authorization": f"token {token}"}, json=payload)

# ---------------------------------------------------------
# MAIN BOT LOGIC
# ---------------------------------------------------------
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo")
    parser.add_argument("--pr")
    args = parser.parse_args()

    token = os.environ["GITHUB_TOKEN"]

    pr_files_url = f"https://api.github.com/repos/{args.repo}/pulls/{args.pr}/files"
    files = github_get(pr_files_url, token)

    drift_results = []

    for f in files:
        filename = f["filename"]

        if not filename.endswith("module.json"):
            continue

        raw_url = f["raw_url"]
        data = requests.get(raw_url).json()

        errors = validate_module_json(data)
        score = score_drift(errors)

        drift_results.append((filename, errors, score))

        # Inline comments for each error
        for err in errors:
            github_post(
                f"https://api.github.com/repos/{args.repo}/pulls/{args.pr}/comments",
                token,
                {
                    "body": f"⚠ Drift detected: **{err}**",
                    "commit_id": f["sha"],
                    "path": filename,
                    "position": 1
                }
            )

    # Summary comment
    summary = "### TriadicFrameworks Drift Guardian Report\n\n"

    for filename, errors, score in drift_results:
        summary += f"{drift_color(score)} **{filename}** — {drift_label(score)}\n"
        if errors:
            for e in errors:
                summary += f"- {e}\n"
        summary += "\n"

    github_post(
        f"https://api.github.com/repos/{args.repo}/issues/{args.pr}/comments",
        token,
        {"body": summary}
    )

    print("Drift Guardian completed.")

if __name__ == "__main__":
    main()
