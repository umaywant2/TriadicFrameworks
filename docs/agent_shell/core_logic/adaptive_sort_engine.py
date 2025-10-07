"""
⚙️ Adaptive Sort Engine
Benchmarks multiple sort algorithms and selects best performer.
Allows manual override and sort mapping.
"""

import time
import random
from sorts import quicksort, mergesort, heapsort, timsort, radixsort

SORT_ALGORITHMS = {
    "quicksort": quicksort,
    "mergesort": mergesort,
    "heapsort": heapsort,
    "timsort": timsort,
    "radixsort": radixsort
}

def benchmark_sort(algorithm, data):
    start = time.time()
    sorted_data = algorithm(data.copy())
    duration = time.time() - start
    return duration, sorted_data

def select_best_sort(data):
    results = {}
    for name, func in SORT_ALGORITHMS.items():
        duration, _ = benchmark_sort(func, data)
        results[name] = duration
        print(f"[Benchmark] {name}: {duration:.4f}s")
    best = min(results, key=results.get)
    print(f"[Selector] Best sort: {best}")
    return SORT_ALGORITHMS[best]

def run_sort(data, override=None):
    if override and override in SORT_ALGORITHMS:
        print(f"[Manual Override] Using: {override}")
        return SORT_ALGORITHMS[override](data)
    best_sort = select_best_sort(data)
    return best_sort(data)
