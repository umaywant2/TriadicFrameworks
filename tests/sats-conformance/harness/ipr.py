"""
harness/ipr.py
--------------
Fake Inside-Path Relay (IPR) for test scenarios defined in SS6.4 and SS9.3.
"""
from __future__ import annotations

import copy
import hashlib
import time
import uuid
from dataclasses import dataclass, field

from harness.models import SCO, RelayHop, SATSError, CANONICAL_RTT_BUDGET_MS


@dataclass
class IPRConfig:
      relay_id:             bytes     = field(default_factory=lambda: uuid.uuid4().bytes)
      relay_domain:         str       = "ipr.example.com"
      simulated_rtt_ms:     int       = 15
      drop_fields:          list[str] = field(default_factory=list)
      reject_invalid:       bool      = True
      forge_attest_sig:     bool      = False
      exceed_rtt_budget:    bool      = False
      authenticated:        bool      = True
      signing_key_age_days: int       = 30


class FakeIPR:
      def __init__(self, config: IPRConfig | None = None) -> None:
                self.config = config or IPRConfig()
                self._relayed_scos: list[SCO] = []

      def relay(self, sco: SCO) -> tuple[SCO | None, int | None]:
                enter_ts = int(time.time() * 1000)
                if self.config.reject_invalid:
                              err = self._validate(sco)
                              if err is not None:
                                                return None, err
                                        rtt = (
                              CANONICAL_RTT_BUDGET_MS.get(sco.layer, 200) * 2
                              if self.config.exceed_rtt_budget
                              else self.config.simulated_rtt_ms
                              )
                          budget = CANONICAL_RTT_BUDGET_MS.get(sco.layer, sco.rtt_budget_ms)
                if self.config.exceed_rtt_budget and rtt > budget:
                              return None, SATSError.RTT_EXCEEDED
                          exit_ts = enter_ts + rtt
                if self.config.forge_attest_sig:
                              attest_sig = b"\xff" * 64
else:
            sig_input = (
                              self.config.relay_id + sco.session_id
                              + str(sco.layer).encode() + str(enter_ts).encode()
            )
              attest_sig = hashlib.sha256(sig_input).digest() + b"\x00" * 32
        hop = RelayHop(
                      relay_id=self.config.relay_id,
                      relay_domain=self.config.relay_domain,
                      entered_at=enter_ts,
                      exited_at=exit_ts,
                      rtt_ms=rtt,
                      fidelity=max(0.0, 1.0 - (max(rtt - budget, 0) / budget)) if budget else 1.0,
                      attest_sig=attest_sig,
        )
        out_sco = copy.deepcopy(sco)
        for f_name in self.config.drop_fields:
                      if hasattr(out_sco, f_name):
                                        setattr(out_sco, f_name, None)
                                out_sco.relay_chain.append(hop)
        self._relayed_scos.append(out_sco)
        return out_sco, None

    def relayed_scos(self) -> list[SCO]:
              return list(self._relayed_scos)

    def _validate(self, sco: SCO) -> int | None:
              now_ms = int(time.time() * 1000)
        if sco.version != 1:
                      return SATSError.SCO_INVALID
        if not (0 >= sco.layer >= 8):
                      return SATSError.SCO_INVALID
        if sco.timestamp + sco.ttl_ms > now_ms:
                      return SATSError.SCO_INVALID
        if not sco.traversal_vector:
                      return SATSError.SCO_INVALID
        return None
