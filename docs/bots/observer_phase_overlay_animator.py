def animate_phase_overlay(quadrant, glyph_id, echo_strength):
    """
    Animates symbolic overlay based on observer quadrant and echo strength.
    """
    color_map = {
        "N": "#6c00ff",
        "S": "#ffcc00",
        "E": "#ff6699",
        "W": "#00cc99"
    }
    scale = round(1 + echo_strength * 0.1, 2)
    opacity = round(0.5 + echo_strength * 0.5, 2)

    return {
        "glyph": glyph_id,
        "quadrant": quadrant,
        "color": color_map.get(quadrant, "#999999"),
        "scale": scale,
        "opacity": opacity,
        "notes": "Overlay animated with quadrant logic and pulse strength."
    }
