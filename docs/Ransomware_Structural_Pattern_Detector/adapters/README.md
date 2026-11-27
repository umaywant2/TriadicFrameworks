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

Windows adapter artifacts:

- `windows.md` — human-readable platform specification defining the Windows observation, normalization, capability, containment, recovery, privacy, and verification boundaries.
- `windows.schema.json` — machine-readable JSON Schema for validating concrete Windows adapter configurations.
- `windows.example.json` — synthetic example configuration demonstrating a conservative Windows endpoint-observation profile.

The Windows adapter follows the same separation used throughout the adapter architecture:

**`windows.md` → semantic specification**

**`windows.schema.json` → adapter configuration contract**

**`windows.example.json` → synthetic conforming instance**

**Shared Structural Event Grammar → runtime interchange contracts**

The example configuration is intentionally illustrative rather than a declaration of Windows platform capability.

A concrete implementation must replace example and `unknown` capability states with evidence-backed declarations appropriate to its actual deployment, observation sources, authorization, and scope.

In particular:

- platform capability does not automatically establish adapter capability;
- adapter capability does not establish authority to act;
- observation does not establish ransomware;
- a requested containment response does not establish execution;
- successful execution does not establish resolution;
- recovery capability does not establish successful restoration;
- bounded endpoint observation must not be promoted into claims about unobserved local, remote, or synchronized state.

The Windows configuration layer therefore describes **what a particular adapter deployment claims it can observe, normalize, enforce, recover, and verify**, while the Shared Structural Event Grammar remains responsible for the portable runtime objects exchanged across the analytical pipeline.

Canonical runtime lineage:

**`tf.resource-transition/v0.1`**

↓

**`tf.structural-pattern/v0.1`**

↓

**`tf.containment-decision/v0.1`**

↓

**`tf.response-outcome/v0.1`**

↓

**`tf.verification/v0.1`**

with:

**`tf.platform-capabilities/v0.1`**

declaring the capabilities available to the concrete adapter environment.

The architectural rule is:

> **Windows provides the environment. The adapter configuration declares the implementation. The shared grammar carries the evidence. The detector interprets the structure. Policy determines authority. Outcome records execution. Verification determines resulting state.**

## macOS

macOS adapter artifact:

- `macos.md` — human-readable platform specification defining the macOS observation, normalization, capability, containment, recovery, privacy, and verification boundaries.

The macOS adapter follows the same architectural separation used throughout the adapter family:

**`macos.md` → semantic specification**

**Adapter configuration → concrete implementation declaration**

**Shared Structural Event Grammar → runtime interchange contracts**

The macOS specification intentionally does not treat the existence of a platform mechanism as proof that a particular adapter implementation possesses or is authorized to use that capability.

A concrete implementation must provide evidence-backed declarations appropriate to its actual deployment, observation sources, authorization, and scope.

In particular:

- platform capability does not automatically establish adapter capability;
- adapter capability does not establish authority to act;
- notification and authorization opportunities have different structural meanings;
- observation does not establish ransomware;
- actor identity or trust does not establish benign intent;
- a requested containment response does not establish execution;
- successful execution does not establish resolution;
- recovery capability does not establish successful restoration;
- bounded local observation must not be promoted into claims about unobserved local, remote, or synchronized state.

The macOS adapter may accommodate different deployment profiles, ranging from bounded application or resource observation to appropriately configured endpoint-security implementations. Those profiles describe possible architectural positions rather than guaranteed capabilities.

The concrete capability declaration remains authoritative for what the deployed adapter can actually:

- observe;
- identify;
- correlate;
- deny or restrict;
- isolate;
- recover;
- rescan;
- verify.

Canonical runtime lineage:

**`tf.resource-transition/v0.1`**

↓

**`tf.structural-pattern/v0.1`**

↓

**`tf.containment-decision/v0.1`**

↓

**`tf.response-outcome/v0.1`**

↓

**`tf.verification/v0.1`**

with:

**`tf.platform-capabilities/v0.1`**

declaring the capabilities available to the concrete adapter environment.

The macOS-specific architectural boundary is:

> **A native event reports evidence available through the deployed observation mechanism. An authorization opportunity provides a bounded point at which a supported operation may potentially be allowed or denied. Neither determines the structural interpretation or policy decision by itself.**

This preserves four separate questions:

**What did macOS expose?**

↓

**What structural transition does that evidence support?**

↓

**What response, if any, is authorized?**

↓

**What state exists after the response?**

The architectural rule is:

> **macOS provides the environment and possible platform mechanisms. The adapter declares its actual implementation capabilities. The shared grammar carries the evidence. The detector interprets the structure. Policy determines authority. Outcome records execution. Verification determines resulting state.**

## Linux

Linux adapter artifacts:

- `linux.md` — human-readable platform specification defining the Linux observation, normalization, capability, containment, recovery, privacy, mount, namespace, container, and verification boundaries.
- `linux.schema.json` — machine-readable JSON Schema for validating concrete Linux adapter configurations.
- `linux.example.json` — synthetic example configuration demonstrating a conservative bounded user-space observer profile.

The Linux adapter follows the same architectural separation used throughout the adapter family:

**`linux.md` → semantic specification**

**`linux.schema.json` → adapter configuration contract**

**`linux.example.json` → synthetic conforming instance**

**Shared Structural Event Grammar → runtime interchange contracts**

The example configuration is intentionally illustrative rather than a declaration of Linux platform capability.

A concrete implementation must replace example and `unknown` capability states with evidence-backed declarations appropriate to its actual deployment, observation sources, privilege boundary, authorization, mount topology, namespace context, container context, and resource scope.

In particular:

- Linux platform capability does not automatically establish adapter capability;
- adapter capability does not establish authority to act;
- privilege does not establish authority;
- observation of one mount does not establish observation of all mounts;
- observation inside a namespace or container does not establish host-wide visibility;
- host-side and container-side observations may describe the same underlying transition;
- multiple telemetry sources do not automatically constitute independent evidence;
- observation does not establish ransomware;
- a requested containment response does not establish execution;
- successful execution does not establish resolution;
- recovery capability does not establish successful restoration;
- an observation gap does not establish absence of activity;
- bounded local observation must not be promoted into claims about unobserved local, remote, containerized, network-backed, or synchronized state.

The Linux configuration layer describes **what a particular adapter deployment claims it can observe, normalize, enforce, recover, and verify**.

Linux-specific configuration also preserves structural context that may materially affect those claims, including:

- mount awareness;
- namespace awareness;
- container awareness;
- host visibility;
- remote-storage awareness;
- privilege context;
- observation continuity;
- cross-mount verification;
- cross-namespace verification;
- cross-environment verification.

These fields describe deployment boundaries.

They do not establish ransomware, authority, or successful containment by themselves.

Canonical runtime lineage:

**`tf.resource-transition/v0.1`**

↓

**`tf.structural-pattern/v0.1`**

↓

**`tf.containment-decision/v0.1`**

↓

**`tf.response-outcome/v0.1`**

↓

**`tf.verification/v0.1`**

with:

**`tf.platform-capabilities/v0.1`**

declaring the capabilities available to the concrete adapter environment.

The Linux-specific architectural boundary can therefore be expressed as:

**Linux environment**

↓

**Mount / namespace / container / privilege boundary**

↓

**Configured observation source**

↓

**Linux adapter**

↓

**`tf.resource-transition/v0.1`**

↓

**Ransomware Structural Pattern Detector**

The reverse response path remains separately bounded:

**Structural pattern**

↓

**Containment decision**

↓

**Capability check**

↓

**Authority check**

↓

**Linux adapter**

↓

**Supported native mechanism**

↓

**Response outcome**

↓

**Verification**

This preserves several separate questions:

**What did the configured Linux observer actually see?**

↓

**Within which mount, namespace, container, host, or resource boundary was it observed?**

↓

**What structural transition does that evidence support?**

↓

**What interpretation does the detector support?**

↓

**What response, if any, is authorized and technically available?**

↓

**What actually executed?**

↓

**What state can be verified afterward?**

The distinction is especially important for Linux because a single platform label can describe substantially different adapter environments.

A bounded user-space observer, privileged host observer, container-scoped observer, and host-side container observer may all participate in the same structural grammar while exposing materially different observation and enforcement capabilities.

The shared semantics remain stable.

The capability declaration changes with the deployment.

The architectural rule is:

> **Linux provides the environment family. The adapter configuration declares the concrete implementation and its boundaries. The shared grammar carries the evidence. The detector interprets the structure. Policy determines authority. The outcome records execution. Verification determines resulting state.**

## Android

Android adapter artifact:

- `android.md` — human-readable platform specification defining the Android observation, normalization, capability, containment, recovery, privacy, synchronization, and verification boundaries.

The Android adapter follows the same architectural separation used throughout the adapter family:

**`android.md` → semantic specification**

**Adapter configuration → concrete implementation declaration**

**Shared Structural Event Grammar → runtime interchange contracts**

The Android specification is intentionally capability-bounded.

A concrete implementation must declare what it can actually observe, normalize, enforce, recover, and verify within its authorized application and resource scope rather than treating the Android platform as a device-wide observation surface.

In particular:

- application-visible state does not establish device-wide state;
- permission to access one resource surface does not imply access to unrelated resources;
- a resource reference does not necessarily correspond to a conventional filesystem path;
- observation does not establish ransomware;
- actor identity does not establish origin or intent;
- a locally visible transition may have originated in another environment;
- synchronized observations do not automatically constitute independent evidence;
- capability does not establish authority;
- a user-mediated response request does not establish execution;
- successful execution does not establish resolution;
- recovery capability does not establish verified restoration;
- inability to observe a surface does not establish that destructive activity is absent.

The Android adapter therefore treats **scope and visibility as part of the evidence model**.

Conceptually:

**Android security and authorization boundary**

↓

**Authorized observation surface**

↓

**Android adapter**

↓

**`tf.resource-transition/v0.1`**

↓

**Ransomware Structural Pattern Detector**

The reverse response path remains separately bounded:

**Structural pattern**

↓

**Containment decision**

↓

**Capability check**

↓

**Authority check**

↓

**Android adapter**

↓

**Supported native or user-mediated response**

↓

**Response outcome**

↓

**Verification**

This preserves several separate questions:

**What could the authorized Android adapter actually observe?**

↓

**What structural transition does that evidence support?**

↓

**Did the transition originate locally or arrive through another actor or environment?**

↓

**What interpretation does the detector support?**

↓

**What response, if any, is both supported and authorized?**

↓

**What actually happened?**

↓

**What resulting state can the adapter verify?**

The distinction is especially important for synchronized and provider-backed resources.

The Android adapter may establish that a transition became visible within its authorized scope without being able to establish where the transition originated.

Where cross-environment evidence exists, the Android adapter should cooperate with the Cloud / Synchronization adapter rather than manufacturing an origin locally.

Canonical runtime lineage:

**`tf.resource-transition/v0.1`**

↓

**`tf.structural-pattern/v0.1`**

↓

**`tf.containment-decision/v0.1`**

↓

**`tf.response-outcome/v0.1`**

↓

**`tf.verification/v0.1`**

with:

**`tf.platform-capabilities/v0.1`**

declaring the capabilities available to the concrete Android adapter environment.

The Android adapter also preserves an important privacy boundary.

Where structural information is sufficient, the shared analytical layer should receive:

- privacy-preserving resource identity;
- resource type and class;
- transition type;
- timing;
- preservation and recovery state;
- actor relationship;
- synchronization context;
- baseline relationship;
- provenance.

Raw resource contents, unnecessary identifying information, authentication material, and unrelated application data remain outside the shared analytical representation.

The architectural rule is:

> **Android provides the constrained execution environment. The adapter declares what the concrete implementation can actually observe and do. The shared grammar carries the evidence. The detector interprets the structure. Policy determines authority. The outcome records execution. Verification determines the resulting observable state.**

## iOS / iPadOS

iOS / iPadOS adapter artifact:

- `ios-ipados.md` — human-readable platform specification defining the iOS and iPadOS observation, normalization, capability, containment, recovery, privacy, synchronization, and verification boundaries.

The iOS / iPadOS adapter follows the same architectural separation used throughout the adapter family:

**`ios-ipados.md` → semantic specification**

**Adapter configuration → concrete implementation declaration**

**Shared Structural Event Grammar → runtime interchange contracts**

The iOS / iPadOS specification is intentionally capability-conservative.

A concrete implementation must declare what it can actually observe, normalize, enforce, recover, and verify within its authorized application and resource scope rather than treating the platform as a device-wide observation surface.

In particular:

- application-visible state does not establish device-wide state;
- unobserved activity does not establish absence of activity;
- state differences derived from repeated observations must remain distinguishable from directly observed native events;
- observation does not establish ransomware;
- actor identity does not establish origin or intent;
- a locally visible transition may have originated in another environment;
- synchronized observations do not automatically constitute independent evidence;
- capability does not establish authority;
- a user-mediated response request does not establish execution;
- successful execution does not establish resolution;
- recovery capability does not establish verified restoration;
- a clean bounded rescan does not establish that unobserved device or remote state is clean.

The iOS / iPadOS adapter therefore treats **bounded visibility as part of the evidence model**.

Conceptually:

**iOS / iPadOS security and authorization boundary**

↓

**Authorized application-visible surface**

↓

**iOS / iPadOS adapter**

↓

**`tf.resource-transition/v0.1`**

↓

**Ransomware Structural Pattern Detector**

Where continuous native observation is unavailable but repeated inspection of an authorized resource is possible, a concrete implementation may represent a bounded state comparison:

**State at T1**

↓

**Authorized observation interval**

↓

**State at T2**

↓

**Derived resource transition**

Such a transition may establish that state changed without establishing every intermediate operation, actor, or causal step.

That distinction must survive normalization.

The reverse response path remains separately bounded:

**Structural pattern**

↓

**Containment decision**

↓

**Capability check**

↓

**Authority check**

↓

**iOS / iPadOS adapter**

↓

**Supported native or user-mediated response**

↓

**Response outcome**

↓

**Verification**

This preserves several separate questions:

**What could the authorized adapter actually observe?**

↓

**Was the transition observed directly or derived through state comparison?**

↓

**What structural transition does that evidence support?**

↓

**Did the transition originate locally or arrive through another environment?**

↓

**What interpretation does the detector support?**

↓

**What response, if any, is both supported and authorized?**

↓

**What actually happened?**

↓

**What resulting state can be verified?**

For synchronized and cloud-backed resources, the iOS / iPadOS adapter should cooperate with the Cloud / Synchronization adapter rather than manufacturing remote origin from local evidence.

The device-side adapter may establish:

> **This transition became observable within the authorized iOS or iPadOS resource scope.**

The Cloud / Synchronization adapter may separately contribute evidence about:

- origin;
- transport;
- propagation;
- replication;
- version relationships;
- cross-environment recovery.

Those observations may be correlated while preserving their dependency.

Canonical runtime lineage:

**`tf.resource-transition/v0.1`**

↓

**`tf.structural-pattern/v0.1`**

↓

**`tf.containment-decision/v0.1`**

↓

**`tf.response-outcome/v0.1`**

↓

**`tf.verification/v0.1`**

with:

**`tf.platform-capabilities/v0.1`**

declaring the capabilities available to the concrete iOS / iPadOS adapter environment.

The capability declaration should begin from evidence rather than assumption.

A generic platform specification does not establish that a particular implementation possesses:

- event observation;
- actor identity;
- actor lineage;
- write denial;
- actor containment;
- resource isolation;
- network isolation;
- quarantine;
- rollback;
- recovery;
- post-action observation;
- recovery verification.

Where a capability has not been established, `unknown` is preferable to an optimistic declaration.

The iOS / iPadOS adapter also preserves a strong privacy boundary.

Where structural information is sufficient, the shared analytical layer should receive:

- privacy-preserving resource identity;
- resource type and class;
- transition type;
- timing;
- preservation state;
- recovery state;
- actor category;
- origin/transport relationship;
- synchronization context;
- baseline relationship;
- provenance.

Raw resource contents, unnecessary identifiers, authentication material, account secrets, and unrelated application data remain outside the shared analytical representation.

The architectural rule is:

> **iOS and iPadOS provide the constrained execution environment. The adapter declares what the concrete implementation can actually observe and do. The shared grammar carries the evidence. The detector interprets the structure. Policy determines authority. The outcome records execution. Verification determines the resulting observable state.**

## Cloud / Synchronization

Cloud / Synchronization adapter artifact:

- `cloud-sync.md` — human-readable cross-environment specification defining synchronization observation, normalization, origin and transport lineage, propagation, evidence independence, capability, containment, recovery, privacy, and verification boundaries.

The Cloud / Synchronization adapter follows the same architectural separation used throughout the adapter family:

**`cloud-sync.md` → semantic specification**

**Adapter configuration → concrete provider or synchronization implementation declaration**

**Shared Structural Event Grammar → runtime interchange contracts**

Unlike the operating-system adapters, the Cloud / Synchronization adapter is not defined primarily by a single device boundary.

Its purpose is to preserve structural lineage when resource transitions cross:

- devices;
- accounts;
- synchronization clients;
- cloud-backed resources;
- shared resource spaces;
- mirrored environments;
- remote storage;
- provider-mediated resource histories.

Its central distinction is:

> **Origin, transport, observation, replication, and propagation are different structural roles.**

A transition may be observed locally without having originated locally.

Likewise, the same originating transition may become visible through several synchronized environments without becoming several independent originating events.

In particular:

- local observation does not establish local origin;
- a synchronization service transporting a transition does not automatically become its origin;
- a trusted synchronization mechanism does not establish that transported state is benign;
- observation count does not establish origin count;
- multiple synchronized observations do not automatically constitute independent evidence;
- replication does not automatically establish a new originating transition;
- visibility does not establish ownership or authority;
- local containment does not establish global containment;
- successful provider execution does not establish cross-environment resolution;
- recovery capability or version history does not establish verified restoration;
- unobserved remote state does not establish safe remote state;
- reappearance may reflect delayed or propagated prior state rather than a new independent origin.

The Cloud / Synchronization adapter therefore treats **lineage across boundaries** as part of the evidence model.

Conceptually:

**Origin actor**

↓

**Origin environment**

↓

**Resource transition**

↓

**Transport actor / synchronization mechanism**

↓

**Cloud or synchronization boundary**

↓

**Recipient environment**

↓

**Observed resource transition**

The adapter should preserve as much of this lineage as the available evidence supports.

Where origin, transport, dependency, or propagation cannot be established, those relationships remain unresolved.

They must not be filled through assumption.

---

### Cross-Environment Correlation

The Cloud / Synchronization adapter may correlate evidence from device-specific adapters.

Conceptually:

**Windows / macOS / Linux / Android / iOS-iPadOS observation**

↓

**Local normalized transition**

↕ correlation

**Cloud / synchronization observation**

↓

**Cross-environment structural lineage**

↓

**Ransomware Structural Pattern Detector**

This allows the detector to distinguish, where evidence permits:

**one transition observed in several places**

from:

**several distinct transitions**

and:

**local materialization**

from:

**local origin**.

The distinction is especially important for downstream calculations involving:

- event count;
- activity rate;
- acceleration;
- affected-resource scope;
- propagation;
- evidence independence;
- confidence.

Correlation must preserve dependency rather than manufacture corroboration.

---

### Evidence Independence

Synchronization can produce many valid observations of the same underlying event.

For example:

**Originating transition**

↓

**Cloud observation**

↓

**Desktop observation**

↓

**Mobile observation**

↓

**Second synchronized endpoint observation**

These observations may strongly support the conclusion that a transition propagated.

They do not automatically provide independent evidence about where or why it originated.

The architectural rule is:

> **Multiple synchronized observations may corroborate propagation without independently corroborating origin or intent.**

Known dependencies should therefore remain visible through shared event and pattern lineage.

---

### Propagation

Propagation is a first-class structural concern for this adapter.

A concrete implementation may contribute evidence about:

- first observable environment;
- subsequent environments;
- transport relationships;
- resource lineage;
- transition timing;
- dependency relationships;
- replication;
- synchronization state;
- recovery relationships.

The adapter supplies the cross-environment evidence.

The detector determines whether that evidence supports a structural state such as expanding or active propagation.

---

### Containment Scope

Containment in synchronized environments must remain explicitly scoped.

Conceptually:

**Local containment**

does not necessarily imply:

**Cloud containment**

and:

**Cloud containment**

does not necessarily imply:

**Every synchronized endpoint is contained**.

A transition may already have:

- propagated;
- been queued;
- materialized elsewhere;
- altered remote state;
- affected another shared resource;
- produced dependent state outside the response boundary.

The response outcome must therefore record the environment, resources, actors, accounts, or synchronization relationships actually affected by the executed response.

> **Containment at one boundary is evidence about that boundary, not proof of containment across the topology.**

---

### Reappearance

Synchronization also makes reappearance structurally significant.

A condition that appears to stop locally may later return through:

- another synchronized device;
- delayed synchronization;
- remote state;
- another synchronized actor;
- restoration of affected state;
- unresolved propagation.

Where evidence permits, reappearance should retain lineage to the earlier transition.

It must not automatically be treated as a new independent origin.

---

### Recovery

Cloud and synchronization environments may expose evidence concerning:

- historical versions;
- preserved prior state;
- deleted-resource state;
- backup state;
- recovery objects;
- rollback mechanisms;
- restoration operations.

These states must remain separate:

**Recovery mechanism exists**

↓

**Recovery artifact or prior state exists**

↓

**Recovery is requested**

↓

**Recovery is attempted**

↓

**Recovery completes**

↓

**Restored state is verified**

Availability of one stage does not establish the next.

---

### Capability Declaration

The generic Cloud / Synchronization specification does not claim universal provider capability.

A concrete implementation must provide an evidence-backed:

**`tf.platform-capabilities/v0.1`**

declaration describing what its environment actually supports.

Where support has not been established, `unknown` is the correct default.

This is particularly important because observation and response capabilities may differ according to:

- provider;
- account;
- resource;
- resource ownership;
- authorization;
- shared-resource relationship;
- deployment;
- synchronization client;
- available interface;
- recovery configuration.

A provider category alone does not establish capability.

---

### Privacy Boundary

Cloud and synchronization observations may expose identities and relationships spanning several environments.

Where structural references are sufficient, the shared analytical layer should prefer:

- pseudonymous resource references;
- environment references;
- actor categories;
- origin and transport relationships;
- synchronization state;
- transition type;
- version relationships;
- recovery relationships;
- propagation relationships;
- provenance.

The shared detector does not require:

- passwords;
- access tokens;
- refresh tokens;
- session secrets;
- provider credentials;
- recovery secrets;
- unnecessary account identities;
- unnecessary resource contents.

The governing privacy rule is:

> **Normalize relationships before exporting identities, credentials, or content.**

---

### Verification

Cross-environment verification must remain bounded to the environments actually observed.

For example:

**Environment A: no continuation observed**

+

**Environment B: not observed**

+

**Cloud state: partially observed**

does not support:

**Globally resolved**

The resulting verification may instead remain:

- `partially_contained`;
- `partially_resolved`;
- `mixed`;
- `persistent`;
- `reappeared`;
- `unable_to_verify`.

A clean result in one environment must not erase uncertainty elsewhere.

Canonical runtime lineage:

**`tf.resource-transition/v0.1`**

↓

**`tf.structural-pattern/v0.1`**

↓

**`tf.containment-decision/v0.1`**

↓

**`tf.response-outcome/v0.1`**

↓

**`tf.verification/v0.1`**

with:

**`tf.platform-capabilities/v0.1`**

declaring the capabilities available to each concrete cloud or synchronization adapter environment.

The architectural rule is:

> **The Cloud / Synchronization adapter follows the transition across boundaries without confusing the actor that originated it, the mechanism that transported it, the environments that observed it, or the copies through which it propagated. The shared grammar preserves that lineage. The detector interprets the resulting structure. Policy determines authority. The outcome records what actually happened. Verification determines what state can actually be established afterward.**

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
