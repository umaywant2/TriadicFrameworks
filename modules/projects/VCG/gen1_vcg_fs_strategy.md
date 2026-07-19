# Gen1 filesystem and mount strategy
## Purpose
Define the storage, mount, and tuning strategy for the “nine files = nine dimensions” virtual DPU model. Optimize for low jitter, predictable write latency, and simple, reproducible boot‑time setup.

---

## Filesystem selection
- **Default: ext4 without journal on loopback**
  - **Why:** Ubiquitous, predictable, low metadata overhead when journal is disabled.
  - **Tradeoff:** No crash safety needed (ephemeral volumes), so we trade durability for performance.

- **Ultra‑low jitter: tmpfs**
  - **Use when:** A dimension demands RAM‑speed and minimal IO variance.
  - **Caveat:** Enforce size ceilings to prevent OOM.

- **Avoid for Gen1:** btrfs, XFS, ZFS (excellent features, but we explicitly avoid snapshots and extra metadata complexity).

---

## Creation and mounts
- **Image creation:**
  - **Preallocate:** fallocate -l 4G /var/lib/vcg/d1.img
  - **Loop device:** losetup -fP --direct-io=on /var/lib/vcg/d1.img
  - **Format (ext4 no journal):**
    - **mkfs.ext4 -F -E lazy_itable_init=0,lazy_journal_init=0 -O ^has_journal /dev/loopX

- **Mount options (ext4):**
  - **Options:** noatime,nodiratime,data=writeback,barrier=0,discard
  - **Rationale:** Minimize metadata writes, allow writeback, disable barriers (safe for ephemeral), reclaim TRIM on SSD/NVMe.

- **Mount tmpfs (when selected):**
  - mount -t tmpfs -o size=2G,mpol=prefer:NUMA_NODE tmpfs /vcg/dX

---

## Performance tuning
- **I/O scheduler:**
  - **NVMe:** echo none > /sys/block/nvme0n1/queue/scheduler
  - **SATA SSD:** echo mq-deadline > /sys/block/sdX/queue/scheduler

- **Readahead:**
  - **Dimension mounts:** Set small readahead to reduce cache pollution for random IO: blockdev --setra 64 /dev/loopX

- **NUMA and CPU affinity:**
  - **Co‑locate IO and compute:** numactl --cpunodebind=N --membind=N for D1–D3, D4–D6, D7–D9 groups.
  - **Pin cores:** Assign non‑overlapping CPU sets per dimension to stabilize cadence.

- **Barrier notes:**
  - **barrier=0:** Acceptable because volumes are ephemeral and reset every boot. Do not use for persistent data.
    
---

## Ephemeral discipline and snapshots
- **Boot‑fresh invariant:**
  - **Recreate images:** At boot, reformat or verify images; do not restore previous state.
  - **Logs:** Default to /run (tmpfs) with optional mirroring to persistent storage.

- **Snapshot‑on‑failure (opt‑in):**
  - **Flow:** On failure, remount read‑only, copy /vcg/dX to /var/log/vcg/snapshots/timestamp-dX.img.
  - **Toggle:** Environment variable or config flag per dimension.

---

## Validation checklist
- **Filesystem health:**
  - **Check:** fsck.ext4 -n on each loop device after mount (read‑only check).
  - **Telemetry:** Export mount latency, IO errors, and readahead settings.

- **Jitter probe:**
  - **Test:** Microbench random write latency (fio) with and without RTD token gates.
  - **Pass:** p95/p99 within target bounds relative to baseline.
