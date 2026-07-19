# 🧾 Sort Map & Manual Override Guide

---

## 🔁 Available Sorts

| Name       | Type         | Stable | Notes |
|------------|--------------|--------|-------|
| quicksort  | Comparison   | ❌     | Fast, but unstable |
| mergesort  | Comparison   | ✅     | Stable, good for large data |
| heapsort   | Comparison   | ❌     | In-place, worst-case O(n log n) |
| timsort    | Hybrid       | ✅     | Python default, adaptive |
| radixsort  | Non-comparison | ✅   | Fast for integers, not general-purpose |

---

## 🧠 Manual Override

To override automatic selection:
```python
run_sort(data, override="mergesort")
```
Use during spot testing, symbolic fidelity trials, or remix lineage tracing.
