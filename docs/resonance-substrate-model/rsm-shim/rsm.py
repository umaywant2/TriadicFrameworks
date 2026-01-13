import json
import sys

def load_config(path):
    return json.load(open(path))

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

