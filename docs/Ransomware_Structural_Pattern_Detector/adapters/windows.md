<img width="1194" height="672" alt="Ransomware_Structural_Pattern_Detector_adapters_windows_" src="https://github.com/user-attachments/assets/49142836-4fd1-44a2-8d92-8ac0283710be" />

# Windows Adapter

> **Platform adapter specification for mapping authorized Windows resource and system observations into the Ransomware Structural Pattern Detector while preserving observation scope, actor lineage, filesystem, recovery, privilege, synchronization, and capability boundaries.**

The Windows adapter connects Windows-observable resource transitions and actor relationships to the platform-neutral Shared Structural Event Grammar.

Windows can support substantially different adapter profiles.

A concrete implementation may be:

- an application-scoped observer;
- a resource-scoped observer;
- an event-driven endpoint observer;
- a filesystem-oriented security component;
- an endpoint-security integration;
- a narrowly configured research or educational implementation;
- another explicitly bounded deployment.

These profiles must not be treated as equivalent.

The governing rule is:

> **Declare what the deployed Windows adapter can actually observe and enforce. Do not promote Windows platform capability into adapter capability, policy authority, execution success, or verified resolution.**

---

## Status

- **Adapter ID:** `rspd-windows`
- **Platform:** Windows
- **Status:** Experimental
- **Role:** Observation, normalization, capability declaration, bounded response mapping, and verification support
- **Normalized observation:** `tf.resource-transition/v0.1`
- **Capability declaration:** `tf.platform-capabilities/v0.1`
- **Decision input:** `tf.containment-decision/v0.1`
- **Execution output:** `tf.response-outcome/v0.1`
- **Verification output:** `tf.verification/v0.1`

---

# 1. Scope

The Windows adapter operates within explicitly established application, filesystem, account, endpoint, authorization, security, storage, and execution boundaries.

Its potential observation scope may include:

- user documents;
- selected directories;
- application data;
- configuration;
- databases;
- archives;
- project files;
- shared resources;
- mounted or mapped resources;
- backup resources;
- recovery resources;
- synchronized resources;
- protected resource sets;
- adapter-controlled canaries;
- relevant actor activity where observable;
- relevant Windows system activity where observable;
- other explicitly configured resources.

A concrete implementation must state its actual observation boundary.

Running on Windows does not by itself establish endpoint-wide visibility.

---

# 2. Deployment Variability

The generic Windows adapter describes an architectural class rather than one installed endpoint product.

Capability may vary according to:

- Windows edition and deployment;
- implementation architecture;
- observation mechanism;
- execution privileges;
- security policy;
- configured resource scope;
- account context;
- storage topology;
- network topology;
- synchronization environment;
- endpoint-security integration;
- recovery configuration;
- authorization.

Therefore:

> **Windows describes the platform family. The concrete capability declaration describes the adapter.**

---

# 3. Observation Model

A Windows implementation may combine one or more authorized sources of structural evidence.

Conceptually:

**Windows observation source**

↓

**adapter-local mapping**

↓

**normalization**

↓

**`tf.resource-transition/v0.1`**

↓

**Ransomware Structural Pattern Detector**

The adapter should preserve which observation source produced each item of evidence.

It must not turn a Windows event directly into a ransomware verdict.

---

# 4. Event-Driven Observation

A concrete implementation may consume event-driven observations exposed through its authorized Windows environment.

Potential structural evidence may concern:

- resource creation;
- resource modification;
- deletion;
- rename;
- relocation;
- replacement;
- access;
- process activity;
- service activity;
- permission or authority changes;
- recovery-state changes;
- network context;
- synchronization behavior;
- other implementation-visible state.

Only fields actually supported by the observation source should be populated.

Unavailable information remains unresolved.

---

# 5. Event Tracing

A Windows implementation may use Event Tracing for Windows or another authorized event source as part of its observation strategy.

At the architecture level, such telemetry may contribute evidence about relationships among:

- processes;
- resource activity;
- configuration state;
- network activity;
- execution sequences;
- other observable system behavior.

The adapter must preserve which observations were actually collected.

The existence of a Windows telemetry facility does not establish that a particular implementation subscribes to every relevant source or receives every relevant event.

---

# 6. Filesystem Observation

A Windows adapter may observe filesystem transitions through an implementation-specific mechanism.

The generic architecture is concerned with the normalized structural result:

- actor;
- resource;
- operation;
- transition;
- context;
- baseline;
- consequence;
- provenance.

The adapter may retain native filesystem evidence locally when needed for:

- correlation;
- containment;
- recovery;
- verification;
- authorized investigation.

The shared detector does not require unrestricted raw filesystem telemetry.

---

# 7. Filesystem Filtering Profile

A concrete Windows security implementation may use a filesystem filtering architecture when appropriately implemented and authorized.

Such a profile may provide an observation or intervention point closer to filesystem activity than a purely post-event observer.

The adapter must still distinguish:

**observation**

from:

**pre-operation intervention**

from:

**completed response**

from:

**verified resulting state**.

A mechanism capable of intercepting an operation does not by itself authorize the adapter to block it.

---

# 8. Multiple Observation Sources

A stronger Windows implementation may correlate several evidence sources.

Conceptually:

**filesystem evidence**

+

**process evidence**

+

**system-event evidence**

+

**network context**

+

**recovery context**

↓

**normalized structural evidence**

Multiple evidence streams may strengthen structural reconstruction.

They must not automatically inflate event count or evidence independence.

> **Multiple telemetry sources may describe one underlying transition.**

---

# 9. Observation Provenance

Normalized observations should retain sufficient provenance to reconstruct their source.

Relevant provenance may include:

- Windows environment;
- adapter identity;
- adapter version;
- observation source;
- native-event reference;
- observation time;
- normalization time;
- capability declaration;
- derivation references;
- redaction classes.

Native logs or event payloads may remain local.

---

# 10. Resource Mapping

Windows-visible resources should map into shared categories according to structural role.

| Windows-visible resource | Shared resource type/class |
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
| Network-backed resource | appropriate type / `network_resource` |
| Cloud-backed resource | appropriate type / `cloud_resource` |
| Temporary resource | appropriate type / `temporary` |
| Canary | appropriate type / `canary` |
| Other resource | appropriate type / `domain_defined` |

The normalized representation should expose structural meaning without unnecessarily exporting user-identifying information.

---

# 11. Resource Identity

Windows resource paths can contain sensitive user, organization, project, or system information.

The central analyzer does not inherently require raw paths.

A concrete adapter should prefer privacy-preserving stable identifiers where sufficient.

Native resource identifiers may remain local for:

- correlation;
- enforcement;
- recovery;
- verification;
- authorized investigation.

The shared event may instead carry structural resource identity and classification.

---

# 12. Volume and Storage Boundaries

A Windows environment may contain resources spanning different storage boundaries.

A concrete implementation should preserve relevant distinctions among:

- local resources;
- separate volumes;
- removable storage where applicable;
- network-backed resources;
- mapped resources;
- synchronized resources;
- cloud-backed resources;
- recovery resources;
- other configured storage boundaries.

Observation of one boundary must not be generalized to another without evidence.

---

# 13. Actor Mapping

Candidate Windows actors include:

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

Where available, the adapter should preserve:

- actor ID;
- actor type;
- actor name;
- parent reference;
- instance reference;
- account reference;
- origin role;
- transport role.

If the observation source cannot reliably establish an actor, the adapter must not invent one.

---

# 14. Process Lineage

Reliable process lineage can materially improve structural analysis.

Conceptually:

**parent actor**

↓

**child actor**

↓

**resource transition**

Where available, the adapter should preserve such relationships.

They may support questions such as:

- Is this operation coherent with the actor's established role?
- Is a familiar application acting through an unexpected child?
- Did several resource transitions share the same actor lineage?
- Is a locally visible process the origin or merely one part of a longer chain?

Process lineage remains evidence.

It does not establish malicious intent.

---

# 15. User, Service, and Automation Context

Windows resource transitions may occur in:

- interactive user sessions;
- service contexts;
- automated tasks;
- application contexts;
- administrative contexts;
- remote contexts;
- synchronization contexts;
- other execution environments.

Where observable, context should be preserved structurally.

The adapter must not equate:

**account under which activity occurred**

with:

**human intent**.

> **Execution identity ≠ human intent.**

---

# 16. Trust and Identity Context

Where legitimate evidence exists, an implementation may preserve actor trust or identity context.

Examples may include whether an actor is:

- known;
- unknown;
- partially identified;
- conflicting in identity;
- trusted under an established policy;
- associated with available publisher or signing information.

This context must not override observed destructive behavior.

> **Trusted actor ≠ safe transition.**

---

# 17. Origin vs. Transport

Synchronization, remote resources, services, management tools, and intermediary processes can separate the locally observed actor from the originating actor.

A Windows actor may:

- originate a transition;
- transport a remote transition;
- materialize synchronized state;
- operate on behalf of another component;
- reflect activity originating elsewhere.

Where evidence permits, preserve:

- origin actor;
- transport actor;
- observed actor;
- origin environment;
- synchronization context.

Otherwise, origin remains unresolved.

---

# 18. Transition Mapping

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
- `authority_change`
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

The adapter should retain a native operation when useful for diagnostic lineage.

---

# 19. Transition Characteristics

Where directly observable or explicitly derived, a Windows implementation may normalize characteristics such as:

- content-change indication;
- structural change;
- size change;
- representation or extension change;
- ownership change;
- permission change;
- authority change;
- scope change;
- recovery-state change;
- prior-state preservation;
- recoverability;
- transition timing;
- synchronization transport;
- repeated mutation.

These fields provide evidence for downstream correlation.

They do not independently establish ransomware.

---

# 20. Baseline Support

A concrete implementation may maintain a baseline for its authorized Windows scope.

Candidate dimensions include:

- known actors;
- expected actor roles;
- typical operations;
- expected resource classes;
- typical transition rate;
- normal resource scope;
- established services;
- known administrative workflows;
- backup behavior;
- synchronization behavior;
- expected high-volume operations.

Baseline deviation strengthens or weakens structural hypotheses.

It does not establish intent.

---

# 21. Legitimate Bulk Activity

Windows systems may perform broad resource transitions for legitimate reasons.

Potential competing explanations include:

- backup;
- restoration;
- synchronization;
- migration;
- software deployment;
- development or build activity;
- archive operations;
- media processing;
- authorized encryption;
- administrative automation;
- other established bulk workflows.

Evidence supporting a legitimate workflow should remain visible as counter-evidence.

Likewise, the presence of a legitimate-looking actor must not erase destructive effects that contradict the expected workflow.

---

# 22. Canary Resources

A concrete Windows implementation may maintain adapter-controlled canary resources inside authorized observation boundaries.

Unexpected transition of a canary may provide strong evidence that destructive activity reached the monitored scope.

It does not independently establish:

- ransomware;
- intent;
- attribution;
- host-wide impact.

Canaries should contain no sensitive user information.

---

# 23. Recovery-State Observation

Recovery state is particularly important to ransomware-oriented structural analysis.

A Windows adapter may, where its concrete environment provides the evidence, observe structural state concerning:

- backup resources;
- historical resource state;
- snapshots;
- recovery configuration;
- recovery-resource availability;
- changes affecting recoverability.

Such observations should be represented as resource and transition evidence.

They should not automatically be labeled malicious.

A recovery-resource transition may have legitimate administrative or backup explanations.

---

# 24. Volume Shadow Copy Service

Where relevant to the concrete environment, Volume Shadow Copy Service state may contribute recovery-context evidence.

The adapter should treat VSS-related state as **recovery structure**, not a standalone ransomware verdict.

A transition affecting shadow-copy or related recovery state may strengthen a destructive-pattern assessment when correlated with other evidence.

But:

> **VSS activity ≠ ransomware.**

Legitimate backup and administrative workflows may also interact with recovery state.

The detector must evaluate the surrounding structure.

---

# 25. Recovery Interference

The detector's `recovery_interference` signal may be supported when normalized Windows evidence establishes material adverse changes to relevant recovery resources or configuration.

The adapter supplies the evidence.

The detector determines whether that evidence contributes to a ransomware-like pattern.

This preserves:

**recovery observation**

↓

**structural correlation**

↓

**bounded assessment**

rather than:

**recovery event**

↓

**automatic ransomware verdict**.

---

# 26. Capability Declaration

Every concrete Windows adapter should provide:

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

Each capability is declared as:

- `supported`
- `partial`
- `unsupported`
- `unknown`

---

# 27. Capability Profiles

A Windows adapter may expose different profiles.

## Application Profile

Narrow resource visibility and limited endpoint-level enforcement.

## Endpoint Observation Profile

Broader system and resource observations where supported by the implementation.

## Filesystem Intervention Profile

An appropriately implemented and authorized profile with a filesystem-level intervention opportunity.

## Security Integration Profile

An adapter obtaining structural evidence or response capability through another authorized endpoint-security mechanism.

## Hybrid Profile

Multiple authorized observation sources correlated while retaining their provenance and dependency.

These profiles describe architecture, not promised capabilities.

---

# 28. Capability Is Not Authority

Windows may expose powerful mechanisms.

That does not authorize their use.

Therefore:

> **Platform mechanism ≠ adapter capability**

> **Adapter capability ≠ policy authority**

> **Policy authority ≠ successful execution**

A containment decision must establish the response boundary separately.

---

# 29. Intervention Opportunity vs. Decision Authority

A native mechanism may expose an opportunity to allow, deny, restrict, suspend, isolate, or otherwise alter an operation.

That technical opportunity does not determine whether the adapter should do so.

The adapter must still evaluate:

- containment decision;
- authorization;
- target;
- scope;
- constraints;
- reversibility;
- declared platform capability.

The structural policy remains outside the native mechanism.

---

# 30. Containment Mapping

An authorized containment decision may request:

- increased observation;
- operator notification;
- resource-write denial;
- actor containment;
- resource isolation;
- network isolation;
- quarantine;
- permission restriction;
- actor disablement;
- evidence preservation;
- recovery preparation;
- recovery initiation;
- manual review.

A concrete Windows implementation maps only supported and authorized requests onto appropriate native mechanisms.

This generic specification intentionally does not mandate one implementation strategy.

---

# 31. Write Containment

Where the concrete adapter possesses an authorized mechanism capable of preventing applicable resource writes, it may map:

`deny_resource_writes`

onto that mechanism.

The outcome must preserve actual scope.

Blocking one operation, actor, directory, resource set, or volume must not silently become a claim of endpoint-wide write containment.

> **Bounded denial remains bounded denial.**

---

# 32. Actor Containment

Where supported and authorized, the adapter may attempt to contain an actor associated with destructive transitions.

The concrete implementation determines the native mechanism.

The outcome should preserve:

- target actor;
- containment scope;
- authorization;
- attempted action;
- executed action;
- direct effects;
- limitations;
- errors.

Local actor containment does not establish that a synchronized or remote origin has disappeared.

---

# 33. Resource Isolation

Where supported, resource isolation may restrict continued access to an affected resource or resource set.

The adapter should record:

- target;
- scope;
- access boundary affected;
- reversibility;
- rollback availability;
- actual outcome.

Resource isolation remains distinct from:

- actor containment;
- network containment;
- quarantine;
- recovery;
- verified resolution.

---

# 34. Network Isolation

Some concrete Windows deployments may provide a mechanism capable of restricting relevant network communication.

This generic specification does not assume such support.

Where available, the outcome must preserve actual scope.

Network isolation of a local endpoint or actor does not establish:

- remote-state containment;
- cloud-state containment;
- resource recovery;
- removal of already propagated state.

---

# 35. Quarantine

Where a concrete implementation supports quarantine, the adapter should represent what actually happened structurally.

Relevant questions include:

- What was quarantined?
- Was the target an actor, resource, or resource set?
- Was access restricted?
- Was the action reversible?
- Was prior state preserved?
- Did quarantine succeed within the requested scope?

Quarantine is an action.

It is not verification that the underlying pattern resolved.

---

# 36. Fallback

If a requested action cannot be performed and fallback is allowed, the adapter may execute a weaker supported alternative.

Conceptually:

**Requested**

`deny_resource_writes`

↓

**requested capability unavailable**

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

The adapter records:

- requested response;
- unavailable capability or authority;
- fallback response;
- degradation;
- actual scope;
- execution result.

---

# 37. Outcome Reporting

Every response attempt should produce or contribute to:

`tf.response-outcome/v0.1`

Possible execution states include:

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
- actual response;
- fallback;
- capability context;
- scope;
- direct effects;
- side effects;
- errors;
- warnings;
- rollback state;
- execution provenance.

---

# 38. Native Success Is Not Resolution

A Windows mechanism may report successful execution.

That establishes evidence about the bounded operation.

It does not independently establish that:

- destructive transitions ceased;
- another actor did not continue the pattern;
- synchronized state did not reintroduce the condition;
- affected resources were restored;
- recovery remained intact;
- remote origin disappeared.

Therefore:

> **Execution success ≠ structural resolution.**

---

# 39. Verification

After an authorized response, the adapter should rescan the relevant observation scope where its capabilities allow.

Verification may ask:

- Are destructive resource transitions continuing?
- Is the relevant actor still producing them?
- Did another actor continue the structural pattern?
- Is affected-resource scope still expanding?
- Did the condition reappear?
- Did synchronized state reintroduce it?
- Did recovery state change?
- Are protected resources stable?
- Did the response create additional disruption?
- Can sufficient state be observed to support the intended conclusion?

Possible results include:

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

# 40. Verification Scope

Verification conclusions must remain bounded to what was actually observed.

For example:

**No further destructive transitions observed in the protected resource set**

does not imply:

**The entire Windows endpoint is clean**

unless the deployment truly provides the evidence needed for that broader claim.

Likewise:

**local actor contained**

does not imply:

**synchronized or remote origin resolved**.

---

# 41. Recovery

Windows recovery capability varies by deployment and resource.

A concrete implementation may have visibility into or support for:

- preserved originals;
- backup state;
- snapshots;
- recovery services;
- historical versions;
- synchronized recovery;
- resource restoration;
- configuration restoration;
- other explicitly configured recovery mechanisms.

The adapter must distinguish:

**recovery capability**

from:

**recovery state available**

from:

**recovery requested**

from:

**recovery attempted**

from:

**recovery completed**

from:

**restored state verified**.

---

# 42. Recovery Resources as Protected Resources

Recovery resources may themselves be important protected resources.

The detector may therefore treat adverse transitions affecting them as structurally significant.

The adapter should normalize recovery-resource activity without assuming its meaning.

For example:

**recovery resource changed**

is an observation.

Whether the transition represents:

- legitimate maintenance;
- scheduled cleanup;
- backup management;
- administrative change;
- harmful recovery interference;
- an unresolved condition

belongs to downstream analysis.

---

# 43. Synchronization

For synchronized resources, the Windows adapter should cooperate with the Cloud / Synchronization adapter.

The Windows side may establish:

> **This local process or synchronization service materialized the transition on this endpoint.**

The cloud-sync side may establish:

> **This transition originated elsewhere or propagated across an environment boundary.**

The resulting observations should be correlated without automatically becoming independent-origin evidence.

---

# 44. Network-Backed Resources

A Windows endpoint may observe transitions affecting resources whose storage authority lies elsewhere.

For such resources:

**local visibility ≠ local origin**

and:

**local access ≠ recovery authority**.

The adapter should preserve resource scope, transport relationships, environment relationships, and available recovery context.

---

# 45. Evidence Independence

Windows deployments may expose the same transition through several telemetry paths.

Those observations may corroborate that an event occurred while remaining dependent evidence about its cause.

The adapter should preserve dependency when known.

This protects downstream calculations from:

- duplicate event inflation;
- false acceleration;
- exaggerated scope;
- false corroboration.

---

# 46. Event Deduplication

A concrete adapter should have a bounded strategy for recognizing duplicate representations of the same underlying transition where sufficient evidence permits.

Candidate correlation dimensions include:

- native event identity;
- resource identity;
- actor identity;
- transition time;
- prior-state reference;
- resulting-state reference;
- correlation identifier;
- observation source.

Deduplication should preserve provenance.

It should distinguish observations, not erase them.

---

# 47. Observation Gaps

A robust Windows implementation should preserve known gaps in telemetry.

Possible reasons include:

- observer initialization;
- adapter restart;
- source disruption;
- configuration changes;
- authorization loss;
- collection failure;
- event loss;
- resource scope changes;
- unknown continuity.

The correct structural result is:

**observation gap**

not:

**no activity**.

---

# 48. Restart and Continuity

The adapter should distinguish:

- uninterrupted observation;
- resumed observation;
- known observation gap;
- baseline reset;
- unknown continuity.

This is important because downstream analysis may derive:

- rate;
- acceleration;
- persistence;
- reappearance;
- scope expansion.

A restart must not make discontinuous evidence appear continuous.

---

# 49. Temporal Ordering

Where several Windows observation sources are correlated, the adapter should preserve:

- source timestamps;
- normalization timestamps;
- event ordering information when available;
- ordering uncertainty.

The detector should not infer causal sequence solely from the order in which normalized events were received.

---

# 50. Privacy and Redaction

Windows endpoint evidence can expose highly sensitive user and system information.

The adapter should minimize what crosses into the shared analytical layer.

Preferred normalized information includes:

- privacy-preserving resource ID;
- resource type;
- resource class;
- scope;
- sensitivity;
- transition type;
- transition timing;
- actor category;
- actor relationship;
- baseline state;
- preservation state;
- recovery state;
- environment relationship;
- provenance.

Avoid exporting unnecessary:

- document contents;
- personal filenames;
- raw filesystem paths;
- plaintext credentials;
- authentication tokens;
- private keys;
- sensitive command-line content;
- unrelated registry or configuration data;
- unrelated network data;
- unrelated account information.

---

# 51. Credential Boundary

The shared detector does not require Windows authentication secrets.

The adapter must not emit:

- passwords;
- access tokens;
- refresh tokens;
- session secrets;
- private keys;
- recovery secrets;
- unrelated credentials.

Where structural identity context is required, use a bounded reference rather than the authentication material itself.

---

# 52. Local Processing Preference

Sensitive Windows-native operations should remain local when normalized structure is sufficient.

Candidate local operations include:

- native-event handling;
- filesystem-path handling;
- actor correlation;
- resource classification;
- identifier pseudonymization;
- baseline comparison;
- telemetry deduplication;
- state comparison;
- redaction;
- mapping native operations into shared transitions.

The detector should receive evidence sufficient for structural reasoning rather than a wholesale copy of endpoint telemetry.

---

# 53. Known Limitations

Concrete Windows adapters should document implementation-specific limitations such as:

- incomplete filesystem scope;
- incomplete telemetry sources;
- event loss;
- insufficient privilege;
- incomplete actor identity;
- incomplete process lineage;
- remote-resource ambiguity;
- synchronization ambiguity;
- incomplete network context;
- incomplete recovery visibility;
- unsupported enforcement actions;
- authorization restrictions;
- inability to observe post-response state;
- incomplete cross-environment verification.

These limitations are analytical evidence.

They should not be hidden.

---

# 54. Capability Posture

The generic Windows adapter begins from:

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
| Resource restore | `unknown` |
| Configuration restore | `unknown` |
| Post-action observation | `unknown` |
| State comparison | `unknown` |
| Persistence detection | `unknown` |
| Reappearance detection | `unknown` |
| Recovery verification | `unknown` |

This does not mean Windows lacks these capabilities.

It means the generic specification does not claim that a particular Windows adapter possesses them.

A concrete deployment replaces `unknown` with evidence-backed declarations.

---

# 55. Why the Generic Posture Is Unknown

A Windows platform feature establishes only that a mechanism exists somewhere in the platform architecture.

It does not establish that:

- this adapter implements it;
- the implementation is appropriately configured;
- the implementation has the required authority;
- the relevant resource lies within scope;
- the mechanism applies to the requested action;
- the current deployment exposes the necessary evidence.

Therefore:

> **Capability is established by the deployed adapter, not inferred from the operating-system name.**

---

# 56. Windows Adapter Invariants

## WINDOWS-INV-01 — Platform Capability ≠ Adapter Capability

The existence of a Windows mechanism does not establish that a concrete adapter implements or can use it.

## WINDOWS-INV-02 — Observation Boundary ≠ Endpoint Boundary

A bounded observer must not imply endpoint-wide visibility.

## WINDOWS-INV-03 — Native Event ≠ Domain Verdict

A Windows event is evidence, not a ransomware conclusion.

## WINDOWS-INV-04 — Actor Identity ≠ Intent

A process, application, service, script, system component, account, or user identity does not establish motive.

## WINDOWS-INV-05 — Trusted Actor ≠ Safe Transition

Known or trusted identity context must not suppress contradictory destructive behavior.

## WINDOWS-INV-06 — Actor ≠ Origin

A locally visible actor may transport or materialize a transition originating elsewhere.

## WINDOWS-INV-07 — Multiple Sources ≠ Independent Transitions

Several Windows telemetry sources may describe the same underlying resource transition.

## WINDOWS-INV-08 — Recovery Event ≠ Ransomware

A transition affecting recovery state does not independently establish ransomware.

## WINDOWS-INV-09 — Privilege ≠ Authority

Technical privilege does not provide policy authorization for containment.

## WINDOWS-INV-10 — Capability ≠ Authority

A supported platform action must still be separately authorized.

## WINDOWS-INV-11 — Intervention Opportunity ≠ Containment Decision

The ability to intercept an operation does not itself establish that the operation should be denied.

## WINDOWS-INV-12 — Requested Response ≠ Executed Response

Blocked, unsupported, partial, failed, and fallback outcomes remain explicit.

## WINDOWS-INV-13 — Execution ≠ Resolution

A successful Windows response does not prove that the destructive structural pattern has resolved.

## WINDOWS-INV-14 — Local Containment ≠ Remote Containment

Local intervention does not establish that synchronized or remote destructive state is resolved.

## WINDOWS-INV-15 — Recovery Capability ≠ Verified Restoration

Availability of a recovery mechanism does not establish successful restoration.

## WINDOWS-INV-16 — Observation Gap ≠ No Activity

Unavailable telemetry cannot be treated as evidence that no transition occurred.

## WINDOWS-INV-17 — Privacy Survives Normalization

Raw content, paths, credentials, and unrelated endpoint telemetry should remain local when structural references are sufficient.

## WINDOWS-INV-18 — Provenance Survives Correlation

Multi-source correlation must retain enough lineage to reconstruct the observations used to produce the shared event.

---

# 57. Non-Goals

The Windows adapter is not:

- a malware-signature engine;
- a ransomware classifier;
- an attribution system;
- a universal EDR implementation;
- a guarantee of endpoint-wide visibility;
- a guarantee of process attribution;
- a guarantee of write containment;
- a guarantee of network isolation;
- a guarantee of recovery;
- an authorization engine;
- a mechanism for bypassing Windows security controls;
- a justification for centralizing raw endpoint telemetry.

Its role is narrower:

> **Observe authorized Windows structural evidence, normalize it faithfully, declare actual capabilities and limitations, map separately authorized responses onto supported mechanisms, record what really happened, and support bounded verification.**

---

# 58. Shared Contracts

The Windows adapter participates in:

- `tf.resource-transition/v0.1`
- `tf.platform-capabilities/v0.1`
- `tf.containment-decision/v0.1`
- `tf.response-outcome/v0.1`
- `tf.verification/v0.1`

The Ransomware Structural Pattern Detector consumes its normalized observations and may produce:

- `tf.structural-pattern/v0.1`

The Windows adapter does not redefine those contracts.

---

# 59. Relationship to Cloud / Synchronization

For synchronized resources, the Windows adapter should cooperate with the Cloud / Synchronization adapter.

Conceptually:

**Windows-local observation**

↓

**local normalized transition**

↕ correlation

**cloud / synchronization observation**

↓

**cross-environment lineage**

The Windows adapter may establish where a transition became visible locally.

The cloud-sync adapter may contribute evidence about origin, transport, replication, or propagation.

Neither layer should invent evidence the other does not possess.

---

# 60. Relationship to Other Platform Adapters

The Windows, macOS, Linux, Android, iOS/iPadOS, and Cloud / Synchronization adapters all share the same structural grammar.

Their capabilities are intentionally not assumed to be equal.

This is the key portability rule:

> **Standardize semantics without pretending mechanisms are identical.**

A `tf.resource-transition/v0.1` object should remain structurally intelligible regardless of whether its observation originated from Windows, Linux, macOS, Android, iOS/iPadOS, or a synchronization environment.

---

# Canonical Summary

> **The Windows adapter maps authorized Windows resource, actor, recovery, and system observations into the Shared Structural Event Grammar while preserving the distinction between platform capability, adapter capability, response authority, actual execution, and verified resulting state.**

Its platform rule is:

> **Windows may provide the mechanism. The deployed adapter must prove that it possesses the capability.**

Its observation rule is:

> **Normalize what the configured observer actually saw and retain enough provenance to reconstruct how it was observed.**

Its filesystem rule is:

> **An opportunity to observe or intercept a resource operation remains distinct from the structural decision to contain it.**

Its actor rule is:

> **A known process can behave anomalously, and a locally visible process may not be the ultimate origin.**

Its recovery rule is:

> **Recovery-state changes are evidence to correlate, not automatic ransomware verdicts.**

Its authority rule is:

> **Privilege and technical capability do not grant permission to act.**

Its response rule is:

> **Record the exact response and scope that actually executed, including partial and fallback behavior.**

Its continuity rule is:

> **Telemetry gaps remain gaps rather than becoming evidence of inactivity.**

Its privacy rule is:

> **Keep raw endpoint detail local when privacy-preserving structural evidence is sufficient.**

Its verification rule is:

> **A blocked operation or contained actor is evidence of intervention, not proof that the overall destructive condition has resolved.**
