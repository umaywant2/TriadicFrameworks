# Incident Rectification Examples — Incident Substrate Model
**Document:** `incident_rectification_examples.md`
**Path:** `/docs/Incident_Substrate_Model/incident_rectification_examples.md`
**Revision:** RTT/1 · Canon Edition
**Status:** Normative Reference
**Issued:** 2026-05-20
**Depends on:** `operator_grammar.md`, `substrate_errors.md`, `operator_lifecycle.md`

---

## How to Read These Examples

Each example presents a complete ISM operator call trace for a real incident
class. Every call is rendered in the following format:

```
── OPERATOR: operator.name ─────────────────────────────────────
   @ 2026-05-20T07:04:11.203Z
   IN  { ... }
   OUT { ... }
   STATE: PRIOR_STATE → NEW_STATE
────────────────────────────────────────────────────────────────
```

Fields abbreviated for readability:
- UUIDs are shown as `<label:first-8>` — e.g., `<rec:a1f9c823>`.
- SHA-256 hashes are shown as `sha256:<first-16>...`.
- Raw payload bytes are shown as structured summaries, not raw binary.
- Approval resolution (human action) is shown as a `[APPROVAL EVENT]` block.
- Hold release (human action) is shown as a `[HOLD RELEASE EVENT]` block.

Annotations prefixed `※` reference specific sections of the companion
documents — e.g., `※ grammar §3.2` refers to `operator_grammar.md` Section 3.2.

---

## Example 1 — AWS Access Key Committed to Public GitHub Repository

**Incident class:** `SECRET_LEAK`
**Severity:** CRITICAL
**Outcome:** RESOLVED
**Lifecycle retention class:** CRITICAL (7 years)
**Operators exercised:** `ingest` · `classify` · `map_surface_area` ·
  `derive_rectification_steps` · `generate_readonly_plan` ·
  `request_operator_approval` · `execute.remove_file` · `execute.rotate_secret`

### Scenario

At 07:00 UTC a GitHub secret scanning webhook fires, reporting that commit
`e3fa9b2` to the public repository `acme-corp/payment-service` contains a
hardcoded AWS access key (`AKIA...`) with IAM administrator privileges. The
key is live and has not yet been used post-exposure. The file
`config/deploy.env` was pushed 4 minutes earlier. Time to remediation is
critical — every minute the key remains active is exploitable.

### Operator Call Trace

```
── OPERATOR: incident.ingest ────────────────────────────────────
   @ 2026-05-20T07:00:44.817Z
   IN  {
         signal_id    : <sig:f7a33b01-...>,
         source       : "github.secret-scanning.webhook",
         content_type : "application/json",
         emitted_at   : "2026-05-20T07:00:40.002Z",
         severity_hint: "CRITICAL",
         raw_payload  : {
           repository    : "acme-corp/payment-service",
           visibility    : "public",
           commit_sha    : "e3fa9b2c",
           file_path     : "config/deploy.env",
           secret_type   : "aws_access_key_id",
           secret_ref    : "AKIA4EXAMPLE7KEY23AB",
           pushed_at     : "2026-05-20T06:56:38.000Z",
           pusher         : "dev-bot@acme-corp.com",
           alert_url     : "https://github.com/acme-corp/payment-service/security/secret-scanning/alerts/142"
         }
       }
   OUT {
         record_id   : <rec:a1f9c823-...>,
         ingested_at : "2026-05-20T07:00:44.817Z",
         status      : "ACCEPTED"
       }
   STATE: (none) → INGESTED
────────────────────────────────────────────────────────────────

── OPERATOR: incident.classify ──────────────────────────────────
   @ 2026-05-20T07:00:45.102Z
   IN  {
         record_id     : <rec:a1f9c823-...>,
         classifier_id : "ism-classifier.secret-pattern-v4",
         category      : "SECRET_LEAK",
         subcategory   : "aws_access_key_id.iam_admin.public_vcs",
         confidence    : 0.98,
         rationale     : "GitHub secret scanning confirmed AWS IAM access key
                          pattern (AKIA prefix + 16-char alphanumeric) in a
                          public repository commit. Key type inferred as
                          aws_access_key_id. IAM privilege level not yet
                          confirmed — subcategory assumes admin pending
                          IAM policy lookup. Confidence 0.98: pattern match
                          is deterministic; privilege level is inferred."
       }
   OUT {
         record_id              : <rec:a1f9c823-...>,
         classification_version : 1,
         effective_at           : "2026-05-20T07:00:45.102Z"
       }
   STATE: INGESTED → CLASSIFIED
   ※ lifecycle §3.2 — ClassificationVersion 1 sealed; chain_hash[1] written
────────────────────────────────────────────────────────────────

── OPERATOR: incident.map_surface_area ──────────────────────────
   @ 2026-05-20T07:00:46.391Z
   IN  {
         record_id    : <rec:a1f9c823-...>,
         scanner_id   : "ism-scanner.github-surface-v2",
         surface_snapshot_hash : "sha256:c4f8a19d3e7b2f01...",
         surfaces     : [
           {
             surface_type : "FILE",
             surface_ref  : "github://acme-corp/payment-service@e3fa9b2c/config/deploy.env",
             access_mode  : "READ",
             confidence   : 0.99,
             notes        : "File containing the exposed secret. Present in git history.
                             Must be removed from HEAD and considered permanently
                             compromised in history — git history rewrite is out-of-scope
                             for ISM; flagged for follow-up."
           },
           {
             surface_type : "SECRET",
             surface_ref  : "aws://iam/access-key/AKIA4EXAMPLE7KEY23AB",
             access_mode  : "EXECUTE",
             confidence   : 0.98,
             notes        : "Live AWS IAM access key. Key ID confirmed via
                             pattern match. Associated IAM user: deploy-bot-prod.
                             Policy attachment: AdministratorAccess (inferred;
                             requires IAM lookup to confirm)."
           }
         ]
       }
   OUT {
         record_id      : <rec:a1f9c823-...>,
         surface_map_id : <smap:b3d72f00-...>,
         surface_count  : 2,
         mapped_at      : "2026-05-20T07:00:46.391Z"
       }
   STATE: CLASSIFIED → SURFACE_MAPPED
────────────────────────────────────────────────────────────────

── OPERATOR: incident.derive_rectification_steps ────────────────
   @ 2026-05-20T07:00:47.019Z
   IN  {
         record_id      : <rec:a1f9c823-...>,
         surface_map_id : <smap:b3d72f00-...>,
         planner_id     : "ism-planner.secret-leak-v3",
         steps          : [
           {
             step_index   : 0,
             operator_ref : "incident.execute.rotate_secret",
             target_ref   : "aws://iam/access-key/AKIA4EXAMPLE7KEY23AB",
             parameters   : {
               rotation_policy    : "IMMEDIATE",
               notify_dependents  : true
             },
             reversible   : false,
             rationale    : "Rotate the exposed IAM access key immediately to
                             invalidate the compromised credential. Executed
                             BEFORE file removal because key rotation closes
                             the active exploit window regardless of whether
                             the file is removed. Rotation is irreversible —
                             the old key cannot be restored."
           },
           {
             step_index   : 1,
             operator_ref : "incident.execute.remove_file",
             target_ref   : "github://acme-corp/payment-service@e3fa9b2c/config/deploy.env",
             parameters   : {
               dry_run  : false,
               checksum : "sha256:9b3ef12c7a480d9e..."
             },
             reversible   : false,
             rationale    : "Remove the file from HEAD to prevent further
                             exposure and satisfy the GitHub secret scanning
                             alert dismissal condition. Note: git history
                             retention is a separate concern — see follow-up
                             flag recommended in surface notes."
           }
         ]
       }
   OUT {
         record_id  : <rec:a1f9c823-...>,
         plan_id    : <plan:cc1d8855-...>,
         step_count : 2,
         derived_at : "2026-05-20T07:00:47.019Z"
       }
   STATE: SURFACE_MAPPED → PLAN_DERIVED
   ※ grammar §4 — step_index 0 = rotate_secret before remove_file;
     rotation closes exploit window faster than file removal alone
────────────────────────────────────────────────────────────────

── OPERATOR: incident.generate_readonly_plan ────────────────────
   @ 2026-05-20T07:00:47.340Z
   IN  {
         record_id : <rec:a1f9c823-...>,
         plan_id   : <plan:cc1d8855-...>,
         format    : "MARKDOWN"
       }
   OUT {
         record_id    : <rec:a1f9c823-...>,
         plan_id      : <plan:cc1d8855-...>,
         rendered_at  : "2026-05-20T07:00:47.340Z",
         rendered_plan: """
           ## Rectification Plan — <rec:a1f9c823>
           **Incident:** SECRET_LEAK · aws_access_key_id.iam_admin.public_vcs
           **Surface count:** 2  |  **Steps:** 2  |  **All steps irreversible**

           ### Step 0 — Rotate AWS IAM Access Key [IRREVERSIBLE]
           Operator : incident.execute.rotate_secret
           Target   : aws://iam/access-key/AKIA4EXAMPLE7KEY23AB
           Policy   : IMMEDIATE rotation
           Notifies : dependent consumers of deploy-bot-prod key
           Rationale: Closes the active exploit window before file removal.

           ### Step 1 — Remove Exposed File from Repository HEAD [IRREVERSIBLE]
           Operator  : incident.execute.remove_file
           Target    : github://acme-corp/payment-service@e3fa9b2c/config/deploy.env
           Checksum  : sha256:9b3ef12c7a480d9e...
           Rationale : Removes the file from HEAD; satisfies scanning alert.
                       ⚠ Git history rewrite not in scope — flag for follow-up.
         """
       }
   ※ grammar §4 — READONLY operator; no state change
────────────────────────────────────────────────────────────────

── OPERATOR: incident.request_operator_approval ─────────────────
   @ 2026-05-20T07:00:48.001Z
   IN  {
         record_id        : <rec:a1f9c823-...>,
         plan_id          : <plan:cc1d8855-...>,
         requesting_agent : "ism-planner.secret-leak-v3",
         approver_set     : ["security-oncall@acme-corp.com"],
         approval_policy  : "ANY_ONE",
         context_note     : "CRITICAL: live AWS admin key exposed in public repo
                             for 4 minutes. Step 0 (key rotation) is irreversible.
                             Step 1 (file removal) is irreversible. Recommend
                             immediate approval — every minute of delay is
                             exploitable. No blocking uncertainty flags."
       }
   OUT {
         record_id           : <rec:a1f9c823-...>,
         approval_request_id : <apr:d9e14c77-...>,
         requested_at        : "2026-05-20T07:00:48.001Z",
         approver_count      : 1
       }
   STATE: PLAN_DERIVED → PENDING_APPROVAL
────────────────────────────────────────────────────────────────

[APPROVAL EVENT]
   @ 2026-05-20T07:02:03.541Z
   approver     : "security-oncall@acme-corp.com"
   decision     : APPROVED
   approval_id  : <apr:d9e14c77-...>
   note         : "Confirmed. Key is live — rotate immediately."
   STATE: PENDING_APPROVAL → APPROVED
────────────────────────────────────────────────────────────────

── OPERATOR: incident.execute.rotate_secret ─────────────────────
   @ 2026-05-20T07:02:04.200Z   [step_index: 0]
   IN  {
         record_id         : <rec:a1f9c823-...>,
         plan_id           : <plan:cc1d8855-...>,
         step_index        : 0,
         secret_ref        : "aws://iam/access-key/AKIA4EXAMPLE7KEY23AB",
         rotation_policy   : "IMMEDIATE",
         notify_dependents : true
       }
   OUT {
         record_id          : <rec:a1f9c823-...>,
         execution_id       : <exec:e0011fa2-...>,
         status             : "ROTATED",
         new_secret_version : "v2-20260520T070204",
         rotated_at         : "2026-05-20T07:02:04.619Z"
       }
   STATE: APPROVED → EXECUTING
   ※ grammar §6 invariant 4 — new secret value not emitted in OUT
   ※ errors EXE-006 — dependent notification succeeded for 3 consumers
     (deploy-pipeline-prod, ci-runner-01, ci-runner-02)
────────────────────────────────────────────────────────────────

── OPERATOR: incident.execute.remove_file ───────────────────────
   @ 2026-05-20T07:02:05.014Z   [step_index: 1]
   IN  {
         record_id  : <rec:a1f9c823-...>,
         plan_id    : <plan:cc1d8855-...>,
         step_index : 1,
         file_path  : "github://acme-corp/payment-service@e3fa9b2c/config/deploy.env",
         checksum   : "sha256:9b3ef12c7a480d9e...",
         dry_run    : false
       }
   OUT {
         record_id      : <rec:a1f9c823-...>,
         execution_id   : <exec:e0022b14-...>,
         status         : "REMOVED",
         removed_at     : "2026-05-20T07:02:05.882Z",
         prior_checksum : "sha256:9b3ef12c7a480d9e..."
       }
   STATE: EXECUTING → RESOLVED
   ※ lifecycle §5.1 — archival triggered immediately (RESOLVED)
   ※ lifecycle §6.1 — RetentionClass: CRITICAL (SECRET_LEAK category)
────────────────────────────────────────────────────────────────
```

### Timeline Summary

| Time (UTC) | Event |
|---|---|
| 06:56:38 | Commit `e3fa9b2c` pushed to public repo — secret exposed |
| 07:00:40 | GitHub secret scanning fires webhook |
| 07:00:44 | `incident.ingest` — record created `<rec:a1f9c823>` |
| 07:00:47 | Plan derived — 2 steps, both irreversible |
| 07:00:48 | Approval requested to `security-oncall` |
| 07:02:03 | Approval granted — 75 seconds after request |
| 07:02:04 | Key rotated — exploit window closed |
| 07:02:05 | File removed from HEAD |
| 07:02:05 | Record → RESOLVED |
| **T+5m27s** | **Total time from exposure to key invalidation** |

### Post-Incident Notes

The git history for `acme-corp/payment-service` still contains commit `e3fa9b2c`
with the plaintext key. This is outside ISM's execution scope but is a genuine
residual risk. A `flag_for_followup` with `MANUAL_REMEDIATION_REQUIRED` and
`THIRD_PARTY_COORDINATION` (GitHub support BFG/history rewrite) should be
raised by the reviewing operator. RetentionClass `CRITICAL` means this record
is held for 7 years.

---

## Example 2 — Critical CVE in Transitive npm Dependency

**Incident class:** `DEPENDENCY_CVE`
**Severity:** HIGH
**Outcome:** RESOLVED (with open follow-up ticket)
**Lifecycle retention class:** STANDARD (2 years)
**Operators exercised:** `ingest` · `classify` · `flag_uncertainty` ·
  `map_surface_area` · `hold_for_review` · `derive_rectification_steps` ·
  `generate_readonly_plan` · `request_operator_approval` ·
  `execute.patch_dependency` · `execute.flag_for_followup`

### Scenario

At 08:30 UTC the ACME dependency scanning service reports that
`fast-xml-parser@4.2.4` — a transitive dependency pulled in by
`@acme/api-gateway@2.11.0` — is affected by CVE-2026-31814: a
prototype pollution vulnerability in the `parse()` method (CVSS 9.1).
The package appears in three production services. However, the scanner
also reports that one service (`legacy-ingest`) uses a custom fork of
`fast-xml-parser` at the same semver, pinned by a monorepo patch file.
The planner cannot confirm whether patching the standard package will
affect the fork — so an uncertainty flag is raised and a hold is
placed before planning proceeds.

### Operator Call Trace

```
── OPERATOR: incident.ingest ────────────────────────────────────
   @ 2026-05-20T08:30:12.004Z
   IN  {
         signal_id    : <sig:0be7d441-...>,
         source       : "acme.dep-scanner.snyk-bridge-v2",
         content_type : "application/json",
         emitted_at   : "2026-05-20T08:30:10.881Z",
         severity_hint: "HIGH",
         raw_payload  : {
           cve_id        : "CVE-2026-31814",
           cvss_score    : 9.1,
           cvss_vector   : "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:N",
           package       : "fast-xml-parser",
           affected_range: ">=4.0.0 <4.3.1",
           fix_version   : "4.3.1",
           vulnerability : "Prototype pollution in XMLParser.parse() via
                            crafted XML attribute names allows arbitrary
                            property injection on Object.prototype.",
           affected_services : [
             "api-gateway@2.11.0",
             "data-pipeline@1.8.3",
             "legacy-ingest@0.9.7 (FORKED — patch file detected)"
           ],
           scanner_confidence : 0.91
         }
       }
   OUT {
         record_id   : <rec:b2e05f11-...>,
         ingested_at : "2026-05-20T08:30:12.004Z",
         status      : "ACCEPTED"
       }
   STATE: (none) → INGESTED
────────────────────────────────────────────────────────────────

── OPERATOR: incident.classify ──────────────────────────────────
   @ 2026-05-20T08:30:12.441Z
   IN  {
         record_id     : <rec:b2e05f11-...>,
         classifier_id : "ism-classifier.cve-triage-v5",
         category      : "DEPENDENCY_CVE",
         subcategory   : "prototype-pollution.npm.transitive.multi-service",
         confidence    : 0.91,
         rationale     : "CVE-2026-31814 confirmed in NVD. CVSS 9.1 network-
                          exploitable prototype pollution. Affects 3 production
                          services via transitive dependency chain. Confidence
                          0.91: scanner reported a forked variant in
                          legacy-ingest that may behave differently — this
                          reduces classification certainty for that service."
       }
   OUT {
         record_id              : <rec:b2e05f11-...>,
         classification_version : 1,
         effective_at           : "2026-05-20T08:30:12.441Z"
       }
   STATE: INGESTED → CLASSIFIED
────────────────────────────────────────────────────────────────

── OPERATOR: incident.flag_uncertainty ──────────────────────────
   @ 2026-05-20T08:30:12.709Z
   IN  {
         record_id        : <rec:b2e05f11-...>,
         flagging_agent   : "ism-classifier.cve-triage-v5",
         uncertainty_code : "SURFACE_INCOMPLETE",
         affected_field   : "surfaces[legacy-ingest]",
         detail           : "Scanner detected a monorepo patch file
                             (patches/fast-xml-parser+4.2.4.patch) in the
                             legacy-ingest service tree. This patch modifies
                             the XMLParser.parse() method — the same code path
                             affected by CVE-2026-31814. It is unknown whether
                             the patch inadvertently mitigates the vulnerability
                             or introduces a variant. Standard fast-xml-parser
                             patch steps may not apply to this fork. Surface
                             mapping and planning for legacy-ingest should
                             proceed with reduced confidence until the patch
                             file is reviewed by a Node.js security engineer."
       }
   OUT {
         record_id  : <rec:b2e05f11-...>,
         flag_id    : <unc:f9901c44-...>,
         flagged_at : "2026-05-20T08:30:12.709Z"
       }
   ※ grammar §4 — no state transition; annotation only
   ※ errors UNC-001, UNC-002 — not triggered; code and detail are valid
────────────────────────────────────────────────────────────────

── OPERATOR: incident.map_surface_area ──────────────────────────
   @ 2026-05-20T08:30:13.100Z
   IN  {
         record_id    : <rec:b2e05f11-...>,
         scanner_id   : "ism-scanner.npm-dep-v3",
         surface_snapshot_hash : "sha256:77d3b201f9e84abc...",
         surfaces     : [
           {
             surface_type : "DEPENDENCY",
             surface_ref  : "npm:fast-xml-parser@4.2.4",
             access_mode  : "EXECUTE",
             confidence   : 0.99,
             notes        : "Canonical package from npm registry. Affects
                             api-gateway and data-pipeline. Upgrade target:
                             4.3.1 (first patched release per NVD advisory)."
           },
           {
             surface_type : "DEPENDENCY",
             surface_ref  : "npm:fast-xml-parser@4.2.4#legacy-ingest-fork",
             access_mode  : "EXECUTE",
             confidence   : 0.61,
             notes        : "Forked variant in legacy-ingest service via
                             patch file. Behaviour under CVE-2026-31814
                             is unverified. Flagged SURFACE_INCOMPLETE.
                             Standard patch steps may not apply."
           }
         ]
       }
   OUT {
         record_id      : <rec:b2e05f11-...>,
         surface_map_id : <smap:c4a19d02-...>,
         surface_count  : 2,
         mapped_at      : "2026-05-20T08:30:13.100Z"
       }
   STATE: CLASSIFIED → SURFACE_MAPPED
────────────────────────────────────────────────────────────────

── OPERATOR: incident.hold_for_review ───────────────────────────
   @ 2026-05-20T08:30:14.002Z
   IN  {
         record_id    : <rec:b2e05f11-...>,
         held_by      : "ism-planner.cve-response-v2",
         reason_code  : "BLOCKING_UNCERTAINTY",
         detail       : "Surface map contains a forked dependency entry
                         (npm:fast-xml-parser@4.2.4#legacy-ingest-fork)
                         with confidence 0.61. Standard patch_dependency
                         steps cannot safely be applied to the fork without
                         manual review of patches/fast-xml-parser+4.2.4.patch.
                         Hold placed until a Node.js security engineer confirms
                         whether the patch mitigates or modifies the CVE-2026-31814
                         attack surface. Estimated review time: 2-4 hours."
         resume_after : "2026-05-20T10:30:00.000Z"
       }
   OUT {
         record_id   : <rec:b2e05f11-...>,
         hold_id     : <hold:a3312e88-...>,
         held_at     : "2026-05-20T08:30:14.002Z",
         prior_state : "SURFACE_MAPPED"
       }
   STATE: SURFACE_MAPPED → HOLD
   ※ lifecycle §4 — hold preserves prior_state for restoration on release
────────────────────────────────────────────────────────────────

[HOLD RELEASE EVENT]
   @ 2026-05-20T10:17:33.009Z
   released_by  : "sri.kumar@acme-corp.com"
   hold_id      : <hold:a3312e88-...>
   finding      : "Patch file reviewed. It modifies XML attribute escaping,
                   not the parse() code path. The fork IS vulnerable to
                   CVE-2026-31814. However, the patch conflicts with the
                   4.3.1 upgrade — the patch must be removed or ported
                   before the standard upgrade can be applied. Recommend:
                   patch standard services now; flag legacy-ingest for
                   manual remediation by the legacy team."
   STATE: HOLD → SURFACE_MAPPED
────────────────────────────────────────────────────────────────

── OPERATOR: incident.derive_rectification_steps ────────────────
   @ 2026-05-20T10:17:45.881Z
   IN  {
         record_id      : <rec:b2e05f11-...>,
         surface_map_id : <smap:c4a19d02-...>,
         planner_id     : "ism-planner.cve-response-v2",
         steps          : [
           {
             step_index   : 0,
             operator_ref : "incident.execute.patch_dependency",
             target_ref   : "npm:fast-xml-parser@4.2.4",
             parameters   : {
               current_version  : "4.2.4",
               target_version   : "4.3.1",
               package_manager  : "NPM",
               verify_checksum  : "sha256:4e9f301ab72cd5f8...",
               dry_run          : false
             },
             reversible   : true,
             rationale    : "Patch canonical fast-xml-parser in api-gateway
                             and data-pipeline from 4.2.4 to 4.3.1. This is
                             the NVD-confirmed patched version. Checksum
                             verified against npm registry integrity field."
           },
           {
             step_index   : 1,
             operator_ref : "incident.execute.flag_for_followup",
             target_ref   : "npm:fast-xml-parser@4.2.4#legacy-ingest-fork",
             parameters   : {
               followup_code : "MANUAL_REMEDIATION_REQUIRED",
               priority      : "HIGH",
               assigned_to   : ["legacy-team@acme-corp.com",
                                "sri.kumar@acme-corp.com"],
               due_by        : "2026-05-27T17:00:00.000Z"
             },
             reversible   : true,
             rationale    : "The forked dependency in legacy-ingest requires
                             patch file removal or porting before the 4.3.1
                             upgrade can be applied. This cannot be automated
                             safely — the patch author must assess compatibility."
           }
         ]
       }
   OUT {
         record_id  : <rec:b2e05f11-...>,
         plan_id    : <plan:dd2e9a03-...>,
         step_count : 2,
         derived_at : "2026-05-20T10:17:45.881Z"
       }
   STATE: SURFACE_MAPPED → PLAN_DERIVED
────────────────────────────────────────────────────────────────

── OPERATOR: incident.generate_readonly_plan ────────────────────
   @ 2026-05-20T10:17:46.201Z
   IN  { record_id: <rec:b2e05f11-...>, plan_id: <plan:dd2e9a03-...>, format: "MARKDOWN" }
   OUT {
         rendered_plan: """
           ## Rectification Plan — <rec:b2e05f11>
           **Incident:** DEPENDENCY_CVE · CVE-2026-31814 (CVSS 9.1)
           **Surface count:** 2  |  **Steps:** 2
           ⚠ Open uncertainty flag: SURFACE_INCOMPLETE on legacy-ingest fork

           ### Step 0 — Patch fast-xml-parser to 4.3.1 [REVERSIBLE]
           Operator  : incident.execute.patch_dependency
           Target    : npm:fast-xml-parser@4.2.4 (api-gateway, data-pipeline)
           From      : 4.2.4  →  To: 4.3.1
           Checksum  : sha256:4e9f301ab72cd5f8...
           Rationale : NVD-confirmed patched version. Checksum verified.

           ### Step 1 — Flag legacy-ingest fork for manual remediation [flag_for_followup]
           Operator  : incident.execute.flag_for_followup
           Target    : npm:fast-xml-parser@4.2.4#legacy-ingest-fork
           Code      : MANUAL_REMEDIATION_REQUIRED
           Priority  : HIGH
           Assigned  : legacy-team, sri.kumar
           Due       : 2026-05-27T17:00:00Z
           Rationale : Fork incompatible with automated patch; requires
                       manual patch file review and upgrade.
         """
       }
────────────────────────────────────────────────────────────────

── OPERATOR: incident.request_operator_approval ─────────────────
   @ 2026-05-20T10:17:47.003Z
   IN  {
         record_id        : <rec:b2e05f11-...>,
         plan_id          : <plan:dd2e9a03-...>,
         requesting_agent : "ism-planner.cve-response-v2",
         approver_set     : ["security-oncall@acme-corp.com",
                             "sri.kumar@acme-corp.com"],
         approval_policy  : "ANY_ONE",
         context_note     : "ACKNOWLEDGED: <unc:f9901c44> — SURFACE_INCOMPLETE
                             on legacy-ingest fork. Confirmed by sri.kumar at
                             10:17Z: fork is vulnerable but incompatible with
                             automated patch. Step 1 (flag_for_followup) closes
                             the automated scope; legacy team handles manually.
                             Step 0 is safe to proceed immediately."
       }
   OUT {
         record_id           : <rec:b2e05f11-...>,
         approval_request_id : <apr:e3f20b55-...>,
         requested_at        : "2026-05-20T10:17:47.003Z",
         approver_count      : 2
       }
   STATE: PLAN_DERIVED → PENDING_APPROVAL
   ※ grammar §5 — uncertainty flag acknowledged in context_note; GUARD passes
────────────────────────────────────────────────────────────────

[APPROVAL EVENT]
   @ 2026-05-20T10:19:02.771Z
   approver  : "security-oncall@acme-corp.com"
   decision  : APPROVED
   note      : "Plan looks correct. Proceed with step 0; legacy team owns step 1."
   STATE: PENDING_APPROVAL → APPROVED
────────────────────────────────────────────────────────────────

── OPERATOR: incident.execute.patch_dependency ──────────────────
   @ 2026-05-20T10:19:03.401Z   [step_index: 0]
   IN  {
         record_id       : <rec:b2e05f11-...>,
         plan_id         : <plan:dd2e9a03-...>,
         step_index      : 0,
         package_ref     : "npm:fast-xml-parser@4.2.4",
         current_version : "4.2.4",
         target_version  : "4.3.1",
         package_manager : "NPM",
         verify_checksum : "sha256:4e9f301ab72cd5f8...",
         dry_run         : false
       }
   OUT {
         record_id       : <rec:b2e05f11-...>,
         execution_id    : <exec:f0133d66-...>,
         status          : "PATCHED",
         patched_version : "4.3.1",
         patched_at      : "2026-05-20T10:19:09.204Z"
       }
   STATE: APPROVED → EXECUTING
   ※ errors EXE-008 — not triggered; current_version matched installed version
   ※ errors EXE-010 — not triggered; npm install exited 0
────────────────────────────────────────────────────────────────

── OPERATOR: incident.execute.flag_for_followup ─────────────────
   @ 2026-05-20T10:19:10.001Z   [step_index: 1]
   IN  {
         record_id     : <rec:b2e05f11-...>,
         plan_id       : <plan:dd2e9a03-...>,
         step_index    : 1,
         target_ref    : "npm:fast-xml-parser@4.2.4#legacy-ingest-fork",
         followup_code : "MANUAL_REMEDIATION_REQUIRED",
         priority      : "HIGH",
         assigned_to   : ["legacy-team@acme-corp.com", "sri.kumar@acme-corp.com"],
         due_by        : "2026-05-27T17:00:00.000Z",
         detail        : "The legacy-ingest service uses a patched fork of
                          fast-xml-parser@4.2.4 via monorepo patch file
                          patches/fast-xml-parser+4.2.4.patch. The fork IS
                          vulnerable to CVE-2026-31814 (confirmed by sri.kumar
                          2026-05-20T10:17Z). Standard npm upgrade to 4.3.1
                          conflicts with the patch file — the patch must be
                          removed or ported before upgrading. Assigned to
                          the legacy-ingest team with HIGH priority and a
                          7-day SLA. ISM record: <rec:b2e05f11>."
       }
   OUT {
         record_id    : <rec:b2e05f11-...>,
         execution_id : <exec:f0244e77-...>,
         followup_id  : <fup:g1355f88-...>,
         status       : "FLAGGED",
         flagged_at   : "2026-05-20T10:19:10.441Z"
       }
   STATE: EXECUTING → RESOLVED
   ※ lifecycle §5.1 — RetentionClass: STANDARD (DEPENDENCY_CVE)
   ※ lifecycle §6.1 — open FollowupTicket <fup:g1355f88> blocks expiry
     until ticket is CLOSED
────────────────────────────────────────────────────────────────
```

### Timeline Summary

| Time (UTC) | Event |
|---|---|
| 08:30:10 | Scanner detects CVE-2026-31814 in fast-xml-parser@4.2.4 |
| 08:30:12 | Record created; classified; uncertainty flag raised |
| 08:30:14 | Hold placed — fork analysis required |
| 10:17:33 | Hold released — sri.kumar confirms fork is vulnerable, patch incompatible |
| 10:17:47 | Approval requested with uncertainty acknowledgment |
| 10:19:02 | Approved |
| 10:19:09 | Canonical package patched to 4.3.1 across api-gateway, data-pipeline |
| 10:19:10 | Legacy-ingest fork flagged for follow-up; assigned to legacy team |
| 10:19:10 | Record → RESOLVED (with open follow-up ticket) |

---

## Example 3 — Publicly Accessible GCS Bucket Containing PII Export Files

**Incident class:** `MISCONFIGURATION`
**Severity:** HIGH
**Outcome:** RESOLVED (all steps via flag_for_followup — infra change required)
**Lifecycle retention class:** STANDARD (2 years)
**Operators exercised:** `ingest` · `classify` · `map_surface_area` ·
  `flag_uncertainty` · `derive_rectification_steps` ·
  `generate_readonly_plan` · `request_operator_approval` ·
  `execute.flag_for_followup` × 2

### Scenario

At 10:00 UTC ACME's cloud posture scanner reports that the GCS bucket
`acme-analytics-exports-prod` has `allUsers` read access on its IAM policy
— making all objects publicly accessible on the internet. The bucket
contains daily PII export files (customer email lists, order summaries)
generated by the analytics pipeline. The misconfiguration has been present
for 11 days based on Cloud Audit Logs. Because fixing a GCS IAM policy
and auditing data exposure are Terraform-managed infra operations, the ISM
cannot apply the fix directly — both steps must be flagged for manual
remediation.

### Operator Call Trace

```
── OPERATOR: incident.ingest ────────────────────────────────────
   @ 2026-05-20T10:00:07.312Z
   IN  {
         signal_id    : <sig:1cf8e552-...>,
         source       : "acme.cloud-posture.cspm-v3",
         content_type : "application/json",
         emitted_at   : "2026-05-20T10:00:05.100Z",
         severity_hint: "HIGH",
         raw_payload  : {
           provider         : "gcp",
           resource_type    : "storage.googleapis.com/Bucket",
           resource_name    : "acme-analytics-exports-prod",
           finding          : "PUBLIC_BUCKET_ACL",
           policy_member    : "allUsers",
           policy_role      : "roles/storage.objectViewer",
           object_count     : 847,
           estimated_pii    : true,
           first_seen       : "2026-05-09T00:00:00.000Z",
           exposure_days    : 11,
           object_prefixes  : ["daily-exports/", "customer-lists/", "order-summaries/"],
           terraform_managed: true,
           tf_resource_path : "infra/gcp/storage/analytics-exports.tf"
         }
       }
   OUT {
         record_id   : <rec:c3f17a22-...>,
         ingested_at : "2026-05-20T10:00:07.312Z",
         status      : "ACCEPTED"
       }
   STATE: (none) → INGESTED
────────────────────────────────────────────────────────────────

── OPERATOR: incident.classify ──────────────────────────────────
   @ 2026-05-20T10:00:07.801Z
   IN  {
         record_id     : <rec:c3f17a22-...>,
         classifier_id : "ism-classifier.cloud-posture-v3",
         category      : "MISCONFIGURATION",
         subcategory   : "gcs.public_acl.pii_exposure.terraform_managed",
         confidence    : 0.96,
         rationale     : "Cloud posture scanner confirmed GCS bucket with
                          allUsers:objectViewer binding. Bucket contains
                          object prefixes consistent with PII exports (daily-
                          exports/, customer-lists/). Exposure confirmed for
                          11 days via Cloud Audit Logs. Classified as
                          MISCONFIGURATION because the root cause is an
                          IAM policy error, not a data exfiltration event.
                          DATA_EXPOSURE not used: no confirmed exfil event —
                          public accessibility ≠ confirmed access by
                          unauthorized parties. Confidence 0.96."
       }
   OUT {
         record_id              : <rec:c3f17a22-...>,
         classification_version : 1,
         effective_at           : "2026-05-20T10:00:07.801Z"
       }
   STATE: INGESTED → CLASSIFIED
────────────────────────────────────────────────────────────────

── OPERATOR: incident.map_surface_area ──────────────────────────
   @ 2026-05-20T10:00:08.441Z
   IN  {
         record_id    : <rec:c3f17a22-...>,
         scanner_id   : "ism-scanner.gcp-iam-v2",
         surface_snapshot_hash : "sha256:8ef4d309a1b7c24f...",
         surfaces     : [
           {
             surface_type : "CONFIG",
             surface_ref  : "gcp://storage/buckets/acme-analytics-exports-prod/iam-policy",
             access_mode  : "WRITE",
             confidence   : 0.99,
             notes        : "GCS bucket IAM policy containing allUsers:objectViewer.
                             Managed by Terraform resource
                             google_storage_bucket_iam_member in
                             infra/gcp/storage/analytics-exports.tf.
                             Fix requires Terraform plan+apply by the infra team.
                             ISM cannot apply GCP IAM mutations directly."
           },
           {
             surface_type : "SERVICE",
             surface_ref  : "gcp://storage/buckets/acme-analytics-exports-prod",
             access_mode  : "READ",
             confidence   : 0.99,
             notes        : "The bucket itself and its 847 objects (daily-exports/,
                             customer-lists/, order-summaries/) were publicly
                             readable for ~11 days. An access log audit is
                             required to determine whether unauthorized reads
                             occurred. Audit must be performed by the data
                             privacy team via Cloud Audit Log export."
           }
         ]
       }
   OUT {
         record_id      : <rec:c3f17a22-...>,
         surface_map_id : <smap:d5b28e13-...>,
         surface_count  : 2,
         mapped_at      : "2026-05-20T10:00:08.441Z"
       }
   STATE: CLASSIFIED → SURFACE_MAPPED
────────────────────────────────────────────────────────────────

── OPERATOR: incident.flag_uncertainty ──────────────────────────
   @ 2026-05-20T10:00:08.712Z
   IN  {
         record_id        : <rec:c3f17a22-...>,
         flagging_agent   : "ism-classifier.cloud-posture-v3",
         uncertainty_code : "EXTERNAL_DEPENDENCY_UNKNOWN",
         affected_field   : "surfaces[gcp://storage/buckets/.../iam-policy]",
         detail           : "The IAM policy is managed by Terraform. The
                             ISM execute.* operators cannot apply Terraform
                             plan+apply cycles — this requires GCP credentials
                             with Terraform state access and an infra team
                             approval workflow external to ISM. The estimated
                             time for infra team to apply the fix is unknown;
                             SLA depends on oncall rotation. Classification
                             as EXTERNAL_DEPENDENCY_UNKNOWN because remediation
                             depends on third-party (infra team) execution
                             of a non-automated workflow."
       }
   OUT {
         record_id  : <rec:c3f17a22-...>,
         flag_id    : <unc:h0012d55-...>,
         flagged_at : "2026-05-20T10:00:08.712Z"
       }
   ※ grammar §4 — annotation only; no state transition
────────────────────────────────────────────────────────────────

── OPERATOR: incident.derive_rectification_steps ────────────────
   @ 2026-05-20T10:00:09.200Z
   IN  {
         record_id      : <rec:c3f17a22-...>,
         surface_map_id : <smap:d5b28e13-...>,
         planner_id     : "ism-planner.misconfiguration-v2",
         steps          : [
           {
             step_index   : 0,
             operator_ref : "incident.execute.flag_for_followup",
             target_ref   : "gcp://storage/buckets/acme-analytics-exports-prod/iam-policy",
             parameters   : {
               followup_code : "MANUAL_REMEDIATION_REQUIRED",
               priority      : "CRITICAL",
               assigned_to   : ["infra-oncall@acme-corp.com"],
               due_by        : "2026-05-20T14:00:00.000Z"
             },
             reversible   : true,
             rationale    : "Remove allUsers:objectViewer from the GCS bucket
                             IAM policy via Terraform. This is a Terraform-
                             managed resource — infra team must run plan+apply.
                             Priority CRITICAL: PII exposure is live. Due by
                             14:00Z today (4-hour SLA)."
           },
           {
             step_index   : 1,
             operator_ref : "incident.execute.flag_for_followup",
             target_ref   : "gcp://storage/buckets/acme-analytics-exports-prod",
             parameters   : {
               followup_code : "THIRD_PARTY_COORDINATION",
               priority      : "HIGH",
               assigned_to   : ["privacy-team@acme-corp.com", "legal@acme-corp.com"],
               due_by        : "2026-05-27T17:00:00.000Z"
             },
             reversible   : true,
             rationale    : "Export Cloud Audit Logs for the bucket covering
                             the 11-day exposure window (2026-05-09 to 2026-05-20).
                             Determine whether unauthorized parties accessed
                             any PII objects. If confirmed access occurred,
                             data breach notification obligations may apply
                             (GDPR Art. 33, CCPA). Legal team coordination
                             required. ISM cannot perform this audit."
           }
         ]
       }
   OUT {
         record_id  : <rec:c3f17a22-...>,
         plan_id    : <plan:ee3fa114-...>,
         step_count : 2,
         derived_at : "2026-05-20T10:00:09.200Z"
       }
   STATE: SURFACE_MAPPED → PLAN_DERIVED
────────────────────────────────────────────────────────────────

── OPERATOR: incident.request_operator_approval ─────────────────
   @ 2026-05-20T10:00:10.001Z
   IN  {
         record_id        : <rec:c3f17a22-...>,
         plan_id          : <plan:ee3fa114-...>,
         requesting_agent : "ism-planner.misconfiguration-v2",
         approver_set     : ["security-oncall@acme-corp.com",
                             "privacy-team@acme-corp.com"],
         approval_policy  : "ALL",
         context_note     : "ACKNOWLEDGED: <unc:h0012d55> — EXTERNAL_DEPENDENCY_UNKNOWN
                             (Terraform-managed policy). Plan is entirely via
                             flag_for_followup — no automated mutations.
                             Requires ALL approvers: security-oncall for infra
                             SLA, privacy-team for audit scope. PII exposure
                             has been live for 11 days — treat as urgent."
       }
   OUT {
         record_id           : <rec:c3f17a22-...>,
         approval_request_id : <apr:ff4gb225-...>,
         requested_at        : "2026-05-20T10:00:10.001Z",
         approver_count      : 2
       }
   STATE: PLAN_DERIVED → PENDING_APPROVAL
────────────────────────────────────────────────────────────────

[APPROVAL EVENT]
   @ 2026-05-20T10:04:41.001Z   approver: "security-oncall@acme-corp.com"
   decision : APPROVED
[APPROVAL EVENT]
   @ 2026-05-20T10:06:17.882Z   approver: "privacy-team@acme-corp.com"
   decision : APPROVED  |  note: "Legal notified. Starting audit log export now."
   STATE: PENDING_APPROVAL → APPROVED  (ALL policy satisfied)
────────────────────────────────────────────────────────────────

── OPERATOR: incident.execute.flag_for_followup ─────────────────
   @ 2026-05-20T10:06:18.500Z   [step_index: 0]
   IN  {
         record_id     : <rec:c3f17a22-...>,
         plan_id       : <plan:ee3fa114-...>,
         step_index    : 0,
         target_ref    : "gcp://storage/buckets/acme-analytics-exports-prod/iam-policy",
         followup_code : "MANUAL_REMEDIATION_REQUIRED",
         priority      : "CRITICAL",
         assigned_to   : ["infra-oncall@acme-corp.com"],
         due_by        : "2026-05-20T14:00:00.000Z",
         detail        : "Remove allUsers:roles/storage.objectViewer from
                          the IAM policy of GCS bucket acme-analytics-exports-prod.
                          Resource is managed by google_storage_bucket_iam_member
                          in infra/gcp/storage/analytics-exports.tf. Run:
                          terraform plan -target=module.analytics_exports.
                          google_storage_bucket_iam_member.public_reader
                          then apply after review. CRITICAL priority: live
                          PII exposure. SLA: 14:00Z today. ISM record:
                          <rec:c3f17a22>. Verification: re-run CSPM check
                          after apply to confirm finding is resolved."
       }
   OUT {
         record_id    : <rec:c3f17a22-...>,
         execution_id : <exec:g1244f99-...>,
         followup_id  : <fup:h2355g00-...>,
         status       : "FLAGGED",
         flagged_at   : "2026-05-20T10:06:18.901Z"
       }
   STATE: APPROVED → EXECUTING
────────────────────────────────────────────────────────────────

── OPERATOR: incident.execute.flag_for_followup ─────────────────
   @ 2026-05-20T10:06:19.200Z   [step_index: 1]
   IN  {
         record_id     : <rec:c3f17a22-...>,
         plan_id       : <plan:ee3fa114-...>,
         step_index    : 1,
         target_ref    : "gcp://storage/buckets/acme-analytics-exports-prod",
         followup_code : "THIRD_PARTY_COORDINATION",
         priority      : "HIGH",
         assigned_to   : ["privacy-team@acme-corp.com", "legal@acme-corp.com"],
         due_by        : "2026-05-27T17:00:00.000Z",
         detail        : "Export and analyze Cloud Audit Logs (data_access logs)
                          for bucket acme-analytics-exports-prod covering
                          2026-05-09T00:00Z through 2026-05-20T10:00Z (11-day
                          exposure window). Identify all GetObject/ListObjects
                          requests from non-ACME principals (filter: NOT
                          protoPayload.authenticationInfo.principalEmail
                          CONTAINS acme-corp.com). If any unauthorized reads
                          are confirmed: (1) notify DPO within 24h;
                          (2) assess GDPR Art. 33 72-hour notification
                          threshold; (3) engage legal for CCPA obligations.
                          Coordinate with Google Workspace Admin for log
                          export if audit log retention window is at risk.
                          ISM record: <rec:c3f17a22>."
       }
   OUT {
         record_id    : <rec:c3f17a22-...>,
         execution_id : <exec:g1355h11-...>,
         followup_id  : <fup:h3466i12-...>,
         status       : "FLAGGED",
         flagged_at   : "2026-05-20T10:06:19.598Z"
       }
   STATE: EXECUTING → RESOLVED
   ※ lifecycle §6.1 — 2 open FollowupTickets block expiry until CLOSED
────────────────────────────────────────────────────────────────
```

### Key Design Point

This example illustrates ISM used entirely as a **coordination and audit
layer** rather than an execution layer. Neither step mutates any target —
both are `flag_for_followup`. The record still reaches `RESOLVED` because
all plan steps are `STEP_EXECUTED` (status `FLAGGED` counts). The ISM
record now serves as the authoritative paper trail binding the incident
to two downstream work items owned by infra and privacy teams.

---

## Example 4 — Compromised GCP Service Account Key with Vault Rotation Failure

**Incident class:** `UNAUTHORIZED_ACCESS`
**Severity:** CRITICAL
**Outcome (parent):** FAULTED
**Outcome (child):** RESOLVED
**Lifecycle — parent:** CRITICAL retention · FAULT_ARCHIVAL_DELAY (24h)
**Lifecycle — child:** CRITICAL retention · SPAWNED_FROM lineage depth 1
**Operators exercised (parent):** `ingest` · `classify` · `map_surface_area` ·
  `derive_rectification_steps` · `generate_readonly_plan` ·
  `request_operator_approval` · `execute.rotate_secret` → **PARTIAL_EXECUTION**
**Operators exercised (child):** `ingest` (SPAWNED_FROM) · `classify` ·
  `map_surface_area` · `derive_rectification_steps` ·
  `request_operator_approval` · `execute.rotate_secret` ·
  `execute.flag_for_followup`

### Scenario

At 11:15 UTC ACME's SIEM fires on an anomalous authentication pattern:
a GCP service account key for `data-export-sa@acme-prod.iam.gserviceaccount.com`
is being used from an IP address in eastern Europe not associated with
any known ACME infrastructure. The key was last rotated 6 months ago.
The ISM initiates rotation through HashiCorp Vault's GCP secrets engine.
Rotation begins but the Vault GCP secrets engine returns an error mid-rotation
— the old key version is deactivated, but the new key version is never
written to Vault. The substrate detects this ambiguous state and emits
`PARTIAL_EXECUTION`, transitioning the parent record to `FAULTED`. A child
record is spawned to complete remediation safely.

### Operator Call Trace — Parent Record `<rec:d4g28b33>`

```
── OPERATOR: incident.ingest ────────────────────────────────────
   @ 2026-05-20T11:15:09.004Z
   IN  {
         signal_id    : <sig:2df9f663-...>,
         source       : "acme.siem.splunk-alert-bridge",
         content_type : "application/json",
         emitted_at   : "2026-05-20T11:15:07.112Z",
         severity_hint: "CRITICAL",
         raw_payload  : {
           alert_id      : "SPLUNK-2026-0914",
           alert_type    : "ANOMALOUS_SA_KEY_USAGE",
           service_account: "data-export-sa@acme-prod.iam.gserviceaccount.com",
           key_id        : "projects/acme-prod/serviceAccounts/data-export-sa@acme-prod.iam.gserviceaccount.com/keys/8f3a21bc...",
           anomaly        : "Authentication from 185.220.101.47 (Tor exit node)",
           last_normal_ip : "34.102.136.0/24 (GCP us-central1)",
           key_age_days   : 183,
           api_calls_last_1h : [
             "storage.objects.list on acme-prod-data-lake",
             "bigquery.tables.getData on acme-prod.analytics.*",
             "iam.serviceAccounts.list"
           ],
           vault_secret_path : "gcp/key/data-export-sa"
         }
       }
   OUT {
         record_id   : <rec:d4g28b33-...>,
         ingested_at : "2026-05-20T11:15:09.004Z",
         status      : "ACCEPTED"
       }
   STATE: (none) → INGESTED
────────────────────────────────────────────────────────────────

── OPERATOR: incident.classify ──────────────────────────────────
   @ 2026-05-20T11:15:09.441Z
   IN  {
         record_id     : <rec:d4g28b33-...>,
         classifier_id : "ism-classifier.siem-triage-v6",
         category      : "UNAUTHORIZED_ACCESS",
         subcategory   : "gcp_sa_key.tor_exit_node.data_lake_access",
         confidence    : 0.95,
         rationale     : "Authentication from a confirmed Tor exit node
                          (185.220.101.47 matches Torproject exit list).
                          Key used to enumerate storage and BigQuery objects
                          in production data lake. iam.serviceAccounts.list
                          call suggests attacker is enumerating further
                          lateral movement targets. Classified UNAUTHORIZED_ACCESS
                          (not SECRET_LEAK): the key was not leaked via code —
                          it was acquired or brute-forced externally.
                          Confidence 0.95: key acquisition vector unknown."
       }
   OUT {
         record_id              : <rec:d4g28b33-...>,
         classification_version : 1,
         effective_at           : "2026-05-20T11:15:09.441Z"
       }
   STATE: INGESTED → CLASSIFIED
────────────────────────────────────────────────────────────────

── OPERATOR: incident.map_surface_area ──────────────────────────
   @ 2026-05-20T11:15:10.200Z
   IN  {
         record_id    : <rec:d4g28b33-...>,
         scanner_id   : "ism-scanner.gcp-iam-v2",
         surface_snapshot_hash : "sha256:9fc5e41ab2c8d3f0...",
         surfaces     : [
           {
             surface_type : "SECRET",
             surface_ref  : "vault://gcp/key/data-export-sa",
             access_mode  : "EXECUTE",
             confidence   : 0.99,
             notes        : "Active GCP service account key managed via
                             HashiCorp Vault GCP secrets engine. Key ID
                             8f3a21bc. Vault path: gcp/key/data-export-sa.
                             Must be rotated immediately via Vault to
                             invalidate current key and issue new one."
           },
           {
             surface_type : "CONFIG",
             surface_ref  : "gcp://iam/projects/acme-prod/serviceAccounts/data-export-sa/policy",
             access_mode  : "WRITE",
             confidence   : 0.88,
             notes        : "SA has roles/bigquery.dataViewer, roles/storage.objectViewer
                             on acme-prod project. If attacker performed
                             iam.serviceAccounts.list for lateral movement,
                             the SA's role bindings should be reviewed and
                             
