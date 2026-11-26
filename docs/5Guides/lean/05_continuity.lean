/-
AACCC Lean Lab 5: Continuity
Question: What remains valid when the transformation changes?
-/

namespace AACCC.Continuity

/-- The original transformation. -/
def double (n : Nat) : Nat := n + n

/-- A changed transformation. -/
def triple (n : Nat) : Nat := n + n + n

/-- Equality is preserved through the original transformation. -/
theorem double_respects_equality
    (a b : Nat)
    (h : a = b) :
    double a = double b := by
  rw [h]

/-- The same proof structure survives the change from `double` to `triple`. -/
theorem triple_respects_equality
    (a b : Nat)
    (h : a = b) :
    triple a = triple b := by
  rw [h]

/--
A general continuity result: every function preserves equality of inputs.
The specific double and triple theorems are instances of this structure.
-/
theorem transformation_respects_equality
    (transform : Nat → Nat)
    (a b : Nat)
    (h : a = b) :
    transform a = transform b := by
  rw [h]

end AACCC.Continuity
