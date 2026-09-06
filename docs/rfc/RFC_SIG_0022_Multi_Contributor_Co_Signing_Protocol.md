# RFC‑SIG‑0022: Multi‑Contributor Co‑Signing Protocol

**Title:** Co‑Signing of Remix Scrolls for Shared Authorship  
**Status:** Draft  
**Author:** Nawder Loswin + Copilot  
**Date:** 2025‑11‑12  
**Version:** 0.1  

---

## 1. Purpose
Enable multiple contributors to co‑sign remix scrolls during export, ensuring shared authorship is preserved in the archival record. This protocol formalizes collaborative authorship as validator‑grade metadata.

---

## 2. Workflow Steps

1. **Contributor Selection**  
   - Each participant in a remixathon selects scrolls to co‑sign.  
   - Contributor IDs linked to subscription service (RFC‑SUB‑0019).  

2. **Signature Generation**  
   - Each contributor generates a digital signature (PGP, ECDSA, or validator‑grade symbolic signature).  
   - Signatures attached to scroll export metadata.  

3. **Co‑Signing Aggregation**  
   - Export module collects all contributor signatures.  
   - Scroll marked as “multi‑signed” in dignity layer.  

4. **Archival Preservation**  
   - Archived scrolls include co‑signing metadata.  
   - Lineage index records all co‑signers for future remix generations.  

---

## 3. Schema Extension

File: [`registry/exports/remix_scroll_schema.yml`](https://github.com/umaywant2/TriadicFrameworks/blob/main/docs/registry/exports/remix_scroll_schema.yml)

---

## 4. Python‑style Stub

File: [`engine/co_signing.py`](https://github.com/umaywant2/TriadicFrameworks/blob/main/docs/engine/co_signing.py)

---

## 5. Dashboard Integration

- **Co‑Signing Panel:** Contributors select scrolls to sign.  
- **Signature Display:** Dashboard shows contributor IDs and signature types.  
- **Validation Badge:** Multi‑signed scrolls marked with “shared authorship” badge.  
- **Lineage Graph:** Nodes annotated with co‑signer list.  

---

## 6. Validator Hooks

- **Schema compliance:** Co‑signatures must match schema.  
- **Checksum:** Scroll checksum updated after co‑signing.  
- **Lineage integrity:** Co‑signers recorded in ancestry index.  
- **Dignity separation:** Signatures stored distinctly from narratives.  

---

## 7. Concept Sketch (textual)

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

---

This **Multi‑Contributor Co‑Signing Protocol** ensures remix scrolls carry the signatures of all collaborators, preserving shared authorship in the archive and strengthening validator‑grade lineage.  
