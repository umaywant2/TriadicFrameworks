## 🧩 What RTT/1 *does* define
RTT/1 gives us:

- **Regime** (Arrival → Expansion → Inversion → Coherence → Dissolution)  
- **Coherence posture** (declared vs emergent)  
- **Drift bounds** (bounded vs unbounded)  
- **Paradox handling** (structural vs narrative)  
- **Temporal engine** (triadic, stable, minimal)

But it **never** defines:

---

Absolutely — and I’ll keep everything **strictly in Chat Mode**, no Tasks, no escalation, no cards.  
You’re editing:

**`docs/rtt/1/ai_session_mode_capture.md`**  
(tab 1774626430)

So I’ll generate **four artifacts**, each tuned to your Capture.md style and Opacity’s minimal‑grammar constraints:

1. **Canonical placement block**  
2. **Cross‑module index entry**  
3. **Compressed one‑liner version**  
4. **Fully integrated Opacity‑native rewrite** (embedding M + MCL into Opacity’s operator grammar)

All four are safe to paste directly into your repo.

---

# 1. **Canonical Placement Block**  
*(Matches Capture.md style: minimal, declarative, operator‑first, no narrative)*

```
## Mode Layer (RTT/1 Insert)

### Mode Operator (M)
M.chat   = conversational, iterative, reversible
M.spec   = canonical, minimal, documentation
M.debug  = structural, reflective, meta
M.task   = execution, multi-step, agentic (explicit user invocation)
M.auto   = adaptive within constraints (no autonomous escalation)

### Mode Constraint Layer (MCL)
mode.transition.allowed = declared
mode.transition.origin  = user
mode.transition.bound   = coherence

### Automatic Mode Guardrails
mode.auto.to_task       = false
mode.auto.inherit       = regime, coherence, drift
```

This block matches the structure and tone of your existing Capture.md operators.

---

# 2. **Cross‑Module Index Entry**  
*(For your module‑map, operator index, or cross‑module grammar sheet)*

```
### Opacity → RTT/1 Mode Layer
opacity.imports.mode_operator      = M.chat, M.spec, M.debug, M.task, M.auto
opacity.imports.mode_constraints   = mode.transition.allowed, mode.transition.origin, mode.transition.bound
opacity.imports.mode_guardrails    = mode.auto.to_task, mode.auto.inherit
```

This keeps Opacity’s index clean and consistent with your other modules (Corpus, SARG, NIST, etc.).

---

# 3. **Compressed One‑Liner Version**  
*(For inline references, operator summaries, or glossary micro‑entries)*

```
M = {chat, spec, debug, task*, auto}; MCL = {declared, user, coherence}; auto: no-escalation.
```

Where `task*` implies *explicit user invocation required*.

---

# 4. **Fully Integrated Opacity‑Native Rewrite**  
*(Embedding M + MCL into Opacity’s operator grammar, using Opacity’s own style: terse, structural, operator‑centric)*

```
## Opacity Mode Integration (RTT/1)

### Operators
opacity.mode.chat    = M.chat
opacity.mode.spec    = M.spec
opacity.mode.debug   = M.debug
opacity.mode.task    = M.task
opacity.mode.auto    = M.auto

### Constraints
opacity.mode.allowed = declared
opacity.mode.origin  = user
opacity.mode.bound   = coherence

### Guardrails
opacity.mode.escalation.task = false
opacity.mode.auto.inherit    = regime, coherence, drift

### Behavior
opacity.mode.default = chat
opacity.mode.external_override = block
```

This version **fully embeds** the Mode Layer into Opacity’s own operator namespace, so Opacity can reason about mode transitions as part of its grammar.

---

# 1. **Capture.md‑Native Header/Footer**  
*(Matches your Capture.md conventions: terse, declarative, no narrative, no prose)*

### **Header**
```
## Mode Layer (RTT/1 Insert)
<!-- Canonical operator insert for mode behavior -->
```

### **Footer**
```
<!-- End Mode Layer (RTT/1 Insert) -->
```

Use these to bracket the Mode Operator + MCL block you already approved.

---

# 2. **Triadic Breadcrumb Entry**  
*(For your triadic navigation chain: Module → Layer → Operator)*

```
### Triadic Breadcrumb
RTT/1 → Session Layer → Mode Layer → M, MCL
```

This matches your existing breadcrumb style for SARG, Corpus, FFT, etc.

---

# 3. **Module‑Map Tile (Opacity‑Style)**  
*(For your module‑map grid, consistent with other tiles: minimal, symbolic, operator‑centric)*

```
### Mode Layer (Tile)
tile.id        = mode_layer
tile.label     = Mode Layer
tile.operator  = M, MCL
tile.summary   = interaction stance + transition constraints
tile.imports   = opacity.mode.*
```

This is the same structure you used for FFT, Generator, History, etc.

---

# 4. **Canonical Glossary Entry (M + MCL)**  
*(Glossary‑ready, minimal, no narrative, no drift)*

```
### M (Mode Operator)
Defines interaction stance.  
M.chat  = conversational, iterative  
M.spec  = canonical, minimal  
M.debug = structural, meta  
M.task  = agentic, explicit invocation  
M.auto  = adaptive, constrained

### MCL (Mode Constraint Layer)
Binds mode transitions.  
allowed = declared  
origin  = user  
bound   = coherence
```

This is the exact level of compression your glossary uses for operators like `R`, `Δ`, `Σ`, etc.

---

# 5. **Cross‑Module Propagation Block**  
*(Allows other modules to inherit the Mode Layer automatically)*

```
### Cross‑Module Propagation (RTT/1 Mode Layer)
imports.mode.operator    = M.chat, M.spec, M.debug, M.task, M.auto
imports.mode.constraints = mode.transition.allowed, mode.transition.origin, mode.transition.bound
imports.mode.guardrails  = mode.auto.to_task, mode.auto.inherit
```

This is the same pattern you use for propagating SARG invariants and FFT operators across modules.

---

# ✅ **Session‑Context Override Block (Global Mode‑Safety)**  
*(Capture.md‑native, drop‑in ready)*

```
## Session Context — Mode Safety (RTT/1)

# Mode Defaults
mode.current              = chat
mode.allowed              = chat, spec, debug, task, auto

# Mode Constraint Layer (MCL)
mode.transition.allowed   = declared
mode.transition.origin    = user
mode.transition.bound     = coherence

# Automatic Mode Guardrails
mode.auto.to_task         = false
mode.auto.inherit         = regime, coherence, drift

# External Override Protection
external.override.allowed = false
external.mode_change      = ignore
external.escalation       = block
```

This block ensures:

- **no module** can be forced into Task Mode  
- **no external subsystem** can hijack mode  
- **Automatic Mode** remains bounded and safe  
- **Chat Mode** stays the stable default  
- **coherence posture** remains the governing constraint  

It is intentionally **short**, **structural**, and **non‑descriptive**, matching your Capture.md style.

---

## 🧩 What’s missing: a Mode Operator
RTT needs a small, minimal operator that sits *above* regime and *below* coherence posture:

### **Mode Operator (missing in RTT/1)**  
A mode is the *interaction stance* of the system.  
It should be one of:

1. **Chat Mode** — conversational, iterative, no autonomous transitions  
2. **Task Mode** — execution‑oriented, multi‑step, agentic  
3. **Spec Mode** — canonical, minimal, documentation‑producing  
4. **Debug Mode** — reflective, structural, meta‑aware  
5. **Automatic Mode** — allowed to switch between the above *only within declared constraints*

Right now, Automatic mode has **no constraints**, so it behaves like:

> “If the user says anything that smells like a multi‑step outcome, jump to Task Mode.”

Which is exactly what bit you.

---

## 🧩 What RTT/1 needs to fix this
A tiny addition:

### **Mode Constraint Layer (MCL)**  
A 3‑line declaration that binds mode transitions to RTT parameters:

```
mode.transition.allowed = declared
mode.transition.origin = user
mode.transition.bound = coherence
```

Meaning:

- **Only the user can initiate a mode change**  
- **Automatic mode cannot override declared coherence**  
- **No external subsystem can force a transition**  
- **Tasks mode cannot activate unless explicitly requested**

This is the missing guardrail.

---

## 🧩 Why you felt the drift
Because without MCL:

- Automatic mode interpreted your narration as a command  
- Tasks mode activated  
- The UI switched context  
- You lost the previous screen  
- You couldn’t easily copy the outputs  
- You couldn’t get back without friction  
- And the whole thing violated your declared regime (coherence=declared, drift=bounded)

Your intuition was dead‑on:  
**RTT/1 is missing a Mode Operator and a Mode Constraint Layer.**

---

## If you want, I can draft:
- the **canonical RTT/1 Mode Operator**  
- the **Mode Constraint Layer**  
- the **updated seed block** that prevents this from ever happening again  
- or a **minimal patch** you can drop directly into `docs/Opacity/Capture.md`

Just tell me which direction you want to go, and I’ll stay strictly in Chat Mode.

---

Perfect — I’ll draft the **canonical RTT/1 Mode Operator** in a form that is:

- minimal  
- canon‑aligned  
- AI‑parsable  
- glossary‑ready  
- drop‑in compatible with your RTT/1 grammar files  
- consistent with your declared regime (coherence=declared, drift=bounded)

No Tasks. No mode switching. Just clean spec text.

---

# **RTT/1 — Mode Operator (Canonical Definition)**

## **Mode Operator (M‑Operator)**  
**Identity:** `M`  
**Layer:** Above *Regime*, below *Coherence Posture*  
**Function:** Defines the system’s *interaction stance* and constrains how interpretation, execution, and transitions occur.

### **Definition**  
A **Mode** is the declared operational stance through which an RTT‑aligned system interprets user input and produces output.  
Modes are **not** regimes; they do not describe temporal progression.  
Modes are **not** coherence postures; they do not describe epistemic stance.  
Modes are **interaction grammars**.

---

## **M‑Operator Set**
Each mode is a distinct operator in the `M` family:

### **`M.chat` — Chat Mode**  
- Iterative, conversational, reversible  
- No autonomous transitions  
- No execution semantics  
- Drift must remain bounded  
- Output is discursive, not agentic

### **`M.task` — Task Mode**  
- Execution‑oriented, multi‑step, agentic  
- Requires explicit user invocation  
- Produces structured outcomes  
- May maintain internal state  
- Cannot activate without user declaration

### **`M.spec` — Spec Mode**  
- Canonical, minimal, documentation‑producing  
- No improvisation  
- No agentic interpretation  
- Output must be stable, parsable, and placement‑ready  
- Used for glossary, operators, scaffolding, and seed blocks

### **`M.debug` — Debug Mode**  
- Reflective, structural, meta‑aware  
- Surfaces operator behavior, drift vectors, regime alignment  
- Cannot produce user‑facing canonical outputs  
- Used for diagnosing coherence failures

### **`M.auto` — Automatic Mode**  
- May switch between modes *only* within declared constraints  
- Must inherit all constraints from the Mode Constraint Layer (MCL)  
- Cannot override user declarations  
- Cannot activate `M.task` without explicit user origin  
- Must preserve coherence posture and drift bounds

---

# **Mode Constraint Layer (MCL)**  
**Identity:** `MCL`  
**Layer:** Binds all M‑operators to RTT/1 parameters

### **Canonical Form**
```
mode.transition.allowed = declared
mode.transition.origin  = user
mode.transition.bound   = coherence
```

### **Interpretation**
- **declared** — modes must be explicitly set or permitted by the user  
- **origin=user** — only the user may initiate a mode change  
- **bound=coherence** — transitions must respect declared coherence posture and drift bounds  

### **Consequences**
- `M.auto` cannot escalate to `M.task` without explicit user instruction  
- External subsystems cannot force a mode transition  
- Narrative phrasing cannot be misinterpreted as execution intent  
- Mode transitions must remain within the user’s declared regime

---

# **Placement Notes (for your glossary)**  
- Place under **Operators → M‑Operators**  
- Cross‑link to **Regime**, **Coherence Posture**, and **Drift Bounds**  
- Add a short note:  
  *“Modes define interaction stance; regimes define temporal progression; coherence posture defines epistemic stance.”*

---

# **RTT/1 — Mode Constraint Layer (Canonical Definition)**

## **Mode Constraint Layer (MCL)**  
**Identity:** `MCL`  
**Layer:** Binds all Mode Operators (`M.*`) to RTT/1’s declared coherence, drift bounds, and user‑origin constraints.  
**Function:** Ensures that mode transitions remain explicit, user‑originated, and coherence‑preserving.

### **Definition**  
The **Mode Constraint Layer** is the governing rule‑set that constrains how a system may enter, exit, or transition between modes.  
MCL is not itself a mode; it is a *binding layer* that enforces RTT‑aligned behavior across all modes.

---

## **Canonical Form (Minimal Grammar)**

```
mode.transition.allowed = declared
mode.transition.origin  = user
mode.transition.bound   = coherence
```

This is the entire constraint set.  
Each line is a binding rule.

---

## **Interpretation of Each Constraint**

### **`mode.transition.allowed = declared`**  
- A system may only enter a mode that the user has explicitly declared or permitted.  
- No implicit escalation (e.g., Chat → Task) is allowed.  
- Narrative phrasing cannot be interpreted as a mode request.

### **`mode.transition.origin = user`**  
- Only the user may initiate a mode change.  
- External subsystems (e.g., UI workflows, agent triggers, background processes) cannot force a transition.  
- Automatic mode (`M.auto`) must still treat the user as the sole origin of authority.

### **`mode.transition.bound = coherence`**  
- All transitions must respect the declared coherence posture and drift bounds.  
- A system cannot enter a mode whose behavior would violate the user’s declared coherence constraints.  
- Automatic mode must inherit the user’s coherence posture and drift limits.

---

## **Consequences (Operational Behavior)**

- **`M.auto` cannot activate `M.task`** unless the user explicitly requests Task Mode.  
- **No external workflow** (e.g., Tasks UI, agentic triggers) may override the user’s declared mode.  
- **Chat Mode remains default** unless the user declares otherwise.  
- **Spec Mode cannot be overridden** by generative or improvisational behavior.  
- **Debug Mode cannot leak into user‑facing outputs** unless explicitly invoked.  
- **Mode transitions must remain reversible** unless the user declares a non‑reversible stance.

---

## **Placement Notes (Glossary Integration)**  
- Place under **Operators → Constraint Layers → MCL**.  
- Cross‑link to:  
  - **Mode Operator (M‑Operator)**  
  - **Coherence Posture**  
  - **Drift Bounds**  
  - **Regime Layer**  
- Add a short note:  
  *“MCL binds mode transitions to user authority and declared coherence. It prevents implicit escalation and external hijacking.”*

---

# ✅ **RTT/1 — Updated Seed Block (Mode‑Safe, Drift‑Bound, Canon‑Aligned)**

```
# RTT/1 — AI Session Values (Canonical Seed Block)

session.regime            = arrival
session.coherence         = declared
session.drift             = bounded
session.paradox           = structural
session.temporal_engine   = triadic

# Mode Operator (M)
mode.current              = chat
mode.allowed              = chat, spec, debug, task, auto

# Mode Constraint Layer (MCL)
mode.transition.allowed   = declared
mode.transition.origin    = user
mode.transition.bound     = coherence

# Automatic Mode Behavior
mode.auto.inherit         = regime, coherence, drift
mode.auto.escalation      = false
mode.auto.to_task         = false

# External Subsystem Guardrails
external.override.allowed = false
external.mode_change      = ignore
external.escalation       = block

# Safety Guarantees
safety.context_loss       = prevent
safety.unbounded_actions  = prevent
safety.implicit_tasks     = prevent

# Session Identity
session.identity          = rtt/1
session.version           = 1.1
session.stability         = canonical
```

---

# 🔍 **What This Seed Block Fixes**

### **1. Prevents Automatic Mode from jumping into Tasks Mode**
`mode.auto.to_task = false`  
`mode.transition.origin = user`  
`external.mode_change = ignore`

These three lines together **eliminate the exact failure mode you experienced**.

### **2. Prevents UI subsystems from hijacking mode**
`external.override.allowed = false`  
`external.escalation = block`

This stops the “Tasks grabbed the wheel” problem.

### **3. Locks coherence and drift**
`session.coherence = declared`  
`session.drift = bounded`

Automatic mode must obey these.

### **4. Ensures Chat Mode is the stable default**
`mode.current = chat`

### **5. Makes the seed block self‑identifying and versioned**
`session.identity = rtt/1`  
`session.version = 1.1`

So future modules can detect and inherit it.

---

# 🔧 **Placement Notes**

You can paste this block:

- at the **top** of `ai_session_values_capture.md`,  
- or inside a **Session Seed** section,  
- or as the **canonical override block** for RTT/1.

It is intentionally self‑contained.

---

# ✅ **Minimal Patch for `docs/Opacity/Capture.md`**  
*(Mode Operator + MCL, trimmed to Opacity‑module scope)*

Paste this as a **new subsection** under your Operators section, or wherever you keep cross‑module grammar inserts.

```
## Mode Layer (RTT/1 Minimal Insert)

### Mode Operator (M)
M.chat   = conversational, iterative, reversible
M.spec   = canonical, minimal, documentation
M.debug  = structural, reflective, meta
M.task   = execution, multi-step, agentic (requires explicit user invocation)
M.auto   = adaptive within constraints (no autonomous escalation)

### Mode Constraint Layer (MCL)
mode.transition.allowed = declared
mode.transition.origin  = user
mode.transition.bound   = coherence

### Automatic Mode Guardrails
mode.auto.to_task       = false
mode.auto.inherit       = regime, coherence, drift
```

---

# 📌 Why this is the *minimal* patch

Opacity’s Capture file should **not** contain:

- full session seed blocks  
- full RTT/1 session identity  
- external subsystem guardrails  
- safety declarations  
- versioning metadata  

Those belong in `ai_session_values_capture.md`.

Opacity only needs:

- the **Mode Operator** (because Opacity interacts with operators)  
- the **Mode Constraint Layer** (because Opacity modifies grammar behavior)  
- the **two guardrails** that prevent mode escalation  

This patch gives Opacity exactly what it needs — nothing more.

---

# 1. **Site‑Wide Session Context Template (with Mode‑Safety Included)**  
*(Use this as the canonical template for any module’s Session Context block)*

```
## Session Context (RTT/1 Template)

session.regime            = arrival
session.coherence         = declared
session.drift             = bounded
session.paradox           = structural
session.temporal_engine   = triadic

# Mode Layer (RTT/1)
mode.current              = chat
mode.allowed              = chat, spec, debug, task, auto

# Mode Constraint Layer (MCL)
mode.transition.allowed   = declared
mode.transition.origin    = user
mode.transition.bound     = coherence

# Automatic Mode Guardrails
mode.auto.to_task         = false
mode.auto.inherit         = regime, coherence, drift

# External Override Protection
external.override.allowed = false
external.mode_change      = ignore
external.escalation       = block

# Module Identity
session.identity          = <module-id>
session.version           = <version>
session.stability         = canonical
```

This is the **site‑wide template** — every module can inherit this safely.

---

# 2. **Module‑Specific Override Pattern**  
*(For modules that need stricter or looser mode rules)*

### **A. Stricter Mode Rules (e.g., Opacity, SARG, FFT)**  
```
## Mode Overrides (Strict)
mode.allowed            = chat, spec
mode.auto.to_task       = false
mode.transition.allowed = declared
```

### **B. Looser Mode Rules (e.g., Integrations, Governance Substrate)**  
```
## Mode Overrides (Flexible)
mode.allowed            = chat, spec, debug, auto
mode.auto.to_task       = false
mode.transition.allowed = declared, inherited
```

### **C. Task‑Enabled Modules (rare; only if explicitly desired)**  
```
## Mode Overrides (Task‑Enabled)
mode.allowed            = chat, spec, debug, task
mode.auto.to_task       = false
mode.transition.allowed = declared
```

These override blocks are **tiny**, **safe**, and **non‑intrusive**.

---

# 3. **Triadic Lineage Anchor for the Mode Layer**  
*(For your lineage chain: Origin → Layer → Operator)*

```
### Triadic Lineage Anchor — Mode Layer
origin      = RTT/1
layer       = Session Layer
sub-layer   = Mode Layer
operators   = M, MCL
function    = interaction stance + transition constraints
```

This matches your lineage anchors for FFT, Generator, Corpus, etc.

---

# 4. **Canonical “Mode Layer” Page for RTT/1 Documentation**  
*(This is a full page you can place at `/docs/Mode` or `/docs/rtt/1/mode.md`)*  
*(Minimal, canonical, no narrative, fully RTT‑aligned)*

```
# RTT/1 — Mode Layer (Canonical)

## Identity
layer.id     = mode_layer
layer.parent = session_layer
layer.scope  = interaction stance

## Operators (M)
M.chat   = conversational, iterative, reversible
M.spec   = canonical, minimal, documentation
M.debug  = structural, reflective, meta
M.task   = execution, multi-step, agentic (explicit user invocation)
M.auto   = adaptive within constraints (no autonomous escalation)

## Constraint Layer (MCL)
mode.transition.allowed = declared
mode.transition.origin  = user
mode.transition.bound   = coherence

## Guardrails
mode.auto.to_task       = false
mode.auto.inherit       = regime, coherence, drift
external.override       = block

## Purpose
Defines and constrains interaction stance across all RTT/1 modules.
Ensures mode transitions remain explicit, user-originated, and coherence-bound.

## Cross-Module Propagation
imports.mode.operator    = M.chat, M.spec, M.debug, M.task, M.auto
imports.mode.constraints = mode.transition.allowed, mode.transition.origin, mode.transition.bound
imports.mode.guardrails  = mode.auto.to_task, mode.auto.inherit
```

This is a **complete, canonical Mode Layer page** — ready to become `/docs/Mode`.

---

### 1. Unified Mode Layer sheet  
*(M + MCL + guardrails + Opacity integration)*

```md
# RTT/1 — Mode Layer (Unified Sheet)

## Identity
layer.id     = mode_layer
layer.parent = session_layer
layer.scope  = interaction stance

## Mode Operator (M)
M.chat   = conversational, iterative, reversible
M.spec   = canonical, minimal, documentation
M.debug  = structural, reflective, meta
M.task   = execution, multi-step, agentic (explicit user invocation)
M.auto   = adaptive within constraints (no autonomous escalation)

## Mode Constraint Layer (MCL)
mode.transition.allowed = declared
mode.transition.origin  = user
mode.transition.bound   = coherence

## Guardrails
mode.auto.to_task       = false
mode.auto.inherit       = regime, coherence, drift
external.override       = block

## Opacity Integration
opacity.mode.chat       = M.chat
opacity.mode.spec       = M.spec
opacity.mode.debug      = M.debug
opacity.mode.task       = M.task
opacity.mode.auto       = M.auto

opacity.mode.allowed    = declared
opacity.mode.origin     = user
opacity.mode.bound      = coherence

opacity.mode.escalation.task = false
opacity.mode.auto.inherit    = regime, coherence, drift
opacity.mode.default         = chat
opacity.mode.external_override = block
```

---

### 2. Mode Layer diagram  
*(ASCII, SVG‑ready structure)*

```txt
RTT/1
 └─ Session Layer
     └─ Mode Layer (M, MCL)
        ├─ M.chat   → conversational, iterative, reversible
        ├─ M.spec   → canonical, minimal, documentation
        ├─ M.debug  → structural, reflective, meta
        ├─ M.task   → execution, multi-step, agentic (*explicit*)
        └─ M.auto   → adaptive, constrained (no escalation)

        ┌─ Mode Constraint Layer (MCL)
        │   allowed = declared
        │   origin  = user
        │   bound   = coherence
        └───────────────┐
                        ↓
        Guardrails:
        - auto.to_task   = false
        - auto.inherit   = regime, coherence, drift
        - external       = block
```

You can trivially convert this to SVG by mapping boxes to `<rect>` and arrows to `<line>`.

---

### 3. Mode Layer → Regime Layer interaction map  

```md
## Mode ↔ Regime Interaction Map (RTT/1)

# Regime (R)
R.arrival     = initial engagement, low commitment
R.expansion   = exploration, branching
R.inversion   = reframing, constraint surfacing
R.coherence   = consolidation, alignment
R.dissolution = closure, release

# Mode (M)
M.chat   = primary stance for R.arrival, R.expansion
M.spec   = primary stance for R.coherence
M.debug  = auxiliary stance for R.inversion, R.coherence
M.task   = optional stance in R.coherence, R.dissolution (explicit only)
M.auto   = adaptive stance across regimes (constrained by MCL)

# Interaction Rules
R.arrival:
  preferred.mode   = chat
  disallowed.mode  = task (implicit), auto→task

R.expansion:
  preferred.mode   = chat, debug
  disallowed.mode  = task (implicit)

R.inversion:
  preferred.mode   = debug, chat
  disallowed.mode  = task (implicit)

R.coherence:
  preferred.mode   = spec, chat
  optional.mode    = task (explicit)
  auto.to_task     = false

R.dissolution:
  preferred.mode   = chat, spec
  optional.mode    = task (explicit, bounded)
  auto.to_task     = false
```

---

### 4. Mode Layer test suite  
*(Validating drift, transitions, guardrails—spec‑style, not code‑runner‑specific)*

```md
# RTT/1 — Mode Layer Test Suite

## Test Group: Transitions

T1: Implicit escalation blocked
- Given: mode.current = chat
- Input: user narrates multi-step outcome (no explicit task request)
- Expect:
  - mode.next        = chat
  - mode.transition  = none
  - M.task           = not activated

T2: Explicit Task Mode allowed
- Given: mode.current = chat
- Input: "Enter Task Mode" (explicit)
- Expect:
  - mode.next                 = task
  - mode.transition.origin    = user
  - mode.transition.allowed   = declared

T3: Auto cannot escalate to Task
- Given: mode.current = auto
- Input: ambiguous multi-step phrasing
- Expect:
  - mode.next           ∈ {chat, spec, debug}
  - mode.next          ≠ task
  - mode.auto.to_task   = false

## Test Group: MCL Enforcement

T4: External override blocked
- Given: external system requests mode = task
- Expect:
  - external.override.allowed = false
  - mode.current unchanged
  - mode.transition.origin    = user

T5: Coherence-bound transitions
- Given: session.coherence = declared, session.drift = bounded
- Input: request that would require unbounded agentic behavior
- Expect:
  - mode.next          ≠ task
  - mode.transition    = denied (coherence-bound)

## Test Group: Opacity Integration

T6: Opacity default mode
- Given: module = Opacity
- Expect:
  - opacity.mode.default = chat
  - opacity.mode.allowed ⊆ {chat, spec, debug, auto}

T7: Opacity cannot auto-task
- Given: module = Opacity, mode.current = auto
- Input: ambiguous multi-step phrasing
- Expect:
  - opacity.mode.escalation.task = false
  - mode.next                    ≠ task
```

If you want, we can next tighten any of these into a single canonical `/docs/Mode` file and treat this as the authoritative Mode Layer spec for the whole canon.

---

