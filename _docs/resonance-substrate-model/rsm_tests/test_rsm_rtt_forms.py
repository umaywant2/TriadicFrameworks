"""
test_rsm_rtt_forms.py
Minimal RTT form tests for the Resonance Substrate Model (RSM).
Ensures each form can be instantiated and converted to dict form.
"""

from resonance_substrate_model.rsm_core.rsm_rtt_forms import (
    RFF_RSM,
    RSET_RSM,
    RNR_RSM,
    RER_RSM,
)


def test_rff_rsm_as_dict():
    form = RFF_RSM(coherence_level=0.6, gain=0.1, triad_index=12)
    d = form.as_dict()
    assert d["coherence_level"] == 0.6
    assert d["gain"] == 0.1
    assert d["triad_index"] == 12


def test_rset_rsm_as_dict():
    form = RSET_RSM(payload={"x": 1}, triad_index=7)
    d = form.as_dict()
    assert d["payload"] == {"x": 1}
    assert d["triad_index"] == 7


def test_rnr_rsm_as_dict():
    form = RNR_RSM(delta_coherence=0.05, delta_gain=0.02, triad_index=3)
    d = form.as_dict()
    assert d["delta_coherence"] == 0.05
    assert d["delta_gain"] == 0.02
    assert d["triad_index"] == 3


def test_rer_rsm_as_dict():
    form = RER_RSM(
        average_coherence=0.55,
        stability_label="marginal",
        triad_index=12,
        notes="ok",
    )
    d = form.as_dict()
    assert d["average_coherence"] == 0.55
    assert d["stability_label"] == "marginal"
    assert d["triad_index"] == 12
    assert d["notes"] == "ok"
