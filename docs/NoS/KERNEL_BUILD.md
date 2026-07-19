# Kernel Build Notes 🧠  
*(RTT‑Aware Instrumentation, Not a Kernel Rewrite)*

NawderOS does **not** replace the Linux kernel.  
It lightly instruments it.

This document describes **where** RTT‑aligned hooks live, **what they observe**, and **what they intentionally do not do**.

If you can build a custom Linux kernel, you can build NawderOS 🙂

---

## Design Philosophy

Before touching code, a few ground rules:

- We **observe**, we don’t control
- We **emit signals**, we don’t enforce policy
- We **prefer tracepoints over logic**
- We **keep patches small and readable**

RTT is about coherence over time — not about adding clever behavior to the kernel.

---

## Supported Kernel Baseline

NawderOS currently targets:

- **Linux 6.x** (LTS preferred)
- Vanilla kernel source
- No out‑of‑tree dependencies required

If you can build a stock kernel, you’re already 90% there.

---

## Where NawderOS Hooks In 🔧

NawderOS touches only a few strategic locations:

### 1️⃣ Boot Path (`init/`)

**Purpose:** Substrate alignment check

- Capture kernel version, config hash, and boot parameters
- Emit a `SUBSTRATE_BASELINE` badge
- No branching, no failure paths

🙂 *This answers: “What did we actually boot?”*

---

### 2️⃣ Scheduler Boundaries (`kernel/sched/`)

**Purpose:** Wrap checks on context transitions

- Observe task switches
- Capture minimal metadata (PID, state, timestamp)
- Emit `WRAP_CHECK` badges on anomalies only

🙂 *We don’t care who runs — we care when transitions drift.*

---

### 3️⃣ Memory Access Boundaries (`mm/`)

**Purpose:** Validation corridor observation

- Hook into existing fault or boundary logic
- Detect access outside declared corridors
- Emit `CORRIDOR_BREACH` badges

🙂 *This is not memory protection — it’s memory awareness.*

---

### 4️⃣ Module Lifecycle (`kernel/module/`)

**Purpose:** Substrate drift detection

- Observe module load/unload
- Compare against declared expectations
- Emit `SUBSTRATE_DRIFT` badges if mismatched

🙂 *“Did the system change under our feet?”*

---

## How Badges Are Emitted 🏷️

Badges are **events**, not logs.

Initial implementations may use:
- `trace_printk`
- tracepoints
- or a simple ring buffer

Later versions may expose:
- `/proc/nawderian`
- `tracefs` integration
- userspace collectors

### Badge Emission Rules
- Append‑only
- No blocking
- No side effects
- No policy decisions

If emitting a badge could crash the system, **don’t emit it** 😄

---

## What NawderOS Does *Not* Do ❌

To keep things sane:

- No syscall interception
- No scheduler modification
- No memory allocation changes
- No security enforcement
- No performance tuning

This is instrumentation, not intervention.

---

## Minimal Patch Strategy 🧩

A good NawderOS kernel patch should:
- Touch as few files as possible
- Be readable in one sitting
- Be removable without breaking the kernel
- Compile cleanly with RTT disabled

If your patch feels “clever,” it’s probably too much.

---

## Build Steps (High Level)

1. Clone vanilla Linux kernel
2. Apply NawderOS patch set
3. Enable RTT flags in `.config`
4. Build kernel as usual
5. Boot and observe badge output

Detailed commands live in `INSTALLATION.md`.

---

## Debugging and Safety 🛟

If something goes wrong:
- Disable RTT hooks via config
- Rebuild kernel
- Boot clean

NawderOS should never prevent a system from booting.

---

## Why This Matters

RTT becomes real when:
- assumptions are visible
- drift is observable
- coherence can be discussed without guesswork

This kernel layer doesn’t *solve* anything.  
It lets you **see** what’s happening.

And seeing is the first step 🙂
