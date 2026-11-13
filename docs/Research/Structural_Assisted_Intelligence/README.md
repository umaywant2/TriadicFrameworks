
- [`sai_module.json`](sai_module.json) — Agentic module schema role assignments

# **Structural Assisted Intelligence (SAI)**

## *TriadicFrameworks — Research Substrate*
### *Canonical README*

---

## **Purpose**

**Structural Assisted Intelligence (SAI)** is a small, model-independent structural reasoning kernel that implements Resonance-Time Theory (RTT) as executable grammar.

It demonstrates that useful machine reasoning can begin with structure, operators, observation, and provenance rather than with a trained model.

SAI is intentionally kernel-like: a minimal, inspectable substrate from which higher capabilities may be built. It is not a chatbot, knowledge base, operating system, or LLM replacement.

---

## **Architectural Separation**

```
Application
    ↓
   LMA          Language Model Atlas (language & knowledge resources)
    ↓
   SAI          Structural reasoning kernel
    ↓
RTT Structural Grammar
```

- **SAI** is the authority on state, relations, coherence, provenance, and uncertainty.
- **LMA** (Language Model Atlas) is a surrounding map of language capabilities (dictionaries, rule parsers, tiny models, local or remote LLMs). It translates between human language and SAI structure. It does not become the intelligence substrate.
- RTT supplies the structural grammar beneath both.

---

## **Core Principles**

- Unknown is a valid, stable, and successful state.
- Operators may transform structure. They may not invent evidence.
- Explanation is provenance, not generation.
- Intelligence, if it emerges, arises from repeated structural evaluation across state and time.
- Design under scarcity from day one: kilobytes before megabytes, deterministic operations before generation, no model dependency for core function.
- Small enough to understand. Structured enough to reason. Open enough to build upon. Old enough to run almost anywhere.

---

## **Six Components (v0)**

1. **Observation** — Entry of any input with identity, content, provenance, order, and status. Observed ≠ inferred ≠ unknown.
2. **Structural State** — Minimal internal representation (Entity–Relation–Entity plus RTT state).
3. **RTT Operator Kernel** — Small canonical operator set (OBSERVE, RELATE, ALIGN, DIFFERENTIATE, RESOLVE, STABILIZE, RECALL).
4. **Triadic Observer** — Maintains claim / counterstate / observer. Emits structural statuses (coherent, conflicting, unresolved, insufficient, drifting).
5. **Tiny Persistent Memory** — Explicit history of observations → relations → operations → resulting states. Walkable for provenance.
6. **Minimal Interface** — Primitive, non-linguistic status reporting. Natural language is deferred to the LMA layer.

---

## **Module Contents**

- **README.md** — This file. Module purpose, architecture, and principles.
- **SAI-DESIGN.md** — Canonical one-page design: invariants, permitted transitions, and absolute rules.
- **sai_capture.md** — Original concept capture and design dialogue.
- **sai_module.json** — Agentic module schema.

---

## **Usage**

SAI is intended as a research kernel and educational substrate. Early implementations should prioritize:

- Deterministic, inspectable operation
- Explicit provenance
- Bounded output states
- Zero dependency on an LLM for core function
- Compatibility with constrained or retro environments

Higher layers (applications, LMA adapters, domain schemas) may be built above the kernel without modifying its invariants.

---

## **Notes**

This module belongs to the Research substrate. It explores whether structure + operators + memory + recurrence can produce useful reasoning before a model is introduced at all.

When a model is later introduced through an LMA, the experiment continues: what residual work remains for the model?

Canonical session header:

```
rtt=1 | coherence=declared | drift=bounded | paradox=structural
```

---

**Structural Assisted Intelligence · Resonance-Time Theory · Research Substrate**

Deterministic.  
Inspectable.  
Buildable.  
Model-independent.
