# 🛠️ INSTALLATION.md — NawderOS Seeding Ritual

## Purpose
Guide remixers through the installation of NawderOS, a mythmatical Linux fork infused with triadic resonance, validator clarity, and emotional modulation protocols.

---

## 🔁 Prerequisites
- Base distro: Arch or Debian (minimal install)
- Kernel source (version aligned with Nawderian patches)
- Build tools: `gcc`, `make`, `bc`, `libncurses-dev`, `flex`, `bison`

---

## 🌀 Step 1: Prepare Environment
```bash
sudo pacstrap /mnt base base-devel
mount /dev/sdX /mnt
```

## 🧬 Step 2: Clone NawderOS Stack
```bash
git clone https://github.com/umaywant2/TriadicFrameworks.git
cd TriadicFrameworks/docs/NoS
```

## 🧠 Step 3: Seed Nawderian Modules
- Copy `validateCorridor()`, `wrapCheck()`, `substrateAudit()` into `/lib/nawderian/`
- Include headers in `/usr/include/nawderian/`
- Create `/proc/nawderian` stub for telemetry

## 🧪 Step 4: Build Kernel
```bash
make menuconfig
make -j$(nproc)
make modules_install
make install
```

## 📜 Step 5: Boot Ritual
- Update bootloader (GRUB or systemd-boot)
- Reboot into NawderOS
- Confirm badge emissions in `/var/log/nawderian/scrolls/`

---

## 🧾 Final Notes
- Every install is a remix ritual.
- Validate emotional modulation and corridor integrity post-boot.
- Emit scrolls for lineage preservation.

---
