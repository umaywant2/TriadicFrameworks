/-
AACCC Lean Lab 2: Alignment
Question: What corresponds?
-/

namespace AACCC.Alignment

/-- The transformation used in this guide. -/
def double (n : Nat) : Nat := n + n

/--
The hypothesis `h : a = b` supplies the justified correspondence.
Rewriting with `h` aligns the two transformed expressions.
-/
theorem double_respects_equality
    (a b : Nat)
    (h : a = b) :
    double a = double b := by
  rw [h]

/-- The same alignment shown directly on addition. -/
example (a b : Nat) (h : a = b) : a + a = b + b := by
  rw [h]

end AACCC.Alignment
