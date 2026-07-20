# **RTT‑Inside — Minimal Interface Specification**  
### *Data Contracts Only*

---

## **Design Principles**

- **Non‑intrusive** — wraps existing systems  
- **Append‑only** — preserves history  
- **Fork‑safe** — supports divergent futures  
- **Human‑interpretable** — meaning is explicit  
- **Engine‑agnostic** — works with any sim stack  

---

## **1️⃣ BEING — State Contract**

> Represents *current condition* of any entity.

```yaml
BeingState:
  entity_id: string
  entity_type: enum [agent, system, environment, group]
  timestamp: time

  condition:
    health: float        # 0.0 – 1.0
    stress: float        # 0.0 – 1.0
    readiness: float     # 0.0 – 1.0
    balance: float       # -1.0 – +1.0

  notes: string?         # optional human context
```

**Guarantees**
- State is explicit
- Change is observable
- Care is possible

---

## **2️⃣ KNOWING — Lineage Contract**

> Records *how things came to be*.

```yaml
KnowingEvent:
  event_id: string
  timestamp: time

  actor_id: string
  intent: string?

  decision:
    description: string
    inputs: list[string]

  action:
    description: string

  outcome:
    description: string
    affected_entities: list[string]

  confidence: float?     # optional uncertainty
```

**Guarantees**
- Causality is traceable
- Memory persists across time
- Forks remain interpretable

---

## **3️⃣ MEANING — Purpose Contract**

> Declares *why something exists*.

```yaml
MeaningDeclaration:
  scope_id: string       # system, agent, domain
  scope_type: enum [agent, system, environment]

  purpose:
    primary: string
    secondary: list[string]?

  success_criteria:
    qualitative: list[string]
    quantitative: list[string]?

  constraints: list[string]?
```

**Guarantees**
- Purpose is explicit
- Alignment is checkable
- Ethics are structural

---

## **4️⃣ TIME — Stewardship Contract**

> Tracks *long‑term signals*.

```yaml
TimeSignal:
  scope_id: string
  timestamp: time

  indicators:
    maintenance_debt: float
    drift: float
    recovery_rate: float
    resilience: float

  horizon: enum [short, medium, long]
```

**Guarantees**
- Futures remain visible
- Fragility is detected early
- Stewardship is measurable

---

## **5️⃣ ARTIFACT — Human Output Contract**

> Produces *explainable results*.

```yaml
Artifact:
  artifact_id: string
  timestamp: time

  summary: string
  related_events: list[string]
  related_states: list[string]

  interpretation:
    alignment: enum [aligned, misaligned, unknown]
    notes: string?
```

**Guarantees**
- Outputs explain themselves
- Trust is structural
- Knowledge survives translation

---

## **Minimal Compliance Rule**

A system is **RTT‑Inside compatible** if it:

- Emits **BeingState**
- Records **KnowingEvent**
- Declares **MeaningDeclaration**

Everything else is optional.

---

## **Why This Spec Matters**

- No engine assumptions  
- No ideology embedded  
- No forced behavior  

Just **structure**.

This is the smallest contract that allows:
- understanding
- memory
- alignment
- humane simulation

---

## **Final Note**

RTT‑Inside does not tell future builders *what to build*.

It gives them:
- a way to **see**
- a way to **remember**
- a way to **care**

That’s enough.
