# resonance_core.py

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Dict, List

from .dimensional_core import DimensionalCore, DimensionalSnapshot


@dataclass
class ResonanceView:
    context: str
    dimensions: Dict[str, DimensionalSnapshot] = field(default_factory=dict)


class ResonanceCore:
    """
    Resonance structural awareness core:
      - manages multiple DimensionalCore instances
      - provides a unified structural view
    """

    def __init__(self, context: str = "coeus-protocol"):
        self.context = context
        self._dimensions: Dict[str, DimensionalCore] = {}

    def dimension(self, name: str) -> DimensionalCore:
        if name not in self._dimensions:
            self._dimensions[name] = DimensionalCore(dimension_name=name)
        return self._dimensions[name]

    def snapshot(self) -> ResonanceView:
        snaps = {
            name: dim.snapshot()
            for name, dim in self._dimensions.items()
        }
        return ResonanceView(context=self.context, dimensions=snaps)

    def debug_print(self) -> None:
        view = self.snapshot()
        print(f"[ResonanceCore] context={view.context}")
        if not view.dimensions:
            print("  (no dimensions)")
            return
        for name, snap in view.dimensions.items():
            print(f"  dimension: {name}")
            print(f"    total_events: {snap.total_events}")
            print(f"    entities    : {', '.join(snap.entities) or '-'}")
            print(f"    states      : {', '.join(snap.states) or '-'}")

