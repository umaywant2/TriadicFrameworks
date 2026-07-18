def map_contributor_echoes(contributor_id, folds):
    """
    Maps contributor impact across folds and glyph overlays.
    """
    echo_map = []
    for fold in folds:
        entry = {
            "contributor": contributor_id,
            "fold_id": fold["id"],
            "glyph": fold["glyph"],
            "pulse_strength": fold["pulse_strength"],
            "remix_trigger": fold["remix_trigger"]
        }
        echo_map.append(entry)
    return echo_map
