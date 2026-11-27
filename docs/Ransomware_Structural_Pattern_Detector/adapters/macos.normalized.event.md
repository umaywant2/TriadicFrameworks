# macOS Normalized Event Example

> **Worked example showing how a macOS-native observation becomes a platform-neutral `tf.resource-transition/v0.1` event without becoming a ransomware verdict.**

This document demonstrates the normalization boundary used by the macOS adapter.

The example is **synthetic**. It illustrates structure and lineage only. It does not represent an event captured from a real device.

The central rule is:

> **Normalization describes what was observed in shared structural vocabulary. Interpretation remains downstream.**

---

## Position in the Pipeline

The example occupies this part of the Ransomware Structural Pattern Detector pipeline:

**Native macOS observation**

↓

**macOS adapter**

↓

**Normalization**

↓

**`tf.resource-transition/v0.1`**

↓

**Correlation**

↓

**`tf.structural-pattern/v0.1`**

The normalized event is therefore an **observation-layer object**.

It is not:

- a ransomware classification;
- an intent assessment;
- an attribution;
- a severity verdict;
- a containment decision;
- an execution outcome;
- a verification result.

---

# Example Scenario

Assume the configured macOS adapter observes a write affecting a protected user document.

The adapter can establish that:

- a file resource changed;
- the observed actor is a known process;
- the operation maps to a write;
- the structural action maps to a modification;
- the resource is inside the configured protected scope;
- the operation is unusual relative to the available baseline;
- the observed activity rate is unusual relative to the available baseline.

The adapter cannot yet establish:

- whether the modification is destructive;
- whether the original resource state remains recoverable;
- whether the actor's broader behavior is coherent with its established role;
- whether the user intended the transition;
- whether another actor ultimately originated the activity;
- whether the transition belongs to a ransomware-like pattern.

Those unknowns remain unknown.

---

# Normalized Event

The resulting normalized event may take the following form:

**Schema:** `tf.resource-transition/v0.1`

**Event identity:** `event://macos-example/000001`

**Source:** filesystem

**Normalized operation:** write

**Structural transition:** modify

**Resource:** protected user document

**Observed actor:** known process

**Intent:** unknown

**Destructiveness:** unresolved

**Recoverability:** unresolved

**Baseline operation:** atypical

**Baseline rate:** atypical

**Propagation:** not observed

**Recovery impact:** unknown

This compact view is useful for humans, but the full normalized object retains the detailed lineage described below.

---

# Event

The event section establishes the identity, timing, source domain, and normalized operation.

Conceptually:

**native observation**

↓

**normalized event identity**

The event records:

- event identifier;
- event time;
- source domain;
- normalized operation;
- native operation when retained;
- processing phase;
- optional correlation identifier.

The important distinction is:

> **Native operation and normalized operation may coexist.**

The native operation preserves diagnostic lineage.

The normalized operation provides a portable structural vocabulary.

For example:

**native macOS operation**

↓

**`write`**

The normalization step does not infer why the write occurred.

---

# Processing Phase

The event uses:

`phase = normalized`

This identifies the object as the normalized representation emitted by the adapter.

It distinguishes the shared event from:

- raw platform evidence;
- downstream derived signals;
- correlated patterns;
- assessments;
- actions;
- outcomes;
- verification.

The processing boundary remains explicit.

---

# Actor

The actor section describes the actor visible at the observation point.

In the example, the actor is represented as a known process.

Possible actor information includes:

- structural actor ID;
- actor type;
- bounded human-readable name;
- parent reference;
- instance reference;
- account reference;
- role;
- trust context.

The normalized actor is evidence about the actor visible to the adapter.

It is not automatically the ultimate origin of the transition.

---

# Actor Identity

The example may establish:

**Identity state:** known

while leaving other questions unresolved.

A known actor does not establish:

- benign behavior;
- harmful behavior;
- user intent;
- originating intent;
- attribution beyond the observed actor.

The invariant is:

> **Actor identity ≠ intent**

---

# Trust Context

Where the adapter has authorized access to relevant trust information, it may preserve that context.

For example, the normalized event may record that the actor carries known identity or signing context.

That evidence must not suppress contradictory behavioral evidence.

The detector therefore preserves:

> **Trusted actor ≠ safe transition**

A previously familiar actor may still produce an anomalous resource transition.

---

# Origin and Transport

The actor visible on the Mac may not be the actor that originated a transition.

This is particularly important for:

- synchronization;
- cloud-backed resources;
- remote resources;
- intermediary services;
- delegated operations.

The normalized event may therefore preserve:

- observed actor;
- origin actor reference;
- transport actor reference;
- origin environment reference;
- synchronization context.

If origin is not established, it remains unresolved.

> **Local observation ≠ local origin**

---

# Resource

The resource section describes the affected structural resource.

In this example:

**Type:** `file`

**Class:** `user_document`

**Scope:** `local`

**Protected:** `true`

**Canary:** `false`

**Recoverable:** unresolved

**Sensitivity:** moderate

The shared event does not require the actual filename or raw filesystem path when those details are unnecessary for structural analysis.

Instead, it may use a pseudonymous identifier such as:

`resource://pseudonymous/document-0087`

This supports correlation without unnecessarily exposing personal information.

---

# Resource Identity

The adapter may retain a native resource reference locally while exposing only the privacy-preserving structural identifier to the detector.

Conceptually:

**native path**

↓

**local adapter mapping**

↓

**pseudonymous resource ID**

The detector can then determine that several transitions affect the same resource without needing the user's filename.

This is an example of:

> **Traceable abstraction rather than destructive abstraction.**

---

# Transition

The transition section describes what structurally happened to the resource.

In the example:

**Native/normalized operation:** write

↓

**Structural action:** modify

The adapter can establish modification.

It cannot yet establish destructiveness.

Therefore:

**Destructive:** unresolved

**Original preserved:** unresolved

**Reversibility:** unknown

This is intentional.

A write operation does not automatically mean destructive rewriting.

---

# Transition Characteristics

The normalized event may retain directly observable or explicitly derived characteristics.

The example records:

- size changed;
- content changed;
- extension did not change;
- ownership did not change;
- permissions did not change;
- authority did not change;
- resource scope did not change.

Other characteristics remain unresolved.

For example:

- structural change;
- entropy shift;
- recovery-state change.

These values may later become evidence in a structural pattern.

They are not themselves the pattern.

---

# Unknown, False, and Unresolved

Normalization depends heavily on distinguishing three different meanings.

## False

The adapter has evidence supporting a negative state.

Example:

`extension_changed = false`

The adapter established that the extension did not change.

## Unknown or Null

The adapter cannot establish the state.

Example:

`recoverable = null`

This means:

> Recoverability was not established.

It does not mean:

> The resource is unrecoverable.

## Unresolved Classification

Some shared fields use an explicit categorical state such as:

`reversibility = unknown`

This preserves uncertainty in the vocabulary appropriate to that field.

The general invariant is:

> **Unknown ≠ false**

---

# Context

The context section records structural circumstances surrounding the transition.

Candidate fields include:

- user intent;
- interactive-session state;
- bulk-operation state;
- network-origin state;
- synchronization-transport state;
- origin environment;
- session reference;
- authorized observation scope.

In the example:

**User intent:** unknown

**Synchronization transport:** false

Other context may remain unresolved.

Again, absence of evidence does not become a convenient negative answer.

---

# User Intent

The normalized event may record whether direct evidence exists that the user initiated or authorized the operation.

Possible states include:

- explicit;
- inferred;
- absent;
- unknown;
- not applicable.

This field remains distinct from broader actor intent.

For example:

**User intent:** unknown

does not imply:

**Actor intent:** harmful.

Intent assessment belongs downstream.

---

# Baseline

The baseline section compares the current observation with available historical or expected structural state.

The example establishes:

- baseline available;
- actor known;
- operation atypical;
- scope typical;
- rate atypical;
- resource type typical;
- overall role coherence unresolved.

This produces a deliberately mixed structural picture.

Conceptually:

**Known actor**

+

**Expected resource class**

+

**Expected scope**

+

**Atypical operation**

+

**Atypical rate**

+

**Unresolved role coherence**

That is much more informative than reducing the entire observation to:

**suspicious = true**

---

# Baseline Is Context, Not Trust

Historical normality does not grant permanent trust.

Likewise, unfamiliarity does not establish hostility.

The baseline answers:

> **How does this observation compare with what has previously been established?**

It does not answer:

> **Is the actor malicious?**

The downstream detector considers baseline deviation together with other supporting, counter, and unresolved evidence.

---

# Consequence

The consequence section records directly observable effects.

In the example:

**State:** resource changed

**Propagation observed:** false

**Recovery impact:** unknown

This means the adapter can establish that the resource changed and did not observe propagation within the available evidence.

It cannot establish the consequence for recovery.

The consequence remains bounded to what was actually observed.

---

# Provenance

Provenance connects the normalized object back to its source evidence.

The example preserves:

- platform;
- adapter;
- adapter version;
- capability declaration;
- observation time;
- normalization time;
- native-event reference;
- raw-event retention state;
- derivation references;
- redaction classes.

Conceptually:

**native observation**

↓

**observation timestamp**

↓

**macOS adapter**

↓

**normalization method**

↓

**redaction**

↓

**`tf.resource-transition/v0.1`**

while:

**native-event reference**

points back toward the original evidence retained inside its authorized boundary.

This is the foundation of reconstructable analysis.

---

# Redaction

The example may remove or generalize fields such as:

- raw path;
- resource name;
- user identity;
- process arguments.

Those redactions are recorded in provenance.

The central detector therefore knows that information was deliberately withheld or generalized rather than assuming the information never existed.

This distinction supports both privacy and evidentiary honesty.

---

# What Normalization May Derive

The adapter may perform bounded derivation where the method is explicit.

Examples include:

- mapping a native resource to `user_document`;
- mapping a native operation to `write`;
- mapping the resulting structural action to `modify`;
- comparing the operation with an established baseline;
- determining that the observed transition lies within an authorized scope;
- pseudonymizing the resource identifier.

Derived information should preserve method or source lineage where material.

---

# What Normalization Must Not Derive

The normalization layer must not silently produce claims such as:

- ransomware confirmed;
- malicious actor;
- harmful intent;
- attacker identity;
- critical severity;
- containment required;
- resource unrecoverable;
- incident resolved.

Those statements belong to later analytical or response stages and require additional evidence.

The normalization boundary is:

> **Represent evidence faithfully before interpreting it aggressively.**

---

# From One Event to a Pattern

One normalized event is usually not very interesting.

The detector becomes useful when many events can be correlated.

For example:

**Event 1**

Known process modifies protected document.

↓

**Event 2**

Same actor modifies another protected document.

↓

**Event 3**

Transition rate increases.

↓

**Event 4**

Affected resource scope expands.

↓

**Event 5**

Prior usable state is no longer preserved.

↓

**Event 6**

Recovery-related resources change.

Only after correlation, baseline comparison, counter-evidence evaluation, and uncertainty preservation does the detector have enough structure to consider a ransomware-like pattern.

Conceptually:

**`tf.resource-transition/v0.1` × N**

↓

**CORRELATE**

↓

**derive structural signals**

↓

**CONTRADICT**

↓

**preserve competing explanations**

↓

**ASSESS**

↓

**`tf.structural-pattern/v0.1`**

---

# Counter-Evidence Still Matters

Suppose the same event sequence also includes evidence that:

- the user explicitly initiated an authorized bulk transformation;
- the application routinely performs this operation;
- originals are preserved;
- recovery remains available;
- activity remains within the expected scope.

Those observations must survive correlation.

The detector does not simply count concerning events.

It evaluates:

> **Destructive deviation against available structural coherence.**

---

# Why This Event Does Not Say "Ransomware"

The normalized event deliberately does not contain:

- `ransomware = true`;
- `malicious = true`;
- `intent = harmful`;
- `severity = critical`;
- `contain = true`.

Instead, it establishes a bounded statement:

> **A known process performed an atypical write affecting a protected user document within the authorized observation scope. The resource changed, the observed rate was atypical, and destructiveness, recoverability, intent, and broader role coherence remain unresolved.**

That statement is less dramatic.

It is also much more useful structurally.

It can be:

- correlated;
- contradicted;
- reproduced;
- reinterpreted;
- compared against future events;
- inspected by humans;
- inspected by AI systems;
- traced back to its source.

---

# Relationship to the macOS Adapter Configuration

`macos.schema.json` validates the configuration of a macOS adapter.

`macos.example.json` demonstrates a synthetic generic adapter configuration.

`macos.endpoint-security.example.json` demonstrates a stronger illustrative deployment profile.

This document demonstrates what a normalized observation produced by such an adapter may look like conceptually.

The roles remain separate:

**`macos.md`**

Defines macOS adapter semantics.

↓

**`macos.schema.json`**

Defines the adapter configuration contract.

↓

**macOS adapter configuration**

Declares concrete observation and response capabilities.

↓

**Native observation**

Provides platform evidence.

↓

**`tf.resource-transition/v0.1`**

Carries normalized structural evidence.

↓

**Ransomware Structural Pattern Detector**

Interprets correlated structure.

---

# Relationship to the Shared Structural Event Grammar

The canonical machine-readable contract for this event is:

`../../Shared_Structural_Event_Grammar/resource-transition.schema.json`

The macOS adapter does not redefine that schema.

Instead, it maps macOS evidence into it.

That is the portability boundary:

**Windows observation**

**Linux observation**

**macOS observation**

**Android observation**

**iOS / iPadOS observation**

**Cloud / synchronization observation**

**Database observation**

**Cache observation**

↓

**Shared Structural Event Grammar**

The native evidence differs.

The normalized structural semantics remain comparable.

---

# Canonical Normalization Rule

The complete normalization path is:

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

**preserve source dependencies**

↓

**compare with available baseline**

↓

**record direct consequence**

↓

**minimize sensitive data**

↓

**retain provenance**

↓

**emit `tf.resource-transition/v0.1`**

Then normalization stops.

The downstream path begins separately:

**Normalized transitions**

↓

**correlation**

↓

**derived signals**

↓

**supporting evidence**

+

**counter-evidence**

+

**unresolved evidence**

↓

**competing explanations**

↓

**structural assessment**

↓

**`tf.structural-pattern/v0.1`**

---

# Canonical Summary

> **A normalized macOS event is a privacy-conscious, provenance-preserving structural representation of what an authorized macOS adapter observed. It is evidence for analysis, not the conclusion of that analysis.**

Its evidence rule is:

> **Record what is known, preserve what is unknown, and do not manufacture the missing bridge between observation and intent.**

Its portability rule is:

> **Keep native detail available through lineage while expressing the structural event through shared vocabulary.**

Its privacy rule is:

> **The detector should receive the structure it needs without receiving sensitive native detail it does not need.**

Its analytical boundary is:

> **Normalization ends at `tf.resource-transition/v0.1`. Ransomware interpretation begins downstream.**
