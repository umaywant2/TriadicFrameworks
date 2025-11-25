"""
entft_validator.py — Resonance Clarity Edition
Validates encrypted outputs and badge triggers for enTFT protocol.
"""

import json
import re
from pathlib import Path

def validate_fff(file_path):
    """
    Validates a .fff file for structural integrity and metadata fidelity.
    """
    path = Path(file_path)
    if not path.exists():
        return False, "File not found."

    with open(path) as f:
        lines = f.readlines()

    if not lines[0].strip().startswith("FFFv1.3"):
        return False, "Missing or incorrect header."

    meta_lines = [line for line in lines if line.startswith("META::")]
    if not meta_lines:
        return False, "Missing metadata block."

    try:
        metadata = json.loads(meta_lines[-1].replace("META::", ""))
        if "observer" not in metadata or "lens" not in metadata:
            return False, "Incomplete metadata."
    except json.JSONDecodeError:
        return False, "Malformed metadata JSON."

    return True, "✅ .fff file is valid."

def validate_badge_trigger(log_path):
    """
    Validates badge trigger logs for symbolic echo and validator match.
    """
    path = Path(log_path)
    if not path.exists():
        return False, "Log file not found."

    with open(path) as f:
        content = f.read()

    if "Badge Triggered" not in content:
        return False, "No badge trigger detected."

    if not re.search(r"Validator:\s*BadgeLogic", content):
        return False, "Validator mismatch."

    return True, "✅ Badge trigger validated."

if __name__ == "__main__":
    fff_result = validate_fff("output.enc.fff")
    print("FFF Validation:", fff_result)

    badge_result = validate_badge_trigger("badge_echo.log")
    print("Badge Trigger Validation:", badge_result)
