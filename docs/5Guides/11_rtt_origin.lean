/-
AACCC / 5Guides Lean Origin Example
10_unified_resonance_theorem.lean

Purpose:
  Formalize one small, inspectable algebraic structure inspired by the
  Unified Resonance Theorem.

Source form:

    Resonance_glyph = Q_z * F_theta * S_dim

Important:
  This Lean example introduces its own small multiplicative structure.

  The common carrier type, multiplication operation, identity element,
  and algebraic laws are assumptions of THIS formal model.

  They are not established merely by the source notation.

Student questions:
  1. What three factors have actually been declared?
  2. What algebraic structure did this Lean model add?
  3. Which conclusions depend on associativity or identity?
  4. What has Lean proved?
  5. What has NOT been proved?
-/


/-!
## A Minimal Multiplicative Structure

Instead of depending on an external algebra library, we explicitly
declare exactly the structure needed by this teaching example.
-/

structure ResonanceAlgebra (α : Type) where
  mul : α → α → α
  one : α
  mul_assoc :
    ∀ a b c : α,
      mul (mul a b) c = mul a (mul b c)
  one_mul :
    ∀ a : α,
      mul one a = a
  mul_one :
    ∀ a : α,
      mul a one = a


/-!
## Three-Factor Composition

The source-inspired factors remain generic.

Their names preserve their roles in the source expression without
assigning additional physical or symbolic meaning inside Lean.
-/

def unifiedResonance
    {α : Type}
    (alg : ResonanceAlgebra α)
    (quadrant frequency dimension : α) : α :=
  alg.mul (alg.mul quadrant frequency) dimension


/-!
## Awareness

The model has three factor values:

* `quadrant`
* `frequency`
* `dimension`

and an explicitly supplied algebra:

* `alg`

That algebra tells Lean how the factors may be combined.
-/


/-!
## Alignment

The intended correspondence is:

    Q_z      -> quadrant
    F_theta  -> frequency
    S_dim    -> dimension

This correspondence is declared by the model.

Lean verifies consequences after these declarations are supplied.
-/


/-!
## Coherence — Associative Regrouping

Because `ResonanceAlgebra` explicitly requires associativity,
we may regroup the three-factor composition.
-/

theorem unifiedResonance_assoc
    {α : Type}
    (alg : ResonanceAlgebra α)
    (quadrant frequency dimension : α) :
    unifiedResonance alg quadrant frequency dimension =
      alg.mul quadrant (alg.mul frequency dimension) := by
  exact alg.mul_assoc quadrant frequency dimension


/-!
## Neutral Factors

The algebra also explicitly supplies an identity element.

Three neutral factors therefore compose to the neutral element.
-/

theorem unifiedResonance_neutral
    {α : Type}
    (alg : ResonanceAlgebra α) :
    unifiedResonance alg alg.one alg.one alg.one = alg.one := by
  unfold unifiedResonance
  rw [alg.one_mul]
  rw [alg.one_mul]


/-!
A neutral quadrant factor leaves the combination of the remaining
two factors unchanged.
-/

theorem neutral_quadrant
    {α : Type}
    (alg : ResonanceAlgebra α)
    (frequency dimension : α) :
    unifiedResonance alg alg.one frequency dimension =
      alg.mul frequency dimension := by
  unfold unifiedResonance
  rw [alg.one_mul]


/-!
A neutral dimension factor leaves the first two-factor composition
unchanged.
-/

theorem neutral_dimension
    {α : Type}
    (alg : ResonanceAlgebra α)
    (quadrant frequency : α) :
    unifiedResonance alg quadrant frequency alg.one =
      alg.mul quadrant frequency := by
  unfold unifiedResonance
  rw [alg.mul_one]


/-!
## Clarity

The assumptions are now impossible to miss.

To construct a `ResonanceAlgebra α`, we must provide:

* a multiplication operation;
* an identity element;
* associativity;
* left identity;
* right identity.

This makes an important distinction explicit:

    source notation

is not automatically the same thing as:

    formal algebraic specification
-/


/-!
## A Concrete Natural-Number Model

For a concrete example, define the required algebra over `Nat`.
-/

def natResonanceAlgebra : ResonanceAlgebra Nat where
  mul := Nat.mul
  one := 1
  mul_assoc := Nat.mul_assoc
  one_mul := Nat.one_mul
  mul_one := Nat.mul_one


example :
    unifiedResonance natResonanceAlgebra 2 3 4 = 24 := by
  rfl


example :
    unifiedResonance natResonanceAlgebra 1 3 4 = 12 := by
  rfl


/-!
## Continuity Question

Suppose one factor changes while the other two remain fixed:

    Q * F1 * S
        ↓
    Q * F2 * S

Ask:

* What changed?
* What remained fixed?
* Did the three-factor structure persist?
* Which proofs still work?
* Which conclusions depend on our algebraic assumptions?

The factor values may change while the declared composition structure
remains available for inspection.
-/


/-!
## Student Challenge

Before changing the model, identify:

1. which factors came from the source expression;
2. which operation was introduced by this Lean formalization;
3. which algebraic laws had to be supplied;
4. which theorem uses each law.

Then try defining another `ResonanceAlgebra`.

Ask:

    What must I prove before Lean will accept it?


## Formalization Boundary

Lean has established consequences of `unifiedResonance` under the
explicit `ResonanceAlgebra` assumptions written in THIS file.

Lean has NOT established that:

* the source factors naturally share one mathematical type;
* their source-level composition is this multiplication operation;
* associativity follows from the original notation;
* an identity factor exists in the original interpretation;
* the factors are empirically measurable;
* or the broader Unified Resonance interpretation is empirically valid.

The key distinction is:

    source notation != complete algebraic specification

In this version, instead of hiding the missing algebra behind an
import, we make the required structure visible.

That is exactly what the AACCC exercise is meant to expose.
-/