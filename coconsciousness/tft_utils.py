"""
tft_utils.py — TriadicFrameworks TFT Time Helpers

This module replaces placeholder τ calculations in demos and validators
with actual calls to the TFT transform from your framework.

Keep it tiny: developers can read it in 60 seconds and see how to swap in
their own TFT or resonance function.
"""

# Placeholder import — replace with your actual TFT library/module import
# from tft_core import tft_transform

def tau_from_tft(classic_time, phase=0.0, **kwargs):
    """
    Convert classic time (seconds) to resonant time τ using TFT transform.
    
    Args:
        classic_time (float): Wall-clock seconds or similar.
        phase (float): Optional phase offset for loop staggering.
        **kwargs: Extra options passed through to TFT transform.
    
    Returns:
        float: Resonant time τ
    """
    # Replace the line below with the real TFT call:
    # return tft_transform(classic_time + phase, **kwargs)
    
    # Temporary fallback: gentle oscillator to keep demos running
    import math
    return math.sin(classic_time + phase)
