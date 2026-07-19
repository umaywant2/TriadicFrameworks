"""
test_rsm_entities.py
Minimal entity tests for the Resonance Substrate Model (RSM).
Ensures ResonanceState, StabilityProfile, and EvaluationContext
behave predictably and independently of QSM/BSM.
"""

from resonance_substrate_model.rsm_core.rsm_entities import (
    ResonanceState,
    StabilityProfile,
    EvaluationContext,
)


# ---------------------------------------------------------------------------
# ResonanceState
# ---------------------------------------------------------------------------

def test_resonance_state_initialization():
    rs = ResonanceState(coherence_level=0.3, gain=0.1)
    assert rs.coherence_level == 0.3
    assert rs.gain == 0.1


def test_resonance_state_update():
    rs = ResonanceState(0.2, 0.0)
    rs.update(coherence_delta=0.1, gain_delta=0.05)
    assert rs.coherence_level == 0.3
    assert rs.gain == 0.05


# ---------------------------------------------------------------------------
# StabilityProfile
# ---------------------------------------------------------------------------

def test_stability_profile_history_and_counts():
    sp = StabilityProfile()
    sp.update("stable")
    sp.update("marginal")
    sp.update("stable")

    assert sp.most_recent() == "stable"
    counts = sp.counts()
    assert counts["stable"] == 2
    assert counts["marginal"] == 1
    assert counts["unstable"] == 0


# ---------------------------------------------------------------------------
# EvaluationContext
# ---------------------------------------------------------------------------

def test_evaluation_context_as_dict():
    ctx = EvaluationContext(triad_index=12, corridor_label="16D-24D", notes="ok")
    d = ctx.as_dict()

    assert d["triad_index"] == 12
    assert d["corridor_label"] == "16D-24D"
    assert d["notes"] == "ok"
