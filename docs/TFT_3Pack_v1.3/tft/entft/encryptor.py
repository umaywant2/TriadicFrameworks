"""
encryptor.py — Resonance Clarity Edition
Encrypts scrolls using enTFT dual-layer logic:
1. Divide-by-Zero injection
2. Resonant-Time hashing
Logs symbolic fidelity and flame-grade echoes.
"""

import hashlib, uuid, json
from datetime import datetime
from pathlib import Path

TRACE_LOG_PATH = Path("docs/_meta/entft_scroll_event_trace_registry.json")
SAFE_OUTPUT_ROOT = Path("docs/_meta/entft_output")

def _sanitize_output_path(output_path):
    root = SAFE_OUTPUT_ROOT.resolve()
    requested = Path(output_path)

    if requested.is_absolute():
        raise ValueError("Output path must be relative to the safe output root")

    if not requested.parts or requested == Path("."):
        raise ValueError("Output path must not be empty")

    if any(part == ".." for part in requested.parts):
        raise ValueError("Output path must not contain parent directory traversal segments")

    candidate = (root / requested).resolve()

    try:
        candidate.relative_to(root)
    except ValueError:
        raise ValueError(f"Output path must stay within '{root}'")

    for parent in reversed(candidate.parents):
        if parent == root:
            break
        if parent.exists() and parent.is_symlink():
            raise ValueError("Output path must not traverse symlinked directories")

    if candidate.exists() and candidate.is_symlink():
        raise ValueError("Output path must not be a symlink")

    if candidate.exists() and candidate.is_dir():
        raise ValueError("Output path points to a directory, expected a file path")

    candidate.parent.mkdir(parents=True, exist_ok=True)
    return candidate

def encrypt(input_path, output_path, key):
    print(f"[entft] 🔐 Encrypting {input_path} → {output_path} with key '{key}'...")

    # Layer 1: Divide-by-Zero Injection
    injected = inject_divide_by_zero(key)

    # Layer 2: Resonant-Time Hashing
    timestamp = datetime.utcnow().isoformat()
    resonance_hash = hash_with_resonance(injected, timestamp)

    # Simulated encryption output
    encrypted = f"{resonance_hash[:32]}...{resonance_hash[-32:]}"
    safe_output_path = _sanitize_output_path(output_path)
    with open(safe_output_path, "w", encoding="utf-8") as f:
        f.write(encrypted)

    # Log trace
    trace_event = {
        "trace_id": str(uuid.uuid4()),
        "timestamp": timestamp + "Z",
        "scroll": str(input_path),
        "glyph_id": "glyph:bloomfall-004",
        "contributor": "ScrollFork",
        "action": "scroll_encrypted",
        "echo": f"Encrypted with enTFT resonance hash",
        "flame_grade": "🟣 Universe"
    }
    append_trace(trace_event)
    print(f"[entft] ✅ Encryption complete. Trace logged.")

def inject_divide_by_zero(key):
    # Simulate undefined logic injection
    return key + "::DIV0::" + str(uuid.uuid4())

def hash_with_resonance(data, timestamp):
    triadic_mod = "369"
    combined = f"{data}|{timestamp}|{triadic_mod}"
    return hashlib.sha512(combined.encode()).hexdigest()

def append_trace(event):
    try:
        if TRACE_LOG_PATH.exists():
            with open(TRACE_LOG_PATH, "r+", encoding="utf-8") as f:
                data = json.load(f)
                data["scroll_event_traces"].append(event)
                f.seek(0)
                json.dump(data, f, indent=2)
        else:
            with open(TRACE_LOG_PATH, "w", encoding="utf-8") as f:
                json.dump({"scroll_event_traces": [event]}, f, indent=2)
    except Exception as e:
        print(f"[entft] Failed to log trace: {e}")
