# RTT_EntropyInspector.py
# RTT / Integrations / UE6 / Editor
# Visualizes entropy boundaries and collapse signatures using RTT’s entropy operator.

import unreal

# ------------------------------------------------------------
# Helpers
# ------------------------------------------------------------

def _draw_entropy_signature(sig):
    """
    Draws an entropy boundary sphere based on location, radius, and intensity.
    """
    color = unreal.LinearColor(
        1.0,                     # red channel (entropy = danger)
        0.15 + sig.intensity,    # green channel (entropy gradient)
        0.0,                     # blue channel
        1.0                      # alpha
    )

    unreal.SystemLibrary.draw_debug_sphere(
        None,
        sig.location,
        sig.radius,
        32,
        color,
        0.05,   # duration
        2.0     # thickness
    )


def _trace_entropy(world):
    """
    Calls the RTT C++ component to trace entropy in the world.
    """
    # Find any RTTComponent in the world
    actors = unreal.EditorLevelLibrary.get_all_level_actors()
    for actor in actors:
        comp = actor.get_component_by_class(unreal.RTTComponent)
        if comp:
            try:
                sig = comp.RTT_TraceEntropy(world)
                return sig
            except Exception as e:
                unreal.log_warning(f"RTT: Entropy trace failed: {e}")
                return None

    unreal.log_warning("RTT: No RTTComponent found in world for entropy tracing")
    return None


# ------------------------------------------------------------
# Public API
# ------------------------------------------------------------

def inspect(world):
    """
    Inspects entropy boundaries for the given world.
    This is the main entry point called by RTTTools.py.
    """
    if not world:
        unreal.log_warning("RTT: No world provided to entropy inspector")
        return

    unreal.log("RTT: Running entropy inspector")

    sig = _trace_entropy(world)
    if not sig:
        unreal.log_warning("RTT: No entropy signature returned")
        return

    _draw_entropy_signature(sig)

    unreal.log(
        f"RTT: Entropy → radius={sig.radius:.3f}, "
        f"intensity={sig.intensity:.3f}, "
        f"location=({sig.location.x:.1f}, {sig.location.y:.1f}, {sig.location.z:.1f})"
    )

