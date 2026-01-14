"""
test_rsm_operators.py
Minimal operator tests for the Resonance Substrate Model (RSM).
Ensures REO, SCO, and RTO_RSM behave predictably.
"""

import pytest

from resonance_substrate_model.rsm_core.rsm_operators import (
    REO,
    SCO,
    RTO_RSM,
)


# ---------------------------------------------------------------------------
# FIXTURES
# ---------------------------------------------------------------------------

@pytest.fixture
def coherence_source():
    class MockSource:
        def __init__(self):
            self.level = 0.65  # mid-range coherence

    return MockSource()


@pytest.fixture
def resonance_state():
    class MockResonanceState:
        def __init__(self):
            self.coherence_level = 0.0
            self.gain = 0.0

    return MockResonanceState()


# ---------------------------------------------------------------------------
# TESTS
# ---------------------------------------------------------------------------

def test_reo_updates_resonance_state(coherence_source, resonance_state):
    """REO should copy coherence into the resonance state."""
    REO(coherence_source, resonance_state)
    assert resonance_state.coherence_level == pytest.approx(0.65)


def test_sco_classification():
    """SCO should classify based on thresholds."""
    class RS:
        def __init__(self, level):
            self.coherence_level = level

    assert SCO(RS(0.8)) == "stable"
    assert SCO(RS(0.5)) == "marginal"
    assert SCO(RS(0.2)) == "unstable"


def test_rto_rsm_packet_structure(resonance_state):
    """RTO_RSM should produce a minimal, triad-aware summary dict."""
    resonance_state.coherence_level = 0.55
    resonance_state.gain = 0.1

    packet = RTO_RSM(resonance_state, stability_label="marginal", triad_index=12)

    assert packet["triad_index"] == 12
    assert packet["coherence_level"] == pytest.approx(0.55)
    assert packet["gain"] == pytest.approx(0.1)
    assert packet["stability_label"] == "marginal"
    assert packet["source"] == "RSM"
