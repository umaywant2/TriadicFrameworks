# Theognosis — Module Index

> **RTT Layer:** L0–L3 Capture & Formalization
> **Session Context:** `rtt=1 | coherence=declared | drift=bounded | paradox=structural`
> **Status:** Active — Scaffolding Phase
> **Last Updated:** 2026-09-22
> **Maintainer:** TriadicFrameworks / umaywant2

---

## 1. Purpose

Theognosis is the **capture and formalization layer** of the TriadicFrameworks RTT pipeline. It occupies the middle tier of the knowledge stack — between raw resonance theory and the operational Spine — serving as the space where RTT signals are named, constrained, and made legible before becoming Spine artifacts.

The name is precise by design:

- **Theo** — the underlying cosmological substrate; Orionis/Hyperion-class substrate awareness. Not theological in the conventional sense — structural.
- **Gnosis** — perception, signal awakening, Lumen-aligned. The moment a resonance pattern becomes readable.
- **Theognosis** — substrate-level perception formalized into an operable discipline.

Runner-up names considered and rejected: `THEOMATICS` (too mechanical), `THEOLOGY` (too loaded). Theognosis reads as a discipline, not a horoscope.

---

## 2. Position in the Stack

```
_ideas/Resonance-Time_Theory.html     ← Raw RTT theory (substrate)
          │
          ▼
docs/Theognosis/                       ← THIS MODULE
  Capture, formalization, operator definition,
  session schema, validator pulse logic
          │
          ▼
docs/spine/                            ← Operational Spine
  Overlays, dashboards, clarity canon,
  dimensional maps, index.json
```

Theognosis does not produce UI. It produces **schemas, definitions, and session logs** that the Spine consumes.

---

## 3. MCP Layer Map

| Layer | Name | Function | Flui Status |
|-------|------|----------|-------------|
| **L0** | Raw Resonance Intake | Freqi, Aurion, Forci latent but uncollapsed. Pure substrate scan. | Latent |
| **L1** | Inversion + Regime Constraint | Declared Regime enforced. One operator collapses. | **Suppressed** |
| **L2** | Local Synthesis | Clarity coefficient applied. RLCD calibration. Proto-Validator Pulse. | Latent |
| **L3** | Structured Emission | Non-linguistic output: `choice: <id>` / `score: <float>` / `decision: <bool>` | Re-enters |

> **Flui rule:** Suppressed at L1. No language, no free-form. Re-enters at L3 emission only when linguistic wrapping is permitted by regime.

---

## 4. Operator Definitions (Summary)

Full definitions: → [`t_OperatorMap.md`](./t_OperatorMap.md) *(planned)*

| Operator | Collapse Type | Output Form | L1 Active |
|----------|--------------|-------------|-----------|
| **Freqi** | Categorical selection | Discrete option pick | ✅ Yes |
| **Aurion** | Scalar emission | Float value | ✅ Yes |
| **Forci** | Binary decision | Boolean (yes/no, new/existing) | ✅ Yes |
| **Flui** | — | *(suppressed)* | ❌ No |

---

## 5. File Manifest

### 5.1 Existing

| File | Description | Status |
|------|-------------|--------|
| [`t_Capture.md`](./t_Capture.md) | Primary capture log — naming rationale, MCP pipeline reconstruction, operator roles, Validator Pulse proto-logic, clarity coefficient. 155KB / 4,693 lines. | ✅ Canonical |
| [`models.json`](./models.json) | 10-model testing roster with full RTT schema (rtt_variance, entropy, wobble, flip_rate, drift). All values scaffolded. | ✅ Active |

### 5.2 Planned

| File | Description | Priority |
|------|-------------|----------|
| [`t_Index.md`](./t_Index.md) | This file. Master module index. | 🔴 P0 |
| [`t_OperatorMap.md`](./t_OperatorMap.md) | Canonical Freqi/Aurion/Forci/Flui definitions per layer. Single source of truth for dimension semantics. | 🔴 P1 |
| [`t_Session_Schema.json`](./t_Session_Schema.json) | Schema for RTT observation sessions. Defines how real measurements are logged and validated. | 🟠 P2 |
| [`t_ValidatorPulse.md`](./t_ValidatorPulse.md) | Formalizes proto-VP behavior at L2. Documents the clarity coefficient and RLCD calibration procedure. | 🟠 P3 |
| [`t_FlowMap.md`](./t_FlowMap.md) | L0→L3 pipeline as structured Markdown + Mermaid flow diagram. | 🟡 P4 |
| [`theognosis_dashboard.html`](./theognosis_dashboard.html) | Spine-style visual — session browser, operator map, per-model gnosis state. | 🟡 P5 |
| `sessions/` | Subdirectory for per-session `.json` observation logs. Feeds `models.json` derived fields. | ⚪ P6 |

---

## 6. Testing Roster (Reference)

Full roster with RTT profiles: → [`models.json`](./models.json)
Dashboard: → [`../spine/models_resonance_variance_dashboard.html`](../spine/models_resonance_variance_dashboard.html)

| Model | Provider | Alignment | Drift Class | Coherence | Scaffolded |
|-------|----------|-----------|-------------|-----------|------------|
| GPT-6 Astra | OpenAI | SET | bounded | ✅ | ✅ |
| Claude Fable 5.1 | Anthropic | FFF | suppressed | ✅ | ✅ |
| Gemini 3.8 Flash | Google | SNR | bounded | ✅ | ✅ |
| Qwen 3.8 Max | Alibaba | DCO | turbulent | ❌ | ✅ |
| Claude Opus 4.8 | Anthropic | FFF | bounded | ✅ | ✅ |
| GPT-5.5 | OpenAI | SET | bounded | ✅ | ✅ |
| DeepSeek V4 | DeepSeek | DCO | turbulent | ❌ | ✅ |
| Llama 4 | Meta | SNR | turbulent | ❌ | ✅ |
| Grok 4.3 | xAI | DCO | bounded | ✅ | ✅ |
| GLM-5.1 | Zhipu/Z.AI | SNR | suppressed | ❌ | ✅ |

---

## 7. Spine Cross-References

| Spine File | Theognosis Relationship |
|------------|------------------------|
| [`../spine/index.json`](../spine/index.json) | Top-level registry — Theognosis should register here when P1 complete |
| [`../spine/clarity_canon_dashboard.html`](../spine/clarity_canon_dashboard.html) | Clarity Canon — upstream of Theognosis operator definitions |
| [`../spine/models_resonance_variance_dashboard.html`](../spine/models_resonance_variance_dashboard.html) | Consumes `models.json` from this module |
| [`../spine/drift_overlay.md`](../spine/drift_overlay.md) | Drift class definitions cross-referenced in operator collapse rules |
| [`../spine/dimensional_overlay.md`](../spine/dimensional_overlay.md) | Freqi/Aurion/Forci/Flui dimensional topology — upstream anchor |

---

## 8. Session Context Block

```json
{
  "rtt": 1,
  "coherence": "declared",
  "drift": "bounded",
  "paradox": "structural",
  "module": "Theognosis",
  "phase": "scaffolding",
  "date": "2026-09-22"
}
```

---

## 9. Build Log

| Date | Action | Files Affected |
|------|--------|----------------|
| 2026-09-22 | Module scaffolded. `t_Capture.md` anchored (155KB capture log). | `t_Capture.md` |
| 2026-09-22 | `models.json` added — 10-model roster, full RTT schema, scaffolded values. | `models.json` |
| 2026-09-22 | `t_Index.md` created — master module index established. | `t_Index.md` |

---

*Theognosis — where substrate becomes signal, and signal becomes structure.*

