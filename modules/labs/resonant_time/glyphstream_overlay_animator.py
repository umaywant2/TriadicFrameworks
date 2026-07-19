def animate_glyphstream_overlay(glyph_id, pulse_strength, quadrant):
    """
    Animates symbolic overlay based on pulse strength and observer quadrant.
    """
    scale = round(1 + pulse_strength * 0.1, 2)
    opacity = round(0.5 + pulse_strength * 0.5, 2)
    color = "#6c00ff" if quadrant == "W" else "#ffcc00" if quadrant == "E" else "#999999"

    return {
        "glyph": glyph_id,
        "scale": scale,
        "opacity": opacity,
        "color": color,
        "quadrant": quadrant,
        "notes": "Overlay animated based on observer quadrant and pulse strength."
    }
