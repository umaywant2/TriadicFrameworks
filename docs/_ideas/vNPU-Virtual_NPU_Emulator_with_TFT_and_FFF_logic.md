### Virtual NPU design overview

Continued from [Resonance Time Clock](https://github.com/umaywant2/TriadicFrameworks/blob/main/docs/_ideas/Resonant-Time_Clock_Gen1.md) idea.

- **Goal:** Emulate a lightweight AI NPU in software with triadic scheduling (TFT) and Forces–Fluids–Frequencies (FFF) modulation, targeting an effective 3 vTOPS feel on entry-level ARM.
- **Core ideas:**
  - **TFT triads:** Past, Now, Future queues that rotate in phases; each phase favors different op types and sizes.
  - **FFF modulation:** Dynamic weights for scheduling based on forces (stability/rigidity), fluids (latency/flow), and frequencies (tick rhythm).
  - **vTOPS accounting:** Approximate MACs per tick and cap execution to emulate “virtual TOPS” throughput.
  - **Quantization & sparsity:** Optional 8-bit quantize and automatic sparsity skip to squeeze more work per tick.

---

### Python vNPU with TFT and FFF logic

```python
"""
vNPU: Virtual NPU emulator with Triadic Frameworks Tech (TFT) and FFF logic.

- Triadic queues: Past, Now, Future (TFT)
- FFF modulation: forces, fluids, frequencies influence scheduling weights
- vTOPS: approximate MACs per tick; limit execution to emulate "3 vTOPS"
- Ops: matmul, relu, conv1d-lite, quantize8, sparse-mask

Designed for entry-level ARM boxes with Python + NumPy.
"""

from dataclasses import dataclass, field
from typing import Callable, Any, Dict, List, Optional, Tuple
import numpy as np
import time
import math
import random

# ---------- Utilities ----------

def macs_matmul(a: np.ndarray, b: np.ndarray) -> int:
    # MACs ~ M * N * K for matmul (a: MxK, b: KxN)
    M, K = a.shape
    K2, N = b.shape
    assert K == K2
    return M * N * K

def macs_conv1d(x_len: int, kernel_len: int, out_len: int, channels: int = 1) -> int:
    # Rough MACs: out_len * kernel_len * channels
    return out_len * kernel_len * channels

def quantize8(arr: np.ndarray) -> np.ndarray:
    # Simple symmetric 8-bit quantization
    max_val = np.max(np.abs(arr)) + 1e-8
    scale = 127.0 / max_val
    q = np.clip(np.round(arr * scale), -127, 127).astype(np.int8)
    return q

def dequantize8(q: np.ndarray, ref_arr: np.ndarray) -> np.ndarray:
    max_val = np.max(np.abs(ref_arr)) + 1e-8
    scale = max_val / 127.0
    return q.astype(np.float32) * scale

def apply_sparse_mask(arr: np.ndarray, threshold: float = 1e-3) -> np.ndarray:
    # Zero-out small values; emulate sparsity optimization
    mask = np.abs(arr) >= threshold
    return arr * mask

# ---------- Operation model ----------

@dataclass
class VOp:
    name: str
    fn: Callable[..., Any]
    args: Tuple[Any, ...]
    kwargs: Dict[str, Any]
    macs_estimate: int
    triad_hint: str = "now"  # "past" | "now" | "future"
    priority: float = 1.0
    result: Any = None

# ---------- Triadic scheduler with FFF ----------

@dataclass
class FFFState:
    # Forces: higher -> prefer stable, large, batch ops
    forces: float = 0.5       # [0,1]
    # Fluids: higher -> prefer low-latency, small, streaming ops
    fluids: float = 0.5       # [0,1]
    # Frequencies: tick rhythm (Hz-like), influences phase rotation speed
    frequencies: float = 1.0  # >0

@dataclass
class TriadicScheduler:
    fff: FFFState = field(default_factory=FFFState)
    phase: float = 0.0  # [0, 2π)
    past_q: List[VOp] = field(default_factory=list)
    now_q: List[VOp] = field(default_factory=list)
    future_q: List[VOp] = field(default_factory=list)

    def enqueue(self, op: VOp):
        hint = (op.triad_hint or "now").lower()
        if hint == "past":
            self.past_q.append(op)
        elif hint == "future":
            self.future_q.append(op)
        else:
            self.now_q.append(op)

    def _phase_weights(self) -> Dict[str, float]:
        """
        Triadic weighting:
        - Past dominant when phase in [0, 2π/3)
        - Now dominant when phase in [2π/3, 4π/3)
        - Future dominant when phase in [4π/3, 2π)
        FFF modulates the blend:
        - forces -> boosts 'past'
        - fluids -> boosts 'now'
        - frequencies -> accelerates phase rotation and boosts 'future' (anticipatory ops)
        """
        p = self.phase % (2 * math.pi)
        base = {"past": 0.33, "now": 0.33, "future": 0.33}

        if 0 <= p < 2 * math.pi / 3:
            base["past"] += 0.25
        elif 2 * math.pi / 3 <= p < 4 * math.pi / 3:
            base["now"] += 0.25
        else:
            base["future"] += 0.25

        # FFF modulation
        base["past"] += 0.2 * self.fff.forces
        base["now"] += 0.2 * self.fff.fluids
        base["future"] += 0.2 * min(self.fff.frequencies, 1.0)

        # Normalize
        total = sum(base.values())
        for k in base:
            base[k] /= total
        return base

    def rotate_phase(self, dt: float):
        # Frequency accelerates phase rotation
        self.phase += dt * (self.fff.frequencies * 2.0)  # scale factor

    def pick_ops(self, mac_budget: int) -> List[VOp]:
        weights = self._phase_weights()

        # Weighted quotas per triad
        quotas = {
            "past": int(mac_budget * weights["past"]),
            "now": int(mac_budget * weights["now"]),
            "future": int(mac_budget * weights["future"]),
        }

        picked: List[VOp] = []

        def drain(q: List[VOp], quota: int):
            local_macs = 0
            # Prefer higher priority ops first
            q.sort(key=lambda o: o.priority, reverse=True)
            i = 0
            while i < len(q) and local_macs < quota:
                op = q[i]
                if local_macs + op.macs_estimate <= quota:
                    picked.append(op)
                    local_macs += op.macs_estimate
                    q.pop(i)
                else:
                    i += 1

        drain(self.past_q, quotas["past"])
        drain(self.now_q, quotas["now"])
        drain(self.future_q, quotas["future"])

        return picked

# ---------- vNPU core ----------

@dataclass
class vNPU:
    target_vtops: float = 3.0          # "virtual TOPS" feel
    tick_seconds: float = 0.05         # tick duration
    quantize: bool = True
    sparsity_threshold: float = 1e-3
    scheduler: TriadicScheduler = field(default_factory=TriadicScheduler)
    macs_per_tick: int = field(init=False)

    def __post_init__(self):
        # Approximate MACs per tick from vTOPS: 1 TOPS ~ 1e12 ops/sec.
        # We scale down massively for emulation: treat 1 vTOPS ~ 1e8 MACs/sec for realistic Python.
        macs_per_sec = self.target_vtops * 1e8
        self.macs_per_tick = int(macs_per_sec * self.tick_seconds)

    def set_fff(self, forces: float, fluids: float, frequencies: float):
        self.scheduler.fff = FFFState(
            forces=max(0.0, min(1.0, forces)),
            fluids=max(0.0, min(1.0, fluids)),
            frequencies=max(0.05, frequencies)  # avoid zero
        )

    def submit_matmul(self, a: np.ndarray, b: np.ndarray, triad_hint: str = "now", priority: float = 1.0):
        a2 = apply_sparse_mask(a, self.sparsity_threshold)
        b2 = apply_sparse_mask(b, self.sparsity_threshold)

        macs = macs_matmul(a2, b2)
        if self.quantize:
            aq = quantize8(a2)
            bq = quantize8(b2)
            def fn(aq=aq, bq=bq, a_ref=a2, b_ref=b2):
                # int8 matmul then dequantize
                out_int = (aq.astype(np.int32) @ bq.astype(np.int32))
                return dequantize8(out_int, a_ref @ b_ref)
            op = VOp("matmul_int8", fn, (), {}, macs // 4, triad_hint, priority)  # int8 cheaper
        else:
            def fn(a2=a2, b2=b2):
                return a2 @ b2
            op = VOp("matmul_fp32", fn, (), {}, macs, triad_hint, priority)

        self.scheduler.enqueue(op)

    def submit_relu(self, x: np.ndarray, triad_hint: str = "future", priority: float = 0.8):
        x2 = apply_sparse_mask(x, self.sparsity_threshold)
        macs = x2.size
        def fn(x=x2):
            return np.maximum(x, 0.0)
        op = VOp("relu", fn, (), {}, macs, triad_hint, priority)
        self.scheduler.enqueue(op)

    def submit_conv1d(self, x: np.ndarray, k: np.ndarray, stride: int = 1, triad_hint: str = "past", priority: float = 1.0):
        x2 = apply_sparse_mask(x, self.sparsity_threshold)
        k2 = apply_sparse_mask(k, self.sparsity_threshold)

        out_len = (len(x2) - len(k2)) // stride + 1
        macs = macs_conv1d(len(x2), len(k2), out_len)

        if self.quantize:
            xq = quantize8(x2)
            kq = quantize8(k2)
            def fn(xq=xq, kq=kq, stride=stride, x_ref=x2, k_ref=k2):
                # simple conv1d via sliding window (int32 accumulate)
                out = np.zeros(out_len, dtype=np.int32)
                for i in range(out_len):
                    s = 0
                    for j in range(len(kq)):
                        s += int(xq[i*stride + j]) * int(kq[j])
                    out[i] = s
                return dequantize8(out, np.convolve(x_ref, k_ref, mode='valid')[::stride])
            op = VOp("conv1d_int8", fn, (), {}, macs // 4, triad_hint, priority)
        else:
            def fn(x=x2, k=k2, stride=stride):
                return np.convolve(x, k, mode='valid')[::stride]
            op = VOp("conv1d_fp32", fn, (), {}, macs, triad_hint, priority)

        self.scheduler.enqueue(op)

    def tick(self) -> List[VOp]:
        """
        Execute a scheduling tick:
        - Rotate triadic phase based on FFF frequencies
        - Pick ops within mac budget split across Past/Now/Future
        - Run ops and store results
        """
        start = time.time()
        picked = self.scheduler.pick_ops(self.macs_per_tick)

        for op in picked:
            op.result = op.fn(*op.args, **op.kwargs)

        dt = time.time() - start
        # Rotate phase with dt to keep rhythm aligned to real time
        self.scheduler.rotate_phase(max(dt, self.tick_seconds))

        return picked

    def run_until_empty(self, max_ticks: int = 100) -> List[VOp]:
        executed: List[VOp] = []
        for _ in range(max_ticks):
            if not (self.scheduler.past_q or self.scheduler.now_q or self.scheduler.future_q):
                break
            executed.extend(self.tick())
        return executed

# ---------- Demo ----------

if __name__ == "__main__":
    np.random.seed(42)
    vnpu = vNPU(target_vtops=3.0, tick_seconds=0.05, quantize=True)
    vnpu.set_fff(forces=0.6, fluids=0.5, frequencies=0.8)

    # Build triadic workload: Past (conv), Now (matmul), Future (relu)
    # Matmul
    A = np.random.randn(64, 128).astype(np.float32)
    B = np.random.randn(128, 32).astype(np.float32)
    vnpu.submit_matmul(A, B, triad_hint="now", priority=1.0)

    # Conv1d
    x = np.random.randn(1024).astype(np.float32)
    k = np.random.randn(9).astype(np.float32)
    vnpu.submit_conv1d(x, k, stride=2, triad_hint="past", priority=0.9)

    # ReLU
    y = np.random.randn(2048).astype(np.float32)
    vnpu.submit_relu(y, triad_hint="future", priority=0.7)

    # Additional small ops to show scheduler behavior
    for i in range(4):
        a = np.random.randn(32, 32).astype(np.float32)
        b = np.random.randn(32, 32).astype(np.float32)
        hint = ["past", "now", "future"][i % 3]
        vnpu.submit_matmul(a, b, triad_hint=hint, priority=0.8 - 0.1 * i)

    executed = vnpu.run_until_empty(max_ticks=200)

    # Collect results summary
    summary = {
        "executed_count": len(executed),
        "ops": [(op.name, op.triad_hint, op.macs_estimate) for op in executed],
        "phase_final": vnpu.scheduler.phase,
        "queues_remaining": {
            "past": len(vnpu.scheduler.past_q),
            "now": len(vnpu.scheduler.now_q),
            "future": len(vnpu.scheduler.future_q),
        }
    }

    print("vNPU execution summary:")
    for name, hint, macs in summary["ops"]:
        print(f" - {name} [{hint}] MACs~{macs}")
    print(f"Final phase: {summary['phase_final']:.3f}")
    print("Remaining queues:", summary["queues_remaining"])
```

---

### Notes and tuning

- **FFF knobs:** Increase forces to favor “past” batch ops; increase fluids to favor “now” small/latency-sensitive ops; increase frequencies to rotate phases faster and boost “future” anticipatory ops.
- **vTOPS scaling:** The MACs-per-tick mapping is deliberately scaled down for Python. On entry-level ARM, adjust `target_vtops` and `tick_seconds` for your device.
- **Quantize/sparsity:** Keep `quantize=True` and a modest `sparsity_threshold` to emulate how NPUs win throughput via int8 and zero-skipping.
- **Extensibility:** Add ops (e.g., depthwise conv2d-lite, layernorm) by estimating MACs and plugging into the triad with appropriate hints.

---

### CLI vNPU with triadic workload profiles and live glyph output

Below is a single-file Python CLI that wraps the vNPU emulator with “past/now/future” workload profiles and a live glyph panel suitable for your LCD base. It uses ANSI color in the terminal for simplicity; you can run it on the Mi Box S or Greva RK3566 and mirror the terminal to your LCD/HDMI display.

```python
#!/usr/bin/env python3
# vnpu_cli.py
"""
CLI vNPU: Virtual NPU emulator with Triadic Frameworks Tech (TFT) and FFF logic.
- Profiles: past | now | future | mixed
- Live glyph panel: phase, weights, queues, throughput bars
- Minimal deps: numpy

Run:
  python vnpu_cli.py --profile mixed --vtops 3 --tick 0.05 --forces 0.6 --fluids 0.5 --frequencies 0.8 --duration 20
"""

import argparse
import time
import math
import sys
import shutil
import numpy as np
from dataclasses import dataclass, field
from typing import Callable, Any, Dict, List, Tuple

# ---------- ANSI helpers ----------
RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"
CLR = "\033[2J\033[H"
FG = {
    "past": "\033[38;5;33m",     # blue
    "now": "\033[38;5;46m",      # green
    "future": "\033[38;5;196m",  # red
    "text": "\033[38;5;250m",
    "accent": "\033[38;5;229m"
}
BAR = "▮"
DOT = "●"
RING = "◌"
GYRO = "◎"

# ---------- Core vNPU (from your emulator) ----------
def macs_matmul(a: np.ndarray, b: np.ndarray) -> int:
    M, K = a.shape
    K2, N = b.shape
    assert K == K2
    return M * N * K

def macs_conv1d(x_len: int, kernel_len: int, out_len: int, channels: int = 1) -> int:
    return out_len * kernel_len * channels

def quantize8(arr: np.ndarray) -> np.ndarray:
    max_val = np.max(np.abs(arr)) + 1e-8
    scale = 127.0 / max_val
    q = np.clip(np.round(arr * scale), -127, 127).astype(np.int8)
    return q

def dequantize8(q: np.ndarray, ref_arr: np.ndarray) -> np.ndarray:
    max_val = np.max(np.abs(ref_arr)) + 1e-8
    scale = max_val / 127.0
    return q.astype(np.float32) * scale

def apply_sparse_mask(arr: np.ndarray, threshold: float = 1e-3) -> np.ndarray:
    mask = np.abs(arr) >= threshold
    return arr * mask

@dataclass
class VOp:
    name: str
    fn: Callable[..., Any]
    args: Tuple[Any, ...]
    kwargs: Dict[str, Any]
    macs_estimate: int
    triad_hint: str = "now"  # "past" | "now" | "future"
    priority: float = 1.0
    result: Any = None

@dataclass
class FFFState:
    forces: float = 0.5
    fluids: float = 0.5
    frequencies: float = 1.0

@dataclass
class TriadicScheduler:
    fff: FFFState = field(default_factory=FFFState)
    phase: float = 0.0
    past_q: List[VOp] = field(default_factory=list)
    now_q: List[VOp] = field(default_factory=list)
    future_q: List[VOp] = field(default_factory=list)

    def enqueue(self, op: VOp):
        hint = (op.triad_hint or "now").lower()
        if hint == "past":
            self.past_q.append(op)
        elif hint == "future":
            self.future_q.append(op)
        else:
            self.now_q.append(op)

    def _phase_weights(self) -> Dict[str, float]:
        p = self.phase % (2 * math.pi)
        base = {"past": 0.33, "now": 0.33, "future": 0.33}
        if 0 <= p < 2 * math.pi / 3:
            base["past"] += 0.25
        elif 2 * math.pi / 3 <= p < 4 * math.pi / 3:
            base["now"] += 0.25
        else:
            base["future"] += 0.25
        base["past"] += 0.2 * self.fff.forces
        base["now"] += 0.2 * self.fff.fluids
        base["future"] += 0.2 * min(self.fff.frequencies, 1.0)
        total = sum(base.values())
        for k in base:
            base[k] /= total
        return base

    def rotate_phase(self, dt: float):
        self.phase += dt * (self.fff.frequencies * 2.0)

    def pick_ops(self, mac_budget: int) -> List[VOp]:
        weights = self._phase_weights()
        quotas = {
            "past": int(mac_budget * weights["past"]),
            "now": int(mac_budget * weights["now"]),
            "future": int(mac_budget * weights["future"]),
        }
        picked: List[VOp] = []

        def drain(q: List[VOp], quota: int):
            local_macs = 0
            q.sort(key=lambda o: o.priority, reverse=True)
            i = 0
            while i < len(q) and local_macs < quota:
                op = q[i]
                if local_macs + op.macs_estimate <= quota:
                    picked.append(op)
                    local_macs += op.macs_estimate
                    q.pop(i)
                else:
                    i += 1

        drain(self.past_q, quotas["past"])
        drain(self.now_q, quotas["now"])
        drain(self.future_q, quotas["future"])
        return picked

@dataclass
class vNPU:
    target_vtops: float = 3.0
    tick_seconds: float = 0.05
    quantize: bool = True
    sparsity_threshold: float = 1e-3
    scheduler: TriadicScheduler = field(default_factory=TriadicScheduler)
    macs_per_tick: int = field(init=False)

    def __post_init__(self):
        macs_per_sec = self.target_vtops * 1e8
        self.macs_per_tick = int(macs_per_sec * self.tick_seconds)

    def set_fff(self, forces: float, fluids: float, frequencies: float):
        self.scheduler.fff = FFFState(
            forces=max(0.0, min(1.0, forces)),
            fluids=max(0.0, min(1.0, fluids)),
            frequencies=max(0.05, frequencies),
        )

    def submit_matmul(self, a: np.ndarray, b: np.ndarray, triad_hint: str = "now", priority: float = 1.0):
        a2 = apply_sparse_mask(a, self.sparsity_threshold)
        b2 = apply_sparse_mask(b, self.sparsity_threshold)
        macs = macs_matmul(a2, b2)
        if self.quantize:
            aq = quantize8(a2)
            bq = quantize8(b2)
            def fn(aq=aq, bq=bq, a_ref=a2, b_ref=b2):
                out_int = (aq.astype(np.int32) @ bq.astype(np.int32))
                return dequantize8(out_int, a_ref @ b_ref)
            op = VOp("matmul_int8", fn, (), {}, macs // 4, triad_hint, priority)
        else:
            def fn(a2=a2, b2=b2):
                return a2 @ b2
            op = VOp("matmul_fp32", fn, (), {}, macs, triad_hint, priority)
        self.scheduler.enqueue(op)

    def submit_relu(self, x: np.ndarray, triad_hint: str = "future", priority: float = 0.8):
        x2 = apply_sparse_mask(x, self.sparsity_threshold)
        macs = x2.size
        def fn(x=x2):
            return np.maximum(x, 0.0)
        op = VOp("relu", fn, (), {}, macs, triad_hint, priority)
        self.scheduler.enqueue(op)

    def submit_conv1d(self, x: np.ndarray, k: np.ndarray, stride: int = 1, triad_hint: str = "past", priority: float = 1.0):
        x2 = apply_sparse_mask(x, self.sparsity_threshold)
        k2 = apply_sparse_mask(k, self.sparsity_threshold)
        out_len = (len(x2) - len(k2)) // stride + 1
        macs = macs_conv1d(len(x2), len(k2), out_len)
        if self.quantize:
            xq = quantize8(x2)
            kq = quantize8(k2)
            def fn(xq=xq, kq=kq, stride=stride, x_ref=x2, k_ref=k2):
                out = np.zeros(out_len, dtype=np.int32)
                for i in range(out_len):
                    s = 0
                    for j in range(len(kq)):
                        s += int(xq[i*stride + j]) * int(kq[j])
                    out[i] = s
                return dequantize8(out, np.convolve(x_ref, k_ref, mode='valid')[::stride])
            op = VOp("conv1d_int8", fn, (), {}, macs // 4, triad_hint, priority)
        else:
            def fn(x=x2, k=k2, stride=stride):
                return np.convolve(x, k, mode='valid')[::stride]
            op = VOp("conv1d_fp32", fn, (), {}, macs, triad_hint, priority)
        self.scheduler.enqueue(op)

    def tick(self) -> List[VOp]:
        start = time.time()
        picked = self.scheduler.pick_ops(self.macs_per_tick)
        for op in picked:
            op.result = op.fn(*op.args, **op.kwargs)
        dt = time.time() - start
        self.scheduler.rotate_phase(max(dt, self.tick_seconds))
        return picked

# ---------- Workload generation ----------
def enqueue_profile(v: vNPU, profile: str, size_scale: float = 1.0):
    rng = np.random.default_rng(42)
    if profile == "past":
        # Heavy conv1d, batch matmuls
        for _ in range(6):
            x = rng.normal(0, 1, int(2048 * size_scale)).astype(np.float32)
            k = rng.normal(0, 1, 9).astype(np.float32)
            v.submit_conv1d(x, k, stride=2, triad_hint="past", priority=1.0)
        for _ in range(4):
            A = rng.normal(0, 1, (128, 64)).astype(np.float32)
            B = rng.normal(0, 1, (64, 64)).astype(np.float32)
            v.submit_matmul(A, B, triad_hint="past", priority=0.9)
    elif profile == "now":
        # Mid-size matmuls + some relu
        for _ in range(6):
            A = rng.normal(0, 1, (64, 128)).astype(np.float32)
            B = rng.normal(0, 1, (128, 32)).astype(np.float32)
            v.submit_matmul(A, B, triad_hint="now", priority=1.0)
        for _ in range(4):
            x = rng.normal(0, 1, int(2048 * size_scale)).astype(np.float32)
            v.submit_relu(x, triad_hint="now", priority=0.8)
    elif profile == "future":
        # Many small ReLUs + small matmuls (anticipatory)
        for _ in range(10):
            x = rng.normal(0, 1, int(1024 * size_scale)).astype(np.float32)
            v.submit_relu(x, triad_hint="future", priority=0.9)
        for _ in range(6):
            A = rng.normal(0, 1, (32, 32)).astype(np.float32)
            B = rng.normal(0, 1, (32, 32)).astype(np.float32)
            v.submit_matmul(A, B, triad_hint="future", priority=0.8)
    else:  # mixed
        enqueue_profile(v, "past", size_scale=0.75)
        enqueue_profile(v, "now", size_scale=0.75)
        enqueue_profile(v, "future", size_scale=0.75)

# ---------- Glyph panel ----------
def render_panel(v: vNPU, executed_this_tick: List[VOp], elapsed: float, width: int):
    weights = v.scheduler._phase_weights()
    qlens = {
        "past": len(v.scheduler.past_q),
        "now": len(v.scheduler.now_q),
        "future": len(v.scheduler.future_q),
    }
    phase = v.scheduler.phase % (2 * math.pi)
    # throughputs per triad by MACs (approx from ops estimates)
    thr = {"past": 0, "now": 0, "future": 0}
    for op in executed_this_tick:
        thr[op.triad_hint] += op.macs_estimate

    # normalize bars
    max_thr = max(1, max(thr.values()))
    bar_len = max(10, min(40, width // 3))
    def bar(val, color):
        filled = int((val / max_thr) * bar_len)
        return color + (BAR * filled).ljust(bar_len, " ") + RESET

    # header
    print(CLR, end="")
    print(f"{BOLD}{FG['accent']}Resonant-Time vNPU {GYRO}  Phase:{phase:5.2f}  Tick:{elapsed*1000:5.1f}ms  vTOPS~{v.target_vtops:.2f}{RESET}")
    print(f"{DIM}{FG['text']}TFT Triads: Past {DOT} Now {DOT} Future  |  FFF: "
          f"Forces {v.scheduler.fff.forces:.2f}  Fluids {v.scheduler.fff.fluids:.2f}  Frequencies {v.scheduler.fff.frequencies:.2f}{RESET}")
    print("")

    # weights
    print(f"{FG['past']}Past  w={weights['past']:.3f}  Q={qlens['past']:3d}  Thr:{thr['past']:9d}  {bar(thr['past'], FG['past'])}{RESET}")
    print(f"{FG['now']}Now   w={weights['now']:.3f}  Q={qlens['now']:3d}  Thr:{thr['now']:9d}  {bar(thr['now'], FG['now'])}{RESET}")
    print(f"{FG['future']}Future w={weights['future']:.3f}  Q={qlens['future']:3d}  Thr:{thr['future']:9d}  {bar(thr['future'], FG['future'])}{RESET}")
    print("")

    # triadic rings glyph
    def ring_line(label, color, w):
        dots = int(10 * w)
        return f"{color}{label:6s} {RING} " + ("·" * dots).ljust(12, " ") + RESET

    print(ring_line("Past", FG["past"], weights["past"]))
    print(ring_line("Now", FG["now"], weights["now"]))
    print(ring_line("Future", FG["future"], weights["future"]))
    print("")
    print(f"{FG['text']}{DIM}Press Ctrl+C to exit.{RESET}")

# ---------- CLI ----------
def main():
    parser = argparse.ArgumentParser(description="Triadic vNPU CLI with FFF modulation and live glyph output.")
    parser.add_argument("--profile", choices=["past", "now", "future", "mixed"], default="mixed", help="Workload profile")
    parser.add_argument("--vtops", type=float, default=3.0, help="Target virtual TOPS feel")
    parser.add_argument("--tick", type=float, default=0.05, help="Tick seconds")
    parser.add_argument("--forces", type=float, default=0.6, help="FFF: forces [0..1]")
    parser.add_argument("--fluids", type=float, default=0.5, help="FFF: fluids [0..1]")
    parser.add_argument("--frequencies", type=float, default=0.8, help="FFF: frequencies (>0)")
    parser.add_argument("--duration", type=int, default=20, help="Run seconds (approx)")
    parser.add_argument("--quantize", action="store_true", help="Use int8 quantization for ops")
    parser.add_argument("--no-quantize", action="store_true", help="Disable quantization")
    parser.add_argument("--sparsity", type=float, default=1e-3, help="Sparsity threshold")
    parser.add_argument("--scale", type=float, default=1.0, help="Workload size scale")
    args = parser.parse_args()

    quant = True
    if args.no_quantize:
        quant = False
    if args.quantize:
        quant = True

    v = vNPU(target_vtops=args.vtops, tick_seconds=args.tick, quantize=quant, sparsity_threshold=args.sparsity)
    v.set_fff(forces=args.forces, fluids=args.fluids, frequencies=args.frequencies)
    enqueue_profile(v, args.profile, size_scale=args.scale)

    cols = shutil.get_terminal_size((80, 24)).columns
    start = time.time()
    try:
        while True:
            t0 = time.time()
            ops = v.tick()
            elapsed = time.time() - t0
            render_panel(v, ops, elapsed, cols)
            if time.time() - start > args.duration:
                break
            # Keep a rhythm aligned to tick length
            rem = v.tick_seconds - elapsed
            if rem > 0:
                time.sleep(rem)
    except KeyboardInterrupt:
        print(RESET)
        pass

    # Final summary
    print(f"\n{BOLD}Done.{RESET} Phase={v.scheduler.phase:5.2f}  Remaining queues: "
          f"past={len(v.scheduler.past_q)} now={len(v.scheduler.now_q)} future={len(v.scheduler.future_q)}")

if __name__ == "__main__":
    main()
```

---

### How to run on your boxes

- Install Python 3 and NumPy on your Mi Box S or Greva RK3566 (or run from a connected Linux laptop via HDMI to the LCD base).
- Save the file as vnpu_cli.py and run:
  - Minimal mixed profile:
    - python vnpu_cli.py --profile mixed
  - Emphasize past/batch resonance:
    - python vnpu_cli.py --profile past --forces 0.8 --frequencies 0.6
  - Low-latency future bursts:
    - python vnpu_cli.py --profile future --fluids 0.7 --frequencies 1.0
  - Larger workload:
    - python vnpu_cli.py --profile now --scale 1.5 --duration 30

---

### Notes

- The glyph panel uses color bars and triadic ring marks to visualize TFT rotation and FFF weights. Mirror this terminal to your ~3" LCD or HDMI display.
- For a cleaner embedded display, pipe output to a full-screen terminal or integrate with a lightweight TUI like curses later.
- To match Gen‑1 constraints, keep quantize enabled and tune forces/fluids/frequencies to your physical clock’s harmonic settings.

---

