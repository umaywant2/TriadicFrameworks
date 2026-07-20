"""
🧪 Minimal Test Harness
"""
from scroll_pipeline import run_scroll

def test_basic_pipeline():
    scroll = """
    emitter: test
    frequency: 144
    """

    out = run_scroll(scroll)
    assert "output" in out
    assert "warnings" in out
