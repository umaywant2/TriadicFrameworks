def generate_overlay(fold_id, frequencies, alignment_scores):
    """
    Generates symbolic overlay SVG coordinates based on resonance data.
    """
    overlay = {
        "fold_id": fold_id,
        "nodes": [],
        "alignment": alignment_scores
    }

    for node, freq in frequencies.items():
        pulse = round(abs(freq % 1), 3)
        overlay["nodes"].append({
            "label": node,
            "frequency": freq,
            "pulse_amplitude": pulse
        })

    return overlay
