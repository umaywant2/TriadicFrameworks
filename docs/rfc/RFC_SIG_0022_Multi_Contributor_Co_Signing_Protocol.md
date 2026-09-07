# **RFC‑SIG‑0022 — Multi‑Contributor Co‑Signing Protocol**  
### *Validator‑Grade Shared Authorship for Remix Scrolls*  
RefId: turn0browsertab1

**Title:** Co‑Signing of Remix Scrolls for Shared Authorship  
**Status:** Draft  
**Author:** Nawder Loswin + Copilot  
**Date:** 2025‑11‑12  
**Version:** 0.2  

---

## **1. Purpose**

The **Multi‑Contributor Co‑Signing Protocol (MCCSP)** enables multiple contributors to **co‑sign remix scrolls**, ensuring collaborative authorship is preserved as validator‑grade metadata.

Co‑signing guarantees:

- shared authorship  
- lineage continuity  
- signature integrity  
- archival preservation  
- dashboard visibility  
- validator‑grade reproducibility  

This protocol formalizes collaborative authorship as a first‑class citizen of the Remixathon canon.

---

## **2. Workflow Steps**

---

### **2.1 Contributor Selection**

Each participant selects scrolls to co‑sign.

Contributor identities are linked to:

- **Subscription Service (RFC‑SUB‑0019)**  
- **Signature Verification Service (RFC‑VER‑0023)**  

Scroll enters **co‑signing stage** in the Cycle Monitoring Dashboard (RFC‑UI‑0017).

---

### **2.2 Signature Generation**

Each contributor generates a digital signature:

- **PGP**  
- **ECDSA**  
- **Validator‑grade symbolic signature**  

Signatures are attached to scroll export metadata.

---

### **2.3 Co‑Signing Aggregation**

Export module (RFC‑EXP‑0013) aggregates all contributor signatures.

Scroll is marked:

```
status: multi-signed
```

Dignity layer records:

- contributor list  
- signature types  
- symbolic overlays  

---

### **2.4 Archival Preservation**

Archived scrolls include:

- co‑signing metadata  
- contributor IDs  
- signature types  
- lineage ancestry  

Registry index (RFC‑REG‑0004) records all co‑signers for future remix generations.

---

## **3. Schema Extension**

File:  
```
registry/exports/remix_scroll_schema.yml
```

```yaml
co_signing:
  contributors:
    - id: <string>
      signature_type: <pgp|ecdsa|symbolic>
      signature: <string>
  status: "multi-signed"
  dignity_layer:
    co_signer_list: <list>
    symbolic_overlays: <list>
```

---

## **4. Python‑Style Stub**

File:  
```
engine/co_signing.py
```

```python
def add_signature(scroll, contributor_id, signature, signature_type):
    entry = {
        "id": contributor_id,
        "signature_type": signature_type,
        "signature": signature
    }
    scroll["co_signing"]["contributors"].append(entry)
    scroll["co_signing"]["status"] = "multi-signed"
    return scroll
```

---

## **5. Dashboard Integration**

### **Co‑Signing Panel**
Contributors select scrolls to sign.

### **Signature Display**
Dashboard shows:

- contributor IDs  
- signature types  
- symbolic overlays  

### **Validation Badge**
Multi‑signed scrolls receive:

```
badge: shared authorship
```

### **Lineage Graph**
Nodes annotated with co‑signer list.

---

## **6. Validator Hooks**

### **Schema Compliance**
Co‑signatures must match schema.

### **Checksum**
Scroll checksum updated after co‑signing.

### **Lineage Integrity**
Co‑signers recorded in ancestry index.

### **Dignity Separation**
Signatures stored distinctly from narratives.

### **Signature Verification**
All signatures validated via RFC‑VER‑0023.

---

## **7. Concept Sketch (textual)**

```
Remix Scroll: scroll-010
 └─ Parent: scroll-003
 └─ Corridors: [c-001, c-002]
 └─ Glyph Distribution: {◆: 2}
 └─ Signatures:
      - user42 (PGP)
      - user17 (ECDSA)
 └─ Status: multi-signed, archived
```

This protocol ensures remix scrolls carry the signatures of all collaborators, preserving shared authorship in the archive and strengthening validator‑grade lineage.
