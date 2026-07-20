"""
rsm_entities.py
Core entity definitions for the Resonance Substrate Model (RSM).

Minimal, independently functional entities:
- ResonanceState
- StabilityProfile
- EvaluationContext

These are designed to work with rsm_eval_engine.py and remain
independent of QSM/BSM.
"""


# ---------------------------------------------------------------------------
# ResonanceState
# ---------------------------------------------------------------------------

class ResonanceState:
    """
    ResonanceState
    Represents a minimal resonance descriptor.

    Attributes
    ----------
    coherence_level : float
        Aggregate coherence value.
    gain : float
        Optional resonance gain metric.
    """

    def __init__(self, coherence_level: float = 0.0, gain: float = 0.0):
        self.coherence_level = float(coherence_level)
        self.gain = float(gain)

    def update(self, coherence_delta: float, gain_delta: float = 0.0):
        """
        Apply a small update to coherence and gain.
        """
        self.coherence_level += coherence_delta
        self.gain += gain_delta
        return self


# ---------------------------------------------------------------------------
# StabilityProfile
# ---------------------------------------------------------------------------

class StabilityProfile:
    """
    StabilityProfile
    Tracks stability labels over time and exposes a simple summary.

    Attributes
    ----------
    history : list[str]
        Sequence of stability labels: "stable", "marginal", "unstable".
    """

    def __init__(self):
        self.history: list[str] = []

    def update(self, label: str):
        """
        Record a new stability label.
        """
        self.history.append(label)

    def most_recent(self) -> str | None:
        """
        Return the most recent stability label, if any.
        """
        return self.history[-1] if self.history else None

    def counts(self) -> dict:
        """
        Return a simple count of each label.
        """
        result = {"stable": 0, "marginal": 0, "unstable": 0}
        for label in self.history:
            if label in result:
                result[label] += 1
        return result


# ---------------------------------------------------------------------------
# EvaluationContext
# ---------------------------------------------------------------------------

class EvaluationContext:
    """
    EvaluationContext
    Triad-aware metadata for an RSM evaluation run.

    Attributes
    ----------
    triad_index : int | None
    corridor_label : str | None
    notes : str
    """

    def __init__(self, triad_index=None, corridor_label=None, notes: str = ""):
        self.triad_index = triad_index
        self.corridor_label = corridor_label
        self.notes = notes

    def as_dict(self) -> dict:
        return {
            "triad_index": self.triad_index,
            "corridor_label": self.corridor_label,
            "notes": self.notes,
        }

