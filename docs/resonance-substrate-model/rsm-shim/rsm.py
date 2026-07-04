import json
import sys
import os
import re

def load_config(path):
    if not isinstance(path, str) or not path.strip():
        raise ValueError("Config path must be a non-empty string")
    if os.path.isabs(path):
        raise ValueError("Absolute config paths are not allowed")
    if path != os.path.basename(path):
        raise ValueError("Config path must be a filename without directories")
    if not re.fullmatch(r"[A-Za-z0-9._-]+\.json", path):
        raise ValueError("Config path must be a safe .json filename")

    base_dir = os.path.dirname(os.path.realpath(__file__))
    full_path = os.path.realpath(os.path.join(base_dir, path))
    if os.path.commonpath([base_dir, full_path]) != base_dir:
        raise ValueError("Config path is outside allowed directory")
    if not os.path.isfile(full_path):
        raise ValueError("Config path must point to an existing file")

    with open(full_path) as f:
        return json.load(f)

def build_substrate(cfg):
    return {
        "grid": cfg["grid"],
        "fields": cfg["fields"],
        "operators": cfg["operators"]
    }

if __name__ == "__main__":
    cfg = load_config(sys.argv[1])
    substrate = build_substrate(cfg)
    print("RSM substrate constructed:")
    print(json.dumps(substrate, indent=2))

