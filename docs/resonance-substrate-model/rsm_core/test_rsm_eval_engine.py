"""
test_rsm_eval_engine.py
Minimal tests for the Resonance Substrate Model (RSM) evaluation engine.
Ensures resonance-time evaluation and stability classification behave predictably.
"""

import pytest
from resonance_substrate_model.rsm_core.rsm_eval_engine import (
    RSMEvalEngine,
    RSMEvalConfig,
)


# ---------------------------------------------------------------------------
# FIXTURES
# ---------------------------------------------------------------------------

@pytest.fixture
def coherence_source():
    class MockSource:
        def __init__(self):
            self.level = 0.55  # mid-range coherence

    return MockSource()


@pytest.fixture
def engine():
    cfg = RSMEvalConfig(
        steps=4,
        stability_threshold_stable=0.7,
        stability_threshold_marginal=0.4,
        triad_index=12,
    )
    return RSMEvalEngine(cfg)


# ---------------------------------------------------------------------------
# TESTS
# ---------------------------------------------------------------------------

def test_single_tick_updates_samples(engine, coherence_source):
    """A single tick should record a coherence sample and return a label."""
    value, label = engine.run_tick(coherence_source)

    assert value == pytest.approx(0.55)
    assert label == "marginal"  # 0.55 is between 0.4 and 0.7
    assert engine.ticks == 1


def test_multi_tick_summary(engine, coherence_source):
    """Running multiple ticks should produce a valid resonance summary."""
    summary = engine.run(coherence_source, steps=4)

    assert summary.ticks == 4
    assert summary.triad_index == 12
    assert summary.average_coherence == pytest.approx(0.55)
    assert summary.stability_label == "marginal"


def test_classification_thresholds(engine, coherence_source):
    """Classification should change when coherence crosses thresholds."""
    # Tick 1: marginal
    engine.run_tick(coherence_source)
    assert engine._classify(0.55) == "marginal"

    # Above stable threshold
    assert engine._classify(0.8) == "stable"

    # Below marginal threshold
    assert engine._classify(0.2) == "unstable"


# This test suite is intentionally tiny, deterministic, and mirrors the QSM/BSM style:
# - simple fixtures
# - predictable thresholds
# - clean classification checks
# - no external dependencies
