/-
AACCC / 5Guides Lean Origin Example
08_nawderian_set_theorem.lean

Purpose:
  Formalize one small, inspectable algebraic structure inspired by
  the Nawderian SET Theorem.

  The teaching model keeps three named SET contributions:
    * spin
    * electrolysis / field-charge
    * temperature

  and combines them with a separately supplied gravitational
  contribution.

Important:
  This file proves consequences inside the declared Lean model.
  It does not establish that the SET decomposition is a complete
  or empirically validated physical description.

Student questions:
  1. What contributions have actually been declared?
  2. Which term corresponds to which contribution?
  3. Does the total contain exactly the terms we intended?
  4. What remains if one or more contributions are zero?
  5. What has Lean proved, and what has it NOT proved?
-/


/-!
## A Small SET Structure

We use integers so the example can represent signed contributions
without introducing additional libraries or physical assumptions.
-/

structure SETContribution where
  spin : Int
  electrolysis : Int
  temperature : Int
  deriving Repr, DecidableEq


/-!
## Compose the SET Contributions

The SET subtotal keeps the three named contributions explicit.
-/

def SETContribution.subtotal (s : SETContribution) : Int :=
  s.spin + s.electrolysis + s.temperature


/-!
## Add a Supplied Gravitational Contribution

Gravity is kept separate from the SET structure in this teaching
model. The total is defined as:

    gravity + spin + electrolysis + temperature
-/

def totalContribution (gravity : Int) (s : SETContribution) : Int :=
  gravity + s.spin + s.electrolysis + s.temperature


/-!
## Awareness

Before proving anything, inspect what has been declared.

The model contains four numeric contributions:

    gravity
    spin
    electrolysis
    temperature

Nothing in the type itself says that these values describe nature.
That interpretation belongs outside this small algebraic model.
-/


/-!
## Alignment

Each named field corresponds to one visible term in the expanded
expression.
-/

theorem total_expands
    (gravity : Int)
    (s : SETContribution) :
    totalContribution gravity s =
      gravity + s.spin + s.electrolysis + s.temperature := by
  rfl


/-!
## Coherence

The implementation should agree with the separately defined SET
subtotal followed by addition of gravity.
-/

theorem total_matches_subtotal
    (gravity : Int)
    (s : SETContribution) :
    totalContribution gravity s = gravity + s.subtotal := by
  simp [totalContribution, SETContribution.subtotal, Int.add_assoc]


/-!
## A Zero Temperature Contribution

If temperature contributes zero, the remaining terms stay visible.
-/

theorem zero_temperature
    (gravity spin electrolysis : Int) :
    totalContribution gravity
      {
        spin := spin
        electrolysis := electrolysis
        temperature := 0
      } =
      gravity + spin + electrolysis := by
  simp [totalContribution, Int.add_assoc]


/-!
## All SET Contributions Neutral

If all three SET contributions are zero, the modeled total reduces
to the supplied gravitational contribution.
-/

theorem zero_set_reduces_to_gravity
    (gravity : Int) :
    totalContribution gravity
      {
        spin := 0
        electrolysis := 0
        temperature := 0
      } = gravity := by
  simp [totalContribution]


/-!
## Concrete Example

Predict the result before asking Lean to reduce it.
-/

def exampleSET : SETContribution :=
  {
    spin := 2
    electrolysis := -1
    temperature := 4
  }


example :
    totalContribution 10 exampleSET = 15 := by
  rfl


/-!
## Continuity Question

Now change only the temperature contribution.

The value of the total changes, but several pieces of structure
remain stable:

* the same four contribution positions exist;
* spin still corresponds to spin;
* electrolysis still corresponds to electrolysis;
* gravity remains separately supplied;
* only the declared temperature value has changed.
-/

def warmerExampleSET : SETContribution :=
  {
    spin := 2
    electrolysis := -1
    temperature := 7
  }


example :
    totalContribution 10 warmerExampleSET = 18 := by
  rfl


/-!
## Student Challenge

Create your own `SETContribution` values and ask:

* Which contribution did you change?
* How did the total change?
* Which structural positions remained the same?
* Does the algebra tell you WHY the physical system changed?

That final question matters.

Lean can verify the arithmetic consequences of the model we supplied.
It does not automatically supply a physical explanation for the
numbers or validate the source framework empirically.


## Formalization Boundary

Lean has established properties of the definitions written in THIS
file.

It has NOT established that:

* Spin, Electrolysis / field-charge behavior, and Temperature form
  a complete physical decomposition;
* the four contributions are independent;
* simple addition is sufficient for every intended application;
* the numeric values correspond to experimentally measured forces;
* or the broader Nawderian SET interpretation is empirically valid.

This file therefore demonstrates a narrower claim:

    Given this declared additive model,
    these algebraic consequences follow.

That boundary is part of the AACCC exercise.
-/
