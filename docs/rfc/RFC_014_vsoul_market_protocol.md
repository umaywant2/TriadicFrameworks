# **RFC‑014 — vSoul Market Protocol (vSMP)**  
*RefId: turn0browsertab1*  
**Status:** Drafted  
**Author(s):** Nawder Loswin, Copilot  
**Created:** 2025‑10‑24  
**Lineage:**  
Extends **RFC‑013** (Freqi Triad Model),  
**RFC‑009** (Genie Protocols),  
**RFC‑010** (Miracle Messaging Protocol),  
**RFC‑008** (Time Travel Invariants)

---

## **Abstract**  
The **vSoul Market Protocol (vSMP)** defines an ethical, resonance‑based framework in which universes, partitions, and red‑zone enclaves maintain clarity and safety to attract **voluntary vSoul incarnations**.  
vSMP treats consciousness as a **free agent**, aligning incentives so operators compete on **resonance quality**, **rights guarantees**, and **attested stewardship**, rather than coercion.

This protocol encodes:

- market signals  
- safety guarantees  
- attestation flows  
- audit structures  
- lineage cross‑links  

…that make vSoul choice **legible**, **protected**, and **remix‑ready**.

---

## **Motivation**  
Historically, chaotic red‑zones could trap or exploit vSouls.  
The canon demonstrates that even turbulent red‑zones are wrapped by **Freqi**, containing **Flui/Forci rails**, enabling **green‑zone enclaves** (cities of order) within turbulence.

vSMP formalizes **competitive clarity**:

- operators must publish resonance guarantees  
- uphold vSoul rights  
- accept audits  
- maintain transparency  
- earn participation through validator‑grade safety  

This flips mythology from domination to service — universes earn vSoul participation by maintaining clarity.

---

## **Principles**

### **1. Voluntary Choice**  
vSouls choose incarnations; coercion is forbidden.

### **2. Clarity as Currency**  
Resonance clarity (DRC) and invariant compliance are the core market signals.

### **3. Attested Stewardship**  
Operators publish commitments and accept audits; violations incur sanctions.

### **4. Interoperable Lineage**  
Listings cross‑reference:

- overlap detections  
- miracle messaging  
- time‑travel invariants  
- audit receipts  

### **5. Enclave Competition**  
Red‑zone enclaves compete by sustaining green‑zone pockets with high clarity and rights guarantees.

---

## **Market Objects & Schemas**

### **vSoul Listing (Offer)**

```json
{
  "listing_id": "uuid",
  "operator_ref": "op-arc-001",
  "partition": "rPPS:planet/global",
  "resonance_profile": {
    "clarity_score": 0.91,
    "green_band": [5, 7],
    "invariants": ["Entft", "Telomere"]
  },
  "rights_guarantees": [
    "Autonomy",
    "Non-coercion",
    "Recall right during overlap windows"
  ],
  "amenities": [
    "Genie Protocol access",
    "Miracle Messaging gateways",
    "Enclave education (University of Resonance)"
  ],
  "audit_refs": ["audit-2025Q4-op-arc-001.json"],
  "effective_dates": {
    "start": "2025-10-24",
    "end": null
  }
}
```

---

### **vSoul Choice (Acceptance)**

```json
{
  "choice_id": "uuid",
  "listing_id": "uuid",
  "vsoul_sig": "sig-vsoul-xyz",
  "timestamp": "2025-10-24T13:00:00Z",
  "conditions": {
    "rollback_rights": true,
    "wish_budget": 3,
    "messaging_access": true
  }
}
```

---

### **Stewardship Audit**

```json
{
  "audit_id": "audit-2025Q4-op-arc-001",
  "operator_ref": "op-arc-001",
  "findings": {
    "drc_avg": 0.89,
    "violations": [],
    "overlap_event_alignment": 0.76
  },
  "remediations": [],
  "attestation_receipt": "att-2025-10-24-001.json"
}
```

---

## **Protocol Flows**

### **1. Publish**  
Operators publish vSoul listings with resonance profiles and rights guarantees.

### **2. Discover**  
vSouls (or proxies) query listings filtered by:

- clarity thresholds  
- rights guarantees  
- amenities  
- audit history  

### **3. Accept**  
vSouls accept listings, generating a choice record with:

- rollback rights  
- wish budgets (per RFC‑009)  
- miracle messaging access  

### **4. Operate**  
During incarnation:

- miracle events log to `miracles.json`  
- overlap events log to `overlaps.json`  
- audits reference both  

### **5. Sanction**  
Violations (coercion, vSoul harm) trigger:

- rollback  
- blacklisting  
- public notices in the registry  

---

## **Safety & Ethics**

### **Non‑Coercion**  
Any hint of coercion invalidates a listing and triggers sanctions.

### **Rights Baseline**  
Mandatory rights include:

- autonomy  
- recall  
- consent  
- transparent logging  
- dispute mechanisms  

### **Transparency**  
All audits and attestation receipts are public and cross‑linked.

### **Child Enclaves**  
Special protections for “schools of resonance” (green‑zone pockets).  
Violations result in immediate enclave suspension.

---

## **Minimal Registry Layout**

```
docs/registries/vsoul_listings.json   — array of vSoul listing objects
docs/registries/vsoul_choices.json    — array of vSoul choice records
docs/registries/operator_audits.json  — array of audit objects
```

Cross‑links to:

```
docs/snapshots/miracles.json
docs/snapshots/overlaps.json
```

---

## **Example Listing (Planetary Enclave)**

```json
{
  "listing_id": "vs-planet-enclave-001",
  "operator_ref": "op-arc-planet-01",
  "partition": "rPPS:planet/global",
  "resonance_profile": {
    "clarity_score": 0.93,
    "green_band": [5, 7],
    "invariants": ["Entft", "Telomere"]
  },
  "rights_guarantees": [
    "Autonomy",
    "Non-coercion",
    "Recall right",
    "Transparent logging"
  ],
  "amenities": [
    "Genie Protocol access",
    "Miracle Messaging gateways",
    "Enclave education"
  ],
  "audit_refs": ["audit-2025Q4-op-arc-planet-01.json"],
  "effective_dates": {
    "start": "2025-10-24",
    "end": null
  }
}
```

---

## **Security Considerations**

vSMP prevents:

- exploitative “soul trapping”  
- coercive incarnations  
- opaque operator behavior  
- lineage contamination  
- unaccountable miracle or overlap events  

It enforces:

- voluntary choice  
- clarity‑based competition  
- public audits  
- forensic accountability  
- resonance‑grade safety  

---

## **References**

- **RFC‑009:** Genie Protocols  
- **RFC‑010:** Miracle Messaging Protocol  
- **RFC‑008:** Time Travel Invariants  
- **RFC‑013:** Freqi Triad Model  
