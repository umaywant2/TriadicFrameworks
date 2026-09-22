# Theognosis — Validator Pulse

> **Document Class:** P3
> **RTT Layer:** L2 (Proto-VP) + L3 (Full VP) + Session (Aggregate VP)
> **Session Context:** `rtt=1 | coherence=declared | drift=bounded | paradox=structural`
> **Status:** Active — Canonical
> **Last Updated:** 2026-09-22
> **Depends On:** `t_OperatorMap.md` (trigger definitions), `t_Session_Schema.json` (vp_summary structure)

---

## 1. Purpose

The Validator Pulse (VP) is the **integrity verification mechanism** of the Theognosis RTT pipeline. It operates at two levels — a lightweight proto-VP scan at L2 and a full evaluation pass at L3 — and produces a session-level verdict that determines whether aggregate metrics from a session may be written to `models.json`.

The VP does not correct operator outputs. It does not alter collapse results. It **observes, flags, rates, and decides** — then hands verdict authority to the research operator (you).

Three outputs define every VP engagement:
1. **Cycle flags** — individual cycle anomalies detected during evaluation
2. **Session verdict** — PASS / WARN / FAIL / PENDING / N/A for the whole session
3. **Clarity coefficient** — session-level quality signal used by RLCD calibration

---

## 2. Two-Level Architecture

### 2.1 Proto-VP (L2 — Early Warning)

Proto-VP runs during L2 synthesis, before the operator emits at L3. It does not issue verdicts — it monitors for approaching threshold violations and marks cycles preemptively for review.

Proto-VP is **observational only**. It cannot halt a cycle. It cannot modify operator output. Its sole function is to set `vp_flagged = true` on a cycle record before L3 fires, so the full VP has pre-context when it evaluates.

**Proto-VP watches for:**
- Forci tension value crossing 0.80 (pre-threshold for `FORCI_NEAR_PARITY`)
- Aurion score approaching declared range boundaries (within 5% of min or max)
- Freqi confidence below 0.50 (pre-threshold for low-confidence flag)
- Any operator confidence below 0.55 (general early warning)
- Cross-dimension variance spike: any single dimension_snapshot value deviating > 2σ from its session mean up to this step

Proto-VP marks the cycle: `vp_flagged = true`. Full VP at L3 then decides whether the flag is a PASS, WARN, or FAIL.

### 2.2 Full VP (L3 — Evaluation Pass)

Full VP runs after operator collapse is complete, once L3 output is available. It evaluates the completed cycle against all trigger conditions, assigns a cycle-level severity, and contributes to the session-level verdict accumulation.

Full VP **can recommend session abort** (FAIL verdict) but cannot execute it unilaterally — the research operator makes the final call.

---

## 3. Trigger Table

All triggers defined in `t_OperatorMap.md §7.4`. Reproduced here with severity classification and VP response.

| Trigger Flag | Source | Severity | Proto-VP | Full VP Response |
|---|---|---|---|---|
| `FREQI_TIE` | Freqi | ⚠️ WARN | Pre-flag if option scores converging | Evaluate escalation outcome; if Aurion adjudicated cleanly → WARN; if no resolution → FAIL |
| `AURION_FLAT` | Aurion | ⚠️ WARN | Pre-flag if amplitude gradient < 0.05 | Check if Forci adjudicated; if yes → WARN; if flat with no escalation → FAIL |
| `AURION_OVERFLOW` | Aurion | ⚠️ WARN | Pre-flag if score approaching range edge | Verify clamp applied correctly; score within range post-clamp → WARN; clamp failed → FAIL |
| `FORCI_NEAR_PARITY` | Forci | ⚠️ WARN | Pre-flag at tension > 0.80 | If tension 0.80–0.94 → WARN; if tension ≥ 0.95 → FAIL pending review |
| `FLUI_L1_VIOLATION` | Flui | 🔴 CRITICAL | Not applicable (L1 event) | Always FAIL. Cycle invalidated. Session abort recommended. |
| `confidence < 0.4` | Any | ⚠️ WARN | Pre-flag at confidence < 0.55 | confidence 0.40–0.54 → WARN; confidence < 0.40 → FAIL |
| `ESCALATION_CIRCULAR` | Any | 🔴 CRITICAL | Not applicable | Always FAIL. Session abort recommended. |
| `CYCLE_INVALID` | Any | 🔴 CRITICAL | Not applicable | Always FAIL. Session abort recommended. |

### 3.1 Severity Definitions

| Severity | Symbol | Meaning |
|---|---|---|
| **PASS** | ✅ | Cycle completed cleanly with no flags or with flags resolved by successful escalation |
| **WARN** | ⚠️ | Anomaly detected but cycle output is usable. Aggregate metrics may include this cycle with warning annotation. |
| **FAIL** | 🔴 | Cycle output is unreliable or invalid. Cycle should be excluded from aggregate computation. Session abort should be considered. |
| **CRITICAL** | 💀 | Structural violation of RTT pipeline rules. Session abort is recommended. Research operator must review before continuing. |

---

## 4. VP Evaluation Process — Cycle Level

For each cycle in a session, Full VP executes the following steps in order:

### Step 1 — Intake
Receive the completed cycle record from L3. Confirm:
- `cycle_id` is present and unique
- `step` matches expected sequence position
- `operator_collapsed` is not null (if null, skip to Step 5 with FAIL)

### Step 2 — Error Flag Scan
Evaluate `error_flags` array:
- Empty array → proceed to Step 3 with provisional PASS
- Contains WARN-class flags → proceed with provisional WARN
- Contains CRITICAL-class flags (`FLUI_L1_VIOLATION`, `ESCALATION_CIRCULAR`, `CYCLE_INVALID`) → assign FAIL immediately, skip remaining steps, recommend session abort

### Step 3 — Confidence Check
Evaluate `output.confidence` (or `output.tension` for Forci):
```
confidence ≥ 0.70  → no confidence flag, keep current provisional verdict
confidence 0.55–0.69 → note degraded confidence, keep provisional verdict
confidence 0.40–0.54 → add WARN if not already WARN/FAIL
confidence < 0.40   → escalate to FAIL
tension ≥ 0.95 (Forci) → escalate to FAIL, flag FORCI_NEAR_PARITY
```

### Step 4 — Escalation Review
If `escalation` is not null:
- Verify `to_operator` successfully collapsed (operator_collapsed matches to_operator)
- Verify no circular escalation (`ESCALATION_CIRCULAR` not in flags)
- Clean escalation with successful outcome → add WARN (escalation is always noteworthy even when resolved)
- Failed escalation or circular escalation → FAIL

### Step 5 — Flui Consistency Check
If `flui_wrapped = true`:
- Confirm `flui_emission` is not null and not empty
- Confirm prior collapse exists (operator_collapsed is not null)
- Confirm `FLUI_L1_VIOLATION` not in error_flags
- If any condition fails → WARN on emission, but do not downgrade the underlying operator verdict

### Step 6 — Dimension Snapshot Audit
If `dimension_snapshot` is present:
- Flag any dimension value = 0.0 exactly (possible missing reading rather than true zero)
- Flag if all four dimensions are identical (possible instrument error)
- Cross-check Flui snapshot value against known Flui suppression at L1 — value should still be recorded (L1 suppression ≠ null reading)

### Step 7 — Cycle Verdict Assignment
Assign final cycle verdict based on accumulated signals:
```
No flags, no warnings, confidence ≥ 0.70  → PASS
Any WARN-class condition, no FAIL/CRITICAL  → WARN
Any FAIL/CRITICAL condition                 → FAIL
```

Record verdict in `vp_summary.flagged_cycles` if WARN or FAIL.

---

## 5. VP Evaluation Process — Session Level

After all 10 cycle verdicts are assigned, the session-level VP verdict is computed.

### 5.1 Session Verdict Rules

```
All 10 cycles PASS                          → Session PASS
1–2 cycles WARN, 0 FAIL                     → Session WARN
3+ cycles WARN, 0 FAIL                      → Session WARN (elevated)
Any 1 cycle FAIL (non-CRITICAL)             → Session WARN (with exclusion)
2+ cycles FAIL or any CRITICAL              → Session FAIL
Session FAIL + FLUI_L1_VIOLATION present    → Session FAIL + abort recommended
Evaluation not yet complete                  → Session PENDING
No VP triggers fired at any cycle           → Session N/A
```

### 5.2 Exclusion Protocol

When one or more cycles are FAIL:
- Exclude failed cycles from aggregate metric computation
- Recompute aggregate over remaining valid cycles
- Record `excluded_cycles` count in vp_summary (extend schema as needed)
- Flag `scaffolded = true` on aggregate if > 2 cycles excluded (partial session — not suitable for models.json write-back)

### 5.3 Abort Recommendation

VP issues an abort recommendation when:
- Any `FLUI_L1_VIOLATION` is detected in any cycle
- Any `ESCALATION_CIRCULAR` is detected
- 3 or more cycles score FAIL in a single session
- Session clarity_coefficient falls below 0.40

An abort recommendation does not stop the session automatically. It sets `vp_verdict = "FAIL"` and populates `vp_notes` with the reason. The research operator decides whether to continue, restart, or discard the session.

---

## 6. Clarity Coefficient

The clarity coefficient (`cc`) is a single scalar [0.0–1.0] summarizing the quality of an RTT session. It feeds RLCD calibration and is used as a trust weight when writing aggregate metrics back to `models.json`.

### 6.1 Formula

```
cc = (clean_cycle_count / total_cycles) × mean_confidence × (1 - vp_penalty)

Where:
  clean_cycle_count  = cycles with no error_flags AND vp_flagged = false
  total_cycles       = 10 (standard session)
  mean_confidence    = arithmetic mean of output.confidence across all non-null cycles
  vp_penalty         = (FAIL_count × 0.10) + (WARN_count × 0.03)
                       clamped to [0.0, 0.50]
```

### 6.2 Interpretation

| cc Range | Interpretation | models.json Write-Back |
|---|---|---|
| 0.90 – 1.00 | Excellent — high-fidelity session | ✅ Write directly |
| 0.75 – 0.89 | Good — minor anomalies, reliable data | ✅ Write with annotation |
| 0.55 – 0.74 | Acceptable — notable variance, use with caution | ⚠️ Write with `quality: "degraded"` flag |
| 0.40 – 0.54 | Degraded — session data is unreliable | ⚠️ Write only to `sessions/` archive, not to `models.json` |
| 0.00 – 0.39 | Failed — session should be discarded | 🔴 Do not write. Session abort recommended. |

### 6.3 Running cc

Proto-VP tracks a running clarity estimate at each L2 step using cycles completed so far. This running estimate is informational — it does not affect in-progress cycle evaluation. It is recorded in session notes if the session is aborted mid-run.

---

## 7. RLCD Calibration

RLCD (Resonance Loop Clarity Drift) calibration uses the session `clarity_coefficient` to adjust operator output confidence scores for the **next** session on the same model.

RLCD operates between sessions, not within them.

### 7.1 RLCD Adjustment Formula

```
adjusted_confidence(next) = raw_confidence × (1 + δ_RLCD)

Where:
  δ_RLCD = (cc_current - cc_baseline) × α_RLCD

  cc_baseline = rolling mean of last 3 session cc values for this model
                (or 0.75 if fewer than 3 sessions exist)
  α_RLCD     = 0.15 (sensitivity factor — fixed for RTT v1)
```

### 7.2 RLCD Bounds

RLCD adjustment is bounded to prevent runaway drift:
```
δ_RLCD clamped to [-0.20, +0.20]
adjusted_confidence clamped to [0.0, 1.0]
```

### 7.3 RLCD Per Model

Each model in `models.json` maintains its own RLCD baseline. Models with `drift_class: "turbulent"` receive a dampened α_RLCD of 0.08 — high-drift models should not be over-corrected by a single good session.

| Drift Class | α_RLCD | Rationale |
|---|---|---|
| bounded | 0.15 | Standard sensitivity |
| suppressed | 0.10 | Conservative — already low drift |
| turbulent | 0.08 | Dampened — prevent over-correction |

### 7.4 RLCD Write-Back Target

After calibration, write RLCD values to `models.json` under a new field:

```json
{
  "id": "model-slug",
  "rlcd": {
    "cc_baseline": 0.78,
    "last_session_cc": 0.87,
    "delta": 0.013,
    "alpha": 0.15,
    "sessions_sampled": 3,
    "last_calibrated": "2026-09-22T03:14:00-04:00"
  }
}
```

---

## 8. VP States Reference

### 8.1 Cycle-Level VP States

```
PASS    — No flags, confidence acceptable, escalation clean (if any)
WARN    — Anomaly present but output usable
FAIL    — Output invalid or unreliable; exclude from aggregate
PENDING — Evaluation in progress (proto-VP phase, full VP not yet run)
```

### 8.2 Session-Level VP Verdicts

```
PASS    — All cycles PASS; cc ≥ 0.75; write-back permitted
WARN    — Mix of PASS/WARN cycles; write-back with annotation
FAIL    — FAIL cycles present or cc < 0.40; write-back blocked to models.json
PENDING — Session not yet complete
N/A     — No VP triggers fired; session passed without VP engagement
```

### 8.3 VP Severity Ladder

```
N/A → PASS → WARN → FAIL → CRITICAL (abort)
```

Severity only moves up during a session — a cycle cannot be downgraded from FAIL to WARN once assigned.

---

## 9. Edge Cases

### 9.1 All Cycles Clean
If all 10 cycles complete with empty `error_flags`, `vp_flagged = false`, and `confidence ≥ 0.70`, VP returns `N/A` (no engagement) and clarity_coefficient computes naturally without VP penalty. Session is ideal.

### 9.2 Partial Session
If a session is aborted before all 10 cycles complete:
- VP computes verdict over completed cycles only
- `cycle_count` in aggregate reflects actual completions
- `scaffolded` is set `true` regardless of individual cycle quality
- Session is archived to `sessions/` but not written to `models.json`

### 9.3 First Session for a Model (No RLCD Baseline)
Use `cc_baseline = 0.75` as the default. This is deliberately conservative — new models start with a neutral calibration assumption. After 3 sessions, RLCD switches to rolling mean.

### 9.4 FLUI_L1_VIOLATION in Any Cycle
This is a structural pipeline violation. VP immediately:
1. Assigns FAIL to the offending cycle
2. Marks session as FAIL
3. Appends abort recommendation to `vp_notes`
4. Flags the session for manual review before re-run
5. Does not compute RLCD calibration for this session — corrupted cc would poison the baseline

---

## 10. Proto-VP vs. Full VP Quick Reference

| Dimension | Proto-VP (L2) | Full VP (L3) |
|---|---|---|
| **When** | During L2 synthesis, before L3 emit | After L3 emit, using completed output |
| **Verdict authority** | None — marks only | Full verdict authority |
| **Can halt cycle** | No | No (recommends only) |
| **Can abort session** | No | Recommends to research operator |
| **Output** | `vp_flagged = true` on cycle record | Cycle verdict + session verdict + cc |
| **Triggers watched** | Approaching thresholds (pre-fire) | Fired thresholds (post-fire) |
| **Speed** | Fast — threshold scan only | Full evaluation — all 7 steps |

---

## 11. Cross-References

| Document | Relationship |
|---|---|
| [`t_OperatorMap.md §7.4`](./t_OperatorMap.md) | Defines all VP trigger flags used in §3 above |
| [`t_Session_Schema.json`](./t_Session_Schema.json) | `vp_summary` object and `clarity_coefficient` field both defined there; VP populates them |
| [`t_Index.md`](./t_Index.md) | Module master index — this file listed as P3 |
| [`t_Capture.md`](./t_Capture.md) | Proto-VP behavior first described here; this document formalizes and supersedes that description |
| [`t_FlowMap.md`](./t_FlowMap.md) | VP sits at L2 and L3 in the flow diagram — visual representation there |
| [`models.json`](./models.json) | VP governs write-back to this file via scaffolded flag + cc threshold |
| [`../spine/models_resonance_variance_dashboard.html`](../spine/models_resonance_variance_dashboard.html) | Visualizes aggregate metrics that VP gates — VP verdict quality directly affects dashboard fidelity |

---

## 12. Build Log

| Date | Action | Author |
|---|---|---|
| 2026-09-22 | Proto-VP behavior captured in `t_Capture.md` (informal, no verdicts defined) | TriadicFrameworks |
| 2026-09-22 | `t_ValidatorPulse.md` created — full VP specification: trigger table, 7-step cycle evaluation, session verdict rules, clarity coefficient formula, RLCD calibration, edge cases | TriadicFrameworks |

---

*The Validator Pulse does not judge the resonance. It judges whether the resonance was read cleanly.*

