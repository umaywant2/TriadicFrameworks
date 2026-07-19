# RTT_MenuExtension.py
# RTT / Integrations / UE6 / Editor
# Adds RTT tools to the Unreal Engine 6 editor toolbar.

import unreal

# ------------------------------------------------------------
# Menu Entry Script
# ------------------------------------------------------------

@unreal.uclass()
class RTTMenuEntry(unreal.ToolMenuEntryScript):
    """
    Base class for RTT menu actions.
    Each subclass implements a single menu command.
    """
    pass


# ------------------------------------------------------------
# Menu Actions
# ------------------------------------------------------------

@unreal.uclass()
class RTTMenu_Resonance(RTTMenuEntry):
    @unreal.ufunction(override=True)
    def execute(self, context):
        from RTTTools import run_resonance_on_selected
        unreal.log("RTT: Menu → Visualize Resonance")
        run_resonance_on_selected()


@unreal.uclass()
class RTTMenu_Entropy(RTTMenuEntry):
    @unreal.ufunction(override=True)
    def execute(self, context):
        from RTTTools import run_entropy_on_world
        unreal.log("RTT: Menu → Inspect Entropy")
        run_entropy_on_world()


@unreal.uclass()
class RTTMenu_Timeline(RTTMenuEntry):
    @unreal.ufunction(override=True)
    def execute(self, context):
        from RTTTools import open_operator_timeline
        unreal.log("RTT: Menu → Operator Timeline")
        open_operator_timeline()


# ------------------------------------------------------------
# Menu Registration
# ------------------------------------------------------------

def register_rtt_menu():
    """
    Registers the RTT menu inside the UE6 Editor toolbar.
    """
    menus = unreal.ToolMenus.get()

    # Create or retrieve the main toolbar menu
    main_menu = menus.find_menu("LevelEditor.MainMenu")
    if not main_menu:
        unreal.log_warning("RTT: Could not find LevelEditor.MainMenu")
        return

    # Create RTT top-level section
    rtt_section = main_menu.add_section("RTTSection", "RTT Tools")

    # Add menu entries
    rtt_section.add_menu_entry_script(
        name="RTT_Resonance",
        label="Visualize Resonance",
        tool_tip="Visualize RTT resonance fields for the selected actor.",
        script_object=RTTMenu_Resonance()
    )

    rtt_section.add_menu_entry_script(
        name="RTT_Entropy",
        label="Inspect Entropy",
        tool_tip="Inspect entropy boundaries in the current world.",
        script_object=RTTMenu_Entropy()
    )

    rtt_section.add_menu_entry_script(
        name="RTT_Timeline",
        label="Operator Timeline",
        tool_tip="Open the RTT operator timeline debugger.",
        script_object=RTTMenu_Timeline()
    )

    menus.refresh_all_widgets()
    unreal.log("RTT: Editor menu registered")


# ------------------------------------------------------------
# Auto‑Register on Script Load
# ------------------------------------------------------------

register_rtt_menu()
