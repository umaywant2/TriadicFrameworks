## `rfc-substrate-awareness.md` — Document Summary

**Identifier:** `TFAWG-0001` · **Status:** Draft · **Category:** Informational · **Date:** 2026-07-02

### Abstract
Defines **Substrate-Aware Transport Services (SATS)** — an extension framework layering EIS substrate-consciousness onto the IETF TAPS transport model (RFC 8095 / RFC 8923), with HTTP-level field extensions aligned to RFC 9110.

---

### Section Coverage

| § | Title | Key Content |
|---|-------|-------------|
| 1 | **Introduction** | Problem framing; four SATS deliverables (SATS framework, SCO, IPR Negotiation, HTTP extensions) |
| 2 | **Conventions & Definitions** | RFC 2119 key words; full glossary: EIS, SATS, SCO, RTT-Budget, IPR, Traversal Vector, Fidelity Grade |
| 3 | **Motivation** | RFC 8923 gaps for enterprise identity; RTT/Inside as the two primary SATS axes |
| 4 | **EIS Substrate Model** | Full Layer 0–8 table (Symbol, Name, Description); canonical RTT budgets, reliability, ordering, and loss tolerance per layer; traversal semantics (ascending, descending, lateral, non-contiguous) |
| 5 | **Substrate Metadata** | SCO structure (CBOR + Structured Fields); `LayerToken` encoding; Traversal Vector construction rules; Fidelity Grade formula (`W_rtt × f_rtt × W_loss × f_loss × W_relay × f_relay × W_order × f_order`) |
| 6 | **Transport-Service Extensions** | RFC 8095/8923 anchoring; four SATS features: `sats-rtt-budget` (advisory/soft/hard enforcement), Inside-Path Relay Negotiation (IPR discovery via `/.well-known/sats-relays`, `RelayHop` structure), `sats-ordering-contract` (layer-transition ordering), `sats-reliability` (fidelity-graded with fallback/abort escalation) |
| 7 | **HTTP-Level Extensions** | 5 request fields (`Substrate-Layer`, `Substrate-Context`, `Substrate-RTT-Budget`, `Substrate-Traversal`, `Substrate-Domain`); 3 response fields; 2 trailer fields; 5 custom status codes (560–564); `sats-layer` media type parameter + `Accept-Substrate` |
| 8 | **Examples** | Five annotated exchanges: L0 bootstrap, L3 identity assertion with RTT budget, L6 semantic payload relay with trailer, non-contiguous 0→4→8 traversal, HTTP/2 push with substrate trailer |
| 9 | **Security Considerations** | SCO spoofing, RTT exhaustion attacks, IPR trust model, header injection, downgrade/strip attacks, SCO privacy requirements |
| 10 | **IANA Considerations** | Three registries: HTTP Header Fields (11 entries), Transport Error Codes (`0x5A01`–`0x5A07`), Layer Profile weights and minimum fidelity thresholds |
| 11–12 | **References** | Normative: RFC 2119, 8174, 8095, 8923, 9110, 8941, 8949, 4648 · Informative: RFC 8303, 9112, 9113, 9114, 8922, TAPS-ARCH |

---

