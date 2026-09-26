# The TriadicFrameworks Canon

> **This page is the authoritative reference for the five canon commitments.**
> It is not a tutorial. For a full unpacking of each commitment — with examples,
> failure modes, and operational implications — see [Part I, Chapter 2](./part-i#chapter-2--the-canon-unpacked).
> This page is the document you cite. Part I is the document you read to understand.

---

## Status of This Document

The canon is **permanent and author-controlled.** Its five commitments cannot be added to,
removed from, modified, or reframed through any contribution process. They are not open
for community revision. Any PR touching the content of this page or the five backing
anchor modules will be closed without review.

If you believe a canon commitment is wrong, bring that concern directly to the author.
Do not express it through a pull request.

**Backing authority:** Each commitment is formally specified in a foundational anchor
module in the registry. The module ID is listed with each commitment. The anchor module
is the machine-readable specification; this page is the human-readable declaration.

**Relationship to the rest of the system:** Every module, session, output, and
contribution in TriadicFrameworks exists *within* the canon — constrained by it,
not in addition to it. A component that violates a canon commitment is not a valid
component of this system, regardless of its quality on other dimensions.

---

## The Canon Declaration

The TriadicFrameworks canon is the set of five irreversible commitments that define
what this system is, what it does, and who made it. The canon is not derived from the
system's modules — the modules are derived from the canon. It is the outermost boundary.
Nothing in the system stands outside it.

The five commitments are stated below in their canonical form. These are the precise
statements. Do not paraphrase them when citing the canon. Do not summarize them when
the full statement is called for. Quote them exactly.

---

## Commitment I — RTT Is the Engine

**Canonical Statement:**
> Recursive Triadic Thinking is the governing engine of the TriadicFrameworks system.
> It is not one methodology among many. It is the structural substrate from which every
> module, session, and output in the system is derived. No practitioner, module, or
> session may operate the system while setting RTT aside.

**Backing Anchor Module:** `canon-anchor-rtt-engine` `[anchor / foundational]`

**What This Commitment Means:**

RTT is not a tool you can choose to apply or not apply depending on the problem.
It is not a framework you adopt for certain session types and skip for others.
It is the engine — the mechanism by which the system produces its outputs.
Every module was specified using RTT. Every session grammar field was defined
using RTT. Every validator criterion was calibrated using RTT. The system is
RTT applied recursively to itself.

A practitioner who produces an output without applying RTT has not produced a
TriadicFrameworks output. They have produced something else using TriadicFrameworks
vocabulary. These are not the same thing.

**What This Commitment Prohibits:**

- Invoking modules without applying RTT to the session's input
- Producing outputs by direct inference, intuition, or pattern-matching and then
  formatting them as StructuredFaces
- Treating RTT as an optional verification step applied after content is already
  decided
- Substituting any other analytical framework — however compatible it may seem —
  for RTT as the primary parsing mechanism

**What Breaks If This Is Violated:**

Outputs become uncheckable. The system's validators are calibrated to evaluate
RTT-derived outputs — outputs that have a generative face, a present face, and a
terminal face produced by genuine triadic parsing. An output produced by a different
mechanism may pass the format check while failing the substantiveness check.
The session appears to complete; the output is structurally hollow. This is the
most dangerous failure mode because it is invisible.

---

## Commitment II — Clarity Is Precision, Not Comfort

**Canonical Statement:**
> Clarity in TriadicFrameworks is defined as signal coherence across validator layers,
> formalized in the Nawderian Theorem of Validator Pulses. It is not a subjective sense
> of understanding. It is not agreement with prior belief. It is not comfort. Outputs
> are evaluated against a structural criterion — not against how a practitioner feels
> about them.

**Backing Anchor Module:** `canon-anchor-clarity-standard` `[anchor / foundational]`
**Theorem Module:** `nawderian-theorem-validator-pulses` `[anchor / foundational]`

**What This Commitment Means:**

The system will sometimes produce outputs that are uncomfortable — that name origins a
practitioner would prefer not to acknowledge, identify failures a practitioner is
implicated in, or describe futures that require difficult action. These outputs are not
errors. They are the system working correctly.

Clarity is a structural property of an output, not a psychological property of the
person reading it. A clear output is one where:
- The signal is high — specific, checkable claims, not vague directional assertions
- The coherence is high — no internal contradictions, no scope violations, no
  drift from the declared intent
- Both properties hold across all validator layers simultaneously

A comfortable output that fails on signal or coherence is not clear. An uncomfortable
output that passes on both is clear. The validator does not know the difference between
comfortable and uncomfortable. It measures signal and coherence. The practitioner's
job is to accept what the validator accepts and revise what the validator flags —
not to accept what feels right and re-run what feels wrong.

**What This Commitment Prohibits:**

- Comfort-filtering: re-running a session until a more agreeable output appears,
  then accepting that one without validator confirmation that it is more correct
- Treating agreement with prior beliefs as evidence of output quality
- Overriding a validator `accept` recommendation because the output is unwelcome
- Overriding a validator `revise` or `re-run` recommendation because the output
  is satisfying

**What Breaks If This Is Violated:**

The system becomes a mirror. A practitioner who filters by comfort will, over time,
produce a body of work that validates their existing beliefs — which is precisely
what a precision system is designed to prevent. The validators become decorative.
The module architecture becomes scaffolding for predetermined conclusions.
The system's value collapses to zero while its vocabulary remains intact.
This is the failure mode that is hardest to detect from the inside.

---

## Commitment III — Modules Are the Unit of Knowledge

**Canonical Statement:**
> Knowledge in TriadicFrameworks is stored and transmitted in modules, not in prose.
> A module is a structured knowledge unit with a defined role, layer, scope, version,
> and dependency map. Prose alone — however accurate, however clear — is not a valid
> unit of knowledge in this system. Every claim the system makes is made by a module
> or depends on one.

**Backing Anchor Module:** `canon-anchor-module-unit` `[anchor / foundational]`

**What This Commitment Means:**

A document can express knowledge. A module *is* knowledge — in a form the system
can traverse, version, validate, and compose. The distinction is not pedantic.
A document cannot be called from another document. Its claims cannot be automatically
checked for consistency with adjacent documents. Its version history does not propagate
to the documents that depend on it.

A module can do all of these things. When you invoke a module in a session, you
gain access to a versioned, scoped, dependency-mapped unit of knowledge — not just
a reference to prose that you must then interpret. This is why the system can
validate outputs: because its knowledge units have structure that validators can
check against.

This commitment also means that the system knows what it does not know. A gap in the
module registry is a declared absence — the system can say "no module covers this"
because modules are the unit of knowledge. A prose-based system cannot make that
declaration; it can only say "I could not find text that covers this."

**What This Commitment Prohibits:**

- Treating well-written prose as equivalent to a ratified module
- Adding knowledge to the system by editing book content without backing it
  with a module specification
- Invoking knowledge in a session without declaring which module that knowledge
  comes from
- Building sessions on information that has no module backing in `active_modules`

**What Breaks If This Is Violated:**

Knowledge accumulates in a form the system cannot traverse. The registry becomes
incomplete relative to what practitioners actually use. Sessions invoke knowledge
that is unversioned and unvalidatable. Over time, the gap between what the registry
declares and what practitioners assume produces a shadow system — undeclared,
untested, and structurally invisible.

---

## Commitment IV — Sessions Are the Unit of Application

**Canonical Statement:**
> Every application of TriadicFrameworks happens inside a session. A session is a
> bounded operational container governed by the 9-field session grammar. No application
> of the system — however small, however informal — produces a valid TriadicFrameworks
> output outside of a correctly initialized session.

**Backing Anchor Module:** `canon-anchor-session-unit` `[anchor / foundational]`
**Grammar Specification:** `session-grammar-anchor` `[anchor / foundational]`

**What This Commitment Means:**

The session is not administrative overhead. It is the mechanism by which the system
produces reproducible outputs. Two practitioners running the same session — same nine
fields, same input, same modules — should produce structurally equivalent outputs.
The session grammar is what makes this possible. Without it, outputs depend on
implicit context that varies by practitioner, by day, by mood, by how the problem was
framed in conversation before the session began.

The nine fields are not suggestions. Each field exists because a class of session
failures was traced to its absence. The intent field exists because sessions without
declared intent wander. The scope field exists because sessions without declared
boundaries creep. The `active_modules` field exists because sessions without declared
knowledge units invoke unversioned, uncheckable knowledge. The validator field exists
because sessions without a declared correctness criterion produce outputs that cannot
be distinguished from noise.

A session that closes before all nine fields have been populated is not a completed
session. It is an abandoned one.

**What This Commitment Prohibits:**

- Applying RTT to a problem without a declared session context
- Producing an output and calling it a TriadicFrameworks result when no session
  grammar was initialized
- Treating session fields as optional based on the perceived simplicity of the task
- Shortcutting the grammar for "quick" analyses — the grammar's value is highest
  precisely when the analysis feels like it should be quick

**What Breaks If This Is Violated:**

Outputs become unreproducible. A practitioner who produces a strong insight outside
a session cannot hand it to another practitioner for verification, extension, or
replication. They cannot return to it themselves with confidence that the context
is preserved. The insight exists — but it is not a system output. It is a personal
observation that happens to use the system's vocabulary.

---

## Commitment V — Attribution Is Honest

**Canonical Statement:**
> TriadicFrameworks was authored by Nawder Loswin — a pen name for the system's
> human author — with AI-augmented authorship. The AI was used as a precision
> instrument in a human-directed creative and analytical process. It was not a
> co-author. It did not make the system's foundational decisions. Every canon
> commitment, every module scope, every design decision is the product of human
> authorial intent. The AI extended the author's capability; it did not substitute
> for the author's judgment.

**Backing Anchor Module:** `canon-anchor-attribution` `[anchor / foundational]`

**What This Commitment Means:**

Attribution in this system is not a formality. It is a structural commitment that
makes the system's lineage auditable. When a canon commitment is questioned, there
is a human intelligence whose reasoning produced it — and whose reasoning can be
examined, challenged, and held accountable. When a foundational design decision
seems arbitrary, there is an authorial intention behind it that can be retrieved and
evaluated.

If AI authorship were attributed creative agency it did not have, the system's
lineage would be falsified in a specific way: the canon's commitments would become
outputs of an anonymous process rather than decisions made by a named intelligence
with a declared intent. Future contributors would not know which commitments to
treat as load-bearing and which to treat as suggestions. The distinction between
"the author decided this" and "the model produced this" would collapse — and with it,
the system's accountability structure.

**The pen name:** Nawder Loswin is a pen name derived from the phrase "one who wanders
inward." It is the author's chosen public identity for this work. It is not an alias
for concealment — it is a deliberate creative identity, fully owned and consistently
maintained.

**What This Commitment Prohibits:**

- Attributing authorial agency to the AI in any TriadicFrameworks document,
  module, or session record
- Claiming co-authorship for any component of the system
- Obscuring the human author's role in any contribution context
- Using the AI-augmented authorship disclosure to diminish the system's
  intellectual seriousness or the author's accountability for its content

**What Breaks If This Is Violated:**

The system loses its accountability structure. No specific module will malfunction.
No session will produce different outputs. But the system as a whole becomes
attributable to no one — a body of work with no responsible author, no accountable
intelligence, no one to ask when the canon seems wrong. Systems without accountable
authors drift. Their canon weakens over time because there is no voice with the
authority to say "no, that is not what this commits to." Attribution is the
mechanism that keeps the canon honest across time.

---

## The Five Commitments: Reference Summary

| # | Name | Formal ID | Prohibits |
|---|------|-----------|----------|
| I | RTT Is the Engine | `canon-anchor-rtt-engine` | Operating the system without applying RTT |
| II | Clarity Is Precision, Not Comfort | `canon-anchor-clarity-standard` | Filtering outputs by comfort rather than validator assessment |
| III | Modules Are the Unit of Knowledge | `canon-anchor-module-unit` | Storing or invoking knowledge outside the module architecture |
| IV | Sessions Are the Unit of Application | `canon-anchor-session-unit` | Producing system outputs outside an initialized session |
| V | Attribution Is Honest | `canon-anchor-attribution` | Misattributing authorial agency or obscuring the author's role |

---

## How to Cite the Canon

When referencing a canon commitment in a module, session, or book contribution,
cite it by commitment number and the backing anchor module ID. Do not paraphrase
the canonical statement.

**Correct:**
> This session is governed by Commitment I (`canon-anchor-rtt-engine`): RTT is the
> governing engine. The input must be processed through a complete RTT pass before
> any output is produced.

**Incorrect:**
> This session uses the RTT approach as its main method.

The canonical statement is precise for a reason. Paraphrasing it introduces
ambiguity. Ambiguity in a foundational reference is not a stylistic issue —
it is a structural error.

---

## What the Canon Is Not

**The canon is not the complete system.**
The five commitments define the system's irreversible boundaries. They do not
specify every module, every session pattern, or every valid output. The system
has enormous latitude within the canon — hundreds of modules, dozens of session
types, multiple lens combinations, an open gap-filling process. The canon is the
floor, not the ceiling.

**The canon is not a checklist.**
The commitments are not steps to follow — they are constraints to operate within.
You do not "complete" Commitment I and move on to Commitment II. All five apply
simultaneously to every session, every module, and every output.

**The canon is not the same as the book.**
The book unpacks the canon, illustrates it, and applies it. The book can be
updated, expanded, and revised. The canon cannot. When the book and the canon
appear to conflict, the canon is correct. Report the conflict as a book error.

**The canon is not negotiable on a per-session basis.**
No session grammar field, no practitioner preference, no urgency, and no
outside authority can suspend a canon commitment for a given session.
The canon applies to every session equally, without exception.

---

## Further Reading

- **Part I, Chapter 2** — [The Canon Unpacked](./part-i#chapter-2--the-canon-unpacked): full treatment of each commitment with failure modes, operational implications, and the constraint model
- **Part III, Chapter 17** — [The Four Canonical Session Failure Modes](./part-iii#chapter-17--the-four-canonical-session-failure-modes): how canon violations manifest in live sessions
- **Contributing Guidelines** — [What You Cannot Contribute](../contributing#what-you-cannot-contribute): the contribution rules derived from the canon

---

→ [Return to Book Index](./index)
→ [Module Registry](./registry)
→ [Part I — Orient](./part-i)

---

*TriadicFrameworks Book — `/docs/book/canon.md`*
*Authored by Nawder Loswin. AI-augmented authorship. All rights reserved.*
