# **Browser UI Mockup — Incident Substrate Model**  
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
┌───────────────────────────────────────────────────────────────┐
│  ⚠️ Incident Substrate Model — Browser UI                      │
├───────────────────────────────────────────────────────────────┤
│  [Incident Source Input]   [Ingest Button]                    │
│                                                               │
│  ┌───────────────────────────────────────────────────────────┐ │
│  │ Incident Intel (Read‑Only)                                │ │
│  │ - CVE / Advisory / Vendor Post                            │ │
│  │ - Extracted Signals                                       │ │
│  │ - Relevant Vectors                                        │ │
│  └───────────────────────────────────────────────────────────┘ │
│                                                               │
│  ┌───────────────────────────────────────────────────────────┐ │
│  │ Classification                                             │ │
│  │ - Type: Supply‑Chain / Dependency / Credential / CI/CD    │ │
│  │ - Confidence Score                                         │ │
│  └───────────────────────────────────────────────────────────┘ │
│                                                               │
│  ┌───────────────────────────────────────────────────────────┐ │
│  │ Surface Area Mapping                                       │ │
│  │ - Files                                                    │ │
│  │ - Dependencies                                             │ │
│  │ - Workflows                                                │ │
│  │ - Secrets                                                  │ │
│  └───────────────────────────────────────────────────────────┘ │
│                                                               │
│  ┌───────────────────────────────────────────────────────────┐ │
│  │ Rectification Plan (Read‑Only)                             │ │
│  │ - Proposed Steps                                           │ │
│  │ - Uncertainties                                            │ │
│  │ - Required Operator Actions                                │ │
│  └───────────────────────────────────────────────────────────┘ │
│                                                               │
│  [Approve Plan]   [Reject Plan]   [Flag for Review]           │
└───────────────────────────────────────────────────────────────┘
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
