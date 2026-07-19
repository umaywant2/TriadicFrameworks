Incident_Substrate_Model 
# ⚠️ Incident Substrate Model  

- [`incident.module.json`](incident.module.json) — Agentic module schema role assignments

`/docs/Incident_Substrate_Model/README.md`

A calm, structured, grammar‑driven substrate for **incident ingestion, analysis, rectification planning, and operator‑approved remediation**.  
Designed for any GitHub repository — open or private — to adopt by adding a single JSON module file.

## 🛑 Important! 
Drift is On-by-Default long sessions lose anchors, turn off drift.

## ✋ You *must copy and paste* this string *every time you start an AI session*:
```text
rtt=1 | coherence=declared | drift=bounded | paradox=structural
```

## ❇️ Now you are ready.

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
---
title: "Incident Substrate Model"
description: "A grammar-driven substrate for calm, structured, deterministic incident ingestion, classification, and rectification."
stability: stable
date: 2026-07-14
section: core
rtt:
  coherence: declared
  drift: bounded
  paradox: structural
---

> ```
> rtt=1 | coherence=declared | drift=bounded | paradox=structural
> ```

## What Is the Incident Substrate Model?

The Incident Substrate Model (ISM) is a grammar-driven substrate for handling incidents
**calmly, structurally, and deterministically**. No drift. No improvisation. No panic.

ISM treats an incident not as an emergency but as a **substrate-level signal** — something
to ingest, classify, map, plan for, approve, and execute against in strict sequence.

---

## Seven Operators

| # | Operator | Function |
|---|----------|----------|
| 1 | `ingest` | Receive the raw incident signal |
| 2 | `classify` | Assign incident type and severity |
| 3 | `map_surface_area` | Identify the full affected substrate surface |
| 4 | `derive_rectification_steps` | Generate the ordered fix plan |
| 5 | `generate_readonly_plan` | Produce a read-only plan artifact for review |
| 6 | `request_operator_approval` | Gate on human approval before any action |
| 7 | `execute` | Apply the approved rectification steps |

---

## Three Fix Types

| Type | When Applied |
|------|-------------|
| **Remove** | Element is harmful and has no valid state |
| **Rotate** | Element is valid but in the wrong position or configuration |
| **Flag** | Element is ambiguous — mark for review without acting |

---

## Design Philosophy

ISM is built on three invariants:

- **Calm** — no urgency signals in the operator chain; urgency causes errors
- **Structured** — every action follows a declared grammar; no improvisation
- **Deterministic** — the same incident, ingested twice, produces the same plan

The `generate_readonly_plan` → `request_operator_approval` gate is non-negotiable.
No rectification step executes without explicit approval.

---

## Related Modules

- [Conditions Substrate Model](../Conditions_Substrate_Model/overview/) — maps the substrate conditions an incident disrupts
- [Governance Substrate Model](../Governance_Substrate_Model/overview/) — defines the approval authority structures ISM gates on
- [Structural Detection](../Structural_Detection/overview/) — detects the anomaly signals that become incident inputs
- [Opacity](../Opacity/overview/) — invisible substrate surfaces expand incident scope

---

v1.0 · Category: Safety / Operations · © 2026 Nawder Loswin · Byte Books Publishing
# **Browser UI Mockup — Incident Substrate Model**  
*TriadicFrameworks • Safety‑Operations • RTT/1*

A minimal, operator‑first UI mockup for interacting with the **Incident Substrate Model** inside a browser‑based environment.  
This mockup defines the **visual structure**, **interaction flow**, and **operator‑safe boundaries** for incident ingestion, classification, rectification planning, and approval.

This is a **UI‑level mockup**, not a functional implementation.

---

## **1. Purpose**

The Browser UI provides a calm, structured interface for:

- ingesting incident intel  
- reviewing classification  
- inspecting surface‑area mapping  
- reviewing the AI‑generated rectification plan  
- approving or rejecting bounded actions  
- tracking remediation status  

It ensures **operator control**, **zero drift**, and **read‑only first‑pass behavior**.

---

## **2. Layout Overview**

```
*
┌────────────────────────────────────────────────────────────────┐
│  ⚠️ Incident Substrate Model — Browser UI                      │
├────────────────────────────────────────────────────────────────┤
│  [Incident Source Input]   [Ingest Button]                     │
│                                                                │
│  ┌───────────────────────────────────────────────────────────┐ │
│  │ Incident Intel (Read‑Only)                                │ │
│  │ - CVE / Advisory / Vendor Post                            │ │
│  │ - Extracted Signals                                       │ │
│  │ - Relevant Vectors                                        │ │
│  └───────────────────────────────────────────────────────────┘ │
│                                                                │
│  ┌───────────────────────────────────────────────────────────┐ │
│  │ Classification                                            │ │
│  │ - Type: Supply‑Chain / Dependency / Credential / CI/CD    │ │
│  │ - Confidence Score                                        │ │
│  └───────────────────────────────────────────────────────────┘ │
│                                                                │
│  ┌───────────────────────────────────────────────────────────┐ │
│  │ Surface Area Mapping                                      │ │
│  │ - Files                                                   │ │
│  │ - Dependencies                                            │ │
│  │ - Workflows                                               │ │
│  │ - Secrets                                                 │ │
│  └───────────────────────────────────────────────────────────┘ │
│                                                                │
│  ┌───────────────────────────────────────────────────────────┐ │
│  │ Rectification Plan (Read‑Only)                            │ │
│  │ - Proposed Steps                                          │ │
│  │ - Uncertainties                                           │ │
│  │ - Required Operator Actions                               │ │
│  └───────────────────────────────────────────────────────────┘ │
│                                                                │
│  [Approve Plan]   [Reject Plan]   [Flag for Review]            │
└────────────────────────────────────────────────────────────────┘
```

---

## **3. Interaction Flow**

### **Step 1 — Ingest**
Operator provides:

- URL  
- CVE ID  
- advisory text  
- or raw intel  

AI performs:

- `incident.ingest`  
- `incident.classify`  
- `incident.map_surface_area`  

All results appear **read‑only**.

---

### **Step 2 — Review**
Operator reviews:

- extracted intel  
- classification  
- surface mapping  
- proposed rectification steps  

No actions are taken automatically.

---

### **Step 3 — Approve**
Operator selects:

- **Approve Plan** → AI may execute bounded actions  
- **Reject Plan** → AI halts  
- **Flag for Review** → AI marks uncertainties  

---

## **4. UI Panels**

### **4.1 Incident Intel Panel**
Displays:

- raw intel  
- extracted signals  
- relevant vectors  
- timestamps  
- source metadata  

Always **read‑only**.

---

### **4.2 Classification Panel**
Displays:

- incident type  
- confidence  
- supporting evidence  

---

### **4.3 Surface Area Mapping Panel**
Displays:

- affected files  
- affected dependencies  
- affected workflows  
- affected secrets  

---

### **4.4 Rectification Plan Panel**
Displays:

- proposed steps  
- uncertainties  
- operator actions required  

Always **read‑only** until approval.

---

## **5. Operator Controls**

| Control | Purpose |
|--------|---------|
| **Ingest** | Trigger incident ingestion + classification |
| **Approve Plan** | Allow bounded execution operators |
| **Reject Plan** | Cancel remediation |
| **Flag for Review** | Mark uncertainties or require human judgment |

---

## **6. Bounded Execution (Post‑Approval)**

If approved, AI may execute:

- `incident.execute.remove_file`  
- `incident.execute.rotate_secret`  
- `incident.execute.patch_dependency`  
- `incident.execute.flag_for_followup`  

All actions are logged in the UI.

---

## **7. Notes**

- No automatic writes  
- No unbounded actions  
- No improvisation  
- All steps are grammar‑locked  
- All actions require operator approval  

---

## **8. Status**

**Version:** 1.0.0  
**Module:** Incident Substrate Model  
**Category:** Safety‑Operations  
**Status:** Canon‑Stable  
# Incident Rectification Examples — Incident Substrate Model
**Document:** `incident_rectification_examples.md`
**Path:** `/docs/Incident_Substrate_Model/incident_rectification_examples.md`
**Revision:** RTT/1 · Canon Edition
**Status:** Normative Reference
**Issued:** 2026-05-20
**Depends on:** `operator_grammar.md`, `substrate_errors.md`, `operator_lifecycle.md`

---

## How to Read These Examples

Each example presents a complete ISM operator call trace for a real incident
class. Every call is rendered in the following format:

```
── OPERATOR: operator.name ─────────────────────────────────────
   @ 2026-05-20T07:04:11.203Z
   IN  { ... }
   OUT { ... }
   STATE: PRIOR_STATE → NEW_STATE
────────────────────────────────────────────────────────────────
```

Fields abbreviated for readability:
- UUIDs are shown as `<label:first-8>` — e.g., `<rec:a1f9c823>`.
- SHA-256 hashes are shown as `sha256:<first-16>...`.
- Raw payload bytes are shown as structured summaries, not raw binary.
- Approval resolution (human action) is shown as a `[APPROVAL EVENT]` block.
- Hold release (human action) is shown as a `[HOLD RELEASE EVENT]` block.

Annotations prefixed `※` reference specific sections of the companion
documents — e.g., `※ grammar §3.2` refers to `operator_grammar.md` Section 3.2.

---

## Example 1 — AWS Access Key Committed to Public GitHub Repository

**Incident class:** `SECRET_LEAK`
**Severity:** CRITICAL
**Outcome:** RESOLVED
**Lifecycle retention class:** CRITICAL (7 years)
**Operators exercised:** `ingest` · `classify` · `map_surface_area` ·
  `derive_rectification_steps` · `generate_readonly_plan` ·
  `request_operator_approval` · `execute.remove_file` · `execute.rotate_secret`

### Scenario

At 07:00 UTC a GitHub secret scanning webhook fires, reporting that commit
`e3fa9b2` to the public repository `acme-corp/payment-service` contains a
hardcoded AWS access key (`AKIA...`) with IAM administrator privileges. The
key is live and has not yet been used post-exposure. The file
`config/deploy.env` was pushed 4 minutes earlier. Time to remediation is
critical — every minute the key remains active is exploitable.

### Operator Call Trace

```
── OPERATOR: incident.ingest ────────────────────────────────────
   @ 2026-05-20T07:00:44.817Z
   IN  {
         signal_id    : <sig:f7a33b01-...>,
         source       : "github.secret-scanning.webhook",
         content_type : "application/json",
         emitted_at   : "2026-05-20T07:00:40.002Z",
         severity_hint: "CRITICAL",
         raw_payload  : {
           repository    : "acme-corp/payment-service",
           visibility    : "public",
           commit_sha    : "e3fa9b2c",
           file_path     : "config/deploy.env",
           secret_type   : "aws_access_key_id",
           secret_ref    : "AKIA4EXAMPLE7KEY23AB",
           pushed_at     : "2026-05-20T06:56:38.000Z",
           pusher         : "dev-bot@acme-corp.com",
           alert_url     : "https://github.com/acme-corp/payment-service/security/secret-scanning/alerts/142"
         }
       }
   OUT {
         record_id   : <rec:a1f9c823-...>,
         ingested_at : "2026-05-20T07:00:44.817Z",
         status      : "ACCEPTED"
       }
   STATE: (none) → INGESTED
────────────────────────────────────────────────────────────────

── OPERATOR: incident.classify ──────────────────────────────────
   @ 2026-05-20T07:00:45.102Z
   IN  {
         record_id     : <rec:a1f9c823-...>,
         classifier_id : "ism-classifier.secret-pattern-v4",
         category      : "SECRET_LEAK",
         subcategory   : "aws_access_key_id.iam_admin.public_vcs",
         confidence    : 0.98,
         rationale     : "GitHub secret scanning confirmed AWS IAM access key
                          pattern (AKIA prefix + 16-char alphanumeric) in a
                          public repository commit. Key type inferred as
                          aws_access_key_id. IAM privilege level not yet
                          confirmed — subcategory assumes admin pending
                          IAM policy lookup. Confidence 0.98: pattern match
                          is deterministic; privilege level is inferred."
       }
   OUT {
         record_id              : <rec:a1f9c823-...>,
         classification_version : 1,
         effective_at           : "2026-05-20T07:00:45.102Z"
       }
   STATE: INGESTED → CLASSIFIED
   ※ lifecycle §3.2 — ClassificationVersion 1 sealed; chain_hash[1] written
────────────────────────────────────────────────────────────────

── OPERATOR: incident.map_surface_area ──────────────────────────
   @ 2026-05-20T07:00:46.391Z
   IN  {
         record_id    : <rec:a1f9c823-...>,
         scanner_id   : "ism-scanner.github-surface-v2",
         surface_snapshot_hash : "sha256:c4f8a19d3e7b2f01...",
         surfaces     : [
           {
             surface_type : "FILE",
             surface_ref  : "github://acme-corp/payment-service@e3fa9b2c/config/deploy.env",
             access_mode  : "READ",
             confidence   : 0.99,
             notes        : "File containing the exposed secret. Present in git history.
                             Must be removed from HEAD and considered permanently
                             compromised in history — git history rewrite is out-of-scope
                             for ISM; flagged for follow-up."
           },
           {
             surface_type : "SECRET",
             surface_ref  : "aws://iam/access-key/AKIA4EXAMPLE7KEY23AB",
             access_mode  : "EXECUTE",
             confidence   : 0.98,
             notes        : "Live AWS IAM access key. Key ID confirmed via
                             pattern match. Associated IAM user: deploy-bot-prod.
                             Policy attachment: AdministratorAccess (inferred;
                             requires IAM lookup to confirm)."
           }
         ]
       }
   OUT {
         record_id      : <rec:a1f9c823-...>,
         surface_map_id : <smap:b3d72f00-...>,
         surface_count  : 2,
         mapped_at      : "2026-05-20T07:00:46.391Z"
       }
   STATE: CLASSIFIED → SURFACE_MAPPED
────────────────────────────────────────────────────────────────

── OPERATOR: incident.derive_rectification_steps ────────────────
   @ 2026-05-20T07:00:47.019Z
   IN  {
         record_id      : <rec:a1f9c823-...>,
         surface_map_id : <smap:b3d72f00-...>,
         planner_id     : "ism-planner.secret-leak-v3",
         steps          : [
           {
             step_index   : 0,
             operator_ref : "incident.execute.rotate_secret",
             target_ref   : "aws://iam/access-key/AKIA4EXAMPLE7KEY23AB",
             parameters   : {
               rotation_policy    : "IMMEDIATE",
               notify_dependents  : true
             },
             reversible   : false,
             rationale    : "Rotate the exposed IAM access key immediately to
                             invalidate the compromised credential. Executed
                             BEFORE file removal because key rotation closes
                             the active exploit window regardless of whether
                             the file is removed. Rotation is irreversible —
                             the old key cannot be restored."
           },
           {
             step_index   : 1,
             operator_ref : "incident.execute.remove_file",
             target_ref   : "github://acme-corp/payment-service@e3fa9b2c/config/deploy.env",
             parameters   : {
               dry_run  : false,
               checksum : "sha256:9b3ef12c7a480d9e..."
             },
             reversible   : false,
             rationale    : "Remove the file from HEAD to prevent further
                             exposure and satisfy the GitHub secret scanning
                             alert dismissal condition. Note: git history
                             retention is a separate concern — see follow-up
                             flag recommended in surface notes."
           }
         ]
       }
   OUT {
         record_id  : <rec:a1f9c823-...>,
         plan_id    : <plan:cc1d8855-...>,
         step_count : 2,
         derived_at : "2026-05-20T07:00:47.019Z"
       }
   STATE: SURFACE_MAPPED → PLAN_DERIVED
   ※ grammar §4 — step_index 0 = rotate_secret before remove_file;
     rotation closes exploit window faster than file removal alone
────────────────────────────────────────────────────────────────

── OPERATOR: incident.generate_readonly_plan ────────────────────
   @ 2026-05-20T07:00:47.340Z
   IN  {
         record_id : <rec:a1f9c823-...>,
         plan_id   : <plan:cc1d8855-...>,
         format    : "MARKDOWN"
       }
   OUT {
         record_id    : <rec:a1f9c823-...>,
         plan_id      : <plan:cc1d8855-...>,
         rendered_at  : "2026-05-20T07:00:47.340Z",
         rendered_plan: """
           ## Rectification Plan — <rec:a1f9c823>
           **Incident:** SECRET_LEAK · aws_access_key_id.iam_admin.public_vcs
           **Surface count:** 2  |  **Steps:** 2  |  **All steps irreversible**

           ### Step 0 — Rotate AWS IAM Access Key [IRREVERSIBLE]
           Operator : incident.execute.rotate_secret
           Target   : aws://iam/access-key/AKIA4EXAMPLE7KEY23AB
           Policy   : IMMEDIATE rotation
           Notifies : dependent consumers of deploy-bot-prod key
           Rationale: Closes the active exploit window before file removal.

           ### Step 1 — Remove Exposed File from Repository HEAD [IRREVERSIBLE]
           Operator  : incident.execute.remove_file
           Target    : github://acme-corp/payment-service@e3fa9b2c/config/deploy.env
           Checksum  : sha256:9b3ef12c7a480d9e...
           Rationale : Removes the file from HEAD; satisfies scanning alert.
                       ⚠ Git history rewrite not in scope — flag for follow-up.
         """
       }
   ※ grammar §4 — READONLY operator; no state change
────────────────────────────────────────────────────────────────

── OPERATOR: incident.request_operator_approval ─────────────────
   @ 2026-05-20T07:00:48.001Z
   IN  {
         record_id        : <rec:a1f9c823-...>,
         plan_id          : <plan:cc1d8855-...>,
         requesting_agent : "ism-planner.secret-leak-v3",
         approver_set     : ["security-oncall@acme-corp.com"],
         approval_policy  : "ANY_ONE",
         context_note     : "CRITICAL: live AWS admin key exposed in public repo
                             for 4 minutes. Step 0 (key rotation) is irreversible.
                             Step 1 (file removal) is irreversible. Recommend
                             immediate approval — every minute of delay is
                             exploitable. No blocking uncertainty flags."
       }
   OUT {
         record_id           : <rec:a1f9c823-...>,
         approval_request_id : <apr:d9e14c77-...>,
         requested_at        : "2026-05-20T07:00:48.001Z",
         approver_count      : 1
       }
   STATE: PLAN_DERIVED → PENDING_APPROVAL
────────────────────────────────────────────────────────────────

[APPROVAL EVENT]
   @ 2026-05-20T07:02:03.541Z
   approver     : "security-oncall@acme-corp.com"
   decision     : APPROVED
   approval_id  : <apr:d9e14c77-...>
   note         : "Confirmed. Key is live — rotate immediately."
   STATE: PENDING_APPROVAL → APPROVED
────────────────────────────────────────────────────────────────

── OPERATOR: incident.execute.rotate_secret ─────────────────────
   @ 2026-05-20T07:02:04.200Z   [step_index: 0]
   IN  {
         record_id         : <rec:a1f9c823-...>,
         plan_id           : <plan:cc1d8855-...>,
         step_index        : 0,
         secret_ref        : "aws://iam/access-key/AKIA4EXAMPLE7KEY23AB",
         rotation_policy   : "IMMEDIATE",
         notify_dependents : true
       }
   OUT {
         record_id          : <rec:a1f9c823-...>,
         execution_id       : <exec:e0011fa2-...>,
         status             : "ROTATED",
         new_secret_version : "v2-20260520T070204",
         rotated_at         : "2026-05-20T07:02:04.619Z"
       }
   STATE: APPROVED → EXECUTING
   ※ grammar §6 invariant 4 — new secret value not emitted in OUT
   ※ errors EXE-006 — dependent notification succeeded for 3 consumers
     (deploy-pipeline-prod, ci-runner-01, ci-runner-02)
────────────────────────────────────────────────────────────────

── OPERATOR: incident.execute.remove_file ───────────────────────
   @ 2026-05-20T07:02:05.014Z   [step_index: 1]
   IN  {
         record_id  : <rec:a1f9c823-...>,
         plan_id    : <plan:cc1d8855-...>,
         step_index : 1,
         file_path  : "github://acme-corp/payment-service@e3fa9b2c/config/deploy.env",
         checksum   : "sha256:9b3ef12c7a480d9e...",
         dry_run    : false
       }
   OUT {
         record_id      : <rec:a1f9c823-...>,
         execution_id   : <exec:e0022b14-...>,
         status         : "REMOVED",
         removed_at     : "2026-05-20T07:02:05.882Z",
         prior_checksum : "sha256:9b3ef12c7a480d9e..."
       }
   STATE: EXECUTING → RESOLVED
   ※ lifecycle §5.1 — archival triggered immediately (RESOLVED)
   ※ lifecycle §6.1 — RetentionClass: CRITICAL (SECRET_LEAK category)
────────────────────────────────────────────────────────────────
```

### Timeline Summary

| Time (UTC) | Event |
|---|---|
| 06:56:38 | Commit `e3fa9b2c` pushed to public repo — secret exposed |
| 07:00:40 | GitHub secret scanning fires webhook |
| 07:00:44 | `incident.ingest` — record created `<rec:a1f9c823>` |
| 07:00:47 | Plan derived — 2 steps, both irreversible |
| 07:00:48 | Approval requested to `security-oncall` |
| 07:02:03 | Approval granted — 75 seconds after request |
| 07:02:04 | Key rotated — exploit window closed |
| 07:02:05 | File removed from HEAD |
| 07:02:05 | Record → RESOLVED |
| **T+5m27s** | **Total time from exposure to key invalidation** |

### Post-Incident Notes

The git history for `acme-corp/payment-service` still contains commit `e3fa9b2c`
with the plaintext key. This is outside ISM's execution scope but is a genuine
residual risk. A `flag_for_followup` with `MANUAL_REMEDIATION_REQUIRED` and
`THIRD_PARTY_COORDINATION` (GitHub support BFG/history rewrite) should be
raised by the reviewing operator. RetentionClass `CRITICAL` means this record
is held for 7 years.

---

## Example 2 — Critical CVE in Transitive npm Dependency

**Incident class:** `DEPENDENCY_CVE`
**Severity:** HIGH
**Outcome:** RESOLVED (with open follow-up ticket)
**Lifecycle retention class:** STANDARD (2 years)
**Operators exercised:** `ingest` · `classify` · `flag_uncertainty` ·
  `map_surface_area` · `hold_for_review` · `derive_rectification_steps` ·
  `generate_readonly_plan` · `request_operator_approval` ·
  `execute.patch_dependency` · `execute.flag_for_followup`

### Scenario

At 08:30 UTC the ACME dependency scanning service reports that
`fast-xml-parser@4.2.4` — a transitive dependency pulled in by
`@acme/api-gateway@2.11.0` — is affected by CVE-2026-31814: a
prototype pollution vulnerability in the `parse()` method (CVSS 9.1).
The package appears in three production services. However, the scanner
also reports that one service (`legacy-ingest`) uses a custom fork of
`fast-xml-parser` at the same semver, pinned by a monorepo patch file.
The planner cannot confirm whether patching the standard package will
affect the fork — so an uncertainty flag is raised and a hold is
placed before planning proceeds.

### Operator Call Trace

```
── OPERATOR: incident.ingest ────────────────────────────────────
   @ 2026-05-20T08:30:12.004Z
   IN  {
         signal_id    : <sig:0be7d441-...>,
         source       : "acme.dep-scanner.snyk-bridge-v2",
         content_type : "application/json",
         emitted_at   : "2026-05-20T08:30:10.881Z",
         severity_hint: "HIGH",
         raw_payload  : {
           cve_id        : "CVE-2026-31814",
           cvss_score    : 9.1,
           cvss_vector   : "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:N",
           package       : "fast-xml-parser",
           affected_range: ">=4.0.0 <4.3.1",
           fix_version   : "4.3.1",
           vulnerability : "Prototype pollution in XMLParser.parse() via
                            crafted XML attribute names allows arbitrary
                            property injection on Object.prototype.",
           affected_services : [
             "api-gateway@2.11.0",
             "data-pipeline@1.8.3",
             "legacy-ingest@0.9.7 (FORKED — patch file detected)"
           ],
           scanner_confidence : 0.91
         }
       }
   OUT {
         record_id   : <rec:b2e05f11-...>,
         ingested_at : "2026-05-20T08:30:12.004Z",
         status      : "ACCEPTED"
       }
   STATE: (none) → INGESTED
────────────────────────────────────────────────────────────────

── OPERATOR: incident.classify ──────────────────────────────────
   @ 2026-05-20T08:30:12.441Z
   IN  {
         record_id     : <rec:b2e05f11-...>,
         classifier_id : "ism-classifier.cve-triage-v5",
         category      : "DEPENDENCY_CVE",
         subcategory   : "prototype-pollution.npm.transitive.multi-service",
         confidence    : 0.91,
         rationale     : "CVE-2026-31814 confirmed in NVD. CVSS 9.1 network-
                          exploitable prototype pollution. Affects 3 production
                          services via transitive dependency chain. Confidence
                          0.91: scanner reported a forked variant in
                          legacy-ingest that may behave differently — this
                          reduces classification certainty for that service."
       }
   OUT {
         record_id              : <rec:b2e05f11-...>,
         classification_version : 1,
         effective_at           : "2026-05-20T08:30:12.441Z"
       }
   STATE: INGESTED → CLASSIFIED
────────────────────────────────────────────────────────────────

── OPERATOR: incident.flag_uncertainty ──────────────────────────
   @ 2026-05-20T08:30:12.709Z
   IN  {
         record_id        : <rec:b2e05f11-...>,
         flagging_agent   : "ism-classifier.cve-triage-v5",
         uncertainty_code : "SURFACE_INCOMPLETE",
         affected_field   : "surfaces[legacy-ingest]",
         detail           : "Scanner detected a monorepo patch file
                             (patches/fast-xml-parser+4.2.4.patch) in the
                             legacy-ingest service tree. This patch modifies
                             the XMLParser.parse() method — the same code path
                             affected by CVE-2026-31814. It is unknown whether
                             the patch inadvertently mitigates the vulnerability
                             or introduces a variant. Standard fast-xml-parser
                             patch steps may not apply to this fork. Surface
                             mapping and planning for legacy-ingest should
                             proceed with reduced confidence until the patch
                             file is reviewed by a Node.js security engineer."
       }
   OUT {
         record_id  : <rec:b2e05f11-...>,
         flag_id    : <unc:f9901c44-...>,
         flagged_at : "2026-05-20T08:30:12.709Z"
       }
   ※ grammar §4 — no state transition; annotation only
   ※ errors UNC-001, UNC-002 — not triggered; code and detail are valid
────────────────────────────────────────────────────────────────

── OPERATOR: incident.map_surface_area ──────────────────────────
   @ 2026-05-20T08:30:13.100Z
   IN  {
         record_id    : <rec:b2e05f11-...>,
         scanner_id   : "ism-scanner.npm-dep-v3",
         surface_snapshot_hash : "sha256:77d3b201f9e84abc...",
         surfaces     : [
           {
             surface_type : "DEPENDENCY",
             surface_ref  : "npm:fast-xml-parser@4.2.4",
             access_mode  : "EXECUTE",
             confidence   : 0.99,
             notes        : "Canonical package from npm registry. Affects
                             api-gateway and data-pipeline. Upgrade target:
                             4.3.1 (first patched release per NVD advisory)."
           },
           {
             surface_type : "DEPENDENCY",
             surface_ref  : "npm:fast-xml-parser@4.2.4#legacy-ingest-fork",
             access_mode  : "EXECUTE",
             confidence   : 0.61,
             notes        : "Forked variant in legacy-ingest service via
                             patch file. Behaviour under CVE-2026-31814
                             is unverified. Flagged SURFACE_INCOMPLETE.
                             Standard patch steps may not apply."
           }
         ]
       }
   OUT {
         record_id      : <rec:b2e05f11-...>,
         surface_map_id : <smap:c4a19d02-...>,
         surface_count  : 2,
         mapped_at      : "2026-05-20T08:30:13.100Z"
       }
   STATE: CLASSIFIED → SURFACE_MAPPED
────────────────────────────────────────────────────────────────

── OPERATOR: incident.hold_for_review ───────────────────────────
   @ 2026-05-20T08:30:14.002Z
   IN  {
         record_id    : <rec:b2e05f11-...>,
         held_by      : "ism-planner.cve-response-v2",
         reason_code  : "BLOCKING_UNCERTAINTY",
         detail       : "Surface map contains a forked dependency entry
                         (npm:fast-xml-parser@4.2.4#legacy-ingest-fork)
                         with confidence 0.61. Standard patch_dependency
                         steps cannot safely be applied to the fork without
                         manual review of patches/fast-xml-parser+4.2.4.patch.
                         Hold placed until a Node.js security engineer confirms
                         whether the patch mitigates or modifies the CVE-2026-31814
                         attack surface. Estimated review time: 2-4 hours."
         resume_after : "2026-05-20T10:30:00.000Z"
       }
   OUT {
         record_id   : <rec:b2e05f11-...>,
         hold_id     : <hold:a3312e88-...>,
         held_at     : "2026-05-20T08:30:14.002Z",
         prior_state : "SURFACE_MAPPED"
       }
   STATE: SURFACE_MAPPED → HOLD
   ※ lifecycle §4 — hold preserves prior_state for restoration on release
────────────────────────────────────────────────────────────────

[HOLD RELEASE EVENT]
   @ 2026-05-20T10:17:33.009Z
   released_by  : "sri.kumar@acme-corp.com"
   hold_id      : <hold:a3312e88-...>
   finding      : "Patch file reviewed. It modifies XML attribute escaping,
                   not the parse() code path. The fork IS vulnerable to
                   CVE-2026-31814. However, the patch conflicts with the
                   4.3.1 upgrade — the patch must be removed or ported
                   before the standard upgrade can be applied. Recommend:
                   patch standard services now; flag legacy-ingest for
                   manual remediation by the legacy team."
   STATE: HOLD → SURFACE_MAPPED
────────────────────────────────────────────────────────────────

── OPERATOR: incident.derive_rectification_steps ────────────────
   @ 2026-05-20T10:17:45.881Z
   IN  {
         record_id      : <rec:b2e05f11-...>,
         surface_map_id : <smap:c4a19d02-...>,
         planner_id     : "ism-planner.cve-response-v2",
         steps          : [
           {
             step_index   : 0,
             operator_ref : "incident.execute.patch_dependency",
             target_ref   : "npm:fast-xml-parser@4.2.4",
             parameters   : {
               current_version  : "4.2.4",
               target_version   : "4.3.1",
               package_manager  : "NPM",
               verify_checksum  : "sha256:4e9f301ab72cd5f8...",
               dry_run          : false
             },
             reversible   : true,
             rationale    : "Patch canonical fast-xml-parser in api-gateway
                             and data-pipeline from 4.2.4 to 4.3.1. This is
                             the NVD-confirmed patched version. Checksum
                             verified against npm registry integrity field."
           },
           {
             step_index   : 1,
             operator_ref : "incident.execute.flag_for_followup",
             target_ref   : "npm:fast-xml-parser@4.2.4#legacy-ingest-fork",
             parameters   : {
               followup_code : "MANUAL_REMEDIATION_REQUIRED",
               priority      : "HIGH",
               assigned_to   : ["legacy-team@acme-corp.com",
                                "sri.kumar@acme-corp.com"],
               due_by        : "2026-05-27T17:00:00.000Z"
             },
             reversible   : true,
             rationale    : "The forked dependency in legacy-ingest requires
                             patch file removal or porting before the 4.3.1
                             upgrade can be applied. This cannot be automated
                             safely — the patch author must assess compatibility."
           }
         ]
       }
   OUT {
         record_id  : <rec:b2e05f11-...>,
         plan_id    : <plan:dd2e9a03-...>,
         step_count : 2,
         derived_at : "2026-05-20T10:17:45.881Z"
       }
   STATE: SURFACE_MAPPED → PLAN_DERIVED
────────────────────────────────────────────────────────────────

── OPERATOR: incident.generate_readonly_plan ────────────────────
   @ 2026-05-20T10:17:46.201Z
   IN  { record_id: <rec:b2e05f11-...>, plan_id: <plan:dd2e9a03-...>, format: "MARKDOWN" }
   OUT {
         rendered_plan: """
           ## Rectification Plan — <rec:b2e05f11>
           **Incident:** DEPENDENCY_CVE · CVE-2026-31814 (CVSS 9.1)
           **Surface count:** 2  |  **Steps:** 2
           ⚠ Open uncertainty flag: SURFACE_INCOMPLETE on legacy-ingest fork

           ### Step 0 — Patch fast-xml-parser to 4.3.1 [REVERSIBLE]
           Operator  : incident.execute.patch_dependency
           Target    : npm:fast-xml-parser@4.2.4 (api-gateway, data-pipeline)
           From      : 4.2.4  →  To: 4.3.1
           Checksum  : sha256:4e9f301ab72cd5f8...
           Rationale : NVD-confirmed patched version. Checksum verified.

           ### Step 1 — Flag legacy-ingest fork for manual remediation [flag_for_followup]
           Operator  : incident.execute.flag_for_followup
           Target    : npm:fast-xml-parser@4.2.4#legacy-ingest-fork
           Code      : MANUAL_REMEDIATION_REQUIRED
           Priority  : HIGH
           Assigned  : legacy-team, sri.kumar
           Due       : 2026-05-27T17:00:00Z
           Rationale : Fork incompatible with automated patch; requires
                       manual patch file review and upgrade.
         """
       }
────────────────────────────────────────────────────────────────

── OPERATOR: incident.request_operator_approval ─────────────────
   @ 2026-05-20T10:17:47.003Z
   IN  {
         record_id        : <rec:b2e05f11-...>,
         plan_id          : <plan:dd2e9a03-...>,
         requesting_agent : "ism-planner.cve-response-v2",
         approver_set     : ["security-oncall@acme-corp.com",
                             "sri.kumar@acme-corp.com"],
         approval_policy  : "ANY_ONE",
         context_note     : "ACKNOWLEDGED: <unc:f9901c44> — SURFACE_INCOMPLETE
                             on legacy-ingest fork. Confirmed by sri.kumar at
                             10:17Z: fork is vulnerable but incompatible with
                             automated patch. Step 1 (flag_for_followup) closes
                             the automated scope; legacy team handles manually.
                             Step 0 is safe to proceed immediately."
       }
   OUT {
         record_id           : <rec:b2e05f11-...>,
         approval_request_id : <apr:e3f20b55-...>,
         requested_at        : "2026-05-20T10:17:47.003Z",
         approver_count      : 2
       }
   STATE: PLAN_DERIVED → PENDING_APPROVAL
   ※ grammar §5 — uncertainty flag acknowledged in context_note; GUARD passes
────────────────────────────────────────────────────────────────

[APPROVAL EVENT]
   @ 2026-05-20T10:19:02.771Z
   approver  : "security-oncall@acme-corp.com"
   decision  : APPROVED
   note      : "Plan looks correct. Proceed with step 0; legacy team owns step 1."
   STATE: PENDING_APPROVAL → APPROVED
────────────────────────────────────────────────────────────────

── OPERATOR: incident.execute.patch_dependency ──────────────────
   @ 2026-05-20T10:19:03.401Z   [step_index: 0]
   IN  {
         record_id       : <rec:b2e05f11-...>,
         plan_id         : <plan:dd2e9a03-...>,
         step_index      : 0,
         package_ref     : "npm:fast-xml-parser@4.2.4",
         current_version : "4.2.4",
         target_version  : "4.3.1",
         package_manager : "NPM",
         verify_checksum : "sha256:4e9f301ab72cd5f8...",
         dry_run         : false
       }
   OUT {
         record_id       : <rec:b2e05f11-...>,
         execution_id    : <exec:f0133d66-...>,
         status          : "PATCHED",
         patched_version : "4.3.1",
         patched_at      : "2026-05-20T10:19:09.204Z"
       }
   STATE: APPROVED → EXECUTING
   ※ errors EXE-008 — not triggered; current_version matched installed version
   ※ errors EXE-010 — not triggered; npm install exited 0
────────────────────────────────────────────────────────────────

── OPERATOR: incident.execute.flag_for_followup ─────────────────
   @ 2026-05-20T10:19:10.001Z   [step_index: 1]
   IN  {
         record_id     : <rec:b2e05f11-...>,
         plan_id       : <plan:dd2e9a03-...>,
         step_index    : 1,
         target_ref    : "npm:fast-xml-parser@4.2.4#legacy-ingest-fork",
         followup_code : "MANUAL_REMEDIATION_REQUIRED",
         priority      : "HIGH",
         assigned_to   : ["legacy-team@acme-corp.com", "sri.kumar@acme-corp.com"],
         due_by        : "2026-05-27T17:00:00.000Z",
         detail        : "The legacy-ingest service uses a patched fork of
                          fast-xml-parser@4.2.4 via monorepo patch file
                          patches/fast-xml-parser+4.2.4.patch. The fork IS
                          vulnerable to CVE-2026-31814 (confirmed by sri.kumar
                          2026-05-20T10:17Z). Standard npm upgrade to 4.3.1
                          conflicts with the patch file — the patch must be
                          removed or ported before upgrading. Assigned to
                          the legacy-ingest team with HIGH priority and a
                          7-day SLA. ISM record: <rec:b2e05f11>."
       }
   OUT {
         record_id    : <rec:b2e05f11-...>,
         execution_id : <exec:f0244e77-...>,
         followup_id  : <fup:g1355f88-...>,
         status       : "FLAGGED",
         flagged_at   : "2026-05-20T10:19:10.441Z"
       }
   STATE: EXECUTING → RESOLVED
   ※ lifecycle §5.1 — RetentionClass: STANDARD (DEPENDENCY_CVE)
   ※ lifecycle §6.1 — open FollowupTicket <fup:g1355f88> blocks expiry
     until ticket is CLOSED
────────────────────────────────────────────────────────────────
```

### Timeline Summary

| Time (UTC) | Event |
|---|---|
| 08:30:10 | Scanner detects CVE-2026-31814 in fast-xml-parser@4.2.4 |
| 08:30:12 | Record created; classified; uncertainty flag raised |
| 08:30:14 | Hold placed — fork analysis required |
| 10:17:33 | Hold released — sri.kumar confirms fork is vulnerable, patch incompatible |
| 10:17:47 | Approval requested with uncertainty acknowledgment |
| 10:19:02 | Approved |
| 10:19:09 | Canonical package patched to 4.3.1 across api-gateway, data-pipeline |
| 10:19:10 | Legacy-ingest fork flagged for follow-up; assigned to legacy team |
| 10:19:10 | Record → RESOLVED (with open follow-up ticket) |

---

## Example 3 — Publicly Accessible GCS Bucket Containing PII Export Files

**Incident class:** `MISCONFIGURATION`
**Severity:** HIGH
**Outcome:** RESOLVED (all steps via flag_for_followup — infra change required)
**Lifecycle retention class:** STANDARD (2 years)
**Operators exercised:** `ingest` · `classify` · `map_surface_area` ·
  `flag_uncertainty` · `derive_rectification_steps` ·
  `generate_readonly_plan` · `request_operator_approval` ·
  `execute.flag_for_followup` × 2

### Scenario

At 10:00 UTC ACME's cloud posture scanner reports that the GCS bucket
`acme-analytics-exports-prod` has `allUsers` read access on its IAM policy
— making all objects publicly accessible on the internet. The bucket
contains daily PII export files (customer email lists, order summaries)
generated by the analytics pipeline. The misconfiguration has been present
for 11 days based on Cloud Audit Logs. Because fixing a GCS IAM policy
and auditing data exposure are Terraform-managed infra operations, the ISM
cannot apply the fix directly — both steps must be flagged for manual
remediation.

### Operator Call Trace

```
── OPERATOR: incident.ingest ────────────────────────────────────
   @ 2026-05-20T10:00:07.312Z
   IN  {
         signal_id    : <sig:1cf8e552-...>,
         source       : "acme.cloud-posture.cspm-v3",
         content_type : "application/json",
         emitted_at   : "2026-05-20T10:00:05.100Z",
         severity_hint: "HIGH",
         raw_payload  : {
           provider         : "gcp",
           resource_type    : "storage.googleapis.com/Bucket",
           resource_name    : "acme-analytics-exports-prod",
           finding          : "PUBLIC_BUCKET_ACL",
           policy_member    : "allUsers",
           policy_role      : "roles/storage.objectViewer",
           object_count     : 847,
           estimated_pii    : true,
           first_seen       : "2026-05-09T00:00:00.000Z",
           exposure_days    : 11,
           object_prefixes  : ["daily-exports/", "customer-lists/", "order-summaries/"],
           terraform_managed: true,
           tf_resource_path : "infra/gcp/storage/analytics-exports.tf"
         }
       }
   OUT {
         record_id   : <rec:c3f17a22-...>,
         ingested_at : "2026-05-20T10:00:07.312Z",
         status      : "ACCEPTED"
       }
   STATE: (none) → INGESTED
────────────────────────────────────────────────────────────────

── OPERATOR: incident.classify ──────────────────────────────────
   @ 2026-05-20T10:00:07.801Z
   IN  {
         record_id     : <rec:c3f17a22-...>,
         classifier_id : "ism-classifier.cloud-posture-v3",
         category      : "MISCONFIGURATION",
         subcategory   : "gcs.public_acl.pii_exposure.terraform_managed",
         confidence    : 0.96,
         rationale     : "Cloud posture scanner confirmed GCS bucket with
                          allUsers:objectViewer binding. Bucket contains
                          object prefixes consistent with PII exports (daily-
                          exports/, customer-lists/). Exposure confirmed for
                          11 days via Cloud Audit Logs. Classified as
                          MISCONFIGURATION because the root cause is an
                          IAM policy error, not a data exfiltration event.
                          DATA_EXPOSURE not used: no confirmed exfil event —
                          public accessibility ≠ confirmed access by
                          unauthorized parties. Confidence 0.96."
       }
   OUT {
         record_id              : <rec:c3f17a22-...>,
         classification_version : 1,
         effective_at           : "2026-05-20T10:00:07.801Z"
       }
   STATE: INGESTED → CLASSIFIED
────────────────────────────────────────────────────────────────

── OPERATOR: incident.map_surface_area ──────────────────────────
   @ 2026-05-20T10:00:08.441Z
   IN  {
         record_id    : <rec:c3f17a22-...>,
         scanner_id   : "ism-scanner.gcp-iam-v2",
         surface_snapshot_hash : "sha256:8ef4d309a1b7c24f...",
         surfaces     : [
           {
             surface_type : "CONFIG",
             surface_ref  : "gcp://storage/buckets/acme-analytics-exports-prod/iam-policy",
             access_mode  : "WRITE",
             confidence   : 0.99,
             notes        : "GCS bucket IAM policy containing allUsers:objectViewer.
                             Managed by Terraform resource
                             google_storage_bucket_iam_member in
                             infra/gcp/storage/analytics-exports.tf.
                             Fix requires Terraform plan+apply by the infra team.
                             ISM cannot apply GCP IAM mutations directly."
           },
           {
             surface_type : "SERVICE",
             surface_ref  : "gcp://storage/buckets/acme-analytics-exports-prod",
             access_mode  : "READ",
             confidence   : 0.99,
             notes        : "The bucket itself and its 847 objects (daily-exports/,
                             customer-lists/, order-summaries/) were publicly
                             readable for ~11 days. An access log audit is
                             required to determine whether unauthorized reads
                             occurred. Audit must be performed by the data
                             privacy team via Cloud Audit Log export."
           }
         ]
       }
   OUT {
         record_id      : <rec:c3f17a22-...>,
         surface_map_id : <smap:d5b28e13-...>,
         surface_count  : 2,
         mapped_at      : "2026-05-20T10:00:08.441Z"
       }
   STATE: CLASSIFIED → SURFACE_MAPPED
────────────────────────────────────────────────────────────────

── OPERATOR: incident.flag_uncertainty ──────────────────────────
   @ 2026-05-20T10:00:08.712Z
   IN  {
         record_id        : <rec:c3f17a22-...>,
         flagging_agent   : "ism-classifier.cloud-posture-v3",
         uncertainty_code : "EXTERNAL_DEPENDENCY_UNKNOWN",
         affected_field   : "surfaces[gcp://storage/buckets/.../iam-policy]",
         detail           : "The IAM policy is managed by Terraform. The
                             ISM execute.* operators cannot apply Terraform
                             plan+apply cycles — this requires GCP credentials
                             with Terraform state access and an infra team
                             approval workflow external to ISM. The estimated
                             time for infra team to apply the fix is unknown;
                             SLA depends on oncall rotation. Classification
                             as EXTERNAL_DEPENDENCY_UNKNOWN because remediation
                             depends on third-party (infra team) execution
                             of a non-automated workflow."
       }
   OUT {
         record_id  : <rec:c3f17a22-...>,
         flag_id    : <unc:h0012d55-...>,
         flagged_at : "2026-05-20T10:00:08.712Z"
       }
   ※ grammar §4 — annotation only; no state transition
────────────────────────────────────────────────────────────────

── OPERATOR: incident.derive_rectification_steps ────────────────
   @ 2026-05-20T10:00:09.200Z
   IN  {
         record_id      : <rec:c3f17a22-...>,
         surface_map_id : <smap:d5b28e13-...>,
         planner_id     : "ism-planner.misconfiguration-v2",
         steps          : [
           {
             step_index   : 0,
             operator_ref : "incident.execute.flag_for_followup",
             target_ref   : "gcp://storage/buckets/acme-analytics-exports-prod/iam-policy",
             parameters   : {
               followup_code : "MANUAL_REMEDIATION_REQUIRED",
               priority      : "CRITICAL",
               assigned_to   : ["infra-oncall@acme-corp.com"],
               due_by        : "2026-05-20T14:00:00.000Z"
             },
             reversible   : true,
             rationale    : "Remove allUsers:objectViewer from the GCS bucket
                             IAM policy via Terraform. This is a Terraform-
                             managed resource — infra team must run plan+apply.
                             Priority CRITICAL: PII exposure is live. Due by
                             14:00Z today (4-hour SLA)."
           },
           {
             step_index   : 1,
             operator_ref : "incident.execute.flag_for_followup",
             target_ref   : "gcp://storage/buckets/acme-analytics-exports-prod",
             parameters   : {
               followup_code : "THIRD_PARTY_COORDINATION",
               priority      : "HIGH",
               assigned_to   : ["privacy-team@acme-corp.com", "legal@acme-corp.com"],
               due_by        : "2026-05-27T17:00:00.000Z"
             },
             reversible   : true,
             rationale    : "Export Cloud Audit Logs for the bucket covering
                             the 11-day exposure window (2026-05-09 to 2026-05-20).
                             Determine whether unauthorized parties accessed
                             any PII objects. If confirmed access occurred,
                             data breach notification obligations may apply
                             (GDPR Art. 33, CCPA). Legal team coordination
                             required. ISM cannot perform this audit."
           }
         ]
       }
   OUT {
         record_id  : <rec:c3f17a22-...>,
         plan_id    : <plan:ee3fa114-...>,
         step_count : 2,
         derived_at : "2026-05-20T10:00:09.200Z"
       }
   STATE: SURFACE_MAPPED → PLAN_DERIVED
────────────────────────────────────────────────────────────────

── OPERATOR: incident.request_operator_approval ─────────────────
   @ 2026-05-20T10:00:10.001Z
   IN  {
         record_id        : <rec:c3f17a22-...>,
         plan_id          : <plan:ee3fa114-...>,
         requesting_agent : "ism-planner.misconfiguration-v2",
         approver_set     : ["security-oncall@acme-corp.com",
                             "privacy-team@acme-corp.com"],
         approval_policy  : "ALL",
         context_note     : "ACKNOWLEDGED: <unc:h0012d55> — EXTERNAL_DEPENDENCY_UNKNOWN
                             (Terraform-managed policy). Plan is entirely via
                             flag_for_followup — no automated mutations.
                             Requires ALL approvers: security-oncall for infra
                             SLA, privacy-team for audit scope. PII exposure
                             has been live for 11 days — treat as urgent."
       }
   OUT {
         record_id           : <rec:c3f17a22-...>,
         approval_request_id : <apr:ff4gb225-...>,
         requested_at        : "2026-05-20T10:00:10.001Z",
         approver_count      : 2
       }
   STATE: PLAN_DERIVED → PENDING_APPROVAL
────────────────────────────────────────────────────────────────

[APPROVAL EVENT]
   @ 2026-05-20T10:04:41.001Z   approver: "security-oncall@acme-corp.com"
   decision : APPROVED
[APPROVAL EVENT]
   @ 2026-05-20T10:06:17.882Z   approver: "privacy-team@acme-corp.com"
   decision : APPROVED  |  note: "Legal notified. Starting audit log export now."
   STATE: PENDING_APPROVAL → APPROVED  (ALL policy satisfied)
────────────────────────────────────────────────────────────────

── OPERATOR: incident.execute.flag_for_followup ─────────────────
   @ 2026-05-20T10:06:18.500Z   [step_index: 0]
   IN  {
         record_id     : <rec:c3f17a22-...>,
         plan_id       : <plan:ee3fa114-...>,
         step_index    : 0,
         target_ref    : "gcp://storage/buckets/acme-analytics-exports-prod/iam-policy",
         followup_code : "MANUAL_REMEDIATION_REQUIRED",
         priority      : "CRITICAL",
         assigned_to   : ["infra-oncall@acme-corp.com"],
         due_by        : "2026-05-20T14:00:00.000Z",
         detail        : "Remove allUsers:roles/storage.objectViewer from
                          the IAM policy of GCS bucket acme-analytics-exports-prod.
                          Resource is managed by google_storage_bucket_iam_member
                          in infra/gcp/storage/analytics-exports.tf. Run:
                          terraform plan -target=module.analytics_exports.
                          google_storage_bucket_iam_member.public_reader
                          then apply after review. CRITICAL priority: live
                          PII exposure. SLA: 14:00Z today. ISM record:
                          <rec:c3f17a22>. Verification: re-run CSPM check
                          after apply to confirm finding is resolved."
       }
   OUT {
         record_id    : <rec:c3f17a22-...>,
         execution_id : <exec:g1244f99-...>,
         followup_id  : <fup:h2355g00-...>,
         status       : "FLAGGED",
         flagged_at   : "2026-05-20T10:06:18.901Z"
       }
   STATE: APPROVED → EXECUTING
────────────────────────────────────────────────────────────────

── OPERATOR: incident.execute.flag_for_followup ─────────────────
   @ 2026-05-20T10:06:19.200Z   [step_index: 1]
   IN  {
         record_id     : <rec:c3f17a22-...>,
         plan_id       : <plan:ee3fa114-...>,
         step_index    : 1,
         target_ref    : "gcp://storage/buckets/acme-analytics-exports-prod",
         followup_code : "THIRD_PARTY_COORDINATION",
         priority      : "HIGH",
         assigned_to   : ["privacy-team@acme-corp.com", "legal@acme-corp.com"],
         due_by        : "2026-05-27T17:00:00.000Z",
         detail        : "Export and analyze Cloud Audit Logs (data_access logs)
                          for bucket acme-analytics-exports-prod covering
                          2026-05-09T00:00Z through 2026-05-20T10:00Z (11-day
                          exposure window). Identify all GetObject/ListObjects
                          requests from non-ACME principals (filter: NOT
                          protoPayload.authenticationInfo.principalEmail
                          CONTAINS acme-corp.com). If any unauthorized reads
                          are confirmed: (1) notify DPO within 24h;
                          (2) assess GDPR Art. 33 72-hour notification
                          threshold; (3) engage legal for CCPA obligations.
                          Coordinate with Google Workspace Admin for log
                          export if audit log retention window is at risk.
                          ISM record: <rec:c3f17a22>."
       }
   OUT {
         record_id    : <rec:c3f17a22-...>,
         execution_id : <exec:g1355h11-...>,
         followup_id  : <fup:h3466i12-...>,
         status       : "FLAGGED",
         flagged_at   : "2026-05-20T10:06:19.598Z"
       }
   STATE: EXECUTING → RESOLVED
   ※ lifecycle §6.1 — 2 open FollowupTickets block expiry until CLOSED
────────────────────────────────────────────────────────────────
```

### Key Design Point

This example illustrates ISM used entirely as a **coordination and audit
layer** rather than an execution layer. Neither step mutates any target —
both are `flag_for_followup`. The record still reaches `RESOLVED` because
all plan steps are `STEP_EXECUTED` (status `FLAGGED` counts). The ISM
record now serves as the authoritative paper trail binding the incident
to two downstream work items owned by infra and privacy teams.

---

## Example 4 — Compromised GCP Service Account Key with Vault Rotation Failure

**Incident class:** `UNAUTHORIZED_ACCESS`
**Severity:** CRITICAL
**Outcome (parent):** FAULTED
**Outcome (child):** RESOLVED
**Lifecycle — parent:** CRITICAL retention · FAULT_ARCHIVAL_DELAY (24h)
**Lifecycle — child:** CRITICAL retention · SPAWNED_FROM lineage depth 1
**Operators exercised (parent):** `ingest` · `classify` · `map_surface_area` ·
  `derive_rectification_steps` · `generate_readonly_plan` ·
  `request_operator_approval` · `execute.rotate_secret` → **PARTIAL_EXECUTION**
**Operators exercised (child):** `ingest` (SPAWNED_FROM) · `classify` ·
  `map_surface_area` · `derive_rectification_steps` ·
  `request_operator_approval` · `execute.rotate_secret` ·
  `execute.flag_for_followup`

### Scenario

At 11:15 UTC ACME's SIEM fires on an anomalous authentication pattern:
a GCP service account key for `data-export-sa@acme-prod.iam.gserviceaccount.com`
is being used from an IP address in eastern Europe not associated with
any known ACME infrastructure. The key was last rotated 6 months ago.
The ISM initiates rotation through HashiCorp Vault's GCP secrets engine.
Rotation begins but the Vault GCP secrets engine returns an error mid-rotation
— the old key version is deactivated, but the new key version is never
written to Vault. The substrate detects this ambiguous state and emits
`PARTIAL_EXECUTION`, transitioning the parent record to `FAULTED`. A child
record is spawned to complete remediation safely.

### Operator Call Trace — Parent Record `<rec:d4g28b33>`

```
── OPERATOR: incident.ingest ────────────────────────────────────
   @ 2026-05-20T11:15:09.004Z
   IN  {
         signal_id    : <sig:2df9f663-...>,
         source       : "acme.siem.splunk-alert-bridge",
         content_type : "application/json",
         emitted_at   : "2026-05-20T11:15:07.112Z",
         severity_hint: "CRITICAL",
         raw_payload  : {
           alert_id      : "SPLUNK-2026-0914",
           alert_type    : "ANOMALOUS_SA_KEY_USAGE",
           service_account: "data-export-sa@acme-prod.iam.gserviceaccount.com",
           key_id        : "projects/acme-prod/serviceAccounts/data-export-sa@acme-prod.iam.gserviceaccount.com/keys/8f3a21bc...",
           anomaly        : "Authentication from 185.220.101.47 (Tor exit node)",
           last_normal_ip : "34.102.136.0/24 (GCP us-central1)",
           key_age_days   : 183,
           api_calls_last_1h : [
             "storage.objects.list on acme-prod-data-lake",
             "bigquery.tables.getData on acme-prod.analytics.*",
             "iam.serviceAccounts.list"
           ],
           vault_secret_path : "gcp/key/data-export-sa"
         }
       }
   OUT {
         record_id   : <rec:d4g28b33-...>,
         ingested_at : "2026-05-20T11:15:09.004Z",
         status      : "ACCEPTED"
       }
   STATE: (none) → INGESTED
────────────────────────────────────────────────────────────────

── OPERATOR: incident.classify ──────────────────────────────────
   @ 2026-05-20T11:15:09.441Z
   IN  {
         record_id     : <rec:d4g28b33-...>,
         classifier_id : "ism-classifier.siem-triage-v6",
         category      : "UNAUTHORIZED_ACCESS",
         subcategory   : "gcp_sa_key.tor_exit_node.data_lake_access",
         confidence    : 0.95,
         rationale     : "Authentication from a confirmed Tor exit node
                          (185.220.101.47 matches Torproject exit list).
                          Key used to enumerate storage and BigQuery objects
                          in production data lake. iam.serviceAccounts.list
                          call suggests attacker is enumerating further
                          lateral movement targets. Classified UNAUTHORIZED_ACCESS
                          (not SECRET_LEAK): the key was not leaked via code —
                          it was acquired or brute-forced externally.
                          Confidence 0.95: key acquisition vector unknown."
       }
   OUT {
         record_id              : <rec:d4g28b33-...>,
         classification_version : 1,
         effective_at           : "2026-05-20T11:15:09.441Z"
       }
   STATE: INGESTED → CLASSIFIED
────────────────────────────────────────────────────────────────

── OPERATOR: incident.map_surface_area ──────────────────────────
   @ 2026-05-20T11:15:10.200Z
   IN  {
         record_id    : <rec:d4g28b33-...>,
         scanner_id   : "ism-scanner.gcp-iam-v2",
         surface_snapshot_hash : "sha256:9fc5e41ab2c8d3f0...",
         surfaces     : [
           {
             surface_type : "SECRET",
             surface_ref  : "vault://gcp/key/data-export-sa",
             access_mode  : "EXECUTE",
             confidence   : 0.99,
             notes        : "Active GCP service account key managed via
                             HashiCorp Vault GCP secrets engine. Key ID
                             8f3a21bc. Vault path: gcp/key/data-export-sa.
                             Must be rotated immediately via Vault to
                             invalidate current key and issue new one."
           },
           {
             surface_type : "CONFIG",
             surface_ref  : "gcp://iam/projects/acme-prod/serviceAccounts/data-export-sa/policy",
             access_mode  : "WRITE",
             confidence   : 0.88,
             notes        : "SA has roles/bigquery.dataViewer, roles/storage.objectViewer
                             on acme-prod project. If attacker performed
                             iam.serviceAccounts.list for lateral movement,
                             the SA's role bindings should be reviewed and
                             
# Operator Grammar — Incident Substrate Model
**Document:** `operator_grammar.md`
**Path:** `/docs/Incident_Substrate_Model/operator_grammar.md`
**Revision:** RTT/1 · Canon Edition
**Status:** Authoritative
**Issued:** 2026-05-20

---

## Preamble

This document defines the complete operator grammar for the **Incident Substrate Model (ISM)** within the TriadicFrameworks canon. All operators are specified under the **RTT/1** (Recursive Triadic Taxonomy, version 1) protocol.

### RTT/1 Grammar Conventions

| Convention | Meaning |
|---|---|
| `OPERATOR` | Fully-qualified operator identifier in dot-namespace notation |
| `IN(...)` | Required input fields; typed and ordered |
| `OUT(...)` | Emitted output fields; typed and deterministic |
| `PRE[...]` | Precondition predicates — must all evaluate `true` before execution |
| `POST[...]` | Postcondition assertions — must all hold immediately after execution |
| `GUARD(...)` | Operator-level safety gates; failure aborts the operator |
| `YIELDS →` | Terminal state transition emitted on success |
| `FAULTS →` | Named fault states; each must be handled by the calling substrate |
| `MODE` | Execution mode: `READONLY`, `MUTATING`, or `APPROVAL_GATED` |
| `IDEMPOTENT` | Operator may be safely retried without side-effect accumulation |

All operators are **deterministic**: identical inputs under identical substrate state must produce identical outputs. Non-determinism is a grammar fault.

Operators marked `READONLY` must not alter any persisted substrate state. Operators marked `MUTATING` must declare all state transitions in `POST[...]`. Operators marked `APPROVAL_GATED` must not proceed past their `GUARD(...)` until an approval token is present in `IN(...)`.

Namespace prefix `incident.` scopes all operators to the ISM substrate. Sub-namespace `incident.execute.*` is reserved for bounded, reversible-or-acknowledged execution operators only.

---

## 1. Operator Family: Ingestion

---

### `incident.ingest`

**MODE:** `MUTATING` · **IDEMPOTENT:** Yes (keyed on `signal_id`)

**Purpose:** Accept a raw incident signal from any upstream emitter and normalize it into a canonical ISM `IncidentRecord`. This is the sole entry point for external signal traffic into the substrate.

```
OPERATOR  incident.ingest

IN(
  signal_id      : UUID,          -- Emitter-assigned unique signal identifier
  source         : String,        -- Emitter identity (service name, sensor label, etc.)
  raw_payload    : Bytes,         -- Unprocessed signal body; encoding declared by content_type
  content_type   : MIME,          -- e.g. "application/json", "text/plain"
  emitted_at     : Timestamp,     -- Emitter-side emission time (UTC ISO-8601)
  severity_hint  : SeverityHint?  -- Optional emitter-declared severity; may be overridden downstream
)

OUT(
  record_id      : UUID,          -- ISM-assigned canonical record identifier
  ingested_at    : Timestamp,     -- Substrate-side ingestion time (UTC ISO-8601)
  status         : IngestionStatus -- ACCEPTED | DUPLICATE | REJECTED
)

PRE[
  signal_id is syntactically valid UUID,
  source is non-empty and registered in the emitter registry,
  raw_payload byte length > 0,
  content_type is a supported MIME type,
  emitted_at <= substrate_clock.now()
]

POST[
  status == ACCEPTED  →  IncidentRecord(record_id) exists in substrate with state = INGESTED,
  status == DUPLICATE →  no new record created; existing record_id returned,
  status == REJECTED  →  no record created; fault emitted
]

GUARD(
  emitter is authorized: source ∈ allowed_emitter_set,
  payload size <= MAX_PAYLOAD_BYTES
)

YIELDS  → INGESTED
FAULTS  → UNAUTHORIZED_EMITTER | PAYLOAD_TOO_LARGE | MALFORMED_SIGNAL | UNSUPPORTED_CONTENT_TYPE
```

---

## 2. Operator Family: Classification

---

### `incident.classify`

**MODE:** `MUTATING` · **IDEMPOTENT:** No (classification may evolve; each call is versioned)

**Purpose:** Assign a structured classification to an `IncidentRecord`. Classification is versioned — successive calls append a new `ClassificationVersion` rather than overwriting, preserving the full classification history on the record.

```
OPERATOR  incident.classify

IN(
  record_id      : UUID,          -- Target IncidentRecord
  classifier_id  : String,        -- Identity of the classifying agent or model
  category       : IncidentCategory,  -- Primary taxonomy node (e.g. SECRET_LEAK, DEPENDENCY_CVE)
  subcategory    : String?,        -- Optional free-form subcategory label
  confidence     : Float[0.0,1.0], -- Classifier confidence in this classification
  rationale      : String          -- Human-readable classification rationale
)

OUT(
  record_id      : UUID,
  classification_version : UInt,   -- Monotonically increasing version index on this record
  effective_at   : Timestamp
)

PRE[
  IncidentRecord(record_id) exists,
  IncidentRecord(record_id).state ∈ {INGESTED, CLASSIFIED, SURFACE_MAPPED},
  confidence ∈ [0.0, 1.0],
  rationale is non-empty
]

POST[
  IncidentRecord(record_id).classification == ClassificationVersion(classification_version),
  IncidentRecord(record_id).state == CLASSIFIED,
  classification_version == previous_version + 1
]

GUARD(
  classifier_id is registered,
  confidence >= MIN_CLASSIFICATION_CONFIDENCE  -- substrate-configured threshold
)

YIELDS  → CLASSIFIED
FAULTS  → RECORD_NOT_FOUND | INVALID_CATEGORY | CONFIDENCE_BELOW_THRESHOLD | INVALID_STATE_TRANSITION
```

---

## 3. Operator Family: Surface Mapping

---

### `incident.map_surface_area`

**MODE:** `MUTATING` · **IDEMPOTENT:** Yes (keyed on `record_id` + `surface_snapshot_hash`)

**Purpose:** Enumerate all substrate surfaces (files, secrets, dependencies, services, configurations) that the classified incident touches. The surface area map is the authoritative scope boundary for all downstream rectification and execution operators.

```
OPERATOR  incident.map_surface_area

IN(
  record_id         : UUID,
  scanner_id        : String,               -- Identity of the surface scanner agent
  surfaces          : List<SurfaceEntry>,   -- See SurfaceEntry schema below
  surface_snapshot_hash : Hash              -- Content hash of the surfaces list for idempotency
)

-- SurfaceEntry schema:
--   surface_type   : SurfaceType  (FILE | SECRET | DEPENDENCY | SERVICE | CONFIG)
--   surface_ref    : String       (path, ARN, package@version, service name, config key)
--   access_mode    : AccessMode   (READ | WRITE | EXECUTE | UNKNOWN)
--   confidence     : Float[0.0,1.0]
--   notes          : String?

OUT(
  record_id         : UUID,
  surface_map_id    : UUID,       -- Stable identifier for this surface map snapshot
  surface_count     : UInt,
  mapped_at         : Timestamp
)

PRE[
  IncidentRecord(record_id) exists,
  IncidentRecord(record_id).state == CLASSIFIED,
  surfaces is non-empty,
  all surface_ref values are syntactically valid for their surface_type,
  surface_snapshot_hash == hash(surfaces)
]

POST[
  IncidentRecord(record_id).surface_map_id == surface_map_id,
  IncidentRecord(record_id).state == SURFACE_MAPPED,
  SurfaceMap(surface_map_id).entries.count == surface_count
]

GUARD(
  scanner_id is registered,
  surface_count <= MAX_SURFACE_ENTRIES  -- prevents unbounded scope creep
)

YIELDS  → SURFACE_MAPPED
FAULTS  → RECORD_NOT_FOUND | INVALID_STATE_TRANSITION | EMPTY_SURFACE_LIST
         | SURFACE_REF_INVALID | SURFACE_LIMIT_EXCEEDED | HASH_MISMATCH
```

---

## 4. Operator Family: Rectification Planning

---

### `incident.derive_rectification_steps`

**MODE:** `MUTATING` · **IDEMPOTENT:** No (step derivation is versioned per surface map)

**Purpose:** Derive an ordered, bounded list of rectification steps from the surface area map. Each step maps to exactly one `incident.execute.*` operator. This operator does not execute anything — it produces a typed, operator-bound plan only.

```
OPERATOR  incident.derive_rectification_steps

IN(
  record_id      : UUID,
  surface_map_id : UUID,
  planner_id     : String,           -- Identity of the planning agent
  steps          : List<RectificationStep>  -- See RectificationStep schema below
)

-- RectificationStep schema:
--   step_index     : UInt          (0-based; must be unique and gapless)
--   operator_ref   : OperatorRef   (must resolve to an incident.execute.* operator)
--   target_ref     : String        (must exist in SurfaceMap(surface_map_id).entries)
--   parameters     : Map<String,Any>
--   reversible     : Bool
--   rationale      : String

OUT(
  record_id      : UUID,
  plan_id        : UUID,
  step_count     : UInt,
  derived_at     : Timestamp
)

PRE[
  IncidentRecord(record_id) exists,
  IncidentRecord(record_id).state == SURFACE_MAPPED,
  IncidentRecord(record_id).surface_map_id == surface_map_id,
  steps is non-empty,
  step indices are 0-based, unique, and gapless,
  all operator_ref values resolve to valid incident.execute.* operators,
  all target_ref values exist in SurfaceMap(surface_map_id).entries
]

POST[
  IncidentRecord(record_id).plan_id == plan_id,
  IncidentRecord(record_id).state == PLAN_DERIVED,
  RectificationPlan(plan_id).steps.count == step_count
]

GUARD(
  planner_id is registered,
  step_count <= MAX_PLAN_STEPS,
  all operator_ref values are within the incident.execute.* namespace only
)

YIELDS  → PLAN_DERIVED
FAULTS  → RECORD_NOT_FOUND | INVALID_STATE_TRANSITION | SURFACE_MAP_MISMATCH
         | STEP_INDEX_INVALID | UNKNOWN_OPERATOR_REF | TARGET_NOT_IN_SURFACE_MAP
         | PLAN_STEP_LIMIT_EXCEEDED
```

---

### `incident.generate_readonly_plan`

**MODE:** `READONLY` · **IDEMPOTENT:** Yes

**Purpose:** Render a human-readable, read-only representation of the current `RectificationPlan` for review. This operator does not modify any substrate state. It is the canonical gate before `incident.request_operator_approval`.

```
OPERATOR  incident.generate_readonly_plan

IN(
  record_id      : UUID,
  plan_id        : UUID,
  format         : PlanFormat   -- MARKDOWN | JSON | TEXT
)

OUT(
  record_id      : UUID,
  plan_id        : UUID,
  rendered_plan  : String,      -- Plan body in requested format; no executable content
  rendered_at    : Timestamp
)

PRE[
  IncidentRecord(record_id) exists,
  IncidentRecord(record_id).plan_id == plan_id,
  IncidentRecord(record_id).state ∈ {PLAN_DERIVED, PENDING_APPROVAL, APPROVED, HOLD},
  format ∈ {MARKDOWN, JSON, TEXT}
]

POST[
  no substrate state modified,
  rendered_plan is non-empty,
  rendered_plan contains no embedded operator invocations or executable directives
]

GUARD(
  rendered_plan must not contain control characters or script injection patterns
)

YIELDS  → (no state transition; read-only)
FAULTS  → RECORD_NOT_FOUND | PLAN_NOT_FOUND | PLAN_ID_MISMATCH | UNSUPPORTED_FORMAT
```

---

### `incident.flag_uncertainty`

**MODE:** `MUTATING` · **IDEMPOTENT:** Yes (keyed on `record_id` + `uncertainty_code`)

**Purpose:** Attach a structured uncertainty annotation to a record when the substrate or a planning agent lacks sufficient confidence to proceed without human review. Flagging uncertainty does not block the record — it enriches the approval context and may trigger escalation routing.

```
OPERATOR  incident.flag_uncertainty

IN(
  record_id        : UUID,
  flagging_agent   : String,
  uncertainty_code : UncertaintyCode,  -- See UncertaintyCode registry below
  affected_field   : String?,          -- Optional pointer to the uncertain field or step
  detail           : String            -- Human-readable description of the uncertainty
)

-- UncertaintyCode registry:
--   CLASSIFICATION_AMBIGUOUS    -- Multiple categories plausible with similar confidence
--   SURFACE_INCOMPLETE          -- Scanner may have missed surfaces
--   STEP_REVERSIBILITY_UNKNOWN  -- Cannot confirm if a rectification step is reversible
--   AUTHORIZATION_AMBIGUOUS     -- Approver set is unclear
--   EXTERNAL_DEPENDENCY_UNKNOWN -- Third-party behavior required for rectification is unverified
--   OTHER                       -- Catch-all; detail is mandatory when used

OUT(
  record_id        : UUID,
  flag_id          : UUID,
  flagged_at       : Timestamp
)

PRE[
  IncidentRecord(record_id) exists,
  uncertainty_code ∈ UncertaintyCode registry,
  detail is non-empty,
  if uncertainty_code == OTHER then detail.length >= MIN_OTHER_DETAIL_LENGTH
]

POST[
  UncertaintyFlag(flag_id) attached to IncidentRecord(record_id),
  IncidentRecord(record_id).uncertainty_flags.count increased by 1
]

GUARD(
  flagging_agent is registered
)

YIELDS  → (no state transition; annotation only)
FAULTS  → RECORD_NOT_FOUND | UNKNOWN_UNCERTAINTY_CODE | EMPTY_DETAIL
         | INSUFFICIENT_OTHER_DETAIL
```

---

## 5. Operator Family: Approval Flow

---

### `incident.request_operator_approval`

**MODE:** `APPROVAL_GATED` · `MUTATING` · **IDEMPOTENT:** No

**Purpose:** Formally request human operator approval for the `RectificationPlan`. Transitions the record to `PENDING_APPROVAL` and notifies the designated approver set. No `incident.execute.*` operator may proceed until this request is satisfied.

```
OPERATOR  incident.request_operator_approval

IN(
  record_id        : UUID,
  plan_id          : UUID,
  requesting_agent : String,
  approver_set     : List<ApproverRef>,  -- At least one approver required
  approval_policy  : ApprovalPolicy,    -- ANY_ONE | MAJORITY | ALL
  context_note     : String?            -- Optional note for the approver set
)

OUT(
  record_id        : UUID,
  approval_request_id : UUID,
  requested_at     : Timestamp,
  approver_count   : UInt
)

PRE[
  IncidentRecord(record_id) exists,
  IncidentRecord(record_id).plan_id == plan_id,
  IncidentRecord(record_id).state == PLAN_DERIVED,
  approver_set is non-empty,
  all ApproverRef values are resolvable in the approver registry,
  approval_policy ∈ {ANY_ONE, MAJORITY, ALL}
]

POST[
  IncidentRecord(record_id).state == PENDING_APPROVAL,
  IncidentRecord(record_id).approval_request_id == approval_request_id,
  approver_set notified via substrate notification channel
]

GUARD(
  requesting_agent is registered,
  plan_id refers to a non-empty, validated RectificationPlan,
  record has no open uncertainty flags with severity >= BLOCKING
    unless explicitly acknowledged in context_note
)

YIELDS  → PENDING_APPROVAL
FAULTS  → RECORD_NOT_FOUND | PLAN_NOT_FOUND | INVALID_STATE_TRANSITION
         | EMPTY_APPROVER_SET | UNKNOWN_APPROVER | BLOCKING_UNCERTAINTY_FLAGS
         | INVALID_APPROVAL_POLICY
```

---

### `incident.hold_for_review`

**MODE:** `MUTATING` · **IDEMPOTENT:** Yes (hold is idempotent if reason matches existing hold)

**Purpose:** Place a record into a `HOLD` state, suspending all pending execution. A hold may be placed at any point after `PLAN_DERIVED`. Holds must be explicitly released by an authorized operator before execution can resume. This operator is the primary safety brake in the ISM approval flow.

```
OPERATOR  incident.hold_for_review

IN(
  record_id    : UUID,
  held_by      : String,      -- Identity of the hold-placing operator or agent
  reason_code  : HoldReason,  -- See HoldReason registry below
  detail       : String,      -- Mandatory detail regardless of reason_code
  resume_after : Timestamp?   -- Optional: earliest time hold may be lifted
)

-- HoldReason registry:
--   MANUAL_REVIEW_REQUESTED
--   BLOCKING_UNCERTAINTY
--   APPROVAL_DISPUTED
--   EXTERNAL_DEPENDENCY_PENDING
--   POLICY_ESCALATION
--   SUBSTRATE_FAULT

OUT(
  record_id   : UUID,
  hold_id     : UUID,
  held_at     : Timestamp,
  prior_state : RecordState   -- State the record was in before hold
)

PRE[
  IncidentRecord(record_id) exists,
  IncidentRecord(record_id).state ∈ {PLAN_DERIVED, PENDING_APPROVAL, APPROVED},
  reason_code ∈ HoldReason registry,
  detail is non-empty
]

POST[
  IncidentRecord(record_id).state == HOLD,
  IncidentRecord(record_id).hold_id == hold_id,
  HoldRecord(hold_id).prior_state == prior_state,
  all queued incident.execute.* steps for record_id are suspended
]

GUARD(
  held_by is authorized to place holds on this record
)

YIELDS  → HOLD
FAULTS  → RECORD_NOT_FOUND | INVALID_STATE_TRANSITION | UNKNOWN_HOLD_REASON
         | HOLD_UNAUTHORIZED | EMPTY_DETAIL
```

---

## 6. Operator Family: Bounded Execution

All `incident.execute.*` operators share these invariants:

> **Execution Invariants (apply to all operators in this family)**
> 1. Target must exist in `SurfaceMap` of the parent `IncidentRecord`.
> 2. Parent record must be in state `APPROVED`.
> 3. No execution operator may exceed the scope declared in the approved `RectificationPlan`.
> 4. Each execution operator emits an immutable `ExecutionRecord` on completion (success or fault).
> 5. Faulted executions must not leave targets in a partially-modified state without a `PARTIAL_EXECUTION` fault being emitted.
> 6. Operators with `reversible: false` steps require explicit step-level re-acknowledgment at execution time.

---

### `incident.execute.remove_file`

**MODE:** `MUTATING` · **IDEMPOTENT:** Yes (if file absent, reports ALREADY_ABSENT)

**Purpose:** Remove a specific file declared in the surface area map. Removal is logged immutably. The file path must exactly match a `FILE`-typed surface entry in the approved plan.

```
OPERATOR  incident.execute.remove_file

IN(
  record_id     : UUID,
  plan_id       : UUID,
  step_index    : UInt,
  file_path     : String,       -- Absolute canonical path; must match surface entry exactly
  checksum      : Hash?,        -- Optional pre-removal checksum for audit
  dry_run       : Bool          -- If true, validate only; do not remove
)

OUT(
  record_id      : UUID,
  execution_id   : UUID,
  status         : ExecutionStatus,  -- REMOVED | ALREADY_ABSENT | DRY_RUN_OK
  removed_at     : Timestamp?,
  prior_checksum : Hash?
)

PRE[
  IncidentRecord(record_id).state == APPROVED,
  IncidentRecord(record_id).plan_id == plan_id,
  RectificationPlan(plan_id).steps[step_index].operator_ref == "incident.execute.remove_file",
  RectificationPlan(plan_id).steps[step_index].target_ref == file_path,
  file_path ∈ SurfaceMap(IncidentRecord(record_id).surface_map_id) with surface_type == FILE
]

POST[
  dry_run == false AND status == REMOVED →
    file at file_path no longer exists,
    ExecutionRecord(execution_id) created with status REMOVED,
  dry_run == true →
    no filesystem state changed,
    ExecutionRecord(execution_id) created with status DRY_RUN_OK
]

GUARD(
  executor has filesystem write access to file_path,
  file_path does not resolve outside declared substrate boundaries (no path traversal)
)

YIELDS  → STEP_EXECUTED
FAULTS  → RECORD_NOT_FOUND | PLAN_STEP_MISMATCH | FILE_NOT_IN_SURFACE_MAP
         | ACCESS_DENIED | PATH_TRAVERSAL_DETECTED | PARTIAL_EXECUTION
         | CHECKSUM_MISMATCH
```

---

### `incident.execute.rotate_secret`

**MODE:** `MUTATING` · **IDEMPOTENT:** No (each rotation produces a new secret version)

**Purpose:** Rotate a secret (API key, credential, token, certificate) declared in the surface area map. The old secret value is invalidated and the new value is stored via the substrate's secret management layer. The new secret value is never emitted in `OUT`.

```
OPERATOR  incident.execute.rotate_secret

IN(
  record_id         : UUID,
  plan_id           : UUID,
  step_index        : UInt,
  secret_ref        : String,         -- ARN, vault path, or secret identifier; must match surface entry
  rotation_policy   : RotationPolicy, -- IMMEDIATE | SCHEDULED
  notify_dependents : Bool            -- If true, substrate notifies registered secret consumers
)

OUT(
  record_id          : UUID,
  execution_id       : UUID,
  status             : ExecutionStatus,  -- ROTATED | SCHEDULED
  new_secret_version : String,           -- Version identifier only; NOT the secret value
  rotated_at         : Timestamp?
)

PRE[
  IncidentRecord(record_id).state == APPROVED,
  IncidentRecord(record_id).plan_id == plan_id,
  RectificationPlan(plan_id).steps[step_index].operator_ref == "incident.execute.rotate_secret",
  RectificationPlan(plan_id).steps[step_index].target_ref == secret_ref,
  secret_ref ∈ SurfaceMap(IncidentRecord(record_id).surface_map_id) with surface_type == SECRET,
  rotation_policy ∈ {IMMEDIATE, SCHEDULED}
]

POST[
  status == ROTATED →
    old secret version invalidated in secret management layer,
    new_secret_version active,
    notify_dependents == true → dependent consumers notified,
  ExecutionRecord(execution_id) created,
  new secret value never stored in ExecutionRecord or any ISM log
]

GUARD(
  executor has secret rotation authorization for secret_ref,
  new secret value is never written to OUT or any audit log (zero-secret-value guarantee)
)

YIELDS  → STEP_EXECUTED
FAULTS  → RECORD_NOT_FOUND | PLAN_STEP_MISMATCH | SECRET_NOT_IN_SURFACE_MAP
         | ROTATION_UNAUTHORIZED | ROTATION_PROVIDER_ERROR | PARTIAL_EXECUTION
         | DEPENDENT_NOTIFICATION_FAILED
```

---

### `incident.execute.patch_dependency`

**MODE:** `MUTATING` · **IDEMPOTENT:** Yes (keyed on `record_id` + `package_ref` + `target_version`)

**Purpose:** Apply a dependency patch — upgrading or pinning a package to a declared target version. The dependency must be declared in the surface area map as a `DEPENDENCY`-typed surface entry. Patch application is followed by a deterministic verification step.

```
OPERATOR  incident.execute.patch_dependency

IN(
  record_id       : UUID,
  plan_id         : UUID,
  step_index      : UInt,
  package_ref     : String,          -- Package identifier, e.g. "npm:lodash" or "pypi:requests"
  current_version : String,          -- Version being replaced; must match installed version
  target_version  : String,          -- Version to install; must be a known-good release
  package_manager : PackageManager,  -- NPM | PIP | CARGO | MAVEN | GRADLE | OTHER
  verify_checksum : Hash?,           -- Optional expected checksum of target package
  dry_run         : Bool
)

OUT(
  record_id       : UUID,
  execution_id    : UUID,
  status          : ExecutionStatus,  -- PATCHED | DRY_RUN_OK | ALREADY_AT_TARGET
  patched_version : String?,
  patched_at      : Timestamp?
)

PRE[
  IncidentRecord(record_id).state == APPROVED,
  IncidentRecord(record_id).plan_id == plan_id,
  RectificationPlan(plan_id).steps[step_index].operator_ref == "incident.execute.patch_dependency",
  RectificationPlan(plan_id).steps[step_index].target_ref == package_ref,
  package_ref ∈ SurfaceMap(IncidentRecord(record_id).surface_map_id) with surface_type == DEPENDENCY,
  current_version is semver-valid,
  target_version is semver-valid,
  target_version > current_version OR target_version is an explicit pinned release
]

POST[
  dry_run == false AND status == PATCHED →
    package at package_ref upgraded to target_version,
    verify_checksum provided → checksum verified against installed package,
    ExecutionRecord(execution_id) created,
  dry_run == true →
    no package state changed,
    ExecutionRecord(execution_id) created with DRY_RUN_OK
]

GUARD(
  executor has write access to the dependency manifest and lock file,
  target_version is not marked deprecated or yanked in package_manager registry,
  verify_checksum provided → checksum must match before activation
)

YIELDS  → STEP_EXECUTED
FAULTS  → RECORD_NOT_FOUND | PLAN_STEP_MISMATCH | DEPENDENCY_NOT_IN_SURFACE_MAP
         | VERSION_MISMATCH | TARGET_VERSION_INVALID | PACKAGE_MANAGER_ERROR
         | CHECKSUM_MISMATCH | PARTIAL_EXECUTION
```

---

### `incident.execute.flag_for_followup`

**MODE:** `MUTATING` · **IDEMPOTENT:** Yes (keyed on `record_id` + `followup_code`)

**Purpose:** Mark a surface entry or plan step as requiring post-incident follow-up action that cannot be completed within the current remediation window. This operator closes the step without mutating the target, emitting a structured follow-up ticket into the substrate's tracking layer.

```
OPERATOR  incident.execute.flag_for_followup

IN(
  record_id       : UUID,
  plan_id         : UUID,
  step_index      : UInt,
  target_ref      : String,           -- Surface entry or step reference being deferred
  followup_code   : FollowupCode,     -- See FollowupCode registry below
  priority        : FollowupPriority, -- CRITICAL | HIGH | MEDIUM | LOW
  assigned_to     : List<String>,     -- Assignee identifiers; at least one required
  due_by          : Timestamp?,       -- Optional deadline
  detail          : String            -- Mandatory description of follow-up action required
)

-- FollowupCode registry:
--   MANUAL_REMEDIATION_REQUIRED     -- Step requires human action beyond substrate capability
--   THIRD_PARTY_COORDINATION        -- Remediation depends on external party
--   DEFERRAL_APPROVED               -- Approved deferral; reason documented in detail
--   RISK_ACCEPTED                   -- Risk explicitly accepted; documented in detail
--   MONITORING_REQUIRED             -- No action now; ongoing monitoring required

OUT(
  record_id    : UUID,
  execution_id : UUID,
  followup_id  : UUID,            -- Tracking ticket identifier
  status       : ExecutionStatus, -- FLAGGED
  flagged_at   : Timestamp
)

PRE[
  IncidentRecord(record_id).state == APPROVED,
  IncidentRecord(record_id).plan_id == plan_id,
  RectificationPlan(plan_id).steps[step_index].operator_ref == "incident.execute.flag_for_followup",
  followup_code ∈ FollowupCode registry,
  priority ∈ {CRITICAL, HIGH, MEDIUM, LOW},
  assigned_to is non-empty,
  detail is non-empty
]

POST[
  FollowupTicket(followup_id) created in substrate tracking layer,
  FollowupTicket(followup_id).assigned_to == assigned_to,
  ExecutionRecord(execution_id) created with status FLAGGED,
  step_index marked FLAGGED_FOR_FOLLOWUP in RectificationPlan(plan_id)
]

GUARD(
  all assigned_to identifiers resolvable in operator registry,
  if followup_code == RISK_ACCEPTED →
    detail.length >= MIN_RISK_ACCEPTANCE_DETAIL_LENGTH
)

YIELDS  → STEP_EXECUTED
FAULTS  → RECORD_NOT_FOUND | PLAN_STEP_MISMATCH | UNKNOWN_FOLLOWUP_CODE
         | INVALID_PRIORITY | EMPTY_ASSIGNEE_LIST | UNRESOLVABLE_ASSIGNEE
         | INSUFFICIENT_RISK_DETAIL | EMPTY_DETAIL
```

---

## 7. State Machine

The canonical ISM record state machine governs legal state transitions. Only transitions listed below are valid; all others are grammar faults.

```
INGESTED
  → CLASSIFIED            via  incident.classify
  → HOLD                  via  incident.hold_for_review

CLASSIFIED
  → SURFACE_MAPPED        via  incident.map_surface_area
  → CLASSIFIED            via  incident.classify            (re-classification; version++)
  → HOLD                  via  incident.hold_for_review

SURFACE_MAPPED
  → PLAN_DERIVED          via  incident.derive_rectification_steps
  → CLASSIFIED            via  incident.classify            (reclassify; resets to CLASSIFIED)
  → HOLD                  via  incident.hold_for_review

PLAN_DERIVED
  → PENDING_APPROVAL      via  incident.request_operator_approval
  → HOLD                  via  incident.hold_for_review

PENDING_APPROVAL
  → APPROVED              via  [approval resolution: external to grammar]
  → PLAN_DERIVED          via  [approval rejection: external to grammar]
  → HOLD                  via  incident.hold_for_review

HOLD
  → [prior_state]         via  [hold release: external to grammar; restores prior_state]

APPROVED
  → EXECUTING             via  [first incident.execute.* invocation]
  → HOLD                  via  incident.hold_for_review

EXECUTING
  → RESOLVED              via  [all plan steps STEP_EXECUTED or FLAGGED_FOR_FOLLOWUP]
  → HOLD                  via  incident.hold_for_review
  → FAULTED               via  [any PARTIAL_EXECUTION fault on any step]

RESOLVED   -- Terminal: no further state transitions permitted
FAULTED    -- Terminal: requires manual intervention; may spawn new record via incident.ingest
```

---

## 8. Type Registry

```
UUID              ::= RFC 4122 v4 UUID string
Timestamp         ::= ISO-8601 UTC datetime string, precision to milliseconds
Hash              ::= SHA-256 hex digest string (64 hex characters)
MIME              ::= IANA-registered MIME type string
SeverityHint      ::= CRITICAL | HIGH | MEDIUM | LOW | UNKNOWN
IncidentCategory  ::= SECRET_LEAK | DEPENDENCY_CVE | MISCONFIGURATION | UNAUTHORIZED_ACCESS
                    | DATA_EXPOSURE | SUPPLY_CHAIN | POLICY_VIOLATION | UNKNOWN
SurfaceType       ::= FILE | SECRET | DEPENDENCY | SERVICE | CONFIG
AccessMode        ::= READ | WRITE | EXECUTE | UNKNOWN
IngestionStatus   ::= ACCEPTED | DUPLICATE | REJECTED
ExecutionStatus   ::= REMOVED | ROTATED | PATCHED | FLAGGED | ALREADY_ABSENT
                    | ALREADY_AT_TARGET | DRY_RUN_OK | SCHEDULED
RecordState       ::= INGESTED | CLASSIFIED | SURFACE_MAPPED | PLAN_DERIVED
                    | PENDING_APPROVAL | APPROVED | EXECUTING | HOLD | RESOLVED | FAULTED
PlanFormat        ::= MARKDOWN | JSON | TEXT
ApprovalPolicy    ::= ANY_ONE | MAJORITY | ALL
PackageManager    ::= NPM | PIP | CARGO | MAVEN | GRADLE | OTHER
FollowupPriority  ::= CRITICAL | HIGH | MEDIUM | LOW
OperatorRef       ::= Fully-qualified dot-namespace string resolving to an incident.execute.* operator
ApproverRef       ::= Opaque string resolvable in the approver registry
```

---

## 9. Substrate Constants

These values are substrate-configured and must be overridden via the ISM configuration layer, not hardcoded in operator implementations.

| Constant | Default | Description |
|---|---|---|
| `MAX_PAYLOAD_BYTES` | 10 485 760 (10 MiB) | Maximum raw_payload size for ingestion |
| `MIN_CLASSIFICATION_CONFIDENCE` | 0.70 | Minimum confidence for classification to proceed |
| `MAX_SURFACE_ENTRIES` | 500 | Maximum surface entries per surface map |
| `MAX_PLAN_STEPS` | 50 | Maximum rectification steps per plan |
| `MIN_OTHER_DETAIL_LENGTH` | 80 chars | Minimum detail length when UncertaintyCode is OTHER |
| `MIN_RISK_ACCEPTANCE_DETAIL_LENGTH` | 150 chars | Minimum detail for RISK_ACCEPTED follow-up flags |

---

## 10. Grammar Invariants

The following invariants hold across the entire ISM operator grammar. Violation of any invariant is a substrate fault, not an operator fault.

1. **Namespace isolation:** No operator outside the `incident.*` namespace may modify an `IncidentRecord`.
2. **Plan immutability:** A `RectificationPlan` is immutable once `PENDING_APPROVAL` is entered. Re-planning requires returning to `PLAN_DERIVED` via approval rejection.
3. **Surface scope enforcement:** `incident.execute.*` operators may only act on targets declared in the approved `SurfaceMap`. Out-of-scope targets are a grammar fault.
4. **Zero secret value guarantee:** Secret values must never appear in any `OUT`, `ExecutionRecord`, log, or audit trail. Version identifiers and references are permitted.
5. **Execution sequencing:** `incident.execute.*` steps must be executed in `step_index` order unless the `RectificationPlan` declares explicit parallel groups. Default is strictly sequential.
6. **Approval gate:** No `incident.execute.*` operator may begin unless `IncidentRecord.state == APPROVED` and `approval_request_id` is present on the record.
7. **Uncertainty flag escalation:** Uncertainty flags with severity `BLOCKING` must be resolved or explicitly acknowledged before `incident.request_operator_approval` may proceed.
8. **Hold supremacy:** A record in state `HOLD` cannot have any `incident.execute.*` operator invoked against it, regardless of approval status.
9. **Terminal state finality:** Records in `RESOLVED` or `FAULTED` states are immutable. New incident signals must enter via `incident.ingest` as new records.
10. **Determinism requirement:** All operators must produce identical `OUT` for identical `IN` under identical substrate state. Any operator exhibiting non-determinism is a grammar fault.

---

*End of operator grammar document.*
*Canonical source: `/docs/Incident_Substrate_Model/operator_grammar.md` · TriadicFrameworks repository*
*RTT/1 Canon · ISM Grammar v1.0*

---

**What's covered:** all 12 operators across 6 families, a 10-state deterministic record state machine, a complete type registry, substrate constants table, and 10 cross-cutting grammar invariants — all in RTT/1 `OPERATOR / IN / OUT / PRE / POST / GUARD / YIELDS / FAULTS` form.
# Operator Lifecycle — Incident Substrate Model
**Document:** `operator_lifecycle.md`
**Path:** `/docs/Incident_Substrate_Model/operator_lifecycle.md`
**Revision:** RTT/1 · Canon Edition
**Status:** Authoritative
**Issued:** 2026-05-20

---

## Trilogy Position

This document is the third and final member of the ISM canon trilogy:

| # | Document | Scope |
|---|---|---|
| 1 | `operator_grammar.md` | Operator contracts: IN/OUT/PRE/POST/GUARD/YIELDS/FAULTS |
| 2 | `substrate_errors.md` | Fault token registry: conditions, severities, handler obligations |
| 3 | `operator_lifecycle.md` | Record lifespan: creation, versioning, lineage, archival, retention, expiry, purge |

All three documents share a single normative boundary. Where they conflict,
the resolution order is: `operator_grammar.md` > `substrate_errors.md` >
`operator_lifecycle.md`. No document in the trilogy is subordinate to any
document outside it.

---

## Preamble

`operator_grammar.md` specifies *what operators do*. `substrate_errors.md`
specifies *what operators emit when they fail*. This document specifies
*what happens to the records those operators produce* — across their entire
lifespan, from the moment a signal is accepted by `incident.ingest` through
to the verified, irrevocable deletion of all associated data.

The lifecycle is the substrate's contract with time. Every record is finite.
Every record's history is immutable. Every record's deletion is receipted.

---

## 1. Lifecycle Phase Model

An `IncidentRecord` passes through exactly seven lifecycle phases. Phases
are distinct from record states (defined in `operator_grammar.md` Section 7)
— states describe *what an operator may do to a record now*; phases describe
*where in its total lifespan a record currently sits*.

```
Phase 1: CREATION      Record identity is minted; signal is bound.
Phase 2: VERSIONING    Mutable sub-objects accumulate versioned snapshots.
Phase 3: LINEAGE       Record is positioned within the incident graph.
Phase 4: ARCHIVAL      Record transitions to a terminal state and is sealed.
Phase 5: RETENTION     Sealed record is held for a policy-defined window.
Phase 6: EXPIRY        Retention window closes; record enters deletion queue.
Phase 7: PURGE         All record data is irreversibly destroyed; receipt issued.
```

Phase transitions are monotonically forward — a record cannot move backward
through phases. Phase 3 (LINEAGE) is the only phase that may overlap with
Phase 2 (VERSIONING); all other phase boundaries are discrete.

```
CREATION → VERSIONING → ARCHIVAL → RETENTION → EXPIRY → PURGE
                ↕
            LINEAGE
```

Phases 1–3 correspond to `IncidentRecord.state ∈ {INGESTED, CLASSIFIED,
SURFACE_MAPPED, PLAN_DERIVED, PENDING_APPROVAL, APPROVED, EXECUTING, HOLD}`.
Phases 4–7 correspond to terminal states `{RESOLVED, FAULTED}` and beyond.

---

## 2. Phase 1 — Record Creation

### 2.1 Identity Model

Every `IncidentRecord` is assigned a globally unique identity at creation
time. Identity is never reused, even after purge. The identity model comprises
four fields that together form the record's immutable fingerprint:

```
RecordIdentity {
  record_id        : UUID         -- RFC 4122 v4; substrate-assigned at ingest
  signal_id        : UUID         -- Emitter-assigned; carried from incident.ingest IN(...)
  source           : String       -- Emitter identity; carried from incident.ingest IN(...)
  ingested_at      : Timestamp    -- Substrate-side acceptance time (UTC ISO-8601, ms precision)
}
```

`record_id` is the primary key for all substrate operations. `signal_id` is
the deduplication key for the emitter. The combination `(signal_id, source)`
is unique within the substrate — the same emitter may not submit the same
signal twice with different outcomes.

`RecordIdentity` is written once at creation and is thereafter immutable.
No operator, configuration change, or administrative action may alter any
field of `RecordIdentity` after the record exits Phase 1.

### 2.2 Creation Gate

Record creation is governed by the following ordered gate sequence, evaluated
by `incident.ingest` before any write:

```
Gate 1: Emitter authorization check         → fault: UNAUTHORIZED_EMITTER
Gate 2: Payload size check                  → fault: PAYLOAD_TOO_LARGE
Gate 3: Content-type support check          → fault: UNSUPPORTED_CONTENT_TYPE
Gate 4: Signal structural validity check    → fault: MALFORMED_SIGNAL
Gate 5: Deduplication check (signal_id)     → yields: status == DUPLICATE (no new record)
Gate 6: Timestamp plausibility check        → fault: MALFORMED_SIGNAL
[WRITE] IncidentRecord created with state = INGESTED
```

Gates are evaluated strictly in order. Failure at any gate aborts the
sequence; later gates are not evaluated. Passing all six gates is the
necessary and sufficient condition for record creation.

A gate-5 DUPLICATE result is not a fault — it is a successful idempotent
response. The existing `record_id` is returned to the caller unchanged.
No new record is created. No state transition occurs on the existing record.

### 2.3 Creation Atomicity

Record creation is atomic. Either all of the following are written in a
single substrate transaction, or none are:

- `RecordIdentity` block
- Initial `RecordState = INGESTED`
- `ingested_at` timestamp
- Normalized signal envelope (source, content_type, emitted_at)
- Raw payload reference (payload is stored separately; the record holds a
  content-addressed reference, not the payload bytes inline)

If the transaction fails after gate 6, the substrate MUST NOT emit
`IngestionStatus == ACCEPTED`. The signal must be re-submitted by the emitter.

### 2.4 Raw Payload Handling

The raw payload is stored in the substrate's content-addressed blob store,
keyed by `SHA-256(raw_payload)`. The `IncidentRecord` holds the hash as a
reference. This has two consequences:

1. **Deduplication at the blob layer:** Identical payloads from different
   signals share one blob. Purge of one record does not purge the blob if
   other records reference it.
2. **Zero inline storage:** The `IncidentRecord` schema never embeds payload
   bytes. All access to raw payload goes through the blob store reference.

Payload blobs are subject to independent retention policy (see Phase 5).
A payload blob is eligible for blob-layer purge only when zero live records
reference it AND the last referencing record has completed Phase 7.

---

## 3. Phase 2 — Record Versioning

### 3.1 Versioned Sub-Object Model

Three sub-objects on an `IncidentRecord` accumulate versioned snapshots
as the record progresses through its operational states. Each version is
immutable once written. Versions are indexed monotonically from 1.

```
VersionedSubObjects {
  classification_versions : List<ClassificationVersion>  -- appended by incident.classify
  surface_map_versions    : List<SurfaceMapVersion>      -- appended by incident.map_surface_area
  plan_versions           : List<PlanVersion>            -- appended by incident.derive_rectification_steps
}
```

The *current* version of each sub-object is always the highest-indexed
entry. The *canonical* version at any given past timestamp is the highest-
indexed entry whose `effective_at` is ≤ that timestamp.

No version may be deleted, overwritten, or reordered. Version indices are
gaps-prohibited: index N+1 may not be written before index N is committed.

### 3.2 ClassificationVersion

```
ClassificationVersion {
  version          : UInt          -- 1-based, monotonically increasing
  classifier_id    : String
  category         : IncidentCategory
  subcategory      : String?
  confidence       : Float[0.0,1.0]
  rationale        : String
  effective_at     : Timestamp
  superseded_at    : Timestamp?    -- null if this is the current version
}
```

When a new classification version is written, the prior version's
`superseded_at` is set to the new version's `effective_at`. This creates
a non-overlapping, gapless temporal chain.

**Classification downgrade protection:** A new classification version whose
`confidence` is more than 0.20 below the prior version's `confidence` MUST
carry an `uncertainty_flag_id` reference pointing to a previously created
`CLASSIFICATION_AMBIGUOUS` uncertainty flag on the same record. Downgrading
without a supporting uncertainty flag is a lifecycle constraint violation.

### 3.3 SurfaceMapVersion

```
SurfaceMapVersion {
  version          : UInt
  surface_map_id   : UUID
  scanner_id       : String
  surface_count    : UInt
  surface_snapshot_hash : Hash
  mapped_at        : Timestamp
  superseded_at    : Timestamp?
}
```

A new `SurfaceMapVersion` may only be written when the record's state is
`CLASSIFIED` or `SURFACE_MAPPED`. Writing a new surface map version while
the record is in `PLAN_DERIVED`, `PENDING_APPROVAL`, or `APPROVED` is
prohibited — the plan is derived against a specific surface map, and
surface re-mapping during the approval window would silently invalidate
the plan.

If a new surface map is genuinely required after planning has begun, the
approval must first be rejected (returning the record to `PLAN_DERIVED`),
then the record must transition back through reclassification to reach
a state where surface re-mapping is permitted.

### 3.4 PlanVersion

```
PlanVersion {
  version          : UInt
  plan_id          : UUID
  planner_id       : String
  surface_map_id   : UUID          -- the surface map this plan was derived against
  step_count       : UInt
  derived_at       : Timestamp
  superseded_at    : Timestamp?
  approved_at      : Timestamp?    -- null until approval resolves
  approved_by      : List<ApproverRef>?
  approval_policy  : ApprovalPolicy?
}
```

A plan version is sealed (becomes immutable beyond `approved_at` and
`approved_by` fields) when `incident.request_operator_approval` is
invoked. Once `PENDING_APPROVAL` is entered, the plan's `steps` list
is frozen — no field of any `RectificationStep` within it may change.

If an approval is rejected, the current plan version's `superseded_at`
is set and the record returns to `PLAN_DERIVED`. A new plan version must
be derived before a new approval can be requested.

### 3.5 Version Chain Integrity Hash

At each version write, the substrate computes and stores a `chain_hash`
over the concatenation of all prior version hashes in that sub-object's
chain plus the new version's canonical serialization:

```
chain_hash[N] = SHA-256(chain_hash[N-1] || serialize(version[N]))
chain_hash[1] = SHA-256(serialize(version[1]))
```

This produces a tamper-evident chain. Any modification to a historical
version invalidates all subsequent chain hashes, which the substrate MUST
verify on every read. A chain hash failure is a substrate integrity fault
and MUST trigger immediate record quarantine and operator alert — it cannot
be resolved by retry.

### 3.6 ExecutionRecord Chain

`incident.execute.*` operators emit `ExecutionRecord` entries that are
appended to the record's execution log. The execution log follows the same
chain hash model as versioned sub-objects. Each `ExecutionRecord` contains:

```
ExecutionRecord {
  execution_id     : UUID
  record_id        : UUID
  plan_id          : UUID
  step_index       : UInt
  operator_ref     : String
  target_ref       : String
  status           : ExecutionStatus
  dry_run          : Bool
  executed_at      : Timestamp
  fault_code       : String?        -- null on success; fault token on failure
  fault_detail     : String?
  chain_hash       : Hash           -- integrity chain over all prior ExecutionRecords
}
```

`ExecutionRecord` entries are append-only and immutable. They are retained
independently of the parent `IncidentRecord` — an `ExecutionRecord` is never
purged before its parent record, and its retention window is always ≥ the
parent's retention window.

---

## 4. Phase 3 — Lineage

### 4.1 The Incident Lineage Graph

The ISM substrate maintains a directed acyclic graph (DAG) of `IncidentRecord`
relationships. Every record is a node; relationships are typed edges. The graph
is append-only — edges are never removed, even after purge (the purge receipt
replaces the node, but edge topology is preserved in the lineage index).

### 4.2 Relationship Types

```
RelationshipType {
  SPAWNED_FROM    -- child record was created to handle a FAULTED parent's unresolved surfaces
  RECLASSIFIED_AS -- record was superseded by a new record with a corrected classification
  SPLIT_INTO      -- record's surface scope was decomposed into multiple child records
  MERGED_FROM     -- record consolidates surfaces from multiple prior records
  LINKED_TO       -- advisory non-causal relationship; used for correlated incidents
}
```

Each relationship is represented as an edge:

```
LineageEdge {
  edge_id          : UUID
  source_record_id : UUID
  target_record_id : UUID
  relationship     : RelationshipType
  created_at       : Timestamp
  created_by       : String       -- operator or agent that established the relationship
  rationale        : String
}
```

### 4.3 Lineage Registration

Lineage edges are registered at the point of the `incident.ingest` call
that creates the child record, not retroactively. The ingesting agent MUST
supply `parent_record_id` and `relationship_type` in the optional lineage
block of `incident.ingest IN(...)` to establish the edge at creation time.

If lineage is not declared at ingest time, it may be registered as a
`LINKED_TO` edge by a subsequent administrative operation, but causal
edge types (`SPAWNED_FROM`, `SPLIT_INTO`, `MERGED_FROM`) are only valid
when declared at the child record's creation moment.

### 4.4 SPAWNED_FROM Semantics

`SPAWNED_FROM` is the primary lineage edge type in the ISM. It is used
when a `FAULTED` record cannot be recovered in place and a new record must
be created to re-attempt remediation. The following constraints apply:

1. The parent record MUST be in state `FAULTED` before a `SPAWNED_FROM`
   child may be ingested.
2. The child record MUST reference the parent's `record_id` in its
   lineage block.
3. The child's `SurfaceMap` MUST be a proper subset of the parent's
   `SurfaceMap` at the point of fault — it may not introduce new surfaces
   not present in the parent's surface history.
4. The parent record's `ExecutionRecord` chain is cross-referenced in
   the child's lineage metadata, giving the child's operators full
   visibility into what the parent attempted.

### 4.5 Lineage Depth Limit

The lineage graph enforces a maximum depth of `MAX_LINEAGE_DEPTH` (default: 5)
for any single `SPAWNED_FROM` chain. A record at depth 5 may not spawn
further children via `SPAWNED_FROM`. At this depth, mandatory human
escalation is required — the incident surface is considered persistently
unresolvable by automated means and must be handled entirely out-of-band.

`LINKED_TO` edges are exempt from depth limits — they are advisory only
and do not represent causal descent.

### 4.6 Graph Traversal Rules

- The lineage graph may be queried at any time, including during active
  execution.
- Traversal results include nodes in all lifecycle phases — including purged
  nodes, represented by their purge receipts.
- The graph is read-only from the perspective of all `incident.*` operators.
  Only lifecycle management processes (archival, lineage registration) may
  write edges.
- Cycles are a substrate integrity fault. The substrate MUST reject any
  edge that would create a cycle in the lineage graph.

---

## 5. Phase 4 — Archival

### 5.1 Archival Trigger

Archival is triggered automatically when an `IncidentRecord` enters either
terminal state:

```
state == RESOLVED  →  archival triggered immediately
state == FAULTED   →  archival triggered after FAULT_ARCHIVAL_DELAY (default: 24h)
                       to allow operators time to inspect the live record
```

`FAULTED` records are not archived immediately because operators routinely
need to read the live record's execution chain and surface map during
incident post-mortems. The delay window is configurable but the minimum
is 1 hour; zero-delay archival of faulted records is not permitted.

### 5.2 Archival Seal

Before archival, the substrate computes the **Archival Seal** — a single
hash over the complete, serialized record at the moment of archival. The
Archival Seal is the authoritative integrity reference for the archived record.

```
ArchivalSeal {
  seal_id          : UUID
  record_id        : UUID
  sealed_at        : Timestamp
  terminal_state   : RecordState   -- RESOLVED | FAULTED
  record_hash      : Hash          -- SHA-256 over canonical record serialization
  chain_hashes     : Map<String,Hash>  -- final chain_hash for each versioned sub-object
  execution_count  : UInt          -- total ExecutionRecord entries at seal time
  lineage_edge_count : UInt
}
```

The `ArchivalSeal` is written to a dedicated, append-only seal ledger that
is independent of the main record store. The seal is never stored inline
with the record it covers — physical separation ensures that seal data
survives even if the record store is compromised.

### 5.3 Post-Archival Record State

After archival, the `IncidentRecord` in the main store is replaced by an
`ArchivedRecordStub`:

```
ArchivedRecordStub {
  record_id        : UUID
  terminal_state   : RecordState
  sealed_at        : Timestamp
  seal_id          : UUID          -- reference to ArchivalSeal in seal ledger
  archive_ref      : ArchiveRef    -- content-addressed location in archive store
  retention_class  : RetentionClass
  expires_at       : Timestamp
  legal_hold       : Bool
}
```

The stub is the only record-store presence of an archived record. All
detailed data is in the archive store, accessed via `archive_ref`. The stub
is itself immutable after creation — the only field that may change is
`legal_hold` (see Phase 5).

### 5.4 Archive Store

The archive store is a content-addressed, write-once object store. Each
archived record occupies a single archive object keyed by
`SHA-256(canonical_serialization)`. Archive objects are:

- **Write-once:** No archive object may be overwritten.
- **Read-many:** Archive objects may be fetched for audit and lineage review.
- **Separately retained:** Archive objects follow the retention policy bound
  to the `ArchivedRecordStub`, not the main store's policy.
- **Cross-referenced:** The `archive_ref` in the stub is a stable, durable
  locator — it does not change if the archive store is migrated.

Secret-typed surface entries within archived records are **redacted** in
the archive object. The `surface_ref` (the identifier, e.g. vault path or
ARN) is retained for audit purposes. The secret *value* was never stored
in the record (per the zero-secret-value guarantee in grammar invariant 4),
so no redaction of values is needed — only a marker noting that this surface
type carries a secret reference is retained.

---

## 6. Phase 5 — Retention

### 6.1 Retention Classes

Every archived record is assigned a `RetentionClass` at the time of archival.
Retention class determines the minimum period for which archived record data
must be held before it becomes eligible for expiry.

```
RetentionClass {
  CRITICAL   -- Minimum retention: 7 years
             -- Applies to: records with IncidentCategory ∈ {SECRET_LEAK,
             --   UNAUTHORIZED_ACCESS, DATA_EXPOSURE, SUPPLY_CHAIN}
             -- Also applies to: any record with MAX_LINEAGE_DEPTH >= 3

  STANDARD   -- Minimum retention: 2 years
             -- Applies to: records with IncidentCategory ∈ {DEPENDENCY_CVE,
             --   MISCONFIGURATION, POLICY_VIOLATION}
             -- Also applies to: any FAULTED record not otherwise CRITICAL

  LOW        -- Minimum retention: 90 days
             -- Applies to: records with IncidentCategory == UNKNOWN where
             --   terminal_state == RESOLVED and lineage depth == 0
             -- Also applies to: dry-run-only records (all steps dry_run == true)
}
```

`RetentionClass` is computed deterministically from the record's
classification history and lineage at seal time. The class is always the
maximum class implied by any single qualifying rule — a record satisfying
both `STANDARD` and `CRITICAL` criteria is assigned `CRITICAL`.

`RetentionClass` is immutable once assigned. A record cannot be downgraded
to a lower class after archival, even if the initial classification is later
determined to have been incorrect.

### 6.2 Retention Period Computation

```
expires_at = sealed_at + retention_period(retention_class) + jitter
```

Where:
- `retention_period(CRITICAL)` = 7 years (2557 days)
- `retention_period(STANDARD)` = 2 years (730 days)
- `retention_period(LOW)`      = 90 days
- `jitter` = deterministic pseudo-random offset in range [0, 24h], keyed
  on `record_id`. Jitter prevents expiry thundering-herd when large batches
  of records are archived simultaneously.

`expires_at` is written into the `ArchivedRecordStub` at archival time and
is thereafter immutable — except for legal hold extension (see 6.3).

### 6.3 Legal Hold

A legal hold prevents expiry and purge regardless of `expires_at`. Legal
holds are set and cleared exclusively by substrate administrators via the
Legal Hold Management Interface — no `incident.*` operator may set or clear
a legal hold.

```
LegalHold {
  hold_id          : UUID
  record_id        : UUID
  placed_at        : Timestamp
  placed_by        : String        -- administrator identity
  authority        : String        -- reference to legal/compliance authority (e.g. case number)
  review_due_at    : Timestamp     -- when the hold must be reviewed for continued necessity
}
```

A record under legal hold:
- Does not enter Phase 6 (EXPIRY) regardless of `expires_at`.
- Must be reviewed at `review_due_at` — the substrate MUST emit a
  notification to the placing administrator at `review_due_at - 30 days`.
- If `review_due_at` passes without a review action, the substrate MUST
  alert and extend `review_due_at` by 90 days automatically, indefinitely.
  It does not lift the hold automatically.

Legal holds are fully audited — every placement, review, extension, and
removal is written to the Legal Hold Audit Ledger, which has its own
independent retention period of `MAX(record_retention, 10 years)`.

### 6.4 Payload Blob Retention

Raw payload blobs stored in the content-addressed blob store are retained
for the lifetime of the longest-retaining referencing record. When the
last record referencing a blob completes Phase 7, the blob becomes eligible
for blob-layer purge at the next blob GC cycle.

Blob GC cycles run no more frequently than once per 24 hours and no less
frequently than once per 7 days.

### 6.5 ExecutionRecord Retention

`ExecutionRecord` entries are retained for:

```
MAX(parent_record_retention, EXECUTION_RECORD_MINIMUM_RETENTION)
```

Where `EXECUTION_RECORD_MINIMUM_RETENTION` = 2 years (730 days), regardless
of the parent record's class. A `LOW`-class parent record may be purged after
90 days, but its `ExecutionRecord` entries are held for the full 2 years.

This ensures that execution audit trails outlive the records that generated
them for all non-CRITICAL incidents, providing a minimum audit window
sufficient for most regulatory frameworks.

---

## 7. Phase 6 — Expiry

### 7.1 Expiry Eligibility

An `ArchivedRecordStub` becomes expiry-eligible when all of the following
are true:

```
substrate_clock.now() >= expires_at
legal_hold == false
all child records in lineage graph are in Phase 4 or later
  (a parent record may not expire while a live child record references it)
no open FollowupTicket references this record_id with status != CLOSED
```

The child-record constraint means lineage roots expire last — a parent
incident cannot be purged while any of its `SPAWNED_FROM` descendants are
still active. This preserves the full causal context for active incidents.

### 7.2 Expiry Notice Window

When a record becomes expiry-eligible, the substrate enters a mandatory
**expiry notice window** of 72 hours before the record is placed into the
purge queue. During this window:

- The `ArchivedRecordStub` is marked `expiry_pending: true`.
- A notification is sent to the substrate's designated expiry notification
  channel (configurable endpoint; default: substrate operations mailbox).
- Any substrate administrator may extend the expiry window by up to 30 days
  via the Expiry Extension Interface. Extensions are limited to 3 per record
  without a legal hold being placed.
- After 3 extensions without a legal hold, the record enters the purge
  queue automatically at the next eligible window.

### 7.3 Expiry Notice Payload

```
ExpiryNotice {
  notice_id        : UUID
  record_id        : UUID
  terminal_state   : RecordState
  retention_class  : RetentionClass
  sealed_at        : Timestamp
  expires_at       : Timestamp
  purge_eligible_at : Timestamp   -- expires_at + 72h notice window
  lineage_summary  : String       -- human-readable: depth, child count, relationship types
  followup_summary : String       -- count of CLOSED FollowupTickets on this record
}
```

Expiry notices are stored in the Expiry Notice Ledger for the duration of
the record's legal hold audit trail (minimum 10 years). They are never
purged with the record they describe.

---

## 8. Phase 7 — Purge

### 8.1 Purge Mechanics

Purge is the irreversible, verified destruction of all primary record data.
It proceeds in the following strict sequence:

```
Step 1: Pre-purge integrity check
  Verify ArchivalSeal(record_id).record_hash against the archive object.
  If hash does not match → abort purge; emit substrate integrity fault.

Step 2: ExecutionRecord purge eligibility check
  Verify all ExecutionRecords for record_id have retention age >=
    EXECUTION_RECORD_MINIMUM_RETENTION.
  If not → defer purge; log deferral reason.

Step 3: FollowupTicket closure check
  Verify all FollowupTickets referencing record_id are in CLOSED state.
  If any are OPEN → abort purge; emit PURGE_BLOCKED_BY_OPEN_FOLLOWUP.

Step 4: Lineage child check
  Verify all child records in lineage are in Phase 4 or later.
  If any child is in Phase 1–3 → abort purge; log blocking child record_id.

Step 5: Legal hold check
  Verify legal_hold == false.
  If true → abort purge; emit PURGE_BLOCKED_BY_LEGAL_HOLD.

Step 6: Purge Receipt pre-issuance
  Write PurgeReceipt (see 8.2) to Purge Receipt Ledger BEFORE destruction.
  If PurgeReceipt write fails → abort entire purge; do not destroy data.

Step 7: Data destruction
  7a. Delete archive object from archive store.
  7b. Purge all ClassificationVersions, SurfaceMapVersions, PlanVersions
      from version store.
  7c. Purge ExecutionRecords (if retention-eligible; see Phase 5).
  7d. Purge UncertaintyFlags, HoldRecords, ApprovalRequests.
  7e. Replace ArchivedRecordStub with PurgeStub (see 8.3).
  7f. Remove payload blob reference; trigger blob GC eligibility.

Step 8: Post-purge verification
  Verify ArchivedRecordStub has been replaced by PurgeStub.
  Verify archive object is no longer retrievable.
  Verify PurgeReceipt.purge_completed_at is set.
  If any verification fails → emit PURGE_INCOMPLETE; alert operators.
```

All eight steps are logged to the Purge Audit Log. Step 6 (pre-issuance
of the purge receipt) MUST complete before any data destruction in step 7.
If the substrate crashes between steps 6 and 7, the purge is idempotent —
on recovery, the substrate detects the pre-issued receipt and re-attempts
destruction only for sub-steps not yet verified complete.

### 8.2 Purge Receipt

```
PurgeReceipt {
  receipt_id       : UUID
  record_id        : UUID          -- preserved permanently
  terminal_state   : RecordState   -- preserved permanently
  retention_class  : RetentionClass
  sealed_at        : Timestamp
  purge_initiated_at  : Timestamp
  purge_completed_at  : Timestamp?  -- null until step 8 verification passes
  purge_initiated_by  : String      -- substrate process identity
  execution_count  : UInt          -- total ExecutionRecords that existed
  surface_count    : UInt          -- total surface entries that existed
  lineage_edges    : UInt          -- total lineage edges at purge time
  seal_id          : UUID          -- reference to ArchivalSeal in seal ledger
  verification_hash : Hash         -- SHA-256 over PurgeReceipt canonical serialization
}
```

The `PurgeReceipt` is the permanent, irrevocable record that a given
`record_id` existed and was destroyed. It contains enough information to
answer audit questions without retaining any of the original incident data.

`PurgeReceipt` entries are **never purged**. They are retained permanently
in the Purge Receipt Ledger, which is a separate, independently backed-up
store. The Purge Receipt Ledger's own integrity is verified by a daily
chain-hash audit over all receipts in chronological order.

### 8.3 Purge Stub

After step 7e, the `ArchivedRecordStub` is replaced by a `PurgeStub`:

```
PurgeStub {
  record_id        : UUID
  receipt_id       : UUID          -- reference to PurgeReceipt
  purge_completed_at : Timestamp
}
```

The `PurgeStub` remains in the main record store permanently, in the same
index position as the original `IncidentRecord`. Its sole purpose is to
ensure that any system holding a cached `record_id` receives a meaningful
and accurate response ("this record was purged") rather than a
`RECORD_NOT_FOUND` error, which would be ambiguous between "never existed"
and "was destroyed."

### 8.4 Zero-Retention Guarantee for Secret Surfaces

The ISM provides a specific, additional guarantee for SECRET-typed surface
entries: at no point during any lifecycle phase do secret *values* enter
any substrate store. This guarantee is enforced at three layers:

1. **Grammar layer:** `incident.execute.rotate_secret` OUT never includes
   the new secret value (grammar invariant 4, `operator_grammar.md`).
2. **Archival layer:** Archive objects for records with SECRET-typed surfaces
   include only the `surface_ref` (the identifier/path) — marked with a
   `[SECRET_SURFACE]` tag — never any value.
3. **Purge layer:** The `PurgeReceipt` records the count of SECRET-typed
   surface entries that existed, but not their refs or values.

This three-layer guarantee means that purging a record containing SECRET
surfaces achieves complete destruction of all secret-adjacent data — there
is no residual secret identifier in any post-purge artifact.

---

## 9. Lifecycle Invariants

The following invariants govern the complete lifecycle. They extend
(and do not contradict) the grammar invariants in `operator_grammar.md`
Section 10.

1. **Phase monotonicity:** A record may not move to an earlier lifecycle
   phase. Archival is irreversible; retention is non-decreasing; purge is
   terminal.

2. **Identity permanence:** `RecordIdentity` fields are immutable from
   Phase 1 onward. No lifecycle event, administrative action, or substrate
   migration may alter `record_id`, `signal_id`, `source`, or `ingested_at`.

3. **Version chain tamper-evidence:** Any break in a versioned sub-object's
   chain hash sequence is a substrate integrity fault. The substrate MUST
   quarantine the affected record and alert operators. Chain hash failures
   are never silently corrected.

4. **Archival seal precedence:** The `ArchivalSeal` is the authoritative
   record of what an `IncidentRecord` contained at terminal state. If the
   archive object and the seal disagree, the seal is correct and the
   archive object is corrupted.

5. **Retention class immutability:** A record's `RetentionClass` is assigned
   once at archival and never reduced. Upward reclassification (e.g., a
   STANDARD record discovered to fall under CRITICAL criteria) requires a
   legal hold to be placed immediately and a substrate administrator review.

6. **Pre-purge receipt requirement:** No record data may be destroyed before
   a `PurgeReceipt` is committed to the Purge Receipt Ledger. Destruction
   without a receipt is a substrate integrity fault.

7. **Purge stub permanence:** `PurgeStub` entries are never deleted. The
   main record store's index is monotonically growing — it only gains
   entries (as new records) or replaces entries with stubs (on purge); it
   never shrinks.

8. **ExecutionRecord longevity floor:** `ExecutionRecord` entries are never
   purged before `EXECUTION_RECORD_MINIMUM_RETENTION` (2 years), regardless
   of the parent record's retention class or purge status.

9. **Lineage graph permanence:** Lineage edges and node references (including
   purge stub references) are never deleted from the lineage graph. The
   lineage graph grows monotonically.

10. **Legal hold audit completeness:** Every legal hold placement, review,
    extension, and removal is recorded in the Legal Hold Audit Ledger. No
    legal hold event may occur without a corresponding audit entry. The
    Legal Hold Audit Ledger is retained for `MAX(record_retention, 10 years)`.

11. **Child-before-parent expiry prohibition:** A record with live children
    (Phase 1–3) in the lineage graph may not enter Phase 6 (EXPIRY). Expiry
    eligibility is re-evaluated whenever a child record transitions to Phase 4.

12. **Secret surface zero-retention:** No secret *value* associated with any
    SECRET-typed surface entry is retained in any substrate store at any
    lifecycle phase. The zero-retention guarantee for secret values is
    unconditional and survives purge.

---

## 10. Lifecycle Schema Extensions

Types introduced by this document, extending the registry in
`operator_grammar.md` Section 8.

```
RecordIdentity     ::= { record_id: UUID, signal_id: UUID,
                          source: String, ingested_at: Timestamp }

ClassificationVersion ::= { version: UInt, classifier_id: String,
                              category: IncidentCategory, subcategory: String?,
                              confidence: Float, rationale: String,
                              effective_at: Timestamp, superseded_at: Timestamp?,
                              chain_hash: Hash }

SurfaceMapVersion  ::= { version: UInt, surface_map_id: UUID, scanner_id: String,
                          surface_count: UInt, surface_snapshot_hash: Hash,
                          mapped_at: Timestamp, superseded_at: Timestamp?,
                          chain_hash: Hash }

PlanVersion        ::= { version: UInt, plan_id: UUID, planner_id: String,
                          surface_map_id: UUID, step_count: UInt, derived_at: Timestamp,
                          superseded_at: Timestamp?, approved_at: Timestamp?,
                          approved_by: List<ApproverRef>?, approval_policy: ApprovalPolicy?,
                          chain_hash: Hash }

ExecutionRecord    ::= { execution_id: UUID, record_id: UUID, plan_id: UUID,
                          step_index: UInt, operator_ref: String, target_ref: String,
                          status: ExecutionStatus, dry_run: Bool, executed_at: Timestamp,
                          fault_code: String?, fault_detail: String?, chain_hash: Hash }

RelationshipType   ::= SPAWNED_FROM | RECLASSIFIED_AS | SPLIT_INTO
                      | MERGED_FROM | LINKED_TO

LineageEdge        ::= { edge_id: UUID, source_record_id: UUID,
                          target_record_id: UUID, relationship: RelationshipType,
                          created_at: Timestamp, created_by: String, rationale: String }

ArchivalSeal       ::= { seal_id: UUID, record_id: UUID, sealed_at: Timestamp,
                          terminal_state: RecordState, record_hash: Hash,
                          chain_hashes: Map<String,Hash>, execution_count: UInt,
                          lineage_edge_count: UInt }

ArchivedRecordStub ::= { record_id: UUID, terminal_state: RecordState,
                          sealed_at: Timestamp, seal_id: UUID,
                          archive_ref: ArchiveRef, retention_class: RetentionClass,
                          expires_at: Timestamp, legal_hold: Bool }

RetentionClass     ::= CRITICAL | STANDARD | LOW

LegalHold          ::= { hold_id: UUID, record_id: UUID, placed_at: Timestamp,
                          placed_by: String, authority: String, review_due_at: Timestamp }

ExpiryNotice       ::= { notice_id: UUID, record_id: UUID, terminal_state: RecordState,
                          retention_class: RetentionClass, sealed_at: Timestamp,
                          expires_at: Timestamp, purge_eligible_at: Timestamp,
                          lineage_summary: String, followup_summary: String }

PurgeReceipt       ::= { receipt_id: UUID, record_id: UUID,
                          terminal_state: RecordState, retention_class: RetentionClass,
                          sealed_at: Timestamp, purge_initiated_at: Timestamp,
                          purge_completed_at: Timestamp?, purge_initiated_by: String,
                          execution_count: UInt, surface_count: UInt,
                          lineage_edges: UInt, seal_id: UUID, verification_hash: Hash }

PurgeStub          ::= { record_id: UUID, receipt_id: UUID, purge_completed_at: Timestamp }

ArchiveRef         ::= Content-addressed locator string in the archive store;
                        format: "ism-archive://<store-id>/<sha256-hex>"

LifecyclePhase     ::= CREATION | VERSIONING | LINEAGE | ARCHIVAL
                      | RETENTION | EXPIRY | PURGE
```

---

## 11. Lifecycle Constants

These values are substrate-configured via the ISM configuration layer.

| Constant | Default | Description |
|---|---|---|
| `FAULT_ARCHIVAL_DELAY` | 24 hours | Delay before FAULTED records are archived |
| `MAX_LINEAGE_DEPTH` | 5 | Maximum SPAWNED_FROM chain depth |
| `RETENTION_CRITICAL` | 7 years (2557 days) | Retention period for CRITICAL class records |
| `RETENTION_STANDARD` | 2 years (730 days) | Retention period for STANDARD class records |
| `RETENTION_LOW` | 90 days | Retention period for LOW class records |
| `EXECUTION_RECORD_MINIMUM_RETENTION` | 2 years (730 days) | Minimum retention for ExecutionRecords regardless of parent class |
| `EXPIRY_NOTICE_WINDOW` | 72 hours | Notice window before purge queue entry |
| `EXPIRY_EXTENSION_MAX` | 3 | Maximum extensions without legal hold |
| `EXPIRY_EXTENSION_PERIOD` | 30 days | Duration of each extension |
| `LEGAL_HOLD_REVIEW_ALERT_LEAD` | 30 days | Alert lead time before `review_due_at` |
| `LEGAL_HOLD_AUDIT_RETENTION` | MAX(record, 10 years) | Retention for Legal Hold Audit Ledger |
| `BLOB_GC_MIN_INTERVAL` | 24 hours | Minimum interval between blob GC cycles |
| `BLOB_GC_MAX_INTERVAL` | 7 days | Maximum interval between blob GC cycles |
| `CHAIN_HASH_AUDIT_INTERVAL` | 24 hours | Frequency of Purge Receipt Ledger integrity audit |

---

## 12. Trilogy Cross-Reference

| Concept | Primary definition | Referenced here |
|---|---|---|
| `IncidentRecord.state` machine | `operator_grammar.md` §7 | §1 (phase mapping), §5.1 (archival trigger) |
| `incident.ingest` gate sequence | `operator_grammar.md` §1 | §2.2 (creation gate) |
| Grammar Invariant 4 (zero-secret-value) | `operator_grammar.md` §10 | §5.4, §8.4 |
| `ExecutionRecord` | `operator_grammar.md` §3.6 | §3.6, §5.5, §8.1 step 7c |
| All fault tokens | `substrate_errors.md` | §2.2 (gate faults), §8.1 (purge faults) |
| `GEN-005 PARTIAL_EXECUTION` | `substrate_errors.md` §GEN | §3.6 (faulted execution chain) |
| `EXE-002 PATH_TRAVERSAL_DETECTED` | `substrate_errors.md` §EXE | §4.3 (SPAWNED_FROM child constraints) |
| Substrate constants | `operator_grammar.md` §9 | §11 (lifecycle constants extend §9) |

---

*End of lifecycle document.*
*Canonical source: `/docs/Incident_Substrate_Model/operator_lifecycle.md` · TriadicFrameworks repository*
*RTT/1 Canon · ISM Lifecycle v1.0*
*Trilogy complete: operator_grammar.md · substrate_errors.md · operator_lifecycle.md*
# Substrate Error Registry — Incident Substrate Model
**Document:** `substrate_errors.md`
**Path:** `/docs/Incident_Substrate_Model/substrate_errors.md`
**Revision:** RTT/1 · Canon Edition
**Status:** Authoritative
**Companion:** `operator_grammar.md`
**Issued:** 2026-05-20

---

## Preamble

This document is the single canonical source of truth for all fault tokens
emitted by operators in the Incident Substrate Model (ISM). Every `FAULTS →`
entry in `operator_grammar.md` resolves to exactly one entry here.

Implementors MUST:
- Treat unrecognized fault tokens as `GEN-005 PARTIAL_EXECUTION` equivalents
  (i.e., assume worst-case substrate contamination and halt).
- Never swallow a fault silently. Every fault must produce an `ExecutionRecord`
  or an `IngestionStatus == REJECTED` where applicable.
- Expose the fault code verbatim to the calling substrate layer — do not
  translate, generalize, or redact fault codes in runtime logs.

---

## How to Read This Registry

Each entry follows this structure:

```
### FAULT_TOKEN_NAME
**Code:**          DOMAIN-NNN
**Severity:**      FATAL | ERROR | WARNING
**Recoverability:** RECOVERABLE | OPERATOR_ACTION_REQUIRED | UNRECOVERABLE
**Emitted by:**    Comma-separated operator list
**Condition:**     Precise trigger condition
**State effect:**  What happens to IncidentRecord state on fault
**Handler MUST:**  Required runtime behavior
**Notes:**         Implementation guidance; edge cases
```

### Severity Tiers

| Tier | Meaning |
|---|---|
| `FATAL` | Record transitions to `FAULTED`; substrate execution halts for this record. All queued steps are cancelled. |
| `ERROR` | Operator aborts; substrate state is unchanged (as if operator was never called). Caller may retry after correction. |
| `WARNING` | Operator completed but with degraded guarantees. An `ExecutionRecord` is created; the step is marked `STEP_EXECUTED` with a warning annotation. |

### Recoverability Tiers

| Tier | Meaning |
|---|---|
| `RECOVERABLE` | Caller corrects the input and retries the operator. No human escalation required. |
| `OPERATOR_ACTION_REQUIRED` | Human or privileged system intervention is needed before retry (e.g., registry update, authorization grant, manual resolution). |
| `UNRECOVERABLE` | The current `IncidentRecord` cannot be repaired. A new record must be created via `incident.ingest` if re-processing is needed. |

---

## Quick Reference Table

48 unique fault tokens across 8 domains.

| Code | Token | Severity | Recoverability | Domain |
|---|---|---|---|---|
| GEN-001 | RECORD_NOT_FOUND | ERROR | RECOVERABLE | Cross-operator |
| GEN-002 | INVALID_STATE_TRANSITION | ERROR | OPERATOR_ACTION_REQUIRED | Cross-operator |
| GEN-003 | PLAN_NOT_FOUND | ERROR | RECOVERABLE | Cross-operator |
| GEN-004 | PLAN_STEP_MISMATCH | ERROR | OPERATOR_ACTION_REQUIRED | Cross-operator |
| GEN-005 | PARTIAL_EXECUTION | FATAL | UNRECOVERABLE | Cross-operator |
| GEN-006 | CHECKSUM_MISMATCH | ERROR | OPERATOR_ACTION_REQUIRED | Cross-operator |
| GEN-007 | EMPTY_DETAIL | ERROR | RECOVERABLE | Cross-operator |
| GEN-008 | ACCESS_DENIED | ERROR | OPERATOR_ACTION_REQUIRED | Cross-operator |
| ING-001 | UNAUTHORIZED_EMITTER | ERROR | OPERATOR_ACTION_REQUIRED | Ingestion |
| ING-002 | PAYLOAD_TOO_LARGE | ERROR | RECOVERABLE | Ingestion |
| ING-003 | MALFORMED_SIGNAL | ERROR | RECOVERABLE | Ingestion |
| ING-004 | UNSUPPORTED_CONTENT_TYPE | ERROR | RECOVERABLE | Ingestion |
| CLS-001 | INVALID_CATEGORY | ERROR | RECOVERABLE | Classification |
| CLS-002 | CONFIDENCE_BELOW_THRESHOLD | ERROR | RECOVERABLE | Classification |
| SRF-001 | EMPTY_SURFACE_LIST | ERROR | RECOVERABLE | Surface Mapping |
| SRF-002 | SURFACE_REF_INVALID | ERROR | RECOVERABLE | Surface Mapping |
| SRF-003 | SURFACE_LIMIT_EXCEEDED | ERROR | OPERATOR_ACTION_REQUIRED | Surface Mapping |
| SRF-004 | HASH_MISMATCH | ERROR | RECOVERABLE | Surface Mapping |
| PLN-001 | SURFACE_MAP_MISMATCH | ERROR | OPERATOR_ACTION_REQUIRED | Planning |
| PLN-002 | STEP_INDEX_INVALID | ERROR | RECOVERABLE | Planning |
| PLN-003 | UNKNOWN_OPERATOR_REF | ERROR | RECOVERABLE | Planning |
| PLN-004 | TARGET_NOT_IN_SURFACE_MAP | ERROR | RECOVERABLE | Planning |
| PLN-005 | PLAN_STEP_LIMIT_EXCEEDED | ERROR | OPERATOR_ACTION_REQUIRED | Planning |
| PLN-006 | PLAN_ID_MISMATCH | ERROR | RECOVERABLE | Planning |
| PLN-007 | UNSUPPORTED_FORMAT | ERROR | RECOVERABLE | Planning |
| UNC-001 | UNKNOWN_UNCERTAINTY_CODE | ERROR | RECOVERABLE | Uncertainty |
| UNC-002 | INSUFFICIENT_OTHER_DETAIL | ERROR | RECOVERABLE | Uncertainty |
| APV-001 | EMPTY_APPROVER_SET | ERROR | RECOVERABLE | Approval Flow |
| APV-002 | UNKNOWN_APPROVER | ERROR | OPERATOR_ACTION_REQUIRED | Approval Flow |
| APV-003 | BLOCKING_UNCERTAINTY_FLAGS | ERROR | OPERATOR_ACTION_REQUIRED | Approval Flow |
| APV-004 | INVALID_APPROVAL_POLICY | ERROR | RECOVERABLE | Approval Flow |
| APV-005 | UNKNOWN_HOLD_REASON | ERROR | RECOVERABLE | Approval Flow |
| APV-006 | HOLD_UNAUTHORIZED | ERROR | OPERATOR_ACTION_REQUIRED | Approval Flow |
| EXE-001 | FILE_NOT_IN_SURFACE_MAP | ERROR | OPERATOR_ACTION_REQUIRED | Bounded Execution |
| EXE-002 | PATH_TRAVERSAL_DETECTED | FATAL | UNRECOVERABLE | Bounded Execution |
| EXE-003 | SECRET_NOT_IN_SURFACE_MAP | ERROR | OPERATOR_ACTION_REQUIRED | Bounded Execution |
| EXE-004 | ROTATION_UNAUTHORIZED | ERROR | OPERATOR_ACTION_REQUIRED | Bounded Execution |
| EXE-005 | ROTATION_PROVIDER_ERROR | ERROR | RECOVERABLE | Bounded Execution |
| EXE-006 | DEPENDENT_NOTIFICATION_FAILED | WARNING | OPERATOR_ACTION_REQUIRED | Bounded Execution |
| EXE-007 | DEPENDENCY_NOT_IN_SURFACE_MAP | ERROR | OPERATOR_ACTION_REQUIRED | Bounded Execution |
| EXE-008 | VERSION_MISMATCH | ERROR | RECOVERABLE | Bounded Execution |
| EXE-009 | TARGET_VERSION_INVALID | ERROR | OPERATOR_ACTION_REQUIRED | Bounded Execution |
| EXE-010 | PACKAGE_MANAGER_ERROR | ERROR | RECOVERABLE | Bounded Execution |
| EXE-011 | UNKNOWN_FOLLOWUP_CODE | ERROR | RECOVERABLE | Bounded Execution |
| EXE-012 | INVALID_PRIORITY | ERROR | RECOVERABLE | Bounded Execution |
| EXE-013 | EMPTY_ASSIGNEE_LIST | ERROR | RECOVERABLE | Bounded Execution |
| EXE-014 | UNRESOLVABLE_ASSIGNEE | ERROR | OPERATOR_ACTION_REQUIRED | Bounded Execution |
| EXE-015 | INSUFFICIENT_RISK_DETAIL | ERROR | RECOVERABLE | Bounded Execution |

---

## Domain GEN — Cross-Operator Faults

These faults may be emitted by any operator. Implementations MUST handle them
at the substrate layer rather than per-operator.

---

### RECORD_NOT_FOUND
**Code:** GEN-001
**Severity:** ERROR
**Recoverability:** RECOVERABLE
**Emitted by:** `incident.classify`, `incident.map_surface_area`,
  `incident.derive_rectification_steps`, `incident.generate_readonly_plan`,
  `incident.flag_uncertainty`, `incident.request_operator_approval`,
  `incident.hold_for_review`, `incident.execute.remove_file`,
  `incident.execute.rotate_secret`, `incident.execute.patch_dependency`,
  `incident.execute.flag_for_followup`
**Condition:** The supplied `record_id` does not resolve to any
  `IncidentRecord` in the substrate store.
**State effect:** None. No state is modified.
**Handler MUST:**
  - Abort operator immediately.
  - Return fault token to caller with the unresolved `record_id`.
  - Do not create a new record as a side effect.
**Notes:** Callers should verify `record_id` provenance before retry. If
  `record_id` was obtained from a prior `incident.ingest` `OUT`, the ingest
  may have returned `status == REJECTED` and no record was created —
  check `IngestionStatus` in the ingest result.

---

### INVALID_STATE_TRANSITION
**Code:** GEN-002
**Severity:** ERROR
**Recoverability:** OPERATOR_ACTION_REQUIRED
**Emitted by:** `incident.classify`, `incident.map_surface_area`,
  `incident.derive_rectification_steps`, `incident.request_operator_approval`,
  `incident.hold_for_review`
**Condition:** The current `IncidentRecord.state` is not a member of the
  operator's declared `PRE[...]` legal state set.
**State effect:** None. Operator aborts before any write.
**Handler MUST:**
  - Abort operator immediately.
  - Log current state and the state set the operator expected.
  - Expose both values in the fault payload to the caller.
  - Do not attempt to force-advance or repair the record's state.
**Notes:** This fault almost always indicates a race condition (concurrent
  operator invocations on the same record) or a missed preceding operator
  in the pipeline. Callers MUST use the state machine in `operator_grammar.md`
  Section 7 to determine the correct remediation path. Never retry without
  first querying the current record state.

---

### PLAN_NOT_FOUND
**Code:** GEN-003
**Severity:** ERROR
**Recoverability:** RECOVERABLE
**Emitted by:** `incident.generate_readonly_plan`,
  `incident.request_operator_approval`
**Condition:** The supplied `plan_id` does not resolve to any
  `RectificationPlan` in the substrate store.
**State effect:** None.
**Handler MUST:**
  - Abort operator immediately.
  - Return the unresolved `plan_id` in the fault payload.
**Notes:** Verify the `plan_id` was emitted by a successful
  `incident.derive_rectification_steps` call on the same record. A
  `PLAN_NOT_FOUND` on a record with `state == PLAN_DERIVED` indicates
  a substrate store inconsistency — escalate to substrate operations.

---

### PLAN_STEP_MISMATCH
**Code:** GEN-004
**Severity:** ERROR
**Recoverability:** OPERATOR_ACTION_REQUIRED
**Emitted by:** `incident.execute.remove_file`,
  `incident.execute.rotate_secret`, `incident.execute.patch_dependency`,
  `incident.execute.flag_for_followup`
**Condition:** The `operator_ref` declared for `step_index` in the approved
  `RectificationPlan` does not match the executing operator, OR `target_ref`
  at that step does not match the input target, OR the step at `step_index`
  has already been executed.
**State effect:** None. Execution is refused before any target mutation.
**Handler MUST:**
  - Abort operator immediately.
  - Log the expected `operator_ref`/`target_ref` from the plan and the
    actual values supplied.
  - Do not advance `step_index`.
**Notes:** This is the primary enforcement mechanism for plan scope
  confinement. A mismatch on `operator_ref` may indicate plan tampering or
  incorrect step routing in the execution layer. Treat with the same
  urgency as a security boundary violation. The fix requires re-examining
  the plan and correcting the execution invocation — the plan itself is
  immutable at this stage.

---

### PARTIAL_EXECUTION
**Code:** GEN-005
**Severity:** FATAL
**Recoverability:** UNRECOVERABLE
**Emitted by:** `incident.execute.remove_file`,
  `incident.execute.rotate_secret`, `incident.execute.patch_dependency`
**Condition:** The execution operator began mutating the target but did not
  complete atomically — the target was left in an intermediate state (e.g.,
  file partially deleted, secret rotation started but not committed, package
  manifest updated but lock file not regenerated).
**State effect:** `IncidentRecord.state` transitions to `FAULTED`.
  All remaining queued steps are cancelled.
**Handler MUST:**
  - Immediately halt all further execution steps on this record.
  - Emit an `ExecutionRecord` with status `PARTIAL_EXECUTION` including the
    last known target state and the point of failure.
  - Transition the record to `FAULTED`.
  - Alert operators via the substrate notification channel.
  - Do NOT attempt automatic rollback — rollback is a manual operator action.
**Notes:** This is the most critical fault in the registry. A `PARTIAL_EXECUTION`
  means the substrate surface is in an unknown and potentially dangerous state.
  The `FAULTED` record MUST be reviewed by a human operator before any new
  `incident.ingest` signal for the same surfaces is processed. Execution
  operators MUST use atomic transactions or rollback-capable primitives
  wherever the target system supports them to minimize exposure to this fault.
  `dry_run == true` invocations are immune to this fault.

---

### CHECKSUM_MISMATCH
**Code:** GEN-006
**Severity:** ERROR
**Recoverability:** OPERATOR_ACTION_REQUIRED
**Emitted by:** `incident.execute.remove_file`,
  `incident.execute.patch_dependency`
**Condition:** A `checksum` or `verify_checksum` was supplied and the computed
  checksum of the target (pre-removal or post-install) does not match the
  declared value.
**State effect:** None. The operator aborts before any mutation is committed
  when checksum is a pre-condition. For post-install verification failure in
  `patch_dependency`, the patch is rolled back if possible; if rollback
  fails, `PARTIAL_EXECUTION` supersedes this fault.
**Handler MUST:**
  - Abort without mutating the target.
  - Log both the expected and computed checksums.
  - Never proceed with a mismatched checksum, even under operator override
    at the call site.
**Notes:** A checksum mismatch on a pre-removal file may indicate the file
  was modified between surface mapping and execution — this is a security
  signal. Callers should consider re-running `incident.map_surface_area`
  and `incident.derive_rectification_steps` before retrying. A mismatch
  on `patch_dependency` post-install indicates a compromised package registry
  or a supply chain integrity failure — do not retry without investigating.

---

### EMPTY_DETAIL
**Code:** GEN-007
**Severity:** ERROR
**Recoverability:** RECOVERABLE
**Emitted by:** `incident.flag_uncertainty`, `incident.hold_for_review`,
  `incident.execute.flag_for_followup`
**Condition:** The `detail` field is present but empty, whitespace-only, or
  below the minimum required length for the given context.
**State effect:** None.
**Handler MUST:**
  - Abort operator.
  - Return the minimum length requirement in the fault payload.
**Notes:** "Empty" includes strings containing only whitespace, newlines, or
  null bytes. Implementations MUST trim the `detail` value before length
  evaluation. The minimum length for `UncertaintyCode.OTHER` and
  `FollowupCode.RISK_ACCEPTED` is governed by substrate constants
  `MIN_OTHER_DETAIL_LENGTH` and `MIN_RISK_ACCEPTANCE_DETAIL_LENGTH`
  respectively (see `operator_grammar.md` Section 9).

---

### ACCESS_DENIED
**Code:** GEN-008
**Severity:** ERROR
**Recoverability:** OPERATOR_ACTION_REQUIRED
**Emitted by:** `incident.execute.remove_file`
**Condition:** The executing agent does not hold the required permission to
  perform the declared operation on the target resource.
**State effect:** None. No mutation is attempted.
**Handler MUST:**
  - Abort operator immediately.
  - Log the identity of the executing agent and the target resource.
  - Do not retry with elevated permissions automatically — permission grants
    require explicit operator action.
**Notes:** Implementations MUST NOT cache or re-use permissions across
  execution steps. Each `incident.execute.*` invocation MUST re-validate
  its authorization at execution time. If access was valid during planning
  but denied at execution, emit `incident.flag_uncertainty` with code
  `AUTHORIZATION_AMBIGUOUS` on the record before escalating.

---

## Domain ING — Ingestion Faults

Emitted exclusively by `incident.ingest`. These faults result in
`IngestionStatus == REJECTED`; no `IncidentRecord` is created.

---

### UNAUTHORIZED_EMITTER
**Code:** ING-001
**Severity:** ERROR
**Recoverability:** OPERATOR_ACTION_REQUIRED
**Emitted by:** `incident.ingest`
**Condition:** The `source` value is not present in the substrate's
  `allowed_emitter_set` registry, or the emitter's authorization token
  is absent, expired, or revoked.
**State effect:** No record created. `IngestionStatus == REJECTED`.
**Handler MUST:**
  - Reject the signal without partial processing.
  - Log the unauthorized `source` identifier and the emission timestamp.
  - Do not expose the contents of `allowed_emitter_set` in the fault payload.
  - Rate-limit repeated unauthorized attempts from the same `source`.
**Notes:** This fault is also the correct response when an emitter's
  credentials are valid but its scope does not include the ISM substrate
  endpoint. Substrate operators must register new emitters via the
  emitter registry management interface — not by modifying this document.

---

### PAYLOAD_TOO_LARGE
**Code:** ING-002
**Severity:** ERROR
**Recoverability:** RECOVERABLE
**Emitted by:** `incident.ingest`
**Condition:** `raw_payload` byte length exceeds `MAX_PAYLOAD_BYTES`
  (default: 10 MiB; see `operator_grammar.md` Section 9).
**State effect:** No record created. `IngestionStatus == REJECTED`.
**Handler MUST:**
  - Reject immediately without reading the full payload into memory.
  - Return `MAX_PAYLOAD_BYTES` and the actual received size in the fault payload.
**Notes:** Emitters SHOULD compress or chunk payloads exceeding the limit
  before re-submission. The substrate does not support streaming ingestion —
  the entire payload must fit within the declared limit. If the limit is
  consistently exceeded for legitimate signals, `MAX_PAYLOAD_BYTES` may be
  increased via the ISM configuration layer.

---

### MALFORMED_SIGNAL
**Code:** ING-003
**Severity:** ERROR
**Recoverability:** RECOVERABLE
**Emitted by:** `incident.ingest`
**Condition:** The `raw_payload` cannot be parsed according to the declared
  `content_type`, or required top-level fields are absent or of the wrong type,
  or `signal_id` is not a syntactically valid RFC 4122 v4 UUID, or
  `emitted_at` is not a valid ISO-8601 UTC timestamp.
**State effect:** No record created. `IngestionStatus == REJECTED`.
**Handler MUST:**
  - Reject the signal.
  - Return the specific field or structural issue that caused the fault.
  - Do not attempt partial parsing or best-effort normalization.
**Notes:** The substrate MUST NOT attempt to infer or correct malformed
  field values. Silent correction masks emitter-side bugs and produces
  unreliable `IncidentRecord` data downstream. Emitter implementors should
  run signals through schema validation before submission.

---

### UNSUPPORTED_CONTENT_TYPE
**Code:** ING-004
**Severity:** ERROR
**Recoverability:** RECOVERABLE
**Emitted by:** `incident.ingest`
**Condition:** The `content_type` value is not present in the substrate's
  list of supported MIME types.
**State effect:** No record created. `IngestionStatus == REJECTED`.
**Handler MUST:**
  - Return the list of supported MIME types in the fault payload.
  - Do not attempt content-type sniffing or fallback parsing.
**Notes:** The supported MIME type list is defined in the ISM configuration
  layer and is substrate-specific. Common supported types are
  `application/json` and `text/plain`. Binary formats require explicit
  registration. Do not add MIME types to this document — update the
  configuration layer.

---

## Domain CLS — Classification Faults

Emitted exclusively by `incident.classify`.

---

### INVALID_CATEGORY
**Code:** CLS-001
**Severity:** ERROR
**Recoverability:** RECOVERABLE
**Emitted by:** `incident.classify`
**Condition:** The `category` value is not a member of the `IncidentCategory`
  type registry (see `operator_grammar.md` Section 8).
**State effect:** None. Record remains in its current state.
**Handler MUST:**
  - Abort classification.
  - Return the invalid value and the full `IncidentCategory` enum in the
    fault payload.
**Notes:** Classifiers MUST validate `category` against the type registry
  before invoking this operator. If the appropriate category does not exist,
  use `UNKNOWN` and document the rationale in `subcategory`. Do not invent
  category tokens outside the registry — classification consistency depends
  on the closed taxonomy.

---

### CONFIDENCE_BELOW_THRESHOLD
**Code:** CLS-002
**Severity:** ERROR
**Recoverability:** RECOVERABLE
**Emitted by:** `incident.classify`
**Condition:** The `confidence` value is below `MIN_CLASSIFICATION_CONFIDENCE`
  (default: 0.70; see `operator_grammar.md` Section 9).
**State effect:** None. Record remains in its current state.
**Handler MUST:**
  - Abort classification.
  - Return the supplied `confidence` value and the current threshold in the
    fault payload.
**Notes:** Classifiers that cannot reach threshold confidence SHOULD invoke
  `incident.flag_uncertainty` with code `CLASSIFICATION_AMBIGUOUS` before
  surfacing the result for manual review. Do not lower `MIN_CLASSIFICATION_CONFIDENCE`
  to bypass this fault — doing so degrades all downstream surface mapping
  and planning accuracy. The threshold may be legitimately adjusted via
  the ISM configuration layer for specific substrate deployments.

---

## Domain SRF — Surface Mapping Faults

Emitted exclusively by `incident.map_surface_area`.

---

### EMPTY_SURFACE_LIST
**Code:** SRF-001
**Severity:** ERROR
**Recoverability:** RECOVERABLE
**Emitted by:** `incident.map_surface_area`
**Condition:** The `surfaces` list is empty (zero entries).
**State effect:** None.
**Handler MUST:**
  - Abort operator.
  - Return a fault indicating that at least one surface entry is required.
**Notes:** A zero-surface submission is almost always a scanner bug or a
  misconfigured scanner scope. If the incident genuinely touches no
  enumerable surfaces, operators should consider whether the classification
  was correct. A `SURFACE_INCOMPLETE` uncertainty flag is more appropriate
  than submitting zero surfaces.

---

### SURFACE_REF_INVALID
**Code:** SRF-002
**Severity:** ERROR
**Recoverability:** RECOVERABLE
**Emitted by:** `incident.map_surface_area`
**Condition:** One or more `surface_ref` values in the `surfaces` list are
  syntactically invalid for their declared `surface_type` (e.g., a `FILE`
  entry with a relative path, a `SECRET` entry with a malformed ARN, a
  `DEPENDENCY` entry missing the `package@version` format).
**State effect:** None.
**Handler MUST:**
  - Abort operator.
  - Return all invalid `surface_ref` values and their `surface_type` in
    the fault payload, not just the first one.
**Notes:** The substrate MUST validate all entries before accepting any.
  Partial surface maps with some valid and some invalid entries MUST be
  rejected in full — partial acceptance would produce a surface map that
  silently omits surfaces, violating scope completeness.

---

### SURFACE_LIMIT_EXCEEDED
**Code:** SRF-003
**Severity:** ERROR
**Recoverability:** OPERATOR_ACTION_REQUIRED
**Emitted by:** `incident.map_surface_area`
**Condition:** The `surfaces` list contains more entries than
  `MAX_SURFACE_ENTRIES` (default: 500; see `operator_grammar.md` Section 9).
**State effect:** None.
**Handler MUST:**
  - Abort operator.
  - Return `MAX_SURFACE_ENTRIES` and the actual submitted count in the
    fault payload.
**Notes:** Exceeding the surface limit almost always indicates either an
  overly broad scanner scope or an incident with an unusually large blast
  radius. Operators SHOULD consider splitting the incident into multiple
  child records via separate `incident.ingest` calls scoped to bounded
  surface clusters. Raising `MAX_SURFACE_ENTRIES` is a configuration change
  requiring explicit operator approval — it is not a per-call override.

---

### HASH_MISMATCH
**Code:** SRF-004
**Severity:** ERROR
**Recoverability:** RECOVERABLE
**Emitted by:** `incident.map_surface_area`
**Condition:** The `surface_snapshot_hash` value does not match the SHA-256
  hash computed by the substrate over the submitted `surfaces` list.
**State effect:** None.
**Handler MUST:**
  - Abort operator.
  - Return the expected hash (computed server-side) and the submitted hash
    in the fault payload.
  - Do NOT store the submitted surfaces, even temporarily.
**Notes:** This fault is the primary defense against in-transit surface list
  corruption or truncation. Callers MUST recompute the hash client-side
  immediately before submission using the same serialization order used to
  build the `surfaces` list. Hash computation must be over the canonical
  wire-format representation of the list, not an in-memory object graph.

---

## Domain PLN — Planning Faults

Emitted by `incident.derive_rectification_steps` and
`incident.generate_readonly_plan`.

---

### SURFACE_MAP_MISMATCH
**Code:** PLN-001
**Severity:** ERROR
**Recoverability:** OPERATOR_ACTION_REQUIRED
**Emitted by:** `incident.derive_rectification_steps`
**Condition:** The `surface_map_id` supplied does not match
  `IncidentRecord(record_id).surface_map_id`, or the referenced surface map
  has been superseded by a newer mapping on this record.
**State effect:** None.
**Handler MUST:**
  - Abort planning.
  - Return both the supplied `surface_map_id` and the current
    `IncidentRecord.surface_map_id` in the fault payload.
**Notes:** Plans MUST be derived against the current surface map only.
  Stale `surface_map_id` values indicate a race where the surface was
  re-mapped between the planner reading the record and submitting the plan.
  The planner must re-fetch the record, obtain the current `surface_map_id`,
  and re-derive all steps.

---

### STEP_INDEX_INVALID
**Code:** PLN-002
**Severity:** ERROR
**Recoverability:** RECOVERABLE
**Emitted by:** `incident.derive_rectification_steps`
**Condition:** The `steps` list contains one or more of: a non-zero-based
  index (first index is not 0), duplicate indices, gaps in the index
  sequence, or non-integer index values.
**State effect:** None.
**Handler MUST:**
  - Abort planning.
  - Return all invalid indices in the fault payload.
**Notes:** Steps MUST form a complete, gapless, 0-based integer sequence.
  The substrate uses `step_index` for ordered sequential execution — gaps
  or duplicates would produce ambiguous or skipped execution steps. Planners
  generating steps programmatically MUST sort and renumber before submission.

---

### UNKNOWN_OPERATOR_REF
**Code:** PLN-003
**Severity:** ERROR
**Recoverability:** RECOVERABLE
**Emitted by:** `incident.derive_rectification_steps`
**Condition:** One or more `operator_ref` values in the `steps` list do not
  resolve to a known `incident.execute.*` operator, or reference an operator
  outside the `incident.execute.*` namespace.
**State effect:** None.
**Handler MUST:**
  - Abort planning.
  - Return all unresolvable `operator_ref` values in the fault payload.
**Notes:** Planners MUST validate `operator_ref` values against the canonical
  operator registry before submission. Typos, version-suffixed refs, and
  references to deprecated operators are all invalid. References to operators
  outside `incident.execute.*` (e.g., `incident.classify`) are explicitly
  forbidden in plan steps — this is a grammar-level constraint, not a
  permissions boundary.

---

### TARGET_NOT_IN_SURFACE_MAP
**Code:** PLN-004
**Severity:** ERROR
**Recoverability:** RECOVERABLE
**Emitted by:** `incident.derive_rectification_steps`
**Condition:** One or more `target_ref` values in the `steps` list do not
  match any `surface_ref` in `SurfaceMap(surface_map_id)`.
**State effect:** None.
**Handler MUST:**
  - Abort planning.
  - Return all unmatched `target_ref` values alongside the available
    `surface_ref` values in the fault payload.
**Notes:** Plans MUST NOT introduce targets that were not declared in the
  surface map. This constraint enforces that execution operators cannot
  exceed the scanned and approved incident surface. If a required target is
  absent from the surface map, operators must re-run `incident.map_surface_area`
  with an updated surface list before re-planning.

---

### PLAN_STEP_LIMIT_EXCEEDED
**Code:** PLN-005
**Severity:** ERROR
**Recoverability:** OPERATOR_ACTION_REQUIRED
**Emitted by:** `incident.derive_rectification_steps`
**Condition:** The `steps` list contains more entries than `MAX_PLAN_STEPS`
  (default: 50; see `operator_grammar.md` Section 9).
**State effect:** None.
**Handler MUST:**
  - Abort planning.
  - Return `MAX_PLAN_STEPS` and the actual submitted step count in the
    fault payload.
**Notes:** Incidents requiring more than 50 rectification steps SHOULD be
  decomposed into multiple bounded incidents via `incident.ingest`, each
  with its own surface map and plan. A single plan with 50+ steps is a
  strong signal that the incident scope is too broad to remediate safely
  in one approval cycle.

---

### PLAN_ID_MISMATCH
**Code:** PLN-006
**Severity:** ERROR
**Recoverability:** RECOVERABLE
**Emitted by:** `incident.generate_readonly_plan`
**Condition:** The supplied `plan_id` does not match
  `IncidentRecord(record_id).plan_id`.
**State effect:** None. This is a `READONLY` operator; no state is
  modified regardless.
**Handler MUST:**
  - Abort operator.
  - Return both the supplied `plan_id` and the current
    `IncidentRecord.plan_id` in the fault payload.
**Notes:** This fault typically indicates a caller holding a stale plan
  reference. Re-fetch the record to obtain the current `plan_id` before
  retrying. Unlike `SURFACE_MAP_MISMATCH`, this fault carries lower urgency
  since the operator is read-only — but the caller must still correct
  its reference before calling any downstream operators.

---

### UNSUPPORTED_FORMAT
**Code:** PLN-007
**Severity:** ERROR
**Recoverability:** RECOVERABLE
**Emitted by:** `incident.generate_readonly_plan`
**Condition:** The `format` value is not a member of `{MARKDOWN, JSON, TEXT}`.
**State effect:** None.
**Handler MUST:**
  - Abort operator.
  - Return the list of supported `PlanFormat` values in the fault payload.
**Notes:** Format negotiation should happen at the call site before
  invoking this operator. Do not default to any format silently — if the
  requested format is not supported, fault and surface the constraint.

---

## Domain UNC — Uncertainty Faults

Emitted exclusively by `incident.flag_uncertainty`.

---

### UNKNOWN_UNCERTAINTY_CODE
**Code:** UNC-001
**Severity:** ERROR
**Recoverability:** RECOVERABLE
**Emitted by:** `incident.flag_uncertainty`
**Condition:** The `uncertainty_code` value is not a member of the
  `UncertaintyCode` registry.
**State effect:** None. No uncertainty flag is attached to the record.
**Handler MUST:**
  - Abort operator.
  - Return the full `UncertaintyCode` registry in the fault payload.
**Notes:** If no registered code adequately describes the uncertainty, use
  `OTHER` with a detailed `detail` field. The `UncertaintyCode` registry
  is closed — codes are not added at call time. Extension requests must
  go through the ISM grammar revision process.

---

### INSUFFICIENT_OTHER_DETAIL
**Code:** UNC-002
**Severity:** ERROR
**Recoverability:** RECOVERABLE
**Emitted by:** `incident.flag_uncertainty`
**Condition:** `uncertainty_code == OTHER` and `detail.length` is below
  `MIN_OTHER_DETAIL_LENGTH` (default: 80 characters; see
  `operator_grammar.md` Section 9).
**State effect:** None.
**Handler MUST:**
  - Abort operator.
  - Return the minimum required length and the actual submitted length
    in the fault payload.
**Notes:** The elevated minimum for `OTHER` exists because `OTHER` is the
  catch-all code and provides no structural information by itself. The
  `detail` field must carry sufficient context for a human reviewer to
  understand the uncertainty without any other context. Generic strings like
  "unknown error" or "see logs" are structurally valid but semantically
  insufficient — reviewers SHOULD be instructed to treat minimal `OTHER`
  flags as low-signal.

---

## Domain APV — Approval Flow Faults

Emitted by `incident.request_operator_approval` and
`incident.hold_for_review`.

---

### EMPTY_APPROVER_SET
**Code:** APV-001
**Severity:** ERROR
**Recoverability:** RECOVERABLE
**Emitted by:** `incident.request_operator_approval`
**Condition:** The `approver_set` list is empty (zero entries).
**State effect:** None. Record remains in `PLAN_DERIVED`.
**Handler MUST:**
  - Abort operator.
  - Require the caller to supply at least one `ApproverRef`.
**Notes:** Approval requests with no approvers would create a `PENDING_APPROVAL`
  record that can never be resolved — a deadlock state. This fault prevents
  that condition at the grammar level.

---

### UNKNOWN_APPROVER
**Code:** APV-002
**Severity:** ERROR
**Recoverability:** OPERATOR_ACTION_REQUIRED
**Emitted by:** `incident.request_operator_approval`
**Condition:** One or more `ApproverRef` values in `approver_set` do not
  resolve in the approver registry.
**State effect:** None. Record remains in `PLAN_DERIVED`.
**Handler MUST:**
  - Abort operator.
  - Return all unresolvable `ApproverRef` values in the fault payload.
  - Do not notify any approvers in the partial set.
**Notes:** Partial approval sets are never accepted — either all approvers
  resolve or none are notified. This prevents phantom approval requests
  where only some approvers receive notification. Unresolvable approvers
  must be registered in the approver registry by a substrate administrator
  before retry.

---

### BLOCKING_UNCERTAINTY_FLAGS
**Code:** APV-003
**Severity:** ERROR
**Recoverability:** OPERATOR_ACTION_REQUIRED
**Emitted by:** `incident.request_operator_approval`
**Condition:** The record has one or more attached `UncertaintyFlag` entries
  with severity `BLOCKING` that have not been resolved or explicitly
  acknowledged in `context_note`.
**State effect:** None. Record remains in `PLAN_DERIVED`.
**Handler MUST:**
  - Abort operator.
  - Return all unresolved blocking flag IDs and their `uncertainty_code`
    values in the fault payload.
**Notes:** Blocking uncertainty flags exist to prevent approval requests
  from proceeding when the plan cannot be safely evaluated. Operators must
  either resolve the underlying uncertainty (by re-running classification
  or surface mapping) or explicitly acknowledge each flag in `context_note`
  using the format: `"ACKNOWLEDGED: <flag_id> — <rationale>"`. Acknowledgment
  without rationale is not accepted.

---

### INVALID_APPROVAL_POLICY
**Code:** APV-004
**Severity:** ERROR
**Recoverability:** RECOVERABLE
**Emitted by:** `incident.request_operator_approval`
**Condition:** The `approval_policy` value is not a member of
  `{ANY_ONE, MAJORITY, ALL}`.
**State effect:** None.
**Handler MUST:**
  - Abort operator.
  - Return the valid `ApprovalPolicy` values in the fault payload.
**Notes:** `MAJORITY` requires an odd-numbered `approver_set` to avoid
  tie deadlocks. Implementations SHOULD warn (but not fault) when
  `approval_policy == MAJORITY` and `approver_set.count` is even. The
  substrate resolves majority ties in favor of rejection.

---

### UNKNOWN_HOLD_REASON
**Code:** APV-005
**Severity:** ERROR
**Recoverability:** RECOVERABLE
**Emitted by:** `incident.hold_for_review`
**Condition:** The `reason_code` value is not a member of the
  `HoldReason` registry.
**State effect:** None. Record is NOT placed on hold.
**Handler MUST:**
  - Abort operator.
  - Return the full `HoldReason` registry in the fault payload.
**Notes:** A failed hold attempt is particularly dangerous because the caller
  intended to stop execution but the hold was not placed. The caller MUST
  treat `UNKNOWN_HOLD_REASON` as equivalent to a failed safety brake and
  escalate immediately. Do not fall through to the next operation on the
  assumption that the hold succeeded.

---

### HOLD_UNAUTHORIZED
**Code:** APV-006
**Severity:** ERROR
**Recoverability:** OPERATOR_ACTION_REQUIRED
**Emitted by:** `incident.hold_for_review`
**Condition:** The `held_by` identity does not hold the required authorization
  to place a hold on this record. Authorization may be scoped by record
  classification, surface type, or organizational policy.
**State effect:** None. Record is NOT placed on hold.
**Handler MUST:**
  - Abort operator.
  - Log the unauthorized `held_by` identity and the record ID.
  - Escalate to a substrate administrator immediately if this occurs during
    an active execution sequence.
**Notes:** Same urgency note as `UNKNOWN_HOLD_REASON` — a failed hold during
  execution means the safety brake did not engage. The caller must not
  continue with execution steps and must escalate to obtain an authorized
  hold-placing identity before retrying.

---

## Domain EXE — Bounded Execution Faults

Emitted by `incident.execute.*` operators. All execution faults produce an
`ExecutionRecord` regardless of whether the step succeeded or failed — the
`ExecutionRecord` is the permanent audit trail.

---

### FILE_NOT_IN_SURFACE_MAP
**Code:** EXE-001
**Severity:** ERROR
**Recoverability:** OPERATOR_ACTION_REQUIRED
**Emitted by:** `incident.execute.remove_file`
**Condition:** The supplied `file_path` does not match any `FILE`-typed
  `surface_ref` in `SurfaceMap(IncidentRecord(record_id).surface_map_id)`.
**State effect:** None. File is not removed.
**Handler MUST:**
  - Abort operator.
  - Return the unmatched `file_path` and the list of FILE-typed surface
    entries in the fault payload.
  - Treat this as a scope boundary violation.
**Notes:** This fault is the execution-layer enforcement of Grammar Invariant 3
  (surface scope enforcement). A target absent from the surface map means
  the removal was not approved as part of the incident. If the file genuinely
  needs to be removed, re-map the surface, re-derive the plan, and re-seek
  approval.

---

### PATH_TRAVERSAL_DETECTED
**Code:** EXE-002
**Severity:** FATAL
**Recoverability:** UNRECOVERABLE
**Emitted by:** `incident.execute.remove_file`
**Condition:** The canonical resolution of `file_path` (after resolving
  symlinks, `..` components, and environment variable expansions) exits
  the declared substrate boundary, or targets a path that was not
  submitted as a surface entry.
**State effect:** `IncidentRecord.state` transitions to `FAULTED`.
  All remaining steps are cancelled.
**Handler MUST:**
  - Abort operator immediately. Do not access the file at any point.
  - Transition the record to `FAULTED`.
  - Log the submitted path and its resolved canonical form.
  - Alert substrate security operations immediately — this may indicate
    an adversarial plan or a compromised planning agent.
  - Preserve the submitted `file_path` value as forensic evidence.
**Notes:** This is a security-critical fault. Path traversal in an
  automated remediation system is a high-severity attack vector. The record
  is immediately terminal. A new investigation should be opened — potentially
  targeting the planning agent that submitted the traversal path — before
  any new ingestion is processed for related surfaces.

---

### SECRET_NOT_IN_SURFACE_MAP
**Code:** EXE-003
**Severity:** ERROR
**Recoverability:** OPERATOR_ACTION_REQUIRED
**Emitted by:** `incident.execute.rotate_secret`
**Condition:** The supplied `secret_ref` does not match any `SECRET`-typed
  `surface_ref` in `SurfaceMap(IncidentRecord(record_id).surface_map_id)`.
**State effect:** None. No rotation is initiated.
**Handler MUST:**
  - Abort operator.
  - Return the unmatched `secret_ref` in the fault payload.
  - Do not expose the list of known secret refs in the fault payload
    (enumeration risk).
**Notes:** Unlike `FILE_NOT_IN_SURFACE_MAP`, the fault payload MUST NOT
  enumerate the full set of SECRET-typed surface entries — doing so would
  leak information about the substrate's secret topology to the caller log.
  Callers should re-fetch the surface map directly to identify valid targets.

---

### ROTATION_UNAUTHORIZED
**Code:** EXE-004
**Severity:** ERROR
**Recoverability:** OPERATOR_ACTION_REQUIRED
**Emitted by:** `incident.execute.rotate_secret`
**Condition:** The executing agent does not hold rotation authorization for
  the target `secret_ref` in the secret management layer (e.g., AWS Secrets
  Manager, HashiCorp Vault, GCP Secret Manager).
**State effect:** None. No rotation is initiated.
**Handler MUST:**
  - Abort operator.
  - Log the executing agent identity and the `secret_ref` (reference only,
    never the secret value).
  - Do not retry with a different agent identity automatically.
**Notes:** Rotation authorization is granted at the secret management layer,
  not within ISM. If the executing agent lacks authorization, a substrate
  administrator must grant the appropriate IAM role, Vault policy, or
  equivalent before retry. This fault SHOULD trigger an
  `incident.flag_uncertainty` with code `AUTHORIZATION_AMBIGUOUS` for
  human awareness.

---

### ROTATION_PROVIDER_ERROR
**Code:** EXE-005
**Severity:** ERROR
**Recoverability:** RECOVERABLE
**Emitted by:** `incident.execute.rotate_secret`
**Condition:** The secret management provider returned an error during the
  rotation attempt (e.g., provider unavailable, rotation plugin failure,
  transient API error). The rotation was not completed.
**State effect:** None. The old secret version remains active.
**Handler MUST:**
  - Abort operator. Confirm with the provider that the rotation was not
    applied before allowing retry.
  - Log the provider error code and message in the `ExecutionRecord`.
  - Apply exponential backoff before retry.
**Notes:** Implementations MUST verify the rotation state with the provider
  before retrying — a provider error does not guarantee the rotation was
  not partially applied. If the provider cannot confirm the rotation state,
  treat as `PARTIAL_EXECUTION` (GEN-005) and transition the record to
  `FAULTED`.

---

### DEPENDENT_NOTIFICATION_FAILED
**Code:** EXE-006
**Severity:** WARNING
**Recoverability:** OPERATOR_ACTION_REQUIRED
**Emitted by:** `incident.execute.rotate_secret`
**Condition:** `notify_dependents == true` and the rotation completed
  successfully, but one or more registered secret consumers could not be
  notified of the new secret version.
**State effect:** None. The rotation itself succeeded; the record step is
  marked `STEP_EXECUTED` with a warning annotation. The `ExecutionRecord`
  is created.
**Handler MUST:**
  - Complete the step as `STEP_EXECUTED` (rotation was successful).
  - Annotate the `ExecutionRecord` with the list of consumers that
    failed to receive notification.
  - Create a follow-up flag automatically via `incident.execute.flag_for_followup`
    with code `MANUAL_REMEDIATION_REQUIRED` and assign it to the substrate
    operations team.
**Notes:** This is the only `WARNING`-severity fault in the registry. The
  rotation is complete and the old secret is invalidated — consumers that
  were not notified may begin failing. The follow-up flag is non-optional;
  unnotified consumers represent a live operational risk.

---

### DEPENDENCY_NOT_IN_SURFACE_MAP
**Code:** EXE-007
**Severity:** ERROR
**Recoverability:** OPERATOR_ACTION_REQUIRED
**Emitted by:** `incident.execute.patch_dependency`
**Condition:** The supplied `package_ref` does not match any
  `DEPENDENCY`-typed `surface_ref` in the approved surface map.
**State effect:** None. No patch is applied.
**Handler MUST:**
  - Abort operator.
  - Return the unmatched `package_ref` and the list of DEPENDENCY-typed
    surface entries in the fault payload.
**Notes:** See `EXE-001` (FILE_NOT_IN_SURFACE_MAP) — identical scope
  enforcement rationale applies. Package refs MUST use the canonical
  format `ecosystem:package@version` (e.g., `npm:lodash@4.17.20`) to
  enable unambiguous matching against surface entries.

---

### VERSION_MISMATCH
**Code:** EXE-008
**Severity:** ERROR
**Recoverability:** RECOVERABLE
**Emitted by:** `incident.execute.patch_dependency`
**Condition:** The `current_version` declared in `IN(...)` does not match
  the version of the package actually installed at `package_ref` in the
  target environment at execution time.
**State effect:** None. No patch is applied.
**Handler MUST:**
  - Abort operator.
  - Return `current_version` as supplied and the actual installed version
    discovered at execution time in the fault payload.
**Notes:** Version drift between plan derivation and execution time is
  the primary cause of this fault. If the installed version is already at
  or beyond `target_version`, the operator returns `ALREADY_AT_TARGET`
  rather than this fault. If the installed version is different from both
  `current_version` and `target_version`, the caller must re-derive the
  plan step with updated version values.

---

### TARGET_VERSION_INVALID
**Code:** EXE-009
**Severity:** ERROR
**Recoverability:** OPERATOR_ACTION_REQUIRED
**Emitted by:** `incident.execute.patch_dependency`
**Condition:** The `target_version` is marked deprecated, yanked, or
  retracted in the `package_manager` registry at execution time, OR
  `target_version` does not satisfy the semver constraint declared in
  the target's manifest, OR `target_version` is not a syntactically
  valid semver string.
**State effect:** None. No patch is applied.
**Handler MUST:**
  - Abort operator.
  - Return the reason for invalidity (deprecated, yanked, semver-invalid,
    manifest-constraint-violation) in the fault payload.
  - Never install a yanked or deprecated package.
**Notes:** A yanked `target_version` at execution time that was valid at
  plan derivation time indicates a supply chain event that occurred during
  the incident response window. Treat this as a signal that the plan
  needs to be re-derived with a new target version. Substrate operators
  SHOULD verify the new target version's provenance before re-approval.

---

### PACKAGE_MANAGER_ERROR
**Code:** EXE-010
**Severity:** ERROR
**Recoverability:** RECOVERABLE
**Emitted by:** `incident.execute.patch_dependency`
**Condition:** The package manager returned a non-zero exit code or error
  response during package installation, resolution, or lock file generation.
  The patch was not successfully applied.
**State effect:** The package manager should have rolled back; if it did
  not, `PARTIAL_EXECUTION` (GEN-005) supersedes this fault.
**Handler MUST:**
  - Abort operator.
  - Capture and log the full package manager error output in the
    `ExecutionRecord`.
  - Verify the package manager performed its own rollback before allowing
    retry.
  - Apply backoff before retry if the error is transient (e.g., registry
    timeout).
**Notes:** Common transient causes: package registry downtime, DNS failure,
  rate limiting. Common non-transient causes: dependency conflict,
  incompatible platform, missing system library. Non-transient errors
  require plan re-derivation with a compatible target package.

---

### UNKNOWN_FOLLOWUP_CODE
**Code:** EXE-011
**Severity:** ERROR
**Recoverability:** RECOVERABLE
**Emitted by:** `incident.execute.flag_for_followup`
**Condition:** The `followup_code` value is not a member of the
  `FollowupCode` registry.
**State effect:** None. No follow-up ticket is created.
**Handler MUST:**
  - Abort operator.
  - Return the full `FollowupCode` registry in the fault payload.
**Notes:** The `FollowupCode` registry is closed. Use `MANUAL_REMEDIATION_REQUIRED`
  as the general-purpose code when no more specific code applies.

---

### INVALID_PRIORITY
**Code:** EXE-012
**Severity:** ERROR
**Recoverability:** RECOVERABLE
**Emitted by:** `incident.execute.flag_for_followup`
**Condition:** The `priority` value is not a member of
  `{CRITICAL, HIGH, MEDIUM, LOW}`.
**State effect:** None. No follow-up ticket is created.
**Handler MUST:**
  - Abort operator.
  - Return the valid `FollowupPriority` values in the fault payload.
**Notes:** Implementations MUST NOT default to any priority value silently.
  Priority must be explicitly supplied by the caller for every follow-up flag.

---

### EMPTY_ASSIGNEE_LIST
**Code:** EXE-013
**Severity:** ERROR
**Recoverability:** RECOVERABLE
**Emitted by:** `incident.execute.flag_for_followup`
**Condition:** The `assigned_to` list is empty (zero entries).
**State effect:** None. No follow-up ticket is created.
**Handler MUST:**
  - Abort operator.
  - Require the caller to supply at least one assignee identifier.
**Notes:** Unassigned follow-up tickets are operationally dead — they will
  never be actioned. The substrate requires at least one assignee to ensure
  accountability. If the correct assignee is unknown, use a team or role
  identifier from the operator registry.

---

### UNRESOLVABLE_ASSIGNEE
**Code:** EXE-014
**Severity:** ERROR
**Recoverability:** OPERATOR_ACTION_REQUIRED
**Emitted by:** `incident.execute.flag_for_followup`
**Condition:** One or more identifiers in `assigned_to` do not resolve in
  the operator registry.
**State effect:** None. No follow-up ticket is created.
**Handler MUST:**
  - Abort operator.
  - Return all unresolvable identifiers in the fault payload.
  - Do not create a partial ticket with only resolved assignees.
**Notes:** All assignees must be resolvable before the ticket is created.
  Partial assignment creates accountability gaps. Unresolvable identifiers
  must be registered in the operator registry by a substrate administrator.

---

### INSUFFICIENT_RISK_DETAIL
**Code:** EXE-015
**Severity:** ERROR
**Recoverability:** RECOVERABLE
**Emitted by:** `incident.execute.flag_for_followup`
**Condition:** `followup_code == RISK_ACCEPTED` and `detail.length` is below
  `MIN_RISK_ACCEPTANCE_DETAIL_LENGTH` (default: 150 characters; see
  `operator_grammar.md` Section 9).
**State effect:** None. No follow-up ticket is created.
**Handler MUST:**
  - Abort operator.
  - Return the minimum required length and the actual submitted length
    in the fault payload.
**Notes:** Risk acceptance is a formal act with audit implications.
  The elevated minimum detail length ensures that risk acceptance decisions
  are substantively documented — not rubber
