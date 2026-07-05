# RTTcode Generator (Python)
# Usage:
#   pip install qrcode[pil]
#   python generate_rttcode.py rttcode-payload.json output.png

import json
import os
import sys
import qrcode
from urllib.parse import urlencode

def validate_payload(payload):
    required = ["domain", "artifact_type", "version", "url"]
    for key in required:
        if key not in payload:
            raise ValueError(f"Missing required field: {key}")

    if not isinstance(payload["domain"], str):
        raise TypeError("domain must be a string")
    if not isinstance(payload["artifact_type"], str):
        raise TypeError("artifact_type must be a string")
    if not isinstance(payload["version"], str):
        raise TypeError("version must be a string")
    if not isinstance(payload["url"], str):
        raise TypeError("url must be a string")

    if "triad" in payload:
        triad = payload["triad"]
        for key in ["f_R", "tau_R", "Q_R"]:
            if key in triad and not isinstance(triad[key], str):
                raise TypeError(f"triad.{key} must be a string")

def build_rttcode_url(payload):
    base_url = "https://triadicframeworks.org/rttcode"
    domain = payload["domain"]
    version = payload["version"]

    f = "f?" if "triad" not in payload or "f_R" not in payload["triad"] else f"f{payload['triad']['f_R']}"
    t = "t?" if "triad" not in payload or "tau_R" not in payload["triad"] else f"t{payload['triad']['tau_R']}"
    q = "Q?" if "triad" not in payload or "Q_R" not in payload["triad"] else f"Q{payload['triad']['Q_R']}"

    token = f"{version}-{f}-{t}-{q}"
    query = urlencode({domain: token})
    return f"{base_url}?{query}"

def generate_qr_code(data, output_path):
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=2
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(output_path)

def _sanitize_filename(user_path):
    if not isinstance(user_path, str) or not user_path.strip():
        raise ValueError("Path must be a non-empty string")

    candidate = user_path.strip()
    if os.path.isabs(candidate):
        raise ValueError(f"Absolute paths are not allowed: {user_path}")

    normalized = os.path.normpath(candidate)
    filename = os.path.basename(normalized)

    if filename in ("", ".", ".."):
        raise ValueError(f"Invalid file name: {user_path}")
    if filename != normalized:
        raise ValueError(f"Directory components are not allowed: {user_path}")

    return filename

def resolve_safe_path(user_path, base_dir, allowed_exts=None, must_exist=False, file_kind=None):
    safe_name = _sanitize_filename(user_path)

    base_real = os.path.realpath(base_dir)
    target_real = os.path.realpath(os.path.join(base_real, safe_name))
    if os.path.commonpath([base_real, target_real]) != base_real:
        raise ValueError(f"Resolved path escapes base directory: {user_path}")

    if allowed_exts is not None:
        _, ext = os.path.splitext(target_real)
        if ext.lower() not in {e.lower() for e in allowed_exts}:
            raise ValueError(f"Disallowed file extension for path: {user_path}")

    # Use a post-validation canonical path for filesystem operations.
    safe_path = os.path.realpath(target_real)

    if must_exist:
        if not os.path.exists(safe_path):
            raise ValueError(f"Path does not exist: {user_path}")
        if file_kind == "file" and not os.path.isfile(safe_path):
            raise ValueError(f"Path is not a regular file: {user_path}")
        if file_kind == "dir" and not os.path.isdir(safe_path):
            raise ValueError(f"Path is not a directory: {user_path}")
    elif file_kind == "file" and os.path.exists(safe_path) and not os.path.isfile(safe_path):
        raise ValueError(f"Path is not a regular file: {user_path}")

    return safe_path

def main():
    if len(sys.argv) != 3:
        print("Usage: python generate_rttcode.py <payload.json> <output.png>")
        sys.exit(1)

    payload_path = sys.argv[1]
    output_path = sys.argv[2]
    base_dir = os.getcwd()

    safe_payload_path = resolve_safe_path(
        payload_path, base_dir, allowed_exts={".json"}, must_exist=True, file_kind="file"
    )
    safe_output_path = resolve_safe_path(
        output_path, base_dir, allowed_exts={".png"}, must_exist=False
    )

    with open(safe_payload_path, "r", encoding="utf-8") as f:
        payload = json.load(f)

    validate_payload(payload)
    rtt_url = build_rttcode_url(payload)
    print("RTTcode URL:", rtt_url)

    generate_qr_code(rtt_url, safe_output_path)
    print("QR code saved to:", safe_output_path)

if __name__ == "__main__":
    main()

