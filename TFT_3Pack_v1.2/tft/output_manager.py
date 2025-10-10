"""
output_manager.py
Resonance-Labs / Tops Unified Output Ritual

Handles screen, file, and glyph outputs.
Supports TXT, JSON, Parquet, and .fff (Triadic Framework File).
"""

import json
import pandas as pd
from pathlib import Path

# -----------------------------
# File Output Functions
# -----------------------------

def save_output(data, filename, formats=["txt", "json", "parquet", "fff"], metadata=None):
    """
    Save simulation results in multiple formats.
    data: list of lists (numeric or ternary values)
    filename: base name (no extension)
    formats: list of formats to export
    metadata: optional dict of metadata (mode, observer, timestamp, etc.)
    """

    Path(filename).parent.mkdir(parents=True, exist_ok=True)

    if "txt" in formats:
        with open(f"{filename}.txt", "w") as f:
            for row in data:
                f.write(",".join(map(str, row)) + "\n")

    if "json" in formats:
        payload = {"metadata": metadata or {}, "data": data}
        with open(f"{filename}.json", "w") as f:
            json.dump(payload, f, indent=2)

    if "parquet" in formats:
        df = pd.DataFrame(data)
        df.to_parquet(f"{filename}.parquet", index=False)

    if "fff" in formats:
        with open(f"{filename}.fff", "w") as f:
            f.write("# Resonance-Labs .fff (Triadic Framework File)\n")
            if metadata:
                for k, v in metadata.items():
                    f.write(f"# {k}: {v}\n")
            f.write("\n")
            for row in data:
                ternary_row = "".join(
                    ["+" if v > 0 else "0" if v == 0 else "-" for v in row]
                )
                f.write(ternary_row + "\n")

# -----------------------------
# Loader for .fff
# -----------------------------

def load_fff(filename):
    """
    Load a .fff file and return ternary-decoded data.
    """
    decoded = []
    with open(filename, "r") as f:
        for line in f:
            if line.startswith("#") or not line.strip():
                continue
            decoded.append([1 if c == "+" else 0 if c == "0" else -1 for c in line.strip()])
    return decoded
