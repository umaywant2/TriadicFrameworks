# Linux Adapter

> **Platform adapter specification for mapping authorized Linux observations and response capabilities into the Ransomware Structural Pattern Detector while preserving distribution, filesystem, namespace, privilege, and deployment boundaries.**

The Linux adapter connects Linux-observable resource transitions to the platform-neutral Shared Structural Event Grammar.

Linux must not be treated as one uniform deployment environment.

A concrete adapter may operate on:

- a personal workstation;
- a server;
- a virtual machine;
- a container host;
- a containerized workload;
- a development system;
- a storage server;
- a cloud-hosted Linux instance;
- another specialized Linux environment.

Observation and enforcement capabilities may vary substantially among those deployments.

The governing rule is:

> **Declare the capabilities of the deployed Linux adapter, not the theoretical capabilities of Linux as a whole.**

---

## Status

- **Adapter ID:** `rspd-linux`
- **Platform:** Linux
- **Status:** Experimental
- **Role:** Observation, normalization, capability declaration, bounded response mapping, and verification support
- **Normalized observation:** `tf.resource-transition/v0.1`
- **Capability declaration:** `tf.platform-capabilities/v0.1`
- **Decision input:** `tf.containment-decision/v0.1`
- **Execution output:** `tf.response-outcome/v0.1`
- **Verification output:** `tf.verification/v0.1`

---

# 1. Scope

The Linux adapter operates within explicitly configured filesystem, process, account, namespace, network, storage, and privilege boundaries.

Its potential observation scope may include:

- selected files;
- selected directories;
- user home resources;
- mounted filesystems;
- application data;
- configuration;
- databases;
- archives;
- project files;
- backup resources;
- recovery resources;
- shared storage;
- mounted network resources;
- synchronized resources;
- container-visible resources;
- host-visible container storage;
- adapter-controlled canaries;
- other explicitly configured Linux resources.

An implementation must state its actual observation boundary.

It must not infer machine-wide visibility merely because it runs on Linux.

---

# 2. Deployment Variability

The Linux adapter specification describes an architectural class rather than one implementation.

Capability can depend upon:

- kernel facilities available to the implementation;
- granted privileges;
- filesystem characteristics;
- mount topology;
- namespace boundaries;
- containerization;
- storage architecture;
- application configuration;
- security policy;
- network topology;
- user authorization;
- deployment-specific observation sources.

A feature available in one Linux environment is not automatically available in another.

Therefore:

> **Linux platform capability must be discovered or configured, then declared. It must not be assumed.**

---

# 3. Observation Model

A Linux implementation may use one or more authorized observation mechanisms.

At the structural level, the adapter requires only that the implementation be able to identify and preserve the provenance of relevant observations.

Conceptually:

**Linux observation source**

↓

**Adapter-local interpretation**

↓

**Normalization**

↓

**`tf.resource-transition/v0.1`**

↓

**Ransomware Structural Pattern Detector**

The adapter must preserve which source produced the observation.

Multiple Linux observation sources describing the same transition must not automatically become independent evidence.

---

# 4. Filesystem Event Observation

A Linux implementation may receive event-driven observations about resource activity where the deployed environment supports them.

Candidate observation classes include:

- creation;
- modification;
- deletion;
- rename;
- move;
- access;
- open or close activity where observable;
- metadata change;
- permission change;
- execution-related resource activity where observable.

The concrete implementation determines which events are actually available.

A normalized event must not claim observations that its native source did not provide.

---

# 5. `inotify` Observation Profile

A Linux implementation may use `inotify`-based observation for explicitly watched filesystem resources.

At the adapter level, this profile should be understood as a **bounded watch-based observation source**.

Its structural use may include observing transitions such as:

- create;
- modify;
- delete;
- move;
- related filesystem changes exposed by the implementation.

An `inotify` observation should retain enough provenance to establish which watch or configured observation surface produced it.

The adapter must not turn:

**not observed by the configured watches**

into:

**did not occur elsewhere**.

---

# 6. `fanotify` Observation Profile

A Linux implementation may use `fanotify` where supported and appropriately authorized.

At the structural level, a `fanotify`-based implementation may provide a different observation scope from a watch-oriented implementation and may support access-control behavior in appropriate configurations.

This does not make `fanotify` support universal.

A concrete adapter must declare:

- whether the facility is available;
- what scope is actually monitored;
- what event classes are available;
- what actor information is available;
- whether permission-related control is available;
- what privilege is required;
- what limitations remain.

The shared detector sees normalized capability, not an assumption about the underlying Linux interface.

---

# 7. Multiple Observation Sources

A stronger Linux implementation may combine multiple observation sources.

Conceptually:

**Filesystem observation**

+

**actor/process evidence**

+

**baseline state**

+

**recovery state**

↓

**normalized structural events**

This may improve lineage or contextual information.

However:

> **Multiple telemetry sources ≠ multiple independent transitions**

If two observation mechanisms describe the same underlying resource transition, their relationship should remain visible.

The adapter should preserve corroborating provenance without inflating event counts.

---

# 8. Native Observation Preservation

Where feasible and authorized, the adapter should retain a local reference to the native evidence used during normalization.

Relevant provenance may include:

- observation source;
- platform environment;
- adapter identity;
- adapter version;
- observation time;
- normalization time;
- native-event reference;
- relevant capability declaration;
- derivation references;
- redaction classes.

Raw native evidence may remain local.

The detector requires structural lineage, not unrestricted Linux telemetry.

---

# 9. Resource Mapping

Linux resources should map into shared structural categories according to their role.

Candidate mappings include:

| Linux-visible resource | Shared resource type/class |
|---|---|
| User document | `file` / `user_document` |
| Photo | `file` / `photo` |
| Video | `file` / `video` |
| Audio | `file` / `audio` |
| Database | `file` or `dataset` / `database` |
| Archive | `file` / `archive` |
| Source/project resource | `file` / `project_file` |
| Application data | `file` or `dataset` / `application_data` |
| Configuration | `configuration` / `configuration` |
| Credential-related store | appropriate type / `credential_store` |
| Backup | appropriate type / `backup` |
| Recovery resource | appropriate type / `recovery_resource` |
| Mounted network resource | appropriate type / `network_resource` |
| Cloud-backed resource | appropriate type / `cloud_resource` |
| Temporary resource | appropriate type / `temporary` |
| Canary | appropriate type / `canary` |
| Other domain resource | appropriate type / `domain_defined` |

The adapter should classify structure without unnecessarily exposing private resource names or contents.

---

# 10. Resource Identity

Linux filesystem paths can expose substantial user and system information.

The central detector does not inherently require raw absolute paths.

A concrete adapter should prefer a stable privacy-preserving resource reference when that is sufficient for correlation.

The adapter may retain native paths locally for:

- correlation;
- enforcement;
- verification;
- recovery;
- authorized investigation.

The shared event may instead expose:

- structural resource ID;
- type;
- class;
- scope;
- sensitivity;
- protection state;
- canary state;
- recoverability;
- bounded location reference when necessary.

---

# 11. Mount Boundaries

Linux resource topology may span multiple filesystems and mounts.

The adapter should preserve the observation boundary represented by its configured sources.

For each relevant resource, the implementation may need to distinguish structurally among:

- locally hosted resources;
- separately mounted resources;
- network-backed resources;
- synchronized resources;
- other deployment-specific storage boundaries.

A detector must not assume that an event stream covering one observation boundary covers every mounted resource visible elsewhere in the environment.

---

# 12. Actor Mapping

Candidate Linux actors include:

- `process`
- `application`
- `service`
- `script`
- `container`
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

Actor identity should reflect actual evidence.

If the observation source does not reliably establish an actor, the adapter should not invent one.

---

# 13. Process Lineage

Where the concrete observation environment exposes reliable process relationships, the adapter may preserve actor lineage.

Conceptually:

**Parent actor**

↓

**Child actor**

↓

**resource transition**

Such lineage can materially improve structural interpretation.

It may help distinguish an established application workflow from unexpected behavior originating deeper in an invocation chain.

Process lineage still does not establish malicious intent.

---

# 14. User and Service Context

A Linux transition may occur under:

- an interactive user context;
- a service context;
- an automated job;
- an application context;
- a remote session;
- a containerized workload;
- another system context.

Where observable and relevant, those relationships may be represented through actor and context references.

The detector may use them when evaluating actor-role coherence.

The adapter must not infer human intent solely from the account under which an operation occurred.

> **Execution identity ≠ human intent**

---

# 15. Origin vs. Transport

Network storage, synchronization, containerization, and remote services can separate the locally visible actor from the originating actor.

A local process may:

- originate a transition;
- transport a remote transition;
- materialize synchronized state;
- execute on behalf of another service;
- reflect a change produced in another namespace or environment.

Where sufficient evidence exists, the adapter should preserve:

- origin actor;
- transport actor;
- origin environment;
- local observer;
- propagation context.

Where origin cannot be established, it remains unresolved.

---

# 16. Transition Mapping

Relevant Linux operations may map into shared operations such as:

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

Corresponding structural actions may include:

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

The adapter should preserve a native operation name when the shared mapping would otherwise lose useful lineage.

---

# 17. Transition Characteristics

Where directly observable or explicitly derived, a Linux implementation may normalize characteristics such as:

- size change;
- content-change indication;
- structural change;
- representation or extension change;
- ownership change;
- permission change;
- scope change;
- recovery-state change;
- prior-state preservation;
- recoverability;
- repeated mutation;
- transition timing.

These characteristics provide evidence for later structural analysis.

They do not independently constitute a ransomware verdict.

---

# 18. Baseline Support

A Linux implementation may maintain structural baselines within its authorized scope.

Candidate dimensions include:

- known actors;
- expected actor roles;
- typical operations;
- normal resource classes;
- ordinary scope;
- transition frequency;
- established services;
- expected batch workflows;
- normal backup activity;
- ordinary synchronization behavior.

A baseline improves context.

It does not create permanent trust.

A historically benign actor may produce anomalous current behavior.

Likewise, an unfamiliar actor is not automatically hostile.

---

# 19. Bulk Operations

Linux systems commonly perform legitimate high-volume resource operations.

Potential competing explanations may include:

- backups;
- restores;
- builds;
- package operations;
- deployments;
- database maintenance;
- migrations;
- media conversion;
- synchronization;
- archival operations;
- administrative batch jobs.

The adapter should preserve evidence supporting these contexts when observable.

The detector remains responsible for determining whether current transitions remain coherent with the expected workflow.

---

# 20. Canary Resources

A concrete implementation may use adapter-controlled canary resources where appropriate and authorized.

A canary transition can provide strong evidence that unexpected mutation reached a monitored resource.

It does not independently establish:

- ransomware;
- intent;
- attribution;
- scope outside the observed resource boundary.

Canaries should contain no sensitive user information.

Their placement and visibility should remain part of adapter-local configuration.

---

# 21. Containers and Namespaces

Containerized Linux environments require explicit boundary handling.

A transition may be visible:

- inside a container;
- from the host;
- through a mounted volume;
- through shared storage;
- through more than one observation source.

The adapter should preserve enough context to distinguish:

- host environment;
- container environment;
- resource ownership boundary;
- actor environment;
- shared resource relationship.

It must not double-count one underlying transition solely because both a container-side and host-side observer report it.

---

# 22. Container Actor Semantics

A process observed within a container may be represented as a `process`, while the containing workload or execution boundary may also be relevant.

Where evidence allows, the adapter may preserve:

- process actor;
- parent actor;
- container reference;
- host reference;
- account or identity context;
- resource relation.

The detector should then reason over the structural lineage rather than flattening the container boundary.

---

# 23. Network-Backed Resources

A Linux system may expose resources backed by another environment.

For such resources:

**local filesystem visibility**

does not necessarily imply:

**local resource origin**

or:

**local recovery authority**.

Where network-backed storage is observable, the adapter should retain:

- resource scope;
- relevant remote/environment reference;
- local actor;
- transport relationship;
- available recovery state;
- authority limitations.

Cross-environment reasoning may then be correlated with the Cloud / Synchronization adapter where appropriate.

---

# 24. Capability Declaration

Every concrete Linux adapter should provide:

`tf.platform-capabilities/v0.1`

The capability declaration must describe the implementation that is actually running.

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

# 25. Capability Profiles

A Linux adapter may expose different capability profiles according to deployment.

For example:

## Bounded User-Space Observer

A narrowly authorized adapter monitoring selected resources may possess useful observation capability but limited enforcement authority.

## Privileged Host Observer

An appropriately authorized host-level implementation may have broader observation and response capabilities.

## Container-Scoped Observer

An adapter operating inside a container may have useful workload visibility while lacking host-wide context.

## Host-Side Container Observer

An implementation running on the host may observe resources used by containers while requiring separate correlation to establish workload-level actor semantics.

These are architectural profiles, not fixed product definitions.

A concrete implementation declares its actual capabilities.

---

# 26. Capability Is Not Authority

Linux may provide a mechanism capable of a powerful response.

That does not authorize its use.

Therefore:

> **Privilege ≠ Authority**

and:

> **Capability ≠ Authority**

The adapter must separately establish:

1. that a mechanism is technically available;
2. that the requested operation is inside the adapter's authority;
3. that the specific containment decision permits execution;
4. that relevant constraints are satisfied.

---

# 27. Containment Mapping

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

A concrete Linux adapter maps these structural requests onto supported mechanisms.

The shared specification does not mandate one native implementation.

---

# 28. Write Containment

Where a deployment supplies an authorized mechanism capable of restricting relevant resource writes, the adapter may map:

`deny_resource_writes`

onto that mechanism.

The outcome must preserve:

- target;
- scope;
- requested response;
- actual response;
- whether execution was attempted;
- actual execution status;
- relevant capability;
- errors or limitations.

A write restriction affecting one filesystem, mount, resource set, or actor must not be represented as broader containment than actually occurred.

---

# 29. Actor Containment

Where supported and authorized, a Linux adapter may attempt to contain an actor associated with destructive transitions.

The adapter must preserve the actual containment scope.

For example, containment of:

- one process;
- a process group;
- a service;
- a container;
- another bounded execution context

must not silently become a claim that every related actor or remote origin was contained.

The exact native mechanism remains implementation-specific.

---

# 30. Resource Isolation

Resource isolation may be available in some deployments.

The adapter should record:

- which resource or resource set was affected;
- which access boundary changed;
- whether the action was reversible;
- whether rollback is available;
- whether the intended scope was achieved.

Resource isolation is not automatically actor containment.

Likewise, actor containment is not automatically resource recovery.

---

# 31. Network Isolation

Some deployments may provide a mechanism for restricting relevant network communication.

Where used, the adapter must preserve its actual boundary.

Network isolation may apply to:

- an actor;
- workload;
- service;
- container;
- host;
- network context;
- another supported scope.

It must not be represented as universal network isolation unless that is what actually occurred.

---

# 32. Fallback

If the preferred response is unavailable and the containment decision permits fallback, the adapter may select a weaker supported response.

Conceptually:

**Requested**

`deny_resource_writes`

↓

**required capability unavailable**

↓

**Fallback**

`contain_actor`

or:

**Requested**

`contain_actor`

↓

**authority unavailable**

↓

**Fallback**

`notify_authorized_operator`

The exact fallback must be policy-driven.

The adapter records:

- requested response;
- unavailable capability or authority;
- fallback response;
- degradation state;
- actual execution result.

---

# 33. Outcome Reporting

Every response attempt should produce or contribute to:

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
- actual executed response;
- fallback;
- capability context;
- direct effects;
- side effects;
- errors;
- warnings;
- rollback state;
- execution provenance.

---

# 34. Execution Is Not Verification

A Linux system call, service operation, policy change, or other mechanism may report successful execution while the larger destructive condition persists.

Therefore:

> **Native success ≠ structural resolution**

The adapter reports execution truth first.

A new observation cycle determines resulting state.

---

# 35. Verification

Post-response verification should rescan the bounded environment using available observation capabilities.

Relevant questions include:

- Are destructive transitions still occurring?
- Is the associated actor still producing them?
- Did another actor continue the pattern?
- Did resource scope continue expanding?
- Did activity cross another mount, namespace, device, or synchronized boundary?
- Did the condition reappear?
- Did recovery state change?
- Are protected resources stable?
- Did containment introduce significant side effects?

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

# 36. Verification Scope

A verification claim must be bounded to what was actually observed.

For example:

**No further destructive transition observed in the protected home-directory scope**

does not imply:

**No destructive activity exists elsewhere on the host**

Similarly:

**Host process stopped**

does not imply:

**Remote origin resolved**

The verification object should preserve scope and limitations.

---

# 37. Recovery

Linux recovery mechanisms vary widely by deployment and storage architecture.

A concrete adapter may be able to observe or interact with:

- preserved originals;
- backup state;
- snapshots;
- versioned resources;
- recovery stores;
- provider-backed recovery;
- other configured recovery mechanisms.

The adapter should distinguish:

**recovery mechanism available**

from:

**usable recovery state observed**

from:

**recovery attempted**

from:

**recovery completed**

from:

**restored state verified**

These stages must remain separate.

---

# 38. Backup Coherence

Backup activity is structurally significant in two different directions.

First, legitimate backup operation may explain broad resource access or transition patterns.

Second, damage to backup or recovery resources may strengthen a destructive-pattern assessment.

Therefore, backup evidence may appear as:

- competing explanation;
- counter-evidence;
- affected resource;
- recovery capability;
- recovery impact.

Its meaning depends on the structural context.

---

# 39. Privacy and Redaction

Linux telemetry can expose sensitive detail.

The adapter should minimize what leaves the local environment.

Preferred normalized information includes:

- privacy-preserving resource ID;
- resource type;
- resource class;
- structural scope;
- sensitivity;
- transition type;
- transition timing;
- actor class;
- actor relationship;
- baseline state;
- preservation state;
- recovery state;
- environment relationship;
- provenance.

Avoid exporting unnecessary:

- document contents;
- plaintext credentials;
- personal filenames;
- raw absolute paths;
- process arguments containing sensitive data;
- environment secrets;
- authentication material;
- unrelated account information;
- unrelated network data.

---

# 40. Credential Boundary

The shared detector does not require Linux authentication material.

The adapter must not emit:

- plaintext passwords;
- private keys;
- session secrets;
- authentication tokens;
- cloud credentials;
- recovery secrets;
- unrelated environment secrets.

A structural reference to an account or authority context is preferable when identity context is required.

---

# 41. Local Processing Preference

Sensitive platform-native operations should remain local when the detector needs only their normalized structural result.

Candidate local operations include:

- native-event processing;
- resource classification;
- path handling;
- identifier pseudonymization;
- actor correlation;
- baseline comparison;
- telemetry deduplication;
- redaction;
- mapping native events into shared transitions.

The central detector should receive structural evidence rather than an unnecessarily complete replica of Linux telemetry.

---

# 42. Event Loss and Observation Gaps

A robust Linux adapter must account for the possibility that its observation stream is incomplete.

If an implementation detects:

- an event-stream gap;
- an overflow condition;
- lost telemetry;
- delayed collection;
- incomplete initialization;
- unknown observation coverage;

that limitation should be preserved.

Subsequent absence of events must not be interpreted as proof that no transitions occurred during the gap.

---

# 43. Restart and Continuity

If the adapter restarts, it should preserve enough state to distinguish:

- continuous observation;
- resumed observation;
- a known observation gap;
- baseline reset;
- unknown continuity.

A restarted observer should not silently imply uninterrupted evidence.

This is particularly important when rate, acceleration, or persistence are derived from event history.

---

# 44. Temporal Ordering

Where multiple Linux observation sources are correlated, their ordering may require normalization.

The adapter should preserve:

- source timestamps;
- normalization timestamps;
- sequence information when available;
- uncertainty where precise ordering cannot be established.

The detector should not infer causal order solely from normalized arrival order when the original timing evidence does not establish it.

---

# 45. Known Limitations

Concrete Linux adapters should explicitly document implementation-specific limitations such as:

- watch coverage;
- mount coverage;
- missing event classes;
- insufficient privilege;
- incomplete actor identity;
- incomplete process lineage;
- namespace visibility;
- container boundaries;
- network-storage ambiguity;
- synchronization ambiguity;
- event loss;
- recovery-state limitations;
- unsupported enforcement mechanisms;
- authorization restrictions;
- incomplete verification.

These limitations are analytical evidence.

They should not be hidden.

---

# 46. Capability Posture

The generic Linux adapter begins from:

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
| Post-action observation | `unknown` |
| State comparison | `unknown` |
| Persistence detection | `unknown` |
| Reappearance detection | `unknown` |
| Recovery verification | `unknown` |

This does **not** mean Linux lacks these capabilities.

It means this generic specification does not claim that any particular implementation possesses them.

A concrete deployment replaces `unknown` with an evidence-backed declaration.

---

# 47. Why the Generic Posture Is Unknown

Linux provides a broad implementation space.

An architectural specification cannot safely infer the capabilities of:

- a user-space process;
- a privileged daemon;
- a container;
- a host-side agent;
- a constrained appliance;
- a server deployment;
- a workstation deployment;

from the word **Linux** alone.

Therefore:

> **Capability follows implementation and authority, not platform name.**

---

# 48. Linux Adapter Invariants

## LINUX-INV-01 — Linux ≠ One Capability Profile

Different deployments may expose materially different observation and enforcement capabilities.

## LINUX-INV-02 — Observation Boundary ≠ Host Boundary

A configured observer may see only part of the resources visible on the system.

## LINUX-INV-03 — Native Event ≠ Domain Verdict

A filesystem or actor event does not independently establish ransomware.

## LINUX-INV-04 — Actor Identity ≠ Intent

A process, service, script, container, or user identity does not establish motive.

## LINUX-INV-05 — Actor ≠ Origin

The locally visible actor may transport or materialize a change originating elsewhere.

## LINUX-INV-06 — Multiple Telemetry Sources ≠ Independent Events

Several observers may report the same underlying resource transition.

## LINUX-INV-07 — Container Observation ≠ Host-Wide Observation

Visibility inside a namespace or container must not be generalized to the rest of the host.

## LINUX-INV-08 — Privilege ≠ Authority

The technical ability to perform a privileged response does not authorize its use.

## LINUX-INV-09 — Capability ≠ Authority

Declared platform support and response authorization are separate structural facts.

## LINUX-INV-10 — Requested Response ≠ Executed Response

Unsupported, blocked, partial, and fallback outcomes remain explicit.

## LINUX-INV-11 — Execution ≠ Resolution

A successfully executed Linux mechanism does not prove that destructive activity has ended.

## LINUX-INV-12 — Local Containment ≠ Remote Containment

Stopping a local actor does not establish that a remote or synchronized origin has been resolved.

## LINUX-INV-13 — Recovery Capability ≠ Verified Restoration

Availability of backups, snapshots, or other recovery mechanisms does not establish successful restoration.

## LINUX-INV-14 — Observation Gap ≠ No Activity

Missing telemetry cannot be interpreted as evidence that no transition occurred.

## LINUX-INV-15 — Raw Path ≠ Required Shared Identity

Sensitive filesystem paths should remain local when a privacy-preserving structural reference is sufficient.

## LINUX-INV-16 — Provenance Survives Normalization

Enough lineage must remain to reconstruct the origin and limitations of each normalized observation.

---

# 49. Non-Goals

The Linux adapter is not:

- a universal Linux endpoint product;
- a malware-signature scanner;
- a ransomware classifier;
- an attribution engine;
- a guarantee of filesystem-wide visibility;
- a guarantee of process attribution;
- a guarantee of host-wide containment;
- a guarantee of network isolation;
- a guarantee of recovery;
- a mechanism for obtaining unauthorized privilege;
- a justification for bypassing Linux security controls;
- an authorization engine.

Its role is narrower:

> **Observe the authorized Linux environment, normalize structural transitions, preserve actor and resource lineage, declare capabilities honestly, map authorized responses onto supported mechanisms, record actual outcomes, and support bounded verification.**

---

# 50. Shared Contracts

The Linux adapter participates in:

- `tf.resource-transition/v0.1`
- `tf.platform-capabilities/v0.1`
- `tf.containment-decision/v0.1`
- `tf.response-outcome/v0.1`
- `tf.verification/v0.1`

The Ransomware Structural Pattern Detector consumes its normalized observations and may produce:

- `tf.structural-pattern/v0.1`

The Linux adapter does not redefine those contracts.

---

# 51. Relationship to Cloud / Synchronization

For synchronized or remotely backed resources, the Linux adapter should cooperate with the Cloud / Synchronization adapter.

The Linux side may establish:

> **This local actor performed or materialized this resource transition.**

The cloud-sync side may establish:

> **This transition originated elsewhere or propagated across a synchronization boundary.**

Those observations can be correlated while preserving their dependency.

Neither should be forced to answer questions outside its available evidence.

---

# 52. Relationship to Container Environments

A Linux host may contain several distinct execution boundaries.

The adapter should preserve those boundaries rather than flattening them into a single actor space.

Conceptually:

**Host**

↓

**container / workload boundary**

↓

**actor**

↓

**resource transition**

A host observation and a workload observation may describe the same event from different structural positions.

The detector should be able to correlate them without automatically treating them as independent evidence.

---

# Canonical Summary

> **The Linux adapter maps authorized Linux resource and actor observations into the Shared Structural Event Grammar while preserving deployment, privilege, mount, namespace, container, remote-resource, and observation boundaries.**

Its platform rule is:

> **Linux describes the environment family. The concrete adapter declaration describes the capability.**

Its observation rule is:

> **An observation source establishes only what that source actually exposed within its configured scope.**

Its actor rule is:

> **A process identity may establish where a transition became observable without establishing intent or ultimate origin.**

Its container rule is:

> **Host and container observations may describe the same structural event from different boundaries. Preserve that relationship rather than double-counting it.**

Its authority rule is:

> **Privilege is a capability condition, not permission to act.**

Its response rule is:

> **Execute only supported, authorized, bounded responses and record the exact scope that actually changed.**

Its continuity rule is:

> **An observation gap remains a gap. Silence during that interval is not evidence of safety.**

Its privacy rule is:

> **Normalize structural identity before exporting raw paths, content, credentials, or unrelated telemetry.**

Its verification rule is:

> **Verify the resulting state across the scope actually observed. Do not promote bounded containment into a host-wide or cross-environment resolution claim.**
