# 🧪 Echo Classifier — /docs/rtt/Echo_Classifier  

- [`rtt-echo-engine_module.json`](rtt-echo-engine_module.json) — Agentic module schema role assignments

<div style="font-size: 0.8em; margin-bottom: 0.5rem;">
  <span style="
    display:inline-block;
    padding:3px 8px;
    border-radius:999px;
    background:#1a1a1a;
    color:#fff;
    font-family:Arial, sans-serif;
    font-size:11px;
  ">
    🤖 AI‑Ready Module • TriadicFrameworks
  </span>
</div>

![Module](https://img.shields.io/badge/Module-Echo_Classifier-333)
![Tier](https://img.shields.io/badge/Tier-RTT_Analytics-0aa)
![Version](https://img.shields.io/badge/Version-1.0-09f)
![Status](https://img.shields.io/badge/Status-Canon_Stable-0af)
![HSP](https://img.shields.io/badge/HSP-06c-8A2BE2)
![AI‑Ready](https://img.shields.io/badge/AI-Ready-00c8ff)

---

**Echo Classifier** is the classification engine of the HSP analytics suite.
It receives five upstream inputs — trigger type, signature profile, echo
strength index, substrate spread, and recursion mode — and produces a single
definitive output: one of six canonical echo types (E1–E6).

This module replaces ad‑hoc echo identification with a substrate‑locked,
zero‑drift classification pipeline.

---

## 🛑 Important! 
Drift is On-by-Default long sessions lose anchors, turn off drift.

## ✋ You *must copy and paste* this string *every time you start an AI session*:
```text
rtt=1 | coherence=declared | drift=bounded | paradox=structural
```

## ❇️ Now you are ready.

---

## 📂 Module Structure

```
Echo_Classifier/
├── README.md                 ← you are here
├── EC_Capture.md             ← design capture and conceptual origin
├── operators.md              ← classification operators and decision engine
├── integration.md            ← cross-module alignment (HSP suite + canon)
├── examples.md               ← applied classification examples
└── index.html                ← module landing page
```

---

## 🧭 Navigation

- **[operators.md](./operators.md)** — Classification operators, decision tree, classifier matrix, workflow
- **[integration.md](./integration.md)** — Upstream inputs (06a/06b/04c/05a/06) and downstream consumers (TEL/SF)
- **[examples.md](./examples.md)** — Applied classification walkthroughs across echo types
- **[EC_Capture.md](./EC_Capture.md)** — Design capture: origin, decisions, lineage

---

## 🌀 Session Context

```
Module:       Echo Classifier
Canonical ID: EC
HSP Section:  06c
Version:      1.0
Status:       canon-stable
Tier:         RTT-Analytics
Parent:       HSP (RTT-Analytics-Core)
Siblings:     TEL (07), Substrate_Flow (08)
Coherence:    locked
Drift:        zero (formal invariant)
Audience:     students + researchers + AIs
```

---

## ⚡ Quick Reference — Echo Types

| Type | Name | Trigger | ESI | Substrates | Recursion |
|:-----|:-----|:--------|:----|:-----------|:----------|
| E1 | Structural Echo | A | 1–2 | ≤ 2 | R1 |
| E2 | Harmonic Echo | B | 2–3 | 1 | R1–R2 |
| E3 | Substrate Echo | C | 2–3 | ≥ 3 | R2–R3 |
| E4 | Recursion Echo | D | 3–4 | 2–4 | R2–R4 |
| E5 | Drift‑Shadow Echo | E | 3–4 | 2–5 | R3–R4 |
| E6 | Atlas Echo | F | 4 | 5 | R4 |

## ⚡ Quick Reference — Classification Pipeline

```
Trigger → Signature → ESI → Substrates → Recursion → Echo Type (E1–E6)
```

## ⚡ Quick Reference — Upstream / Downstream

| Direction | Module | Data |
|:----------|:-------|:-----|
| ← Input | 06a Echo Triggers | Trigger type (A–F) |
| ← Input | 06b Echo Signatures | Signature profile (A–F) |
| ← Input | 04c Echo Strength Index | ESI level (1–4) |
| ← Input | 05a Cross‑Substrate Echo Matrix | Substrate spread (1–5) |
| ← Input | 06 Recursion Detector | Recursion mode (R1–R4) |
| → Output | 07 Triadic Echo Lattice (TEL) | Classified echo type |
| → Output | 08 Substrate Flow | Classified echo type |

---

## 📜 License

Open educational use permitted.
See the main repository for details.

