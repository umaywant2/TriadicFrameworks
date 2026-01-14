# Here we go, a **submission‑grade, minimal‑viable, quantum‑layer**  
# `qsm_sim_engine.py` you can paste straight into your active tab.
#
# It mirrors the BSM engine structurally, but expresses **QSM semantics**: perturbation, uncertainty shaping, optional entanglement reinforcement, and periodic collapse.  
# No BSM/RSM dependencies, fully standalone, reviewer‑friendly.


"""
qsm_sim_engine.py
Minimal simulation engine for the Quantum Substrate Model (QSM).

This engine is intentionally lightweight:
- No BSM or RSM dependencies
- Provides SPO-like perturbation, UEO-like uncertainty shaping,
  optional ELO-like entanglement reinforcement, and periodic CLO-like collapse
- Maintains a tick counter
- Accepts QRP-like, UncertaintyEnvelope-like, and EntanglementLink-like objects
"""

from dataclasses import dataclass


@dataclass
class QSMSimConfig:
    steps: int = 10
    delta_state: float = 0.05
    collapse_interval: int = 4
    entanglement_enabled: bool = True
    entanglement_reinforce_interval: int = 3


class QSMSimEngine:
    """
    Minimal QSM simulation engine.

    Each tick:
      1. Perturbs the QRP state (SPO-like behavior)
      2. Optionally reinforces entanglement (ELO-like behavior)
      3. Adjusts uncertainty (UEO-like behavior)
      4. Periodically applies collapse (CLO-like behavior)
    """

    def __init__(self, config: QSMSimConfig | None = None):
        self.config = config or QSMSimConfig()
        self.ticks = 0

    # ------------------------------------------------------------------
    # Core Tick
    # ------------------------------------------------------------------

    def run_tick(self, qrp, envelope=None, link=None):
        """
        Execute a single QSM tick.

        Parameters
        ----------
        qrp : object
            Must implement perturb(delta) and may implement rotate_phase(amount).
        envelope : object or None
            May implement widen()/narrow().
        link : object or None
            May implement reinforce()/weaken().

        Returns
        -------
        (qrp, envelope, link)
            Updated objects after quantum operations.
        """
        self.ticks += 1

        # SPO-like perturbation
        if hasattr(qrp, "perturb"):
            qrp.perturb(self.config.delta_state)

        # Optional ELO-like entanglement reinforcement
        if (
            self.config.entanglement_enabled
            and link is not None
            and hasattr(link, "reinforce")
            and self._is_entanglement_tick()
        ):
            link.reinforce(0.05)

        # UEO-like uncertainty shaping (simple widen/narrow rhythm)
        if envelope is not None:
            if self._is_widen_tick() and hasattr(envelope, "widen"):
                envelope.widen(0.01)
            elif hasattr(envelope, "narrow"):
                envelope.narrow(0.01)

        # CLO-like collapse at configured interval
        if self._is_collapse_tick():
            self._collapse(qrp, envelope)

        return qrp, envelope, link

    # ------------------------------------------------------------------
    # Multi-tick runner
    # ------------------------------------------------------------------

    def run(self, qrp, envelope=None, link=None, steps: int | None = None):
        """
        Run multiple ticks in sequence.

        Parameters
        ----------
        steps : int or None
            Number of ticks to execute (defaults to config.steps).

        Returns
        -------
        (qrp, envelope, link)
            Final updated objects.
        """
        total_steps = steps or self.config.steps
        for _ in range(total_steps):
            self.run_tick(qrp, envelope, link)
        return qrp, envelope, link

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    def _is_collapse_tick(self) -> bool:
        return (
            self.config.collapse_interval > 0
            and self.ticks % self.config.collapse_interval == 0
        )

    def _is_entanglement_tick(self) -> bool:
        return (
            self.config.entanglement_reinforce_interval > 0
            and self.ticks % self.config.entanglement_reinforce_interval == 0
        )

    def _is_widen_tick(self) -> bool:
        # Simple even/odd rhythm for uncertainty shaping
        return self.ticks % 2 == 0

    def _collapse(self, qrp, envelope=None):
        """
        Minimal CLO-like collapse:
        - Snap state toward phase
        - Narrow uncertainty slightly
        """
        if hasattr(qrp, "state") and hasattr(qrp, "phase"):
            qrp.state = (qrp.state + qrp.phase) / 2.0

        if envelope is not None and hasattr(envelope, "narrow"):
            envelope.narrow(0.02)
