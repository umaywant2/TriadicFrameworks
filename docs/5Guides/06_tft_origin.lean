/-
AACCC / 5Guides Lean Origin Example
06_tft_origin.lean

Purpose:
  Formalize one small, inspectable structure inspired by the
  triadic organization used in the Triadic Framework for Everything.

Important:
  This file does not formalize TFT's broader physical or
  cosmological proposals.

  It introduces a generic three-part structure and proves
  properties of transformations applied to that structure.

Student questions:
  1. What structure has actually been declared?
  2. Which outputs correspond to which inputs?
  3. What survives when a transformation is applied?
  4. What has Lean proved?
  5. What has NOT been proved?
-/

/-!
## A Generic Triad

The three positions are intentionally generic.

They do not yet mean "Light", "Darkness", dimensions,
physical quantities, or anything else.

That keeps the formal claim small and inspectable.
-/

structure Triad (α : Type) where
  first  : α
  second : α
  third  : α
  deriving Repr, DecidableEq

/-!
## Transform a Triad

`map` applies the same transformation to each position.
-/

def Triad.map {α β : Type} (f : α → β) (t : Triad α) : Triad β :=
  {
    first  := f t.first
    second := f t.second
    third  := f t.third
  }

/-!
## Awareness

Before proving anything, inspect what has been declared:

* `Triad α` contains exactly three values of type `α`.
* `map` does not add or remove positions.
* `map` applies `f` independently to each position.

The structure is the observation.

Any meaning assigned to those positions would be an
additional interpretation.
-/

/-!
## Alignment

Each input position corresponds directly to one output position:

    first  -> first
    second -> second
    third  -> third

We can make those relationships explicit.
-/

theorem map_first
    {α β : Type}
    (f : α → β)
    (t : Triad α) :
    (Triad.map f t).first = f t.first := by
  rfl

theorem map_second
    {α β : Type}
    (f : α → β)
    (t : Triad α) :
    (Triad.map f t).second = f t.second := by
  rfl

theorem map_third
    {α β : Type}
    (f : α → β)
    (t : Triad α) :
    (Triad.map f t).third = f t.third := by
  rfl

/-!
## Coherence

If we map the identity function across a triad,
nothing should change.

This checks that our transformation behaves coherently
with the structure we declared.
-/

theorem map_identity
    {α : Type}
    (t : Triad α) :
    Triad.map (fun x => x) t = t := by
  cases t
  rfl

/-!
## Composition

Suppose we apply transformation `f` and then transformation `g`.

That should produce the same triad as applying the composed
transformation directly.
-/

theorem map_composition
    {α β γ : Type}
    (f : α → β)
    (g : β → γ)
    (t : Triad α) :
    Triad.map g (Triad.map f t) =
      Triad.map (fun x => g (f x)) t := by
  cases t
  rfl

/-!
## A Concrete Example

Now give the abstract structure some simple values.
-/

def exampleTriad : Triad Nat :=
  {
    first  := 3
    second := 6
    third  := 9
  }

def increment (x : Nat) : Nat :=
  x + 1

def doubled (x : Nat) : Nat :=
  x * 2

/-!
Before asking Lean, predict:

    Triad.map increment exampleTriad

What should each position contain?
-/

example :
    Triad.map increment exampleTriad =
      {
        first  := 4
        second := 7
        third  := 10
      } := by
  rfl

/-!
Now apply two transformations.

First increment:

    3, 6, 9
       ↓
    4, 7, 10

Then double:

    4, 7, 10
       ↓
    8, 14, 20
-/

example :
    Triad.map doubled (Triad.map increment exampleTriad) =
      {
        first  := 8
        second := 14
        third  := 20
      } := by
  rfl

/-!
## Continuity Question

Something changed:

    3, 6, 9

became:

    4, 7, 10

and later:

    8, 14, 20

But something also remained stable:

* there are still three positions;
* first still corresponds to first;
* second still corresponds to second;
* third still corresponds to third.

The values changed.

The declared triadic structure persisted.
-/

/-!
## Student Challenge

Define your own transformation:

    def myTransform (x : Nat) : Nat := ...

Then compare:

    Triad.map myTransform exampleTriad

with the original `exampleTriad`.

Ask:

* What changed?
* What remained?
* Which correspondences were preserved?
* What assumptions did you introduce?


## Formalization Boundary

Lean has established properties of the `Triad` and `Triad.map`
definitions written in THIS file.

It has NOT established that:

* every real system is triadic;
* these positions correspond to particular physical quantities;
* the values 3, 6, and 9 possess special physical properties;
* or TFT's broader claims follow from this example.

This distinction is part of the exercise:

    Formal validity != empirical validation

The little model is useful precisely because we can see
what we declared, what followed from it, and where our claims stop.
-/
