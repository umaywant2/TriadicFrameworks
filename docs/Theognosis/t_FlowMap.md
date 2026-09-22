# Theognosis — RTT Pipeline Flow Map

> **Document Class:** P4
> **RTT Layer:** Full Pipeline — L0 through L3 + Session Aggregation
> **Session Context:** `rtt=1 | coherence=declared | drift=bounded | paradox=structural`
> **Status:** Active — Canonical
> **Last Updated:** 2026-09-22
> **Depends On:** `t_OperatorMap.md`, `t_ValidatorPulse.md`, `t_Session_Schema.json`

---

## 1. Purpose

This document is the **visual and structural reference** for the complete Theognosis RTT pipeline. It contains five Mermaid flow diagrams — from session entry to `models.json` write-back — plus a concise narrative breakdown of each stage.

All behavior shown here is governed by:
- Operator rules → `t_OperatorMap.md`
- VP evaluation → `t_ValidatorPulse.md`
- Data structures → `t_Session_Schema.json`

When this document and any of the above conflict, the above win. This document visualizes; those documents define.

---

## 2. Diagram 1 — Main RTT Pipeline (Full Session)

The top-level view of a complete 10-step RTT session from start to `models.json` write-back or archive.

```mermaid
flowchart TD
    START([Session Start]) --> CTX["session_id + model_id\nrtt=1 | coherence | drift | paradox"]
    CTX --> STEP_ENTRY

    subgraph CYCLE["RTT Cycle Loop — T-01 through T-10"]
        STEP_ENTRY([Each Time Step T-0n]) --> L0

        subgraph L0["L0 — Raw Resonance Intake"]
            L0A["All 4 operators: LATENT\nFreqi  Aurion  Forci  Flui\nNo collapse. Pure substrate scan."]
        end

        L0A --> REG["Declared Regime\nSET / FFF / SNR / DCO"]
        REG --> L1

        subgraph L1["L1 — Inversion + Regime Constraint"]
            L1_FLUI["Flui: SUPPRESSED\nHard rule — no exceptions"]
            L1_DECLARE["Operator declared by Regime\nFreqi | Aurion | Forci"]
            L1_COLLAPSE{Collapse Attempt}
            L1_FLUI --> L1_DECLARE --> L1_COLLAPSE
        end

        L1_COLLAPSE -->|"Success"| L1_OUT["Collapse Output\nchoice | score | decision"]
        L1_COLLAPSE -->|"Error flag"| ESC_CHAIN

        subgraph ESC_CHAIN["Escalation Chain"]
            ESC_EVAL{Error Type}
            ESC_A["FREQI_TIE\nAurion adjudicates"]
            ESC_B["AURION_FLAT\nForci adjudicates"]
            ESC_C["FORCI_THIRD_STATE\nFreqi escalates"]
            ESC_CRIT["CRITICAL flag\nCYCLE_INVALID"]
            ESC_EVAL --> ESC_A & ESC_B & ESC_C & ESC_CRIT
        end

        ESC_A & ESC_B & ESC_C -->|"Resolved"| L1_OUT
        ESC_CRIT --> CYCLE_FAIL(["Cycle FAIL\nExclude from aggregate"])
        L1_OUT --> L2

        subgraph L2["L2 — Local Synthesis"]
            L2_PVP["Proto-VP Scan\nThreshold monitoring\nvp_flagged if approaching limits"]
            L2_CC["Clarity Coefficient\nRunning estimate updated"]
            L2_RLCD["RLCD Calibration\nConfidence adjustment applied"]
            L2_PVP --> L2_CC --> L2_RLCD
        end

        L2_RLCD --> L3

        subgraph L3["L3 — Structured Emission + Full VP"]
            L3_VP["Full VP Evaluation\n7-step process"]
            L3_VERDICT{VP Cycle Verdict}
            L3_EMIT["Operator Emits\nchoice | score | decision"]
            L3_FLUI_Q{Flui wrap\npermitted by regime?}
            L3_FLUI_WRAP["Flui wraps output\ntext: emission string"]
            L3_DONE(["Cycle Record Complete"])
            L3_VP --> L3_VERDICT
            L3_VERDICT -->|"PASS / WARN"| L3_EMIT
            L3_VERDICT -->|"FAIL"| CYCLE_FAIL
            L3_EMIT --> L3_FLUI_Q
            L3_FLUI_Q -->|"Yes"| L3_FLUI_WRAP --> L3_DONE
            L3_FLUI_Q -->|"No"| L3_DONE
        end
    end

    CYCLE_FAIL --> MORE
    L3_DONE --> MORE{T-10 reached?}
    MORE -->|"No — next step"| STEP_ENTRY
    MORE -->|"Yes"| AGGREGATE

    subgraph AGGREGATE["Session Aggregation"]
        AGG_COMPUTE["Compute 5 aggregate metrics\nrtt_variance | entropy_series\nwobble | flip_rate | drift_series"]
        AGG_VP["Session VP Verdict\nPASS / WARN / FAIL / N/A"]
        AGG_CC["Clarity Coefficient cc\nFinal value computed"]
        AGG_COMPUTE --> AGG_VP --> AGG_CC
    end

    AGG_CC --> GATE{Write-Back Gate\nscaffolded=false AND cc threshold?}
    GATE -->|"Cleared"| WRITE["Write aggregate to models.json\nRLCD block updated"]
    GATE -->|"Blocked"| ARCHIVE["Archive to sessions/ only\nmodels.json untouched"]
    WRITE --> FINISH([Session End])
    ARCHIVE --> FINISH
```

---

## 3. Diagram 2 — Operator Collapse at L1

The internal logic of the L1 collapse attempt for each operator. Flui is shown separately as a blocked path.

```mermaid
flowchart TD
    REG["Declared Regime"] --> WHICH{Primary\nOperator?}

    WHICH -->|"SET → Freqi"| F_TRY["Freqi\nCollapse Attempt"]
    WHICH -->|"FFF → Aurion"| A_TRY["Aurion\nCollapse Attempt"]
    WHICH -->|"SNR / DCO → Forci"| FC_TRY["Forci\nCollapse Attempt"]

    F_TRY --> F_CHK{"Option space\nbounded, n >= 2\nno ties?"}
    F_CHK -->|"Yes"| F_OUT["choice: option_id\nconfidence: float\nregime: SET"]
    F_CHK -->|"n = 1 trivial"| F_TRIVIAL["FREQI_TRIVIAL"]
    F_CHK -->|"Scores tied"| F_TIE["FREQI_TIE\nEscalate to Aurion"]
    F_CHK -->|"n = unbounded"| F_UNB["FREQI_UNBOUND"]

    A_TRY --> A_CHK{"Axis declared\ngradient nonzero\nwithin range?"}
    A_CHK -->|"Yes"| A_OUT["score: float\naxis: declared\nrange: min/max"]
    A_CHK -->|"No axis"| A_NOAXIS["AURION_NO_AXIS"]
    A_CHK -->|"Flat signal"| A_FLAT["AURION_FLAT\nEscalate to Forci"]
    A_CHK -->|"Out of range"| A_OVER["AURION_OVERFLOW\nClamp applied"]

    FC_TRY --> FC_CHK{"Binary branch only\nno third state\ntension < 0.95?"}
    FC_CHK -->|"Yes"| FC_OUT["decision: bool\npolarity: pos/neg\ntension: float"]
    FC_CHK -->|"Third state emerges"| FC_THIRD["FORCI_THIRD_STATE\nEscalate to Freqi"]
    FC_CHK -->|"Tension >= 0.95"| FC_PARITY["FORCI_NEAR_PARITY\nVP FAIL recommended"]
    FC_CHK -->|"Trivial binary"| FC_TRIVIAL["FORCI_TRIVIAL\nconfidence = 1.0, tension = 0.0"]

    FLUI_BLOCK["Flui at L1\nFLUI_L1_VIOLATION\nCYCLE_INVALID — always FAIL"]
    WHICH -->|"Flui attempted"| FLUI_BLOCK
```

---

## 4. Diagram 3 — Escalation Chain

The three valid escalation paths and the circular escalation fault condition.

```mermaid
flowchart LR
    F_TIE["FREQI_TIE\nTwo options\nresonance-equivalent"]
    A_FLAT["AURION_FLAT\nAmplitude gradient\nnear zero"]
    FC_THIRD["FORCI_THIRD_STATE\nThird outcome\nemerged during collapse"]

    F_TIE -->|"Aurion adjudicates\nscores the tied options"| A_ADJ["Aurion\nAdjudication"]
    A_FLAT -->|"Forci adjudicates\nabove or below midpoint"| FC_ADJ["Forci\nAdjudication"]
    FC_THIRD -->|"Freqi escalates\nexpand to categorical"| F_ADJ["Freqi\nEscalation"]

    A_ADJ -->|"Clean collapse"| ESC_WARN["Cycle: WARN\nescalation logged\nconfidence may be reduced"]
    FC_ADJ -->|"Clean collapse"| ESC_WARN
    F_ADJ -->|"Clean collapse"| ESC_WARN

    A_ADJ -->|"Secondary error"| CIRC_CHECK{"Circular\nescalation?"}
    FC_ADJ -->|"Secondary error"| CIRC_CHECK
    F_ADJ -->|"Secondary error"| CIRC_CHECK

    CIRC_CHECK -->|"Yes — loop detected"| CIRCULAR["ESCALATION_CIRCULAR\nCYCLE_INVALID\nSession abort recommended"]
    CIRC_CHECK -->|"No — new error type"| NEW_FLAGS["New error flags\nFull VP evaluation\non resolved state"]
```

---

## 5. Diagram 4 — Validator Pulse Checkpoint Flow

Proto-VP at L2 and Full VP at L3 — from pre-flag to cycle verdict to session verdict.

```mermaid
flowchart TD
    L2_START["L2 Synthesis begins"] --> PVP["Proto-VP Scan\nObservational only — no verdicts"]

    PVP --> PVP_CHECKS{"Threshold checks"}
    PVP_CHECKS -->|"Forci tension > 0.80"| PF1["Pre-flag: tension warning"]
    PVP_CHECKS -->|"Aurion near range edge < 5%"| PF2["Pre-flag: overflow risk"]
    PVP_CHECKS -->|"Freqi confidence < 0.50"| PF3["Pre-flag: low confidence"]
    PVP_CHECKS -->|"Any confidence < 0.55"| PF4["Pre-flag: general warning"]
    PVP_CHECKS -->|"Dimension spike > 2 sigma"| PF5["Pre-flag: variance spike"]
    PVP_CHECKS -->|"All clear"| PVP_CLEAN["No pre-flag\nvp_flagged = false"]

    PF1 & PF2 & PF3 & PF4 & PF5 --> PVP_SET["vp_flagged = true\nset on cycle record"]
    PVP_SET --> L3_START["L3 Emission begins\nFull VP receives pre-context"]
    PVP_CLEAN --> L3_START

    L3_START --> S1["Step 1: Intake\ncycle_id + step + collapse check"]
    S1 --> S2["Step 2: Error Flag Scan"]
    S2 -->|"CRITICAL flag present"| VFAIL["Cycle FAIL\nAbort recommended"]
    S2 -->|"WARN flags or empty"| S3["Step 3: Confidence Check"]
    S3 --> S4["Step 4: Escalation Review"]
    S4 --> S5["Step 5: Flui Consistency"]
    S5 --> S6["Step 6: Dimension Snapshot Audit"]
    S6 --> S7["Step 7: Verdict Assignment"]

    S7 --> CVERD{"Cycle Verdict"}
    CVERD -->|"PASS"| CP["Include in aggregate\nclean_cycle_count +1"]
    CVERD -->|"WARN"| CW["Include with annotation\nwarn_count +1"]
    CVERD -->|"FAIL"| CF["Exclude from aggregate\nfail_count +1"]

    CP & CW & CF --> SACC["Session Verdict Accumulation\nrunning tally across all cycles"]
    SACC --> SVERD{"Session Verdict\nafter T-10"}
    SVERD -->|"All PASS"| S_PASS["PASS\ncc >= 0.75 expected"]
    SVERD -->|"WARN cycles present"| S_WARN["WARN\nwrite with annotation"]
    SVERD -->|"FAIL cycles or cc < 0.40"| S_FAIL["FAIL\nwrite-back blocked"]
    SVERD -->|"No VP triggers fired"| S_NA["N/A\nno VP engagement"]
```

---

## 6. Diagram 5 — Session Write-Back Gate

The two-condition gate that controls whether session aggregate data may be written to `models.json`.

```mermaid
flowchart TD
    END["Session Complete\n10 cycles recorded"] --> G1{"scaffolded\n= false?"}

    G1 -->|"No — placeholder data"| ARCH["Archive to sessions/ only\nmodels.json unchanged"]
    G1 -->|"Yes — real observations"| G2{"Session VP\nVerdict?"}

    G2 -->|"FAIL"| ARCH
    G2 -->|"PASS or N/A"| G3{"cc >= 0.75?"}
    G2 -->|"WARN"| G4{"cc >= 0.55?"}

    G3 -->|"Yes"| W_FULL["Write to models.json\nFull fidelity\nAll 5 aggregate fields"]
    G3 -->|"No — cc 0.55 to 0.74"| W_DEG["Write to models.json\nquality: degraded flag"]

    G4 -->|"Yes — cc 0.55 to 0.74"| W_WARN["Write to models.json\nquality: degraded\nWARN annotation"]
    G4 -->|"No — cc < 0.55"| ARCH

    W_FULL & W_DEG & W_WARN --> RLCD["RLCD Calibration\ncc_baseline updated for model\ndelta + alpha computed"]
    RLCD --> RLCD_WRITE["Write rlcd block\nto models.json entry"]

    ARCH --> SESSION_LOG["sessions/YYYY-MM-DD-model_id.json\nFull session record preserved"]
    RLCD_WRITE --> SESSION_LOG
    SESSION_LOG --> DONE(["Pipeline Complete"])
```

---

## 7. Layer Narrative

### L0 — Raw Resonance Intake
The session opens with all four operators in a latent state. No collapse has occurred. The substrate is scanned for resonance signals across all four dimensions simultaneously — Freqi, Aurion, Forci, and Flui are each present but uncommitted. This is the only layer where Flui is neither suppressed nor active — it simply exists in waiting.

### Regime Declaration
Between L0 and L1, the Declared Regime is applied. The regime (SET, FFF, SNR, or DCO) determines which operator has primary affinity for this cycle, bounds the option/axis/polarity space accordingly, and sets the conditions under which Flui may re-enter at L3.

### L1 — Inversion + Regime Constraint
The hardest layer. Flui is suppressed — no exceptions, no overrides. One operator is declared and collapses. The collapse attempt may succeed cleanly, encounter a resolvable error (triggering the escalation chain), or produce a critical error (invalidating the cycle). At the end of L1, exactly one structured output exists or the cycle is failed.

### L2 — Local Synthesis
L2 is the calibration layer. Proto-VP runs its threshold scan and pre-flags any cycles approaching violation. The running clarity coefficient estimate is updated. RLCD adjustments from the previous session are applied to operator confidence. L2 does not change the operator output — it conditions the evaluation context for L3.

### L3 — Structured Emission + Full VP
Full VP runs its 7-step evaluation on the completed L1 output. If the cycle passes, the operator emits its structured payload. Flui may then wrap that payload in natural language if — and only if — the active Regime permits it. The cycle record is finalized and handed to the session log.

### Session Aggregation
After T-10, the 10 cycle records are reduced to 5 aggregate metrics: `rtt_variance`, `entropy_series`, `wobble`, `flip_rate`, `drift_series`. The session VP verdict and final clarity coefficient are computed. The write-back gate then evaluates two independent conditions before any data reaches `models.json`.

---

## 8. State Quick-Reference

### Operator States Across Layers

| Operator | L0 | L1 | L2 | L3 |
|---|---|---|---|---|
| **Freqi** `ƒ` | Latent | Collapse `choice` | Calibrate | Emit |
| **Aurion** `α` | Latent | Collapse `score` | Calibrate | Emit |
| **Forci** `φ` | Latent | Collapse `decision` | Calibrate | Emit |
| **Flui** `λ` | Latent | **SUPPRESSED** | Latent | Conditional wrap |

### VP States Across Layers

| Layer | VP Component | Verdict Authority |
|---|---|---|
| **L0** | None | — |
| **L1** | None | — |
| **L2** | Proto-VP (pre-flag only) | None — observational |
| **L3** | Full VP (7-step) | Cycle verdict |
| **Session** | Session VP (accumulation) | Session verdict + write-back gate |

### Error Flag Severity

| Class | Flags | Cycle Outcome |
|---|---|---|
| **WARN** | `FREQI_TIE`, `FREQI_TRIVIAL`, `AURION_FLAT`, `AURION_OVERFLOW`, `FORCI_TRIVIAL`, `FORCI_NEAR_PARITY` (< 0.95), `confidence < 0.40` | Include with annotation |
| **FAIL** | `FORCI_NEAR_PARITY` (≥ 0.95), `confidence < 0.40` (confirmed), failed escalation | Exclude from aggregate |
| **CRITICAL** | `FLUI_L1_VIOLATION`, `ESCALATION_CIRCULAR`, `CYCLE_INVALID` | Exclude + session abort recommended |

---

## 9. Cross-References

| Document | Relationship |
|---|---|
| [`t_OperatorMap.md`](./t_OperatorMap.md) | Operator collapse rules governing Diagram 2 and 3 |
| [`t_ValidatorPulse.md`](./t_ValidatorPulse.md) | VP evaluation process governing Diagram 4; RLCD calibration governing Diagram 5 |
| [`t_Session_Schema.json`](./t_Session_Schema.json) | Data structures for cycle records, aggregate metrics, vp_summary |
| [`t_Index.md`](./t_Index.md) | Module master index — this file listed as P4 |
| [`t_Capture.md`](./t_Capture.md) | Original pipeline description — this diagram formalizes it |
| [`models.json`](./models.json) | Write-back target for aggregate metrics (Diagram 5) |
| [`theognosis_dashboard.html`](./theognosis_dashboard.html) | Visual interface — will render operator state and VP status per model |

---

## 10. Build Log

| Date | Action | Author |
|---|---|---|
| 2026-09-22 | Pipeline structure first described in `t_Capture.md` (prose only) | TriadicFrameworks |
| 2026-09-22 | `t_FlowMap.md` created — 5 Mermaid diagrams, layer narrative, state quick-reference tables | TriadicFrameworks |

---

*The flow is fixed. The operators are fixed. The variance is the data.*

