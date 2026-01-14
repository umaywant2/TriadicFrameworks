"""
rsm_operators.py
Core operators for the Resonance Substrate Model (RSM).

Minimal behaviors:
- REO  (Resonance Evaluation Operator)
- SCO  (Stability Classification Operator)
- RTO_RSM (Resonance-Time Outflow)

All operators are lightweight and independent of QSM/BSM.
"""


# ---------------------------------------------------------------------------
# REO — Resonance Evaluation Operator
# ---------------------------------------------------------------------------

def REO(coherence_source, resonance_state):
    """
    Resonance Evaluation Operator.

    Minimal behavior:
    - Read a coherence-like value from coherence_source
    - Update the ResonanceState with a small delta
    """
    coherence_value = _extract_coherence(coherence_source)
    # For now, treat coherence_value as the new level directly
    resonance_state.coherence_level = coherence_value
    return resonance_state


# ---------------------------------------------------------------------------
# SCO — Stability Classification Operator
# ---------------------------------------------------------------------------

def SCO(resonance_state, stable_threshold=0.7, marginal_threshold=0.4):
    """
    Stability Classification Operator.

    Returns one of: "stable", "marginal", "unstable".
    """
    value = float(getattr(resonance_state, "coherence_level", 0.0))
    if value >= stable_threshold:
        return "stable"
    if value >= marginal_threshold:
        return "marginal"
    return "unstable"


# ---------------------------------------------------------------------------
# RTO_RSM — Resonance-Time Outflow
# ---------------------------------------------------------------------------

def RTO_RSM(resonance_state, stability_label, triad_index=None):
    """
    Resonance-Time Outflow.

    Minimal behavior:
    - Produce a small, triad-aware summary dict suitable for logging or routing.
    """
    return {
        "triad_index": triad_index,
        "coherence_level": getattr(resonance_state, "coherence_level", None),
        "gain": getattr(resonance_state, "gain", None),
        "stability_label": stability_label,
        "source": "RSM",
    }


# ---------------------------------------------------------------------------
# Internal helper
# ---------------------------------------------------------------------------

def _extract_coherence(source) -> float:
    """
    Extract a coherence-like value from the source object.
    Tries common attribute names in order.
    """
    for attr in ("coherence_level", "coherence", "level"):
        if hasattr(source, attr):
            try:
                return float(getattr(source, attr))
            except (TypeError, ValueError):
                continue
    return 0.0

