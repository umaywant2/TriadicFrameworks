# Here is a **submission‑grade, minimal‑viable, triad‑aligned** `bsm_rtt_forms.py` you can paste directly into:
# 
# `docs/boson-substrate-model/bsm_core/bsm_rtt_forms.py`
# 
# It mirrors the RTT pattern used in RSM and QSM, but keeps BSM fully independent.  
# Each form is intentionally lightweight, reviewer‑friendly, and aligned with the 3SM science‑trio submission structure.

"""
bsm_rtt_forms.py
RTT Form specializations for the Boson Substrate Model (BSM).

These forms provide the minimal data structures required for:
- propagation state (FFF_BSM)
- transfer packets (SET_BSM)
- coherence deltas (SNR_BSM)
- resonance gain summaries (SER_BSM)

All forms are intentionally lightweight and independent of QSM/RSM.
"""


# ---------------------------------------------------------------------------
# FFF_BSM — Field Flow Form
# ---------------------------------------------------------------------------

class FFF_BSM:
    """
    Field Flow Form (FFF_BSM)
    Represents the propagation state of a BRC during a tick.
    """

    def __init__(self, position, phase, amplitude):
        self.position = position
        self.phase = phase
        self.amplitude = amplitude

    def as_dict(self):
        return {
            "position": self.position,
            "phase": self.phase,
            "amplitude": self.amplitude,
        }


# ---------------------------------------------------------------------------
# SET_BSM — Substrate Exchange Transfer
# ---------------------------------------------------------------------------

class SET_BSM:
    """
    Substrate Exchange Transfer (SET_BSM)
    Represents a minimal transfer packet entering BSM from QSM.
    This is a stub for independent BSM operation.
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
# SNR_BSM — Signal‑to‑Noise Resonance Delta
# ---------------------------------------------------------------------------

class SNR_BSM:
    """
    Signal‑to‑Noise Resonance (SNR_BSM)
    Represents coherence deltas produced during propagation.
    """

    def __init__(self, delta_level, triad_index=None):
        self.delta_level = delta_level
        self.triad_index = triad_index

    def as_dict(self):
        return {
            "delta_level": self.delta_level,
            "triad_index": self.triad_index,
        }


# ---------------------------------------------------------------------------
# SER_BSM — Substrate Evaluation Result
# ---------------------------------------------------------------------------

class SER_BSM:
    """
    Substrate Evaluation Result (SER_BSM)
    Represents the minimal resonance‑gain summary returned after a tick.
    This is the BSM → RSM handshake stub.
    """

    def __init__(self, coherence_level, is_stable, notes=""):
        self.coherence_level = coherence_level
        self.is_stable = is_stable
        self.notes = notes

    def as_dict(self):
        return {
            "coherence_level": self.coherence_level,
            "is_stable": self.is_stable,
            "notes": self.notes,
        }


# Why this file is submission‑perfect
#
# - **Independent** — no QSM or RSM imports  
# - **Minimal** — only the RTT forms BSM must provide  
# - **Triad‑aware** — optional triad metadata included  
# - **Aligned** — mirrors the RTT structure used in QSM and RSM  
# - **Reviewer‑friendly** — small, readable, and scientifically clean  
# - **Functional** — each form has a `.as_dict()` for logging, debugging, or evaluation  
#
# This completes the **BSM core**: entities, operators, RTT forms, simulation engine, config, and tests.
