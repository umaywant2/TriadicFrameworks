# RTTTools.py
# RTT / Integrations / UE6 / Editor
# Entry point for all RTT editor utilities inside Unreal Engine 6

import unreal

@unreal.uclass()
class RTTTools(unreal.GlobalEditorUtilityBase):
    """
    RTTTools is the central access point for all RTT editor utilities.
    It exposes resonance visualization, entropy inspection, and operator
    timeline debugging for UE6.
    """
    pass


# ------------------------------------------------------------
# Resonance Visualization
# ------------------------------------------------------------

def visualize_resonance(actor):
    """
    Visualize resonance fields for the selected actor.
    Calls the RTT_ResonanceVisualizer module.
    """
    unreal.log(f"RTT: Visualizing resonance for {actor.get_name()}")
    try:
        import RTT_ResonanceVisualizer as rv
        rv.visualize(actor)
    except Exception as e:
        unreal.log_warning(f"RTT: Resonance visualizer failed: {e}")


# ------------------------------------------------------------
# Entropy Inspection
# ------------------------------------------------------------

def inspect_entropy(world):
    """
    Inspect entropy boundaries and collapse signatures in the world.
    Calls the RTT_EntropyInspector module.
    """
    unreal.log(f"RTT: Inspecting entropy in world {world.get_name()}")
    try:
        import RTT_EntropyInspector as ei
        ei.inspect(world)
    except Exception as e:
        unreal.log_warning(f"RTT: Entropy inspector failed: {e}")


# ------------------------------------------------------------
# Operator Timeline Debugger
# ------------------------------------------------------------

def open_operator_timeline():
    """
    Open the operator timeline debugger.
    Calls the RTT_OperatorTimeline module.
    """
    unreal.log("RTT: Opening operator timeline")
    try:
        import RTT_OperatorTimeline as ot
        timeline = ot.OperatorTimeline()
        timeline.render()
    except Exception as e:
        unreal.log_warning(f"RTT: Operator timeline failed: {e}")


# ------------------------------------------------------------
# Utility Helpers
# ------------------------------------------------------------

def get_selected_actor():
    """
    Returns the currently selected actor in the editor.
    """
    selected = unreal.EditorUtilityLibrary.get_selected_assets()
    if selected:
        return selected[0]
    return None


def run_resonance_on_selected():
    """
    Convenience function: run resonance visualization on the selected actor.
    """
    actor = get_selected_actor()
    if actor:
        visualize_resonance(actor)
    else:
        unreal.log_warning("RTT: No actor selected for resonance visualization")


def run_entropy_on_world():
    """
    Convenience function: run entropy inspection on the current world.
    """
    world = unreal.EditorLevelLibrary.get_editor_world()
    if world:
        inspect_entropy(world)
    else:
        unreal.log_warning("RTT: No world context available for entropy inspection")
