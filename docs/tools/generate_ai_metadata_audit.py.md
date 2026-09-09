Here’s your **AI‑metadata auditor**, aligned with your existing tooling and safe to paste directly into your active `docs/tools` tab.

Save as:

```text
docs/tools/generate_ai_metadata_audit.py
```

Run from repo root:

```bash
python3 docs/tools/generate_ai_metadata_audit.py
```

It will create:

```text
docs/spine/ai_metadata_audit.json
```

—a canon‑wide JSON report of AI‑related metadata per module.

---

```python
import os
import json

ROOT = "docs"
EXCLUDED = {"spine","_template","assets","images","tools"}
SPINE = os.path.join(ROOT, "spine")
OUT_PATH = os.path.join(SPINE, "ai_metadata_audit.json")

EXPECTED_AI_INIT = {
    "load_spine_first": True,
    "load_canon_first": True,
    "apply_session_context": True,
    "triad_validation": True
}

EXPECTED_AI_META_KEYS = [
    "purpose",
    "audience",
    "keywords",
    "version",
    "mode",
]

def find_modules():
    out = []
    for root, dirs, files in os.walk(ROOT):
        if any(ex in root for ex in EXCLUDED):
            continue
        if "module.json" in files:
            out.append(os.path.join(root, "module.json"))
    return out

def safe_load(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return {}

def audit_ai_block(module):
    ai = module.get("ai")
    result = {
        "has_ai_block": isinstance(ai, dict),
        "has_initialization": False,
        "initialization_mismatches": [],
        "has_metadata": False,
        "metadata_missing_keys": [],
        "metadata_extra_keys": [],
    }

    if not isinstance(ai, dict):
        return result

    # initialization audit
    init = ai.get("initialization")
    if isinstance(init, dict):
        result["has_initialization"] = True
        for k, v in EXPECTED_AI_INIT.items():
            if init.get(k) != v:
                result["initialization_mismatches"].append(f"initialization.{k} != {v}")
    else:
        result["initialization_mismatches"].append("initialization block missing")

    # metadata audit (ai.metadata or ai.meta)
    meta = ai.get("metadata") or ai.get("meta")
    if isinstance(meta, dict):
        result["has_metadata"] = True
        present_keys = set(meta.keys())
        expected_keys = set(EXPECTED_AI_META_KEYS)
        missing = sorted(expected_keys - present_keys)
        extra = sorted(present_keys - expected_keys)
        result["metadata_missing_keys"] = missing
        result["metadata_extra_keys"] = extra
    else:
        result["metadata_missing_keys"] = EXPECTED_AI_META_KEYS

    return result

def main():
    print("\n=== TriadicFrameworks AI‑Metadata Auditor ===\n")

    modules = find_modules()
    os.makedirs(SPINE, exist_ok=True)

    audit = {}
    summary = {
        "total_modules": len(modules),
        "with_ai_block": 0,
        "with_initialization": 0,
        "with_metadata": 0,
    }

    for path in modules:
        name = os.path.basename(os.path.dirname(path))
        data = safe_load(path)
        module = data.get("module", {})

        ai_result = audit_ai_block(module)
        audit[name] = ai_result

        if ai_result["has_ai_block"]:
            summary["with_ai_block"] += 1
        if ai_result["has_initialization"]:
            summary["with_initialization"] += 1
        if ai_result["has_metadata"]:
            summary["with_metadata"] += 1

        print(f"✔ audited {name}")

    out = {
        "summary": summary,
        "modules": audit,
    }

    with open(OUT_PATH, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2)

    print(f"\n✔ Created {OUT_PATH}")
    print(
        f"\nSummary: modules={summary['total_modules']}, "
        f"with_ai_block={summary['with_ai_block']}, "
        f"with_initialization={summary['with_initialization']}, "
        f"with_metadata={summary['with_metadata']}"
    )
    print("\n✨ AI‑metadata audit captured.\n")

if __name__ == "__main__":
    main()
```
