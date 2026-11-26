/-
AACCC / 5Guides Lean Origin Example
07_nawderian_theorem.lean

Purpose:
  Formalize the explicitly declared dimension groups used in the
  Nawderian Theorem and inspect their ordinary membership relations.

Important:
  This teaching model uses predicates over Nat as simple set-like groups.
  It proves membership, shared membership, and a non-containment result.

  It does not define a special meaning for "wraps". If "wraps" means
  something other than ordinary containment, that relation must be
  defined separately before Lean can reason about it.

Student questions:
  1. What groups have actually been declared?
  2. Which dimensions occur in more than one group?
  3. Does ordinary containment support the proposed wrapping idea?
  4. What additional definition would be required for "wraps"?
-/

/-!
## Declared Dimension Groups

We represent each group as a predicate on natural numbers.
This keeps the example self-contained and avoids assuming a richer
set library merely for four small groups.
-/

def Corridor (n : Nat) : Prop :=
  n = 1 ∨ n = 2 ∨ n = 6


def Wrapping (n : Nat) : Prop :=
  n = 3 ∨ n = 6 ∨ n = 9


def Visible (n : Nat) : Prop :=
  n = 4 ∨ n = 5 ∨ n = 6


def Invisible (n : Nat) : Prop :=
  n = 6 ∨ n = 7 ∨ n = 8


/-!
## Awareness

Before interpreting the groups, inspect what has actually been declared.
Each proposition answers a simple membership question.
-/

theorem six_in_corridor : Corridor 6 := by
  exact Or.inr (Or.inr rfl)


theorem six_in_wrapping : Wrapping 6 := by
  exact Or.inr (Or.inl rfl)


theorem six_in_visible : Visible 6 := by
  exact Or.inr (Or.inr rfl)


theorem six_in_invisible : Invisible 6 := by
  exact Or.inl rfl


/-!
## Alignment

Dimension 6 is a shared member of several declared groups.
The next theorem makes one such intersection explicit.
-/

theorem six_shared_visible_invisible :
    Visible 6 ∧ Invisible 6 := by
  constructor
  · exact six_in_visible
  · exact six_in_invisible


/-!
We can also state the shared membership across all four groups.
-/

theorem six_shared_all :
    Corridor 6 ∧ Wrapping 6 ∧ Visible 6 ∧ Invisible 6 := by
  constructor
  · exact six_in_corridor
  · constructor
    · exact six_in_wrapping
    · constructor
      · exact six_in_visible
      · exact six_in_invisible


/-!
## Coherence Check: Ordinary Containment

Suppose we interpret "Wrapping contains Visible" as ordinary logical
set containment:

    for every n, Visible n -> Wrapping n

That interpretation does not follow from the declared groups.
Dimension 4 supplies a counterexample.
-/

theorem four_is_visible : Visible 4 := by
  exact Or.inl rfl


theorem four_not_wrapping : ¬ Wrapping 4 := by
  intro h
  rcases h with h | h | h
  · contradiction
  · contradiction
  · contradiction


theorem visible_not_subset_wrapping :
    ¬ (∀ n : Nat, Visible n → Wrapping n) := by
  intro h
  exact four_not_wrapping (h 4 four_is_visible)


/-!
The same issue appears if we ask whether the union of Visible and
Invisible is ordinarily contained by Wrapping.
-/

theorem visible_or_invisible_not_subset_wrapping :
    ¬ (∀ n : Nat, (Visible n ∨ Invisible n) → Wrapping n) := by
  intro h
  have hWrapping4 : Wrapping 4 := h 4 (Or.inl four_is_visible)
  exact four_not_wrapping hWrapping4


/-!
## Clarity

We have now separated two different statements:

1. 6 is shared by the declared groups.
2. Wrapping ordinarily contains Visible and Invisible.

Lean verifies the first.
Under the definitions in this file, Lean lets us prove that the second
interpretation is false.

That does not tell us that a broader "wrapping" concept is impossible.
It tells us that such a concept needs its own explicit definition.
-/


/-!
## Student Challenge

If the intended idea of "wraps" is not ordinary containment, propose a
new relation such as:

    def Wraps (outer inner : Nat -> Prop) : Prop := ...

Before implementing it, ask:

* What should `Wraps A B` actually mean?
* What evidence would make it true?
* Should it be reflexive?
* Should it be transitive?
* Does sharing one anchor point suffice?

Do not define the relation merely so that the desired theorem becomes
true. Define the intended relationship first, then let Lean test it.
-/


/-!
## Formalization Boundary

Lean has established consequences of the four predicates declared in
THIS file.

It has verified that:

* dimension 6 belongs to all four declared groups;
* Visible and Invisible share dimension 6;
* ordinary containment does not make Visible a subset of Wrapping;
* ordinary containment also does not place the Visible/Invisible union
  inside Wrapping.

Lean has NOT established that:

* the dimension groups describe physical reality;
* dimension 6 has a special physical role;
* the intended source meaning of "wraps" is ordinary containment;
* or a different, properly defined wrapping relation could not hold.

The lesson is structural:

    Shared membership != containment

and:

    A named relationship needs explicit semantics before it can be proved.
-/
