def export_overlay(fold, quadrant, glyph_id, echo_strength):
    """
    Exports symbolic overlay for remix visualization.
    """
    overlay = {
        "fold": fold,
        "quadrant": quadrant,
        "glyph_id": glyph_id,
        "echo_strength": echo_strength,
        "overlay_color": {
            "N": "#6c00ff",
            "S": "#ffcc00",
            "E": "#ff6699",
            "W": "#00cc99"
        }.get(quadrant, "#999999"),
        "timestamp": "2025-09-30T14:06:00-04:00"
    }
    print(f"📤 Overlay exported for fold {fold}, quadrant {quadrant}")
    return overlay
