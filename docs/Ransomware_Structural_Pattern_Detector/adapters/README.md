<img width="1194" height="672" alt="Ransomware_Structural_Pattern_Detector_adapters_" src="https://github.com/user-attachments/assets/4a84e91f-6cf3-4340-9975-1a34002126f8" />

# Ransomware Structural Pattern Detector — Adapters

> **Adapters translate native platform, environment, service, and resource observations into the platform-neutral structural contracts used by the Ransomware Structural Pattern Detector.**

Adapters form the boundary between native environments and the Ransomware Structural Pattern Detector.

Their purpose is not to decide whether activity is ransomware.

Their purpose is to:

1. observe what an authorized environment can actually expose;
2. normalize relevant observations into the Shared Structural Event Grammar;
3. preserve provenance, uncertainty, and source dependencies;
4. declare what the concrete adapter can and cannot observe, enforce, recover, or verify;
5. receive separately authorized response requests;
6. execute only supported and authorized actions;
7. record what actually happened;
8. support bounded post-response verification.

The governing rule is:

> **Adapters provide mechanism and evidence. The detector provides bounded interpretation. Policy provides authority. Outcome records execution. Verification establishes resulting state.**

---

# Directory Role

This directory contains the adapter layer for the Ransomware Structural Pattern Detector.

The adapter family now includes:

## Platform Adapters

- Windows
- macOS
- Linux
- Android
- iOS / iPadOS

## Cross-Environment Adapters

- Cloud / Synchronization

## Resource / Service Adapters

- Database
- Cache

These adapters share the same structural grammar while preserving the boundaries unique to their environments.

The architecture deliberately standardizes **semantics without pretending mechanisms are identical**.

---

# Machine-Readable Registry

The adapter family is indexed by:

`detector.json`

This adapter-layer `detector.json` is distinct from:

`../detector.json`

Their responsibilities are different.

**`../detector.json`**

defines the Ransomware Structural Pattern Detector's analytical contract.

It answers:

> **How does RSPD interpret normalized structural evidence?**

**`adapters/detector.json`**

defines the adapter registry and routing contract.

It answers:

> **Which structural boundaries can feed or act for RSPD, and where are their specifications, schemas, examples, and shared contracts?**

The adapter registry groups adapters into:

- `platform`
- `cross_environment`
- `resource_service`

It also records cross-adapter routing and composition relationships.

---

# Artifact Pattern

Most adapters now follow a common three-artifact structure:

**`<adapter>.md`**

↓

**`<adapter>.schema.json`**

↓

**`<adapter>.example.json`**

These artifacts serve different purposes.

## Semantic Specification

`<adapter>.md`

Defines:

- adapter scope;
- native observation model;
- actor semantics;
- resource mappings;
- structural boundaries;
- capability semantics;
- containment boundaries;
- recovery semantics;
- verification boundaries;
- privacy expectations;
- invariants;
- known limitations.

## Configuration Schema

`<adapter>.schema.json`

Defines the machine-readable contract for concrete adapter configuration.

It may validate:

- adapter identity;
- deployment profile;
- observation sources;
- scope;
- normalization behavior;
- platform or service context;
- capability declarations;
- containment mapping;
- recovery mapping;
- verification support;
- privacy settings;
- limitations;
- provenance.

## Example Configuration

`<adapter>.example.json`

Provides a synthetic configuration demonstrating how the adapter schema may be instantiated.

Example configurations are illustrative.

They do not establish the capabilities of a real deployed system.

Where capability has not been established, examples should prefer:

`unknown`

over optimistic assumptions.

---

# Shared Runtime Contracts

Adapter configuration objects are not runtime events.

Runtime interchange uses the Shared Structural Event Grammar.

Canonical contracts include:

- `tf.resource-transition/v0.1`
- `tf.structural-pattern/v0.1`
- `tf.platform-capabilities/v0.1`
- `tf.containment-decision/v0.1`
- `tf.response-outcome/v0.1`
- `tf.verification/v0.1`

The underlying schemas live in:

`../../Shared_Structural_Event_Grammar/`

The roles are:

**`tf.resource-transition/v0.1`**

Normalized structural observation.

**`tf.structural-pattern/v0.1`**

Bounded analytical interpretation produced by the detector.

**`tf.platform-capabilities/v0.1`**

Evidence-backed declaration of adapter/environment capabilities.

**`tf.containment-decision/v0.1`**

Bounded response decision and authority context.

**`tf.response-outcome/v0.1`**

Execution truth: what was actually attempted or executed.

**`tf.verification/v0.1`**

Post-response observed state.

---

# Canonical Runtime Lineage

The shared runtime lineage is:

**Native / Service Observation**

↓

**Adapter**

↓

**Normalize**

↓

**`tf.resource-transition/v0.1`**

↓

**Ransomware Structural Pattern Detector**

↓

**`tf.structural-pattern/v0.1`**

↓

**`tf.containment-decision/v0.1`**

↓

**Adapter**

↓

**Native / Service Mechanism**

↓

**`tf.response-outcome/v0.1`**

↓

**Post-Response Observation**

↓

**`tf.verification/v0.1`**

The adapter participates at both ends of the pipeline without owning the analytical policy between them.

---

# Core Separation of Responsibilities

The architecture deliberately preserves six different questions.

## Observation

> **What did the native environment expose?**

## Normalization

> **How can that evidence be represented through portable structural vocabulary?**

## Interpretation

> **What structural pattern might the evidence collectively support?**

## Decision

> **What response, if any, is justified and authorized?**

## Outcome

> **What action was actually attempted or executed?**

## Verification

> **What state can be established afterward?**

These questions must not silently collapse into one another.

---

# Adapter Responsibilities

Every adapter should address the following responsibilities.

## 1. Establish Scope

Define the environment and observation boundary.

An adapter should identify:

- what resources are in scope;
- what actors may be observable;
- what environments are represented;
- what resource classes are included;
- what authorization boundary applies;
- what is explicitly outside scope.

Observation scope is part of the evidence.

---

## 2. Observe

Identify the native or service-level evidence sources available to the concrete adapter.

Possible evidence may concern:

- resource transitions;
- actors;
- actor lineage;
- resource classes;
- transition timing;
- permissions;
- recovery state;
- network context;
- synchronization context;
- provider context;
- transactions;
- cache state;
- platform state.

An adapter must also document what it cannot observe reliably.

Missing observability remains missing observability.

---

## 3. Normalize

Convert relevant native observations into:

`tf.resource-transition/v0.1`

Normalization should preserve enough information to reconstruct how the shared event was produced without requiring the detector to understand every platform-native API, provider format, database mechanism, or cache implementation.

A normalized object may contain:

- event identity;
- observation time;
- normalized operation;
- native operation;
- actor identity;
- actor role;
- resource identity;
- resource type;
- resource class;
- resource scope;
- structural transition;
- transition characteristics;
- context;
- baseline state;
- direct consequence;
- provenance.

Normalization ends at structural evidence.

It does not produce a ransomware verdict.

---

# Normalization Reference

The cross-adapter normalization rules are documented in:

`normalization_fields.md`

That document defines the common rules for:

- observed vs. derived fields;
- native vs. normalized operations;
- unknown vs. false;
- actor vs. origin;
- source dependencies;
- resource abstraction;
- baseline derivation;
- consequence;
- privacy;
- provenance;
- redaction;
- adapter-specific preservation fields.

The canonical rule is:

> **Normalization ends at `tf.resource-transition/v0.1`. Interpretation begins downstream.**

---

# Native Observation Preservation

Where feasible and permitted, adapters should retain a reference to the native evidence from which a normalized event was produced.

The shared event may preserve:

- source environment;
- adapter identity;
- adapter version;
- observation time;
- normalization time;
- native-event reference;
- capability declaration;
- derivation references;
- redaction classes.

Raw evidence may remain within its native security and privacy boundary.

A centralized detector does not inherently require raw evidence when normalized structure is sufficient.

---

# Observed vs. Derived Fields

An adapter may derive bounded structural properties where the derivation is explicit.

Examples include:

- classifying a native resource;
- mapping a native operation;
- establishing whether a resource lies inside configured scope;
- pseudonymizing resource identity;
- comparing a transition with baseline;
- correlating duplicate observations.

Derived fields should retain lineage where material.

An adapter must never disguise domain interpretation as native evidence.

For example:

**rapid resource modification**

must not silently become:

**ransomware**

during normalization.

---

# Unknown vs. False

Unknown state is first-class.

Examples:

**False**

The adapter has evidence supporting a negative state.

**Unknown**

The adapter cannot establish the state.

**Unavailable**

The required evidence cannot currently be obtained.

**Not applicable**

The structural question does not apply.

The central invariant is:

> **Unknown ≠ False**

Unavailable evidence must not silently become:

- absent;
- safe;
- unsupported;
- resolved.

---

# Actor Mapping

Adapters should represent the actor visible at the observation point without assuming that this actor originated the transition.

Possible actors include:

- process;
- application;
- service;
- script;
- container;
- remote actor;
- synchronization service;
- system;
- user;
- agent;
- database engine;
- cache service;
- unknown actor.

Where available, adapters should preserve:

- parent or invoking actor;
- instance identity;
- execution account;
- origin actor;
- transport actor;
- actor lineage.

The central invariant is:

> **Observed actor ≠ proven origin actor**

---

# Origin and Transport

Origin and transport must remain distinguishable where evidence supports the distinction.

A synchronization service may transport a transition created elsewhere.

A database engine may execute a logical mutation initiated by another application.

A cache service may execute a replicated transition whose origin is another node.

A local process may materialize remote state.

Therefore:

> **Executor ≠ necessarily origin**

and:

> **Transport ≠ origin**

When origin cannot be established, it remains unresolved.

---

# Resource Mapping

Native resources should map into portable structural categories where possible.

Examples include:

- user documents;
- photos;
- video;
- audio;
- databases;
- archives;
- project files;
- application data;
- configuration;
- credential stores;
- backups;
- recovery resources;
- network resources;
- cloud resources;
- cache resources;
- temporary resources;
- canaries;
- domain-defined resources.

The normalized representation should expose the minimum information required for structural analysis.

---

# Transition Mapping

Adapters normalize native operations into structural transitions.

Possible normalized operations include:

- read;
- write;
- create;
- delete;
- rename;
- move;
- truncate;
- copy;
- replace;
- permission change;
- metadata change;
- recovery change;
- state change;
- scope change;
- authority change;
- synchronization;
- execution;
- other.

Possible structural actions include:

- access;
- modify;
- create;
- remove;
- replace;
- relocate;
- duplicate;
- restrict;
- grant;
- revoke;
- expose;
- conceal;
- inject;
- quarantine;
- restore;
- propagate;
- transform;
- other.

Native operation identity may be retained where useful for lineage.

---

# Source Dependency and Deduplication

Several observations may describe one underlying transition.

Examples include:

- several Windows telemetry sources;
- Linux host and container views;
- macOS native and state observations;
- cloud and endpoint synchronization events;
- database logical and storage-layer observations;
- replicated cache-node observations.

Adapters should preserve source dependencies and support bounded deduplication where possible.

Otherwise, duplicate evidence may distort:

- event count;
- rate;
- acceleration;
- resource scope;
- propagation;
- confidence;
- evidence independence.

The invariant is:

> **Multiple observations ≠ multiple independent originating transitions.**

---

# Capability Declaration

Every concrete adapter should provide or generate a declaration conforming to:

`tf.platform-capabilities/v0.1`

Capability families include:

## Observation

- event observation;
- actor identity;
- actor lineage;
- resource classification;
- network context;
- origin/transport distinction;
- baseline access;
- recovery-state observation;
- adapter-specific observation context.

## Enforcement

- write denial;
- actor containment;
- resource isolation;
- network isolation;
- quarantine;
- permission restriction;
- actor disablement;
- session termination;
- adapter-specific bounded enforcement.

## Recovery

- rollback;
- snapshot restoration;
- resource restoration;
- configuration restoration;
- rebuild;
- adapter-specific recovery.

## Verification

- post-action observation;
- state comparison;
- persistence detection;
- reappearance detection;
- recovery verification;
- cross-environment comparison where appropriate.

Capability states are:

- `supported`
- `partial`
- `unsupported`
- `unknown`

The distinction between `unsupported` and `unknown` is significant.

---

# Capability Is Not Authority

A platform or service may technically support an action without the adapter being authorized to perform it.

Therefore:

> **Platform capability ≠ adapter capability**

> **Adapter capability ≠ authority**

> **Authority ≠ execution**

The capability declaration answers:

> **Can this concrete adapter support the mechanism?**

The containment decision answers:

> **Is the response requested and authorized?**

The response outcome answers:

> **What actually happened?**

Verification answers:

> **What state exists afterward?**

---

# Receiving Containment Decisions

An adapter may receive:

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

Receipt of a decision object is not automatically sufficient authority when additional authorization is required.

---

# Response Selection

Where the requested response is supported and authorized:

**Requested response**

↓

**Capability check**

↓

**Authority check**

↓

**Native response mapping**

↓

**Execution attempt**

↓

**Actual outcome**

Where the preferred response is unavailable, an adapter may use a bounded fallback only when permitted.

The fallback must remain visible.

---

# Recording Execution

After response execution or attempted execution, the adapter should produce or contribute to:

`tf.response-outcome/v0.1`

The outcome may preserve:

- requested response;
- whether execution was attempted;
- execution status;
- executed response;
- fallback;
- capability context;
- direct effects;
- side effects;
- errors;
- warnings;
- rollback availability;
- rollback state;
- provenance.

The central invariant is:

> **Requested response ≠ executed response**

---

# Execution Does Not Mean Resolution

A native mechanism reporting success does not establish that the destructive structural condition stopped.

Therefore:

> **Execution ≠ Resolution**

The adapter reports execution through:

`tf.response-outcome/v0.1`

Resolution requires subsequent observation and verification.

---

# Verification

After a response, the adapter should support another bounded observation cycle where capability permits.

Possible verification questions include:

- Did destructive transitions continue?
- Does the actor remain active?
- Did another actor continue the pattern?
- Did propagation continue?
- Did the condition reappear?
- Did new resources become affected?
- Did recovery state change?
- Was restored state verified?
- Is enough of the relevant environment observable?

Verification belongs in:

`tf.verification/v0.1`

Possible results include:

- contained;
- partially contained;
- persistent;
- reappeared;
- resolved;
- partially resolved;
- new condition detected;
- mixed;
- unable to verify.

Verification conclusions must remain bounded to the observed scope.

---

# Recovery

Recovery is distinct from containment.

A concrete adapter may expose:

- rollback;
- snapshots;
- version history;
- preserved originals;
- backup restoration;
- resource restoration;
- configuration restoration;
- provider restoration;
- cache rebuild;
- database recovery;
- other environment-specific mechanisms.

These states must remain separate:

**Recovery mechanism exists**

↓

**Usable recovery state exists**

↓

**Recovery requested**

↓

**Recovery attempted**

↓

**Recovery completed**

↓

**Restored state verified**

The invariant is:

> **Recovery capability ≠ verified restoration**

---

# Data Minimization

Adapters sit closest to potentially sensitive native information.

The default rule is:

> **Normalize structure before exporting content.**

Where sufficient for analysis, expose:

- privacy-preserving resource identifiers;
- resource classes;
- structural scopes;
- transition types;
- timing;
- actor relationships;
- preservation state;
- recovery state;
- baseline relationships;
- environment relationships;
- provenance.

Avoid unnecessary:

- document contents;
- database record contents;
- cache contents;
- raw cache keys;
- plaintext credentials;
- personal filenames;
- full native paths;
- account identities;
- provider tokens;
- device names;
- process arguments containing sensitive data;
- authentication material.

---

# Local Processing

Sensitive native processing should remain local when normalized structure is sufficient.

Candidate local operations include:

- native-event collection;
- path or provider handling;
- resource classification;
- identifier pseudonymization;
- actor correlation;
- baseline comparison;
- deduplication;
- redaction;
- normalization;
- state comparison.

The objective is not to centralize every item of telemetry.

The objective is to export sufficient structural evidence.

---

# Adapter Conformance

An adapter conforms to the architecture when it:

- emits structurally valid normalized observations;
- preserves provenance;
- separates observation from interpretation;
- preserves observed vs. derived distinctions;
- preserves unknown state;
- preserves relevant source dependencies;
- distinguishes origin from transport where evidence allows;
- declares actual capabilities;
- respects authority boundaries;
- does not claim unsupported execution;
- records requested vs. executed responses;
- records fallback honestly;
- distinguishes execution from resolution;
- supports bounded verification where possible;
- reports verification limitations;
- minimizes unnecessary sensitive-data exposure.

Conformance does not require every adapter to support every capability.

> **Honest limitation is preferable to false portability.**

---

# Core Adapter Invariants

## ADAPTER-INV-01 — Native Observation ≠ Domain Verdict

An adapter does not label activity as ransomware merely because it appears suspicious.

## ADAPTER-INV-02 — Actor ≠ Origin

The actor visible at an observation boundary may be an executor, intermediary, or transport.

## ADAPTER-INV-03 — Unknown ≠ False

Unavailable evidence remains unresolved.

## ADAPTER-INV-04 — Capability ≠ Authority

Technical ability to perform an action does not authorize its use.

## ADAPTER-INV-05 — Decision ≠ Execution

A containment decision does not prove that its requested response was performed.

## ADAPTER-INV-06 — Requested Response ≠ Executed Response

Fallback and partial execution remain visible.

## ADAPTER-INV-07 — Execution ≠ Resolution

A successful native operation does not prove that the structural condition resolved.

## ADAPTER-INV-08 — Recovery Capability ≠ Recovery Success

Availability of recovery does not establish successful restoration.

## ADAPTER-INV-09 — Correlation ≠ Independence

Multiple observations of one originating transition do not automatically constitute independent evidence.

## ADAPTER-INV-10 — Provenance Survives Normalization

Enough lineage must remain to reconstruct how normalized evidence was produced.

## ADAPTER-INV-11 — Privacy Survives Portability

Normalization exposes only the information required for structural analysis.

## ADAPTER-INV-12 — Limitation Is Valid Output

Unable-to-observe, unable-to-act, and unable-to-verify states are valid architectural outcomes.

## ADAPTER-INV-13 — Derived ≠ Observed

Derived structural fields remain distinguishable from native observations.

## ADAPTER-INV-14 — Bounded Verification ≠ Global Resolution

A clean result inside one observation scope does not establish state outside that scope.

---

# Platform Adapters

## Windows

Windows adapter artifacts:

- `windows.md`
- `windows.schema.json`
- `windows.example.json`

Configuration schema:

`tf.rspd-adapter.windows/v0.1`

Windows preserves boundaries involving:

- platform capability vs. adapter capability;
- actor identity vs. intent;
- multi-source event dependency;
- recovery context;
- local observation vs. remote origin.

Artifact lineage:

**`windows.md`**

↓

**`windows.schema.json`**

↓

**`windows.example.json`**

↓

**Shared Structural Event Grammar**

---

## macOS

macOS adapter artifacts:

- `macos.md`
- `macos.schema.json`
- `macos.example.json`
- `macos.endpoint-security.example.json`
- `macos.normalized.event.md`
- `macos.normalized.event.example.json`

Configuration schema:

`tf.rspd-adapter.macos/v0.1`

macOS preserves boundaries involving:

- notification vs. authorization;
- authorization opportunity vs. policy authority;
- platform capability vs. adapter capability;
- actor identity and trust vs. behavioral safety;
- local observation vs. remote origin.

The generic example demonstrates a synthetic adapter configuration.

The Endpoint Security example demonstrates a stronger illustrative deployment profile.

The normalized-event files demonstrate the transition from native evidence into:

`tf.resource-transition/v0.1`

Artifact lineage:

**`macos.md`**

↓

**`macos.schema.json`**

↓

**`macos.example.json`**

or:

**`macos.endpoint-security.example.json`**

↓

**normalized event**

↓

**Shared Structural Event Grammar**

---

## Linux

Linux adapter artifacts:

- `linux.md`
- `linux.schema.json`
- `linux.example.json`

Configuration schema:

`tf.rspd-adapter.linux/v0.1`

Linux preserves structural boundaries involving:

- mount scope;
- namespace scope;
- container vs. host;
- privilege vs. authority;
- remote storage;
- observation continuity.

A bounded user-space observer, privileged host observer, container-scoped observer, and host-side container observer may all participate in the same grammar while declaring different capabilities.

Artifact lineage:

**`linux.md`**

↓

**`linux.schema.json`**

↓

**`linux.example.json`**

↓

**Shared Structural Event Grammar**

---

## Android

Android adapter artifacts:

- `android.md`
- `android.schema.json`
- `android.example.json`

Configuration schema:

`tf.rspd-adapter.android/v0.1`

Android preserves boundaries involving:

- application scope vs. device scope;
- resource authorization;
- application storage;
- user-selected resources;
- shared resources;
- provider-backed resources;
- direct observation vs. derived state comparison;
- user-mediated response;
- local observation vs. remote origin.

The generic Android adapter must not convert bounded application-visible evidence into device-wide claims.

Artifact lineage:

**`android.md`**

↓

**`android.schema.json`**

↓

**`android.example.json`**

↓

**Shared Structural Event Grammar**

---

## iOS / iPadOS

iOS / iPadOS adapter artifacts:

- `ios-ipados.md`
- `ios-ipados.schema.json`
- `ios-ipados.example.json`

Configuration schema:

`tf.rspd-adapter.ios-ipados/v0.1`

The adapter preserves boundaries involving:

- application scope vs. device scope;
- resource authorization;
- direct observation vs. state comparison;
- user-mediated response;
- local verification vs. device-wide verification;
- local observation vs. remote origin.

A state comparison may establish that:

**State at T1 ≠ State at T2**

without establishing:

- every intermediate operation;
- exact transition time;
- responsible actor;
- causal chain.

Artifact lineage:

**`ios-ipados.md`**

↓

**`ios-ipados.schema.json`**

↓

**`ios-ipados.example.json`**

↓

**Shared Structural Event Grammar**

---

# Cross-Environment Adapter

## Cloud / Synchronization

Cloud / Synchronization adapter artifacts:

- `cloud-sync.md`
- `cloud-sync.schema.json`
- `cloud-sync.example.json`

Configuration schema:

`tf.rspd-adapter.cloud-sync/v0.1`

This adapter preserves:

- origin;
- transport;
- observation;
- replication;
- propagation;
- environment relationships;
- resource lineage;
- evidence dependencies;
- response scope;
- cross-environment verification.

Its central invariant is:

> **Origin, transport, observation, replication, and propagation are different structural roles.**

A transition observed on several synchronized endpoints may remain one originating transition.

Artifact lineage:

**`cloud-sync.md`**

↓

**`cloud-sync.schema.json`**

↓

**`cloud-sync.example.json`**

↓

**Shared Structural Event Grammar**

---

# Resource / Service Adapters

## Database

Database adapter artifacts:

- `database.md`
- `database.schema.json`
- `database.example.json`

Configuration schema:

`tf.rspd-adapter.database/v0.1`

The Database adapter preserves boundaries among:

- application request;
- transaction;
- logical mutation;
- database engine;
- underlying storage;
- replication;
- recovery.

Its central rule is:

> **Logical database transition ≠ storage transition**

Database-layer and operating-system-layer observations may be correlated while preserving their distinct provenance.

Artifact lineage:

**`database.md`**

↓

**`database.schema.json`**

↓

**`database.example.json`**

↓

**Shared Structural Event Grammar**

---

## Cache

Cache adapter artifacts:

- `cache.md`
- `cache.schema.json`
- `cache.example.json`

Configuration schema:

`tf.rspd-adapter.cache/v0.1`

The Cache adapter preserves boundaries among:

- cached state;
- authoritative source state;
- expiration;
- eviction;
- invalidation;
- persistence;
- replication;
- recovery.

Its central rules include:

> **Cache state ≠ source state**

> **Eviction ≠ destructive deletion**

> **Expiration ≠ malice**

> **Invalidation ≠ corruption**

Cache and source adapters may correlate their observations while preserving distinct evidence layers.

Artifact lineage:

**`cache.md`**

↓

**`cache.schema.json`**

↓

**`cache.example.json`**

↓

**Shared Structural Event Grammar**

---

# Cross-Adapter Composition

Complex environments may require more than one adapter.

The architecture permits cross-adapter correlation while requiring provenance and dependency preservation.

Examples include:

## Windows + Cloud / Synchronization

**Windows-local transition**

+

**cloud transport evidence**

↓

**cross-environment lineage**

## macOS + Cloud / Synchronization

**macOS-local actor/resource evidence**

+

**remote synchronization lineage**

↓

**bounded origin/transport reconstruction**

## Android + Cloud / Synchronization

**Android-visible provider resource**

+

**cloud synchronization evidence**

↓

**device-side observation separated from remote origin**

## iOS/iPadOS + Cloud / Synchronization

**bounded device-side state**

+

**cross-environment evidence**

↓

**transport and propagation correlation**

## Database + Linux

**logical database transition**

+

**Linux storage or process evidence**

↓

**correlated multi-layer transition**

## Database + Windows

**database-layer observation**

+

**Windows resource or actor observation**

↓

**cross-layer evidence without semantic collapse**

## Cache + Database

**cache mutation**

+

**authoritative database state**

↓

**cache/source relationship**

Neither adapter is required to impersonate the other.

---

# Cross-Adapter Correlation Rules

Cross-adapter correlation should:

- preserve source adapter;
- preserve source evidence;
- preserve derivation lineage;
- preserve observation scope;
- preserve capability boundaries;
- preserve origin/transport relationships;
- preserve source dependencies;
- avoid duplicate-event inflation;
- avoid false evidence independence;
- retain unresolved relationships.

The key rule is:

> **Correlate evidence across boundaries without erasing the boundaries that made the evidence meaningful.**

---

# Adapter Configuration Is Not Capability Evidence by Itself

Adapter configuration describes a declared implementation.

A generic example does not establish real-world support.

Likewise, the existence of a schema field does not establish that the environment supports that capability.

For example:

`write_denial`

appearing in an adapter schema means:

> This capability can be represented.

It does not mean:

> This adapter supports write denial.

The concrete capability declaration remains authoritative.

---

# Examples Are Synthetic Unless Explicitly Established Otherwise

Files named:

`*.example.json`

are intended as synthetic configuration or event examples unless explicitly documented otherwise.

Their purpose is to support:

- schema understanding;
- conformance testing;
- teaching;
- AI inspection;
- implementation scaffolding.

They must not be interpreted as observations from a real device or deployment.

---

# Validation Direction

The adapter family is structured so validation can proceed in several distinct layers.

## Configuration Validation

**Adapter example**

↓

**Adapter schema**

For example:

`android.example.json`

↓

`android.schema.json`

## Runtime Event Validation

**Normalized event**

↓

**Shared Structural Event Grammar schema**

For example:

`macos.normalized.event.example.json`

↓

`resource-transition.schema.json`

## Analytical Lineage Validation

Runtime examples may later validate the complete chain:

**Resource Transition**

↓

**Structural Pattern**

↓

**Containment Decision**

↓

**Response Outcome**

↓

**Verification**

This keeps configuration validation separate from runtime evidence validation.

---

# Errors and Uncertainty

Adapters should fail transparently.

Relevant uncertainty states include:

- native source unavailable;
- observation gap;
- event loss possible;
- actor identity incomplete;
- actor lineage unavailable;
- resource classification incomplete;
- provider context incomplete;
- origin unresolved;
- transport unresolved;
- evidence dependency unresolved;
- recovery state unknown;
- enforcement capability unknown;
- authorization unavailable;
- execution partial;
- verification incomplete;
- cross-environment state unresolved.

These states are legitimate output.

They are not errors to hide behind stronger claims.

---

# Non-Goals

The adapter layer is not:

- the ransomware detector;
- a malware classifier;
- an attribution engine;
- a threat-intelligence service;
- an independent authorization engine;
- a universal platform abstraction hiding real capability differences;
- proof that every environment supports equivalent containment;
- proof that a response executed;
- proof that executed containment resolved the condition;
- proof that recovery succeeded;
- a reason to centralize sensitive native data.

Its role is narrower:

> **Observe faithfully, normalize minimally, preserve lineage, declare capability honestly, act only within authority, record what actually occurred, and support bounded verification.**

---

# Canonical Adapter Architecture

The complete adapter architecture is:

**Native / Service / Resource Evidence**

↓

**ADAPTER**

↓

**NORMALIZE**

↓

**PRESERVE LINEAGE**

↓

**MINIMIZE SENSITIVE DATA**

↓

**`tf.resource-transition/v0.1`**

↓

**DETECTOR**

↓

**`tf.structural-pattern/v0.1`**

↓

**POLICY / AUTHORITY**

↓

**`tf.containment-decision/v0.1`**

↓

**ADAPTER**

↓

**NATIVE / SERVICE RESPONSE**

↓

**`tf.response-outcome/v0.1`**

↓

**POST-RESPONSE OBSERVATION**

↓

**`tf.verification/v0.1`**

---

# Canonical Summary

> **A Ransomware Structural Pattern Detector adapter translates between native environments and the platform-neutral Shared Structural Event Grammar without taking ownership of ransomware interpretation or response policy.**

Its observation path is:

**OBSERVE → NORMALIZE → PRESERVE LINEAGE → MINIMIZE → EMIT**

Its response path is:

**RECEIVE → CHECK CAPABILITY → CHECK AUTHORITY → MAP → ACT → RECORD**

Its verification path is:

**RESCAN → COMPARE → PRESERVE LIMITATIONS → REPORT**

Its composition rule is:

> **Different adapters may observe different layers of the same structural event. Correlate those observations without flattening their provenance or inventing evidence independence.**

Its capability rule is:

> **A representable capability is not necessarily an available capability, and an available capability is not necessarily an authorized action.**

Its evidence rule is:

> **Observation is evidence. Normalization makes that evidence portable. Interpretation remains downstream.**

And its architectural boundary is:

> **The adapter knows how its environment exposes and acts on state. The detector interprets structural behavior. Policy determines authority. The outcome records execution. Verification determines what state can actually be established afterward.**
