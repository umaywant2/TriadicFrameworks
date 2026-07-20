# 📝 RTT Facilities — Component Proposal Form  
**Design System Intake & Governance Review**

This form must be completed **before any new component** is created or added to the RTT Facilities design system.

Its purpose is to ensure that every component:
- Serves a clear governance function  
- Aligns with canonical Facilities concepts  
- Avoids duplication and semantic drift  
- Is reviewable before design or build effort begins  

---

## 1. Proposal Metadata

- **Proposed Component Name**  
  _(Must follow the Component Naming Convention)_  
  ```
  [Domain] / [Category] / [Function]
  ```

- **Proposer Name**  
- **Date Submitted**  
- **Related Domain(s)**  
  ☐ Facilities  
  ☐ AGERI  
  ☐ Dashboards  
  ☐ City‑Facing  

---

## 2. Component Purpose

**In one sentence, what does this component do?**

> _Describe the governance or decision function it supports._

---

## 3. Problem Statement

**What problem does this component solve?**

- What is currently unclear, repetitive, or error‑prone?
- Who experiences this problem?
- Why is an existing component insufficient?

---

## 4. Governance Alignment

**Which Facilities concepts does this component represent or support?**

- ☐ Corridor classification  
- ☐ Risk scoring (drift, harmonics, propagation)  
- ☐ Capital planning  
- ☐ Audit & accountability  
- ☐ System status  
- ☐ Intervention tracking  

Explain briefly how the component supports governance clarity.

---

## 5. Audience & Context

**Primary audience(s):**
- ☐ Operator  
- ☐ Department leadership  
- ☐ City executive  
- ☐ Public / resident  

**Where will this component appear?**
- ☐ Dashboards  
- ☐ Reports  
- ☐ City‑facing materials  
- ☐ Internal tools  

---

## 6. Data & Schema Mapping

**Which Global Index Schema fields does this component map to?**

_List exact schema paths (e.g., `scores.drift`, `capital.modernization_cycle`)._

If no direct mapping exists, explain why.

---

## 7. Variants & States

**Does this component require variants?**
- ☐ No  
- ☐ Yes (describe)

**Expected states:**
- ☐ Default  
- ☐ Active  
- ☐ Disabled  
- ☐ Warning / Error  
- ☐ Data unavailable  

---

## 8. Accessibility Considerations

Confirm that the component will:
- ☐ Meet contrast requirements  
- ☐ Not rely on color alone  
- ☐ Support keyboard navigation  
- ☐ Minimize motion  

---

## 9. Existing Component Review

**Have you reviewed the existing component library?**
- ☐ Yes  
- ☐ No  

List any similar components and explain why they are insufficient.

---

## 10. Risks & Tradeoffs

**What risks does this component introduce?**

- Semantic overlap  
- Increased complexity  
- Maintenance burden  
- Misinterpretation risk  

Explain how these risks are mitigated.

---

## 11. Review Checklist (For Steward Use)

- ☐ Naming convention compliant  
- ☐ Governance intent clear  
- ☐ Schema alignment confirmed  
- ☐ No duplication detected  
- ☐ Accessibility considered  

---

## 12. Approval Status

- **Design System Steward Review:** ☐ Approved ☐ Revisions Required  
- **Approval Date:**  
- **Notes:**

---

## 13. Canonical Status

Once approved:
- Component name is frozen  
- Purpose is canonical  
- Changes require a new proposal  

Unapproved components must not be created.

---

### Why this form matters

This proposal form ensures that:
- Components are intentional, not reactive  
- Meaning is reviewed before pixels are drawn  
- Governance clarity is preserved  
- The design system scales without entropy  
