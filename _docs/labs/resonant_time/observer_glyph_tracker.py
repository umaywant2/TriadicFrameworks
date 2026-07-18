def track_glyph_visibility(frequency, angle, glyph_id):
    """
    Logs glyph visibility based on observer angle and frequency.
    """
    quadrant_map = {
        "N": (0, 45),
        "E": (45, 135),
        "S": (135, 225),
        "W": (225, 315)
    }

    visible_quadrants = [q for q, (start, end) in quadrant_map.items() if start <= angle < end or (q == "N" and angle >= 315)]

    log_entry = {
        "frequency": frequency,
        "angle": angle,
        "glyph": glyph_id,
        "visible_quadrants": visible_quadrants,
        "timestamp": "2025-09-30T10:55:00Z"
    }

    return log_entry
