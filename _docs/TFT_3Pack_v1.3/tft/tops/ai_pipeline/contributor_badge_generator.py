def generate_contributor_badge(contributor_id, remix_count):
    """
    Generates symbolic badge based on remix lineage impact.
    """
    tier = "Mythic" if remix_count >= 3 else "Echo" if remix_count == 2 else "Seed"
    badge = {
        "contributor": contributor_id,
        "tier": tier,
        "symbol": f"{tier.lower()}_badge.svg",
        "awarded_at": "2025-09-30T11:39:00-04:00"
    }

    return badge
