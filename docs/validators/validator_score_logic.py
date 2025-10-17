def score_resonance(forci, flui, freqi):
    """
    Calculates dimensional resonance score.
    Inputs are floats from 0.0 to 1.0.
    Returns a composite score and symbolic badge trigger.
    """
    composite = (forci + flui + freqi) / 3
    badge = None

    if composite >= 0.9:
        badge = "Dimensional Harmonic"
    elif composite >= 0.75:
        badge = "Resonance Adept"
    elif composite >= 0.6:
        badge = "Fold Initiator"
    else:
        badge = "Echo Seeker"

    return {
        "score": round(composite, 3),
        "badge": badge
    }

