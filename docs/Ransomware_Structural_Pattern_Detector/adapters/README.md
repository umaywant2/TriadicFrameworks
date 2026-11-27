<img width="1194" height="672" alt="Ransomware_Structural_Pattern_Detector_adapters_" src="https://github.com/user-attachments/assets/4a84e91f-6cf3-4340-9975-1a34002126f8" />

# Ransomware Structural Pattern Detector — Platform Adapters

> **Platform adapters translate native observations and enforcement mechanisms into the platform-neutral structural contracts used by the Ransomware Structural Pattern Detector.**

Adapters form the boundary between operating environments and the detector.

Their purpose is not to decide whether activity is ransomware.

Their purpose is to:

1. observe what the platform can actually expose;
2. normalize relevant observations into the Shared Structural Event Grammar;
3. declare what the platform can and cannot observe or enforce;
4. receive separately authorized response requests;
5. execute only supported and authorized actions;
6. record what actually happened;
7. support post-response verification.

The governing rule is:

> **Adapters provide mechanism and evidence. The detector provides bounded interpretation. Policy provides authority.**

---

## Directory Role

This directory contains platform-specific adapter specifications for the Ransomware Structural Pattern Detector.

Current scaffold:

- `windows.md`
- `macos.md`
- `linux.md`
- `android.md`
- `ios-ipados.md`
- `cloud-sync.md`

Each adapter documents how a particular environment maps native observations and available mechanisms into the shared structural model.

The adapter specifications are intentionally separated from `detector.json`.

`detector.json` defines ransomware-relevant analytical semantics.

The files in this directory define platform-specific observation and response boundaries.

---

# Architectural Position

The adapter participates at both ends of the structural pipeline.

## Observation Path

**Native Platform Event**

↓

**Platform Adapter**

↓

**Normalize**

↓

**`tf.resource-transition/v0.1`**

↓

**Ransomware Structural Pattern Detector**

↓

**`tf.structural-pattern/v0.1`**

## Response Path

**`tf.structural-pattern/v0.1`**

↓

**`tf.containment-decision/v0.1`**

↓

**Platform Adapter**

↓

**Native Platform Mechanism**

↓

**`tf.response-outcome/v0.1`**

↓

**Post-Response Observation**

↓

**`tf.verification/v0.1`**

The adapter therefore translates in both directions without owning the analytical policy between them.

---

# Adapter Responsibilities

Every adapter should address seven responsibilities.

## 1. Observe

Identify the native event sources available in the environment.

An adapter should document what it can observe about:

- resource transitions;
- actors;
- actor lineage;
- resource classes;
- transition timing;
- permissions;
- recovery state;
- network context;
- synchronization context;
- relevant platform state.

An adapter must also document what it **cannot** observe reliably.

Missing observability must remain missing observability.

It must not be filled with assumptions.

---

## 2. Normalize

Convert relevant native observations into:

`tf.resource-transition/v0.1`

Normalization should preserve enough information to reconstruct how the shared event was produced without requiring the detector to understand every native platform API or telemetry format.

The normalized object may include:

- event identity and time;
- normalized operation;
- actor identity;
- actor role;
- resource identity;
- resource class;
- resource scope;
- structural transition;
- transition characteristics;
- context;
- baseline information;
- direct consequence;
- provenance.

Normalization must preserve the distinction between:

**native observation**

and

**derived structural property**

and

**domain interpretation**

The adapter owns the first two only where derivation is explicitly documented.

It must not silently produce a ransomware verdict.

---

# Native Event Preservation

Where feasible and permitted, the adapter should retain a reference to the native observation from which a normalized event was produced.

The shared event should preserve:

- source platform;
- adapter identity;
- adapter version;
- observation time;
- normalization time;
- native-event reference when available;
- derivation references;
- redactions;
- relevant platform-capability declaration.

Raw evidence may remain within the native platform's security and privacy boundary.

A centralized detector does not inherently require the native event itself when its normalized structural representation is sufficient.

---

# Actor Mapping

Adapters should represent the actor visible at the observation point without assuming that the visible actor originated the transition.

Relevant mappings may include:

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
- unknown actor.

Where available, an adapter should preserve:

- parent or invoking actor;
- instance identity;
- execution account;
- origin actor;
- transport actor;
- actor lineage.

The central rule is:

> **Observed actor ≠ proven origin actor**

This is particularly important for distributed, synchronized, remote, automated, and intermediary services.

---

# Origin and Transport

An adapter should preserve the distinction between **origin** and **transport** whenever the platform provides sufficient evidence.

For example, an adapter may observe that a synchronization service performed a local resource modification.

That observation establishes the local transport mechanism.

It does not automatically establish where the destructive transition originated.

When origin cannot be established, the adapter should represent it as unresolved.

It should not substitute the transport actor for the origin merely because the transport actor is locally observable.

---

# Resource Mapping

Platform-native resources should be normalized into reusable structural categories where possible.

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
- temporary resources;
- canaries;
- domain-defined resources.

The normalized representation should expose the minimum information required for structural analysis.

A detector may need to know that a resource is:

**a protected user document**

rather than:

**the exact full pathname and personally identifying filename of that document**

when the latter contributes nothing to the analysis.

---

# Transition Mapping

Adapters normalize native operations into structural transitions.

The native mechanism may report operations such as:

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
- synchronization.

The shared representation describes their structural consequence where evidence permits.

Examples include:

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
- restore;
- propagate;
- transform.

Adapters should preserve the native operation when useful for diagnostic lineage.

---

# Observed vs. Derived Fields

An adapter may derive structural properties from native evidence when the derivation is deterministic or otherwise explicitly documented.

Examples might include:

- classifying a native resource into a shared resource class;
- determining whether a pathname falls inside an authorized observation scope;
- mapping a native operation to a shared transition;
- correlating a native process identifier with available parent-process information.

Derived fields must retain their derivation lineage where practical.

An adapter must not disguise a domain inference as a native observation.

In particular, the adapter should not turn:

**rapid resource modification**

into:

**ransomware**

during normalization.

That determination belongs to the detector.

---

# Capability Declaration

Every adapter should provide or generate a declaration conforming to:

`tf.platform-capabilities/v0.1`

The declaration describes what the current adapter/environment can support.

Capability families include:

## Observation

- event observation;
- actor identity;
- actor lineage;
- resource classification;
- network context;
- origin/transport distinction;
- baseline access;
- recovery-state observation.

## Enforcement

- write denial;
- actor containment;
- resource isolation;
- network isolation;
- quarantine;
- permission restriction;
- actor disablement;
- session termination.

## Recovery

- rollback;
- snapshot restoration;
- resource restoration;
- configuration restoration.

## Verification

- post-action observation;
- state comparison;
- persistence detection;
- reappearance detection;
- recovery verification.

Each capability should be represented honestly as:

- `supported`
- `partial`
- `unsupported`
- `unknown`

The distinction between `unsupported` and `unknown` matters.

An adapter must not advertise a capability simply because the underlying platform may expose some mechanism that appears related.

---

# Capability Is Not Authority

A platform may be technically capable of performing an action without the detector or adapter being authorized to perform it.

Therefore:

> **Capability ≠ Authority**

The capability declaration answers:

> **Can this adapter/environment support the mechanism?**

The containment decision answers:

> **Is the response requested, and under what authority?**

The response outcome answers:

> **What did the adapter actually do?**

These questions must remain separate.

---

# Receiving Containment Decisions

An adapter may receive a:

`tf.containment-decision/v0.1`

The adapter should evaluate:

- requested action;
- target;
- scope;
- required capability;
- declared platform capability;
- authorization;
- constraints;
- reversibility expectations;
- whether fallback is permitted.

The adapter must not treat receipt of a decision object as sufficient authority when that decision explicitly requires additional authorization.

---

# Response Selection

When the requested response is supported and authorized, an adapter may map the shared response onto an appropriate native mechanism.

When the exact response is unavailable, the adapter must not pretend otherwise.

If fallback is allowed, it may select a bounded supported alternative and record the difference.

Conceptually:

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

The adapter should prefer the smallest mechanism sufficient to implement the authorized structural response.

---

# Fallback

Platform differences make fallback a first-class part of the adapter contract.

A requested response may be:

- fully supported;
- partially supported;
- unsupported;
- blocked by authorization;
- constrained by platform policy;
- replaced with a weaker supported action;
- referred for manual intervention.

If fallback occurs, the adapter should preserve:

- requested action;
- executed or attempted fallback;
- reason for fallback;
- degree of degradation;
- capability limitation.

A weaker response must never be recorded as though the original stronger response was performed.

---

# Recording Execution

After attempting a response, the adapter should produce or contribute to:

`tf.response-outcome/v0.1`

The outcome records execution truth.

It may preserve:

- requested response;
- whether execution was attempted;
- execution status;
- executed response;
- fallback;
- relevant capability context;
- direct effects;
- side effects;
- errors;
- warnings;
- rollback availability;
- rollback status;
- provenance.

The adapter must report failure, partial execution, unsupported behavior, and authorization boundaries honestly.

---

# Execution Does Not Mean Resolution

A successfully invoked platform mechanism does not prove that the destructive condition has stopped.

For example:

**Native mechanism returned success**

does not imply:

**Structural pattern resolved**

Therefore:

> **Execution ≠ Resolution**

The adapter reports execution through `tf.response-outcome/v0.1`.

Resolution belongs to post-response verification.

---

# Verification Support

After a response, the adapter should support another bounded observation cycle where its declared capabilities allow.

That may include observing whether:

- destructive transitions continue;
- the affected actor remains active;
- writes resume;
- propagation continues;
- the pattern reappears;
- new resources become affected;
- recovery state changes;
- restoration is observable.

Verification results belong in:

`tf.verification/v0.1`

Possible resulting states include:

- contained;
- partially contained;
- persistent;
- reappeared;
- resolved;
- partially resolved;
- new condition detected;
- mixed;
- unable to verify.

If the adapter cannot observe enough of the resulting state, it must preserve that limitation.

---

# Recovery

Recovery mechanisms are platform-specific.

An adapter may expose capabilities related to:

- rollback;
- snapshots;
- version history;
- preserved originals;
- backup restoration;
- resource restoration;
- configuration restoration;
- other native recovery facilities.

A recovery capability means only that a mechanism is available.

It does not prove:

- that a valid recovery point exists;
- that the recovery point is unaffected;
- that restoration was attempted;
- that restoration succeeded;
- that the resulting resource is correct.

Those distinctions belong in outcome and verification records.

---

# Data Minimization

Adapters sit closest to potentially sensitive native data and therefore carry an important privacy responsibility.

The default rule is:

> **Normalize structure before exporting content.**

Where sufficient for analysis, export:

- privacy-preserving resource identifiers;
- resource classes;
- structural scopes;
- transition types;
- timing;
- actor relationships;
- preservation state;
- recovery state;
- baseline relationships;
- platform provenance.

Avoid exporting unnecessary:

- document contents;
- plaintext credentials;
- personally identifying filenames;
- full local paths;
- unrelated account information;
- unrelated process arguments;
- user content.

If sensitive information is removed or generalized during normalization, the event provenance should record the relevant redaction class.

---

# Local Processing

Some adapter operations may be best performed locally.

Examples include:

- native-event collection;
- sensitive path handling;
- resource classification;
- identifier pseudonymization;
- deduplication;
- redaction;
- mapping native operations into shared transitions.

The objective is not to centralize every piece of telemetry.

The objective is to provide enough normalized structure for the detector to reason reliably while preserving platform and privacy boundaries.

---

# Event Deduplication

Adapters should minimize duplicate representations of the same native transition.

Duplicate observations can otherwise distort:

- event counts;
- activity rates;
- acceleration;
- affected-resource scope;
- evidence independence.

Where multiple telemetry sources observe the same underlying transition, the adapter should preserve their provenance without automatically presenting them as separate independent transitions.

---

# Synchronized Environments

Synchronization requires special care.

A local adapter may observe real destructive resource changes that originated somewhere else.

The adapter should preserve, where available:

- synchronization state;
- transport actor;
- origin-environment reference;
- resource lineage;
- propagation context.

It should not assume:

**local modification = local origin**

Nor should it assume:

**trusted synchronization mechanism = benign transported transition**

The `cloud-sync.md` adapter specification exists specifically to document these cross-environment concerns.

---

# Errors and Uncertainty

Adapters should fail transparently.

Relevant uncertainty states include:

- native source unavailable;
- event loss possible;
- actor identity incomplete;
- actor lineage unavailable;
- resource classification incomplete;
- origin unresolved;
- recovery state unknown;
- enforcement capability partial;
- authorization unavailable;
- verification incomplete.

The correct representation of unavailable evidence is usually:

**unknown**

not:

**false**

and not:

**safe**

---

# Adapter Specification Template

Each platform adapter document should cover the same conceptual areas.

## 1. Scope

Define the environment and adapter boundary.

## 2. Native Observation Sources

Describe the classes of platform evidence available to the adapter.

## 3. Resource Mapping

Map platform-native resources into shared resource types and classes.

## 4. Actor Mapping

Describe actor identity, lineage, origin, and transport semantics.

## 5. Transition Mapping

Map native operations into `tf.resource-transition/v0.1`.

## 6. Capability Declaration

Document supported, partial, unsupported, and unknown capabilities.

## 7. Containment Mapping

Describe how authorized structural responses map onto supported native mechanisms.

## 8. Fallback Behavior

Describe bounded alternatives when the preferred response is unavailable.

## 9. Outcome Reporting

Define how execution results map into `tf.response-outcome/v0.1`.

## 10. Verification

Describe which resulting states can be observed after intervention.

## 11. Recovery

Describe available recovery mechanisms and their evidentiary limits.

## 12. Privacy and Redaction

Document what remains local, what is normalized, and what may be removed or generalized.

## 13. Known Limitations

Explicitly record observational, enforcement, recovery, and verification gaps.

---

# Adapter Conformance

An adapter conforms to this architecture when it:

- emits structurally valid normalized observations;
- preserves observation provenance;
- separates observation from inference;
- declares actual capabilities;
- preserves unknown states;
- distinguishes origin from transport when evidence allows;
- respects authorization boundaries;
- does not execute unsupported actions;
- records requested versus executed responses;
- records fallback honestly;
- distinguishes execution from resolution;
- supports verification where possible;
- states verification limitations where not possible;
- minimizes unnecessary sensitive data exposure.

Conformance does **not** require every platform to provide every capability.

Honest limitation is preferable to false portability.

---

# Core Adapter Invariants

## ADAPTER-INV-01 — Native Observation ≠ Domain Verdict

An adapter does not label activity as ransomware merely because it appears suspicious.

## ADAPTER-INV-02 — Actor ≠ Origin

The actor visible in the local event may be a transport or intermediary.

## ADAPTER-INV-03 — Unknown ≠ False

Unavailable evidence remains unresolved.

## ADAPTER-INV-04 — Capability ≠ Authority

Technical ability to perform an action does not authorize its use.

## ADAPTER-INV-05 — Decision ≠ Execution

Receiving a containment decision does not prove that its requested response was performed.

## ADAPTER-INV-06 — Requested Response ≠ Executed Response

Fallback or partial execution must remain visible.

## ADAPTER-INV-07 — Execution ≠ Resolution

A successful native operation does not prove that the structural condition has been resolved.

## ADAPTER-INV-08 — Recovery Capability ≠ Recovery Success

Availability of a recovery mechanism does not establish successful restoration.

## ADAPTER-INV-09 — Correlation ≠ Independence

Multiple observations of the same originating transition must not silently become independent evidence.

## ADAPTER-INV-10 — Provenance Survives Normalization

Enough lineage must remain to reconstruct how the normalized observation was produced.

## ADAPTER-INV-11 — Privacy Survives Portability

Normalization should expose only the information required for structural analysis.

## ADAPTER-INV-12 — Limitation Is Valid Output

An adapter may explicitly state that an observation, action, or verification result cannot be produced reliably.

---

# Platform Adapter Files

## Windows

`windows.md`

Defines the Windows-specific observation, normalization, capability, containment, recovery, and verification boundary.

## macOS

`macos.md`

Defines the macOS-specific boundary.

## Linux

`linux.md`

Defines the Linux-specific boundary while accounting for variation among distributions and deployment environments.

## Android

`android.md`

Defines the Android-specific boundary, including constraints imposed by the mobile application and permission model.

## iOS / iPadOS

`ios-ipados.md`

Defines the iOS and iPadOS boundary and explicitly records capabilities unavailable to the adapter.

## Cloud / Synchronization

`cloud-sync.md`

Defines cross-environment and synchronization-specific mappings, especially the distinction between origin and transport actors.

---

# Shared Contracts

Adapters operate against the following Shared Structural Event Grammar contracts:

- `tf.resource-transition/v0.1`
- `tf.platform-capabilities/v0.1`
- `tf.containment-decision/v0.1`
- `tf.response-outcome/v0.1`
- `tf.verification/v0.1`

The detector additionally produces:

- `tf.structural-pattern/v0.1`

Adapters should consume the shared contracts rather than inventing platform-specific replacements for their semantics.

Native platform details remain local to the adapter layer.

---

# Non-Goals

The adapter layer is not:

- the ransomware detector;
- a malware classifier;
- an attribution system;
- a threat-intelligence service;
- an independent authorization engine;
- a universal platform abstraction that hides real capability differences;
- proof that every platform supports equivalent containment;
- proof that an executed action resolved an incident.

Its role is narrower:

> **Observe faithfully, normalize minimally, declare capabilities honestly, act only within authority, report what actually occurred, and support verification.**

---

# Canonical Summary

> **A Ransomware Structural Pattern Detector adapter translates between native platform observations and mechanisms and the platform-neutral Shared Structural Event Grammar without taking ownership of ransomware interpretation or response policy.**

Its observation path is:

**OBSERVE → NORMALIZE → PRESERVE LINEAGE → EMIT**

Its response path is:

**RECEIVE → CHECK CAPABILITY → CHECK AUTHORITY → MAP → ACT → RECORD**

Its verification path is:

**RESCAN → COMPARE → REPORT**

And its architectural boundary is:

> **The adapter knows how the platform works.  
> The detector interprets structural behavior.  
> Policy determines what is authorized.  
> The outcome records what actually happened.  
> Verification determines what state exists afterward.**
