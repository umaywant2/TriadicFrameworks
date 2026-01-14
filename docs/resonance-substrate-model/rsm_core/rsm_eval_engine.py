# Here we go, a **submission‑grade, minimal‑viable, triad‑aligned**  
# `rsm_eval_engine.py` that matches the pattern of the QSM/BSM engines and the `rsm_submission.md` you just locked in.


"""
rsm_eval_engine.py
Minimal evaluation engine for the Resonance Substrate Model (RSM).

This engine is intentionally lightweight:
- No QSM or BSM dependencies
- Accepts any resonance-like and coherence-like objects
- Produces stability classifications and resonance-time summaries
- Maintains a tick counter and triad-aware evaluation context
"""

from dataclasses import dataclass


# ---------------------------------------------------------------------------
# Configuration and simple DTOs
# ---------------------------------------------------------------------------

@dataclass
class RSMEvalConfig:
    """
    Minimal configuration for the RSM evaluation engine.
    """
    steps: int = 8
    stability_threshold_stable: float = 0.7
    stability_threshold_marginal: float = 0.4
    triad_index: int | None = None


@dataclass
class ResonanceSummary:
    """
    Minimal resonance-time summary DTO.
    """
    triad_index: int | None
    average_coherence: float
    stability_label: str
    ticks: int


# ---------------------------------------------------------------------------
# RSM Evaluation Engine
# ---------------------------------------------------------------------------

class RSMEvalEngine:
    """
    Minimal RSM evaluation engine.

    Each tick:
      1. Samples a coherence-like value from the input object
      2. Accumulates resonance-time statistics
      3. Optionally updates a stability profile-like object

    After N ticks:
      - Produces a ResonanceSummary
      - Classifies stability as stable / marginal / unstable
    """

    def __init__(self, config: RSMEvalConfig | None = None):
        self.config = config or RSMEvalConfig()
        self.ticks = 0
        self._coherence_samples: list[float] = []

    # ------------------------------------------------------------------
    # Core Tick
    # ------------------------------------------------------------------

    def run_tick(self, coherence_source, stability_profile=None):
        """
        Execute a single RSM evaluation tick.

        Parameters
        ----------
        coherence_source : object
            Must expose a numeric coherence-like attribute, e.g.:
              - level
              - coherence
              - coherence_level
        stability_profile : object or None
            May expose an update(label: str) method.

        Returns
        -------
        (coherence_value, stability_label)
        """
        self.ticks += 1

        coherence_value = self._extract_coherence(coherence_source)
        self._coherence_samples.append(coherence_value)

        # Provisional stability label based on current sample
        stability_label = self._classify(coherence_value)

        # Optionally update a stability profile-like object
        if stability_profile is not None and hasattr(stability_profile, "update"):
            stability_profile.update(stability_label)

        return coherence_value, stability_label

    # ------------------------------------------------------------------
    # Multi-tick runner
    # ------------------------------------------------------------------

    def run(self, coherence_source, stability_profile=None, steps: int | None = None):
        """
        Run multiple evaluation ticks in sequence.

        Parameters
        ----------
        steps : int or None
            Number of ticks to execute (defaults to config.steps).

        Returns
        -------
        ResonanceSummary
            Final resonance-time summary after all ticks.
        """
        total_steps = steps or self.config.steps
        for _ in range(total_steps):
            self.run_tick(coherence_source, stability_profile)

        return self.summarize()

    # ------------------------------------------------------------------
    # Summary and helpers
    # ------------------------------------------------------------------

    def summarize(self) -> ResonanceSummary:
        """
        Produce a minimal resonance-time summary.
        """
        if not self._coherence_samples:
            avg = 0.0
        else:
            avg = sum(self._coherence_samples) / len(self._coherence_samples)

        label = self._classify(avg)

        return ResonanceSummary(
            triad_index=self.config.triad_index,
            average_coherence=avg,
            stability_label=label,
            ticks=self.ticks,
        )

    def _extract_coherence(self, source) -> float:
        """
        Extract a coherence-like value from the source object.
        Tries common attribute names in order.
        """
        for attr in ("coherence_level", "coherence", "level"):
            if hasattr(source, attr):
                value = getattr(source, attr)
                try:
                    return float(value)
                except (TypeError, ValueError):
                    continue
        # Fallback: treat missing coherence as 0.0
        return 0.0

    def _classify(self, value: float) -> str:
        """
        Classify stability based on configured thresholds.
        """
        if value >= self.config.stability_threshold_stable:
            return "stable"
        if value >= self.config.stability_threshold_marginal:
            return "marginal"
        return "unstable"
