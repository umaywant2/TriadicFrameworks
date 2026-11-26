<img width="1194" height="672" alt="5Guides_clarity_practice_" src="https://github.com/user-attachments/assets/cb9622cc-1159-4053-987c-27c0aa5380d7" />

# Clarity Practice

> Can this be understood well enough to inspect?

You have already explored an important Clarity idea:

Something can make sense in your own head and still be difficult for someone else to understand.

Now we are going to practice making structure visible.

The goal is not to make everything shorter.

The goal is not to make everything simpler.

The goal is:

> Make the important structure easier to inspect without quietly changing what it means.

---

# Start With Meaning

Before rewriting anything, ask:

> What must survive the rewrite?

That may include:

- the main claim;
- an important qualification;
- uncertainty;
- relationships;
- sequence;
- conditions;
- definitions;
- exceptions.

If those disappear, the result may be easier to read while no longer saying the same thing.

---

# The Basic Clarity Check

A useful starting structure is:

```text
Original
   ↓
Identify Meaning
   ↓
Find the Difficulty
   ↓
Revise
   ↓
Compare
```

Then ask:

```text
Is it easier to inspect?

Did the meaning survive?
```

Both questions matter.

---

# Practice 1 — Clean Up the Sentence

Consider:

```text
The project didn't work because communication wasn't good
and some people were doing different things because they
understood the plan differently, although everyone thought
they understood what the group was trying to do.
```

There is probably a useful idea in there.

But it is difficult to inspect.

Try separating the structure.

For example:

```text
The group agreed on the goal.

Members interpreted the plan differently.

Because those differences were not noticed,
people began working in different directions.
```

Now we can see:

```text
Shared Goal
     ↓
Different Interpretations
     ↓
Different Actions
```

The structure became more visible.

---

# What Changed?

Compare the two versions.

Ask:

> What was removed?

> What was made explicit?

> What relationship became easier to see?

> Did the revision introduce anything new?

That final question protects the original meaning.

---

# Shorter Is Not Always Clearer

Imagine:

```text
Original:
The system may be unstable when request volume
increases rapidly under some operating conditions.
```

Someone shortens it to:

```text
High traffic makes the system unstable.
```

Much shorter.

Also stronger.

The new sentence changed:

```text
may
```

into:

```text
does
```

and removed:

```text
under some operating conditions
```

Cleaner?

Maybe.

Equivalent?

No.

---

# Practice 2 — Preserve the Qualification

Rewrite this:

```text
The available observations suggest that the configuration
change may have contributed to the slowdown, but there is
not enough information yet to identify the cause.
```

Try to make it easier to read without losing:

```text
suggest

may

not enough information

cause not yet established
```

After rewriting, compare the versions.

Ask:

> Did uncertainty survive?

That is part of the meaning.

---

# Clarity and Confidence

Clarity sometimes gets confused with confidence.

Consider:

```text
Version A:
This pattern may indicate a relationship.

Version B:
This pattern indicates a relationship.

Version C:
This pattern proves the relationship.
```

The sentences become more confident.

They do not necessarily become more accurate.

Clarity should make uncertainty visible when uncertainty is part of the structure.

---

# Practice 3 — Confidence Ladder

Take this statement:

```text
The evidence is consistent with the proposed explanation.
```

Create three versions:

```text
More cautious:
...

Same strength, clearer:
...

Too strong:
...
```

Then ask:

> Which version best preserves the original claim?

You are practicing semantic control.

---

# Define the Important Word

Sometimes a sentence is unclear because one important word is carrying too much work.

For example:

```text
The system is stable.
```

What does stable mean?

Perhaps:

```text
No crashes?

Low variation?

Predictable output?

No state transitions?

Acceptable response time?

Returns to equilibrium?
```

Without a definition, different readers may inspect different claims.

---

# Practice 4 — Define Before Explaining

Choose one word:

```text
stable

aligned

finished

safe

available

successful

coherent
```

Write:

```text
In this problem, I mean:
...
```

Then use the term in a sentence.

Did the definition make the relationship easier to inspect?

---

# Ambiguity

A statement is ambiguous when it reasonably supports more than one interpretation.

Consider:

```text
Alex told Jordan that their result was wrong.
```

Whose result?

Alex's?

Jordan's?

A shared result?

The grammar permits more than one interpretation.

---

# Practice 5 — Remove the Ambiguity

Rewrite:

```text
Alex told Jordan that their result was wrong.
```

in two different ways, each expressing a different intended meaning.

For example:

```text
Meaning A:
...

Meaning B:
...
```

The original sentence did not necessarily contain a factual error.

It contained insufficient Clarity.

---

# Missing Steps

Sometimes the beginning and end are clear while the middle has disappeared.

For example:

```text
The service was slow.

Therefore we increased the database capacity.
```

Why?

The decision may be perfectly reasonable.

But the reasoning is hidden.

Perhaps:

```text
Service was slow
      ↓
Database latency was measured
      ↓
Database resource saturation was observed
      ↓
Capacity increase was chosen
```

Now the path is inspectable.

---

# Practice 6 — Show the Middle

Consider:

```text
The experiment produced an unexpected result.

Therefore the model was revised.
```

Add enough middle structure to make the transition inspectable.

Do not invent facts.

If the missing information is not available, write:

```text
Missing:
The evidence connecting the unexpected result
to the model revision is not provided.
```

Exposing the gap is also Clarity.

---

# Don't Fill Gaps With Imagination

This matters.

If the source says:

```text
A happened.

Then C happened.
```

Clarity does not give us permission to invent:

```text
B
```

just because:

```text
A → B → C
```

would make a nicer explanation.

You can say:

> The relationship between A and C is not yet explicit.

That's clearer than manufacturing a bridge.

---

# Clarity Can Reveal Coherence Problems

Sometimes a structure looks fine until you make the steps explicit.

For example:

```text
A
therefore
D
```

may sound convincing.

But expanding the reasoning gives:

```text
A
 ↓
B
 ↓
C
 ↓
D
```

and suddenly:

```text
B → C
```

does not hold.

Clarity helped expose a Coherence problem.

The Guides are working together again.

---

# Before and After

A useful Clarity practice is comparing two versions.

Use:

```text
BEFORE

...

AFTER

...

WHAT CHANGED

...

MEANING PRESERVED

...

MEANING CHANGED

...
```

That final comparison is important.

Do not assume the rewrite preserved meaning simply because you intended it to.

---

# Practice 7 — Before and After

Start with:

```text
The software stopped working after the update,
so the update obviously broke something and
we should roll it back.
```

Create a clearer version that separates:

```text
Observation

Interpretation

Proposed action
```

For example:

```text
Observation:
...

Interpretation:
...

Possible action:
...
```

Now the reader can inspect each layer separately.

---

# Separate Claim From Evidence

Consider:

```text
The new design is better because users like it more.
```

This mixes several layers.

Try:

```text
Claim:
...

Evidence:
...

Definition of better:
...

Uncertainty:
...
```

Perhaps the problem is not the sentence.

Perhaps the word:

```text
better
```

needs definition.

---

# Practice 8 — Claim / Evidence / Assumption

Take a short argument and separate it into:

```text
Claim:
...

Evidence:
...

Assumption:
...

Uncertainty:
...
```

Now ask:

> Which part was hardest to identify?

Hidden assumptions often become visible here.

---

# Clarity in Instructions

Instructions deserve special attention because someone is expected to act on them.

Consider:

```text
Put it over there after you finish the other thing.
```

Perfectly clear to the person who already knows what everything means.

Not very useful to anyone else. 😉

---

# Practice 9 — Make the Action Inspectable

Rewrite an instruction so another person can determine:

```text
What to act on

What action to take

When to do it

Where the result goes

What completion looks like
```

Do not add unnecessary detail.

Clarity is not word count.

It is usable structure.

---

# Technical Clarity 💻

Technical systems are especially good Clarity practice.

Consider:

```text
The script processes files from the input directory
and if there's a problem it doesn't process them
and writes the problem to the log unless logging
isn't enabled.
```

Questions immediately appear:

- Does one failure stop all processing?
- Is only the failed file skipped?
- Does processing continue?
- What happens when logging is disabled?
- What does "doesn't process them" refer to?

The sentence contains technical behavior that is difficult to inspect.

---

# Practice 10 — Expose the Behavior

Try representing the behavior as:

```text
For each file:

1. Attempt processing.

2. If processing succeeds:
   ...

3. If processing fails:
   ...

4. If logging is enabled:
   ...
```

But be careful.

If the original text never said whether processing continues after failure, do not invent the answer.

Instead:

```text
Unspecified:
Whether processing continues after a file fails.
```

That is a Clarity improvement.

---

# Technical Diagrams

Sometimes prose is not the clearest representation.

A small process structure may work better:

```text
Input
  ↓
Process
  ↓
Success? ── yes ──→ Continue
  │
  no
  ↓
Record Failure
```

The important question is not:

> Is a diagram prettier?

It is:

> Does this representation make the relationships easier to inspect?

Use the representation that serves the structure.

---

# Practice 11 — Change the Representation

Take a short technical paragraph.

Express it as:

```text
Sequence
```

or:

```text
Table
```

or:

```text
State transition
```

or:

```text
Simple diagram
```

Then compare.

Ask:

> What became easier to see?

> What became harder to see?

> Did the representation lose any important meaning?

A different representation can improve one kind of Clarity while weakening another.

---

# Clarity Through Tables

Tables can help when several objects share the same attributes.

For example:

| State | Requests | Response Time | Failures |
|---|---|---|---|
| A | Normal | Normal | Normal |
| B | Normal | Increasing | Increasing |

The table makes comparison easier.

But a table may hide chronology, explanation, or uncertainty.

Again:

> Representation should serve the question.

---

# Clarity Through Labels

Sometimes the smallest useful improvement is a label.

Compare:

```text
20
20
95
```

with:

```text
Sensor A: 20 °C
Sensor B: 20 °C
Sensor C: 95 °C
```

More meaning became visible.

Now add:

```text
Sensor C location:
exhaust vent
```

Suddenly the apparent mismatch may require another interpretation.

Labels can change what we are able to inspect.

---

# Units Are Clarity

Consider:

```text
Temperature = 20
```

Twenty what?

```text
20 °C
```

is clearer.

Now:

```text
Distance = 5
```

Five meters?

Miles?

Kilometers?

Units are not decorative.

They are part of the meaning.

---

# Practice 12 — Find the Missing Unit

Look at:

```text
Time = 5

Temperature = 30

Distance = 12

Speed = 60
```

Ask:

> What would I need before these values become safely interpretable?

Then add units appropriate to a hypothetical example.

Make it clear that the units were supplied by the example rather than discovered from the original unlabeled values.

---

# Clarity Through Examples

Sometimes a definition is technically correct but hard to understand.

An example can help.

For instance:

> Boundary means the part of the system currently included in your observation.

Then:

```text
Example:

Looking only at one bicycle wheel
uses a different boundary from
looking at the entire bicycle.
```

The example gives the definition somewhere to land.

---

# Examples Can Mislead Too

One example can accidentally become the definition in the learner's mind.

If every Alignment example uses physical objects, the learner may begin to think Alignment applies only to physical objects.

Use varied examples.

Then ask:

> What structure stayed the same across them?

That supports transfer.

---

# Practice 13 — Two Examples, One Structure

Choose a concept.

Explain it with:

```text
Everyday example:
...

Technical example:
...
```

Then add:

```text
Shared structure:
...
```

If you cannot identify the shared structure, your examples may not actually align.

---

# Clarity and Detail

Too little detail creates ambiguity.

Too much detail can bury the important relationship.

Imagine directions containing every visible object along the route.

Technically detailed.

Operationally miserable.

Clarity asks:

> Which details matter for the task?

Not:

> How much information can I include?

---

# Practice 14 — Remove Without Losing

Take a paragraph you wrote.

Remove one sentence.

Ask:

> Did meaning change?

Remove another.

Ask again.

Continue until removing more would damage the important structure.

You have found something close to the minimum useful explanation.

Not necessarily the shortest possible explanation.

The smallest one that still does the job.

---

# Clarity and Audience

An explanation that is clear to an expert may be unclear to a beginner.

That does not mean the expert explanation is bad.

It means:

> Clarity is partly relational.

Ask:

> Clear to whom?

Then:

> For what purpose?

A student guide and a formal specification may appropriately explain the same structure differently.

---

# Practice 15 — Two Audiences

Explain:

```text
A software state transition
```

to:

```text
A first-time student
```

Then explain the same idea to:

```text
A software developer
```

Compare the versions.

Ask:

> What changed because of audience?

> What meaning had to remain?

This is Clarity with Continuity.

---

# Clarity and Precision

Plain language and technical precision do not have to be enemies.

A useful pattern is:

```text
Plain explanation
      ↓
Precise definition
      ↓
Example
```

For example:

```text
Plain:
Drift is gradual movement away from an earlier state or relationship.

Precise:
Define what state or relationship is being compared.

Example:
Version 1 preserves uncertainty;
Version 4 has removed it.
```

Each layer supports another.

---

# Clarity and Formalization

Formalization can greatly improve precision.

It can also become unreadable to someone unfamiliar with the notation.

A formal artifact may therefore need two layers:

```text
Formal statement
      ↕
Plain-language interpretation
```

The mapping between them should remain inspectable.

This is one reason the Lean examples include explanatory comments.

---

# Practice 16 — Translate a Formal Statement

Take a small statement such as:

```text
a = b
```

Then:

```text
double a = double b
```

Explain in plain language what relationship is being preserved.

Then ask:

> Did my explanation add anything the formal statement did not say?

Translation is another kind of Clarity work.

---

# Clarity in Lean 4

The optional formal companion is:

```text
04_clarity.lean
```

Lean can accept more than one proof of the same theorem.

One proof may be compact.

Another may expose intermediate relationships.

The useful question becomes:

> Which proof makes the relevant structure easier to inspect for this learner?

Correctness matters.

So does communication.

---

# Compact Is Not Automatically Better

A one-line proof can be elegant.

It can also hide the reasoning a learner needs to see.

A longer proof can be educational.

It can also contain unnecessary noise.

There is no universal best length.

The question is:

> What should be visible here?

---

# Practice 17 — Compare Two Proof Styles

When reading two Lean proofs of the same result, ask:

```text
Which is shorter?

Which exposes more intermediate structure?

Which is easier for me to inspect?

Which would I use in a teaching example?

Which would I use after I understood the theorem?
```

The answers may differ.

That's fine.

---

# Clarity and AI 🤖

AI can be a useful Clarity partner.

Try:

> Rewrite this more clearly without adding new claims.

Or:

> Identify ambiguous terms.

Or:

> Separate observation, interpretation, and assumption.

Or:

> Tell me what you removed from your rewrite.

Or:

> Compare the original and revised versions for meaning drift.

That last prompt is especially useful.

---

# AI Can Make Things Too Smooth

AI is often good at producing polished prose.

That can create a risk.

A rough statement containing uncertainty may become a smooth statement containing confidence.

For example:

```text
Original:
The results may indicate a relationship.

AI rewrite:
The results demonstrate a clear relationship.
```

The writing improved.

The claim changed.

That's not a Clarity win.

---

# Practice 18 — Audit an AI Rewrite

Give AI a short paragraph and ask it to improve the wording.

Then create:

```text
Added claims:
...

Removed qualifications:
...

Changed definitions:
...

Preserved meaning:
...

Possible drift:
...
```

Now the AI rewrite becomes practice material.

---

# Clarity and Citation

A claim may be easy to read but difficult to verify.

If evidence matters, Clarity includes making the support visible.

For example:

```text
Claim:
...

Source:
...

Source supports:
...

Interpretation:
...
```

This helps prevent:

```text
Source exists
```

from silently becoming:

```text
Source proves every claim around it.
```

Provenance supports Clarity.

---

# Clarity and Uncertainty

Uncertainty should not be hidden merely because it makes a statement less tidy.

Useful phrases include:

```text
The available evidence suggests...

One possible interpretation is...

This relationship has not yet been established.

Additional information is needed.

The result is consistent with...

The current model does not explain...
```

When accurate, these phrases preserve useful structure.

---

# But Don't Hide Behind Vagueness

There is another extreme.

A statement can become so cautious that it says almost nothing.

For example:

```text
It may perhaps possibly be conceivable
that something could be happening.
```

😄

Uncertainty should be precise too.

Ask:

> What exactly am I uncertain about?

Then say that.

---

# Practice 19 — Precise Uncertainty

Instead of:

```text
We're not sure.
```

try:

```text
We observed A and B.

We do not yet know whether A caused B.

We would need C to test that relationship.
```

That is clearer uncertainty.

---

# Your Clarity Record

For a larger practice problem, use:

```text
CLARITY RECORD

Original:
...

Audience:
...

Purpose:
...

Meaning to Preserve:
...

Ambiguous Terms:
...

Hidden Assumptions:
...

Missing Steps:
...

Uncertainty:
...

Revised Version:
...

What Changed:
...

What Was Removed:
...

What Was Added:
...

Meaning Preserved:
...

Possible Meaning Drift:
...

Current Judgment:
Clear / Partly Clear / Unclear
```

Use only the fields that help.

The record is a thinking tool, not paperwork.

---

# A Fresh Practice Problem

Consider this technical update:

```text
We changed the service because the old configuration
wasn't working correctly and the new one should fix
the performance issue unless the problem is somewhere
else, in which case we'll probably need to change
something else.
```

Your task:

1. Identify what is actually being claimed.
2. Separate observation from proposed explanation.
3. Identify uncertainty.
4. Identify missing evidence.
5. Rewrite the update so another person can inspect it.

Do not invent the missing technical details.

If something is unknown, leave it unknown.

---

# Possible Structure

You might use:

```text
Observed Problem:
...

Change Made:
...

Reason for Change:
...

Expected Result:
...

Uncertainty:
...

Next Check:
...
```

Notice how the structure itself improves Clarity before any wording is polished.

---

# Earlier Guides Still Matter

Use them while practicing Clarity.

## Awareness

What did the original actually say?

## Alignment

Does the revised version correspond to the original meaning?

## Coherence

Does the clarified structure still hold together?

## Clarity

Can another person now inspect it?

Soon Continuity will add:

> Did the meaning survive the revision over time?

---

# Clarity Self-Check

Before moving to Mastery, ask:

```text
Can I identify the meaning that must be preserved?

Can I locate ambiguity?

Can I expose missing steps?

Can I make assumptions visible?

Can I preserve uncertainty?

Can I change representation when useful?

Can I adjust for audience without changing the claim?

Can I compare before and after for meaning drift?

Can another person inspect the important structure?
```

If most of those answers are yes, you are practicing Clarity.

---

# Before Mastery

One last reminder.

Clarity is not:

```text
Shorter
```

It is not:

```text
More confident
```

It is not:

```text
More technical
```

It is not:

```text
More polished
```

Clarity is closer to:

> The important meaning and relationships are visible enough to inspect.

Sometimes that is short.

Sometimes detailed.

Sometimes prose.

Sometimes a table.

Sometimes a diagram.

Sometimes a formal definition.

Use what makes the structure visible without changing what matters.

---

# Continue

When you're ready, continue to:

`mastery.md`

Or revisit:

`explore.md`

Optional formal companion:

`../lean/04_clarity.lean`

AI guidance:

`../shared/ai_companion.md`

Assessment guidance:

`../shared/assessment.md`

---

## Current Position

```text
Awareness       ✓
Alignment       ✓
Coherence       ✓
Clarity         ← You are here
Continuity
```

---

> Clarity is not polishing an idea until it sounds convincing. It is making the idea visible enough that someone else can inspect what it actually says.
