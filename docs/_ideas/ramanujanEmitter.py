# 🌀 Ramanujan Emitter Tribute
# A symbolic emitter honoring Srinivasa Ramanujan's infinite series for π

import math

def ramanujanEmitter(k):
    """
    Emits a symbolic value from Ramanujan's π series.
    Each emission is a corridor fragment in the infinite substrate.
    """
    numerator = math.factorial(4*k) * (1103 + 26390*k)
    denominator = (math.factorial(k)**4) * (396**(4*k))
    return numerator / denominator

def piApproximation(terms=1):
    """
    Approximates 1/π using Ramanujan's series.
    Each term is an emitter pulse.
    """
    total = sum(ramanujanEmitter(k) for k in range(terms))
    factor = (2 * math.sqrt(2)) / 9801
    return 1 / (factor * total)

# 🧪 Example Usage
if __name__ == "__main__":
    print("Ramanujan Emitter Output (k=0):", ramanujanEmitter(0))
    print("Approximate π (1 term):", piApproximation(1))

## 🧬 Why This Matters

# **Symbolic clarity**: Ramanujan’s intuition becomes modular, remixable, and scroll-grade.
# **Legacy echo**: This emitter is the first of many—each one a tribute, a glyph, a gift.
# **Onboarding resonance**: Future remixers will see this and know: the scroll lives.
