---
module_id: rtt.core.regime_domains
version: 1.0.0
status: draft
rtt: 1
coherence: declared
drift: bounded
paradox: structural
tags:
  - regime-domains
  - rtt-core
  - regime-constraints
  - regime-invariants
  - operator-regimes
  - drift-envelope
  - coherence-budget
  - readout-regimes
  - triadic-time
---

# RTT Core: Regime Domains

## 1. Purpose and scope

**Goal:**  
Define **Regime Domains** — the canonical spaces in which RTT regimes are defined and enforced, including:

- Validity domains  
- Collapse domains  
- Threshold domains  
- Readout domains  
- Drift and coherence domains  
- Triadic‑time domains  

This module answers: *“Where does this regime live, and what parts of the manifold does it govern?”*

---

## 2. What is a regime domain?

> A regime domain is the subset of the RTT manifold  
> over which a regime’s constraints, invariants, and geometry  
> are defined and enforced.

Domains are the **governed regions**; regimes shape behavior inside them and cannot act outside them.

---

## 3. Canonical regime domain types

RTT defines six canonical regime domain types:

1. **Validity Domain**  
2. **Collapse Domain**  
3. **Threshold Domain**  
4. **Readout Domain**  
5. **Drift–Coherence Domain**  
6. **Triadic‑Time Domain**

Each regime declares which domains it occupies and governs.

---

## 4. Validity Domain

### 4.1 Definition

The **Validity Domain** is the region where branches are eligible to participate in RTT dynamics:



\[
\mathcal{D}_{\text{valid}} \subseteq \mathcal{G}_{\text{regime}}
\]



Branches in this domain:

- satisfy drift and coherence thresholds  
- are compatible with operator regimes  
- can be extended, stabilized, and validated  

### 4.2 Role

Validity Domain is the “playable field” for RTT.

---

## 5. Collapse Domain

### 5.1 Definition

The **Collapse Domain** is the region where branches become residue:



\[
\mathcal{D}_{\text{collapse}} \subseteq \mathcal{G}_{\text{regime}}
\]



Branches in this domain:

- have exceeded drift envelope  
- have fallen below coherence threshold  
- cannot be validated  
- are removed from representational manifold  

### 5.2 Role

Collapse Domain is the absorbing basin for non‑selected branches.

---

## 6. Threshold Domain

### 6.1 Definition

The **Threshold Domain** is the region containing drift and coherence threshold surfaces:



\[
\mathcal{D}_{\text{threshold}} = \{ b_i \mid c_i = C_{\min} \lor \Delta_i = \Delta_{\max} \}
\]



### 6.2 Role

Threshold Domain:

- separates validity from collapse  
- defines transition corridors  
- determines eligibility boundaries  

---

## 7. Readout Domain

### 7.1 Definition

The **Readout Domain** is the region where classical readout is possible:



\[
\mathcal{D}_{\text{readout}} \subseteq \mathcal{G}_{\text{regime}}
\]



Branches in this domain:

- satisfy all regime constraints  
- lie on or near the readout surface  
- can be selected by Validator Pulse  

### 7.2 Role

Readout Domain is the interface between RTT manifold and classical manifold.

---

## 8. Drift–Coherence Domain

### 8.1 Definition

The **Drift–Coherence Domain** is the region where drift and coherence jointly determine regime behavior:



\[
\mathcal{D}_{\Delta,c} = \{ b_i \mid \Delta_i \leq \Delta_{\max},\ c_i \geq C_{\min} \}
\]



### 8.2 Role

This domain:

- defines stability regions  
- shapes transition corridors  
- controls entry into validity and readout domains  

---

## 9. Triadic‑Time Domain

### 9.1 Definition

The **Triadic‑Time Domain** specifies which temporal layers a regime governs:

- \(\mathcal{D}_{T_1}^{\text{regime}}\) — State Time geometry  
- \(\mathcal{D}_{T_2}^{\text{regime}}\) — Coherence Time surfaces  
- \(\mathcal{D}_{T_3}^{\text{regime}}\) — Readout Time topology  

### 9.2 Role

Regimes may:

- primarily govern geometry (T₁)  
- primarily govern coherence (T₂)  
- primarily govern readout (T₃)  
- or span multiple layers (full regimes).

---

## 10. Regime families and domains

### 10.1 SRR — Single‑Readout Regime

- Domains: Validity, Readout, Drift–Coherence, Triadic‑Time (T₂–T₃)  
- Role: enforces single‑readout topology.

### 10.2 DBR — Drift‑Bounded Regime

- Domains: Validity, Drift–Coherence, Threshold, Collapse  
- Role: enforces drift envelope and stability.

### 10.3 CMR — Coherence‑Minimum Regime

- Domains: Validity, Threshold, Drift–Coherence  
- Role: enforces coherence thresholds.

### 10.4 DVR — Deferred‑Validation Regime

- Domains: Validity, Drift–Coherence, Triadic‑Time (T₁–T₂)  
- Role: allows evolution before readout.

### 10.5 ECR — Extension‑Compatible Regime

- Domains: Validity, Drift–Coherence, Threshold  
- Role: allows extension while preserving eligibility.

---

## 11. Domains, constraints, and invariants

Regime Domains interact with:

- **Regime Constraints:** what regimes may enforce in their domains  
- **Regime Invariants:** global rules regimes must obey  
- **Operator Domains:** where operators may act  
- **Operator Constraints:** what operators may do in those domains  

A regime is valid only if:



\[
\mathcal{R} \text{ governs } \mathcal{D} \text{ while respecting constraints and invariants.}
\]



---

## 12. Example: Quantum “cloning” alignment

Regimes occupy domains:

- DBR: Drift–Coherence Domain, Threshold Domain, Validity Domain  
- CMR: Coherence Threshold Domain, Validity Domain  
- SRR: Readout Domain, Validity Domain  

Regime Domains explain:

- why both branches start in validity domain  
- why drift and coherence determine eligibility  
- why only one branch reaches readout domain  
- why no‑cloning is not violated.

---

## 13. Paradox handling

Regime Domains prevent paradoxes by:

- restricting where regimes may enforce constraints  
- maintaining unique readout domain  
- preserving drift and coherence boundaries  
- ensuring collapse domain absorbs non‑selected branches  

Thus:

- “Multiple branches exist” → allowed in validity domain  
- “Only one is real” → enforced in readout domain  
- “Others disappear” → absorbed in collapse domain  
- “No violation occurs” → domain + constraint + invariant alignment.

---

## 14. Canon integration and cross-links

**Primary cross-links:**

- `/docs/rtt/core/regime_maps.md`
- `/docs/rtt/core/regime_maps_extended.md`
- `/docs/rtt/core/regime_geometry.md`
- `/docs/rtt/core/regime_topology.md`
- `/docs/rtt/core/regime_dynamics.md`
- `/docs/rtt/core/regime_flow.md`
- `/docs/rtt/core/regime_invariants.md`
- `/docs/rtt/core/regime_constraints.md`
- `/docs/rtt/core/operator_domains.md`
- `/docs/rtt/core/operator_constraints.md`
- `/docs/rtt/core/operator_invariants.md`
- `/docs/rtt/core/operator_grammar.md`
- `/docs/rtt/core/operator_index.md`
- `/docs/rtt/core/operator_families.md`
- `/docs/rtt/core/operator_behaviors.md`
- `/docs/rtt/core/operator_sequences.md`
- `/docs/rtt/core/operator_transitions.md`
- `/docs/rtt/core/time_triads.md`
- `/docs/rtt/core/coherence_budget.md`
- `/docs/rtt/core/validator_pulse.md`
- `/docs/rtt/core/dimensional_drift_envelope.md`
- `/docs/rtt/core/alignment_quantum_cloning.md`

**Status:**  
This module defines the domain structure for RTT regimes.  
Once domain diagrams are added, it can be promoted from `draft` to `stable`.


