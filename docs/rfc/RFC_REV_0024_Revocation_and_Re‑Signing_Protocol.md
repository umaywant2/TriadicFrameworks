# **RFC‑REV‑0024 — Revocation and Re‑Signing Protocol**  
### *Validator‑Grade Signature Revocation, Replacement, and Lineage Continuity*  
RefId: turn0browsertab1

**Title:** Signature Revocation and Re‑Signing for Remix Scrolls  
**Status:** Draft  
**Author:** Nawder Loswin + Copilot  
**Date:** 2025‑11‑12  
**Version:** 0.2  

---

## **1. Purpose**

The **Revocation and Re‑Signing Protocol (RRSP)** provides contributors with a secure, lineage‑safe mechanism to:

- revoke compromised signatures  
- replace them with new signatures  
- preserve collaborative authorship  
- maintain validator‑grade authenticity  
- ensure remix lineage continuity  

RRSP ensures that revocation does **not** break ancestry, does **not** erase dignity, and does **not** invalidate scrolls — it simply updates authorship state while preserving historical trace.

---

## **2. Workflow Overview**

RRSP defines a five‑stage revocation → re‑signing lifecycle.

---

### **2.1 Revocation Request**

Contributor submits a revocation event citing:

- compromised key  
- lost private key  
- accidental exposure  
- contributor‑initiated reset  
- validator‑initiated security event  

Registry marks signature as **revoked** in the verification schema.

Scroll remains valid but flagged **pending re‑signing**.

---

### **2.2 Re‑Signing Invitation**

Triggered automatically via:

- **Subscription Protocol (RFC‑SUB‑0019)**  
- **Alert Orchestration (RFC‑ALR‑0020)**  

Contributors receive:

- dashboard notification  
- email/WebSocket alert  
- lineage graph highlight  

Scroll enters **re‑signing stage** in the Cycle Monitoring Dashboard (RFC‑UI‑0017).

---

### **2.3 Signature Replacement**

Contributor generates a new signature:

- **PGP**  
- **ECDSA**  
- **symbolic signature**  
- **multi‑contributor co‑signing (RFC‑SIG‑0022)**  

New signature is appended to scroll metadata.

Revoked signature is preserved in the **dignity layer** for historical trace.

---

### **2.4 Lineage Continuity Update**

Registry updates lineage index:

```
revoked_signature → replacement_signature
```

Lineage graph shows:

- authorship continuity  
- revocation event  
- re‑signing event  
- contributor identity stability  

Scroll ancestry remains unbroken.

---

### **2.5 Verification Report Update**

Signature Verification Service (RFC‑VER‑0023):

- re‑validates scroll  
- updates contributor status  
- marks scroll as **authorship re‑signed**  
- issues updated verification badge  

---

## **3. Schema Extension**

File:  
```
registry/signatures/revocation_schema.yml
```

```yaml
revocation_event:
  scroll_id: <string>
  contributor_id: <string>
  revoked_signature: <string>
  reason: <string>
  timestamp: <datetime>
  replacement_signature: <string|null>
  dignity_layer:
    preserved_revoked_signature: true
    notes: <string>
  lineage_update:
    parent_signature: <string>
    child_signature: <string>
  checksum: <string>
```

---

## **4. API Endpoints**

### **POST /signatures/revoke**  
Submit revocation event.

### **POST /signatures/resign**  
Submit replacement signature.

### **GET /signatures/status/{scroll_id}**  
Retrieve signature status for a scroll.

### **GET /signatures/history/{contributor_id}**  
View contributor’s revocation/re‑sign history.

---

## **5. Python‑Style Stub**

File:  
```
api/revocation_service.py
```

```python
def revoke_signature(scroll_id, contributor_id, reason):
    event = {
        "scroll_id": scroll_id,
        "contributor_id": contributor_id,
        "reason": reason,
        "revoked_signature": get_current_signature(scroll_id),
        "timestamp": now(),
        "replacement_signature": None
    }
    save_revocation_event(event)
    mark_signature_revoked(scroll_id)
    notify_contributors(scroll_id)
    return event

def resign_signature(scroll_id, contributor_id, new_signature):
    event = {
        "scroll_id": scroll_id,
        "contributor_id": contributor_id,
        "replacement_signature": new_signature,
        "timestamp": now()
    }
    append_signature(scroll_id, new_signature)
    update_lineage(scroll_id)
    update_verification_report(scroll_id)
    return event
```

---

## **6. Dashboard Integration**

### **Revocation Panel**
Contributors submit revocation requests.

### **Re‑Signing Panel**
Contributors upload replacement signatures.

### **Lineage Graph Overlay**
Nodes show:

```
revoked → re‑signed
```

### **Verification Badge**
Scroll marked **authorship re‑signed** once validated.

---

## **7. Validator Hooks**

### **Schema Compliance**
Revocation events must match `revocation_schema.yml`.

### **Checksum**
Each revocation/re‑sign event includes reproducibility checksum.

### **Lineage Integrity**
Revoked signatures preserved in ancestry index.

### **Dignity Separation**
Revocation reasons stored separately from cultural narratives.

### **Continuity Guarantee**
Scroll lineage must remain unbroken.

---

## **8. Concept Sketch (textual)**

```
Scroll: scroll-010
 └─ Contributor: user42
 └─ Signature: revoked (reason: compromised)
 └─ Replacement Signature: valid (PGP)
 └─ Status: re-signed
 └─ Lineage: scroll-003 → scroll-010 (authorship continuity preserved)
```

RRSP ensures compromised signatures can be revoked and replaced **without breaking lineage continuity**, preserving validator‑grade authenticity and collaborative dignity.
