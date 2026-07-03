"""
harness/ordering.py
-------------------
Substrate-Aware Ordering Contract (SAOC) engine -- SS6.5.
Models layer-transition ordering with per-layer message queues.
"""
from __future__ import annotations

import time
from collections import defaultdict
from dataclasses import dataclass, field

from harness.models import SCO, SATSError


@dataclass
class Message:
      layer:   int
      payload: bytes
      sent_at: int  = field(default_factory=lambda: int(time.time() * 1000))
      acked:   bool = False


class OrderingEngine:
      """
          Enforces layer-transition ordering for a single SATS session.

              engine = OrderingEngine()
                  engine.enqueue(msg_at_layer_3)
                      engine.enqueue(msg_at_layer_4)  # held until L3 queue is empty + acked
                          delivered = engine.drain_ready()
                              """

    def __init__(self) -> None:
              self._queues: dict[int, list[Message]] = defaultdict(list)
              self._max_acked_layer: int = -1
              self._violations: list[tuple[int, int]] = []

    def enqueue(self, msg: Message) -> int | None:
              pending_layers = [l for l, q in self._queues.items() if any(not m.acked for m in q)]
              if pending_layers:
                            max_pending = max(pending_layers)
                            if msg.layer > max_pending:
                                              self._violations.append((msg.layer, max_pending))
                                              return SATSError.ORDER_VIOLATION
                                      self._queues[msg.layer].append(msg)
                        return None

    def ack_layer(self, layer: int) -> None:
              for msg in self._queues.get(layer, []):
                            msg.acked = True
                        if layer > self._max_acked_layer:
                                      self._max_acked_layer = layer

    def drain_ready(self) -> list[Message]:
              ready: list[Message] = []
        for layer in sorted(self._queues):
                      lower_layers_clear = all(
                                        all(m.acked for m in self._queues.get(l, []))
                                        for l in range(layer)
                      )
                      if lower_layers_clear:
                                        ready.extend(self._queues[layer])
                                return ready

    def violations(self) -> list[tuple[int, int]]:
              return list(self._violations)

    def queue_depth(self, layer: int) -> int:
              return len(self._queues.get(layer, []))

    def active_layers(self) -> list[int]:
              return [l for l, q in self._queues.items() if q]
