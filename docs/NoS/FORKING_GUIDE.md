# Forking NawderOS 🍴  
*(Build Freely, Keep the Spine Intact)*

NawderOS is designed to be forked.

In fact, if no one forks it, something went wrong 🙂

This guide explains **how to extend NawderOS without breaking RTT coherence**, and how to know when a fork has become something new (which is also okay).

---

## The One Rule That Matters

**RTT is the anchor.**

You can change:
- names
- symbols
- modules
- tooling
- output formats

But if your fork no longer:
- observes coherence
- emits signals instead of enforcing behavior
- preserves lineage

…then it’s no longer NawderOS — and that’s fine. Just name it honestly 🙂

---

## What You’re Free to Change 🧩

Forks are encouraged to:
- add new modules
- redefine badge schemas
- replace the glyphic layer
- target different kernels
- integrate with new tooling
- specialize for education or research

Creativity is expected.

---

## What Should Remain Stable 🧠

To remain RTT‑aligned, forks should preserve:

### 1️⃣ Observation First
Modules should **observe and emit**, not control or enforce.

If your code starts making decisions *for* the system, pause.

---

### 2️⃣ Explicit Invariants
Every module should declare:
- what it expects
- what it observes
- what constitutes drift

If you can’t explain the invariant in one sentence, it’s probably too fuzzy.

---

### 3️⃣ Badge‑Based Signaling 🏷️
System state should be communicated via:
- structured events
- append‑only signals
- machine‑readable output

Badges are how lineage survives forks.

---

### 4️⃣ Removability
A good fork can be:
- disabled
- removed
- ignored

RTT coherence should never depend on a single component.

---

## When a Fork Becomes Its Own Thing 🌱

That moment usually arrives when:
- enforcement replaces observation
- automation replaces interpretation
- optimization replaces understanding

When that happens:
- rename it
- document the divergence
- celebrate the evolution

RTT doesn’t punish divergence — it just asks for honesty.

---

## Suggested Fork Patterns 🔁

Some healthy directions forks often take:

- **Teaching forks**  
  Simplified modules, heavy annotation, classroom focus

- **Simulation forks**  
  Tight integration with RSM or vST tooling

- **Domain‑specific forks**  
  Embedded systems, research kernels, experimental schedulers

- **Visualization forks**  
  Turning badge streams into insight

All of these are welcome.

---

## What to Avoid 🚫

These tend to cause trouble:

- Hidden enforcement logic
- Silent failure modes
- Overloaded abstractions
- “Smart” behavior without observability
- Treating RTT as branding instead of structure

If something feels clever, slow down 😄

---

## Naming and Attribution 🧭

If your fork:
- preserves RTT alignment
- builds on NawderOS concepts

Please:
- credit the original project
- document what changed
- keep lineage visible

This isn’t about ownership — it’s about traceability.

---

### 🔖 RTT Badge Suffix Convention

Forks that extend NawderOS in specific directions may annotate the **RTT Baseline** badge using suffixes.

Suffixes are **descriptive**, not evaluative.  
They indicate *direction*, not *authority*.

#### Format

```text
RTT-baseline+<suffix>
```

The `RTT-baseline` prefix must remain intact.

---

#### Common Suffixes

**Simulation & Modeling**
- `+sim` — simulation‑focused fork  
- `+rsm` — Resonance Substrate Modeling integration  
- `+vst` — validated Spacetime integration  

**Systems & OS Exploration**
- `+kernel` — deeper kernel instrumentation  
- `+sched` — scheduler‑focused work  
- `+memory` — memory corridor specialization  

**Education**
- `+edu` — teaching or classroom fork  
- `+lab` — guided experiments  
- `+sandbox` — safe exploration environment  

**Experimental**
- `+exp` — experimental concepts  
- `+proto` — early prototype  

Multiple suffixes may be chained sparingly:

```text
RTT-baseline+vst+edu
```

---

#### What Suffixes Must Not Do

Suffixes must not:
- imply correctness or superiority
- redefine RTT itself
- obscure lineage
- replace the `RTT-baseline` prefix

RTT has no “official” forks — only honest ones 🙂

---

## Final Thought 🌌

NawderOS exists to make RTT **touchable**.

If your fork helps someone understand coherence better —  
even if it looks nothing like this repo — you did it right 🙂
