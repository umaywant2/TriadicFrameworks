"""
Remix Generation Engine
TriadicFrameworks • Workflows Subsystem

Produces remix variants of `.fff` scroll artifacts using scroll‑centric
remix rules. This engine is substrate‑agnostic and preserves canonical
anchors (τᵣ, dimensional constants, emitter identity) while generating
lineage‑safe remix metadata.

API:
    remix_scroll(scroll_obj, *, rules=None)
"""

from pathlib import Path
import uuid
import yaml

from tft.scrolls.parse import parse_scroll
from tft.scrolls.remix import apply_remix_rules
from tft.scrolls.export import export_scroll


def remix_scroll(scroll_obj, *, rules=None):
    """Return a new remix variant of a scroll object."""
    base = parse_scroll(scroll_obj)
    remixed = apply_remix_rules(base, rules=rules)

    remixed["metadata"]["remix_id"] = str(uuid.uuid4())
    remixed["metadata"]["lineage"] = base["metadata"].get("id")

    return remixed


def remix_to_file(scroll_obj, outfile, *, rules=None):
    """Generate a remix and write it to a `.fff` file."""
    remixed = remix_scroll(scroll_obj, rules=rules)
    text = export_scroll(remixed)

    Path(outfile).write_text(text, encoding="utf-8")
    return outfile
