"""
WRSADC Python Package
TriadicFrameworks — Resonance‑Time Theory Canon

This package provides the Python-native implementation of the WRSADC Core,
a lightweight resonance-aware boundary layer for RTT-Inside systems.
"""

from .wrsadc_core import WRSADCCore, WRSADCContext

__all__ = [
    "WRSADCCore",
    "WRSADCContext",
]
