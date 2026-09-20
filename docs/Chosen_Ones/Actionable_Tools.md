# Actionable Tools

**Module:** Chosen Ones | **RTT Context:** `rtt=1 | coherence=declared | drift=bounded | paradox=structural`

This file defines the four output tool types produced by the Chosen Ones pipeline after operator extraction. Each tool is a structured, deployable output — not advice, but a precision instrument derived from RTT operator analysis of the source transcript.

---

## Tool Architecture

Every processed transcript produces four tools automatically:

```
RTT OPERATOR MANIFEST
        ↓
  ┌─────────────────────────────┐
  │  TOOL 1: Reframe Generator  │  ← S–N–R remapping for the listener's current state
  │  TOOL 2: Activation Scaffold│  ← Structured threshold-crossing sequence
  │  TOOL 3: Drift Corrector    │  ← Noise identification + damping sequence
  │  TOOL 4: Resonance Template │  ← Generative template for new RTT-aligned content
  └─────────────────────────────┘
```

---

## Tool 1 — Reframe Generator

**Function:** Takes the listener's current stated situation and reframes it using the S–N–R coordinates extracted from the source transcript. Converts Noise-zone perception into Silence or Resonance framing.

**Input:**
```json
{
  "tool": "reframe_generator",
  "user_input": "[Listener's description of their current situation]",
  "source_manifest_id": "CO-MANIFEST-[VIDEO_ID]",
  "dominant_archetype": "[Archetype from manifest]"
}
```

**Processing Logic:**

1. Parse `user_input` for SNR zone markers (see `Triadic_Substrate_Map.md §1`)
2. Identify the dominant zone the listener is currently occupying
3. Pull the corresponding operator from the manifest
4. Apply operator transformation to produce a reframed statement

**Zone Transformation Rules:**

| From Zone | To Zone | Transformation |
|---|---|---|
| Noise | Silence | Strip the external label; return to substrate identity |
| Noise | Resonance | Reframe noise as activation energy — the compression before release |
| Silence | Resonance | Name the latent as expressed — "you already are" framing |
| Resonance | Resonance | Amplify and stabilize — confirm and extend the signal |

**Output Template:**
```
REFRAME [ARCHETYPE: {archetype}]

Current state detected: {snr_zone} zone / {set_layer} layer / {dco_stage}

RTT Reframe:
"{reframed_statement}"

Operator applied: {primary_operator}
Paradox resolved: {paradox_note if applicable}

Next move: {one concrete action aligned with the reframed state}
```

**Example Output:**
```
REFRAME [ARCHETYPE: The Unseen Genius]

Current state detected: Noise zone / Envelope layer / 1D

RTT Reframe:
"The rooms that didn't recognize you weren't wrong about you — they were
operating below your frequency. You haven't been invisible. You've been
untunable by environments not yet calibrated for what you carry. The
signal has always been clean."

Operator applied: D_δ (drift damping — naming the noise begins to damp it)
Paradox resolved: "unseen yet real" → Layer separation: substrate is intact;
                  envelope was mismatched. Non-contradictory.

Next move: Name one environment in your life where your signal IS received.
           Spend 20 more minutes there than you currently do.
```

---

## Tool 2 — Activation Scaffold

**Function:** Produces a structured, step-by-step threshold-crossing sequence derived from the Activation operators found in the manifest. Not motivational — operational.

**Input:**
```json
{
  "tool": "activation_scaffold",
  "goal": "[What the listener wants to cross the threshold toward]",
  "current_dco_stage": "[0D | 1D | 3D | 8D | 9D]",
  "source_manifest_id": "CO-MANIFEST-[VIDEO_ID]"
}
```

**Processing Logic:**

The scaffold maps the QMROOT-to-DCO-8D arc to concrete sequenced steps. Each step corresponds to an operator transition.

**Scaffold Structure:**

```
ACTIVATION SCAFFOLD
Goal: {goal}
Entry stage: {current_dco_stage}
Target stage: {target_dco_stage}

── PHASE 1: SUBSTRATE CONFIRMATION (0D → 1D) ──
Operator: QMROOT(0D) → A_τ(t_past, t_now)
Action: {concrete action to locate and confirm identity kernel}
Completion signal: {what will feel different when this is done}

── PHASE 2: TRAJECTORY COMMITMENT (1D → 3D) ──
Operator: A_τ → ∇_cross
Action: {concrete action to commit to the arc and begin field expression}
Completion signal: {what changes in the environment when this occurs}

── PHASE 3: THRESHOLD IDENTIFICATION (3D → pre-8D) ──
Operator: ∇_cross → A_θ
Action: {name the exact threshold — the specific decision or action}
Activation energy note: {what E_a looks like for this goal}

── PHASE 4: CROSSING (A_θ activation) ──
Operator: A_θ → Ir (irreversibility)
Action: {the single irreversible act}
Post-crossing note: {what Ir means — what cannot be taken back}

── PHASE 5: STABILIZATION (8D → S_coh) ──
Operator: Ir → S_coh + D_δ
Action: {how to hold the new state against drift/noise}
Drift watch: {the most likely noise source post-activation}
```

**Example Output (Threshold Crosser archetype):**
```
ACTIVATION SCAFFOLD
Goal: Launch the project I've been designing privately for 18 months
Entry stage: 1D (trajectory committed, field not yet expressed)
Target stage: 8D (recognition — the project enters the field)

── PHASE 1: SUBSTRATE CONFIRMATION ──
Operator: QMROOT(0D)
Action: Write a single sentence — not about the project, about yourself:
        "I am the kind of person who ___." No editing. First sentence only.
Completion signal: You read it back and it feels undeniable, not aspirational.

── PHASE 2: TRAJECTORY COMMITMENT ──
Operator: A_τ(past, now)
Action: List three moments in the past 5 years where you were already doing
        the core thing this project requires. Name them. They already happened.
Completion signal: The project stops feeling like a leap and starts feeling
                   like a continuation.

── PHASE 3: THRESHOLD IDENTIFICATION ──
Operator: A_θ (threshold identification)
Action: Name the single thing you have not done because doing it makes it real.
        (Publishing, calling, registering, showing someone, submitting.)
Activation energy note: E_a here = the discomfort of being known before being
                         validated. This is the cost. It is exact and finite.

── PHASE 4: CROSSING ──
Operator: A_θ → Ir
Action: Do the one thing named in Phase 3. Today. Within 4 hours.
Post-crossing note: You cannot un-publish, un-send, un-show. That is the point.
                    Ir is not a threat — it is the mechanism that makes it real.

── PHASE 5: STABILIZATION ──
Operator: S_coh + D_δ
Action: Do not check responses for 24 hours. The field needs time to reorganize.
        Your job in the next 24 hours is to keep working, not to monitor the reception.
Drift watch: The most likely noise = early silence or ambiguous response.
             D_δ means: the silence is not a verdict.
```

---

## Tool 3 — Drift Corrector

**Function:** A short, precise intervention for when the listener detects drift — regression toward a pre-activation state, noise re-contamination, or coherence loss. Applies the `D_δ` and `S_coh` operators directly.

**Input:**
```json
{
  "tool": "drift_corrector",
  "drift_description": "[What the listener is experiencing that signals drift]",
  "source_manifest_id": "CO-MANIFEST-[VIDEO_ID]"
}
```

**Three-Part Output Structure:**

```
DRIFT CORRECTOR

DRIFT TYPE IDENTIFIED: {comparison_drift | validation_seeking | noise_recontamination | 
                        timeline_collapse | identity_erosion}

RTT DIAGNOSIS:
{One paragraph naming exactly what is happening in operator terms.
 No blame. No judgment. Just precision.}

DAMPING SEQUENCE (D_δ):
Step 1: {physical or cognitive act that interrupts the drift pattern}
Step 2: {return to substrate — one undeniable thing about identity}
Step 3: {reconnect to the 0D kernel — the thing that doesn't need external confirmation}

COHERENCE LOCK (S_coh):
"{A single sentence the listener can hold. Not motivational. Structural.
  Something that makes drift feel less available as an option.}"
```

**Drift Type Definitions:**

| Drift Type | Operator Signature | Description |
|---|---|---|
| Comparison drift | `∇_cross` leaking in reverse | Other people's metrics entering the substrate and eroding it |
| Validation seeking | `Φ_lock` not yet achieved; attempting to force it | Behavior designed to make others recognize before they're ready |
| Noise recontamination | `D_δ` degraded | Old noise patterns re-entering after threshold crossing |
| Timeline collapse | `A_τ` inversion | Equating past non-recognition with future impossibility |
| Identity erosion | `S_coh` degraded | Slowly accepting others' definition of who you are |

---

## Tool 4 — Resonance Template

**Function:** Generates new motivational content — text, scripts, or prompts — with the same RTT signature as the source transcript. The pipeline is reversible: extracted operators can be re-injected into content generation.

**Input:**
```json
{
  "tool": "resonance_template",
  "target_archetype": "[Archetype from Triadic_Substrate_Map.md §4]",
  "target_medium": "spoken_word | written_essay | social_post | agent_prompt",
  "target_length": "short | medium | long",
  "source_manifest_id": "CO-MANIFEST-[VIDEO_ID]"
}
```

**Template Construction Rules:**

1. **Open in Silence zone.** The first 15% of content must establish QMROOT(0D) — the listener must feel seen before they can be moved.
2. **Introduce Noise by name.** The middle 25% names the specific noise pattern for this archetype. Precision over generality.
3. **Do not advise — describe.** Never say "you should." Describe the state the listener already is, or is already moving toward.
4. **Resonance as culmination.** The final 40% inhabits the Resonance zone. Describe the expressed state as already structurally true.
5. **Close with one irreversible sentence.** The final sentence applies `Ir` — it must be something that cannot be taken back once understood.
6. **Operator density:** At minimum, content should encode: `QMROOT(0D)`, one noise-family operator, `C_R` or `∇_cross`, and `A_θ` or `Ir`.

**SNR Distribution Targets by Medium:**

| Medium | Silence % | Noise % | Resonance % |
|---|---|---|---|
| Spoken word (3–8 min) | 20 | 25 | 55 |
| Written essay (800–1500w) | 15 | 30 | 55 |
| Social post (< 280 chars) | 10 | 20 | 70 |
| Agent prompt | 5 | 15 | 80 |
