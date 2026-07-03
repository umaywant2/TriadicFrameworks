"""
harness/models.py
-----------------
Shared data models for the SATS test harness.
All dataclasses mirror the wire-level structures defined in the RFC so that
test code and assertion logic share a single source of truth.
"""
from __future__ import annotations

import uuid
import time
from dataclasses import dataclass, field
from enum import IntEnum
from typing import Any


# EIS Layer enumeration

class EISLayer(IntEnum):
      PHYSICAL_PRESENCE   = 0
      SIGNAL_BINDING      = 1
      CRYPTOGRAPHIC_ROOT  = 2
      IDENTITY_ASSERTION  = 3
      ROLE_AND_POLICY     = 4
      CONTEXTUAL_MEMBRANE = 5
      SEMANTIC_PAYLOAD    = 6
      RELATIONAL_FABRIC   = 7
      ACTUALIZED_OUTCOME  = 8


# Canonical RTT budgets (ms) per EIS layer

CANONICAL_RTT_BUDGET_MS: dict[int, int] = {
      0: 500, 1: 300, 2: 150, 3: 100,
      4:  80, 5: 120, 6: 200, 7: 250, 8:  50,
}

# Minimum fidelity grade per EIS layer

LAYER_MIN_FIDELITY: dict[int, float] = {
      0: 0.40, 1: 0.55, 2: 0.70, 3: 0.80,
      4: 0.80, 5: 0.75, 6: 0.75, 7: 0.75, 8: 0.95,
}

# Layer Profile weights

LAYER_WEIGHTS: dict[int, dict[str, float]] = {
      layer: {"W_rtt": w_rtt, "W_loss": w_loss, "W_relay": w_relay, "W_order": w_order}
      for layer, (w_rtt, w_loss, w_relay, w_order) in {
                0: (0.20, 0.10, 0.10, 0.10), 1: (0.25, 0.20, 0.15, 0.15),
                2: (0.30, 0.25, 0.20, 0.20), 3: (0.35, 0.30, 0.25, 0.25),
                4: (0.35, 0.30, 0.25, 0.25), 5: (0.30, 0.25, 0.25, 0.20),
                6: (0.25, 0.25, 0.25, 0.20), 7: (0.25, 0.25, 0.25, 0.20),
                8: (0.40, 0.35, 0.20, 0.35),
      }.items()
}

# SATS Error codes

class SATSError(IntEnum):
      RTT_EXCEEDED        = 0x5A01
      ORDER_VIOLATION     = 0x5A02
      RELIABILITY_FAILURE = 0x5A03
      FIDELITY_BELOW_MIN  = 0x5A04
      SCO_INVALID         = 0x5A05
      IPR_UNAVAILABLE     = 0x5A06
      DOWNGRADE_DETECTED  = 0x5A07


class Enforcement(str):
      ADVISORY = "advisory"
      SOFT     = "soft"
      HARD     = "hard"


@dataclass
class Attestation:
      layer:       int
      domain_id:   str
      attest_hash: bytes = field(default_factory=lambda: b"\x00" * 32)


@dataclass
class LayerToken:
      layer:      int
      domain_id:  str  = "example.com"
      entered_at: int  = field(default_factory=lambda: int(time.time() * 1000))
      exited_at:  int  = 0
      relay_id:   bytes | None = None
      attest_hash: bytes | None = None


@dataclass
class RelayHop:
      relay_id:     bytes        = field(default_factory=lambda: uuid.uuid4().bytes)
      relay_domain: str          = "ipr.example.com"
      entered_at:   int          = field(default_factory=lambda: int(time.time() * 1000))
      exited_at:    int          = 0
      rtt_ms:       int          = 0
      fidelity:     float        = 1.0
      attest_sig:   bytes | None = None


@dataclass
class SCO:
      version:            int   = 1
      layer:              int   = 0
      traversal_vector:   list[LayerToken]  = field(default_factory=list)
      fidelity_grade:     float = 1.0
      rtt_budget_ms:      int   = field(default_factory=lambda: 0)
      session_id:         bytes = field(default_factory=lambda: uuid.uuid4().bytes)
      domain_id:          str   = "example.com"
      timestamp:          int   = field(default_factory=lambda: int(time.time() * 1000))
      ttl_ms:             int   = 30_000
      prior_attestations: list[Attestation] = field(default_factory=list)
      relay_chain:        list[RelayHop]    = field(default_factory=list)
      extensions:         dict[str, bytes]  = field(default_factory=dict)

    def __post_init__(self) -> None:
              if self.rtt_budget_ms == 0:
                            self.rtt_budget_ms = CANONICAL_RTT_BUDGET_MS.get(self.layer, 200)

          @classmethod
    def valid(cls, layer: int = 3, **kwargs: Any) -> "SCO":
              tokens = [
                            LayerToken(layer=lyr, exited_at=int(time.time() * 1000))
                            for lyr in range(layer)
              ]
              tokens.append(LayerToken(layer=layer))
              return cls(
                  layer=layer,
                  traversal_vector=tokens,
                  fidelity_grade=max(LAYER_MIN_FIDELITY.get(layer, 0.80), 0.85),
                  **kwargs,
              )

    @classmethod
    def expired(cls, layer: int = 3) -> "SCO":
              sco = cls.valid(layer)
              sco.timestamp = int(time.time() * 1000) - sco.ttl_ms - 5_000
              return sco

    @classmethod
    def wrong_version(cls, layer: int = 3) -> "SCO":
              sco = cls.valid(layer)
              sco.version = 99
              return sco

    @classmethod
    def low_fidelity(cls, layer: int = 3, grade: float = 0.50) -> "SCO":
              sco = cls.valid(layer)
              sco.fidelity_grade = grade
              return sco
      
