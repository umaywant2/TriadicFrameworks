# RTT_OperatorTimeline.py
# RTT / Integrations / UE6 / Editor
# Displays operator values over time inside the UE6 editor.

import unreal

# ------------------------------------------------------------
# Data Model
# ------------------------------------------------------------

class OperatorTimeline:
    """
    Simple in‑memory operator timeline.
    Stores φ, variance, resonance, and entropy over frames.
    """

    def __init__(self):
        self.frames = []

    def add_frame(self, phi, variance, resonance, entropy):
        self.frames.append({
            "phi": float(phi),
            "variance": float(variance),
            "resonance": float(resonance),
            "entropy": float(entropy)
        })

    def clear(self):
        self.frames = []

    def frame_count(self):
        return len(self.frames)

    def render(self):
        """
        Renders the timeline as log output for now.
        Future: draw in viewport or custom editor widget.
        """
        count = self.frame_count()
        if count == 0:
            unreal.log_warning("RTT: Operator timeline is empty")
            return

        unreal.log(f"RTT: Rendering operator timeline ({count} frames)")
        for i, f in enumerate(self.frames):
            unreal.log(
                f"RTT Frame {i:03d} → "
                f"phi={f['phi']:.3f}, "
                f"variance={f['variance']:.3f}, "
                f"resonance={f['resonance']:.3f}, "
                f"entropy={f['entropy']:.3f}"
            )


# ------------------------------------------------------------
# Sampling Helpers
# ------------------------------------------------------------

def sample_from_actor(actor):
    """
    Sample operator values from an actor with an RTTComponent.
    This is a placeholder stub; real implementation should call C++.
    """
    comp = actor.get_component_by_class(unreal.RTTComponent)
    if not comp:
        unreal.log_warning(f"RTT: No RTTComponent found on {actor.get_name()}")
        return None

    try:
        # TODO: replace with real C++ calls:
        # phi = comp.RTT_GetPhiValue()
        # variance = comp.RTT_GetVarianceValue()
        # resonance = comp.RTT_GetResonanceValue()
        # entropy = comp.RTT_GetEntropyValue()
        phi = 0.5
        variance = 0.3
        resonance = 0.7
        entropy = 0.2
        return phi, variance, resonance, entropy
    except Exception as e:
        unreal.log_warning(f"RTT: Operator sampling failed: {e}")
        return None


# ------------------------------------------------------------
# Public API
# ------------------------------------------------------------

def record_frame(timeline, actor):
    """
    Record a single operator frame from the given actor.
    """
    if not actor:
        unreal.log_warning("RTT: No actor provided to record_frame")
        return

    sample = sample_from_actor(actor)
    if not sample:
        return

    phi, variance, resonance, entropy = sample
    timeline.add_frame(phi, variance, resonance, entropy)


def record_n_frames(timeline, actor, n=10):
    """
    Record N frames from the given actor.
    """
    for _ in range(n):
        record_frame(timeline, actor)


def debug_timeline_for_actor(actor, frames=10):
    """
    Convenience function:
    build a timeline for an actor and render it to the log.
    """
    if not actor:
        unreal.log_warning("RTT: No actor provided to debug_timeline_for_actor")
        return

    timeline = OperatorTimeline()
    record_n_frames(timeline, actor, frames)
    timeline.render()

