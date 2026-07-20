# Substrate Error Registry — Incident Substrate Model
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
