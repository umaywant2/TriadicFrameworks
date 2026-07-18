def generate_fold_glyph(forci, flui, freqi):
    """
    Generates symbolic glyph overlay based on FFF alignment.
    """
    glyph_id = "glyph_protein_echo_02.svg" if freqi > 0.9 else "bridge_glyph_overlay_01.svg"
    pulse_color = "#6c00ff" if forci + flui + freqi > 2.7 else "#999999"
    pulse_strength = round((forci * flui * freqi), 3)

    return {
        "glyph": glyph_id,
        "color": pulse_color,
        "pulse_strength": pulse_strength,
        "notes": "Glyph selected based on triadic resonance alignment."
    }
