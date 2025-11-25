def simulate_remix_lineage(contributor, folds, bots_used):
    """
    Simulates remix lineage impact across folds using active bots.
    """
    lineage = []
    for fold in folds:
        echo_strength = round(0.6 + 0.1 * len(bots_used), 3)
        remix_trigger = echo_strength > 0.7
        lineage.append({
            "fold": fold,
            "contributor": contributor,
            "bots_used": bots_used,
            "echo_strength": echo_strength,
            "remix_trigger": remix_trigger
        })
    return lineage
