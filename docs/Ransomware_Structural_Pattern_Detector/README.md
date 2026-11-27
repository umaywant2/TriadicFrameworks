<img width="1194" height="672" alt="Ransomware_Structural_Pattern_Detector_" src="https://github.com/user-attachments/assets/32009e0c-cd0d-45e8-b871-e0f91f96f90f" />

- [`detector.json`](detector.json) — Agentic module schema role assignments

# Ransomware Structural Pattern Detector

> **A platform-neutral structural analyzer for detecting accelerating destructive resource-transition patterns and producing bounded, evidence-preserving containment decisions.**

The Ransomware Structural Pattern Detector (RSPD) is a specialized TriadicFrameworks system-security analyzer.

Its purpose is to identify structural behavior consistent with ransomware-like destructive activity without requiring individual observations, actors, applications, services, or resources to be labeled malicious in advance.

The detector consumes normalized structural observations, correlates them across time, actors, resources, environments, and baselines, preserves supporting evidence, counter-evidence, dependencies, competing explanations, and uncertainty, and produces bounded assessments suitable for downstream response decisions.

Its governing principle is:

> **Detect destructive structure early enough to limit damage, but never convert anomaly into intent, attribution, or certainty without evidence.**

---

## Status

- **Name:** Ransomware Structural Pattern Detector
- **Abbreviation:** RSPD
- **Status:** Experimental
- **Role:** Specialized system-security structural analyzer
- **Input grammar:** Shared Structural Event Grammar
- **Primary event:** `tf.resource-transition/v0.1`
- **Primary analytical output:** `tf.structural-pattern/v0.1`
- **Capability interface:** `tf.platform-capabilities/v0.1`
- **Decision interface:** `tf.containment-decision/v0.1`
- **Outcome interface:** `tf.response-outcome/v0.1`
- **Verification interface:** `tf.verification/v0.1`
- **Machine-readable detector definition:** `detector.json`
- **Adapter layer:** `adapters/`
- **Runtime examples:** `examples/`
- **Validation layer:** `validation/`

---

# Module Structure

The module is organized into four primary layers:

**Detector semantics**

`detector.json`

↓

**Adapter layer**

`adapters/`

↓

**Runtime example lineage**

`examples/`

↓

**Validation**

`validation/`

These layers serve different purposes.

## Detector Definition

`detector.json`

defines the machine-readable analytical contract for ransomware-relevant structural reasoning.

It does not define platform-specific observation or response mechanisms.

## Adapters

`adapters/`

defines how native platforms, cross-environment systems, databases, caches, and other resource boundaries translate observations and actions into the shared structural grammar.

## Examples

`examples/`

provides a synthetic end-to-end runtime lineage demonstrating:

**observation → pattern → decision → outcome → verification**

## Validation

`validation/`

defines reproducible structural checks over schemas, configurations, examples, lineage, and architectural invariants.

---

# Purpose

Traditional ransomware indicators may focus on recognizable artifacts such as:

- signatures;
- known process names;
- file extensions;
- ransom notes;
- known malicious identities;
- static indicators.

RSPD operates at a different layer.

It asks:

> **Are observed resource transitions forming a destructive, accelerating, expanding, or otherwise materially harmful structural pattern that is approaching or exceeding an acceptable damage boundary?**

The distinction matters because the actor visible during destructive activity may be:

- previously known;
- signed or trusted;
- a legitimate application being abused;
- a defective application;
- an automation tool;
- a database engine acting on behalf of another client;
- a cache service propagating another actor's state;
- a synchronization service transporting remote changes;
- an unidentified process;
- one component in a longer actor chain.

The detector therefore evaluates **behavioral structure rather than reputation alone**.

---

# Architectural Position

RSPD sits above normalized observations and below policy-governed intervention.

Canonical lineage:

**Native / Service / Resource Observation**

↓

**Adapter / Normalizer**

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

**Native / Service Response**

↓

**`tf.response-outcome/v0.1`**

↓

**Post-Response Observation**

↓

**`tf.verification/v0.1`**

This separation keeps:

- observation distinct from interpretation;
- interpretation distinct from policy decision;
- capability distinct from authority;
- decision distinct from execution;
- requested response distinct from executed response;
- execution distinct from verification;
- containment distinct from resolution;
- recovery capability distinct from verified restoration.

---

# Six Structural Questions

The architecture deliberately separates six questions.

## 1. What was observed?

Answered primarily by:

`tf.resource-transition/v0.1`

## 2. What pattern does the evidence support?

Answered by:

`tf.structural-pattern/v0.1`

## 3. What can the environment actually do?

Declared through:

`tf.platform-capabilities/v0.1`

## 4. What response is justified and authorized?

Represented by:

`tf.containment-decision/v0.1`

## 5. What actually happened?

Recorded through:

`tf.response-outcome/v0.1`

## 6. What state exists afterward?

Represented by:

`tf.verification/v0.1`

No one object should silently answer all six.

---

# Shared Structural Event Grammar

RSPD consumes and produces contracts from the Shared Structural Event Grammar rather than redefining a ransomware-specific event lineage.

Relevant schema families include:

- `tf.resource-transition/v0.1`
- `tf.structural-pattern/v0.1`
- `tf.platform-capabilities/v0.1`
- `tf.containment-decision/v0.1`
- `tf.response-outcome/v0.1`
- `tf.verification/v0.1`

This allows ransomware-specific reasoning to remain specialized while the underlying structures for observation, evidence, capability, action, outcome, and verification remain reusable.

The architectural rule is:

> **The shared grammar represents structure. RSPD interprets ransomware-relevant structure. Adapters observe and act within their own boundaries.**

---

# Normalization Boundary

The detector consumes normalized `tf.resource-transition/v0.1` objects.

Normalization translates heterogeneous native evidence into shared structural vocabulary.

Conceptually:

**Native evidence**

↓

**identify observation source**

↓

**establish authorized scope**

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

**preserve dependencies**

↓

**preserve provenance**

↓

**minimize sensitive data**

↓

**emit `tf.resource-transition/v0.1`**

Then normalization stops.

Ransomware interpretation begins downstream.

The detailed cross-adapter normalization contract is documented in:

`adapters/normalization_fields.md`

---

# Observation vs. Interpretation

A normalized observation may establish:

> **A known process modified a protected user document at an atypical rate.**

It should not silently become:

> **Ransomware modified the document.**

The detector may later correlate many such observations and conclude that they support a ransomware-like structural pattern.

That conclusion belongs to the analytical stage.

The invariant is:

> **Native observation ≠ domain verdict**

---

# What the Detector Looks For

RSPD is concerned with **patterns of resource transition**, not isolated suspicious-looking events.

Candidate structural signals include:

- unusual transition rate;
- accelerating modification rate;
- expanding resource scope;
- destructive or replacement transitions;
- originals not being preserved;
- unexpected transformation of protected resources;
- deviation from an actor's established role;
- deviation from historical activity;
- recovery-resource interference;
- propagation across resources or environments;
- repeated behavior inconsistent with baseline;
- reappearance after apparent containment;
- cross-layer destructive coherence.

No single signal is sufficient to establish ransomware.

The detector correlates evidence while continually testing its proposed interpretation against counter-evidence and competing explanations.

---

# Structural Progression

A ransomware-like pattern may emerge progressively.

Conceptually:

**Normal activity**

↓

**Unusual transition activity**

↓

**Correlated deviation**

↓

**Destructive transformation**

↓

**Acceleration**

↓

**Scope expansion**

↓

**Damage boundary approached**

↓

**Bounded containment candidate**

This is deliberately not a universal fixed scoring formula.

Different systems, resource classes, environments, and policies may require different calibration.

The portable detector preserves structural dimensions.

Concrete deployments determine appropriate thresholds.

---

# Actor Semantics

An observed actor is not automatically the origin of a destructive transition.

The detector should preserve, where evidence permits:

- observed actor;
- origin candidate;
- transport actor;
- parent or invoking actor;
- actor lineage;
- originating environment;
- execution account;
- service relationship.

Examples illustrate why this matters.

A synchronization service may transport destructive changes created elsewhere.

A database engine may execute a mutation requested by another application.

A cache service may replicate a mutation originating on another node.

A host process may materialize remote state.

Therefore:

> **Observed actor ≠ proven origin actor**

and:

> **Trusted actor ≠ safe transition**

---

# Baseline and Role Deviation

A baseline may help answer:

- Is this actor known?
- Is this operation typical?
- Is this transition rate typical?
- Is this resource scope typical?
- Is this resource class typical for the actor?
- Is this behavior coherent with the actor's established role?
- Is this propagation pattern expected?
- Is this recovery activity ordinary?

Baseline deviation is useful evidence.

It is not proof of malice.

Legitimate workflows capable of producing large transition volumes include:

- backups;
- restores;
- migration;
- synchronization;
- media processing;
- authorized encryption;
- software deployment;
- development builds;
- database maintenance;
- cache rebuilding;
- bulk administration.

The detector treats deviation as something to explain, not something to condemn.

---

# Supporting Evidence

Supporting evidence strengthens a destructive-pattern interpretation.

Candidate evidence includes:

- accelerating transition rate;
- expanding scope;
- destructive rewriting;
- replacement of usable prior state;
- unexpected transformation;
- recovery interference;
- actor-role deviation;
- cross-boundary propagation;
- reappearance following containment;
- several structurally coherent signals from distinct evidence sources.

Supporting evidence should retain references to the observations and derivations that produced it.

---

# Counter-Evidence

Counter-evidence is equally important.

Candidate examples include:

- explicit user initiation;
- expected bulk workflow;
- established actor role;
- known destination or transformation;
- preservation of originals;
- verified recovery state;
- expected synchronization;
- expected database maintenance;
- expected cache expiration or eviction;
- operation consistent with baseline.

Counter-evidence must not disappear merely because alarming signals accumulate.

The detector evaluates:

> **Destructive deviation against available structural coherence.**

---

# Competing Explanations

The detector should preserve plausible alternatives where evidence supports them.

Examples may include:

- authorized bulk transformation;
- defective application behavior;
- migration;
- backup or restoration;
- administrative automation;
- synchronization;
- database maintenance;
- cache expiration;
- cache eviction;
- recovery activity.

A competing explanation may be:

- supported;
- plausible;
- weak;
- unresolved;
- contradicted;
- rejected;

according to the relevant analytical vocabulary.

The objective is not to generate excuses for destructive behavior.

It is to avoid converting incomplete evidence into unsupported certainty.

---

# Unresolved Evidence

Important questions may remain unanswered.

Examples include:

- Did the observed actor originate or transport the transition?
- Is the transformation reversible?
- Are several observations independent?
- Does recovery remain available?
- Was the activity explicitly authorized?
- Does related state exist outside the observation scope?
- Did the same originating transition propagate elsewhere?

These conditions remain explicitly unresolved.

The detector must not convert missing evidence into negative evidence.

> **Unknown ≠ false**

---

# Evidence Independence

Multiple observations do not necessarily constitute independent corroboration.

Dependent evidence may arise from:

- synchronized devices;
- mirrored storage;
- duplicate telemetry;
- host and container observers;
- copied reports;
- shared upstream event sources;
- database logical and storage layers;
- replicated cache nodes;
- one native event represented by several telemetry systems.

Several observations may strongly confirm that a transition occurred or propagated while still representing one originating event.

The detector should preserve source dependencies where known.

> **Correlation ≠ independence**

---

# Structural Assessment

RSPD produces a structural assessment rather than an accusation.

Relevant dimensions may include:

- pattern state;
- baseline deviation;
- trajectory;
- resource scope;
- destructiveness;
- propagation;
- severity;
- confidence;
- reversibility;
- recovery impact;
- competing explanations;
- evidence independence;
- intent uncertainty;
- attribution uncertainty.

A valid assessment may simultaneously report:

**Structural confidence:** High

**Severity:** High

**Intent:** Unknown

**Attribution:** Unresolved

These conclusions are compatible.

---

# Intent and Attribution

Ransomware-like structure, harmful intent, and actor attribution are different questions.

The detector may establish:

> **An accelerating destructive resource-transition pattern is occurring.**

without establishing:

> **A particular human, application, organization, or remote actor deliberately caused it.**

Therefore:

> **Structural confidence ≠ intent confidence ≠ attribution confidence**

Containment may still be justified by observable damage trajectory.

---

# Damage Boundary

RSPD supports a bounded damage model.

Relevant dimensions may include:

- resource sensitivity;
- affected-resource scope;
- transition rate;
- acceleration;
- reversibility;
- recovery availability;
- propagation risk;
- recovery impact;
- collateral response impact.

The detector does not define one universal numerical damage formula.

Instead, it provides evidence that policy may use to determine whether the observed state is:

- within limit;
- approaching limit;
- at limit;
- beyond limit;
- unresolved.

The governing rule is:

> **Intervene according to observable structural risk and bounded authority, not according to certainty about motive.**

---

# Platform and Environment Capabilities

Capabilities are represented through:

`tf.platform-capabilities/v0.1`

Capabilities may concern:

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
- session termination;
- adapter-specific bounded enforcement.

## Recovery

- rollback;
- snapshots;
- resource restoration;
- configuration restoration;
- version restoration;
- rebuild.

## Verification

- post-action observation;
- state comparison;
- persistence detection;
- reappearance detection;
- recovery verification;
- cross-environment comparison.

Capability values should distinguish:

- `supported`
- `partial`
- `unsupported`
- `unknown`

The invariant is:

> **Capability ≠ authority**

---

# Adapter Layer

Native implementation belongs under:

`adapters/`

The adapter family now includes three structural categories.

## Platform

- Windows
- Linux
- macOS
- Android
- iOS / iPadOS

## Cross-Environment

- Cloud / Synchronization

## Resource / Service

- Database
- Cache

This classification reflects the module's evolution beyond filesystem-oriented platform adapters.

A database adapter and operating-system adapter may observe different layers of the same underlying activity.

A cache adapter and database adapter may represent derived and authoritative state.

A device adapter and cloud-sync adapter may observe local materialization and remote transport.

The architecture permits these observations to coexist without forcing one layer to impersonate another.

---

# Adapter Artifact Model

Canonical adapters generally follow:

**`<adapter>.md`**

↓

**`<adapter>.schema.json`**

↓

**`<adapter>.example.json`**

These represent:

**semantic specification**

↓

**machine-readable configuration contract**

↓

**synthetic conforming instance**

Adapter-specific configuration does not replace the Shared Structural Event Grammar.

Configuration tells us how an adapter is declared.

Runtime grammar tells us how structural evidence is exchanged.

The adapter registry is:

`adapters/detector.json`

The detailed adapter architecture is documented in:

`adapters/README.md`

---

# Cross-Adapter Composition

Complex environments may require several adapters.

Examples include:

**Windows + Cloud / Synchronization**

**macOS + Cloud / Synchronization**

**Android + Cloud / Synchronization**

**iOS/iPadOS + Cloud / Synchronization**

**Database + Linux**

**Database + Windows**

**Cache + Database**

Cross-adapter correlation should preserve:

- source adapter;
- observation scope;
- capability boundary;
- origin/transport relationships;
- source dependencies;
- derivation lineage;
- privacy boundary.

The governing rule is:

> **Correlate across layers without erasing the layers.**

---

# Containment Decision

Containment is downstream from detection.

The policy-facing contract is:

`tf.containment-decision/v0.1`

A containment decision may consider:

- structural confidence;
- severity;
- damage trajectory;
- affected-resource sensitivity;
- reversibility;
- capability;
- authority;
- collateral impact;
- recovery state;
- unresolved evidence.

A rapidly expanding destructive pattern may justify bounded containment even while intent and attribution remain unresolved.

That is not a contradiction.

The response is justified by observable structural risk.

---

# Proportional Response

A response should be bounded by:

- evidence strength;
- damage trajectory;
- resource sensitivity;
- reversibility;
- available capability;
- authorization;
- collateral impact;
- recovery state.

A weaker reversible response may be preferable when it sufficiently bounds immediate risk.

The detector therefore separates:

**What is happening?**

from:

**Why is it happening?**

from:

**Who caused it?**

from:

**What intervention is justified?**

---

# Requested vs. Executed Response

The response requested by policy may differ from what the adapter can actually execute.

Canonical path:

**Requested response**

↓

**Capability check**

↓

**Authority check**

↓

**Native mechanism mapping**

↓

**Execution attempt**

↓

**`tf.response-outcome/v0.1`**

The outcome preserves:

- requested response;
- execution status;
- executed response;
- fallback;
- capability constraints;
- direct effects;
- side effects;
- errors;
- warnings;
- rollback state;
- provenance.

The invariant is:

> **Requested response ≠ executed response**

---

# Execution vs. Resolution

Execution does not complete the analytical cycle.

A native mechanism may report success.

That establishes evidence about the bounded action.

It does not establish that:

- destructive activity stopped;
- another actor did not continue the pattern;
- synchronized state did not reintroduce the condition;
- affected state became recoverable;
- remote origin disappeared.

Therefore:

> **Execution ≠ resolution**

---

# Verification

After response, the environment is observed again.

Verification asks:

- Did destructive activity stop?
- Does the pattern persist?
- Did it reappear?
- Did another actor continue it?
- Did new conditions emerge?
- Is the affected state recoverable?
- Did propagation continue?
- Are some areas impossible to verify?
- Did the response create additional structural problems?

Possible high-level states include:

- contained;
- partially contained;
- persistent;
- reappeared;
- resolved;
- partially resolved;
- new condition detected;
- mixed;
- unable to verify.

The central rule is:

> **Containment is an action. Resolution is an observed state.**

Verification scope must remain explicit.

> **Bounded verification ≠ global resolution**

---

# Recovery

Recovery is distinct from containment and verification.

Potential mechanisms include:

- snapshots;
- backups;
- preserved originals;
- version history;
- provider restoration;
- recovery stores;
- database restoration;
- cache rebuild;
- other adapter-specific mechanisms.

These states must remain separate:

**Recovery capability exists**

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

# End-to-End Examples

The `examples/` directory provides a synthetic example lineage.

Canonical sequence:

**`examples/resource-transition.example.json`**

↓

**`examples/structural-pattern.example.json`**

↓

**`examples/containment-decision.example.json`**

↓

**`examples/response-outcome.example.json`**

↓

**`examples/verification.example.json`**

The examples deliberately demonstrate a non-trivial case:

- an unusual normalized transition is observed;
- multiple observations support an accelerating destructive pattern;
- structural confidence becomes high;
- intent remains unknown;
- attribution remains unresolved;
- a bounded containment response is authorized;
- the response executes within its scope;
- verification establishes containment within that scope;
- remote-origin and recovery state remain unresolved.

This is intentional.

The example lineage shows that the architecture can act under uncertainty without pretending the uncertainty disappeared.

---

# Validation

The validation layer lives under:

`validation/`

Its human-readable contract is:

`validation/README.md`

Its machine-readable validation plan is:

`validation/manifest.json`

Validation may check:

- JSON syntax;
- JSON Schema conformance;
- adapter artifact relationships;
- runtime schema relationships;
- example lineage;
- cross-artifact invariants.

Validation does not establish empirical detector effectiveness.

The governing rule is:

> **Conformance establishes structural consistency. It does not establish empirical truth.**

---

# Validation vs. Evaluation

Two activities must remain separate.

## Validation

> **Does an artifact satisfy its declared structural contract?**

## Evaluation

> **Does the detector behave effectively on representative real or experimental data?**

A schema-valid detector may still perform poorly.

An experimentally useful detector may reveal flaws in the schemas.

Neither result should be hidden.

---

# Data Minimization

RSPD does not inherently require central access to raw user resources.

It may need structural facts such as:

- resource class;
- transition type;
- preservation state;
- recoverability;
- rate;
- actor relationship;
- scope;
- baseline deviation;
- environment relationship;
- evidence dependency.

It may not need:

- document contents;
- database contents;
- cache contents;
- raw cache keys;
- full filenames;
- personal directory names;
- credentials;
- provider tokens;
- private keys;
- unrelated account information.

Adapters should normalize and redact whenever structural representation is sufficient.

> **Detect the transition without unnecessarily exposing the resource.**

---

# Provenance

Evidence lineage must survive every stage.

Relevant provenance may connect:

**Native evidence**

↓

**Normalized transition**

↓

**Derived signal**

↓

**Structural pattern**

↓

**Containment decision**

↓

**Response outcome**

↓

**Verification**

This enables:

- reconstruction;
- critique;
- human inspection;
- AI inspection;
- validation;
- revision;
- comparison;
- future reanalysis.

The objective is not merely to produce a conclusion.

It is to preserve enough structure to understand how the conclusion was reached.

---

# Core Invariants

## RSPD-INV-01 — Transition ≠ Intent

A destructive transition does not independently establish malicious intent.

## RSPD-INV-02 — Actor ≠ Origin

The actor visible at the observation point may be an executor, intermediary, or transport.

## RSPD-INV-03 — Trust ≠ Behavioral Safety

A trusted or previously benign actor may still participate in a destructive transition.

## RSPD-INV-04 — Anomaly ≠ Ransomware

Baseline deviation alone does not establish a ransomware-like pattern.

## RSPD-INV-05 — Pattern ≠ Attribution

Detection of a ransomware-like structural pattern does not independently identify its ultimate cause.

## RSPD-INV-06 — Correlation ≠ Independence

Several observations derived from one transition do not automatically constitute independent corroboration.

## RSPD-INV-07 — Unknown ≠ False

Unavailable evidence remains unresolved.

## RSPD-INV-08 — Capability ≠ Authority

Technical ability does not authorize an action.

## RSPD-INV-09 — Decision ≠ Execution

A containment decision does not prove that its requested response occurred.

## RSPD-INV-10 — Requested Response ≠ Executed Response

Fallback, partial execution, blocked execution, and failure remain explicit.

## RSPD-INV-11 — Execution ≠ Resolution

A successfully executed response does not prove that destructive activity was resolved.

## RSPD-INV-12 — Recovery Capability ≠ Recovery Success

The existence of a recovery mechanism does not establish successful restoration.

## RSPD-INV-13 — Bounded Verification ≠ Global Resolution

A clean result inside one observation scope does not establish state outside it.

## RSPD-INV-14 — Derived ≠ Observed

Derived structural evidence remains distinguishable from native observation.

## RSPD-INV-15 — Evidence Lineage Must Survive

Observations, derivations, decisions, outcomes, and verification retain sufficient provenance for reconstruction.

## RSPD-INV-16 — Validation ≠ Empirical Truth

A structurally valid artifact does not establish the empirical correctness of its claims or analytical behavior.

---

# Non-Goals

RSPD is not:

- a malware-signature database;
- a threat-intelligence feed;
- an attribution engine;
- a universal ransomware classifier;
- a replacement for endpoint security;
- a guarantee that ransomware will be detected;
- a guarantee that containment will succeed;
- a guarantee that recovery will succeed;
- a mechanism for bypassing platform security controls;
- an authorization engine;
- a license to destroy or quarantine data without appropriate authority;
- a system for automatically assigning hostile intent to anomalous activity.

It is a **structural behavioral analyzer**.

---

# Relationship to Profile Rectification

RSPD emerged as a specialized system-security analyzer alongside Profile Rectification, but it is not embedded inside Profile Rectification.

The distinction is intentional.

**Profile Rectification**

provides consent-bound orchestration and structural hygiene across authorized human and AI-context surfaces.

**RSPD**

evaluates destructive system-resource transition patterns.

Both may consume the Shared Structural Event Grammar.

Neither needs to own it.

---

# Machine-Readable Detector Definition

The detector's machine-facing analytical contract is:

`detector.json`

That file defines detector-specific vocabulary and operating semantics without duplicating the generic schemas supplied by the Shared Structural Event Grammar.

The responsibilities are separated:

**`README.md`**

Human-readable architecture and analytical boundaries.

**`detector.json`**

Machine-readable detector-specific semantics.

**Shared Structural Event Grammar**

Portable runtime contracts.

**`adapters/`**

Native observation, capability declaration, normalization, response mapping, and bounded verification.

**`examples/`**

Synthetic runtime lineage.

**`validation/`**

Structural conformance and lineage validation.

---

# Repository Navigation

Primary module artifacts:

- `README.md`
- `detector.json`

Adapter layer:

- `adapters/README.md`
- `adapters/detector.json`
- `adapters/normalization_fields.md`

Runtime examples:

- `examples/resource-transition.example.json`
- `examples/structural-pattern.example.json`
- `examples/containment-decision.example.json`
- `examples/response-outcome.example.json`
- `examples/verification.example.json`

Validation:

- `validation/README.md`
- `validation/manifest.json`

Adapter-specific specifications, configuration schemas, examples, and deployment examples live under:

`adapters/`

---

# Canonical Summary

> **The Ransomware Structural Pattern Detector is a platform-neutral structural analyzer that detects accelerating destructive resource-transition patterns, preserves supporting and contradictory evidence, bounds uncertainty, and provides sufficient structure for proportionate containment and subsequent verification.**

Its evidence path is:

**OBSERVE → NORMALIZE → PRESERVE**

Its analytical path is:

**CORRELATE → DERIVE → CONTRADICT → ASSESS → BOUND**

Its response path is:

**DECIDE → ADAPT → ACT → RECORD**

Its verification path is:

**RESCAN → COMPARE → PRESERVE LIMITATIONS → REPORT**

Its validation path is:

**PARSE → SCHEMA → RELATE → TRACE → CHECK INVARIANTS**

Its evidence rule is:

> **Detect destructive structure without pretending to know more than the evidence establishes.**

Its containment rule is:

> **Intervene proportionately to observable damage and available authority, not merely to certainty about motive.**

Its adapter rule is:

> **Standardize structural semantics without pretending platforms, services, or resources expose identical mechanisms.**

Its privacy rule is:

> **Prefer structural evidence over unnecessary native content or identity.**

Its verification rule is:

> **Execution is not resolution. Observe the resulting state.**

Its validation rule is:

> **Structural conformance is evidence of consistency, not proof of empirical truth.**
