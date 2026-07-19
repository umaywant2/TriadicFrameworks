# wrsadc_core.py

from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional
import uuid


@dataclass
class WRSADCEvent:
    id: str
    timestamp: datetime
    dimension: str
    entity: str
    state: str
    meta: Dict[str, Any] = field(default_factory=dict)


@dataclass
class WRSADCSnapshot:
    context: str
    total_events: int
    dimensions: List[str]
    entities: List[str]
    states: List[str]
    last_event: Optional[WRSADCEvent]


class WRSADC:
#    """
#    Wrapped Resonance Structural Aware Dimensional Core (WRSADC)
#
#    Provides:
#      - dimensional tracking
#      - state transitions
#      - structural snapshots
#      - triadic-friendly introspection
#
#    Designed for TFT_3Pack_v1.3 tools.
#    """

    def __init__(self, context: str = "tft-3pack"):
        self.context = context
        self._events: List[WRSADCEvent] = []

    def observe(
        self,
        dimension: str,
        entity: str,
        state: str,
        meta: Optional[Dict[str, Any]] = None,
    ) -> WRSADCEvent:
        event = WRSADCEvent(
            id=str(uuid.uuid4()),
            timestamp=datetime.utcnow(),
            dimension=dimension,
            entity=entity,
            state=state,
            meta=meta or {},
        )
        self._events.append(event)
        return event

    def snapshot(self) -> WRSADCSnapshot:
        dims = sorted({e.dimension for e in self._events})
        ents = sorted({e.entity for e in self._events})
        states = sorted({e.state for e in self._events})
        last_event = self._events[-1] if self._events else None

        return WRSADCSnapshot(
            context=self.context,
            total_events=len(self._events),
            dimensions=dims,
            entities=ents,
            states=states,
            last_event=last_event,
        )

    def debug_print(self) -> None:
        snap = self.snapshot()
        print(f"[WRSADC] context={snap.context}")
        print(f"  total_events: {snap.total_events}")
        print(f"  dimensions  : {', '.join(snap.dimensions) or '-'}")
        print(f"  entities    : {', '.join(snap.entities) or '-'}")
        print(f("  states      : {', '.join(snap.states) or '-'}"))
        if snap.last_event:
            le = snap.last_event
            print(f"  last_event  : {le.dimension}:{le.entity} -> {le.state} @ {le.timestamp.isoformat()}Z")

