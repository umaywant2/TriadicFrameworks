# Here is a **submission‑grade, minimal‑viable, triad‑aligned**  
# `qsm_rtt_forms.py` ready to paste directly into your active GitHub editor tab.
#
# It mirrors the structure of **bsm_rtt_forms.py**, but expresses the **quantum‑layer RTT forms**: quantum flow, collapse packets, uncertainty deltas, and QSM→BSM transfer summaries.  
# Everything is intentionally lightweight, independently functional, and aligned with the 3SM science‑trio submission pattern.


"""
qsm_rtt_forms.py
RTT Form specializations for the Quantum Substrate Model (QSM).

These forms provide the minimal data structures required for:
- QFF_QSM : quantum flow form
- QSET_QSM: quantum substrate exchange transfer
- QNR_QSM : quantum noise/uncertainty delta
- QER_QSM : quantum evaluation result

All forms are intentionally lightweight and independent of BSM/RSM.
"""


# ---------------------------------------------------------------------------
# QFF_QSM — Quantum Flow Form
# ---------------------------------------------------------------------------

class QFF_QSM:
    """
    Quantum Flow Form (QFF_QSM)
    Represents the evolving quantum state of a QRP during a tick.
    """

    def __init__(self, amplitude, phase, state):
        self.amplitude = amplitude
        self.phase = phase
        self.state = state

    def as_dict(self):
        return {
            "amplitude": self.amplitude,
            "phase": self.phase,
            "state": self.state,
        }


# ---------------------------------------------------------------------------
# QSET_QSM — Quantum Substrate Exchange Transfer
# ---------------------------------------------------------------------------

class QSET_QSM:
    """
    Quantum Substrate Exchange Transfer (QSET_QSM)
    Represents a minimal transfer packet for QSM → BSM.
    """

    def __init__(self, payload, triad_index=None):
        self.payload = payload
        self.triad_index = triad_index

    def as_dict(self):
        return {
            "payload": self.payload,
            "triad_index": self.triad_index,
        }


# ---------------------------------------------------------------------------
# QNR_QSM — Quantum Noise/Uncertainty Resonance Delta
# ---------------------------------------------------------------------------

class QNR_QSM:
    """
    Quantum Noise/Uncertainty Resonance (QNR_QSM)
    Represents uncertainty deltas produced during perturbation or collapse.
    """

    def __init__(self, delta_spread, triad_index=None):
        self.delta_spread = delta_spread
        self.triad_index = triad_index

    def as_dict(self):
        return {
            "delta_spread": self.delta_spread,
            "triad_index": self.triad_index,
        }


# ---------------------------------------------------------------------------
# QER_QSM — Quantum Evaluation Result
# ---------------------------------------------------------------------------

class QER_QSM:
    """
    Quantum Evaluation Result (QER_QSM)
    Represents the minimal evaluation summary after a QSM tick.
    """

    def __init__(self, state_value, uncertainty, notes=""):
        self.state_value = state_value
        self.uncertainty = uncertainty
        self.notes = notes

    def as_dict(self):
        return {
            "state_value": self.state_value,
            "uncertainty": self.uncertainty,
            "notes": self.notes,
        }


# This completes the **QSM RTT layer**, giving you a clean, minimal, independently functional quantum‑side RTT structure that mirrors BSM while preserving QSM semantics.
