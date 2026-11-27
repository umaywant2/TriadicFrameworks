<img width="1194" height="672" alt="Ransomware_Structural_Pattern_Detector_adapters_macos_" src="https://github.com/user-attachments/assets/e16ebd2c-1779-4496-8bee-67ffc822ce4a" />

# macOS Adapter

> **Platform adapter specification for mapping authorized macOS resource and system observations into the Ransomware Structural Pattern Detector while preserving observation scope, system-extension, authorization, privacy, recovery, and capability boundaries.**

The macOS adapter connects macOS-observable resource transitions and actor relationships to the platform-neutral Shared Structural Event Grammar.

macOS can support substantially different adapter profiles.

A concrete implementation may be:

- an application-scoped observer;
- a user-authorized resource observer;
- a system-extension-based security component;
- an endpoint-oriented observer with broader system visibility;
- a narrowly configured research or educational implementation;
- another explicitly bounded deployment.

These profiles must not be treated as equivalent.

The governing rule is:

> **Declare what the deployed macOS adapter can actually observe and enforce. Do not promote platform capability into implementation capability, authority, or successful execution.**

---

## Status

- **Adapter ID:** `rspd-macos`
- **Platform:** macOS
- **Status:** Experimental
- **Role:** Observation, normalization, capability declaration, bounded response mapping, and verification support
- **Normalized observation:** `tf.resource-transition/v0.1`
- **Capability declaration:** `tf.platform-capabilities/v0.1`
- **Decision input:** `tf.containment-decision/v0.1`
- **Execution output:** `tf.response-outcome/v0.1`
- **Verification output:** `tf.verification/v0.1`

---

# 1. Scope

The macOS adapter operates within explicitly established application, filesystem, system-extension, authorization, privacy, account, and execution boundaries.

Its potential observation scope may include:

- selected user resources;
- user documents;
- application data;
- project resources;
- configuration;
- archives;
- databases;
- backup-visible resources;
- recovery-visible resources;
- synchronized resources;
- mounted resources;
- adapter-controlled canaries;
- relevant actor activity where exposed;
- relevant system events where exposed;
- other explicitly configured macOS resources.

The implementation must state its actual observation boundary.

Running on macOS does not by itself establish system-wide visibility.

---

# 2. Adapter Profiles

The architecture recognizes several possible macOS adapter profiles.

## Application-Scoped Observer

Observes resources and state available to an ordinary authorized application.

This profile may provide useful structural evidence while possessing limited system-wide actor or enforcement visibility.

## Resource-Scoped Observer

Observes explicitly configured or authorized resource sets.

Its conclusions remain bounded to those resources.

## Endpoint Security Observer

Uses an appropriately provisioned and authorized Endpoint Security client to receive supported macOS system-event information.

This profile may provide stronger actor and event lineage than a purely application-scoped observer.

## Endpoint Security Authorization Profile

Where supported by the concrete implementation and applicable event type, the adapter may participate in authorization handling before a monitored operation completes.

This is a materially different capability from receiving an event notification after an operation.

## Hybrid Observer

Correlates multiple authorized evidence sources while preserving their individual provenance and dependency.

These profiles are descriptive.

A concrete implementation must declare which capabilities it actually possesses.

---

# 3. Endpoint Security Boundary

macOS provides an Endpoint Security framework through which appropriately configured clients can monitor supported system events.

At the structural level:

**Endpoint Security event**

↓

**macOS adapter**

↓

**normalized observation**

↓

**`tf.resource-transition/v0.1`**

↓

**Ransomware Structural Pattern Detector**

The adapter must preserve the fact that Endpoint Security is an observation and authorization source.

It must not turn a native event directly into a ransomware verdict.

---

# 4. Notification vs. Authorization

The adapter must preserve an important distinction between:

**notification**

and:

**authorization**

A notification describes a monitored action that occurred.

An authorization event represents an operation for which an Endpoint Security client may be asked to participate in an allow-or-deny decision before completion.

These have different structural meanings.

A notification can contribute evidence.

An authorization path may also provide an enforcement opportunity.

The adapter must not represent one as the other.

---

# 5. Entitlement and Deployment

Availability of Endpoint Security as a macOS technology does not establish that a particular adapter can use it.

A concrete implementation must separately establish the conditions required for its chosen deployment.

The capability declaration should therefore represent the implementation actually running rather than theoretical framework availability.

If an Endpoint Security client is not available to the implementation, its capabilities must not be advertised merely because macOS provides the framework.

---

# 6. Observation Sources

A macOS implementation may consume one or more authorized evidence sources.

Candidate source classes include:

- Endpoint Security events where available;
- user-authorized resource observations;
- direct application resource activity;
- adapter-maintained state comparisons;
- resource metadata;
- actor/process evidence exposed to the implementation;
- mounted-resource observations;
- synchronization state;
- recovery-state observations;
- user-supplied evidence;
- adapter-maintained baselines.

The normalized event should preserve which source produced the evidence.

---

# 7. Multiple Observation Sources

A stronger implementation may correlate more than one native observation source.

Conceptually:

**system-event evidence**

+

**resource evidence**

+

**actor lineage**

+

**baseline state**

↓

**normalized structural evidence**

Multiple evidence sources may improve confidence and lineage.

They must not automatically inflate event count.

If two sources describe the same underlying transition, their dependency should remain visible.

> **Multiple observations ≠ multiple independent transitions**

---

# 8. Native Observation Preservation

Where feasible and authorized, the adapter should retain a local reference to the native evidence used during normalization.

Useful provenance includes:

- native observation source;
- event reference;
- observation time;
- adapter identity;
- adapter version;
- normalization time;
- relevant capability declaration;
- derivation references;
- redaction classes.

Native evidence may remain local.

The detector requires sufficient structural lineage, not unrestricted raw endpoint telemetry.

---

# 9. Resource Mapping

macOS-visible resources should map into shared structural categories according to role.

Candidate mappings include:

| macOS-visible resource | Shared resource type/class |
|---|---|
| User document | `file` / `user_document` |
| Photo | `file` / `photo` |
| Video | `file` / `video` |
| Audio | `file` / `audio` |
| Database | `file` or `dataset` / `database` |
| Archive | `file` / `archive` |
| Project resource | `file` / `project_file` |
| Application data | `file` or `dataset` / `application_data` |
| Configuration | `configuration` / `configuration` |
| Credential-related store | appropriate type / `credential_store` |
| Backup | appropriate type / `backup` |
| Recovery resource | appropriate type / `recovery_resource` |
| Mounted network resource | appropriate type / `network_resource` |
| Cloud-backed resource | appropriate type / `cloud_resource` |
| Temporary resource | appropriate type / `temporary` |
| Canary | appropriate type / `canary` |
| Other structural resource | appropriate type / `domain_defined` |

The normalized representation should expose structural meaning without unnecessarily exporting user-identifying resource information.

---

# 10. Resource Identity

Raw resource paths may expose personal or sensitive information.

The adapter should prefer a stable privacy-preserving resource reference when that is sufficient for structural correlation.

A native resource reference may remain local for:

- correlation;
- enforcement;
- recovery;
- verification;
- authorized investigation.

The shared event may instead carry:

- resource ID;
- resource type;
- resource class;
- scope;
- sensitivity;
- protection state;
- canary state;
- recoverability;
- bounded location reference when structurally necessary.

---

# 11. Actor Mapping

Candidate macOS actor mappings include:

- `process`
- `application`
- `service`
- `script`
- `remote_actor`
- `sync_service`
- `system`
- `user`
- `agent`
- `unknown`

Where evidence supports it, the adapter may preserve:

- actor ID;
- actor name;
- actor instance;
- parent reference;
- account reference;
- origin relationship;
- transport relationship.

The evidence source must determine how strongly actor identity can be stated.

---

# 12. Actor Lineage

Where reliable actor relationships are exposed, the adapter should preserve them.

Conceptually:

**invoking actor**

↓

**observed actor**

↓

**resource transition**

Actor lineage can strengthen structural reasoning about whether an operation is coherent with the actor's established role.

It does not establish intent.

A familiar or signed actor can still participate in a destructive structural transition.

---

# 13. Trust and Signing Context

Where the implementation obtains bounded trust or signing information, it may preserve that context in the shared actor representation.

Such information may help describe:

- whether an actor is known;
- whether available identity evidence is consistent;
- whether a recognized signing or publisher relationship exists.

It must not suppress contradictory behavioral evidence.

The detector follows:

> **Trusted actor ≠ safe transition**

and:

> **known identity ≠ benign intent**

---

# 14. Origin vs. Transport

Synchronization, remote resources, services, and intermediary applications can separate observed actor from ultimate origin.

A locally visible actor may:

- originate a transition;
- transport a remote transition;
- materialize synchronized state;
- operate on behalf of another process or service;
- reflect state originating elsewhere.

Where sufficient evidence exists, the adapter should preserve:

- origin actor;
- transport actor;
- origin environment;
- observed actor;
- synchronization context.

Otherwise, origin remains unresolved.

---

# 15. Transition Mapping

Candidate normalized operations include:

- `read`
- `write`
- `create`
- `delete`
- `rename`
- `move`
- `truncate`
- `copy`
- `replace`
- `open`
- `close`
- `permission_change`
- `metadata_change`
- `recovery_change`
- `state_change`
- `scope_change`
- `execute`
- `sync`
- `other`

Candidate structural actions include:

- `access`
- `modify`
- `create`
- `remove`
- `replace`
- `relocate`
- `duplicate`
- `restrict`
- `grant`
- `revoke`
- `expose`
- `conceal`
- `restore`
- `propagate`
- `transform`
- `other`

A native operation should be retained where forcing it into the shared vocabulary would lose relevant lineage.

---

# 16. Transition Characteristics

Where observable or explicitly derived, the adapter may normalize characteristics such as:

- content-change indication;
- structural change;
- size change;
- representation change;
- ownership or authority change;
- permission change;
- recovery-state change;
- prior-state preservation;
- recoverability;
- repeated mutation;
- transition timing;
- synchronization transport.

These are structural observations or derivations.

They are not ransomware classifications.

---

# 17. Baseline Support

A concrete implementation may maintain a structural baseline for its authorized scope.

Candidate baseline dimensions include:

- known actors;
- expected actor roles;
- typical operations;
- expected resource classes;
- typical transition rate;
- common resource scope;
- established applications;
- backup behavior;
- synchronization behavior;
- known bulk workflows.

Baseline comparison may help distinguish destructive deviation from ordinary system activity.

An unfamiliar actor or unusual transition remains evidence to evaluate, not proof of malicious intent.

---

# 18. Legitimate Bulk Activity

macOS may host workflows capable of changing many resources legitimately.

Potential competing explanations include:

- backups;
- restores;
- synchronization;
- migrations;
- development builds;
- media processing;
- archival operations;
- authorized encryption;
- application-managed transformation;
- user-directed bulk activity.

Where observable, evidence supporting those explanations should remain visible.

The detector evaluates whether the current behavior remains coherent with the claimed workflow.

---

# 19. Canary Resources

A concrete implementation may use adapter-controlled canary resources where appropriate and authorized.

A canary transition may provide strong evidence that unexpected mutation reached a monitored surface.

It does not independently establish:

- ransomware;
- malicious intent;
- actor attribution;
- scope outside the canary's observation boundary.

Canaries should contain no sensitive user information.

---

# 20. Capability Declaration

Every concrete macOS adapter should provide:

`tf.platform-capabilities/v0.1`

The declaration describes the implementation actually deployed.

Possible observation capabilities include:

- event observation;
- actor identity;
- actor lineage;
- resource classification;
- network context;
- origin/transport distinction;
- baseline access;
- resource metadata;
- recovery-state observation.

Possible enforcement capabilities include:

- write denial;
- actor containment;
- resource isolation;
- network isolation;
- quarantine;
- permission restriction;
- actor disablement;
- session termination.

Possible recovery capabilities include:

- recovery;
- rollback;
- snapshot restoration;
- resource restoration;
- configuration restoration.

Possible verification capabilities include:

- post-action observation;
- state comparison;
- persistence detection;
- reappearance detection;
- recovery verification.

Each capability must be declared as:

- `supported`
- `partial`
- `unsupported`
- `unknown`

---

# 21. Capability Profiles

A macOS implementation may expose substantially different profiles.

## Application Profile

Useful resource-level observation with limited endpoint-wide visibility or enforcement.

## Endpoint Observation Profile

Broader system-event evidence where an appropriately configured Endpoint Security implementation is available.

## Endpoint Authorization Profile

A profile in which applicable native operations can participate in authorization decisions.

## Hybrid Profile

Multiple authorized event and resource sources correlated through the adapter.

The profile name does not determine capability by itself.

The actual `tf.platform-capabilities/v0.1` declaration remains authoritative.

---

# 22. Capability Is Not Authority

Availability of a native macOS mechanism does not authorize its use.

Therefore:

> **Framework capability ≠ adapter capability**

> **Adapter capability ≠ authority**

> **Authority ≠ execution**

The containment decision must establish the governing response boundary independently of technical support.

---

# 23. Authorization-Event Handling

Where a concrete implementation legitimately supports Endpoint Security authorization events, it may map an authorized structural response onto a supported allow-or-deny decision.

This is a pre-execution intervention opportunity.

The adapter must still preserve:

- requested action;
- relevant native event;
- decision authority;
- actual native response;
- execution result;
- resulting structural state.

A native denial does not establish that the wider destructive pattern is resolved.

It establishes that the bounded operation was denied.

---

# 24. Notification-Event Handling

Notification events provide post-event evidence.

They may contribute to:

- transition reconstruction;
- actor lineage;
- baseline assessment;
- pattern correlation;
- verification.

They must not be represented as pre-execution control.

The adapter should preserve whether evidence came from:

**notification**

or:

**authorization**

when that distinction materially affects interpretation.

---

# 25. Containment Mapping

An authorized containment decision may request responses such as:

- increase observation;
- notify an authorized operator;
- deny resource writes;
- contain an actor;
- isolate a resource set;
- isolate a network scope;
- quarantine affected resources;
- restrict actor permissions;
- disable an actor;
- preserve evidence;
- prepare recovery;
- initiate recovery;
- request manual review.

A concrete macOS adapter maps only supported and authorized actions onto native mechanisms.

This generic specification intentionally does not mandate one implementation for each structural response.

---

# 26. Write Denial

Where the concrete implementation possesses an appropriate authorized mechanism for denying an applicable write operation, it may map:

`deny_resource_writes`

onto that mechanism.

The adapter must preserve the actual scope.

A denied operation on one resource or bounded target does not establish:

- actor-wide containment;
- filesystem-wide containment;
- host-wide containment;
- cross-environment containment.

The outcome records what was actually denied.

---

# 27. Actor Containment

Where supported and authorized, an adapter may attempt an action intended to contain a relevant actor.

The exact native mechanism remains implementation-specific.

The outcome should preserve:

- actor target;
- containment scope;
- whether execution was attempted;
- what actually executed;
- direct effects;
- errors;
- limitations.

Containing a local actor does not establish that a remote or synchronized origin has been resolved.

---

# 28. Resource Isolation

Where a concrete implementation can isolate or restrict an affected resource set, it should preserve:

- resource scope;
- access boundary;
- reversibility;
- rollback availability;
- actual resulting state.

Resource isolation is distinct from:

- actor containment;
- network isolation;
- recovery;
- resolution.

---

# 29. Network Isolation

Some concrete deployments may have a supported mechanism for limiting network communication.

This generic adapter does not assume such capability.

Where available, the adapter must describe its actual scope and limitations.

Network isolation of a local execution context does not automatically establish containment of:

- remote state;
- cloud-backed state;
- already propagated resources;
- another device.

---

# 30. Fallback

If a requested response cannot be executed and fallback is permitted, the adapter may select a bounded alternative.

Conceptually:

**Requested**

`deny_resource_writes`

↓

**native capability unavailable for requested scope**

↓

**Fallback**

`contain_actor`

or:

**Requested**

`contain_actor`

↓

**authorization unavailable**

↓

**Fallback**

`notify_authorized_operator`

The actual fallback is policy-driven.

The adapter records the degradation honestly.

---

# 31. Outcome Reporting

Every attempted response should produce or contribute to:

`tf.response-outcome/v0.1`

Relevant execution states include:

- `not_attempted`
- `blocked`
- `unsupported`
- `authorization_required`
- `attempted`
- `partially_executed`
- `executed`
- `failed`
- `unknown`

The outcome should preserve:

- requested response;
- execution attempt;
- executed response;
- fallback;
- capability context;
- actual scope;
- direct effects;
- side effects;
- errors;
- warnings;
- rollback state;
- execution provenance.

---

# 32. Native Success Is Not Structural Resolution

A macOS mechanism may report that its bounded operation succeeded.

That means only that the operation completed as reported within its native boundary.

It does not establish:

- that the destructive pattern stopped everywhere;
- that another actor did not continue it;
- that synchronized state did not reintroduce it;
- that affected resources were recovered;
- that the originating condition disappeared.

Therefore:

> **Execution success ≠ verification success**

---

# 33. Verification

Post-response verification should rescan the authorized environment with the capabilities actually available.

Relevant questions include:

- Are destructive transitions continuing?
- Is the relevant actor still active?
- Did another actor continue the same pattern?
- Did resource scope continue to expand?
- Did synchronization reintroduce the transition?
- Did the condition reappear?
- Did recovery state change?
- Are protected resources now stable?
- Did the containment action produce material side effects?
- Is the observation scope sufficient to make the intended claim?

Verification may produce:

- `contained`
- `partially_contained`
- `persistent`
- `reappeared`
- `resolved`
- `partially_resolved`
- `new_condition_detected`
- `mixed`
- `unable_to_verify`

---

# 34. Verification Scope

Verification conclusions must remain bounded.

For example:

**No further destructive transition observed in the protected resource set**

does not imply:

**The entire Mac is clean**

Likewise:

**Local actor no longer observed**

does not imply:

**Remote origin resolved**

The verification object's observation scope and limitations determine the strength of the conclusion.

---

# 35. Recovery

Recovery capability depends on the concrete resource and deployment.

An implementation may have visibility into or support for:

- preserved originals;
- backup state;
- historical versions;
- snapshots;
- synchronized history;
- recovery resources;
- other configured restoration mechanisms.

The adapter should distinguish:

**mechanism exists**

from:

**usable recovery state exists**

from:

**recovery requested**

from:

**recovery attempted**

from:

**recovery completed**

from:

**restored state verified**

---

# 36. Synchronization

For synchronized resources, the macOS adapter should cooperate with the Cloud / Synchronization adapter.

The macOS side may establish:

> **This local actor or synchronization client materialized this transition.**

The cloud-sync side may establish:

> **This transition originated elsewhere or propagated across an environment boundary.**

The combined lineage should preserve dependency rather than turning each observation into a separate independent origin.

---

# 37. Mounted and Remote Resources

A macOS adapter may observe transitions affecting resources whose storage origin lies elsewhere.

For such resources:

**local observation**

does not automatically establish:

**local origin**

or:

**local recovery authority**.

The adapter should preserve resource scope, transport relationships, environment relationships, and available recovery context where known.

---

# 38. Privacy and Redaction

macOS endpoint observations may expose sensitive resource and actor information.

The adapter should minimize what leaves the local environment.

Preferred shared information includes:

- privacy-preserving resource ID;
- resource class;
- resource scope;
- sensitivity;
- transition type;
- transition timing;
- actor category;
- actor relationship;
- baseline state;
- preservation state;
- recovery state;
- synchronization context;
- platform provenance.

Avoid exporting unnecessary:

- document contents;
- personal filenames;
- raw absolute paths;
- credentials;
- authentication tokens;
- private keys;
- sensitive process arguments;
- unrelated application data;
- unrelated account information.

---

# 39. Credential Boundary

The shared detector does not require authentication secrets.

The macOS adapter must not emit:

- plaintext passwords;
- private keys;
- session secrets;
- authentication tokens;
- cloud credentials;
- recovery secrets.

Where identity context is structurally relevant, a bounded account or authority reference should be used instead.

---

# 40. Local Processing Preference

Sensitive native operations should remain local when normalized structure is sufficient.

Candidate local operations include:

- native-event handling;
- actor correlation;
- resource classification;
- path handling;
- identifier pseudonymization;
- baseline comparison;
- source deduplication;
- state comparison;
- redaction;
- native-to-shared transition mapping.

The objective is not to centralize raw endpoint activity.

It is to expose enough structural evidence for reliable analysis.

---

# 41. Event Loss and Observation Gaps

A concrete adapter should preserve known gaps in event coverage.

Examples include:

- observer initialization gaps;
- event-stream disruption;
- unavailable native source;
- adapter restart;
- temporary loss of authorization;
- lost or incomplete telemetry;
- unobserved resource scope.

An observation gap must remain a gap.

Silence during the gap is not evidence that no transition occurred.

---

# 42. Restart and Continuity

The adapter should preserve enough state to distinguish:

- uninterrupted observation;
- resumed observation;
- known observation gap;
- baseline reset;
- unknown continuity.

This is particularly important when downstream analysis derives:

- activity rate;
- acceleration;
- persistence;
- reappearance;
- scope expansion.

A restarted observer must not silently imply continuous evidence.

---

# 43. Temporal Ordering

When multiple observation sources are correlated, ordering should follow the best available source evidence.

The adapter should preserve:

- native event time;
- normalization time;
- sequence context where available;
- ordering uncertainty.

The detector should not infer causal order merely from the order in which normalized events arrived.

---

# 44. Known Limitations

Concrete macOS adapters should document implementation-specific limitations such as:

- unavailable Endpoint Security capability;
- entitlement or deployment constraints;
- application-only visibility;
- incomplete filesystem scope;
- inaccessible resources;
- incomplete actor identity;
- incomplete actor lineage;
- mounted-resource ambiguity;
- synchronization ambiguity;
- incomplete network context;
- incomplete recovery state;
- unsupported enforcement actions;
- authorization restrictions;
- event gaps;
- incomplete post-response verification.

Limitations belong in the structural record.

---

# 45. Capability Posture

The generic macOS adapter begins from:

| Capability | Generic posture |
|---|---|
| Event observation | `unknown` |
| Actor identity | `unknown` |
| Actor lineage | `unknown` |
| Resource classification | `unknown` |
| Network context | `unknown` |
| Origin / transport distinction | `unknown` |
| Baseline access | `unknown` |
| Recovery-state observation | `unknown` |
| Write denial | `unknown` |
| Actor containment | `unknown` |
| Resource isolation | `unknown` |
| Network isolation | `unknown` |
| Quarantine | `unknown` |
| Permission restriction | `unknown` |
| Actor disablement | `unknown` |
| Session termination | `unknown` |
| Recovery | `unknown` |
| Rollback | `unknown` |
| Snapshot restore | `unknown` |
| Post-action observation | `unknown` |
| State comparison | `unknown` |
| Persistence detection | `unknown` |
| Reappearance detection | `unknown` |
| Recovery verification | `unknown` |

This does not mean macOS lacks these capabilities.

It means the generic specification does not claim that a particular implementation possesses them.

---

# 46. Why the Generic Posture Is Unknown

Apple documents Endpoint Security as a macOS facility for monitoring system events, with support for notification and authorization handling for supported monitored operations.

That establishes platform capability.

It does not establish that:

- a given adapter uses Endpoint Security;
- the adapter has the required deployment conditions;
- the relevant event is exposed;
- the requested resource is within scope;
- the required authorization exists;
- another response mechanism is available.

Therefore:

> **Platform capability is evidence about the platform. Adapter capability is evidence about the implementation.**

The latter belongs in `tf.platform-capabilities/v0.1`.

---

# 47. macOS Adapter Invariants

## MACOS-INV-01 — Platform Capability ≠ Adapter Capability

The existence of a macOS framework does not establish that a concrete adapter can use it.

## MACOS-INV-02 — Notification ≠ Authorization

An event notification and an authorization opportunity have different structural semantics.

## MACOS-INV-03 — Observation Boundary ≠ Host Boundary

A bounded observer must not imply visibility across the entire Mac.

## MACOS-INV-04 — Native Event ≠ Ransomware Verdict

A system or filesystem event is evidence, not a domain conclusion.

## MACOS-INV-05 — Actor Identity ≠ Intent

A process, application, service, script, system component, or user identity does not establish motive.

## MACOS-INV-06 — Trusted Actor ≠ Safe Transition

Known identity or trust context must not suppress contradictory destructive behavior.

## MACOS-INV-07 — Actor ≠ Origin

A local actor may transport or materialize a transition originating elsewhere.

## MACOS-INV-08 — Multiple Sources ≠ Independent Transitions

Several native observations may describe one underlying structural change.

## MACOS-INV-09 — Capability ≠ Authority

Technical support for an action does not authorize its use.

## MACOS-INV-10 — Authorization Opportunity ≠ Policy Authorization

A native event that can technically be allowed or denied does not itself establish the policy decision to deny it.

## MACOS-INV-11 — Requested Response ≠ Executed Response

Unsupported, blocked, partial, failed, and fallback outcomes remain explicit.

## MACOS-INV-12 — Execution ≠ Resolution

A successful native response does not prove that the broader destructive pattern has resolved.

## MACOS-INV-13 — Local Containment ≠ Remote Containment

Local intervention does not establish that synchronized, cloud, or other remote origin state is resolved.

## MACOS-INV-14 — Recovery Capability ≠ Verified Restoration

Availability of a recovery mechanism does not establish successful resource recovery.

## MACOS-INV-15 — Observation Gap ≠ No Activity

Unavailable telemetry cannot be interpreted as proof that no transition occurred.

## MACOS-INV-16 — Privacy Survives Normalization

Raw content, resource paths, credentials, and unrelated endpoint telemetry should remain local when structural references are sufficient.

---

# 48. Non-Goals

The macOS adapter is not:

- a malware-signature engine;
- a ransomware classifier;
- an attribution system;
- a guarantee of endpoint-wide visibility;
- a guarantee that Endpoint Security is available to every implementation;
- a guarantee of process attribution;
- a guarantee of containment;
- a guarantee of recovery;
- an authorization engine;
- a mechanism for bypassing macOS security controls;
- a reason to centralize raw user content or credentials.

Its role is narrower:

> **Observe authorized macOS structural evidence, normalize it faithfully, declare actual capabilities and limitations, map separately authorized responses onto supported mechanisms, record what actually happened, and support bounded verification.**

---

# 49. Shared Contracts

The macOS adapter participates in:

- `tf.resource-transition/v0.1`
- `tf.platform-capabilities/v0.1`
- `tf.containment-decision/v0.1`
- `tf.response-outcome/v0.1`
- `tf.verification/v0.1`

The Ransomware Structural Pattern Detector consumes its normalized observations and may produce:

- `tf.structural-pattern/v0.1`

The macOS adapter does not redefine those contracts.

---

# 50. Relationship to Cloud / Synchronization

For synchronized resources, the macOS adapter should cooperate with the Cloud / Synchronization adapter.

The local adapter may establish:

> **This actor or synchronization component materialized the transition on this Mac.**

The cloud-sync adapter may establish:

> **The transition originated or propagated through another environment.**

The detector may correlate both pieces of evidence while preserving their dependency.

---

# 51. Relationship to iOS / iPadOS

The macOS and iOS / iPadOS adapters share the same structural grammar but intentionally do not assume equal capability.

The macOS adapter may be able to consume system-level observation sources unavailable to a conventional application-scoped mobile adapter.

The exact capability of either adapter remains deployment-specific.

The grammar stays stable while the capability declaration changes.

This is the intended architecture:

> **Portable semantics, explicit platform variance.**

---

# Canonical Summary

> **The macOS adapter maps authorized macOS resource, actor, and supported system-event observations into the Shared Structural Event Grammar while preserving the distinction between platform capability, adapter capability, policy authority, execution, and verified state.**

Its platform rule is:

> **A macOS API establishes a possible platform mechanism, not an automatic adapter capability.**

Its observation rule is:

> **Normalize what the deployed observer actually sees and preserve the source of that evidence.**

Its Endpoint Security rule is:

> **Notification describes evidence of a monitored action. Authorization provides a bounded opportunity to allow or deny a supported action. Neither independently establishes ransomware.**

Its actor rule is:

> **Known or trusted identity does not override contradictory destructive behavior, and the locally visible actor may not be the ultimate origin.**

Its response rule is:

> **A native control may implement an authorized structural response only within its actual supported scope.**

Its continuity rule is:

> **Observation gaps remain evidence gaps.**

Its privacy rule is:

> **Keep raw endpoint detail local whenever privacy-preserving structural representation is sufficient.**

Its verification rule is:

> **A successfully denied or contained operation is evidence about that operation, not proof that the entire destructive pattern has resolved.**
