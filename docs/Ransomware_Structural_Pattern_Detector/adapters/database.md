<img width="1194" height="672" alt="Ransomware_Structural_Pattern_Detector_adapters_database_" src="https://github.com/user-attachments/assets/730c8479-ff92-4614-836c-bf61e51b605f" />

# Database Adapter

> **Adapter specification for representing authorized database resource transitions within the Ransomware Structural Pattern Detector without confusing logical data mutation, storage mutation, transaction activity, recovery state, or database availability.**

The Database adapter connects database-visible structural transitions to the Shared Structural Event Grammar.

Its governing rule is:

> **Observe database structure at the layer where evidence exists. Do not silently translate a logical database event into a filesystem event, or a storage event into a logical database conclusion.**

---

## Status

- **Adapter ID:** `rspd-database`
- **Environment:** Database systems
- **Status:** Experimental
- **Role:** Database observation, normalization, capability declaration, bounded response mapping, recovery-state representation, and verification support
- **Normalized observation:** `tf.resource-transition/v0.1`
- **Capability declaration:** `tf.platform-capabilities/v0.1`
- **Decision input:** `tf.containment-decision/v0.1`
- **Execution output:** `tf.response-outcome/v0.1`
- **Verification output:** `tf.verification/v0.1`

---

# Architectural Boundary

A database may expose several distinct structural layers:

**Application / User / Service Actor**

↓

**Database Operation**

↓

**Transaction**

↓

**Logical Database Resource**

↓

**Database Engine**

↓

**Underlying Storage**

A transition observed at one layer must not automatically become an observation at another.

For example:

**logical records changed**

does not by itself establish:

**database storage files were destructively rewritten**

Likewise:

**database storage files changed**

does not by itself establish:

**logical records were maliciously modified**

The adapter preserves the layer from which evidence originated.

---

# Database Resources

Candidate shared resources include:

- database;
- schema;
- table or collection;
- record set;
- configuration;
- transaction state;
- backup;
- snapshot;
- recovery resource;
- replication state;
- database storage;
- audit or history resource;
- domain-defined database resource.

Where the shared resource vocabulary is less specific than the native database model, database-specific detail should remain in adapter configuration, provenance, or extensions rather than redefining the shared grammar.

---

# Actor Semantics

Candidate actors include:

- user;
- application;
- service;
- script;
- administrative process;
- database engine;
- replication service;
- backup service;
- remote actor;
- system;
- unknown actor.

The database engine may be the locally observable actor performing a storage mutation while another application, account, transaction, or remote system originated the logical request.

Therefore:

> **Database engine ≠ necessarily origin actor**

and:

> **Execution account ≠ human intent**

---

# Observation Layers

A concrete adapter may observe one or more layers.

## Logical Observation

Database-native evidence concerning logical resources or operations.

## Transaction Observation

Evidence concerning transaction boundaries, transaction behavior, or resulting state.

## Actor Observation

Evidence associating database activity with an application, service, session, account, or other actor.

## Storage Observation

Evidence concerning underlying storage obtained through another authorized observation source.

## Recovery Observation

Evidence concerning backups, snapshots, history, replicas, or other recoverability structures.

## Replication Observation

Evidence concerning transitions transported between database environments.

Each layer retains its own provenance.

---

# Normalization

Database observations normalize into:

**`tf.resource-transition/v0.1`**

Normalization should preserve:

- observed layer;
- actor;
- resource;
- operation;
- structural action;
- transaction or correlation context where available;
- baseline state;
- direct consequence;
- recovery relationship;
- replication relationship;
- provenance.

The adapter must preserve unknown values rather than filling gaps through assumption.

---

# Correlation

Multiple database observations may describe one underlying transition.

For example:

**Application request**

↓

**Transaction**

↓

**Logical mutation**

↓

**Database-engine storage mutation**

These observations may provide useful lineage without representing four independent destructive events.

The adapter should preserve dependencies so the detector can avoid:

- duplicate event inflation;
- false acceleration;
- exaggerated scope;
- false evidence independence.

---

# Baseline

A database-specific baseline may describe:

- known actors;
- expected application roles;
- typical operation classes;
- ordinary transaction rate;
- normal affected-resource scope;
- normal maintenance activity;
- expected backup activity;
- expected replication behavior;
- established batch workloads.

Deviation from this baseline is evidence to evaluate.

It is not proof of ransomware.

---

# Competing Explanations

Legitimate database activity may produce broad or rapid structural transitions.

Relevant competing explanations can include:

- backup;
- restore;
- migration;
- maintenance;
- archival;
- batch processing;
- application deployment;
- synchronization;
- replication;
- administrative change;
- data transformation;
- testing;
- other authorized bulk activity.

Counter-evidence must remain present when a destructive-pattern hypothesis is assessed.

---

# Recovery Structure

Database recovery requires particularly careful state separation:

**Recovery mechanism exists**

↓

**Usable recovery state is observed**

↓

**Recovery is requested**

↓

**Recovery is attempted**

↓

**Recovery completes**

↓

**Logical database state is verified**

Availability of a backup or recovery mechanism is not proof that restoration will succeed.

Likewise, successful restoration execution is not proof that the resulting logical data state is correct.

---

# Replication

A database transition may propagate across:

- replicas;
- clusters;
- synchronized instances;
- remote services;
- cloud environments;
- other database nodes.

The adapter should preserve:

- origin candidate;
- transport actor;
- source environment;
- recipient environment;
- replication relationship;
- timing;
- evidence dependency.

A replicated transition does not become an independent origin merely because it appears on another database node.

---

# Containment

Potential structural response classes include:

- increase observation;
- notify an authorized operator;
- restrict writes;
- isolate a database resource;
- restrict an actor;
- suspend replication;
- preserve evidence;
- prepare recovery;
- initiate recovery;
- request manual review.

Availability of these actions is implementation-specific.

The generic adapter does not claim that a database system supports any particular enforcement mechanism.

---

# Verification

Post-response verification may evaluate:

- whether destructive logical transitions continue;
- whether another actor continues the pattern;
- whether affected-resource scope expands;
- whether replication reintroduces the condition;
- whether recovery state remains usable;
- whether restored logical state matches the intended bounded baseline;
- whether the adapter possesses sufficient visibility to support the conclusion.

Verification remains bounded to the database resources and environments actually observed.

---

# Core Invariants

## DATABASE-INV-01 — Logical Transition ≠ Storage Transition

A logical database mutation and its underlying storage representation are distinct observations.

## DATABASE-INV-02 — Database Engine ≠ Origin

The engine executing a mutation may not be the actor that originated it.

## DATABASE-INV-03 — Transaction ≠ Intent

A valid transaction does not establish benign intent.

## DATABASE-INV-04 — Bulk Mutation ≠ Ransomware

High-volume database activity requires structural interpretation and competing explanations.

## DATABASE-INV-05 — Replication ≠ Independent Origin

Replicated state must not automatically become independent evidence of multiple originating transitions.

## DATABASE-INV-06 — Capability ≠ Authority

Technical ability to restrict or restore database state does not authorize the action.

## DATABASE-INV-07 — Execution ≠ Resolution

A successfully executed containment operation does not prove the structural condition has resolved.

## DATABASE-INV-08 — Backup Exists ≠ Recovery Verified

Recovery availability, execution, and verified logical restoration are separate states.

## DATABASE-INV-09 — Observation Gap ≠ No Activity

Unavailable history or telemetry cannot establish absence of transitions.

## DATABASE-INV-10 — Provenance Survives Layer Changes

Correlation across application, transaction, logical, storage, replication, and recovery layers must preserve evidentiary lineage.

---

# Shared Contracts

The Database adapter participates in:

- `tf.resource-transition/v0.1`
- `tf.platform-capabilities/v0.1`
- `tf.containment-decision/v0.1`
- `tf.response-outcome/v0.1`
- `tf.verification/v0.1`

The Ransomware Structural Pattern Detector may produce:

- `tf.structural-pattern/v0.1`

---

# Canonical Summary

> **The Database adapter represents authorized database transitions while preserving the distinction between logical mutation, transaction activity, actors, underlying storage, replication, recovery, execution, and verified resulting state.**

Its core rule is:

> **Preserve the layer where the evidence was observed. Correlate across layers without collapsing them.**
