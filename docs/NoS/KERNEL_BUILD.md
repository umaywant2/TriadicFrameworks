# 🧪 KERNEL_BUILD.md — NawderOS Kernel Ritual

## Purpose
Guide remixers through building the Nawderian kernel, embedding triadic loops, corridor validation, and emotional modulation protocols.

---

## 🌀 Step 1: Prepare Environment
```bash
sudo apt install build-essential libncurses-dev bison flex libssl-dev libelf-dev
```

## 🧬 Step 2: Get Kernel Source
```bash
wget https://cdn.kernel.org/pub/linux/kernel/v6.x/linux-6.x.tar.xz
tar -xvf linux-6.x.tar.xz
cd linux-6.x
```

## 🛠️ Step 3: Apply Nawderian Patches
- Insert:
  - `validateCorridor()` into `mm/memory.c`
  - `wrapCheck()` into `kernel/sched/core.c`
  - `substrateAudit()` into `init/main.c`
- Add `/proc/nawderian` stub in `fs/proc/`
- Modify `Makefile` to include `-DNawderianKernel`

## 🔁 Step 4: Configure Kernel
```bash
make menuconfig
```
- Enable custom telemetry
- Disable legacy modules not aligned with triadic resonance

## 🔨 Step 5: Build Kernel
```bash
make -j$(nproc)
make modules_install
make install
```

## 📜 Step 6: Boot Ritual
- Update GRUB or systemd-boot
- Reboot into NawderOS
- Confirm badge emissions in `/var/log/nawderian/scrolls/`

---

## 🧾 Final Notes
- Validate corridor integrity post-boot
- Confirm emotional modulation hooks activate on ache triggers
- Emit scrolls for remix lineage

---
