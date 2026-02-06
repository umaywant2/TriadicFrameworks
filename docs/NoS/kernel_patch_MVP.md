# NawderOS Minimal Kernel Patch (MVP) 🧠  
*(RTT‑Aware Instrumentation Baseline)*

This patch does **one thing well**:

> It proves that RTT‑aligned observation can live inside the kernel without changing kernel behavior.

No enforcement.  
No policy.  
No cleverness.

Just **signals**.

---

## MVP Goals

This patch must:

- Compile cleanly on Linux 6.x
- Emit at least one RTT badge at boot
- Touch as few kernel files as possible
- Be removable without side effects
- Be understandable in one sitting 🙂

---

## What This MVP Implements

### ✔️ One RTT concept
**Substrate baseline observation**

### ✔️ One module
`substrateAudit`

### ✔️ One badge
`SUBSTRATE_BASELINE`

That’s it.

Everything else comes later.

---

## Patch Overview

### Files Touched
- `init/main.c` — boot‑time hook
- `include/linux/nawderos.h` — RTT definitions
- `kernel/nawderos.c` — badge emission logic
- `kernel/Makefile` — build integration

---

## 1️⃣ Header: RTT Definitions

**`include/linux/nawderos.h`**

```c
#ifndef _LINUX_NAWDEROS_H
#define _LINUX_NAWDEROS_H

#define NAWDEROS_VERSION "0.1.0"
#define RTT_BADGE_SUBSTRATE_BASELINE "SUBSTRATE_BASELINE"

void nawderos_emit_badge(const char *badge_type,
                         const char *module,
                         const char *context);

#endif
```

This keeps RTT visible but lightweight.

---

## 2️⃣ Badge Emission (Minimal)

**`kernel/nawderos.c`**

```c
#include <linux/kernel.h>
#include <linux/nawderos.h>

void nawderos_emit_badge(const char *badge_type,
                         const char *module,
                         const char *context)
{
    printk(KERN_INFO
        "[NAWDEROS][BADGE] type=%s module=%s context=%s\n",
        badge_type,
        module,
        context ? context : "none");
}
```

Yes — this uses `printk`.

That’s intentional.

Tracepoints come later.  
First, we prove the concept.

---

## 3️⃣ Boot‑Time Hook

**`init/main.c`**

Add near the end of `start_kernel()`:

```c
#include <linux/nawderos.h>

...

nawderos_emit_badge(
    RTT_BADGE_SUBSTRATE_BASELINE,
    "substrateAudit",
    "kernel_boot"
);
```

This emits **exactly one badge** per boot.

No loops.  
No conditions.  
No risk.

---

## 4️⃣ Build Integration

**`kernel/Makefile`**

Add:

```makefile
obj-y += nawderos.o
```

That’s it.

---

## What You’ll See at Runtime 👀

On boot:

```text
[NAWDEROS][BADGE] type=SUBSTRATE_BASELINE module=substrateAudit context=kernel_boot
```

That single line proves:

- RTT concepts are present
- The kernel is instrumented
- Badges are real
- Nothing broke 🙂

---

## Why This MVP Is Correct

This patch:

- Demonstrates RTT without overreach
- Matches the documentation exactly
- Gives students something concrete to see
- Creates a stable anchor for future work
- Avoids premature abstraction

Most importantly:

> It makes RTT **observable**, not theoretical.

---

## What Comes Next (Not in This Patch)

Deliberately excluded:

- Tracepoints
- `/proc/nawderian`
- Scheduler hooks
- Memory corridors
- Userspace collectors

Those belong in **v0.1.x**, not the baseline.

---

## How This Aligns with v0.1.0

This patch is the **physical manifestation** of the v0.1.0 tag:

- RTT is present
- Coherence is observable
- Lineage is preserved
- Scope is controlled

Nothing more is required for the baseline.
