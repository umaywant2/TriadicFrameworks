
# dimensional_core.py

from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional
import uuid


@dataclass
class DimensionEvent:
    id: str
    timestamp: datetime
    entity_id: str
    state: str
    meta: Dict[str, Any] = field(default_factory=dict)


@dataclass
class DimensionalSnapshot:
    dimension_name: str
    total_events: int
    entities: List[str]
    states: List[str]
    last_event: Optional[DimensionEvent]


class DimensionalCore:
    """
    Dimensional core:
      - tracks entities and their state changes
      - provides structural snapshots for RTT-style reasoning
    """

    def __init__(self, dimension_name: str = "coeus"):
        self.dimension_name = dimension_name
        self._events: List[DimensionEvent] = []

    def observe(
        self,
        entity_id: str,
        state: str,
        meta: Optional[Dict[str, Any]] = None,
    ) -> DimensionEvent:
        event = DimensionEvent(
            id=str(uuid.uuid4()),
            timestamp=datetime.utcnow(),
            entity_id=entity_id,
            state=state,
            meta=meta or {},
        )
        self._events.append(event)
        return event

    def snapshot(self) -> DimensionalSnapshot:
        total = len(self._events)
        entities = sorted({e.entity_id for e in self._events})
        states = sorted({e.state for e in self._events})
        last_event = self._events[-1] if self._events else None

        return DimensionalSnapshot(
            dimension_name=self.dimension_name,
            total_events=total,
            entities=entities,
            states=states,
            last_event=last_event,
        )

    def debug_print(self) -> None:
        snap = self.snapshot()
        print(f"[DimensionalCore] dimension={snap.dimension_name}")
        print(f"  total_events: {snap.total_events}")
        print(f"  entities    : {', '.join(snap.entities) or '-'}")
        print(f"  states      : {', '.join(snap.states) or '-'}")
        if snap.last_event:
            le = snap.last_event
            print(f"  last_event  : {le.entity_id} -> {le.state} @ {le.timestamp.isoformat()}Z")
