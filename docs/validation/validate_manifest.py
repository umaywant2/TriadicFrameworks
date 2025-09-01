import yaml
import os
from datetime import datetime

MANIFEST_PATH = ".github/repo_manifest.yaml"
LOG_PATH = "validation/manifest_log.md"

def load_manifest(path):
    with open(path, "r") as f:
        return yaml.safe_load(f)

def validate_structure(manifest):
    missing = []
    for item in manifest.get("repo_structure", []):
        if isinstance(item, dict):
            for folder, subfolders in item.items():
                if not os.path.isdir(folder):
                    missing.append(folder)
                else:
                    for sub in subfolders:
                        if not os.path.isdir(os.path.join(folder, sub)):
                            missing.append(f"{folder}/{sub}")
        else:
            if not os.path.exists(item):
                missing.append(item)
    return missing

def log_results(missing):
    timestamp = datetime.utcnow().isoformat()
    with open(LOG_PATH, "a") as log:
        log.write(f"## Manifest Validation — {timestamp}\n")
        if missing:
            log.write("❌ Missing Items:\n")
            for m in missing:
                log.write(f"- {m}\n")
        else:
            log.write("✅ All items present. Structure aligned.\n")
        log.write("\n")

if __name__ == "__main__":
    manifest = load_manifest(MANIFEST_PATH)
    missing_items = validate_structure(manifest)
    log_results(missing_items)
