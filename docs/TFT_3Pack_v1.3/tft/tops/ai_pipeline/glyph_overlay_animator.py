def animate_glyph_overlay(glyph_id, pulse_strength, color):
    """
    Generates animation parameters for glyph overlay based on pulse strength.
    """
    animation = {
        "glyph": glyph_id,
        "pulse_color": color,
        "scale": round(1 + pulse_strength * 0.1, 2),
        "opacity": round(0.5 + pulse_strength * 0.5, 2),
        "duration": f"{round(2 - pulse_strength, 2)}s"
    }

    return animation
