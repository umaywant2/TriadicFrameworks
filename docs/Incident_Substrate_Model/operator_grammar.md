# Operator Grammar — Incident Substrate Model
**Document:** `operator_grammar.md`
**Path:** `/docs/Incident_Substrate_Model/operator_grammar.md`
**Revision:** RTT/1 · Canon Edition
**Status:** Authoritative
**Issued:** 2026-05-20

---

## Preamble

This document defines the complete operator grammar for the **Incident Substrate Model (ISM)** within the TriadicFrameworks canon. All operators are specified under the **RTT/1** (Recursive Triadic Taxonomy, version 1) protocol.

### RTT/1 Grammar Conventions

| Convention | Meaning |
|---|---|
| `OPERATOR` | Fully-qualified operator identifier in dot-namespace notation |
| `IN(...)` | Required input fields; typed and ordered |
| `OUT(...)` | Emitted output fields; typed and deterministic |
| `PRE[...]` | Precondition predicates — must all evaluate `true` before execution |
| `POST[...]` | Postcondition assertions — must all hold immediately after execution |
| `GUARD(...)` | Operator-level safety gates; failure aborts the operator |
| `YIELDS →` | Terminal state transition emitted on success |
| `FAULTS →` | Named fault states; each must be handled by the calling substrate |
| `MODE` | Execution mode: `READONLY`, `MUTATING`, or `APPROVAL_GATED` |
| `IDEMPOTENT` | Operator may be safely retried without side-effect accumulation |

All operators are **deterministic**: identical inputs under identical substrate state must produce identical outputs. Non-determinism is a grammar fault.

Operators marked `READONLY` must not alter any persisted substrate state. Operators marked `MUTATING` must declare all state transitions in `POST[...]`. Operators marked `APPROVAL_GATED` must not proceed past their `GUARD(...)` until an approval token is present in `IN(...)`.

Namespace prefix `incident.` scopes all operators to the ISM substrate. Sub-namespace `incident.execute.*` is reserved for bounded, reversible-or-acknowledged execution operators only.

---

## 1. Operator Family: Ingestion

---

### `incident.ingest`

**MODE:** `MUTATING` · **IDEMPOTENT:** Yes (keyed on `signal_id`)

**Purpose:** Accept a raw incident signal from any upstream emitter and normalize it into a canonical ISM `IncidentRecord`. This is the sole entry point for external signal traffic into the substrate.

```
OPERATOR  incident.ingest

IN(
  signal_id      : UUID,          -- Emitter-assigned unique signal identifier
  source         : String,        -- Emitter identity (service name, sensor label, etc.)
  raw_payload    : Bytes,         -- Unprocessed signal body; encoding declared by content_type
  content_type   : MIME,          -- e.g. "application/json", "text/plain"
  emitted_at     : Timestamp,     -- Emitter-side emission time (UTC ISO-8601)
  severity_hint  : SeverityHint?  -- Optional emitter-declared severity; may be overridden downstream
)

OUT(
  record_id      : UUID,          -- ISM-assigned canonical record identifier
  ingested_at    : Timestamp,     -- Substrate-side ingestion time (UTC ISO-8601)
  status         : IngestionStatus -- ACCEPTED | DUPLICATE | REJECTED
)

PRE[
  signal_id is syntactically valid UUID,
  source is non-empty and registered in the emitter registry,
  raw_payload byte length > 0,
  content_type is a supported MIME type,
  emitted_at <= substrate_clock.now()
]

POST[
  status == ACCEPTED  →  IncidentRecord(record_id) exists in substrate with state = INGESTED,
  status == DUPLICATE →  no new record created; existing record_id returned,
  status == REJECTED  →  no record created; fault emitted
]

GUARD(
  emitter is authorized: source ∈ allowed_emitter_set,
  payload size <= MAX_PAYLOAD_BYTES
)

YIELDS  → INGESTED
FAULTS  → UNAUTHORIZED_EMITTER | PAYLOAD_TOO_LARGE | MALFORMED_SIGNAL | UNSUPPORTED_CONTENT_TYPE
```

---

## 2. Operator Family: Classification

---

### `incident.classify`

**MODE:** `MUTATING` · **IDEMPOTENT:** No (classification may evolve; each call is versioned)

**Purpose:** Assign a structured classification to an `IncidentRecord`. Classification is versioned — successive calls append a new `ClassificationVersion` rather than overwriting, preserving the full classification history on the record.

```
OPERATOR  incident.classify

IN(
  record_id      : UUID,          -- Target IncidentRecord
  classifier_id  : String,        -- Identity of the classifying agent or model
  category       : IncidentCategory,  -- Primary taxonomy node (e.g. SECRET_LEAK, DEPENDENCY_CVE)
  subcategory    : String?,        -- Optional free-form subcategory label
  confidence     : Float[0.0,1.0], -- Classifier confidence in this classification
  rationale      : String          -- Human-readable classification rationale
)

OUT(
  record_id      : UUID,
  classification_version : UInt,   -- Monotonically increasing version index on this record
  effective_at   : Timestamp
)

PRE[
  IncidentRecord(record_id) exists,
  IncidentRecord(record_id).state ∈ {INGESTED, CLASSIFIED, SURFACE_MAPPED},
  confidence ∈ [0.0, 1.0],
  rationale is non-empty
]

POST[
  IncidentRecord(record_id).classification == ClassificationVersion(classification_version),
  IncidentRecord(record_id).state == CLASSIFIED,
  classification_version == previous_version + 1
]

GUARD(
  classifier_id is registered,
  confidence >= MIN_CLASSIFICATION_CONFIDENCE  -- substrate-configured threshold
)

YIELDS  → CLASSIFIED
FAULTS  → RECORD_NOT_FOUND | INVALID_CATEGORY | CONFIDENCE_BELOW_THRESHOLD | INVALID_STATE_TRANSITION
```

---

## 3. Operator Family: Surface Mapping

---

### `incident.map_surface_area`

**MODE:** `MUTATING` · **IDEMPOTENT:** Yes (keyed on `record_id` + `surface_snapshot_hash`)

**Purpose:** Enumerate all substrate surfaces (files, secrets, dependencies, services, configurations) that the classified incident touches. The surface area map is the authoritative scope boundary for all downstream rectification and execution operators.

```
OPERATOR  incident.map_surface_area

IN(
  record_id         : UUID,
  scanner_id        : String,               -- Identity of the surface scanner agent
  surfaces          : List<SurfaceEntry>,   -- See SurfaceEntry schema below
  surface_snapshot_hash : Hash              -- Content hash of the surfaces list for idempotency
)

-- SurfaceEntry schema:
--   surface_type   : SurfaceType  (FILE | SECRET | DEPENDENCY | SERVICE | CONFIG)
--   surface_ref    : String       (path, ARN, package@version, service name, config key)
--   access_mode    : AccessMode   (READ | WRITE | EXECUTE | UNKNOWN)
--   confidence     : Float[0.0,1.0]
--   notes          : String?

OUT(
  record_id         : UUID,
  surface_map_id    : UUID,       -- Stable identifier for this surface map snapshot
  surface_count     : UInt,
  mapped_at         : Timestamp
)

PRE[
  IncidentRecord(record_id) exists,
  IncidentRecord(record_id).state == CLASSIFIED,
  surfaces is non-empty,
  all surface_ref values are syntactically valid for their surface_type,
  surface_snapshot_hash == hash(surfaces)
]

POST[
  IncidentRecord(record_id).surface_map_id == surface_map_id,
  IncidentRecord(record_id).state == SURFACE_MAPPED,
  SurfaceMap(surface_map_id).entries.count == surface_count
]

GUARD(
  scanner_id is registered,
  surface_count <= MAX_SURFACE_ENTRIES  -- prevents unbounded scope creep
)

YIELDS  → SURFACE_MAPPED
FAULTS  → RECORD_NOT_FOUND | INVALID_STATE_TRANSITION | EMPTY_SURFACE_LIST
         | SURFACE_REF_INVALID | SURFACE_LIMIT_EXCEEDED | HASH_MISMATCH
```

---

## 4. Operator Family: Rectification Planning

---

### `incident.derive_rectification_steps`

**MODE:** `MUTATING` · **IDEMPOTENT:** No (step derivation is versioned per surface map)

**Purpose:** Derive an ordered, bounded list of rectification steps from the surface area map. Each step maps to exactly one `incident.execute.*` operator. This operator does not execute anything — it produces a typed, operator-bound plan only.

```
OPERATOR  incident.derive_rectification_steps

IN(
  record_id      : UUID,
  surface_map_id : UUID,
  planner_id     : String,           -- Identity of the planning agent
  steps          : List<RectificationStep>  -- See RectificationStep schema below
)

-- RectificationStep schema:
--   step_index     : UInt          (0-based; must be unique and gapless)
--   operator_ref   : OperatorRef   (must resolve to an incident.execute.* operator)
--   target_ref     : String        (must exist in SurfaceMap(surface_map_id).entries)
--   parameters     : Map<String,Any>
--   reversible     : Bool
--   rationale      : String

OUT(
  record_id      : UUID,
  plan_id        : UUID,
  step_count     : UInt,
  derived_at     : Timestamp
)

PRE[
  IncidentRecord(record_id) exists,
  IncidentRecord(record_id).state == SURFACE_MAPPED,
  IncidentRecord(record_id).surface_map_id == surface_map_id,
  steps is non-empty,
  step indices are 0-based, unique, and gapless,
  all operator_ref values resolve to valid incident.execute.* operators,
  all target_ref values exist in SurfaceMap(surface_map_id).entries
]

POST[
  IncidentRecord(record_id).plan_id == plan_id,
  IncidentRecord(record_id).state == PLAN_DERIVED,
  RectificationPlan(plan_id).steps.count == step_count
]

GUARD(
  planner_id is registered,
  step_count <= MAX_PLAN_STEPS,
  all operator_ref values are within the incident.execute.* namespace only
)

YIELDS  → PLAN_DERIVED
FAULTS  → RECORD_NOT_FOUND | INVALID_STATE_TRANSITION | SURFACE_MAP_MISMATCH
         | STEP_INDEX_INVALID | UNKNOWN_OPERATOR_REF | TARGET_NOT_IN_SURFACE_MAP
         | PLAN_STEP_LIMIT_EXCEEDED
```

---

### `incident.generate_readonly_plan`

**MODE:** `READONLY` · **IDEMPOTENT:** Yes

**Purpose:** Render a human-readable, read-only representation of the current `RectificationPlan` for review. This operator does not modify any substrate state. It is the canonical gate before `incident.request_operator_approval`.

```
OPERATOR  incident.generate_readonly_plan

IN(
  record_id      : UUID,
  plan_id        : UUID,
  format         : PlanFormat   -- MARKDOWN | JSON | TEXT
)

OUT(
  record_id      : UUID,
  plan_id        : UUID,
  rendered_plan  : String,      -- Plan body in requested format; no executable content
  rendered_at    : Timestamp
)

PRE[
  IncidentRecord(record_id) exists,
  IncidentRecord(record_id).plan_id == plan_id,
  IncidentRecord(record_id).state ∈ {PLAN_DERIVED, PENDING_APPROVAL, APPROVED, HOLD},
  format ∈ {MARKDOWN, JSON, TEXT}
]

POST[
  no substrate state modified,
  rendered_plan is non-empty,
  rendered_plan contains no embedded operator invocations or executable directives
]

GUARD(
  rendered_plan must not contain control characters or script injection patterns
)

YIELDS  → (no state transition; read-only)
FAULTS  → RECORD_NOT_FOUND | PLAN_NOT_FOUND | PLAN_ID_MISMATCH | UNSUPPORTED_FORMAT
```

---

### `incident.flag_uncertainty`

**MODE:** `MUTATING` · **IDEMPOTENT:** Yes (keyed on `record_id` + `uncertainty_code`)

**Purpose:** Attach a structured uncertainty annotation to a record when the substrate or a planning agent lacks sufficient confidence to proceed without human review. Flagging uncertainty does not block the record — it enriches the approval context and may trigger escalation routing.

```
OPERATOR  incident.flag_uncertainty

IN(
  record_id        : UUID,
  flagging_agent   : String,
  uncertainty_code : UncertaintyCode,  -- See UncertaintyCode registry below
  affected_field   : String?,          -- Optional pointer to the uncertain field or step
  detail           : String            -- Human-readable description of the uncertainty
)

-- UncertaintyCode registry:
--   CLASSIFICATION_AMBIGUOUS    -- Multiple categories plausible with similar confidence
--   SURFACE_INCOMPLETE          -- Scanner may have missed surfaces
--   STEP_REVERSIBILITY_UNKNOWN  -- Cannot confirm if a rectification step is reversible
--   AUTHORIZATION_AMBIGUOUS     -- Approver set is unclear
--   EXTERNAL_DEPENDENCY_UNKNOWN -- Third-party behavior required for rectification is unverified
--   OTHER                       -- Catch-all; detail is mandatory when used

OUT(
  record_id        : UUID,
  flag_id          : UUID,
  flagged_at       : Timestamp
)

PRE[
  IncidentRecord(record_id) exists,
  uncertainty_code ∈ UncertaintyCode registry,
  detail is non-empty,
  if uncertainty_code == OTHER then detail.length >= MIN_OTHER_DETAIL_LENGTH
]

POST[
  UncertaintyFlag(flag_id) attached to IncidentRecord(record_id),
  IncidentRecord(record_id).uncertainty_flags.count increased by 1
]

GUARD(
  flagging_agent is registered
)

YIELDS  → (no state transition; annotation only)
FAULTS  → RECORD_NOT_FOUND | UNKNOWN_UNCERTAINTY_CODE | EMPTY_DETAIL
         | INSUFFICIENT_OTHER_DETAIL
```

---

## 5. Operator Family: Approval Flow

---

### `incident.request_operator_approval`

**MODE:** `APPROVAL_GATED` · `MUTATING` · **IDEMPOTENT:** No

**Purpose:** Formally request human operator approval for the `RectificationPlan`. Transitions the record to `PENDING_APPROVAL` and notifies the designated approver set. No `incident.execute.*` operator may proceed until this request is satisfied.

```
OPERATOR  incident.request_operator_approval

IN(
  record_id        : UUID,
  plan_id          : UUID,
  requesting_agent : String,
  approver_set     : List<ApproverRef>,  -- At least one approver required
  approval_policy  : ApprovalPolicy,    -- ANY_ONE | MAJORITY | ALL
  context_note     : String?            -- Optional note for the approver set
)

OUT(
  record_id        : UUID,
  approval_request_id : UUID,
  requested_at     : Timestamp,
  approver_count   : UInt
)

PRE[
  IncidentRecord(record_id) exists,
  IncidentRecord(record_id).plan_id == plan_id,
  IncidentRecord(record_id).state == PLAN_DERIVED,
  approver_set is non-empty,
  all ApproverRef values are resolvable in the approver registry,
  approval_policy ∈ {ANY_ONE, MAJORITY, ALL}
]

POST[
  IncidentRecord(record_id).state == PENDING_APPROVAL,
  IncidentRecord(record_id).approval_request_id == approval_request_id,
  approver_set notified via substrate notification channel
]

GUARD(
  requesting_agent is registered,
  plan_id refers to a non-empty, validated RectificationPlan,
  record has no open uncertainty flags with severity >= BLOCKING
    unless explicitly acknowledged in context_note
)

YIELDS  → PENDING_APPROVAL
FAULTS  → RECORD_NOT_FOUND | PLAN_NOT_FOUND | INVALID_STATE_TRANSITION
         | EMPTY_APPROVER_SET | UNKNOWN_APPROVER | BLOCKING_UNCERTAINTY_FLAGS
         | INVALID_APPROVAL_POLICY
```

---

### `incident.hold_for_review`

**MODE:** `MUTATING` · **IDEMPOTENT:** Yes (hold is idempotent if reason matches existing hold)

**Purpose:** Place a record into a `HOLD` state, suspending all pending execution. A hold may be placed at any point after `PLAN_DERIVED`. Holds must be explicitly released by an authorized operator before execution can resume. This operator is the primary safety brake in the ISM approval flow.

```
OPERATOR  incident.hold_for_review

IN(
  record_id    : UUID,
  held_by      : String,      -- Identity of the hold-placing operator or agent
  reason_code  : HoldReason,  -- See HoldReason registry below
  detail       : String,      -- Mandatory detail regardless of reason_code
  resume_after : Timestamp?   -- Optional: earliest time hold may be lifted
)

-- HoldReason registry:
--   MANUAL_REVIEW_REQUESTED
--   BLOCKING_UNCERTAINTY
--   APPROVAL_DISPUTED
--   EXTERNAL_DEPENDENCY_PENDING
--   POLICY_ESCALATION
--   SUBSTRATE_FAULT

OUT(
  record_id   : UUID,
  hold_id     : UUID,
  held_at     : Timestamp,
  prior_state : RecordState   -- State the record was in before hold
)

PRE[
  IncidentRecord(record_id) exists,
  IncidentRecord(record_id).state ∈ {PLAN_DERIVED, PENDING_APPROVAL, APPROVED},
  reason_code ∈ HoldReason registry,
  detail is non-empty
]

POST[
  IncidentRecord(record_id).state == HOLD,
  IncidentRecord(record_id).hold_id == hold_id,
  HoldRecord(hold_id).prior_state == prior_state,
  all queued incident.execute.* steps for record_id are suspended
]

GUARD(
  held_by is authorized to place holds on this record
)

YIELDS  → HOLD
FAULTS  → RECORD_NOT_FOUND | INVALID_STATE_TRANSITION | UNKNOWN_HOLD_REASON
         | HOLD_UNAUTHORIZED | EMPTY_DETAIL
```

---

## 6. Operator Family: Bounded Execution

All `incident.execute.*` operators share these invariants:

> **Execution Invariants (apply to all operators in this family)**
> 1. Target must exist in `SurfaceMap` of the parent `IncidentRecord`.
> 2. Parent record must be in state `APPROVED`.
> 3. No execution operator may exceed the scope declared in the approved `RectificationPlan`.
> 4. Each execution operator emits an immutable `ExecutionRecord` on completion (success or fault).
> 5. Faulted executions must not leave targets in a partially-modified state without a `PARTIAL_EXECUTION` fault being emitted.
> 6. Operators with `reversible: false` steps require explicit step-level re-acknowledgment at execution time.

---

### `incident.execute.remove_file`

**MODE:** `MUTATING` · **IDEMPOTENT:** Yes (if file absent, reports ALREADY_ABSENT)

**Purpose:** Remove a specific file declared in the surface area map. Removal is logged immutably. The file path must exactly match a `FILE`-typed surface entry in the approved plan.

```
OPERATOR  incident.execute.remove_file

IN(
  record_id     : UUID,
  plan_id       : UUID,
  step_index    : UInt,
  file_path     : String,       -- Absolute canonical path; must match surface entry exactly
  checksum      : Hash?,        -- Optional pre-removal checksum for audit
  dry_run       : Bool          -- If true, validate only; do not remove
)

OUT(
  record_id      : UUID,
  execution_id   : UUID,
  status         : ExecutionStatus,  -- REMOVED | ALREADY_ABSENT | DRY_RUN_OK
  removed_at     : Timestamp?,
  prior_checksum : Hash?
)

PRE[
  IncidentRecord(record_id).state == APPROVED,
  IncidentRecord(record_id).plan_id == plan_id,
  RectificationPlan(plan_id).steps[step_index].operator_ref == "incident.execute.remove_file",
  RectificationPlan(plan_id).steps[step_index].target_ref == file_path,
  file_path ∈ SurfaceMap(IncidentRecord(record_id).surface_map_id) with surface_type == FILE
]

POST[
  dry_run == false AND status == REMOVED →
    file at file_path no longer exists,
    ExecutionRecord(execution_id) created with status REMOVED,
  dry_run == true →
    no filesystem state changed,
    ExecutionRecord(execution_id) created with status DRY_RUN_OK
]

GUARD(
  executor has filesystem write access to file_path,
  file_path does not resolve outside declared substrate boundaries (no path traversal)
)

YIELDS  → STEP_EXECUTED
FAULTS  → RECORD_NOT_FOUND | PLAN_STEP_MISMATCH | FILE_NOT_IN_SURFACE_MAP
         | ACCESS_DENIED | PATH_TRAVERSAL_DETECTED | PARTIAL_EXECUTION
         | CHECKSUM_MISMATCH
```

---

### `incident.execute.rotate_secret`

**MODE:** `MUTATING` · **IDEMPOTENT:** No (each rotation produces a new secret version)

**Purpose:** Rotate a secret (API key, credential, token, certificate) declared in the surface area map. The old secret value is invalidated and the new value is stored via the substrate's secret management layer. The new secret value is never emitted in `OUT`.

```
OPERATOR  incident.execute.rotate_secret

IN(
  record_id         : UUID,
  plan_id           : UUID,
  step_index        : UInt,
  secret_ref        : String,         -- ARN, vault path, or secret identifier; must match surface entry
  rotation_policy   : RotationPolicy, -- IMMEDIATE | SCHEDULED
  notify_dependents : Bool            -- If true, substrate notifies registered secret consumers
)

OUT(
  record_id          : UUID,
  execution_id       : UUID,
  status             : ExecutionStatus,  -- ROTATED | SCHEDULED
  new_secret_version : String,           -- Version identifier only; NOT the secret value
  rotated_at         : Timestamp?
)

PRE[
  IncidentRecord(record_id).state == APPROVED,
  IncidentRecord(record_id).plan_id == plan_id,
  RectificationPlan(plan_id).steps[step_index].operator_ref == "incident.execute.rotate_secret",
  RectificationPlan(plan_id).steps[step_index].target_ref == secret_ref,
  secret_ref ∈ SurfaceMap(IncidentRecord(record_id).surface_map_id) with surface_type == SECRET,
  rotation_policy ∈ {IMMEDIATE, SCHEDULED}
]

POST[
  status == ROTATED →
    old secret version invalidated in secret management layer,
    new_secret_version active,
    notify_dependents == true → dependent consumers notified,
  ExecutionRecord(execution_id) created,
  new secret value never stored in ExecutionRecord or any ISM log
]

GUARD(
  executor has secret rotation authorization for secret_ref,
  new secret value is never written to OUT or any audit log (zero-secret-value guarantee)
)

YIELDS  → STEP_EXECUTED
FAULTS  → RECORD_NOT_FOUND | PLAN_STEP_MISMATCH | SECRET_NOT_IN_SURFACE_MAP
         | ROTATION_UNAUTHORIZED | ROTATION_PROVIDER_ERROR | PARTIAL_EXECUTION
         | DEPENDENT_NOTIFICATION_FAILED
```

---

### `incident.execute.patch_dependency`

**MODE:** `MUTATING` · **IDEMPOTENT:** Yes (keyed on `record_id` + `package_ref` + `target_version`)

**Purpose:** Apply a dependency patch — upgrading or pinning a package to a declared target version. The dependency must be declared in the surface area map as a `DEPENDENCY`-typed surface entry. Patch application is followed by a deterministic verification step.

```
OPERATOR  incident.execute.patch_dependency

IN(
  record_id       : UUID,
  plan_id         : UUID,
  step_index      : UInt,
  package_ref     : String,          -- Package identifier, e.g. "npm:lodash" or "pypi:requests"
  current_version : String,          -- Version being replaced; must match installed version
  target_version  : String,          -- Version to install; must be a known-good release
  package_manager : PackageManager,  -- NPM | PIP | CARGO | MAVEN | GRADLE | OTHER
  verify_checksum : Hash?,           -- Optional expected checksum of target package
  dry_run         : Bool
)

OUT(
  record_id       : UUID,
  execution_id    : UUID,
  status          : ExecutionStatus,  -- PATCHED | DRY_RUN_OK | ALREADY_AT_TARGET
  patched_version : String?,
  patched_at      : Timestamp?
)

PRE[
  IncidentRecord(record_id).state == APPROVED,
  IncidentRecord(record_id).plan_id == plan_id,
  RectificationPlan(plan_id).steps[step_index].operator_ref == "incident.execute.patch_dependency",
  RectificationPlan(plan_id).steps[step_index].target_ref == package_ref,
  package_ref ∈ SurfaceMap(IncidentRecord(record_id).surface_map_id) with surface_type == DEPENDENCY,
  current_version is semver-valid,
  target_version is semver-valid,
  target_version > current_version OR target_version is an explicit pinned release
]

POST[
  dry_run == false AND status == PATCHED →
    package at package_ref upgraded to target_version,
    verify_checksum provided → checksum verified against installed package,
    ExecutionRecord(execution_id) created,
  dry_run == true →
    no package state changed,
    ExecutionRecord(execution_id) created with DRY_RUN_OK
]

GUARD(
  executor has write access to the dependency manifest and lock file,
  target_version is not marked deprecated or yanked in package_manager registry,
  verify_checksum provided → checksum must match before activation
)

YIELDS  → STEP_EXECUTED
FAULTS  → RECORD_NOT_FOUND | PLAN_STEP_MISMATCH | DEPENDENCY_NOT_IN_SURFACE_MAP
         | VERSION_MISMATCH | TARGET_VERSION_INVALID | PACKAGE_MANAGER_ERROR
         | CHECKSUM_MISMATCH | PARTIAL_EXECUTION
```

---

### `incident.execute.flag_for_followup`

**MODE:** `MUTATING` · **IDEMPOTENT:** Yes (keyed on `record_id` + `followup_code`)

**Purpose:** Mark a surface entry or plan step as requiring post-incident follow-up action that cannot be completed within the current remediation window. This operator closes the step without mutating the target, emitting a structured follow-up ticket into the substrate's tracking layer.

```
OPERATOR  incident.execute.flag_for_followup

IN(
  record_id       : UUID,
  plan_id         : UUID,
  step_index      : UInt,
  target_ref      : String,           -- Surface entry or step reference being deferred
  followup_code   : FollowupCode,     -- See FollowupCode registry below
  priority        : FollowupPriority, -- CRITICAL | HIGH | MEDIUM | LOW
  assigned_to     : List<String>,     -- Assignee identifiers; at least one required
  due_by          : Timestamp?,       -- Optional deadline
  detail          : String            -- Mandatory description of follow-up action required
)

-- FollowupCode registry:
--   MANUAL_REMEDIATION_REQUIRED     -- Step requires human action beyond substrate capability
--   THIRD_PARTY_COORDINATION        -- Remediation depends on external party
--   DEFERRAL_APPROVED               -- Approved deferral; reason documented in detail
--   RISK_ACCEPTED                   -- Risk explicitly accepted; documented in detail
--   MONITORING_REQUIRED             -- No action now; ongoing monitoring required

OUT(
  record_id    : UUID,
  execution_id : UUID,
  followup_id  : UUID,            -- Tracking ticket identifier
  status       : ExecutionStatus, -- FLAGGED
  flagged_at   : Timestamp
)

PRE[
  IncidentRecord(record_id).state == APPROVED,
  IncidentRecord(record_id).plan_id == plan_id,
  RectificationPlan(plan_id).steps[step_index].operator_ref == "incident.execute.flag_for_followup",
  followup_code ∈ FollowupCode registry,
  priority ∈ {CRITICAL, HIGH, MEDIUM, LOW},
  assigned_to is non-empty,
  detail is non-empty
]

POST[
  FollowupTicket(followup_id) created in substrate tracking layer,
  FollowupTicket(followup_id).assigned_to == assigned_to,
  ExecutionRecord(execution_id) created with status FLAGGED,
  step_index marked FLAGGED_FOR_FOLLOWUP in RectificationPlan(plan_id)
]

GUARD(
  all assigned_to identifiers resolvable in operator registry,
  if followup_code == RISK_ACCEPTED →
    detail.length >= MIN_RISK_ACCEPTANCE_DETAIL_LENGTH
)

YIELDS  → STEP_EXECUTED
FAULTS  → RECORD_NOT_FOUND | PLAN_STEP_MISMATCH | UNKNOWN_FOLLOWUP_CODE
         | INVALID_PRIORITY | EMPTY_ASSIGNEE_LIST | UNRESOLVABLE_ASSIGNEE
         | INSUFFICIENT_RISK_DETAIL | EMPTY_DETAIL
```

---

## 7. State Machine

The canonical ISM record state machine governs legal state transitions. Only transitions listed below are valid; all others are grammar faults.

```
INGESTED
  → CLASSIFIED            via  incident.classify
  → HOLD                  via  incident.hold_for_review

CLASSIFIED
  → SURFACE_MAPPED        via  incident.map_surface_area
  → CLASSIFIED            via  incident.classify            (re-classification; version++)
  → HOLD                  via  incident.hold_for_review

SURFACE_MAPPED
  → PLAN_DERIVED          via  incident.derive_rectification_steps
  → CLASSIFIED            via  incident.classify            (reclassify; resets to CLASSIFIED)
  → HOLD                  via  incident.hold_for_review

PLAN_DERIVED
  → PENDING_APPROVAL      via  incident.request_operator_approval
  → HOLD                  via  incident.hold_for_review

PENDING_APPROVAL
  → APPROVED              via  [approval resolution: external to grammar]
  → PLAN_DERIVED          via  [approval rejection: external to grammar]
  → HOLD                  via  incident.hold_for_review

HOLD
  → [prior_state]         via  [hold release: external to grammar; restores prior_state]

APPROVED
  → EXECUTING             via  [first incident.execute.* invocation]
  → HOLD                  via  incident.hold_for_review

EXECUTING
  → RESOLVED              via  [all plan steps STEP_EXECUTED or FLAGGED_FOR_FOLLOWUP]
  → HOLD                  via  incident.hold_for_review
  → FAULTED               via  [any PARTIAL_EXECUTION fault on any step]

RESOLVED   -- Terminal: no further state transitions permitted
FAULTED    -- Terminal: requires manual intervention; may spawn new record via incident.ingest
```

---

## 8. Type Registry

```
UUID              ::= RFC 4122 v4 UUID string
Timestamp         ::= ISO-8601 UTC datetime string, precision to milliseconds
Hash              ::= SHA-256 hex digest string (64 hex characters)
MIME              ::= IANA-registered MIME type string
SeverityHint      ::= CRITICAL | HIGH | MEDIUM | LOW | UNKNOWN
IncidentCategory  ::= SECRET_LEAK | DEPENDENCY_CVE | MISCONFIGURATION | UNAUTHORIZED_ACCESS
                    | DATA_EXPOSURE | SUPPLY_CHAIN | POLICY_VIOLATION | UNKNOWN
SurfaceType       ::= FILE | SECRET | DEPENDENCY | SERVICE | CONFIG
AccessMode        ::= READ | WRITE | EXECUTE | UNKNOWN
IngestionStatus   ::= ACCEPTED | DUPLICATE | REJECTED
ExecutionStatus   ::= REMOVED | ROTATED | PATCHED | FLAGGED | ALREADY_ABSENT
                    | ALREADY_AT_TARGET | DRY_RUN_OK | SCHEDULED
RecordState       ::= INGESTED | CLASSIFIED | SURFACE_MAPPED | PLAN_DERIVED
                    | PENDING_APPROVAL | APPROVED | EXECUTING | HOLD | RESOLVED | FAULTED
PlanFormat        ::= MARKDOWN | JSON | TEXT
ApprovalPolicy    ::= ANY_ONE | MAJORITY | ALL
PackageManager    ::= NPM | PIP | CARGO | MAVEN | GRADLE | OTHER
FollowupPriority  ::= CRITICAL | HIGH | MEDIUM | LOW
OperatorRef       ::= Fully-qualified dot-namespace string resolving to an incident.execute.* operator
ApproverRef       ::= Opaque string resolvable in the approver registry
```

---

## 9. Substrate Constants

These values are substrate-configured and must be overridden via the ISM configuration layer, not hardcoded in operator implementations.

| Constant | Default | Description |
|---|---|---|
| `MAX_PAYLOAD_BYTES` | 10 485 760 (10 MiB) | Maximum raw_payload size for ingestion |
| `MIN_CLASSIFICATION_CONFIDENCE` | 0.70 | Minimum confidence for classification to proceed |
| `MAX_SURFACE_ENTRIES` | 500 | Maximum surface entries per surface map |
| `MAX_PLAN_STEPS` | 50 | Maximum rectification steps per plan |
| `MIN_OTHER_DETAIL_LENGTH` | 80 chars | Minimum detail length when UncertaintyCode is OTHER |
| `MIN_RISK_ACCEPTANCE_DETAIL_LENGTH` | 150 chars | Minimum detail for RISK_ACCEPTED follow-up flags |

---

## 10. Grammar Invariants

The following invariants hold across the entire ISM operator grammar. Violation of any invariant is a substrate fault, not an operator fault.

1. **Namespace isolation:** No operator outside the `incident.*` namespace may modify an `IncidentRecord`.
2. **Plan immutability:** A `RectificationPlan` is immutable once `PENDING_APPROVAL` is entered. Re-planning requires returning to `PLAN_DERIVED` via approval rejection.
3. **Surface scope enforcement:** `incident.execute.*` operators may only act on targets declared in the approved `SurfaceMap`. Out-of-scope targets are a grammar fault.
4. **Zero secret value guarantee:** Secret values must never appear in any `OUT`, `ExecutionRecord`, log, or audit trail. Version identifiers and references are permitted.
5. **Execution sequencing:** `incident.execute.*` steps must be executed in `step_index` order unless the `RectificationPlan` declares explicit parallel groups. Default is strictly sequential.
6. **Approval gate:** No `incident.execute.*` operator may begin unless `IncidentRecord.state == APPROVED` and `approval_request_id` is present on the record.
7. **Uncertainty flag escalation:** Uncertainty flags with severity `BLOCKING` must be resolved or explicitly acknowledged before `incident.request_operator_approval` may proceed.
8. **Hold supremacy:** A record in state `HOLD` cannot have any `incident.execute.*` operator invoked against it, regardless of approval status.
9. **Terminal state finality:** Records in `RESOLVED` or `FAULTED` states are immutable. New incident signals must enter via `incident.ingest` as new records.
10. **Determinism requirement:** All operators must produce identical `OUT` for identical `IN` under identical substrate state. Any operator exhibiting non-determinism is a grammar fault.

---

*End of operator grammar document.*
*Canonical source: `/docs/Incident_Substrate_Model/operator_grammar.md` · TriadicFrameworks repository*
*RTT/1 Canon · ISM Grammar v1.0*

---

**What's covered:** all 12 operators across 6 families, a 10-state deterministic record state machine, a complete type registry, substrate constants table, and 10 cross-cutting grammar invariants — all in RTT/1 `OPERATOR / IN / OUT / PRE / POST / GUARD / YIELDS / FAULTS` form.
