# RFC‑REV‑0024: Revocation and Re‑Signing Protocol

**Title:** Signature Revocation and Re‑Signing for Remix Scrolls  
**Status:** Draft  
**Author:** Nawder Loswin + Copilot  
**Date:** 2025‑11‑12  
**Version:** 0.1  

---

## 1. Purpose
Provide contributors with a secure mechanism to revoke compromised signatures and re‑sign scrolls without breaking lineage continuity. This ensures validator‑grade authenticity while maintaining collaborative authorship across remix generations.

---

## 2. Workflow Steps

1. **Revocation Request**  
   - Contributor submits revocation event citing compromised signature.  
   - Registry marks signature as *revoked* in verification schema.  
   - Scroll remains valid but flagged for re‑signing.

2. **Re‑Signing Invitation**  
   - Contributors notified via subscription service (RFC‑SUB‑0019).  
   - Scroll enters “pending re‑signing” stage in cycle monitoring dashboard.  

3. **Signature Replacement**  
   - Contributor generates new signature (PGP/ECDSA/symbolic).  
   - New signature appended to scroll metadata.  
   - Revoked signature preserved in dignity layer for historical trace.

4. **Lineage Continuity**  
   - Scroll lineage index updated to include both revoked and re‑signed events.  
   - Ancestry graph shows continuity: revoked signature → re‑signed signature.  

5. **Verification Report Update**  
   - Signature Verification Service (RFC‑VER‑0023) re‑validates scroll.  
   - Report updated with new contributor status.  

---

## 3. Schema Extension

File: [`registry/signatures/revocation_schema.yml`](https://github.com/umaywant2/TriadicFrameworks/blob/main/docs/registry/signatures/revocation_schema.yml)

---

## 4. API Endpoints

- `POST /signatures/revoke` → Submit revocation event.  
- `POST /signatures/resign` → Submit replacement signature.  
- `GET /signatures/status/{scroll_id}` → Retrieve signature status for a scroll.  
- `GET /signatures/history/{contributor_id}` → View contributor’s revocation/re‑sign history.  

---

## 5. Python‑style Stub

File: [`api/revocation_service.py`](https://github.com/umaywant2/TriadicFrameworks/blob/main/docs/api/revocation_service.py)

---

## 6. Dashboard Integration

- **Revocation Panel:** Contributors submit revocation requests.  
- **Re‑Signing Panel:** Contributors upload replacement signatures.  
- **Lineage Graph Overlay:** Nodes show revoked → re‑signed transitions.  
- **Verification Badge:** Scroll marked “authorship re‑signed” once validated.  

---

## 7. Validator Hooks

- **Schema compliance:** Revocation events must match `revocation_schema.yml`.  
- **Checksum:** Each revocation/re‑sign event includes checksum for reproducibility.  
- **Lineage integrity:** Revoked signatures preserved in ancestry index.  
- **Dignity separation:** Revocation reasons stored distinctly from narratives.  

---

## 8. Concept Sketch (textual)

```
Scroll: scroll-010
 └─ Contributor: user42
 └─ Signature: revoked (reason: compromised)
 └─ Replacement Signature: valid (PGP)
 └─ Status: re-signed
 └─ Lineage: scroll-003 → scroll-010 (authorship continuity preserved)
```

---

This **Revocation and Re‑Signing Protocol** ensures compromised signatures can be revoked and replaced without breaking lineage continuity, preserving validator‑grade authenticity and collaborative dignity.  
