# Here is a **submission‑grade, minimal‑viable, triad‑aligned**  
# `qsm_entities.py` ready to drop directly into your active editing tab.
#
# It mirrors the structure of **bsm_entities.py**, but expresses the **quantum‑layer primitives**: QRPs, Uncertainty Envelopes, and Entanglement Links.  
# Everything is intentionally lightweight, independently functional, and aligned with the 3SM science‑trio submission pattern.


"""
qsm_entities.py
Core entity definitions for the Quantum Substrate Model (QSM).

This file provides the minimal, independently functional quantum-layer entities:
- QRP (Quantum Resonance Packet)
- UncertaintyEnvelope
- EntanglementLink

These entities are intentionally lightweight and match the expectations of:
- qsm_operators.py
- qsm_rtt_forms.py
- qsm_sim_engine.py
- the QSM test suite
"""


# ---------------------------------------------------------------------------
# QRP — Quantum Resonance Packet
# ---------------------------------------------------------------------------

class QRP:
    """
    Quantum Resonance Packet (QRP)
    Represents a discrete quantum packet in the QSM layer.

    Attributes
    ----------
    amplitude : float
        Magnitude of the packet.
    phase : float
        Phase offset used during collapse and entanglement.
    state : float
        Abstract quantum state value (minimal placeholder).
    """

    def __init__(self, amplitude=1.0, phase=0.0, state=0.0):
        self.amplitude = float(amplitude)
        self.phase = float(phase)
        self.state = float(state)

    def perturb(self, delta):
        """
        Minimal SPO-like perturbation behavior.
        Adjusts the quantum state slightly.
        """
        self.state += delta
        return self

    def rotate_phase(self, amount):
        """
        Minimal phase rotation behavior.
        """
        self.phase += amount
        return self


# ---------------------------------------------------------------------------
# UncertaintyEnvelope — Local Quantum Uncertainty Structure
# ---------------------------------------------------------------------------

class UncertaintyEnvelope:
    """
    UncertaintyEnvelope
    Represents the local uncertainty bounds around a QRP.

    Attributes
    ----------
    spread : float
        Width of the uncertainty distribution.
    bias : float
        Optional directional bias.
    """

    def __init__(self, spread=0.1, bias=0.0):
        self.spread = float(spread)
        self.bias = float(bias)

    def widen(self, amount=0.02):
        """
        Increase uncertainty spread.
        """
        self.spread += amount
        return self

    def narrow(self, amount=0.02):
        """
        Decrease uncertainty spread.
        """
        self.spread -= amount
        return self


# ---------------------------------------------------------------------------
# EntanglementLink — QRP-to-QRP Entanglement Structure
# ---------------------------------------------------------------------------

class EntanglementLink:
    """
    EntanglementLink
    Represents a minimal entanglement relationship between two QRPs.

    Attributes
    ----------
    qrp_a : QRP
    qrp_b : QRP
    strength : float
        Entanglement strength (0.0–1.0).
    """

    def __init__(self, qrp_a, qrp_b, strength=0.5):
        self.qrp_a = qrp_a
        self.qrp_b = qrp_b
        self.strength = float(strength)

    def reinforce(self, amount=0.05):
        """
        Strengthen the entanglement link.
        """
        self.strength = min(1.0, self.strength + amount)
        return self

    def weaken(self, amount=0.05):
        """
        Weaken the entanglement link.
        """
        self.strength = max(0.0, self.strength - amount)
        return self


# This gives you a **fully functional QSM entity layer** that mirrors the BSM structure while preserving the quantum‑layer semantics: perturbation, uncertainty, and entanglement.
