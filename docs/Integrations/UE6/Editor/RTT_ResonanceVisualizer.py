# RTT_ResonanceVisualizer.py
# RTT / Integrations / UE6 / Editor
# Visualizes resonance fields for any Actor using RTT’s resonance operator.

import unreal

# ------------------------------------------------------------
# Helpers
# ------------------------------------------------------------

def _draw_resonance_sphere(actor, frame):
    """
    Draws a resonance sphere based on amplitude, frequency, and phase.
    """
    loc = actor.get_actor_location()

    # Color encodes resonance amplitude (hot → cold)
    color = unreal.LinearColor(
        frame.amplitude,          # red channel
        0.1 + frame.phase * 0.2,  # green channel
        1.0 - frame.amplitude,    # blue channel
        1.0                       # alpha
    )

    radius = 50.0 + frame.amplitude * 200.0

    unreal.SystemLibrary.draw_debug_sphere(
        actor,
        loc,
        radius,
        32,
        color,
        0.05,   # duration
        2.0     # thickness
    )


def _probe_resonance(actor):
    """
    Calls the RTT C++ component to get a resonance frame.
    """
    comp = actor.get_component_by_class(unreal.RTTComponent)
    if not comp:
        unreal.log_warning(f"RTT: No RTTComponent found on {actor.get_name()}")
        return None

    try:
        frame = comp.RTT_ProbeResonance(actor)
        return frame
    except Exception as e:
        unreal.log_warning(f"RTT: Resonance probe failed: {e}")
        return None


# ------------------------------------------------------------
# Public API
# ------------------------------------------------------------

def visualize(actor):
    """
    Visualizes the resonance field for the given actor.
    This is the main entry point called by RTTTools.py.
    """
    if not actor:
        unreal.log_warning("RTT: No actor provided to resonance visualizer")
        return

    unreal.log(f"RTT: Running resonance visualizer for {actor.get_name()}")

    frame = _probe_resonance(actor)
    if not frame:
        unreal.log_warning("RTT: No resonance frame returned")
        return

    _draw_resonance_sphere(actor, frame)

    unreal.log(
        f"RTT: Resonance → amplitude={frame.amplitude:.3f}, "
        f"frequency={frame.frequency:.3f}, phase={frame.phase:.3f}"
    )
