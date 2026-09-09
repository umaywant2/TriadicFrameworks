import os
import json
import argparse
import requests
import subprocess

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
# VALIDATION + FIXING
# ---------------------------------------------------------
def fix_module_json(path):
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    module = data.get("module", {})
    fixes = []

    # canon_ref
    if module.get("canon_ref") != EXPECTED_CANON_REF:
        module["canon_ref"] = EXPECTED_CANON_REF
        fixes.append("canon_ref corrected")

    # inherit
    inherit = module.setdefault("inherit", {})
    for key, expected in EXPECTED_INHERIT.items():
        if inherit.get(key) != expected:
            inherit[key] = expected
            fixes.append(f"inherit.{key} corrected")

    # rtt
    rtt = module.setdefault("rtt", {})
    for key, expected in EXPECTED_RTT.items():
        if rtt.get(key) != expected:
            rtt[key] = expected
            fixes.append(f"rtt.{key} corrected")

    # ai.initialization
    ai = module.setdefault("ai", {}).setdefault("initialization", {})
    for key, expected in EXPECTED_AI_INIT.items():
        if ai.get(key) != expected:
            ai[key] = expected
            fixes.append(f"ai.initialization.{key} corrected")

    # Write back if fixes occurred
    if fixes:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
    return fixes

# ---------------------------------------------------------
# GITHUB API HELPERS
# ---------------------------------------------------------
def github_post(url, token, payload):
    return requests.post(url, headers={"Authorization": f"token {token}"}, json=payload)

# ---------------------------------------------------------
# MAIN BOT LOGIC
# ---------------------------------------------------------
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo")
    parser.add_argument("--pr")
    parser.add_argument("--branch")
    args = parser.parse_args()

    token = os.environ["GITHUB_TOKEN"]

    # Get changed files in PR
    pr_files_url = f"https://api.github.com/repos/{args.repo}/pulls/{args.pr}/files"
    files = requests.get(pr_files_url, headers={"Authorization": f"token {token}"}).json()

    fixes_summary = []

    for f in files:
        filename = f["filename"]

        if not filename.endswith("module.json"):
            continue

        local_path = filename

        if not os.path.exists(local_path):
            continue

        fixes = fix_module_json(local_path)

        if fixes:
            fixes_summary.append((filename, fixes))

    # Commit fixes if any
    if fixes_summary:
        subprocess.run(["git", "config", "user.name", "TriadicFrameworks-AutoFix"])
        subprocess.run(["git", "config", "user.email", "autofix@triadicframeworks.org"])

        subprocess.run(["git", "add", "."])
        subprocess.run(["git", "commit", "-m", "Auto-fix: Canon purity corrections"])
        subprocess.run(["git", "push", "origin", args.branch])

        # Post PR comment
        summary = "### Canon Auto-Fix Applied\n\n"
        for filename, fixes in fixes_summary:
            summary += f"**{filename}**\n"
            for fix in fixes:
                summary += f"- {fix}\n"
            summary += "\n"

        github_post(
            f"https://api.github.com/repos/{args.repo}/issues/{args.pr}/comments",
            token,
            {"body": summary}
        )

    print("Canon Auto-Fix completed.")

if __name__ == "__main__":
    main()
