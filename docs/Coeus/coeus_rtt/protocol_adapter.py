# protocol_adapter.py

from __future__ import annotations
from typing import Any, Dict

from .resonance_core import ResonanceCore


class CoeusRTTAdapter:
    """
    Coeus + RTT integration layer.

    Intended usage:
      - attach to your Coeus protocol handler
      - call record_* methods at key lifecycle points
      - use resonance.debug_print() or snapshot() for structural introspection
    """

    def __init__(self, context: str = "coeus-protocol"):
        self.resonance = ResonanceCore(context=context)

    def record_connection(self, client_id: str, state: str, meta: Dict[str, Any] | None = None) -> None:
        dim = self.resonance.dimension("connections")
        dim.observe(entity_id=client_id, state=state, meta=meta)

    def record_message(self, message_id: str, state: str, meta: Dict[str, Any] | None = None) -> None:
        dim = self.resonance.dimension("messages")
        dim.observe(entity_id=message_id, state=state, meta=meta)

    def record_entity(self, entity_id: str, state: str, meta: Dict[str, Any] | None = None) -> None:
        dim = self.resonance.dimension("entities")
        dim.observe(entity_id=entity_id, state=state, meta=meta)

    def structural_view(self):
        """Return a full resonance snapshot for external tooling / UI."""
        return self.resonance.snapshot()

    def debug_print(self) -> None:
        self.resonance.debug_print()

