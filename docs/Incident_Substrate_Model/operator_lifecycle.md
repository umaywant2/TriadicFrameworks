# Operator Lifecycle — Incident Substrate Model
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
