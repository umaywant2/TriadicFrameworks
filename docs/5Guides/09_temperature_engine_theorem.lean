/-
AACCC / 5Guides Lean Origin Example
09_temperature_engine_theorem.lean

Purpose:
  Formalize one small, inspectable algebraic model inspired by the
  Nawderian Temperature Engine Theorem.

Important:
  The source relation is represented in simplified form as:

      F_T = -α∇T

  This teaching example reduces the fuller spatial/vector idea to a
  one-dimensional signed integer model.

  Lean therefore verifies consequences of THIS simplified definition.
  It does not establish the empirical validity of the broader
  Temperature Engine interpretation.

Student questions:
  1. What quantities have actually been declared?
  2. How does the sign of the gradient affect the modeled force?
  3. What happens when either the gradient or coupling is zero?
  4. What has Lean proved?
  5. What has NOT been proved?
-/


/-!
## A Small Temperature-Force Model

We use integers so that positive and negative gradients can be
represented directly.

The modeled relation is:

    force = -(coupling * gradient)
-/

def temperatureForce (coupling gradient : Int) : Int :=
  -(coupling * gradient)


/-!
## Awareness

The model contains two inputs:

* `coupling`
* `gradient`

and produces one modeled output:

* `temperatureForce coupling gradient`

Nothing in this definition independently determines whether the
inputs correspond to measurable physical quantities.

That interpretation comes from outside this small algebraic model.
-/


/-!
## Zero Gradient

If there is no modeled gradient, the resulting modeled force is zero.
-/

theorem zero_gradient (coupling : Int) :
    temperatureForce coupling 0 = 0 := by
  simp [temperatureForce]


/-!
## Zero Coupling

Likewise, if the coupling factor is zero, the modeled force is zero.
-/

theorem zero_coupling (gradient : Int) :
    temperatureForce 0 gradient = 0 := by
  simp [temperatureForce]


/-!
## Gradient Reversal

Now reverse the sign of the gradient.

Within this algebraic model, reversing the gradient reverses the
sign of the resulting modeled force.
-/

theorem reverse_gradient (coupling gradient : Int) :
    temperatureForce coupling (-gradient) =
      -(temperatureForce coupling gradient) := by
  simp only [temperatureForce]
  rw [Int.mul_neg]
  rw [Int.neg_neg]
  rw [Int.neg_neg]


/-!
## Concrete Examples

Use a coupling value of 2.

With gradient 5:

    -(2 * 5) = -10

With gradient -5:

    -(2 * -5) = 10
-/

example :
    temperatureForce 2 5 = -10 := by
  native_decide


example :
    temperatureForce 2 (-5) = 10 := by
  native_decide


/-!
## Alignment

The important relationship in this simplified model is directional:

    positive gradient  -> negative modeled force
    negative gradient  -> positive modeled force

when the coupling is positive.

The theorem above does not need that interpretation in order to prove
the algebraic sign reversal.

That distinction is important:

    algebraic consequence != physical interpretation
-/


/-!
## Coherence

The zero cases and sign-reversal property all follow from the same
declared definition:

    temperatureForce coupling gradient =
      -(coupling * gradient)

They are therefore internally coherent consequences of the model.
-/


/-!
## Clarity

The definition deliberately keeps the relationship visible:

    input coupling
    input gradient
          ↓
    multiply
          ↓
    reverse sign
          ↓
    modeled force

A more complicated formalization might eventually use vectors,
spatial fields, gradients, units, and additional assumptions.

Those structures have not been silently inserted here.
-/


/-!
## Continuity Challenge

Try evaluating a sequence of gradients:

    5
    2
    1
    0
    -1
    -2
    -5

Ask:

* What changes?
* What happens at zero?
* What relationship persists as the gradient changes sign?
* Which conclusions depend on the coupling remaining unchanged?

The sequence gives us a simple way to think about change while
preserving the definition that relates one state to the next.


## Student Challenge

Choose your own coupling and gradient values.

Before asking Lean, predict:

    temperatureForce coupling gradient

Then reverse the gradient and predict again.

Finally ask:

    What did I calculate?

and separately:

    What physical meaning, if any, am I assuming?


## Formalization Boundary

Lean has established properties of the `temperatureForce` definition
written in THIS file.

It has NOT established that:

* this one-dimensional model captures the full source proposal;
* the source relation is empirically validated;
* temperature gradients alone determine physical motion;
* `coupling` corresponds to a particular measured physical constant;
* or this model replaces established thermodynamic or mechanical
  descriptions.

The mathematical result is intentionally narrower:

    Given this definition,
    these algebraic consequences follow.

That is exactly the boundary we want students to be able to see.
-/
