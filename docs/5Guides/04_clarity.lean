/-
AACCC Lean Lab 4: Clarity
Question: Can another reader inspect the proof without guessing?
-/

namespace AACCC.Clarity

/-- A clearly named transformation. -/
def double (n : Nat) : Nat := n + n

/--
A step-by-step proof. The intermediate expressions make the reasoning
visible while preserving exactly the original claim.
-/
theorem double_respects_equality_clear
    (left right : Nat)
    (same_input : left = right) :
    double left = double right := by
  calc
    double left = left + left := rfl
    _ = right + right := by rw [same_input]
    _ = double right := rfl

/-- A shorter proof of the same statement for comparison. -/
theorem double_respects_equality_compact
    (left right : Nat)
    (same_input : left = right) :
    double left = double right := by
  rw [same_input]

end AACCC.Clarity
