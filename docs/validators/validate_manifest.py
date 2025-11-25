# 🧪 Manifest Validator
# Confirms symbolic structure and onboarding logic in curriculum modules

import json

def validate_manifest(manifest_path):
    with open(manifest_path, 'r') as f:
        content = f.read()

    checks = {
        "has_intro": "## Introduction" in content,
        "has_resonance": "## Resonance Logic" in content,
        "has_remix_guide": "## Remix Guide" in content,
        "has_badge_trigger": "badge_trigger:" in content
    }

    score = sum(checks.values())
    result = {
        "file": manifest_path,
        "score": score,
        "checks": checks,
        "badge_eligible": score >= 3
    }

    print(json.dumps(result, indent=2))
    return result
