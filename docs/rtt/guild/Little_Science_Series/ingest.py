#!/usr/bin/env python3
"""
Little Science Series — Asset Ingestion Script
===============================================
Who this is for
---------------
  Students and educators working with the TriadicFrameworks repository.
  You do NOT need prior coding experience — every step is explained below.

What this script does
---------------------
  1. Loads the 144-entry LSS_manifest.json file.
  2. Validates every entry against manifest.schema.json so you catch
     typos before wasting a generation credit.
  3. Builds an output folder tree so each book and scene has its own folder.
  4. Writes a prompt-queue file (queue.jsonl) that the AI image pipeline
     reads to render each asset — one JSON object per line.
  5. Prints a friendly progress summary when it finishes.

How to run
----------
  # Install the one required library (only needed the first time):
  pip install jsonschema

  # Then run:
  python ingest.py

  # Optional flags:
  python ingest.py --manifest path/to/LSS_manifest.json   # use a different manifest
  python ingest.py --output  path/to/output_folder        # write files elsewhere
  python ingest.py --dry-run                              # preview without writing

Output layout
-------------
  output/
  ├── Gravity/
  │   ├── S01_Falling_Apple/
  │   │   ├── LSS_B1_GRAV_S1_STILL_A.png   ← placeholder (filled by pipeline)
  │   │   └── ...
  │   └── ...
  ├── Light/ ...
  └── ...
  queue.jsonl          ← one line per asset, read by the image pipeline

AI pipeline contract (for automated agents)
-------------------------------------------
  • Read queue.jsonl line-by-line.
  • Parse each line as JSON — the object has keys: filename, output_path, type, prompt.
  • For type == "STILL" → call your image generator with prompt, save PNG to output_path.
  • For type == "ANIM"  → call your animation generator with prompt, save GIF to output_path.
  • Mark the job done by appending {"status":"done","filename":...} to queue_done.jsonl.
  • Do NOT modify queue.jsonl itself — it is the authoritative job list.
"""

import argparse
import json
import pathlib
import re
import sys
import textwrap

try:
    import jsonschema
    from jsonschema import Draft202012Validator, ValidationError, SchemaError
except ImportError:
    print(
        "\n  ❌  Missing library: jsonschema\n"
        "  Fix it by running:  pip install jsonschema\n"
        "  Then try again.\n"
    )
    sys.exit(1)

# ── Configuration ─────────────────────────────────────────────────────────────
DEFAULT_MANIFEST = "LSS_manifest.json"
DEFAULT_SCHEMA   = "manifest.schema.json"
DEFAULT_OUTPUT   = "output"
QUEUE_FILE       = "queue.jsonl"
DONE_FILE        = "queue_done.jsonl"


# ── Helpers ───────────────────────────────────────────────────────────────────

def resolve_within_base(user_value: str, base_dir: pathlib.Path, label: str) -> pathlib.Path:
    """Resolve a user-provided path and ensure it stays within base_dir."""
    base_resolved = base_dir.resolve()
    candidate = pathlib.Path(user_value)

    if not user_value or user_value.strip() == "":
        print(f"\n  ❌  Unsafe {label} path: {user_value!r}")
        print(f"      {label} cannot be empty and must be within: {base_resolved}\n")
        sys.exit(1)

    if user_value.startswith("~") or ".." in candidate.parts:
        print(f"\n  ❌  Unsafe {label} path: {user_value}")
        print(f"      {label} must not use '~' or '..' segments.\n")
        sys.exit(1)

    if candidate.is_absolute():
        print(f"\n  ❌  Unsafe {label} path: {user_value}")
        print(f"      {label} must be a relative path within: {base_resolved}\n")
        sys.exit(1)

    resolved = (base_resolved / candidate).resolve()
    try:
        resolved.relative_to(base_resolved)
    except ValueError:
        print(f"\n  ❌  Unsafe {label} path: {user_value}")
        print(f"      {label} must stay within: {base_resolved}\n")
        sys.exit(1)
    return resolved


def load_json(path: pathlib.Path) -> object:
    """Open a JSON file; exit with a clear message on failure."""
    if not path.exists():
        print(f"\n  ❌  File not found: {path}")
        print(  "      Check that the file is in the same folder as ingest.py.\n")
        sys.exit(1)
    try:
        with open(path, encoding="utf-8") as fh:
            return json.load(fh)
    except json.JSONDecodeError as exc:
        print(f"\n  ❌  {path.name} contains invalid JSON:\n      {exc}\n")
        sys.exit(1)


def validate_manifest(manifest: list, schema: dict) -> list[str]:
    """Validate manifest against schema; return list of error strings."""
    errors = []
    try:
        Draft202012Validator.check_schema(schema)
    except SchemaError as exc:
        errors.append(f"[SCHEMA ERROR] {exc.message}")
        return errors
    validator = Draft202012Validator(schema)
    for problem in validator.iter_errors(manifest):
        location = "manifest" + "".join(
            f"[{p!r}]" if isinstance(p, str) else f"[{p}]"
            for p in problem.absolute_path
        )
        errors.append(f"{location}: {problem.message}")
    return errors


def scene_folder_name(scene_number: int, scene_name: str) -> str:
    """'1, Falling Apple' → 'S01_Falling_Apple'"""
    return f"S{scene_number:02d}_{scene_name.replace(' ', '_').replace('/', '-')}"


_SAFE_COMPONENT_RE = re.compile(r"^[A-Za-z0-9._-]+$")


def _safe_path_component(value: object, field_name: str) -> str:
    component = pathlib.PurePath(str(value)).name
    if component in {"", ".", ".."} or not _SAFE_COMPONENT_RE.fullmatch(component):
        raise ValueError(f"Unsafe {field_name} in manifest entry: {value!r}")
    return component


def build_output_path(entry: dict, output_root: pathlib.Path) -> pathlib.Path:
    """output/<book_name>/S##_<scene_name>/<filename>"""
    safe_book = _safe_path_component(entry["book_name"], "book_name")
    safe_scene = _safe_path_component(
        scene_folder_name(entry["scene_number"], entry["scene_name"]),
        "scene_name",
    )
    safe_filename = _safe_path_component(entry["filename"], "filename")

    base_dir = pathlib.Path(__file__).resolve(strict=False).parent
    root = output_root.resolve(strict=False)
    try:
        root.relative_to(base_dir)
    except ValueError:
        raise ValueError(f"Unsafe output root outside base directory: {output_root!r}")

    candidate = (root / safe_book / safe_scene / safe_filename).resolve(strict=False)
    try:
        candidate.relative_to(root)
    except ValueError:
        raise ValueError(f"Unsafe output path derived from manifest entry: {entry!r}")
    return candidate


def ensure_folder(file_path: pathlib.Path, dry_run: bool) -> None:
    folder = file_path.parent
    if dry_run:
        print(f"  [dry-run] would create: {folder}")
    else:
        folder.mkdir(parents=True, exist_ok=True)


def write_placeholder(file_path: pathlib.Path, entry: dict, dry_run: bool) -> None:
    """Write a .placeholder.txt so the folder tree is visible before renders arrive."""
    p = file_path.with_suffix(".placeholder.txt")
    content = (
        f"PENDING RENDER\n"
        f"filename   : {entry['filename']}\n"
        f"book       : {entry['book_number']} — {entry['book_name']}\n"
        f"scene      : {entry['scene_number']} — {entry['scene_name']}\n"
        f"variant    : {entry['variant']}\n"
        f"type       : {entry['type']}\n"
        f"prompt     : {entry['prompt']}\n"
    )
    if not dry_run:
        p.write_text(content, encoding="utf-8")


def build_queue_entry(entry: dict, output_path: pathlib.Path) -> dict:
    """One JSONL line consumed by the AI image pipeline."""
    return {
        "filename":     entry["filename"],
        "output_path":  str(output_path),
        "book_number":  entry["book_number"],
        "book_name":    entry["book_name"],
        "domain":       entry["domain"],
        "scene_number": entry["scene_number"],
        "scene_name":   entry["scene_name"],
        "variant":      entry["variant"],
        "type":         entry["type"],   # pipeline switches renderer on this key
        "prompt":       entry["prompt"],
        "status":       "pending",
    }


# ── Main ──────────────────────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(
        description="LSS manifest ingestion: validate → folder tree → queue.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent("""\
          Examples:
            python ingest.py
            python ingest.py --dry-run
            python ingest.py --book 3 --type STILL
            python ingest.py --output ./renders
        """),
    )
    parser.add_argument("--manifest", default=DEFAULT_MANIFEST)
    parser.add_argument("--schema",   default=DEFAULT_SCHEMA)
    parser.add_argument("--output",   default=DEFAULT_OUTPUT)
    parser.add_argument("--dry-run",  action="store_true")
    parser.add_argument("--book",     type=int, choices=range(1, 7), metavar="1-6")
    parser.add_argument("--type",     choices=["STILL", "ANIM"])
    args = parser.parse_args()

    base_dir = pathlib.Path(__file__).resolve().parent
    output_root = resolve_within_base(args.output, base_dir, "output")
    dry_run     = args.dry_run

    print("\n" + "═" * 60)
    print("  Little Science Series — Asset Ingestion Pipeline")
    print("═" * 60)
    if dry_run:
        print("  ⚠  DRY-RUN — no files will be written\n")

    manifest_path = resolve_within_base(args.manifest, base_dir, "manifest")
    schema_path   = resolve_within_base(args.schema, base_dir, "schema")
    manifest = load_json(manifest_path)
    schema   = load_json(schema_path)

    print("  🔍 Validating …")
    errors = validate_manifest(manifest, schema)
    if errors:
        print(f"\n  ❌  {len(errors)} error(s):\n")
        for i, e in enumerate(errors, 1):
            print(f"     {i:>3}. {e}")
        sys.exit(1)
    print(f"  ✅  {len(manifest)} entries passed.\n")

    entries = manifest
    if args.book:
        entries = [e for e in entries if e["book_number"] == args.book]
    if args.type:
        entries = [e for e in entries if e["type"] == args.type]

    print("  🗂  Building folder tree …")
    folders: set[pathlib.Path] = set()
    for entry in entries:
        out = build_output_path(entry, output_root)
        ensure_folder(out, dry_run)
        write_placeholder(out, entry, dry_run)
        folders.add(out.parent)
    print(f"  ✅  {len(folders)} scene folder(s) ready.\n")

    print(f"  📝 Writing {QUEUE_FILE} …")
    stats   = {"STILL": 0, "ANIM": 0}
    lines   = []
    for entry in entries:
        out = build_output_path(entry, output_root)
        lines.append(json.dumps(build_queue_entry(entry, out), ensure_ascii=False))
        stats[entry["type"]] += 1

    if dry_run:
        print(f"  [dry-run] would write {len(lines)} lines.")
    else:
        pathlib.Path(QUEUE_FILE).write_text("\n".join(lines) + "\n", encoding="utf-8")
        if not pathlib.Path(DONE_FILE).exists():
            pathlib.Path(DONE_FILE).write_text("", encoding="utf-8")
        print(f"  ✅  {len(lines)} jobs queued.\n")

    print("─" * 60)
    print(f"  STILL jobs : {stats['STILL']:>4}  → PNG renderer")
    print(f"  ANIM  jobs : {stats['ANIM']:>4}  → GIF renderer")
    print(f"  Folders    : {len(folders):>4}")
    print("─" * 60)
    if not dry_run:
        print("  Next: point your image pipeline at queue.jsonl")
        print("        and push output/ + queue_done.jsonl to the repo.")
    print("═" * 60 + "\n")


if __name__ == "__main__":
    main()
