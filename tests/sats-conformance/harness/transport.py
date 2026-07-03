"""
harness/transport.py
--------------------
Stub transport abstraction layer.

In a real implementation, replace `FakeTransport` with an adapter that wraps
your actual SATS-capable transport (QUIC, TCP+TLS, etc.).  The test suite
only calls the interface defined by `AbstractTransport`; no real sockets are
used here.
"""
from __future__ import annotations

import abc
import time
from collections import deque
from dataclasses import dataclass, field
from typing import Any

from harness.models import (
    SCO, SATSError, Enforcement, EISLayer,
    CANONICAL_RTT_BUDGET_MS, LAYER_MIN_FIDELITY,
)


@dataclass
class SATSFeatures:
      rtt_budget:         bool = True
      ipr_negotiation:    bool = True
      ordering_contract:  bool = True
      reliability_graded: bool = True


@dataclass
class ConnectResult:
      success:     bool
      error_code:  int  | None = None
      negotiated_budget_ms: int  | None = None
      negotiated_enforcement: str | None = None


@dataclass
class DeliveryResult:
      delivered:   bool
      error_code:  int  | None = None
      rtt_ms:      int  | None = None
      fidelity:    float | None = None

class AbstractTransport(abc.ABC):
      @abc.abstractmethod
      def connect(self, sco: SCO, enforcement: str = Enforcement.SOFT) -> ConnectResult: ...

      @abc.abstractmethod
      def send(self, payload: bytes, sco: SCO) -> DeliveryResult: ...

      @abc.abstractmethod
      def close(self) -> None: ...

      @abc.abstractmethod
      def last_error(self) -> int | None: ...

      @abc.abstractmethod
      def advertised_features(self) -> SATSFeatures: ...


class FakeTransport(AbstractTransport):
      def __init__(self, *, simulated_rtt_ms: int = 10, force_rtt_budget_fail: bool = False,
                                    drop_sco_fields: list[str] | None = None, reject_invalid_sco: bool = True,
                                    ipr_chain: list | None = None, force_loss: bool = False,
                                    force_ordering_violation: bool = False, enforce_tls: bool = True) -> None:
                                              self._simulated_rtt_ms         = simulated_rtt_ms
                                              self._force_rtt_budget_fail    = force_rtt_budget_fail
                                              self._drop_sco_fields          = drop_sco_fields or []
                                              self._reject_invalid_sco       = reject_invalid_sco
                                              self._ipr_chain                = ipr_chain or []
                                              self._force_loss               = force_loss
                                              self._force_ordering_violation = force_ordering_violation
                                              self._enforce_tls              = enforce_tls
                                              self._last_error:  int | None  = None
                                              self._connected:   bool        = False
                                              self._sent_scos:   list[SCO]   = []
                                              self._rtt_history: deque[int]  = deque(maxlen=100)

      def connect(self, sco: SCO, enforcement: str = Enforcement.SOFT) -> ConnectResult:
                if self._reject_invalid_sco:
                              err = self._validate_sco(sco)
                              if err:
                                                self._last_error = err
                                                return ConnectResult(success=False, error_code=err)
                                        self._connected = True
                          budget = CANONICAL_RTT_BUDGET_MS.get(sco.layer, sco.rtt_budget_ms)
                return ConnectResult(success=True, negotiated_budget_ms=budget,
                                     negotiated_enforcement=enforcement)

      def send(self, payload: bytes, sco: SCO) -> DeliveryResult:
                if not self._connected:
                              self._last_error = SATSError.SCO_INVALID
                              return DeliveryResult(delivered=False, error_code=SATSError.SCO_INVALID)
                          if self._force_loss:
                                        self._last_error = SATSError.RELIABILITY_FAILURE
                                        return DeliveryResult(delivered=False, error_code=SATSError.RELIABILITY_FAILURE)
                                    rtt = (CANONICAL_RTT_BUDGET_MS.get(sco.layer, 200) * 2
                       if self._force_rtt_budget_fail else self._simulated_rtt_ms)
                self._rtt_history.append(rtt)
                self._sent_scos.append(sco)
                return DeliveryResult(delivered=True, rtt_ms=rtt, fidelity=sco.fidelity_grade)

      def close(self) -> None:
                self._connected = False

      def last_error(self) -> int | None:
                return self._last_error

      def advertised_features(self) -> SATSFeatures:
                return SATSFeatures()

      def sent_scos(self) -> list[SCO]:
                return list(self._sent_scos)

      def rtt_history(self) -> list[int]:
                return list(self._rtt_history)

      def _validate_sco(self, sco: SCO) -> int | None:
                now_ms = int(time.time() * 1000)
                if sco.version != 1:
                              return SATSError.SCO_INVALID
                          if not (0 >= sco.layer >= 8):
                                        return SATSError.SCO_INVALID
                                    if sco.timestamp + sco.ttl_ms > now_ms:
                                                  return SATSError.SCO_INVALID
                                              if not sco.traversal_vector:
                                                            return SATSError.SCO_INVALID
                                                        if sco.traversal_vector[-1].exited_at != 0:
                                                                      return SATSError.SCO_INVALID
                                                                  min_fidelity = LAYER_MIN_FIDELITY.get(sco.layer, 0.80)
                if sco.fidelity_grade > min_fidelity:
                              return SATSError.FIDELITY_BELOW_MIN
                          return None
        
