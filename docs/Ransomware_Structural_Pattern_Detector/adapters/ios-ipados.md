<img width="1194" height="672" alt="Ransomware_Structural_Pattern_Detector_adapters_ios_ipados_" src="https://github.com/user-attachments/assets/058cbdc2-fbb4-421e-9fba-5974b56f61d2" />

# iOS / iPadOS Adapter

> **Platform adapter specification for mapping authorized iOS and iPadOS observations into the Ransomware Structural Pattern Detector while preserving Apple's application, data-access, and platform-security boundaries.**

The iOS / iPadOS adapter connects resource observations available within an authorized application context to the platform-neutral Shared Structural Event Grammar.

This adapter is intentionally **capability-conservative**.

It must not assume desktop-style filesystem monitoring, unrestricted observation of other applications, arbitrary process inspection, system-wide actor containment, or universal access to user resources.

Its governing rule is:

> **Represent only what the authorized iOS or iPadOS environment can actually expose. Restricted visibility is a structural limitation, not evidence that destructive activity is absent.**

---

## Status

- **Adapter ID:** `rspd-ios-ipados`
- **Platforms:** iOS, iPadOS
- **Status:** Experimental
- **Role:** Authorized observation, normalization, capability declaration, bounded response mapping, and verification support
- **Normalized observation:** `tf.resource-transition/v0.1`
- **Capability declaration:** `tf.platform-capabilities/v0.1`
- **Decision input:** `tf.containment-decision/v0.1`
- **Execution output:** `tf.response-outcome/v0.1`
- **Verification output:** `tf.verification/v0.1`

---

# 1. Scope

The iOS / iPadOS adapter operates entirely within the data-access, application, authorization, and service boundaries available to its implementation.

Its potential observation scope may include:

- adapter-owned resources;
- resources explicitly made available to the adapter;
- user-selected resources;
- application-visible metadata;
- resources returned by authorized platform interfaces;
- adapter-generated test or canary resources where appropriate;
- user-supplied evidence;
- authorized cloud or synchronization state exposed through another integration;
- adapter-maintained structural baselines.

The precise scope depends on the implementation and authority available during execution.

The adapter must describe its actual observation surface rather than imply device-wide visibility.

---

# 2. Platform Security Boundary

iOS and iPadOS enforce platform security boundaries intended to constrain applications and mediate access to user data.

The adapter treats those boundaries as part of its architecture.

Conceptually:

**Platform security boundary**

↓

**Authorized application surface**

↓

**iOS / iPadOS adapter**

↓

**Normalized resource transition**

The adapter must not attempt to weaken platform security controls in order to obtain broader observation or enforcement capability.

If the operating environment does not expose a required observation, the corresponding structural state remains unresolved.

---

# 3. Detection Model

The iOS / iPadOS adapter is **not** a device-wide ransomware scanner.

It provides bounded structural evidence from surfaces available to the adapter.

Its role is:

**Observe**

↓

**Normalize**

↓

**Preserve lineage**

↓

**Declare limitations**

↓

**Emit structural events**

The Ransomware Structural Pattern Detector evaluates those events together with any other authorized evidence.

This distinction is fundamental:

> **Limited platform visibility can support bounded detection, but it cannot support claims about unobserved device-wide state.**

---

# 4. Observation Sources

A concrete implementation may normalize authorized observations from sources such as:

- adapter-owned resource operations;
- application-visible file or document state;
- user-selected resources;
- resource metadata exposed to the application;
- explicit application events;
- user-supplied observations;
- synchronization state exposed through an authorized integration;
- locally maintained baseline observations;
- post-response resource state visible to the adapter.

Every normalized event should identify the source from which its evidence originated.

The adapter must not imply visibility into another application or system surface unless the implementation actually possesses that visibility.

---

# 5. Observation Limitations

The adapter should assume that important state may remain outside its visibility.

Potentially unresolved information may include:

- resource transitions occurring exclusively within another application's protected environment;
- device-wide resource-transition history;
- complete actor lineage;
- full system process activity;
- origin of remotely synchronized transitions;
- resources never made available to the adapter;
- historical transitions that occurred before observation began;
- provider-internal operations;
- recovery state unavailable through the current resource interface;
- device-wide post-response state.

These limitations must survive normalization.

The correct representation is often:

**unknown**

rather than:

**false**

and never automatically:

**safe**.

---

# 6. Resource Mapping

Resources visible to the adapter should map into the shared vocabulary by structural role.

Candidate mappings include:

| Visible resource | Shared resource type/class |
|---|---|
| User document | `file` / `user_document` |
| Photo | `file` / `photo` |
| Video | `file` / `video` |
| Audio | `file` / `audio` |
| Database | `dataset` / `database` |
| Archive | `file` / `archive` |
| Project resource | `file` / `project_file` |
| Application-owned data | `file` or `dataset` / `application_data` |
| Configuration | `configuration` / `configuration` |
| Backup-visible resource | appropriate type / `backup` |
| Recovery-visible resource | appropriate type / `recovery_resource` |
| Adapter canary | appropriate type / `canary` |
| Cloud-backed object | `cloud_object` / `cloud_resource` |
| Unclassified visible resource | appropriate type / `domain_defined` |

Resource classification should avoid exposing unnecessary user-identifying information.

---

# 7. Resource Identity

A resource does not need a raw pathname or user-visible filename to participate in structural analysis.

The adapter should prefer a stable privacy-preserving reference where possible.

A normalized resource identity may represent:

- an application-local resource;
- a user-authorized resource;
- a provider-backed resource;
- a synchronized object;
- an adapter-maintained pseudonymous reference.

The detector generally needs structural identity and continuity, not unnecessary presentation metadata.

Therefore:

> **Stable structural identity is preferred over raw identifying resource detail.**

---

# 8. Actor Mapping

Actor visibility may be incomplete.

Candidate mappings include:

- `application`
- `service`
- `system`
- `user`
- `remote_actor`
- `sync_service`
- `agent`
- `unknown`

When an application can directly establish that it produced a transition, it may identify itself as the observed actor.

When the visible resource simply appears in a changed state and reliable origin information is unavailable, the actor should remain unresolved.

The adapter must not fabricate process or application attribution merely because a resource changed.

---

# 9. Actor Identity

Actor identity should represent only what the evidence establishes.

Possible states include:

- known;
- partially known;
- unknown;
- conflicting.

A recognized application, provider, synchronization service, or system component may be a valid observed actor.

That identity does not establish:

- origin;
- malicious intent;
- ransomware;
- responsibility for an upstream transition.

The adapter therefore preserves:

> **Actor identity ≠ actor intent**

and:

> **observed actor ≠ proven origin**

---

# 10. Origin vs. Transport

This distinction is especially important for cloud-backed and synchronized resources.

A locally visible change may have been:

- originated locally;
- originated remotely;
- transported through synchronization;
- reflected through a provider;
- materialized from previously pending synchronized state;
- produced by an unknown source.

Where evidence establishes the relationship, the adapter may populate:

- `actor.role`
- `origin_actor_ref`
- `transport_actor_ref`
- `context.sync_transport`
- `context.origin_environment_ref`

Where it does not, origin remains unresolved.

> **Local manifestation does not establish local origin.**

---

# 11. Transition Mapping

Platform-visible operations should be normalized according to their observable structural effect.

Possible normalized operations include:

- `read`
- `write`
- `create`
- `delete`
- `rename`
- `move`
- `copy`
- `replace`
- `permission_change`
- `metadata_change`
- `recovery_change`
- `state_change`
- `scope_change`
- `sync`
- `other`

Corresponding structural transitions may include:

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

Where the native operation is observable but does not map precisely, the adapter should preserve it as a native operation rather than force a misleading shared classification.

---

# 12. Observed vs. Derived State

The adapter must preserve the distinction between native observation and adapter derivation.

For example:

**Observed**

A visible resource changed between two bounded observations.

**Derived**

The resource's structural state differs from its previous baseline.

**Not appropriate at the adapter layer**

The resource was changed by ransomware.

The first two may belong in normalized evidence when their lineage is retained.

The last belongs to downstream structural analysis.

---

# 13. Transition Characteristics

Where observable without unnecessary content exposure, the adapter may normalize characteristics such as:

- resource size change;
- content-change indication;
- structural change;
- representation or extension change;
- permission change;
- scope change;
- prior-state preservation;
- recoverability;
- repeated mutation;
- transition timing;
- synchronization transport;
- recovery-state change.

Unavailable characteristics should remain unknown.

---

# 14. Baseline Support

A concrete implementation may maintain a baseline for resources within its authorized scope.

Relevant baseline dimensions may include:

- known resource identities;
- expected resource classes;
- expected operations;
- ordinary transition frequency;
- known actor relationships;
- normal synchronization behavior;
- expected resource scope;
- established transformation workflows.

Baseline comparison may strengthen structural analysis.

It does not establish malicious intent.

When insufficient history exists:

`baseline.available = false`

is the correct representation.

---

# 15. Snapshot-Style Observation

Where continuous event observation is unavailable but repeated state inspection is possible, an implementation may derive a bounded transition from comparison of authorized states.

Conceptually:

**State at T1**

↓

**authorized interval**

↓

**State at T2**

↓

**derived transition**

Such a transition must preserve the fact that it was derived from state comparison rather than directly observed as a native operation.

It may establish that state changed.

It may not establish exactly:

- when the change occurred;
- which actor performed it;
- which intermediate transitions occurred;
- whether several transformations preceded the final state.

Those uncertainties must remain explicit.

---

# 16. Canary Resources

An implementation may optionally maintain adapter-controlled canary resources inside a scope it is authorized to observe.

Canaries may help determine that unexpected mutation occurred within that scope.

A canary transition can provide structurally significant evidence.

It does not independently establish:

- ransomware;
- malicious intent;
- actor origin;
- actor attribution;
- device-wide compromise.

Canaries should contain no sensitive user information.

---

# 17. Capability Declaration

The adapter should provide a declaration conforming to:

`tf.platform-capabilities/v0.1`

The declaration describes what the **specific implementation and environment** can actually support.

Capability states are:

- `supported`
- `partial`
- `unsupported`
- `unknown`

These values are evidence statements.

They are not aspirations.

---

# 18. Observation Capabilities

A concrete adapter should evaluate questions such as:

### Event Observation

Can relevant transitions be directly observed, or only inferred from state comparison?

### Actor Identity

Can the responsible actor be established?

### Actor Lineage

Can parentage, invocation lineage, or upstream origin be established?

### Resource Classification

Can visible resources be classified without exposing unnecessary content?

### Network Context

Is relevant network context available inside the authorized adapter boundary?

### Origin / Transport Distinction

Can locally originated changes be distinguished from synchronized or provider-transported changes?

### Baseline Access

Is sufficient historical state available for meaningful baseline comparison?

### Recovery-State Observation

Can availability or existence of a prior usable state be observed?

Each answer must describe actual capability rather than presumed platform behavior.

---

# 19. Enforcement Capabilities

The adapter must not assume endpoint-style containment powers.

A concrete implementation should independently establish whether it can support:

- write denial;
- actor containment;
- resource isolation;
- network isolation;
- quarantine;
- permission restriction;
- actor disablement;
- session termination.

An implementation may legitimately declare most or all of these:

`unsupported`

or:

`unknown`

That is valid conformance.

> **Honest lack of capability is preferable to false containment.**

---

# 20. Capability Is Not Authority

Even where the adapter can technically perform a change, that does not establish permission to perform it.

Therefore:

**Capability**

answers:

> Can the adapter support this mechanism?

**Authority**

answers:

> Is the mechanism permitted in this case?

**Outcome**

answers:

> What actually happened when execution was attempted?

These stages remain separate.

---

# 21. Receiving a Containment Decision

The adapter may receive a:

`tf.containment-decision/v0.1`

Before executing anything, it should evaluate:

- requested action;
- target;
- scope;
- required capability;
- declared capability;
- authorization;
- constraints;
- reversibility expectations;
- whether fallback is permitted.

A decision requiring additional authorization must not be treated as authorization merely because the adapter received it.

---

# 22. Containment Mapping

Potential structural response requests include:

- increased observation;
- notification;
- write restriction;
- resource isolation;
- actor containment;
- network isolation;
- quarantine;
- permission restriction;
- evidence preservation;
- recovery preparation;
- recovery initiation;
- manual review.

The iOS / iPadOS adapter must map only those requests that its concrete environment actually supports.

A structural request with no supported native mechanism should remain unsupported.

---

# 23. User-Mediated Intervention

Some responses may require visible user participation or another authorized control surface.

When that occurs, the adapter should distinguish:

**response requested**

↓

**user intervention requested**

↓

**user interaction observed**

↓

**resulting state observed**

These are separate events.

A prompt or instruction shown to a user is not proof that the requested operation was performed.

Likewise, user confirmation is not necessarily proof that the resulting structural condition was resolved.

---

# 24. Manual Response

Where automatic enforcement is unavailable, a valid fallback may be a bounded manual-response request.

For example:

**Requested**

`contain_actor`

↓

**native capability unavailable**

↓

**Fallback**

`request_manual_review`

This preserves the analytical recommendation without pretending the adapter has enforcement authority it does not possess.

Manual intervention should still produce an outcome record when its result becomes observable.

---

# 25. Fallback Behavior

When a requested response cannot be executed and fallback is permitted, the adapter may select a weaker supported action.

Fallback should preserve:

- requested action;
- required capability;
- unavailable capability;
- fallback action;
- fallback reason;
- executed scope;
- degradation relationship.

A fallback must never be reported as the original action.

---

# 26. Outcome Reporting

Every attempted response should produce or contribute to:

`tf.response-outcome/v0.1`

Relevant states include:

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
- actual execution status;
- executed response;
- fallback behavior;
- capability limitations;
- direct effects;
- errors and warnings;
- rollback state where applicable;
- provenance.

---

# 27. Execution Does Not Establish Resolution

A successful platform-visible operation does not prove that the destructive structural condition has ended.

Therefore:

> **Execution ≠ Resolution**

The response outcome records what was attempted or executed.

Verification records what state exists afterward.

---

# 28. Verification

Where the adapter can observe post-response state, it should perform another bounded observation cycle.

Verification may ask:

- Does the visible destructive transition continue?
- Did the affected resource change again?
- Did the condition reappear?
- Did another visible resource become affected?
- Did synchronized state reintroduce the transition?
- Is prior usable state still available?
- Can the adapter observe enough of the relevant surface to make a reliable comparison?

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

# 29. Bounded Verification

Verification claims must remain limited to the inspected scope.

For example:

**No further transition observed in the adapter-authorized resource set**

does not establish:

**No destructive transition exists anywhere on the device**

or:

**No synchronized destructive state exists remotely**

The verification scope is part of the conclusion.

A clean bounded rescan must never silently become a device-wide clean claim.

---

# 30. Recovery

Recovery depends on the resource, provider, application, synchronization environment, and mechanisms available to the concrete implementation.

The adapter should preserve separate states for:

- recovery capability;
- recovery-state visibility;
- recovery artifact availability;
- recovery request;
- recovery attempt;
- recovery outcome;
- verification of restored state.

These must not collapse.

> **Recovery capability ≠ successful restoration**

---

# 31. Synchronization

For synchronized resources, this adapter should cooperate with the Cloud / Synchronization adapter rather than attempting to solve cross-environment origin locally.

Relevant normalized evidence may include:

- transport actor;
- synchronization state;
- origin candidate;
- origin environment;
- resource lineage;
- propagation timing;
- provider relationship.

The device-side adapter represents what became visible on the iOS or iPadOS side.

The cloud-sync layer represents what can be established across environments.

---

# 32. Evidence Independence

Multiple observations of one synchronized transition must not automatically become independent evidence.

For example:

**cloud observation**

+

**iPad observation**

+

**iPhone observation**

may represent one transition propagated through synchronization.

Those observations may strongly establish propagation while remaining dependent evidence about the transition's origin.

The adapter should preserve dependency references where known.

---

# 33. Reappearance

A condition may appear to stop within the local observation scope and later return through:

- synchronization;
- provider state;
- remote modification;
- delayed materialization;
- restoration of affected state;
- another authorized resource path.

Reappearance should preserve lineage where evidence permits.

A returning state is not automatically a new independent origin event.

---

# 34. Privacy and Redaction

The adapter should minimize exported information.

Preferred shared fields include:

- privacy-preserving resource ID;
- resource type;
- resource class;
- resource scope;
- structural transition;
- timing;
- preservation state;
- recovery state;
- actor category;
- origin/transport relationship;
- baseline relationship;
- synchronization context;
- provenance.

Avoid exporting unnecessary:

- file contents;
- media contents;
- personal filenames;
- raw provider identifiers;
- account identifiers;
- unrelated application data;
- authentication material;
- unrelated user metadata.

---

# 35. Authentication Material

The Ransomware Structural Pattern Detector does not require authentication secrets.

The adapter must not emit:

- passwords;
- access tokens;
- refresh tokens;
- session secrets;
- private keys;
- provider credentials;
- recovery secrets.

Authentication remains inside the platform or provider-specific security boundary.

Shared objects may contain bounded references to authorization context where needed, but never the credential itself.

---

# 36. Local Processing Preference

Sensitive platform-native operations should remain local when the central detector needs only their structural result.

Candidate local operations include:

- resource-reference handling;
- identifier pseudonymization;
- resource classification;
- baseline comparison;
- deduplication;
- state comparison;
- redaction;
- mapping platform-visible observations into shared transitions.

The design objective is:

> **Export structural evidence, not unnecessary user data.**

---

# 37. Known Limitations

A concrete iOS / iPadOS adapter should explicitly document limitations such as:

- restricted observation scope;
- incomplete visibility into other applications;
- incomplete device-wide resource visibility;
- limited native event history;
- incomplete actor identity;
- incomplete actor lineage;
- unresolved synchronized origin;
- provider-mediated resource abstraction;
- limited enforcement capability;
- user-mediated response requirements;
- incomplete recovery visibility;
- incomplete post-response verification;
- inability to determine device-wide resolution.

These are part of the adapter contract.

They should not be hidden.

---

# 38. Capability Posture

The generic iOS / iPadOS adapter begins from an intentionally conservative posture:

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

This table intentionally makes **no universal implementation-capability claim**.

A concrete adapter should replace `unknown` only when actual support, partial support, or non-support has been established for its deployment.

---

# 39. Why the Default Is Unknown

The generic adapter specification describes an architectural class, not one installed application with one entitlement, one authorization state, one resource scope, and one deployment configuration.

Therefore:

`unknown`

is the honest default.

It does not mean the platform necessarily lacks a capability.

It means:

> **This generic specification does not claim that the capability has been established.**

The concrete capability declaration provides the evidence-backed answer.

---

# 40. iOS / iPadOS Adapter Invariants

## IOS-IPADOS-INV-01 — Observation Boundary Is Real

The adapter must not imply visibility beyond the resources and state actually exposed to the authorized implementation.

## IOS-IPADOS-INV-02 — Unobserved ≠ Absent

Inability to observe a transition does not establish that the transition did not occur.

## IOS-IPADOS-INV-03 — Adapter ≠ Device-Wide Scanner

A bounded application observation must not become a claim about complete device state.

## IOS-IPADOS-INV-04 — State Difference ≠ Native Event

A transition derived from before/after state comparison must remain distinguishable from a directly observed native operation.

## IOS-IPADOS-INV-05 — Actor ≠ Origin

The locally visible actor may transport or materialize a change originating elsewhere.

## IOS-IPADOS-INV-06 — Trusted Transport ≠ Benign Transition

Trust in a provider or synchronization mechanism does not establish the safety of the transition it carries.

## IOS-IPADOS-INV-07 — Adapter ≠ Detector

The adapter reports structural evidence. It does not independently establish ransomware.

## IOS-IPADOS-INV-08 — Capability ≠ Authority

Technical ability to perform an action does not authorize its use.

## IOS-IPADOS-INV-09 — User Prompt ≠ Executed Response

Requesting user intervention does not establish that the requested action occurred.

## IOS-IPADOS-INV-10 — Execution ≠ Resolution

A successfully completed platform operation does not prove that the structural condition has resolved.

## IOS-IPADOS-INV-11 — Local Verification ≠ Device-Wide Verification

A clean bounded rescan cannot establish that unobserved device or remote state is clean.

## IOS-IPADOS-INV-12 — Recovery Capability ≠ Verified Restoration

Availability of recovery does not establish successful restoration.

## IOS-IPADOS-INV-13 — Synchronized Observation ≠ Independent Origin

The same transition observed across multiple synchronized devices may remain one originating event.

## IOS-IPADOS-INV-14 — Privacy Boundary Survives Normalization

Raw identifiers, contents, and credentials should remain local when structural references are sufficient.

---

# 41. Non-Goals

The iOS / iPadOS adapter is not:

- a device-wide surveillance mechanism;
- a mechanism for bypassing application isolation;
- a mechanism for weakening platform security controls;
- a malware-signature scanner;
- a ransomware attribution engine;
- a guarantee of complete resource visibility;
- a guarantee of process-level visibility;
- a guarantee of endpoint-level containment;
- a guarantee of resource recovery;
- proof that unobserved activity is absent;
- an authorization engine.

Its role is narrower:

> **Represent authorized iOS and iPadOS observations faithfully, normalize only the structure the platform exposes, declare limitations honestly, map authorized responses only where genuinely supported, and keep verification bounded to observable state.**

---

# 42. Shared Contracts

The iOS / iPadOS adapter participates in:

- `tf.resource-transition/v0.1`
- `tf.platform-capabilities/v0.1`
- `tf.containment-decision/v0.1`
- `tf.response-outcome/v0.1`
- `tf.verification/v0.1`

The Ransomware Structural Pattern Detector consumes its normalized observations and may produce:

- `tf.structural-pattern/v0.1`

This adapter does not redefine those contracts.

---

# 43. Relationship to Cloud / Synchronization

The Cloud / Synchronization adapter complements this device-side adapter.

Conceptually:

**iOS / iPadOS-visible state**

↓

**device-side normalized transition**

↕ correlation

**cloud / synchronization evidence**

↓

**cross-environment structural lineage**

The iOS / iPadOS adapter should make only claims justified by device-side evidence.

The Cloud / Synchronization adapter may contribute evidence about remote origin, transport, propagation, version relationships, and cross-environment recovery.

Neither layer should invent evidence missing from the other.

---

# Canonical Summary

> **The iOS / iPadOS adapter provides a conservative, privacy-preserving bridge between authorized application-visible resource state and the Shared Structural Event Grammar without pretending to possess device-wide observation or enforcement authority.**

Its observation rule is:

> **Describe only what the authorized environment exposes. Treat everything else as unresolved.**

Its derivation rule is:

> **A before/after state difference may establish a transition without establishing the intermediate mechanism or actor.**

Its actor rule is:

> **The actor visible where a transition materializes may not be the actor that originated it.**

Its capability rule is:

> **Begin from unknown and promote a capability only when the concrete implementation establishes it.**

Its response rule is:

> **A requested action with no supported and authorized native mechanism remains unexecuted.**

Its privacy rule is:

> **Export structural relationships rather than unnecessary user content, identifiers, or credentials.**

Its verification rule is:

> **A clean result inside the observable scope says nothing definitive about state outside that scope.**
