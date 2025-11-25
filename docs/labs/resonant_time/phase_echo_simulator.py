def simulate_phase_echo(frequency, angle, lineage_id):
    """
    Simulates symbolic phase echo based on observer angle and remix lineage.
    """
    echo_strength = round((frequency % 144) / 144, 3)
    glyph = "glyph_protein_echo_02.svg" if echo_strength > 0.9 else "bridge_glyph_overlay_01.svg"
    trigger = "Remix lineage pulse" if lineage_id else "Residual harmonic"

    return {
        "frequency": frequency,
        "angle": angle,
        "echo_strength": echo_strength,
        "glyph": glyph,
        "trigger": trigger,
        "lineage": lineage_id or "Anonymous"
    }
