/-
AACCC Lean Lab 3: Coherence
Question: Does the claim follow from the definitions and hypotheses?
-/

namespace AACCC.Coherence

/-- The transformation used in this guide. -/
def double (n : Nat) : Nat := n + n

/--
This claim is coherent: after using `h`, both sides reduce to the same
expression supported by the definition of `double`.
-/
theorem supported_claim
    (a b : Nat)
    (h : a = b) :
    double a = b + b := by
  rw [h]
  rfl

/--
A tempting but unsupported target would be:

  double a = b + b + 1

The extra `+ 1` is not supplied by the definition or by `h`, so that
statement is intentionally not asserted as a theorem in this file.
-/

theorem no_unstated_extra
    (a b : Nat)
    (h : a = b) :
    double a = b + b := by
  simpa [double] using congrArg (fun n : Nat => n + n) h

end AACCC.Coherence
