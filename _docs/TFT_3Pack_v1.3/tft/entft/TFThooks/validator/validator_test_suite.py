"""
validator_test_suite.py — Resonance Clarity Edition
Simulates hook validation scenarios across TFThooks.
"""

from hook_validator import validate_hook_file
import os

def run_edge_case_tests():
    print("🧪 Running edge case simulations...\n")

    # Case 1: Missing hook_entry
    with open("TFThooks/test_missing_entry.py", "w") as f:
        f.write("# No hook_entry here\ntrigger_symbol = 'badge_alpha'\nruntime.extend('alpha')\n")
    result = validate_hook_file("TFThooks/test_missing_entry.py")
    print("❌ Missing hook_entry:", result)

    # Case 2: Malformed badge trigger
    with open("TFThooks/test_bad_trigger.py", "w") as f:
        f.write("def hook_entry(): pass\ntrigger_symbol = badge_alpha\nruntime.extend('alpha')\n")
    result = validate_hook_file("TFThooks/test_bad_trigger.py")
    print("❌ Malformed badge trigger:", result)

    # Case 3: Missing runtime extension
    with open("TFThooks/test_no_runtime.py", "w") as f:
        f.write("def hook_entry(): pass\ntrigger_symbol = 'badge_alpha'\n")
    result = validate_hook_file("TFThooks/test_no_runtime.py")
    print("❌ Missing runtime extension:", result)

    # Case 4: Valid hook
    with open("TFThooks/test_valid_hook.py", "w") as f:
        f.write("def hook_entry(): pass\ntrigger_symbol = 'badge_alpha'\nruntime.extend('alpha')\n")
    result = validate_hook_file("TFThooks/test_valid_hook.py")
    print("✅ Valid hook:", result)

    # Cleanup
    for file in os.listdir("TFThooks"):
        if file.startswith("test_"):
            os.remove(os.path.join("TFThooks", file))

if __name__ == "__main__":
    run_edge_case_tests()
