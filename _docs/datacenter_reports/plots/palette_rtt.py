"""
palette_rtt.py
RTT-Inside Color Palettes for Datacenter Reports
------------------------------------------------
Defines canonical color palettes used across RTT visualizations.

Design goals:
- Operator-first, drift-bounded
- Consistent across heatmaps, interactive plots, and dashboards
- Student-accessible, AI-parsable
- Matches the five-regime RTT palette (Stable, Transitional, Paradox, Interference, Coherence)
"""

# ------------------------------------------------------------
# Core Triadic Palettes
# ------------------------------------------------------------

RTT_PALETTE = {

    # Triadic gradient used for structural + global visualizations
    "triadic": [
        "#1a237e",  # deep indigo
        "#3949ab",  # indigo
        "#5c6bc0",  # soft indigo
        "#7e57c2",  # violet
        "#9575cd",  # soft violet
    ],

    # Dimensional fields palette (planetary → cultural → governance → compute → infrastructure)
    "dimensional": [
        "#0d47a1",  # planetary blue
        "#00838f",  # cultural teal
        "#6a1b9a",  # governance violet
        "#283593",  # compute indigo
        "#4e342e",  # infrastructure brown
    ],

    # Compute + qCompute palette (density, thermal, energy envelope)
    "compute": [
        "#1b5e20",  # deep green (energy envelope)
        "#43a047",  # compute density
        "#81c784",  # cooling
        "#c8e6c9",  # thermal buffer
    ],

    # Structural fields palette (facilities, governance, cultural substrate, standards, human envelope)
    "structural": [
        "#263238",  # facilities (slate)
        "#37474f",  # governance (steel)
        "#455a64",  # cultural substrate (blue-gray)
        "#546e7a",  # standards (cool gray)
        "#607d8b",  # human envelope (soft gray)
    ],

    # ------------------------------------------------------------
    # RTT Regime Palettes (canonical five-regime color system)
    # ------------------------------------------------------------

    "regime": {
        "stable": "#0d47a1",        # deep blue
        "transitional": "#ffb300",  # amber
        "paradox": "#c62828",       # crimson
        "interference": "#8e24aa",  # violet
        "coherence": "#2e7d32",     # emerald
    },

    # Convenience list for regime heatmaps
    "regime_list": [
        "#0d47a1",  # stable
        "#ffb300",  # transitional
        "#c62828",  # paradox
        "#8e24aa",  # interference
        "#2e7d32",  # coherence
    ],
}


def get_palette(name: str):
    """
    Retrieve a palette by name.
    """
    if name not in RTT_PALETTE:
        raise KeyError(f"Palette '{name}' not found in RTT_PALETTE.")
    return RTT_PALETTE[name]

