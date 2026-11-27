# Cloud / Synchronization Adapter

> **Cross-environment adapter specification for representing synchronized resource transitions without confusing origin, transport, replication, observation, or propagation.**

The Cloud / Synchronization adapter provides the structural boundary between synchronized resource environments and the Ransomware Structural Pattern Detector.

Unlike an operating-system adapter, this adapter is not defined by one device or kernel boundary.

Its concern is the movement of structural transitions across:

- devices;
- accounts;
- synchronization clients;
- cloud-backed resources;
- shared resource spaces;
- mirrored environments;
- remote storage;
- provider-mediated resource histories.

Its governing rule is:

> **A synchronized transition may be locally real without being locally originated. Preserve the lineage of the change before assigning meaning to the actor that transported it.**

---

## Status

- **Adapter ID:** `rspd-cloud-sync`
- **Environment:** Cloud and synchronized resource systems
- **Status:** Experimental
- **Role:** Cross-environment observation, normalization, lineage preservation, propagation mapping, capability declaration, bounded response mapping, and verification support
- **Normalized observation:** `tf.resource-transition/v0.1`
- **Capability declaration:** `tf.platform-capabilities/v0.1`
- **Decision input:** `tf.containment-decision/v0.1`
- **Execution output:** `tf.response-outcome/v0.1`
- **Verification output:** `tf.verification/v0.1`

---

# 1. Scope

The Cloud / Synchronization adapter represents resource transitions that cross or depend upon synchronization boundaries.

Its potential scope includes:

- cloud-backed resources;
- synchronized user resources;
- shared resource spaces;
- mirrored resource collections;
- provider-mediated transitions;
- replicated changes;
- synchronization metadata;
- resource history;
- recovery-visible state;
- remote-to-local transitions;
- local-to-remote transitions;
- remote-to-remote transitions where observable;
- multi-device propagation.

The exact scope depends on the provider, account, deployment, permissions, and interfaces available to the implementation.

The adapter must declare the scope it can actually observe.

It must not imply visibility across an entire synchronization topology when only one segment is observable.

---

# 2. Structural Problem

Synchronization creates an attribution problem that does not exist in the same form for purely local observations.

Consider:

**Remote transition**

↓

**Synchronization transport**

↓

**Cloud-backed state**

↓

**Local synchronization client**

↓

**Local resource transition**

A local operating-system adapter may truthfully observe that a synchronization process modified a resource.

A cloud adapter may truthfully observe that a cloud object changed.

Another device may observe the same transition arriving locally.

All three observations can be valid.

They are not necessarily three independent destructive events.

They may be three observations of one originating structural transition.

The adapter therefore preserves:

> **Observation count ≠ origin count ≠ independent evidence count**

---

# 3. Structural Roles

Synchronization analysis should distinguish several roles.

## Origin

The environment or actor where the relevant transition originated, when evidence establishes it.

## Transport

The actor, service, client, or mechanism that carried the transition between environments.

## Provider

The infrastructure or service through which synchronized state is represented or propagated.

## Observer

The adapter or environment from which evidence about the transition was collected.

## Recipient

An environment or resource that received the synchronized transition.

## Propagation Target

An additional environment or resource to which the transition subsequently spread.

These roles may overlap.

They must not be assumed to be identical.

---

# 4. Origin Is Not Always Observable

A synchronization provider may reveal that a transition occurred without exposing enough information to establish its true origin.

Possible states include:

- origin directly observed;
- origin inferred with supporting lineage;
- origin candidate identified;
- multiple origin candidates;
- origin conflicting;
- origin unknown.

The adapter should preserve the strongest state actually supported by evidence.

It must not assign the synchronization service itself as the origin merely because that service is observable.

---

# 5. Native Observation Sources

A Cloud / Synchronization implementation may consume authorized observations from sources such as:

- provider-visible change records;
- synchronization state;
- client-visible synchronization events;
- resource metadata;
- resource history;
- version or recovery state;
- account-visible activity;
- shared-resource activity;
- authorized platform-adapter observations;
- explicit user-supplied evidence;
- adapter-maintained baseline history.

The exact mechanisms are provider-specific and must be documented by concrete implementations.

This specification does not assume that every synchronization provider exposes equivalent telemetry.

---

# 6. Observation Boundary

The adapter should explicitly declare:

- which provider or synchronization environment is represented;
- which account or authorized scope is visible;
- which resource classes are observable;
- whether historical observations are available;
- whether origin information is available;
- whether transport identity is available;
- whether receiving environments are visible;
- whether resource history is visible;
- whether recovery state is visible;
- whether enforcement is supported;
- whether post-response verification is supported.

Missing visibility remains missing visibility.

> **Unobserved remote state must not become presumed safe state.**

---

# 7. Resource Mapping

Provider-native resources should map into the Shared Structural Event Grammar according to structural role.

Candidate mappings include:

| Synchronized resource | Shared resource type/class |
|---|---|
| Cloud-hosted document | `cloud_object` / `user_document` |
| Cloud photo | `cloud_object` / `photo` |
| Cloud video | `cloud_object` / `video` |
| Cloud audio | `cloud_object` / `audio` |
| Archive | `cloud_object` / `archive` |
| Project resource | `cloud_object` / `project_file` |
| Application data | `cloud_object` / `application_data` |
| Configuration | `cloud_object` / `configuration` |
| Shared resource | appropriate type / domain-appropriate class |
| Backup | `cloud_object` / `backup` |
| Recovery object | `cloud_object` / `recovery_resource` |
| Cloud canary | `cloud_object` / `canary` |
| Provider metadata object | `cloud_object` / `domain_defined` |

The adapter should classify structure without unnecessarily exporting provider-native names or user content.

---

# 8. Stable Resource Identity

A synchronized resource may appear differently on different devices or through different interfaces.

For example, one structural resource may have:

- a cloud-side identifier;
- a desktop-local representation;
- a mobile-provider reference;
- a synchronized working copy;
- a historical version;
- a shared-resource representation.

The adapter should preserve a stable privacy-conscious resource identity where evidence allows.

A key objective is to distinguish:

**same structural resource observed in multiple environments**

from:

**multiple genuinely distinct resources**

without forcing raw provider identifiers into the central analytical layer when they are unnecessary.

---

# 9. Resource Lineage

Where observable, the adapter should preserve relationships among:

- current resource;
- prior resource state;
- synchronized representation;
- local representation;
- remote representation;
- historical version;
- restored version;
- copied resource;
- moved resource;
- replaced resource.

This lineage is particularly important when destructive transitions propagate through synchronization.

A local replacement and a remote replacement may be manifestations of the same upstream transition.

---

# 10. Actor Mapping

Candidate actor categories include:

- `user`
- `application`
- `service`
- `remote_actor`
- `sync_service`
- `system`
- `agent`
- `unknown`

An adapter should not interpret service identity as originating intent.

For example:

`actor.type = "sync_service"`

may accurately describe a transport actor.

It does not establish that the service originated the destructive transformation.

---

# 11. Origin and Transport Mapping

When evidence permits, normalized transitions should preserve:

- observed actor;
- origin actor reference;
- transport actor reference;
- origin environment reference;
- synchronization context;
- correlation identifier;
- provider provenance.

Conceptually:

**Origin Actor**

↓

**Origin Environment**

↓

**Transition**

↓

**Transport Actor**

↓

**Synchronization Boundary**

↓

**Recipient Environment**

↓

**Observed Resource Transition**

When any stage is unknown, that uncertainty should be retained.

---

# 12. Transition Mapping

Relevant normalized operations may include:

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

Corresponding structural actions may include:

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

Synchronization itself may be a transport operation rather than the underlying structural cause.

The adapter should therefore distinguish:

**transition being transported**

from:

**transport operation**

where the evidence supports that distinction.

---

# 13. Propagation

Propagation is a first-class concern for this adapter.

A destructive transition may move through a topology such as:

**Origin environment**

↓

**Cloud/synchronization layer**

↓

**Device A**

↓

**Device B**

↓

**Shared resource consumer**

The adapter should preserve evidence of:

- first observable environment;
- subsequent observed environments;
- transport relationships;
- resource lineage;
- transition timing;
- dependency relationships;
- propagation state.

The detector may then classify the resulting structural pattern as:

- possible propagation;
- observed propagation;
- active propagation;
- ceased propagation;
- unknown propagation state.

The adapter supplies the evidence.

The detector supplies the bounded interpretation.

---

# 14. Evidence Independence

Synchronization makes evidence-independence analysis essential.

Suppose the same destructive transition is observed by:

- a cloud event source;
- a desktop synchronization client;
- a mobile client;
- a second cloud interface.

Those observations may strengthen confidence that the transition occurred.

They do not automatically provide independent evidence about its origin or cause.

The adapter should preserve known dependencies among observations.

Conceptually:

**One source transition**

↓

**multiple synchronized observations**

must not silently become:

**multiple independent source transitions**

This distinction protects rate, acceleration, scope, and confidence calculations from synchronization-induced inflation.

---

# 15. Deduplication

Concrete implementations should support a bounded deduplication strategy where sufficient evidence is available.

Candidate correlation dimensions include:

- resource identity;
- version or state identity;
- transition timing;
- origin reference;
- transport reference;
- correlation identifier;
- provider event reference;
- prior-state reference;
- resulting-state reference;
- environment relationship.

Deduplication should preserve the original observation records.

Its purpose is not to discard evidence.

Its purpose is to distinguish:

**multiple observations of one transition**

from:

**multiple distinct transitions**

The derivation method should remain reconstructable.

---

# 16. Mirrored State

Mirroring can create apparently independent resource changes that are structurally dependent.

The adapter should therefore preserve whether an observed state is:

- original;
- synchronized;
- mirrored;
- replicated;
- restored;
- copied;
- unresolved.

Where the precise relationship cannot be established, it should remain unresolved rather than being assigned independent status.

---

# 17. Baseline Support

A synchronization baseline may include:

- expected synchronization direction;
- expected devices or environments;
- known transport services;
- expected resource classes;
- typical transition rate;
- normal propagation delay;
- known shared-resource relationships;
- normal bulk synchronization behavior;
- established recovery behavior.

The baseline should help distinguish ordinary synchronization from structurally abnormal propagation.

It must not convert deviation directly into malicious intent.

---

# 18. Expected Synchronization as Counter-Evidence

Broad or rapid resource transition is not automatically suspicious in a synchronized environment.

Potential competing explanations include:

- initial synchronization;
- authorized bulk migration;
- restoration;
- provider-side reindexing reflected as changes;
- expected bulk transformation;
- user-authorized relocation;
- synchronization after extended disconnection;
- legitimate application workflow.

Where supported, these should remain visible as counter-evidence or competing explanations.

The existence of a synchronization explanation does not automatically make destructive effects benign.

Likewise, destructive appearance does not automatically make synchronization malicious.

Both sides of the evidence boundary must survive.

---

# 19. Recovery State

Cloud-backed systems may expose structural evidence related to:

- historical versions;
- preserved prior state;
- deleted-resource state;
- backup state;
- recovery objects;
- rollback mechanisms;
- restoration operations.

The adapter should distinguish:

**recovery mechanism exists**

from:

**recovery state is available**

from:

**recovery artifact exists**

from:

**recovery was attempted**

from:

**recovery succeeded**

from:

**restored state was verified**

These stages must not collapse into one recovery flag.

---

# 20. Capability Declaration

The adapter should provide a declaration conforming to:

`tf.platform-capabilities/v0.1`

Capability values must describe the actual synchronization environment represented by the implementation.

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

- rollback;
- snapshot or version restoration;
- resource restoration;
- configuration restoration.

Possible verification capabilities include:

- post-action observation;
- state comparison;
- persistence detection;
- reappearance detection;
- recovery verification.

Each must be declared as:

- `supported`
- `partial`
- `unsupported`
- `unknown`

A concrete provider implementation determines the correct value.

---

# 21. Capability Is Provider-Specific

This specification must not imply that all synchronization providers expose equivalent capabilities.

A capability available in one deployment may be unavailable in another.

Likewise, capability may vary by:

- authorization;
- account type;
- resource type;
- resource ownership;
- shared-resource relationship;
- deployment configuration;
- provider interface;
- client environment.

The correct declaration is the one established for the current adapter environment.

> **Provider category does not establish capability.**

---

# 22. Containment Mapping

An authorized containment decision may request structural responses such as:

- increase observation;
- notify an authorized operator;
- deny resource writes;
- isolate affected resources;
- restrict permissions;
- contain propagation;
- preserve evidence;
- prepare recovery;
- initiate recovery;
- request manual review.

A cloud-sync implementation may execute only responses supported by its declared capabilities and governing authorization.

The shared action name describes structural intent.

The concrete provider implementation determines the native mechanism, if one exists.

---

# 23. Local vs. Remote Containment

Cross-environment incidents may require containment at more than one boundary.

For example:

**Local containment**

may stop one device from continuing an originating transition.

But:

**remote synchronized state**

may already contain the destructive transition.

Likewise:

**remote containment**

may stop further synchronization.

But:

**another endpoint**

may already hold a pending or locally materialized destructive state.

Therefore:

> **Containment at one synchronization boundary does not establish containment across the topology.**

The outcome must identify the actual scope of the action performed.

---

# 24. Propagation Containment

When authorized and supported, the adapter may participate in attempts to bound propagation.

The structural response may target:

- a resource;
- a resource set;
- an account;
- a session;
- an environment;
- a shared scope;
- a synchronization relationship.

The adapter must not claim broader containment than the mechanism's actual scope.

A response affecting one account or resource set does not automatically establish that another environment is protected.

---

# 25. Authority Boundaries

Cloud and synchronization systems may involve several distinct authority domains.

Examples include:

- resource owner;
- account owner;
- shared-resource participant;
- device owner;
- organization;
- provider;
- local platform;
- external synchronized participant.

The adapter must operate only within explicitly established authority.

Visibility into a resource does not automatically authorize:

- deletion;
- quarantine;
- permission changes;
- synchronization suspension;
- rollback;
- restoration;
- account modification.

Therefore:

> **Visibility ≠ ownership ≠ authority**

---

# 26. Fallback Behavior

If a requested response cannot be executed as requested, and fallback is allowed, the adapter may choose a bounded alternative.

The outcome should preserve:

- requested response;
- required capabilities;
- unavailable capabilities;
- fallback action;
- fallback reason;
- actual scope;
- degradation relationship.

Potential structural fallback classes include:

- increased observation;
- notification;
- narrower resource isolation;
- narrower permission restriction;
- evidence preservation;
- recovery preparation;
- manual intervention request.

A fallback must not be recorded as equivalent unless it truly provides equivalent structural effect.

---

# 27. Outcome Reporting

Execution results should map into:

`tf.response-outcome/v0.1`

The record should distinguish:

- response requested;
- execution attempted;
- response actually executed;
- fallback;
- actual scope;
- capability constraints;
- direct effects;
- side effects;
- errors;
- warnings;
- rollback state;
- execution provenance.

For synchronized environments, provenance should retain enough information to identify the environment and adapter that performed or observed the response.

---

# 28. Verification

Verification must examine resulting synchronized state rather than trusting execution success.

Relevant questions include:

- Did destructive transitions cease?
- Did synchronization continue transporting them?
- Did the pattern reappear?
- Did another environment propagate the transition again?
- Are additional resources now affected?
- Has the remote state stabilized?
- Has the local state stabilized?
- Are historical or recovery states still available?
- Did a supposedly isolated resource change again?
- Can all relevant environments actually be observed?

Possible verification results include:

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

# 29. Cross-Environment Verification

A pattern should not be declared globally resolved solely because one environment appears clean.

Conceptually:

**Environment A: no continuation observed**

+

**Environment B: unobserved**

+

**Cloud state: partially observed**

does not imply:

**globally resolved**

The correct result may instead be:

- partially contained;
- mixed;
- partially resolved;
- unable to verify.

The verification scope must remain explicit.

---

# 30. Reappearance

Synchronization can make reappearance structurally important.

A destructive transition may appear to stop locally and then return through:

- another device;
- remote state;
- delayed synchronization;
- a different synchronized actor;
- restoration of contaminated state;
- unresolved propagation.

The adapter should preserve the lineage of the reappearing transition where possible.

A reappeared condition should not automatically be treated as a wholly new independent event.

---

# 31. Loops and Echoes

Synchronized systems may produce observations that appear cyclic.

Conceptually:

**Environment A**

↓

**Provider**

↓

**Environment B**

↓

**new synchronized state**

↓

**Provider**

↓

**Environment A**

An implementation should preserve enough lineage to distinguish repeated independent transitions from synchronization echoes where evidence permits.

Otherwise, the detector could incorrectly inflate:

- event count;
- rate;
- acceleration;
- affected scope;
- evidence independence.

Unresolved loops should remain explicitly unresolved.

---

# 32. Conflict State

Some synchronized environments may expose multiple competing versions or states of a resource.

Where the adapter can observe such a condition, it should preserve it structurally rather than arbitrarily selecting one state as canonical.

A conflict may affect:

- current-resource identity;
- prior-state comparison;
- recoverability;
- propagation analysis;
- verification.

Conflict does not itself establish ransomware.

It may, however, materially affect what the detector can conclude.

---

# 33. Privacy and Redaction

Synchronization environments may expose identifiers spanning accounts, devices, recipients, shared resources, and providers.

The adapter should minimize exported identity information.

Preferred structural representations include:

- pseudonymous resource reference;
- environment reference;
- actor category;
- transport relationship;
- origin relationship;
- synchronization state;
- transition type;
- version relationship;
- recovery relationship;
- propagation relationship;
- provenance.

Avoid exporting unnecessary:

- document contents;
- plaintext credentials;
- personal filenames;
- account email addresses;
- recipient identities;
- provider tokens;
- device names;
- full provider-native paths;
- unrelated activity.

Raw identifiers may remain local when structural references are sufficient.

---

# 34. Credential Boundary

The shared detector does not require provider credentials.

Credential handling belongs entirely outside the normalized analytical objects except for bounded references indicating authorization or account context where necessary.

The adapter must not place into shared detector output:

- passwords;
- access tokens;
- refresh tokens;
- session secrets;
- API secrets;
- recovery secrets.

Authentication material must remain inside the provider-specific security boundary.

---

# 35. Data Minimization

The adapter should export only what the detector needs to reason about destructive structure.

For example, the detector may need:

- a stable resource reference;
- resource class;
- resource sensitivity;
- transition type;
- timing;
- origin/transport state;
- propagation relationship;
- preservation state;
- recovery state;
- baseline deviation;
- evidence dependency.

It usually does not need the underlying resource content.

The governing rule remains:

> **Normalize relationships before exporting identities or content.**

---

# 36. Known Limitations

Concrete cloud-sync implementations should explicitly document limitations such as:

- incomplete event history;
- delayed observation;
- incomplete origin information;
- transport identity without origin identity;
- inaccessible remote environments;
- incomplete resource lineage;
- unreliable cross-device timing;
- missing historical versions;
- incomplete recovery visibility;
- ambiguous shared-resource authority;
- partial enforcement capability;
- provider-specific response limitations;
- incomplete post-response verification;
- inability to determine evidence independence;
- inability to distinguish propagation from repeated independent transitions.

These are legitimate analytical states.

They must not be hidden behind optimistic defaults.

---

# 37. Capability Posture

This generic adapter does not declare universal capability support.

Its default posture is:

| Capability | Generic cloud-sync posture |
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

This is intentional.

`cloud-sync` represents a **class of environments**, not one provider implementation.

Concrete provider adapters replace `unknown` with evidence-backed capability declarations.

---

# 38. Cloud / Synchronization Adapter Invariants

## CLOUD-SYNC-INV-01 — Local Observation ≠ Local Origin

A transition observed locally may have originated elsewhere.

## CLOUD-SYNC-INV-02 — Transport ≠ Origin

A synchronization client or provider carrying a transition must not automatically be identified as its origin.

## CLOUD-SYNC-INV-03 — Trusted Transport ≠ Benign Transition

Trust in the synchronization mechanism does not establish that the transported change is safe.

## CLOUD-SYNC-INV-04 — Observation Count ≠ Event Independence

Multiple observations of the same propagated transition must not automatically become independent evidence.

## CLOUD-SYNC-INV-05 — Replication ≠ New Origin

A replicated destructive state does not establish a new originating transition at every recipient.

## CLOUD-SYNC-INV-06 — Visibility ≠ Authority

The ability to observe synchronized state does not authorize its modification.

## CLOUD-SYNC-INV-07 — Local Containment ≠ Global Containment

Containment in one environment does not establish containment elsewhere.

## CLOUD-SYNC-INV-08 — Execution ≠ Resolution

A successfully executed provider action does not prove that destructive state no longer exists elsewhere in the synchronization topology.

## CLOUD-SYNC-INV-09 — Recovery Mechanism ≠ Verified Recovery

Available history or rollback capability does not establish successful restoration.

## CLOUD-SYNC-INV-10 — Unknown Remote State ≠ Safe Remote State

An environment that cannot be observed remains unresolved.

## CLOUD-SYNC-INV-11 — Reappearance ≠ Necessarily New Event

A condition that returns after apparent containment may be propagated or delayed state from an earlier transition.

## CLOUD-SYNC-INV-12 — Provenance Must Cross Boundaries

Cross-environment normalization must preserve enough lineage to reconstruct the relationship among origin candidates, transports, observers, recipients, and resources.

---

# 39. Non-Goals

The Cloud / Synchronization adapter is not:

- a universal cloud-provider API;
- a provider-specific implementation;
- a ransomware classifier;
- an attribution engine;
- a synchronization trust engine;
- proof that cloud-backed resources are recoverable;
- proof that a synchronization service caused a transported transition;
- a guarantee of cross-device visibility;
- a guarantee of global containment;
- a mechanism for bypassing provider authorization;
- a reason to centralize user content or credentials.

Its role is narrower:

> **Represent cross-environment transitions faithfully enough to distinguish origin, transport, propagation, replication, evidence dependency, response scope, and verification boundaries.**

---

# 40. Shared Contracts

The Cloud / Synchronization adapter participates in:

- `tf.resource-transition/v0.1`
- `tf.platform-capabilities/v0.1`
- `tf.containment-decision/v0.1`
- `tf.response-outcome/v0.1`
- `tf.verification/v0.1`

The Ransomware Structural Pattern Detector consumes the resulting normalized observations and may produce:

- `tf.structural-pattern/v0.1`

A concrete provider adapter should reuse these contracts rather than redefining their semantics.

---

# 41. Relationship to Platform Adapters

The cloud-sync adapter complements rather than replaces device-specific adapters.

A device adapter may observe:

> **A synchronization process modified this local resource.**

The cloud-sync adapter may observe:

> **A related transition crossed a synchronization boundary.**

The detector may then correlate those observations while preserving their dependency.

Conceptually:

**Windows / macOS / Linux / Android / iOS observation**

↓

**local normalized transition**

↕ correlation

**cloud-sync normalized transition**

↓

**shared structural pattern**

This allows a cross-environment pattern to be reconstructed without pretending every observation originated independently.

---

# Canonical Summary

> **The Cloud / Synchronization adapter represents destructive resource transitions across synchronization boundaries while preserving the distinction between origin, transport, observation, replication, propagation, execution scope, and verified state.**

Its lineage rule is:

> **Follow the transition, not merely the process that delivered it.**

Its evidence rule is:

> **Multiple synchronized observations may confirm that a transition propagated without independently confirming where or why it originated.**

Its containment rule is:

> **Containment is scoped to the environments and resources actually affected by the executed response.**

Its privacy rule is:

> **Normalize relationships before exporting identities, credentials, or content.**

Its verification rule is:

> **A clean observation in one environment cannot establish resolution in another environment that was not observed.**

And its architectural rule is:

> **Origin, transport, propagation, and observation are different structural roles. Preserve those distinctions all the way through the lineage.**
