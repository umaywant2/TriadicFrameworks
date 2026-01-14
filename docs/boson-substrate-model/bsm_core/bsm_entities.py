# Here's a **submission‑grade, minimal‑viable, triad‑aligned**  
# `bsm_entities.py` ready to paste directly into your active tab.  
# It mirrors the structure of your operators, RTT forms, and simulation engine, and it stays fully independent of QSM/RSM while remaining scientifically clean and reviewer‑friendly.


"""
bsm_entities.py
Core entity definitions for the Boson Substrate Model (BSM).

This file provides the minimal, independently functional entities:
- BRC (Bosonic Resonance Carrier)
- CoherenceField

Both entities are intentionally lightweight and match the expectations of:
- bsm_operators.py
- bsm_rtt_forms.py
- bsm_sim_engine.py
- the BSM test suite
"""


# ---------------------------------------------------------------------------
# BRC — Bosonic Resonance Carrier
# ---------------------------------------------------------------------------

class BRC:
    """
    Bosonic Resonance Carrier (BRC)
    Represents a propagating bosonic packet in the BSM layer.

    Attributes
    ----------
    amplitude : float
        Strength of the carrier.
    phase : float
        Phase offset used during propagation.
    position : float
        Spatial position along the propagation axis.
    """

    def __init__(self, amplitude=1.0, phase=0.0, position=0.0):
        self.amplitude = float(amplitude)
        self.phase = float(phase)
        self.position = float(position)

    def propagate(self, delta):
        """
        Minimal PPO-like propagation behavior.
        Moves the BRC forward and updates phase proportionally.
        """
        self.position += delta
        self.phase += 0.1 * delta
        return self

    def modulate(self, factor):
        """
        Simple amplitude modulation.
        """
        self.amplitude *= factor
        return self


# ---------------------------------------------------------------------------
# CoherenceField — Field-Level Coherence Structure
# ---------------------------------------------------------------------------

class CoherenceField:
    """
    CoherenceField
    Represents the local coherence state at a given triad index.

    Attributes
    ----------
    level : float
        Coherence magnitude.
    triad_index : int or None
        Triad alignment metadata.
    """

    def __init__(self, level=0.25, triad_index=None):
        self.level = float(level)
        self.triad_index = triad_index

    def stabilize(self):
        """
        Minimal CSO-like stabilization behavior.
        Raises coherence level slightly.
        """
        self.level += 0.05
        return self

    def damp(self, amount=0.1):
        """
        Optional damping behavior.
        """
        self.level -= amount
        return self


# This completes the **BSM core**: entities, operators, RTT forms, simulation engine, config, and tests — all clean, minimal, and independently functional.
