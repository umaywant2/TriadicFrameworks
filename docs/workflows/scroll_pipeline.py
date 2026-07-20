"""
Scroll Pipeline (Python)
TriadicFrameworks • Workflows Subsystem

Executes `.fff` scroll artifacts in Python environments.
Mirrors the JS pipeline API:

    run_scroll(scroll_text)

Returns:
    { "output": ..., "warnings": [...], "metadata": {...} }
"""

from tft.scrolls.parse import parse_scroll
from tft.scrolls.pipeline import execute_scroll


def run_scroll(scroll_text):
    """Parse and execute a scroll, returning a structured result."""
    parsed = parse_scroll(scroll_text)
    result = execute_scroll(parsed)

    return {
        "output": result.get("output"),
        "warnings": result.get("warnings", []),
        "metadata": result.get("metadata", {})
    }
