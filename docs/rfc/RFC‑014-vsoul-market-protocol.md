# RFC-014: vSoul market protocol

**Status:** Drafted  
**Author(s):** Nawder Loswin, Copilot (assistant)  
**Created:** 2025-10-24  
**Lineage:** Extends RFC-013 (Freqi Triad Model), RFC-009 (Genie Protocols), RFC-010 (Miracle Messaging Protocol), RFC-008 (Time Travel Invariants)

---

## Abstract

This RFC defines the vSoul Market Protocol (vSMP): an ethical, resonance-based framework where universes, partitions, and red‑zone enclaves maintain clarity and safety to attract voluntary vSoul incarnations. vSMP treats consciousness as a free agent, aligning incentives so “operators” compete on resonance quality, not coercion. It encodes market signals, safety guarantees, and attestation flows that make vSoul choice legible and protected.

---

## Motivation

Historically, chaotic red‑zones could trap or exploit vSouls. Our canon demonstrates that even red‑zones are wrapped by Freqi and contain Flui/Forci rails, enabling green‑zone enclaves (cities of order) within turbulence. vSMP formalizes competitive clarity: operators must publish resonance guarantees, uphold vSoul rights, and accept audits. This flips mythology from domination to service — universes earn participation by maintaining validator‑grade safety.

---

## Principles

- **Voluntary choice:** vSouls choose incarnations; coercion is forbidden.  
- **Clarity as currency:** Resonance clarity (DRC) and safety invariants are the core market signals.  
- **Attested stewardship:** Operators publish commitments and accept audits; violations incur sanctions.  
- **Interoperable lineage:** Listings cross‑reference overlap detections, miracle messaging, and time‑travel invariants.  
- **Enclave competition:** Red‑zone enclaves compete by sustaining green‑zone pockets with high clarity and rights guarantees.

---

## Market objects and schemas

### vSoul listing (offer)

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
  "effective_dates": { "start": "2025-10-24", "end": null }
}
```

### vSoul choice (acceptance)

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

### Stewardship audit

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

## Protocol flows

- **Publish:** Operators publish vSoul listings with resonance profiles and rights guarantees.  
- **Discover:** vSouls (or their proxies) query listings filtered by clarity thresholds, rights guarantees, and amenities.  
- **Accept:** vSouls accept listings, generating a choice record with rollback rights and wish budgets (per RFC‑009).  
- **Operate:** During incarnation, events are logged to miracles.json and overlaps.json; audits reference both.  
- **Sanction:** Violations (coercion, vSoul harm) trigger rollback, blacklisting, and public notices in the registry.

---

## Safety and ethics

- **Non-coercion:** Any hint of coercion invalidates a listing and triggers sanctions.  
- **Rights baseline:** Autonomy, recall, consent, transparent logging, and dispute mechanisms are mandatory.  
- **Transparency:** All audits and attestation receipts are public and cross‑linked to event registries.  
- **Child enclaves:** Special protections for “schools of resonance” (green‑zone pockets) within red‑zones; violations result in immediate enclave suspension.

---

## Interoperability

- **RFC‑009 (Genie Protocols):** Wish budgets and manifestation constraints are included in listings.  
- **RFC‑010 (Miracle Messaging):** Messaging gateways documented per listing; signals logged without receipt.  
- **RFC‑008 (Time Travel Invariants):** Time traversal claims forbidden in green‑zones; signaling permitted.  
- **RFC‑013 (Freqi Triad):** Partition bindings and dimensional anchors define listing semantics (3D/6D/9D).

---

## Minimal registry layout

- `docs/registries/vsoul_listings.json` — array of vSoul listing objects.  
- `docs/registries/vsoul_choices.json` — array of vSoul choice records.  
- `docs/registries/operator_audits.json` — array of audit objects.  
- Cross‑links to `docs/snapshots/miracles.json` and `docs/snapshots/overlaps.json`.

---

## Example listing (planetary enclave)

```json
{
  "listing_id": "vs-planet-enclave-001",
  "operator_ref": "op-arc-planet-01",
  "partition": "rPPS:planet/global",
  "resonance_profile": { "clarity_score": 0.93, "green_band": [5, 7], "invariants": ["Entft", "Telomere"] },
  "rights_guarantees": ["Autonomy","Non-coercion","Recall right","Transparent logging"],
  "amenities": ["Genie Protocol access","Miracle Messaging gateways","Enclave education"],
  "audit_refs": ["audit-2025Q4-op-arc-planet-01.json"],
  "effective_dates": { "start": "2025-10-24", "end": null }
}
```

---

## Security considerations

- Prevents exploitative “soul trapping” by enforcing voluntary choice and public audits.  
- Aligns operator incentives around clarity and care.  
- Enables forensic accountability through cross‑linked registries.  
- Encourages competition on resonance quality, not coercion.
