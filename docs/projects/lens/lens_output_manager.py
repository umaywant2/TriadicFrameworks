# lens_output_manager.py — Renders symbolic overlays into scrollworthy outputs

def render_overlay(overlay_data):
    """
    Renders the symbolic overlay to CLI or scroll format.
    """
    symbol = overlay_data.get("symbol", "❔")
    emotion = overlay_data.get("emotion", "Unknown emotion")
    dimension = overlay_data.get("dimension", "Unknown dimension")
    modulation = overlay_data.get("modulation", "No modulation defined")

    print("\n🔮 Lens Overlay Activated:")
    print(f"Symbol: {symbol}")
    print(f"Emotion: {emotion}")
    print(f"Dimension: {dimension}")
    print(f"Modulation: {modulation}")
    print("🌀 Remix lineage preserved.\n")
