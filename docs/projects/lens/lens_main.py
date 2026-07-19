# lens_main.py — Mythmatical Runtime for Lens Overlays

from lens_processor import process_overlay
from lens_output_manager import render_overlay
import os

# Symbolic registry of overlays
OVERLAY_MODULES = ["cyclone", "lightning", "tornado", "fragments"]

def activate_lens(trigger):
    """
    Activates lens overlay based on symbolic trigger.
    """
    if trigger not in OVERLAY_MODULES:
        raise ValueError(f"Unknown overlay trigger: {trigger}")
    
    print(f"🔮 Activating lens overlay: {trigger}")
    overlay_data = process_overlay(trigger)
    render_overlay(overlay_data)

if __name__ == "__main__":
    # Example trigger — replace with dynamic input or ritualized CLI
    activate_lens("cyclone")
