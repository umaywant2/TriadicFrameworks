<img width="1194" height="672" alt="Ransomware_Structural_Pattern_Detector_adapters_normalization_fields_" src="https://github.com/user-attachments/assets/0c60df95-7ef4-4720-8102-44a10df4bde2" />

# Normalization Fields

> **Reference guide for translating native platform, service, resource, and cross-environment observations into the Shared Structural Event Grammar without collapsing observation into interpretation.**

Normalization is the boundary between native evidence and portable structural evidence.

Its purpose is to answer:

> **How can an observation be represented consistently enough for structural analysis while preserving what was observed, what was derived, what remains unknown, and where the evidence came from?**

Normalization does **not** answer:

> **What does this activity ultimately mean?**

That distinction is fundamental to the Ransomware Structural Pattern Detector.

---

# Position in the Architecture

The normalization boundary is:

**Native observation**

↓

**Adapter**

↓

**Normalization**

↓

**`tf.resource-transition/v0.1`**

Then normalization stops.

Downstream analysis begins separately:

**Normalized resource transitions**

↓

**Correlation**

↓

**Derived structural signals**

↓

**Supporting evidence**

+

**Counter-evidence**

+

**Unresolved evidence**

↓

**Competing explanations**

↓

**Structural assessment**

↓

**`tf.structural-pattern/v0.1`**

A normalized transition is therefore evidence for interpretation.

It is not the interpretation itself.

---

# Adapter-Neutral Principle

All adapters may emit the same shared transition family while observing very different native environments.

Current adapter classes include:

## Platform Adapters

- Windows
- Linux
- macOS
- Android
- iOS / iPadOS

## Cross-Environment Adapters

- Cloud / Synchronization

## Resource / Service Adapters

- Database
- Cache

The native evidence differs.

The shared structural representation remains comparable.

This is the normalization contract.

---

# Core Normalization Fields

The exact adapter configuration varies by environment, but the following fields express the common normalization responsibilities.

| Field | Purpose |
|---|---|
| `output_schema` | Declares the canonical normalized object produced by the adapter. |
| `preserve_native_operation` | Retains the platform- or service-native operation where available and useful. |
| `preserve_provenance` | Requires lineage showing where the normalized observation originated. |
| `preserve_unknowns` | Prevents missing evidence from silently becoming `false`, `safe`, `absent`, or another definite state. |
| `preserve_source_dependencies` | Retains relationships among observations that may share the same originating event. |
| `preserve_origin_transport_distinction` | Prevents the locally visible actor from automatically becoming the presumed originating actor. |
| `derive_resource_class` | Allows native resources to map into portable structural classes. |
| `derive_baseline_state` | Allows explicitly derived comparisons with established historical or expected state. |
| `redaction_enabled` | Allows sensitive native detail to be minimized before normalized evidence leaves the adapter boundary. |

Adapter families may add additional preservation fields for structural distinctions specific to their environment.

---

# `output_schema`

The canonical output for normalized observations is:

`tf.resource-transition/v0.1`

The authoritative schema is:

`../../Shared_Structural_Event_Grammar/resource-transition.schema.json`

This establishes the shared portable envelope.

An adapter-specific configuration schema does not redefine `tf.resource-transition/v0.1`.

Instead:

**Adapter schema**

defines how a concrete adapter is configured.

**Resource Transition schema**

defines the normalized event it may emit.

---

# Native Operation vs. Normalized Operation

A native environment may describe an operation using platform-specific terminology.

Normalization may map that operation into a shared vocabulary while preserving the native value.

Conceptually:

**Native operation**

↓

**adapter mapping**

↓

**normalized operation**

For example:

**native filesystem operation**

↓

`write`

or:

**native database operation**

↓

`state_change`

or:

**native synchronization operation**

↓

`sync`

The shared operation enables cross-adapter structural comparison.

The native operation preserves diagnostic lineage.

Neither establishes domain interpretation.

---

# Observation vs. Derivation

Normalization may contain both direct observations and bounded derivations.

These must remain distinguishable.

## Observed

Evidence supplied directly by the underlying observation source.

Examples:

- a resource changed;
- an operation was reported;
- a synchronization service transported an update;
- an actor identifier was supplied;
- a database transaction completed;
- a cache entry expired.

## Derived

A value calculated or classified from observations.

Examples:

- native resource mapped to `user_document`;
- event mapped to `write`;
- resource determined to fall inside protected scope;
- operation compared with baseline;
- resource identifier pseudonymized;
- two observations correlated as representations of the same transition.

## Interpreted

A domain-level conclusion.

Examples:

- ransomware-like structural pattern;
- harmful behavior;
- malicious intent;
- attribution;
- containment threshold crossed.

Interpretation does **not** belong in normalization.

The boundary is:

> **Observed and explicitly derived structure may enter the normalized event. Domain conclusions do not.**

---

# `preserve_native_operation`

A normalized operation may simplify platform-specific evidence.

The original operation should remain available when useful for:

- diagnostics;
- reconstruction;
- comparison;
- validator testing;
- future remapping;
- platform-specific investigation.

Conceptually:

**Native operation**

↓

**shared operation**

without destroying the native lineage.

This allows the shared grammar to remain stable even if native event vocabularies differ substantially.

---

# `preserve_provenance`

Every normalized event should retain sufficient lineage to answer:

- Where was this observed?
- Which adapter observed or normalized it?
- When was it observed?
- When was it normalized?
- Which capability declaration applied?
- Which native evidence supported it?
- Which derivation method produced bounded derived values?
- What information was removed or generalized?

A typical provenance object may preserve:

- `platform`
- `adapter`
- `adapter_version`
- `capabilities_ref`
- `observed_at`
- `normalized_at`
- `native_event_ref`
- `raw_event_retained`
- `derivation_refs`
- `redactions`

Normalization should therefore be **traceable abstraction**, not evidence destruction.

---

# `preserve_unknowns`

Unknown state is first-class.

Normalization must distinguish:

**false**

from:

**unknown**

from:

**not applicable**

from:

**not observed**

from:

**unavailable**

where the relevant schema supports those distinctions.

For example:

`recoverable = false`

means evidence establishes that the resource is not recoverable.

Whereas:

`recoverable = null`

means recoverability was not established.

These statements are not interchangeable.

The core invariant is:

> **Unknown ≠ false**

---

# Null vs. False

Boolean observations frequently need three-valued reasoning.

Consider:

`propagation_observed = false`

This means the available observation supports the statement that propagation was not observed within the applicable scope.

By contrast:

`network_origin = null`

means network origin could not be established.

A missing answer is not a negative answer.

Normalization must preserve that distinction.

---

# `preserve_source_dependencies`

Several observations may refer to the same underlying transition.

Examples include:

- multiple telemetry sources observing one filesystem operation;
- host and container observers reporting one resource change;
- cloud and endpoint observers seeing one synchronized transition;
- database logical and storage layers representing one operation chain;
- replicated cache nodes seeing the same propagated mutation.

Normalization and correlation must preserve these dependencies.

Otherwise:

**one underlying transition**

could become:

**several supposedly independent events**

which could distort:

- event count;
- rate;
- acceleration;
- scope;
- propagation;
- confidence;
- evidence independence.

The invariant is:

> **Multiple observations ≠ multiple independent originating transitions.**

---

# `preserve_origin_transport_distinction`

The actor visible at the point of observation may not be the actor that originated the transition.

This occurs frequently with:

- synchronization systems;
- cloud providers;
- databases;
- caches;
- services;
- remote resources;
- delegated operations.

The shared model may therefore preserve:

- observed actor;
- origin actor reference;
- transport actor reference;
- origin environment;
- synchronization or replication context.

The invariant is:

> **Observed actor ≠ proven origin actor**

---

# Resource Normalization

Native resources map into shared structural types and classes.

Examples include:

- file → `user_document`
- file → `photo`
- dataset → `database`
- cloud object → `cloud_resource`
- backup object → `backup`
- recovery object → `recovery_resource`
- adapter-controlled resource → `canary`
- AI context → `context_resource`

The purpose is structural classification.

It is not to expose unnecessary native identity.

---

# Privacy-Preserving Resource Identity

A normalized event may use a pseudonymous structural identifier such as:

`resource://pseudonymous/document-0087`

rather than exposing:

- full filesystem path;
- user-visible document name;
- account identity;
- provider-native identifier;
- database record contents;
- cache key;
- resource contents.

The adapter may retain native identity locally when required for authorized correlation, response, verification, or recovery.

The central detector usually needs continuity of structural identity, not raw presentation detail.

---

# Resource Type vs. Resource Class

The shared model distinguishes general structural type from analytical class.

For example:

**Type:** `file`

**Class:** `user_document`

or:

**Type:** `cloud_object`

**Class:** `backup`

or:

**Type:** `dataset`

**Class:** `database`

The type describes what kind of structural resource is represented.

The class describes the role that resource plays in analysis.

---

# Transition Normalization

Native operations map into structural transitions.

Examples may include:

| Native behavior | Shared operation | Structural action |
|---|---|---|
| resource write | `write` | `modify` |
| creation | `create` | `create` |
| deletion | `delete` | `remove` |
| replacement | `replace` | `replace` |
| permission modification | `permission_change` | `restrict`, `grant`, or `revoke` |
| synchronization | `sync` | `propagate` or another supported structural action |
| state mutation | `state_change` | `transform` or another bounded mapping |

The mapping should remain conservative.

If the native event does not support a precise structural action, the adapter should preserve uncertainty rather than force an overly specific classification.

---

# Transition Characteristics

Normalization may preserve characteristics such as:

- size change;
- content change;
- structural change;
- entropy shift;
- representation or extension change;
- ownership change;
- permission change;
- authority change;
- scope change;
- recovery-state change;
- prior-state preservation;
- reversibility.

These characteristics become potential evidence.

They do not independently establish ransomware.

---

# Context Normalization

Context describes circumstances surrounding the transition.

Candidate fields include:

- user intent;
- interactive-session state;
- bulk-operation state;
- network origin;
- synchronization transport;
- origin environment;
- session reference;
- authorized observation scope.

These fields help downstream analysis evaluate competing explanations.

They must not be converted into unsupported conclusions.

---

# User Intent

Where evidence allows, the shared event may distinguish:

- explicit;
- inferred;
- absent;
- unknown;
- not applicable.

This is **user-intent evidence**, not a general statement about actor motive.

For example:

**User intent:** unknown

does not mean:

**Actor intent:** harmful.

Broader intent assessment belongs downstream.

---

# Baseline Derivation

Where an appropriate baseline exists, normalization or a bounded derived stage may compare the current transition against established history.

Possible fields include:

- known actor;
- operation typical;
- scope typical;
- rate typical;
- resource typical;
- role coherent.

A baseline may produce a mixed result:

**known actor**

+

**expected resource**

+

**expected scope**

+

**atypical operation**

+

**atypical rate**

+

**role coherence unresolved**

That mixed state should survive.

Do not collapse it into:

`suspicious = true`

---

# Consequence

The consequence object records observable effects of the transition.

Examples include:

- resource changed;
- resource unavailable;
- resource exposed;
- resource restricted;
- resource propagated;
- recovery affected;
- authority changed;
- context changed.

Consequences should remain bounded to directly supported evidence.

A changed resource does not automatically mean destructive loss.

A recovery-related change does not automatically mean recovery interference.

A propagated transition does not automatically establish independent origin at each destination.

---

# Adapter-Specific Preservation Fields

The common normalization contract is extended by adapter-specific structural distinctions.

These fields preserve evidence boundaries. They do not create new domain verdicts.

---

# macOS

macOS may use:

- `preserve_event_semantics`
- `preserve_trust_context`
- `preserve_synchronization_context`

The critical distinction is:

**notification**

≠

**authorization opportunity**

≠

**policy authority**

A notification describes evidence.

An authorization event may provide a pre-operation decision opportunity.

Neither determines the RSPD policy decision by itself.

---

# Windows

Windows may preserve:

- native operation identity;
- multi-source event dependencies;
- process lineage;
- recovery-state context;
- synchronization relationships.

The adapter must maintain:

**platform mechanism**

≠

**adapter capability**

≠

**policy authority**

---

# Linux

Linux may use:

- `preserve_namespace_context`
- `preserve_mount_context`
- source dependency preservation;
- continuity information.

Important Linux boundaries include:

**mount observation ≠ all mounts**

**container observation ≠ host observation**

**namespace observation ≠ global host state**

**privilege ≠ authority**

---

# Android

Android may use:

- `preserve_observation_mode`
- `preserve_provider_context`
- `preserve_synchronization_context`
- `preserve_origin_transport_distinction`

Important Android distinctions include:

**application-visible state ≠ device-wide state**

**provider-backed resource ≠ conventional local path**

**state comparison ≠ directly observed operation**

**user-intervention request ≠ completed response**

---

# iOS / iPadOS

iOS / iPadOS may use:

- `preserve_observation_mode`
- `preserve_synchronization_context`
- `preserve_origin_transport_distinction`
- source dependency preservation.

A particularly important distinction is:

**State at T1**

↓

**State at T2**

↓

**Derived transition**

A derived state change may establish that a transition occurred without establishing:

- every intermediate operation;
- exact transition time;
- responsible actor;
- causal chain.

Those uncertainties must survive normalization.

---

# Cloud / Synchronization

Cloud-sync normalization may preserve:

- origin/transport distinction;
- source dependencies;
- replication relationships;
- propagation relationships;
- version lineage.

Its central boundary is:

**origin**

≠

**transport**

≠

**observation**

≠

**replication**

≠

**propagation**

A transition observed on several synchronized endpoints may still have one originating transition.

---

# Database

Database normalization must preserve the observation layer.

Possible layers include:

- application request;
- transaction;
- logical database mutation;
- database-engine activity;
- underlying storage;
- replication;
- recovery.

The central distinction is:

> **Logical database transition ≠ storage transition**

A logical database mutation must not silently become a filesystem observation.

Likewise, a storage mutation must not automatically become a claim about logical database state.

---

# Cache

Cache normalization preserves the relationship between cached state and authoritative state.

Important distinctions include:

**cache state ≠ source state**

**eviction ≠ destructive deletion**

**expiration ≠ malice**

**invalidation ≠ corruption**

**replication ≠ independent origin**

Cache normalization may also preserve:

- authority relationship;
- expiration context;
- eviction context;
- persistence relationships;
- replication relationships.

A cache transition remains evidence about the cache unless source lineage establishes a broader effect.

---

# Redaction

Normalization may deliberately remove or generalize sensitive information before emitting shared evidence.

Examples include:

- raw filesystem path;
- filename;
- user identity;
- account identity;
- provider-native identifier;
- process arguments;
- database query contents;
- database record contents;
- cache keys;
- cache contents;
- device identity;
- authentication material;
- environment secrets.

The provenance object should record relevant redaction classes.

This distinguishes:

**information deliberately withheld**

from:

**information never observed**.

---

# Credential Boundary

Normalized events and adapter configurations must not require secrets merely for structural analysis.

Shared evidence should not expose:

- passwords;
- API secrets;
- access tokens;
- refresh tokens;
- session secrets;
- private keys;
- provider credentials;
- database connection secrets;
- recovery secrets.

Where identity context is structurally relevant, use a bounded reference rather than authentication material.

---

# Correlation IDs

A correlation identifier may link observations believed to participate in a broader activity.

This can support:

- activity windows;
- transaction relationships;
- cross-adapter correlation;
- process lineage;
- synchronization chains;
- database operations;
- cache replication;
- verification.

A correlation identifier is a relationship aid.

It does not establish that every correlated observation has the same origin or meaning.

---

# Native Event References

`native_event_ref` provides a bridge back toward adapter-local evidence.

The reference may identify:

- platform event;
- provider observation;
- database event;
- cache event;
- local state comparison;
- other retained evidence.

The actual raw evidence may remain within the native privacy and security boundary.

This supports reconstructability without requiring central storage of sensitive native telemetry.

---

# Derivation References

`derivation_refs` identify the methods or intermediate objects used to produce derived structural values.

Examples include:

- resource-classification method;
- baseline-comparison method;
- pseudonymization method;
- event-deduplication method;
- state-comparison method;
- cross-environment correlation method.

Derived values should be reconstructable when they materially affect downstream analysis.

---

# Observation Time vs. Normalization Time

Two times may matter:

**`observed_at`**

When the underlying evidence was recorded.

**`normalized_at`**

When the adapter produced the shared representation.

They may differ.

This becomes important with:

- delayed collection;
- polling;
- synchronization;
- provider events;
- resumed observation;
- offline processing;
- state comparison.

Normalization must not silently replace observation time with processing time.

---

# Observation Continuity

Adapters may operate under different continuity states, such as:

- continuous;
- polling;
- snapshot;
- state comparison;
- resumed;
- delayed;
- gapped;
- unknown.

Continuity affects what downstream analysis may safely infer about:

- rate;
- acceleration;
- persistence;
- reappearance;
- absence of activity.

The invariant is:

> **Observation gap ≠ no activity**

---

# Evidence Independence

Normalization preserves enough lineage for downstream analysis to evaluate whether evidence is genuinely independent.

Examples of dependent observations include:

- one transition seen by multiple endpoint telemetry sources;
- one synchronized transition observed by several devices;
- one database operation represented at logical and storage layers;
- one cache mutation replicated across nodes;
- host and container observations of one underlying resource transition.

Dependency does not make evidence useless.

It changes what the evidence corroborates.

Several dependent observations may strongly corroborate that a transition propagated while providing only one originating event.

---

# Normalization Must Remain Reversible in Reasoning

Normalization does not have to preserve every native field centrally.

It should preserve enough lineage to answer:

- What native evidence produced this shared field?
- Was the field observed or derived?
- Which adapter produced it?
- Which scope applied?
- Which capability declaration applied?
- What information was redacted?
- What remains unresolved?

That is sufficient for analytical reconstruction without demanding unnecessary raw-data centralization.

---

# What Normalization Must Never Assert Automatically

Normalization must not automatically produce:

- `ransomware = true`
- `malicious = true`
- `intent = harmful`
- `attribution = resolved`
- `severity = critical`
- `containment_required = true`
- `recovery_failed = true`
- `incident_resolved = true`

Those claims belong downstream and require the relevant evidence.

A normalized event may contain strong evidence.

It remains an event.

---

# Normalization and Structural Patterns

The handoff is explicit:

**`tf.resource-transition/v0.1`**

records normalized structural evidence.

**`tf.structural-pattern/v0.1`**

records what an analyzer thinks a collection of evidence may mean.

This allows:

**Event A**

+

**Event B**

+

**Event C**

+

**counter-evidence**

+

**unresolved observations**

+

**baseline**

↓

**bounded structural assessment**

without rewriting the original events.

The original evidence remains independently inspectable.

---

# Normalization and Containment

Normalization does not authorize containment.

The chain remains:

**Observation**

↓

**Normalization**

↓

**Pattern**

↓

**Assessment**

↓

**Containment Decision**

↓

**Platform / Service Action**

↓

**Response Outcome**

↓

**Verification**

This preserves another core boundary:

> **Evidence ≠ authority**

---

# Normalization and Verification

Verification may produce new normalized observations.

That means the architecture is cyclic rather than terminal:

**Initial normalized events**

↓

**pattern**

↓

**decision**

↓

**outcome**

↓

**post-response observations**

↓

**normalized events**

↓

**verification**

A verifier therefore relies on the same evidence discipline as the initial detector.

Post-response silence is not automatically resolution.

The observation scope and capability still matter.

---

# Canonical Invariants

## NORM-INV-01 — Native Observation ≠ Normalized Interpretation

Normalization maps evidence into shared structure without assigning a domain verdict.

## NORM-INV-02 — Unknown ≠ False

Unavailable evidence remains explicitly unresolved.

## NORM-INV-03 — Observed Actor ≠ Proven Origin

The locally visible actor may be an origin, intermediary, executor, or transport.

## NORM-INV-04 — Multiple Observations ≠ Independent Events

Source dependencies must remain available for downstream evidence analysis.

## NORM-INV-05 — Derived ≠ Observed

Derived structural properties retain their derivation boundary.

## NORM-INV-06 — Baseline Deviation ≠ Malice

Historical deviation remains evidence rather than intent.

## NORM-INV-07 — Resource Identity ≠ Raw Native Identity

Privacy-preserving structural identity may replace unnecessary native identifying detail.

## NORM-INV-08 — Redacted ≠ Unobserved

Deliberate minimization should remain distinguishable from unavailable evidence.

## NORM-INV-09 — Platform Capability ≠ Adapter Capability

Native platform possibilities do not establish deployment capability.

## NORM-INV-10 — Capability ≠ Authority

Normalization and capability recording do not authorize response.

## NORM-INV-11 — Execution ≠ Resolution

A response outcome requires subsequent verification.

## NORM-INV-12 — Provenance Survives Normalization

Enough lineage must remain to reconstruct the evidence path.

---

# Canonical Normalization Path

The complete normalization path is:

**Native evidence**

↓

**identify observation source**

↓

**establish authorized scope**

↓

**preserve observation mode**

↓

**map actor**

↓

**map resource**

↓

**map operation**

↓

**describe transition**

↓

**preserve unknowns**

↓

**preserve origin / transport**

↓

**preserve source dependencies**

↓

**derive bounded structural fields**

↓

**compare with available baseline**

↓

**record direct consequence**

↓

**minimize sensitive data**

↓

**record redaction**

↓

**retain provenance**

↓

**emit `tf.resource-transition/v0.1`**

Then normalization stops.

---

# Downstream Analytical Path

The next path is separate:

**Normalized transitions**

↓

**CORRELATE**

↓

**DERIVE**

↓

**CONTRADICT**

↓

**ASSESS**

↓

**BOUND**

↓

**`tf.structural-pattern/v0.1`**

If response is justified and authorized:

**`tf.structural-pattern/v0.1`**

↓

**`tf.containment-decision/v0.1`**

↓

**adapter capability + authority boundary**

↓

**native action**

↓

**`tf.response-outcome/v0.1`**

↓

**post-response observation**

↓

**`tf.verification/v0.1`**

---

# Canonical Summary

> **Normalization converts heterogeneous native observations into portable, privacy-conscious, provenance-preserving structural evidence without prejudging what that evidence ultimately means.**

Its representation rule is:

> **Map native evidence into shared vocabulary while preserving enough native lineage to reconstruct the mapping.**

Its uncertainty rule is:

> **Unknown remains unknown.**

Its actor rule is:

> **Observed actor and originating actor remain separate unless evidence connects them.**

Its dependency rule is:

> **Multiple observations remain dependent when they share an originating transition.**

Its privacy rule is:

> **Export structural identity and relationships before exporting native identity or content.**

Its evidence rule is:

> **Derived structure is allowed when derivation is explicit. Domain verdicts are not.**

Its architectural boundary is:

> **Normalization ends at `tf.resource-transition/v0.1`. Interpretation begins downstream.**
