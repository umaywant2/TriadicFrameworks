<img width="1194" height="672" alt="5Guides_shared_privacy_" src="https://github.com/user-attachments/assets/55b02ea8-f209-4a92-bc65-019202ac1681" />

# Privacy

> **Learning does not grant us permission to observe the learner***

Privacy in 5Guides is not an optional feature added after the learning experience is built.

It is part of the design.

The basic principle is simple:

> **Collect only what the learning experience actually needs.**

If we do not need to know something about a learner, our first choice should be **not to collect it**.

---

# Learning Without Surveillance

A student should be able to explore the Five Guides without feeling that the educational material is quietly studying them in return.

The normal learning path is:

```text
Explore
   ↓
Practice
   ↓
Demonstrate
   ↓
Reflect
   ↓
Continue
```

The learner should not have to exchange unnecessary personal information for access to that path.

---

# What We Mean by Privacy

For 5Guides, privacy means designing toward:

- minimal collection;
- voluntary disclosure;
- understandable choices;
- separation between learning and feedback;
- no unnecessary identity requirements;
- no hidden pressure to participate;
- and clear boundaries around anything that is collected.

The goal is not to promise something technically impossible.

The goal is to make sure the implementation reflects the principle:

> **Know less about the learner when knowing more is unnecessary.**

---

# Separate Learning From Measurement

It is easy for educational systems to mix together several different things:

```text
Learning
Assessment
Identity
Analytics
Feedback
Recognition
```

5Guides should keep them separate wherever possible.

In particular:

```text
Learning
    ↓
Mastery
    ↓
Badge
```

should not depend upon:

```text
Optional Feedback
```

A learner who chooses not to provide feedback has still completed the same learning milestone.

---

# No Identity Required Just to Learn

The educational material itself should not require a learner to provide:

- a real name;
- an email address;
- a phone number;
- a school;
- an employer;
- a social-media account;
- an age;
- a gender;
- or another unnecessary personal identifier.

If a future technical implementation requires an account for a particular optional feature, that requirement should be explained separately rather than quietly becoming a requirement for the learning material itself.

---

# Local First Where Practical

When a learner's temporary state can reasonably remain with the learner, prefer that approach.

Examples might eventually include:

- current Guide position;
- unfinished exercises;
- private reflections;
- draft student records;
- or progress through a local activity.

The exact technical implementation will be decided later.

The design preference is:

> **Don't send information somewhere merely because we can.**

---

# Private Reflection Means Private

Many exercises ask learners to reflect.

For example:

> **What changed about how you approached the problem?**

A reflection prompt does not automatically mean:

> **Send us your answer.**

Unless the learner is explicitly invited to submit something, reflection should be treated as belonging to the learner.

They may:

- think about it;
- write it privately;
- discuss it with someone;
- explore it with an AI assistant;
- or simply move on.

---

# AI Is Optional

AI assistance is available as a learning option.

It should never be required simply to understand or complete the ordinary Five Guides experience.

If a learner chooses to use an external AI assistant, that interaction may involve a separate service with its own data practices.

5Guides should therefore encourage learners to avoid unnecessarily sharing:

- personal information;
- private records;
- identifying details;
- sensitive information;
- or information about other people.

The same Awareness question applies:

> **What am I choosing to share?**

---

# Awareness Checks

An Awareness Check asks:

> **What stuck after first exposure?**

Its purpose is educational.

It should not quietly become a behavioral profile of the learner.

A learner may discover:

- what they remembered;
- what they missed;
- what they misunderstood;
- or what they want to revisit.

That result can be useful without becoming permanent analytics.

---

# Mastery

A Mastery Checkpoint asks:

> **Can I use the skill on a fresh problem?**

Mastery should focus on the learner's interaction with the exercise.

It should not require building an unnecessary identity record around the learner.

The educational result is:

> **The defined skill was demonstrated.**

That does not automatically require us to know who the learner is outside the learning experience.

---

# Badges

A badge represents a learning milestone.

For example:

> **Awareness Badge**

means:

> **The Awareness learning journey was completed and its defined skill was demonstrated.**

It does not need to mean:

> **We now require a detailed student profile.**

Badge design should preserve the distinction between:

**recognizing an accomplishment**

and:

**building an identity system.**

---

# Optional Student Footprint

After completing a Guide, a learner may eventually choose to leave a small voluntary Footprint.

The intended minimal form is:

```text
Where are you learning from?
[ Optional country ]

One thought about your experience:
[ Optional short reflection ]
```

No name is required.

No email is required.

No public student profile is required.

Declining to leave a Footprint changes nothing about:

- completion;
- mastery;
- badge status;
- access to the next Guide;
- or the value of the learner's work.

See:

`student_footprint.md`

---

# Ask, Don't Infer

If we want to know the broad country a participating learner wishes to associate with a Footprint, ask them.

Do not design the Footprint around silently inferring it from:

- an IP address;
- device information;
- browser information;
- location services;
- or another hidden signal.

The distinction matters:

> **Information volunteered by the learner is not the same thing as information inferred about the learner.**

---

# Country Is Optional

Prefer:

> **Where are you learning from?**

rather than:

> **Country of origin**

"Country of origin" can suggest:

- nationality;
- birthplace;
- ancestry;
- citizenship;
- or family background.

None of those are required for the purpose of the Footprint.

The field should be optional.

---

# Free Text Needs Extra Care

Even a short reflection can accidentally contain personal information.

A learner might include:

- a full name;
- an email address;
- a phone number;
- a school;
- a workplace;
- a location;
- another person's information;
- or something they later regret making public.

The interface should therefore remind learners:

> **Please do not include personal or identifying information in your reflection.**

If reflections are ever displayed publicly, submission should not automatically mean immediate publication.

Appropriate review and safety controls should be considered during implementation.

---

# Don't Turn Feedback Into Analytics

The Student Footprint exists so a learner can voluntarily leave something behind.

It is not intended to answer questions such as:

- Who visited?
- How long did they stay?
- Which pages did they read?
- What route did they take?
- How often did they return?
- What device did they use?
- Which exercise caused them to leave?
- How can we increase conversion?

Those are different questions.

5Guides begins with a deliberate choice:

> **Curiosity about learners does not automatically justify observing them.**

---

# Silence Is Not Data

Suppose 100 people visit and three voluntarily leave Footprints.

The three Footprints tell us something about those three submissions.

The other visitors did not tell us anything simply by remaining silent.

We should resist turning absence into invented information.

A missing Footprint does not mean:

- the learner disliked the Guides;
- the learner failed;
- the learner did not finish;
- the learner was confused;
- or the learner never existed.

It means:

> **No Footprint was voluntarily provided.**

Nothing more should be inferred.

---

# Don't Build a Shadow Profile

A collection of individually harmless details can become identifying when joined together.

For example:

```text
Country
+
Timestamp
+
Browser
+
Device
+
Exact workflow position
+
Repeated visits
```

may reveal far more than any single field suggests.

So privacy cannot be evaluated only field by field.

Ask:

> **What could these pieces reveal when combined?**

If the combined record begins to resemble a behavioral profile, it has drifted away from the original purpose.

---

# Data Minimization

Before collecting anything, ask:

> **Why do we need this?**

Then:

> **Could the feature work without it?**

Then:

> **Would the learner reasonably expect us to have it?**

If the answer is:

> **It might be useful someday**

that is not enough.

Prefer:

> **Don't collect tomorrow's data today.**

---

# Technical Server Data

A deployed web service may necessarily receive technical information while handling requests.

The exact behavior depends on the eventual architecture, hosting environment, logging configuration, security controls, and services involved.

Those details should be documented once the system actually exists.

Until then, avoid promises such as:

> **No server ever receives any technical information.**

Instead, keep the design commitment precise:

> **5Guides should not intentionally build unnecessary identity, behavioral tracking, or profiling into the learning experience.**

Once implementation begins, the privacy documentation should be updated to describe actual behavior rather than assumptions.

---

# Logging

Operational logging may eventually be necessary for:

- security;
- reliability;
- abuse prevention;
- or diagnosis.

If so, logs should be evaluated separately from learner-facing features.

Ask:

- What is logged?
- Why?
- How long is it retained?
- Who can access it?
- Does it contain identifying information?
- Can the same operational purpose be achieved with less information?

Operational necessity should not become an excuse for unlimited collection.

---

# Retention

If information is collected, ask:

> **How long do we actually need it?**

A voluntary reflection does not automatically need to exist forever.

Operational logs do not automatically need indefinite retention.

A future implementation should establish retention rules appropriate to each type of information actually stored.

The principle is simple:

> **Keeping data forever should require a reason too.**

---

# Deletion and Correction

People change their minds.

Someone may:

- submit something accidentally;
- notice identifying information afterward;
- want a reflection corrected;
- or simply no longer want a contribution displayed.

A future Footprint implementation should anticipate reasonable removal and correction workflows.

Voluntary participation should not become irreversible merely because someone clicked Submit once.

---

# Public Display

Publicly showing a learner's voluntary contribution creates a different privacy boundary from privately receiving it.

If Footprints are displayed:

- keep them minimal;
- avoid unnecessary metadata;
- do not attach engagement statistics;
- do not create public learner histories;
- avoid detailed filtering that could expose individuals;
- and be particularly careful with small groups.

The public board should feel like:

> **A collection of small notes**

not:

> **A searchable database of learners.**

---

# Small Groups Need More Care

Even broad information can become identifying when very few people match it.

For example, a narrow combination of:

```text
Country
+
Guide
+
Date
+
Reflection
```

could reveal more than intended.

Public presentation should therefore avoid unnecessary precision.

When in doubt:

> **Show less.**

---

# No Dark Patterns

Consent should be easy to give and easy to withhold.

Avoid:

> **No thanks, I don't want to help.**

Prefer:

> **Continue without leaving a Footprint**

Do not:

- hide the skip option;
- repeatedly ask after someone declines;
- make the learner feel guilty;
- imply that feedback is necessary for completion;
- or make privacy the inconvenient choice.

A meaningful choice requires a comfortable **no**.

---

# No Privacy Theater

A page can say:

> **We respect your privacy**

while the implementation does something completely different.

That's not enough.

Privacy promises should remain tied to observable implementation.

If the system changes, revisit the promise.

If the promise is wrong, update it.

If an implementation violates the principle, fix the implementation rather than hiding the mismatch behind friendlier wording.

---

# Use AACCC on the Privacy Design

The Five Guides should inspect themselves.

## Awareness

> **What information actually enters the system?**

Include:

- explicit fields;
- technical requests;
- logs;
- third-party services;
- derived information.

Do not stop at the visible form.

## Alignment

> **Does each collected element correspond to a real purpose?**

If a field has no clear purpose, ask why it exists.

## Coherence

> **Do our implementation and our privacy promises agree?**

If we say:

> **We don't track learners**

while quietly building detailed behavioral histories, the design is incoherent.

## Clarity

> **Could an ordinary learner understand what happens to their information?**

Privacy explanations should be written for people, not merely compliance.

## Continuity

> **If the system changes, does the privacy model still hold?**

A new feature may change the answer.

Privacy needs to survive system evolution.

---

# Privacy Is Also a Boundary Problem

Awareness taught us to ask:

> **Where is the boundary?**

For privacy, important boundaries include:

```text
Learner
   ↓
Browser
   ↓
5Guides
   ↓
Hosting Infrastructure
   ↓
Optional External Services
```

Information crossing one boundary may have different consequences from information remaining inside another.

The eventual system design should make those boundaries visible.

---

# Privacy Is Also an Alignment Problem

Every collected field should align with a legitimate function.

For example:

```text
Optional country
        ↓
Broad voluntary learner footprint
```

The relationship is understandable.

But:

```text
Detailed browser fingerprint
        ↓
Broad voluntary learner footprint
```

doesn't obviously align.

That mismatch tells us to stop and ask why the information is being collected.

---

# Privacy Is Also a Coherence Problem

Suppose the project says:

> **We don't need to know who you are.**

Then requires:

> **Full name + email + account**

simply to complete an Awareness exercise.

Those pieces don't hold together.

The privacy promise and the system architecture should describe the same reality.

---

# Privacy Is Also a Clarity Problem

Learners should not need to decode vague phrases such as:

> "Information may be processed for service optimization purposes."

when the system could instead say plainly what happens.

Prefer:

> **This optional form stores the country you select and the reflection you submit.**

when that accurately describes the implemented feature.

Plain language makes privacy inspectable.

---

# Privacy Is Also a Continuity Problem

The first version of 5Guides may be minimal.

Later versions may add:

- badges;
- optional persistence;
- server-backed mastery;
- public Footprints;
- AI integration;
- or new learning tools.

Each addition changes the system.

So ask again:

> **Does the original privacy promise still hold?**

If not, something needs to change.

Privacy cannot be frozen while the implementation evolves around it.

---

# The Core Separation

Keep these two paths distinct:

```text
STUDENT LEARNING

Explore
   ↓
Practice
   ↓
Mastery
   ↓
Badge
   ↓
Continue
```

and:

```text
VOLUNTARY PARTICIPATION

Optional Country
      +
Optional Reflection
      ↓
Optional Footprint
```

One path should not secretly require the other.

---

# What Privacy Success Looks Like

A successful privacy design should allow us to say something like:

> **We built enough system to support the learning experience without building unnecessary machinery for watching the learner.**

And if someone asks:

> **Who visited today?**

sometimes the correct answer should genuinely be:

> **We don't know.**

That's not missing analytics.

That's the consequence of choosing not to collect information we didn't need.

---

# One Final Principle

The Five Guides teach students to inspect systems.

That means the Five Guides themselves should tolerate inspection.

A learner should be able to ask:

> **What are you observing about me?**

and receive a clear answer.

They should be able to ask:

> **Why do you need it?**

and receive a real reason.

They should be able to decline optional participation without losing access to the learning experience.

Most importantly:

> ## **The learner is a participant in the system, not raw material for the system.**

That principle should remain intact as 5Guides grows.

---

## Related

- `student_footprint.md`
- `assessment.md`
- `badges.md`
- `ai_companion.md`

---

> **Collect less. Explain clearly. Ask when appropriate. Respect no. Revisit the promise when the system changes.**
