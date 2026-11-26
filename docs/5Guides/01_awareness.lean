/-
AACCC Lean Lab 1: Awareness
Question: What is actually given, and what must be proved?
-/

namespace AACCC.Awareness

/-- `double n` records the transformation we will inspect across the lab. -/
def double (n : Nat) : Nat := n + n

/--
Awareness exercise:
- Input: `n : Nat`
- Goal: `double n = n + n`
- No extra hypothesis is available or needed.
-/
theorem double_observed (n : Nat) : double n = n + n := by
  rfl

/-- A concrete check that exposes the computed value. -/
example : double 4 = 8 := by
  decide

end AACCC.Awareness
