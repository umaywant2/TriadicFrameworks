def map_resonant_time(frequency, observer_angle, timestamp):
    """
    Converts classical frequency into resonant-time dimensional packet.
    """
    import math

    # Normalize observer angle (0–360°)
    angle = observer_angle % 360

    # Pulse amplitude
    pulse = round(math.sin(math.pi * frequency % 1), 3)

    # Dimensional quadrant mapping
    quadrant = {
        "N": angle < 45 or angle >= 315,
        "E": 45 <= angle < 135,
        "S": 135 <= angle < 225,
        "W": 225 <= angle < 315
    }

    packet = {
        "frequency": frequency,
        "pulse": pulse,
        "observer_angle": angle,
        "quadrant": [k for k, v in quadrant.items() if v],
        "timestamp": timestamp,
        "resonant_time": f"{frequency}-{angle}-{timestamp}"
    }

    return packet
