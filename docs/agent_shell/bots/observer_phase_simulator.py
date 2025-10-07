def simulate_observer_phase(quadrant, echo_strength):
    """
    Simulates overlay color and remix probability based on observer quadrant.
    """
    color_map = {
        "N": "#6c00ff",
        "S": "#ffcc00",
        "E": "#ff6699",
        "W": "#00cc99"
    }
    remix_probability = round(echo_strength * 0.85, 3)
    return {
        "quadrant": quadrant,
        "overlay_color": color_map.get(quadrant, "#999999"),
        "remix_probability": remix_probability
    }
