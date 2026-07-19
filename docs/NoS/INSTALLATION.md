# Installing NawderOS 🛠️  
*(RTT‑Aware, Minimal, and Reversible)*

NawderOS is designed to be **easy to try and easy to remove**.  
If you can build a Linux kernel, you can install NawderOS.

No special hardware required.  
No permanent changes required.  
No fear required 🙂

---

## Before You Start

### What You’ll Need
- A Linux system (or VM)
- Basic familiarity with building a kernel
- Disk space for a kernel build
- Curiosity 😄

### What You *Don’t* Need
- A dedicated machine
- Deep kernel hacking experience
- Belief in RTT (seriously)

---

## Recommended Setup 🧪

For first‑time users, we recommend:

- A **virtual machine** (QEMU, VirtualBox, etc.)
- Or a **secondary boot entry** on a dev machine

NawderOS should never replace your daily driver OS.

---

## Step 1: Get the Source 📦

Clone the TriadicFrameworks repository:

```bash
git clone https://github.com/umaywant2/TriadicFrameworks.git
cd TriadicFrameworks
```

This repo contains:
- Documentation
- Kernel patch notes
- Optional tooling

---

## Step 2: Get a Linux Kernel 🌱

Clone a vanilla Linux kernel (LTS preferred):

```bash
git clone https://git.kernel.org/pub/scm/linux/kernel/git/stable/linux.git
cd linux
```

Any recent 6.x kernel should work.

---

## Step 3: Apply NawderOS Patches 🔧

NawderOS uses **minimal, readable patches**.

From the kernel directory:

```bash
patch -p1 < ../TriadicFrameworks/docs/NoS/patches/nawderos.patch
```

(Exact patch paths may evolve — check `KERNEL_BUILD.md`.)

If the patch applies cleanly, you’re good 🙂

---

## Step 4: Configure the Kernel ⚙️

Start from a known‑good config:

```bash
make defconfig
```

Then enable RTT‑related options (names may change):

```bash
make menuconfig
```

Look for:
- `CONFIG_NAWDEROS`
- `CONFIG_RTT_OBSERVATION`
- `CONFIG_NAWDER_BADGES`

These options **only enable observation**, not enforcement.

---

## Step 5: Build the Kernel 🧠

Build as usual:

```bash
make -j$(nproc)
```

Then install modules and kernel:

```bash
sudo make modules_install
sudo make install
```

This should add a new boot entry.

---

## Step 6: Boot and Observe 👀

Reboot and select the NawderOS kernel.

Once booted:
- Check kernel logs
- Look for badge emissions
- Confirm the system behaves normally

If something feels wrong, reboot into your previous kernel.  
Nothing permanent has changed 🙂

---

## Where to See RTT in Action 🏷️

Depending on configuration, badges may appear in:
- kernel logs
- trace output
- `/proc/nawderian` (if enabled)

Badges are **signals**, not errors.

Seeing nothing is also valid — it means nothing drifted 😄

---

## Uninstalling / Rolling Back 🔄

To remove NawderOS:
- Boot into your original kernel
- Remove the NawderOS kernel entry
- Delete the patched kernel source if desired

No system state is altered beyond the kernel itself.

---

## Troubleshooting 🛟

If something goes wrong:
- Disable RTT options in `.config`
- Rebuild the kernel
- Boot clean

If the system fails to boot:
- Use your previous kernel
- RTT hooks should never block boot

---

## Final Notes 🌱

NawderOS is about **learning and observation**, not perfection.

If you break it:
- you learned something
- that’s a win 🙂
