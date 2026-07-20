def simulate_observer_view(frequency, angle):
    """
    Simulates what an observer sees from a given angle in the resonance field.
    """
    quadrant_map = {
        "N": (0, 45),
        "E": (45, 135),
        "S": (135, 225),
        "W": (225, 315)
    }

    visible_quadrants = [q for q, (start, end) in quadrant_map.items() if start <= angle < end or (q == "N" and angle >= 315)]

    glyph_shadow = "glyph_protein_echo_02.svg" if frequency == 144 else "bridge_glyph_overlay_01.svg"
    phase_echo = "Remix lineage pulse detected" if frequency in [144, 33] else "Residual harmonic"

    return {
        "frequency": frequency,
        "angle": angle,
        "visible_quadrants": visible_quadrants,
        "glyph_shadow": glyph_shadow,
        "phase_echo": phase_echo
    }
