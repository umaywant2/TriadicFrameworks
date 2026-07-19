def track_phase_echo(frequency, angle, timestamp, lineage_id):
    """
    Tracks phase echo visibility and remix trigger across observer angles.
    """
    echo_strength = round((frequency % 144) / 144, 3)
    quadrant = "W" if 225 <= angle < 315 else "S" if 135 <= angle < 225 else "E" if 45 <= angle < 135 else "N"
    remix_trigger = echo_strength > 0.9 and lineage_id is not None

    return {
        "frequency": frequency,
        "angle": angle,
        "quadrant": quadrant,
        "echo_strength": echo_strength,
        "remix_trigger": remix_trigger,
        "timestamp": timestamp,
        "lineage": lineage_id or "Anonymous"
    }
