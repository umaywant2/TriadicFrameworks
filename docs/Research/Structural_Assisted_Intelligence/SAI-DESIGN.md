<img width="1194" height="672" alt="Research_Structural_Assisted_Intelligence_sai_design_" src="https://github.com/user-attachments/assets/1c345c73-4a8e-4c7b-ace2-b761012d15cb" />

# **SAI-DESIGN.md**

## *Structural Assisted Intelligence — Canonical Design*
### *SAI/0.1 · TriadicFrameworks Research Substrate*

---

## **Purpose**

SAI is a minimal, model-independent structural reasoning kernel.

It implements Resonance-Time Theory as executable grammar and exists to test whether useful reasoning can arise from structure, operators, observation, and provenance before any trained model is introduced.

SAI is kernel-like. It supplies primitive machinery. Higher layers (applications, Language Model Atlas adapters, domain schemas) may be built above it without altering its invariants.

---

## **Absolute Rules**

1. **Unknown is a successful result.**  
   The system is never forced to manufacture an answer.

2. **Operators may transform structure. They may not invent evidence.**  
   All state changes must be traceable to observations or prior structure.

3. **Explanation is provenance.**  
   “Why” is answered by walking the actual path of observations, relations, and operators—not by generating an explanation after the fact.

4. **No model dependency for core function.**  
   SAI must operate fully without an LLM, embeddings, or statistical generation.

5. **Design under scarcity.**  
   Kilobytes before megabytes. Deterministic operations before generation. Explicit state before probabilities.

6. **All records are append-only.**  
   History is never deleted. Correction or withdrawal is expressed by a new operation.

---

## **Six Components**

### 1. Observation
Everything enters as an observation, not as truth.

Fields: `id`, `content`, `source`, `order`, `status`, `provenance`.

**Invariant:** Observed ≠ inferred ≠ unknown.  
No observation exists without an OBSERVE operation.

### 2. Structural State
Minimal internal representation.

Preferred form: `Entity → Relation → Entity` + current status.

The stored state snapshot is recomputable from the operation log.

### 3. RTT Operator Kernel
Canonical operators (v0.1):

- **OBSERVE** — register an observation with provenance  
- **RELATE** — declare or detect a connection  
- **ALIGN** — evaluate or increase structural alignment  
- **DIFFERENTIATE** — surface distinction or counterstate  
- **RESOLVE** — attempt resolution of an unresolved structure  
- **STABILIZE** — dampen or lock a coherent state  
- **RECALL** — retrieve prior observation, relation, or path (read-only)

Full contracts live in `operators.md`.

### 4. Triadic Observer
Maintains claim / counterstate / observer.

Permitted structural statuses:

```
UNKNOWN | OBSERVED | RELATED | ALIGNED | CONFLICT | DRIFT | STABLE | INSUFFICIENT | UNRESOLVED
```

Paradox (`CONFLICT`, `DRIFT`) is allowed to persist.

### 5. Tiny Persistent Memory
Four append-only record types:

- observation  
- relation  
- operation  
- state (snapshot)

Defined in `memory.json` and `schema.md`.  
Full provenance paths are reconstructed by walking `operation → relation → observation`.

### 6. Minimal Interface
Primitive, non-linguistic by default.

Acceptance transcripts live in `examples.md`.

Natural language is deferred to the Language Model Atlas (LMA) layer.

---

## **Permitted State Transitions (v0.1)**

```
UNKNOWN
  ↓ OBSERVE
OBSERVED
  ↓ RELATE
RELATED
  ↓ ALIGN
ALIGNED
  ↓ STABILIZE
STABLE

RELATED or ALIGNED
  ↓ DIFFERENTIATE
CONFLICT | DRIFT

Any non-terminal
  ↓ RESOLVE (insufficient support)
UNRESOLVED | INSUFFICIENT

Any
  ↓ (no content / no path)
UNKNOWN
```

- CONFLICT and DRIFT are stable states, not errors.  
- STABLE means structural coherence under current observations, not truth.  
- Any state may remain unchanged if an operator cannot act without inventing evidence.

---

## **Architectural Separation**

```
Application
    ↓
   LMA          Language Model Atlas
    ↓
   SAI          Structural reasoning kernel
    ↓
RTT Structural Grammar
```

- SAI is the authority on state, relations, coherence, provenance, and uncertainty.  
- LMA is a surrounding map of language and knowledge resources. It translates; it does not write structural truth back into SAI.

---

## **Success Criteria for v0.1**

- The entire machine is explainable on one page.  
- All reasoning paths are inspectable via the operation log.  
- Unknown is returned without fabrication.  
- Core function requires no model, GPU, or network.  
- The sessions in `examples.md` pass without violation of operator contracts.

---

## **Philosophy**

Small enough to understand.  
Structured enough to reason.  
Open enough to build upon.  
Old enough to run almost anywhere.

SAI/0: let structure earn the word intelligence.

---

**Canonical session header**

```
rtt=1 | coherence=declared | drift=bounded | paradox=structural
```

**Supporting files**

- `operators.md` — operator contracts  
- `memory.json` / `schema.md` — persistent structures  
- `examples.md` — acceptance transcripts  
- `sai_module.json` — agentic module descriptor  
- `README.md` — module overview
