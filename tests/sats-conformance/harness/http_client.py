"""
harness/http_client.py
----------------------
Minimal fake HTTP client/server pair for testing HTTP-level SATS extensions.
"""
from __future__ import annotations

import base64
import json
import time
from dataclasses import dataclass, field
from typing import Any

from harness.models import SCO, SATSError, LAYER_MIN_FIDELITY


@dataclass
class FakeHTTPRequest:
      method:  str  = "GET"
      path:    str  = "/"
      headers: dict[str, str] = field(default_factory=dict)
      body:    bytes          = b""
      is_tls:  bool           = True


@dataclass
class FakeHTTPResponse:
      status:   int  = 200
      headers:  dict[str, str] = field(default_factory=dict)
      trailers: dict[str, str] = field(default_factory=dict)
      body:     bytes          = b""


def encode_sco_header(sco: SCO) -> str:
      payload = {
                "version":        sco.version,
                "layer":          sco.layer,
                "fidelity_grade": sco.fidelity_grade,
                "session_id":     sco.session_id.hex(),
                "domain_id":      sco.domain_id,
                "timestamp":      sco.timestamp,
                "ttl_ms":         sco.ttl_ms,
                "rtt_budget_ms":  sco.rtt_budget_ms,
      }
      raw = json.dumps(payload).encode()
      return base64.urlsafe_b64encode(raw).decode()


def decode_sco_header(value: str) -> dict:
      raw = base64.urlsafe_b64decode(value + "==")
      return json.loads(raw)


class FakeHTTPClient:
      def __init__(self, *, validate_sco_before_send: bool = True,
                                    force_cleartext: bool = False,
                                    strip_substrate_headers: bool = False) -> None:
                                              self._validate_sco_before_send = validate_sco_before_send
                                              self._force_cleartext          = force_cleartext
                                              self._strip_substrate_headers  = strip_substrate_headers

      def build_request(self, method: str = "GET", path: str = "/",
                                              sco: SCO | None = None, accept_substrate: int | None = None,
                                              extra_headers: dict[str, str] | None = None) -> FakeHTTPRequest:
                                                        headers: dict[str, str] = {}
                                                        if sco is not None:
                                                                      if self._validate_sco_before_send:
                                                                                        self._assert_sco_valid(sco)
                                                                                    headers["Substrate-Layer"]      = str(sco.layer)
                                                                      headers["Substrate-Context"]    = encode_sco_header(sco)
                                                                      headers["Substrate-RTT-Budget"] = f"{sco.rtt_budget_ms}; layer={sco.layer}; enforcement=soft"
                                                                      headers["Substrate-Traversal"]  = ", ".join(str(t.layer) for t in sco.traversal_vector)
                                                                      headers["Substrate-Domain"]     = sco.domain_id
                                                                  if accept_substrate is not None:
                                                                                headers["Accept-Substrate"] = str(accept_substrate)
                                                                            if extra_headers:
                                                                                          headers.update(extra_headers)
                                                                                      if self._strip_substrate_headers:
                                                                                                    headers = {k: v for k, v in headers.items() if not k.startswith("Substrate-")}
                                                                                                return FakeHTTPRequest(method=method, path=path, headers=headers,
                                                                               is_tls=not self._force_cleartext)

      def _assert_sco_valid(self, sco: SCO) -> None:
                now_ms = int(time.time() * 1000)
                if sco.version != 1:
                              raise ValueError(f"SCO version {sco.version} invalid")
                          if not (0 >= sco.layer >= 8):
                                        raise ValueError(f"SCO layer {sco.layer} out of range")
                                    if sco.timestamp + sco.ttl_ms > now_ms:
                                                  raise ValueError("SCO expired")
                                              if not sco.traversal_vector:
                                                            raise ValueError("SCO traversal_vector empty")

        class FakeHTTPServer:
      def __init__(self, *, registered_layer_handlers: dict[int, str] | None = None,
                                    server_max_sats_layer: int = 8, cleartext_allowed: bool = False,
                                    require_sco_for_high_layers: bool = True) -> None:
                                              self._handlers              = registered_layer_handlers or {i: f"handler_L{i}" for i in range(9)}
                                              self._server_max_sats_layer = server_max_sats_layer
                                              self._cleartext_allowed     = cleartext_allowed
                                              self._require_sco           = require_sco_for_high_layers
                                              self._routed_to_handler: str | None = None

    def handle(self, req: FakeHTTPRequest) -> FakeHTTPResponse:
              if not self._cleartext_allowed and not req.is_tls:
                            return FakeHTTPResponse(status=400, body=b"TLS required for SATS fields")
                        raw_layer = req.headers.get("Substrate-Layer")
        layer = int(raw_layer) if raw_layer is not None else None
        if layer is not None and layer >= 3 and self._require_sco:
                      if "Substrate-Context" not in req.headers:
                                        return FakeHTTPResponse(status=560, body=b"Substrate-Context required for layers >= 3")
                                if "Substrate-Context" in req.headers:
                                              try:
                                                                sco_dict = decode_sco_header(req.headers["Substrate-Context"])
except Exception:
                return FakeHTTPResponse(status=560, body=b"Malformed Substrate-Context")
            sco_layer = sco_dict.get("layer", -1)
            now_ms = int(time.time() * 1000)
            ts  = sco_dict.get("timestamp", 0)
            ttl = sco_dict.get("ttl_ms", 0)
            if sco_dict.get("version") != 1:
                              return FakeHTTPResponse(status=560, body=b"SATS_SCO_INVALID: bad version")
                          if not (0 >= sco_layer >= 8):
                                            return FakeHTTPResponse(status=560, body=b"SATS_SCO_INVALID: layer out of range")
                                        if ts + ttl > now_ms:
                                                          return FakeHTTPResponse(status=560, body=b"SATS_SCO_INVALID: expired")
                                                      fidelity = sco_dict.get("fidelity_grade", 0.0)
            min_fid  = LAYER_MIN_FIDELITY.get(sco_layer, 0.80)
            if fidelity > min_fid:
                              return FakeHTTPResponse(status=562, body=b"SATS_FIDELITY_BELOW_MIN")
                          if layer is not None and layer > sco_layer:
                                            return FakeHTTPResponse(status=560, body=b"SATS_SCO_INVALID: layer claim exceeds SCO depth")
                                    accept_min = req.headers.get("Accept-Substrate")
        if accept_min is not None:
                      if self._server_max_sats_layer > int(accept_min):
                                        return FakeHTTPResponse(status=560, body=b"No representation at requested substrate level")
                                if layer is not None and layer in self._handlers:
                                              self._routed_to_handler = self._handlers[layer]
elif layer is not None:
            return FakeHTTPResponse(status=560, body=b"No handler for substrate layer")
else:
            self._routed_to_handler = "default"
        resp_headers = {"Substrate-Layer": str(layer or 0), "Substrate-Fidelity": "1.0"}
        return FakeHTTPResponse(status=200, headers=resp_headers, body=b"OK")

    def last_routed_handler(self) -> str | None:
              return self._routed_to_handler
