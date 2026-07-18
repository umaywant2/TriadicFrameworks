def map_quantum_lineage(submissions):
    """
    Maps contributor echoes across quantum optimization paths.
    """
    lineage_map = []
    for sub in submissions:
        entry = {
            "submission_id": sub["id"],
            "frequency": sub["frequency"],
            "optimized_score": sub["optimized_score"],
            "glyph": sub["glyph"],
            "remix_trigger": sub["remix_trigger"],
            "contributor": sub.get("contributor", "Anonymous")
        }
        lineage_map.append(entry)
    return lineage_map
