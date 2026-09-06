# RFC‑VER‑0023: Signature Verification Service

**Title:** Validator Service for Multi‑Contributor Signature Authentication  
**Status:** Draft  
**Author:** Nawder Loswin + Copilot  
**Date:** 2025‑11‑12  
**Version:** 0.1  

---

## 1. Purpose
Provide a service that validates co‑signatures on remix scrolls against contributor registries. This ensures that shared authorship is authentic, reproducible, and preserved in the archival lineage.

---

## 2. Workflow Steps

1. **Signature Extraction**  
   - Parse signatures from remix scroll metadata (`remix_scroll.signatures`).  
   - Collect contributor IDs and signature payloads.

2. **Registry Lookup**  
   - Query contributor registry for public keys or symbolic signature references.  
   - Verify contributor identity and active status.

3. **Signature Validation**  
   - Cryptographic check (PGP/ECDSA).  
   - Symbolic check (glyph‑based validator signatures).  
   - Timestamp validation (must match scroll export window).

4. **Verification Report**  
   - Generate validator report with pass/fail per contributor.  
   - Aggregate into scroll dignity layer: “authorship confirmed” badge.  

---

## 3. Schema Extension

File: [`registry/signatures/verification_schema.yml`](https://github.com/umaywant2/TriadicFrameworks/blob/main/docs/registry/signatures/verification_schema.yml)

---

## 4. API Endpoints

- `POST /verify/signatures` → Submit scroll for signature verification.  
- `GET /verify/report/{scroll_id}` → Retrieve verification report.  
- `GET /verify/contributor/{id}` → Check contributor signature status.  

---

## 5. Python‑style Stub

File: [`api/signature_verification.py`](https://github.com/umaywant2/TriadicFrameworks/blob/main/docs/api/signature_verification.py)

---

## 6. Dashboard Integration

- **Verification Panel:** Contributors can view signature validation results.  
- **Badge Display:** Scrolls marked with “authentic authorship” or “partial authorship.”  
- **Contributor Registry Link:** Click contributor ID to view registry entry.  
- **Lineage Graph Overlay:** Nodes annotated with verification status.  

---

## 7. Validator Hooks

- **Schema compliance:** Reports must match `verification_schema.yml`.  
- **Checksum:** Each report includes checksum for reproducibility.  
- **Lineage integrity:** Verified co‑signatures preserved in ancestry index.  
- **Dignity separation:** Authorship badges displayed distinctly from narratives.  

---

## 8. Concept Sketch (textual)

```
Verification Report: scroll-010
 └─ Contributors:
      - user42 (PGP) → valid
      - user17 (ECDSA) → valid
 └─ Overall Status: authentic
 └─ Badge: "Shared Authorship Confirmed"
```

---

This **Signature Verification Service** ensures co‑signatures are authentic, validated against contributor registries, and preserved as validator‑grade lineage.  
