# nist_indexer.py — Auto-index NIST domains

import os
import json

ROOT = "docs/nist/"

def index_domain(path):
    domain = os.path.basename(path)
    files = sorted(os.listdir(path))
    return {
        "domain": domain,
        "files": files,
        "has_data": "data" in files,
        "has_overview": "overview.md" in files
    }

if __name__ == "__main__":
    domains = [
        index_domain(os.path.join(ROOT, d))
        for d in os.listdir(ROOT)
        if os.path.isdir(os.path.join(ROOT, d))
    ]
    with open("nist_index.json", "w") as f:
        json.dump(domains, f, indent=2)
