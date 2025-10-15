def predict_remix_trigger(forci, flui, freqi, lineage_id):
    """
    Predicts whether a fold will trigger remix lineage based on FFF alignment and contributor presence.
    """
    strength = forci * flui * freqi
    trigger = strength > 0.7 and lineage_id is not None

    return {
        "pulse_strength": round(strength, 3),
        "remix_trigger": trigger,
        "lineage": lineage_id or "Anonymous"
    }
