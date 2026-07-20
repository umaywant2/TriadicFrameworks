"""
rsm_rtt_forms.py
RTT Form specializations for the Resonance Substrate Model (RSM).

Minimal data structures:
- RFF_RSM  : resonance flow form
- RSET_RSM : resonance transfer packet
- RNR_RSM  : resonance delta
- RER_RSM  : resonance evaluation result

All forms are lightweight and independent of QSM/BSM.
"""


# ---------------------------------------------------------------------------
# RFF_RSM — Resonance Flow Form
# ---------------------------------------------------------------------------

class RFF_RSM:
    """
    Resonance Flow Form (RFF_RSM)
    Represents resonance flow during an evaluation window.
    """

    def __init__(self, coherence_level, gain, triad_index=None):
        self.coherence_level = coherence_level
        self.gain = gain
        self.triad_index = triad_index

    def as_dict(self):
        return {
            "coherence_level": self.coherence_level,
            "gain": self.gain,
            "triad_index": self.triad_index,
        }


# ---------------------------------------------------------------------------
# RSET_RSM — Resonance Substrate Exchange Transfer
# ---------------------------------------------------------------------------

class RSET_RSM:
    """
    Resonance Substrate Exchange Transfer (RSET_RSM)
    Minimal transfer packet for BSM → RSM or RSM → external.
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
# RNR_RSM — Resonance Delta
# ---------------------------------------------------------------------------

class RNR_RSM:
    """
    Resonance Delta (RNR_RSM)
    Represents a small change in coherence or gain.
    """

    def __init__(self, delta_coherence, delta_gain=0.0, triad_index=None):
        self.delta_coherence = delta_coherence
        self.delta_gain = delta_gain
        self.triad_index = triad_index

    def as_dict(self):
        return {
            "delta_coherence": self.delta_coherence,
            "delta_gain": self.delta_gain,
            "triad_index": self.triad_index,
        }


# ---------------------------------------------------------------------------
# RER_RSM — Resonance Evaluation Result
# ---------------------------------------------------------------------------

class RER_RSM:
    """
    Resonance Evaluation Result (RER_RSM)
    Minimal evaluation summary after an RSM run.
    """

    def __init__(self, average_coherence, stability_label, triad_index=None, notes=""):
        self.average_coherence = average_coherence
        self.stability_label = stability_label
        self.triad_index = triad_index
        self.notes = notes

    def as_dict(self):
        return {
            "average_coherence": self.average_coherence,
            "stability_label": self.stability_label,
            "triad_index": self.triad_index,
            "notes": self.notes,
        }

