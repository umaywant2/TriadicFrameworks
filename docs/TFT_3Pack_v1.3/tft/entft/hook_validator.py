"""
hook_validator.py — Resonance Clarity Edition
Validates TFThook extensions for symbolic fidelity and runtime compatibility.
"""

import os
import re
from pathlib import Path

def validate_hook_file(file_path):
    """
    Validates a TFThook file for required structure and symbolic triggers.
    """
    path = Path(file_path)
    if not path.exists():
        return False, "Hook file not found."

    with open(path) as f:
        content = f.read()

    if "def hook_entry(" not in content:
        return False, "Missing hook_entry function."

    if not re.search(r"trigger_symbol\s*=\s*['\"]badge_[a-zA-Z0-9]+['\"]", content):
        return False, "Missing or malformed badge trigger."

    if "runtime.extend(" not in content:
        return False, "Missing runtime extension call."

    return True, "✅ Hook file is valid."

def validate_all_hooks(folder="TFThooks"):
    """
    Validates all .py files in the TFThooks folder.
    """
    results = {}
    for file in os.listdir(folder):
        if file.endswith(".py"):
            full_path = os.path.join(folder, file)
            valid, message = validate_hook_file(full_path)
            results[file] = message
    return results

if __name__ == "__main__":
    results = validate_all_hooks()
    for file, message in results.items():
        print(f"{file}: {message}")
