Sure. In the sample event, the **normalization fields are mainly the fields under normalization in the adapter config plus the provenance and normalized vocabulary in the emitted event.** Their job is to make native observations portable **without pretending the normalization step knows what the event means.**

### The normalization contract
| Field | Meaning | 
|--|--|
| output_schema	| Declares the canonical object produced by normalization. Here, tf.resource-transition/v0.1. |
| preserve_native_operation	| Keeps the original platform operation available instead of throwing it away after mapping it to a shared operation. |
| preserve_provenance	| Requires lineage showing where the normalized observation came from. |
| preserve_unknowns	| Prevents lack of evidence from quietly becoming false, safe, or some other definite state. |
| preserve_event_semantics | Keeps macOS notification evidence distinct from an authorization opportunity. |
| preserve_origin_transport_distinction | Prevents the locally observed actor from automatically becoming the presumed originating actor. |
| preserve_source_dependencies | Keeps relationships among overlapping observations so several reports of one transition aren't automatically treated as independent events. |
| preserve_synchronization_context | Retains evidence that a transition may have arrived through synchronization. |
| preserve_trust_context | Retains available actor trust/identity context without letting it determine whether the behavior is benign. |
| derive_resource_class	| Allows native resources to be mapped into portable structural classes such as user_document. |
| derive_baseline_state	| Allows comparison with established history to produce fields such as operation_typical or rate_typical. |
| redaction_enabled	| Allows sensitive native details to be minimized before the normalized event leaves the adapter. |

### How that appears in the normalized event

Take this fragment from the example:
```json
"event": {
  "source": "filesystem",
  "operation": "write",
  "native_operation": "example-write-notification",
  "phase": "normalized"
}
```
There are three layers here.

**native_operation** preserves what the platform adapter originally called the observation.

**operation** maps that into the shared vocabulary:
```text
native platform observation
        ↓
example-write-notification
        ↓ normalize
write
```
**phase: "normalized"** makes clear that we're looking at the adapter's portable representation, not the raw source event.

That distinction is important because normalization can simplify representation without claiming interpretation.

---

### resource
This part:
```json
"resource": {
  "id": "resource://pseudonymous/document-0087",
  "type": "file",
  "class": "user_document",
  "scope": "local",
  "protected": true,
  "canary": false,
  "recoverable": null,
  "sensitivity": "moderate"
}
```
demonstrates several normalization functions.

type: "file" gives us a general structural type.
class: "user_document" gives us useful semantic classification without exposing the filename.
id is deliberately pseudonymous.

And:
```json
"recoverable": null
```
is particularly important.

It means:
> 
> Recoverability was not established.
> 
It does not mean:
```text
recoverable = false
```
That is preserve_unknowns doing real work.

---

### transition
The transition object converts platform behavior into structural behavior:
```json
"transition": {
  "action": "modify",
  "destructive": null,
  "original_preserved": null,
  "reversibility": "unknown"
}
```
Notice the epistemic restraint.

We know:

**the resource was modified.**

We do not yet know:
- whether the modification was destructive;
- whether an original survives somewhere;
- whether the modification is reversible.

So normalization produces:
```text
write
  ↓
modify
```
but stops before producing:
```text
write
  ↓
destructive transformation
  ↓
ransomware
```
Those latter conclusions require downstream analysis.

---

### characteristics
These fields capture structural properties that may later become evidence:
```json
"characteristics": {
  "size_changed": true,
  "content_changed": true,
  "structure_changed": null,
  "entropy_shift": null,
  "extension_changed": false
}
```
This does not say:
> 
> "The detector found ransomware."
> 
It says something closer to:
> 
> "For this resource transition, size and content changes were established, the extension did not change, and structural/entropy changes were not established."
> 
The structural-pattern detector can later correlate those facts across hundreds of transitions.

### context
```json
"context": {
  "user_intent": "unknown",
  "interactive_session": null,
  "bulk_operation": null,
  "network_origin": null,
  "sync_transport": false
}
```
This is contextual evidence surrounding the transition.

Again, unknown, null, and false mean different things.

For example:
```text
sync_transport = false
```
means the current observation indicates it wasn't synchronization transport.

Whereas:
```text
network_origin = null
```
means network origin wasn't established.

And:
```text
user_intent = "unknown"
```
means the adapter cannot establish user intent.

That is exactly the distinction we want.
```text
baseline
```
This is where normalized history begins becoming analytically useful:
```json
"baseline": {
  "available": true,
  "known_actor": true,
  "operation_typical": false,
  "scope_typical": true,
  "rate_typical": false,
  "resource_typical": true,
  "role_coherent": null
}
```
This says:
- we've seen this actor before;
- this operation is atypical;
- the affected scope is typical;
- the activity rate is atypical;
- this kind of resource is normally associated with the actor;
- we don't yet know whether the overall behavior is coherent with the actor's role.

So even here the result is mixed:
```text
known actor
+ expected resource class
+ expected scope
+ unusual operation
+ unusual rate
+ unresolved role coherence
```
That's much richer than:
```text
suspicious = true
```
And importantly, it preserves evidence that could argue against the ransomware hypothesis.

---

### consequence

The consequence describes what directly resulted from the transition:
```json
"consequence": {
  "state": "resource_changed",
  "propagation_observed": false,
  "recovery_impact": "unknown"
}
```
Again, it stays observational.
We know the resource changed.
We haven't established that recovery was damaged.
We haven't observed propagation.
None of that establishes motivation.

---

### provenance

This is arguably the most important part of normalization:
```json
"provenance": {
  "platform": "macos",
  "adapter": "rspd-macos-endpoint-security-example",
  "adapter_version": "0.1.0",
  "observed_at": "2026-11-26T20:15:32Z",
  "normalized_at": "2026-11-26T20:15:32Z",
  "native_event_ref": "native-event://macos-example/18421",
  "raw_event_retained": true,
  "derivation_refs": [
    "method://macos-es-resource-normalization/v0.1"
  ],
  "redactions": [
    "raw_path",
    "resource_name",
    "user_identity",
    "process_arguments"
  ]
}
```
This gives us the lineage:
```text
native observation
       │
       ├── observed_at
       │
       ▼
macOS adapter
       │
       ├── normalization method
       ├── redaction
       │
       ▼
tf.resource-transition/v0.1
       │
       └── native_event_ref
             points backward
```
So normalization isn't destructive abstraction.

It's **traceable abstraction.**

The normalized object can omit a sensitive pathname while still retaining a local reference through which an authorized implementation could reconstruct the source evidence.

---

### The larger principle

I'd summarize normalization in our architecture as:
```text
Native evidence
      ↓
classify
      ↓
minimize
      ↓
preserve unknowns
      ↓
preserve dependencies
      ↓
preserve provenance
      ↓
map to shared vocabulary
      ↓
tf.resource-transition/v0.1
```
Then, critically:
```text
NORMALIZATION STOPS HERE
────────────────────────
      ↓
correlation
      ↓
counter-evidence
      ↓
assessment
      ↓
tf.structural-pattern/v0.1
```
So normalization answers **"How do we represent what we observed?"**

The detector answers **"What structural pattern might these observations collectively support?"**

That boundary is one of the strongest aspects of what we've built: it lets Windows, Linux, macOS, mobile, cloud-sync, database, and cache adapters speak one structural language **without requiring any of them to prejudge the meaning of their observations.**
