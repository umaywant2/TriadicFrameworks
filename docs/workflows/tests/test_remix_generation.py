"""
🧪 Minimal Test Harness
"""

from remix_generation import remix_scroll

def test_basic_remix():
    scroll = """
    emitter: test
    frequency: 144
    """

    out = remix_scroll(scroll)
    assert "metadata" in out
    assert "remix_id" in out["metadata"]
