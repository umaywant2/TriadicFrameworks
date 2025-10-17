def simulate_quantum_echo(frequency, optimized_score):
    """
    Simulates symbolic echo from quantum optimization output.
    """
    glyph = "glyph_protein_echo_02.svg" if optimized_score > 2.7 else "bridge_glyph_overlay_01.svg"
    echo_strength = round(optimized_score / 3.0, 3)
    remix_trigger = optimized_score > 2.5

    return {
        "frequency": frequency,
        "optimized_score": optimized_score,
        "glyph": glyph,
        "echo_strength": echo_strength,
        "remix_trigger": remix_trigger
    }
