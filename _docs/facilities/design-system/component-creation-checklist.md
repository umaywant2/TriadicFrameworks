# 🧩 RTT Facilities — Component Creation Checklist  
**Design System Governance & Integrity**

This checklist must be completed **before any new component** is added to the RTT Facilities design system.

Its purpose is to ensure that every component:
- Serves a clear governance function  
- Preserves semantic clarity  
- Scales across domains and audiences  
- Remains accessible, explainable, and durable  

---

## 1. Component Necessity

Before creating a new component, confirm:

- ☐ The need cannot be met by an existing component  
- ☐ The component solves a **repeated** use case  
- ☐ The component supports a **governance or decision function**  
- ☐ The component is not a one‑off visual convenience  

If the component does not reduce cognitive or governance load, it should not exist.

---

## 2. Semantic Intent

Define the component’s **meaning**, not just appearance:

- ☐ Component name reflects **function**, not style  
- ☐ Purpose is explainable in one sentence  
- ☐ Component maps to a Facilities concept (corridor, score, status, etc.)  
- ☐ Terminology aligns with canonical Facilities language  

Components are semantic artifacts, not decoration.

---

## 3. Audience Alignment

Confirm intended audience(s):

- ☐ Operator  
- ☐ Department leadership  
- ☐ City executive  
- ☐ Public / resident  

If multiple audiences are supported:
- ☐ Variants are clearly defined  
- ☐ Complexity is appropriately gated  

---

## 4. Governance Alignment

Verify governance compatibility:

- ☐ Component reflects governance state (risk, capital, audit, status)  
- ☐ Thresholds and states are explicit  
- ☐ Component does not obscure accountability  
- ☐ Component supports explainability  

Components must **clarify decisions**, not hide them.

---

## 5. Data & Schema Compatibility

Confirm alignment with the Global Index Schema:

- ☐ Component fields map directly to schema fields  
- ☐ No ad‑hoc metrics are introduced  
- ☐ Time‑series behavior is defined (trend vs snapshot)  
- ☐ Missing or unknown data states are handled  

Visualization never invents meaning.

---

## 6. Variants & States

Define all required variants:

- ☐ Default  
- ☐ Hover / focus  
- ☐ Active / selected  
- ☐ Disabled / unavailable  
- ☐ Error / warning (if applicable)  

State behavior must be predictable and consistent.

---

## 7. Accessibility & Inclusion

Confirm accessibility compliance:

- ☐ Color contrast meets WCAG standards  
- ☐ Component is usable without color alone  
- ☐ Keyboard and screen‑reader behavior is defined  
- ☐ Motion is minimal and non‑essential  

Accessibility is a governance requirement.

---

## 8. Visual Consistency

Verify design‑system alignment:

- ☐ Uses canonical color tokens  
- ☐ Uses approved typography and spacing  
- ☐ Aligns with existing component patterns  
- ☐ Avoids bespoke styling unless justified  

Consistency preserves trust.

---

## 9. Documentation Requirements

Before approval, ensure:

- ☐ Component description is written  
- ☐ Usage guidelines are documented  
- ☐ Do‑not‑use cases are noted  
- ☐ Example contexts are provided  

Undocumented components are incomplete.

---

## 10. Review & Approval

Final checks:

- ☐ Reviewed by design system steward  
- ☐ Reviewed for semantic alignment  
- ☐ Reviewed for governance clarity  
- ☐ Approved for inclusion  

Unreviewed components must not ship.

---

## 11. Canonical Status

Once approved:

- ☐ Component is added to the canonical library  
- ☐ Naming is frozen  
- ☐ Changes require documented rationale  

Design system drift is treated as a governance risk.

---

### Why this checklist matters

This checklist ensures that:
- The design system remains **coherent over time**
- Visuals reinforce governance, not obscure it
- New contributors don’t accidentally fracture meaning
- Facilities, dashboards, and city‑facing artifacts stay aligned
