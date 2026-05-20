# **Incident Substrate Model**  

- [`incident.module.json`](incident.module.json) — Agentic module schema role assignments

`/docs/Incident_Substrate_Model/README.md`

A calm, structured, grammar‑driven substrate for **incident ingestion, analysis, rectification planning, and operator‑approved remediation**.  
Designed for any GitHub repository — open or private — to adopt by adding a single JSON module file.

This module enables AI partners to:

- ingest public incident intelligence  
- classify the incident  
- map its surface area  
- derive rectification steps  
- generate a **read‑only remediation plan**  
- request operator approval  
- execute only **grammar‑bounded**, safe, deterministic actions  

No improvisation.  
No drift.  
No panic.  
Just **RECTIFY**.

---

## **How AI Should Use `incident.module.json` in This Repo**

AI partners must treat [`incident.module.json`](incident.module.json) as the **authoritative substrate** for all incident‑related activity in this repository. The file defines the allowed operators, analyzer layers, checks, fixes, and session rules. Models must follow these principles:

### **1. Read‑Only First Pass**  
AI must always begin in **read‑only mode**, using the module to:

- ingest public incident intel  
- classify the incident  
- map the potential surface area  
- derive rectification steps  
- generate a structured, operator‑reviewable plan  

No write actions are permitted until explicit operator approval.

### **2. Grammar‑Bounded Actions Only**  
All actions must use the operators defined in the module:

- `incident.ingest`  
- `incident.classify`  
- `incident.map_surface_area`  
- `incident.derive_rectification_steps`  
- `incident.generate_readonly_plan`  
- `incident.request_operator_approval`  
- `incident.execute.*` (only after approval)

Models must **never** invent new operators or perform actions outside the grammar.

### **3. Use the Checks and Fixes Exactly as Declared**  
AI must apply the `checks` array to evaluate the repository and propose rectification steps.  
AI must only propose or execute fixes listed under `fixes`:

- `remove`  
- `rotate`  
- `flag`  

No other fix types are allowed.

### **4. Operator Approval Is Mandatory**  
Before any write action (file removal, secret rotation, dependency patching), AI must:

- present the plan  
- request approval  
- wait for explicit confirmation  

### **5. Maintain Coherence and Avoid Drift**  
AI must adhere to the analyzer layers:

- **Regime:** incident  
- **Operator:** rectification  
- **Drift:** panic, improvisation  
- **Coherence:** structured, calm, deterministic  

All reasoning must remain within these boundaries.

---

## **6. Module Identity**

| Field | Value |
|------|--------|
| **Name** | Incident Substrate Model |
| **Category** | Safety / Operations |
| **Version** | 1.0.0 |
| **Purpose** | Provide a universal, grammar‑driven substrate for incident response |
| **Audience** | Repo maintainers, operators, AI partners |
| **Front Door** | This README |

---

## **7. Session Context**

This module uses the canonical TriadicFrameworks session‑context structure.

```html
<section class="session-context">
  <div class="context-label">Canon</div>
  <div class="context-value">RTT/1 — Operator‑Safe Incident Rectification</div>

  <div class="context-label">Modules</div>
  <div class="context-value">Incident Substrate Model</div>

  <div class="context-label">Drift</div>
  <div class="context-value">Panic, improvisation, unbounded actions</div>

  <div class="context-label">Coherence</div>
  <div class="context-value">Calm, structured, grammar‑driven remediation</div>

  <div class="context-label">Version</div>
  <div class="context-value">1.0.0</div>

  <div class="context-label">Format</div>
  <div class="context-value">Markdown + JSON substrate</div>

  <div class="context-label">Front door</div>
  <div class="context-value">/docs/Incident_Substrate_Model/README.md</div>

  <div class="context-label">Every page</div>
  <div class="context-value">Operator‑first, read‑only until approval</div>

  <div class="context-label">Audience</div>
  <div class="context-value">Repo maintainers, AI partners, security operators</div>
</section>
```

---

## **8. Concept Overview**

Incidents follow patterns.  
Rectification follows grammar.

This module defines:

- **how incidents are ingested**  
- **how surface area is mapped**  
- **how rectification steps are derived**  
- **how plans are generated**  
- **how operators approve**  
- **how AI executes bounded actions**  

The substrate ensures:

- no drift  
- no unsafe actions  
- no direct writes without approval  
- no hallucinated remediation  
- no improvisation  

Everything is **structured**, **deterministic**, and **operator‑safe**.

---

## **9. Operator Grammar**

These are the verbs and nouns the AI is allowed to use.

### **9.1 Incident Ingestion Operators**

| Operator | Description |
|---------|-------------|
| `incident.ingest` | Pull public intel (CVE, advisory, vendor post, trending event) |
| `incident.classify` | Determine incident type (supply‑chain, credential leak, dependency vuln, etc.) |
| `incident.map_surface_area` | Identify which repo components could be affected |

### **9.2 Rectification Planning Operators**

| Operator | Description |
|---------|-------------|
| `incident.derive_rectification_steps` | Convert intel → actionable steps |
| `incident.generate_readonly_plan` | Produce a structured, operator‑reviewable plan |
| `incident.flag_uncertainty` | Mark areas requiring human judgment |

### **9.3 Operator Approval Operators**

| Operator | Description |
|---------|-------------|
| `incident.request_operator_approval` | Present plan for review |
| `incident.hold_for_review` | Pause until operator input |

### **9.4 Bounded Execution Operators**

These are **never** executed without explicit operator approval.

| Operator | Description |
|---------|-------------|
| `incident.execute.remove_file` | Remove unsafe or accidental files |
| `incident.execute.rotate_secret` | Rotate compromised or risky credentials |
| `incident.execute.patch_dependency` | Apply dependency updates |
| `incident.execute.flag_for_followup` | Mark items requiring manual remediation |

---

## **10. Analyzer Layers**

The substrate uses RTT analyzer layers to maintain coherence.

| Layer | Purpose |
|-------|---------|
| **Regime** | Incident classification (supply‑chain, dependency, credential, etc.) |
| **Operator** | Defines allowed actions |
| **Drift** | Prevents panic, improvisation, unsafe automation |
| **Coherence** | Ensures structured, calm, deterministic remediation |
| **Cross‑cutting** | Repo safety, dependency safety, CI/CD safety |

---

## **11. Example `incident.module.json`**

This is the drop‑in file any repo can adopt.

```json
{
  "ai.module": "incident_substrate_model",
  "ai.version": "1.0.0",
  "ai.purpose": "Ingest incidents, derive rectification steps, generate read-only plans, execute bounded actions.",
  "analyzer_layer": {
    "regime": "incident",
    "operator": "rectification",
    "drift": "panic_improvisation",
    "coherence": "structured_calm_deterministic"
  },
  "checks": [
    { "id": "secret_scan", "pattern": ["API_KEY", "BEGIN RSA", ".env"] },
    { "id": "machine_artifacts", "pattern": [".DS_Store", ".vscode/settings.json"] },
    { "id": "infra_leak", "pattern": ["ssh", "server", "ip", "token"] },
    { "id": "private_notes", "pattern": ["TODO", "PRIVATE", "DRAFT"] }
  ],
  "fixes": {
    "remove": ["machine_artifacts"],
    "rotate": ["secret_scan"],
    "flag": ["private_notes", "infra_leak"]
  }
}
```

---

## **12. Example Workflow: How to RECTIFY an Incident**

### **Step 1 — Ingest**
AI pulls public intel:

- CVE  
- vendor advisory  
- GitHub security post  
- trending incident  

### **Step 2 — Classify**
AI determines:

- supply‑chain  
- dependency  
- credential  
- CI/CD  
- repo‑safety  

### **Step 3 — Map Surface Area**
AI identifies:

- affected files  
- affected dependencies  
- affected workflows  
- affected secrets  

### **Step 4 — Derive Rectification Steps**
AI converts intel → actions:

- remove file  
- rotate secret  
- update dependency  
- patch workflow  
- flag for review  

### **Step 5 — Generate Read‑Only Plan**
AI produces a structured plan:

- safe  
- calm  
- deterministic  
- operator‑reviewable  

### **Step 6 — Operator Approval**
You approve or modify.

### **Step 7 — Execute Bounded Actions**
AI performs only the approved actions.

---

## **13. Philosophy**

Incidents are inevitable.  
Scramble is optional.

The Incident Substrate Model replaces panic with:

- structure  
- grammar  
- clarity  
- safety  
- determinism  

This is how we RECTIFY.
