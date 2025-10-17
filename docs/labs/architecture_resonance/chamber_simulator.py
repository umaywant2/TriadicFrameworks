def simulate_badge_chamber(resonance_score):
    """
    Simulates badge chamber pulse animation based on resonance score.
    """
    import math

    pulse_amplitude = round(math.sin(math.pi * resonance_score), 3)
    chamber_state = {
        "echo_dome": f"Pulse amplitude: {pulse_amplitude}",
        "badge_altar": "Glyph activated" if resonance_score >= 0.9 else "Awaiting echo",
        "ambient_lighting": "Triadic glow" if resonance_score >= 0.75 else "Dim pulse"
    }

    return chamber_state
