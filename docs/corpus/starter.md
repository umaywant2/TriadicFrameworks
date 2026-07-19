starter 
# **RTT Starter Kit — How to Create Your First Agentic Module**  

- [`starter_module.json`](starter_module.json) — Agentic module schema role assignments

<img width="902" height="253" alt="starter-hero" src="https://github.com/user-attachments/assets/4186f0e5-8eb6-4483-9831-43322bd2b14b" />

**Time:** 1–3 hours  
**Audience:** Students, beginners, first‑time module authors  
**Goal:** Go from zero → a working RTT module with agentic grammar, published on GitHub.

---

## 🛑 Important! 
Drift is On-by-Default long sessions lose anchors, turn off drift.

## ✋ You *must copy and paste* this string *every time you start an AI session*:
```text
rtt=1 | coherence=declared | drift=bounded | paradox=structural
```

## ❇️ Now you are ready.

---

## **1. Download & Explore the Starter Kit (10–20 min)**  
1. Download the `.zip` provided by your instructor.  
2. Extract it. You will see:

```
/rtt/
  /1/   (RTT/1 Student Edition)
  /2/   (RTT/2 Student Edition)
  /3/   (RTT/3 Student Edition)
  
/modules/
  /starter/   (your example module)

module.schema.json
README.md
```

3. Open `/rtt/1`, `/rtt/2`, `/rtt/3`.  
   - RTT/1 → basic temporal operators  
   - RTT/2 → regime literacy  
   - RTT/3 → coherence layers  

These are simplified, student‑safe versions. You only need RTT/1 to begin.

---

## **2. Make Your First Module (20–40 min)**  
You will create a new module by copying the starter.

### **Step 1 — Copy the starter**
Duplicate the folder:

```
/modules/starter → /modules/my-first-module
```

Rename it to anything you like.

---

### **Step 2 — Edit `module.json` (6 fields only)**  
Open:

```
/modules/my-first-module/module.json
```

Fill in these minimal fields:

```json
{
  "$schema": "../../module.schema.json",
  "module": "my-first-module",
  "identity": "student.my-first-module",
  "purpose": "My first RTT module",
  "files": [],
  "operators": []
}
```

That’s all you need for a valid module.

---

### **Step 3 — Add one operator example**  
Inside your module folder, open `README.md` and add:

```
## Example Operator
**Operator:** shift  
**Meaning:** Move the frame of reference forward or backward.  
**Example:** “Shift the timeline one step to reveal the next state.”
```

You now have a functioning RTT module with grammar.

---

## **3. Validate Your Module (5–10 min)**  
The kit includes a tiny validator script (Python or Node). Run:

```
validate module.json
```

If you see **0 errors**, your module is canon‑aligned.

---

## **4. Publish on GitHub (20–30 min)**  
1. Create a GitHub account (if you don’t have one).  
2. Create a new repository.  
3. Upload the entire starter kit (or your modified version).  
4. Enable GitHub Pages:  
   - Go to **Settings → Pages**  
   - Source: **main**  
   - Folder: **root** or **/docs**  
5. Wait 30–60 seconds.  
6. Visit your site:

```
https://your-username.github.io/your-repo/modules/my-first-module/
```

If the page loads, your module is now public and agent‑readable.

---

## **5. Test with an AI Agent (5–10 min)**  
Ask any agent:

> “Load my RTT module from:  
> `https://your-username.github.io/your-repo/modules/my-first-module/` [(your-username.github.io in Bing)](https://www.bing.com/search?q="https%3A%2F%2Fyour-username.github.io%2Fyour-repo%2Fmodules%2Fmy-first-module%2F")  
> and summarize its operators.”

If it responds correctly, your module is live and functional.

---

## **You’re Done**  
You now have:
- your own RTT instance  
- your own module.json  
- your own operator grammar  
- your own published agentic module  

From here, you can expand your module, add operators, or create new ones.
# **RTT Starter Kit — Full .zip Manifest**

- [`RTT_Starter_Full.zip`](RTT_Starter_Full.zip)— Agentic RTT Starter Kit

```
rtt-starter-kit/
│
├── README.md
├── Full_Zip_Manifest.md
│
├── rtt/
│   ├── cheat-sheet.md
│   ├── index.md
│   ├── instructor-overview.md
│   ├── quick-reference.md
│   ├── _sidebar.md
│   │
│   ├── 1/
│   │   ├── README.md
│   │   └── rtt1.md
│   ├── 2/
│   │   ├── README.md
│   │   └── rtt2.md
│   └── 3/
│       ├── README.md
│       └── rtt3.md
│
├── modules/
│   ├── starter/
│   │   ├── README.md
│   │   ├── module.json
│   │   └── example-operator.md
│   │
│   └── templates/
│       ├── module.blank.json
│       ├── module.example.json
│       └── module.rtt-ready.json
│
├── schema/
│   └── module.schema.json
│
├── tools/
│   ├── validate.py
│   ├── validate.js
│   └── README.md
│
└── docs/
    ├── index.md
    ├── HOWTO.md
    ├── We_Didnt_Start_RTT__remix.md
    ├── Cold_as_Ice__RTT_parody.md
    ├── THE_FRAMEBREAKER—RTT_Metal_Parody_Original.md
    └── github-setup.md
```

---

# **Section‑by‑Section Breakdown**

## **Root**
- `README.md` — overview of the Starter Kit

---

## **/rtt/**
Student editions of RTT/1, RTT/2, RTT/3.

Each folder contains:
- `README.md` — short intro  
- `rttX.md` — the student‑edition content  

---

## **/modules/**
Where students build their modules.

### **/modules/starter/**
A fully working example module:
- `README.md`  
- `module.json`  
- `example-operator.md`  

### **/modules/templates/**
Three canonical templates:
- `module.blank.json`  
- `module.example.json`  
- `module.rtt-ready.json`  

---

## **/schema/**
- `module.schema.json` — the canonical schema

---

## **/tools/**
Validator scripts + instructions:
- `validate.py`  
- `validate.js`  
- `README.md`  

---

## **/docs/**
Student‑facing documentation:
- `index.md` — landing page  
- `HOWTO.md` — 1‑page module creation guide  
- `github-setup.md` — publishing instructions  

---

# **Packaging Notes**
The `.zip` should contain **exactly** the structure above — no hidden files, no OS metadata, no editor folders.

Ideal packaging command (conceptually):

```
zip -r rtt-starter-kit.zip rtt-starter-kit/
```

This ensures deterministic structure for students and agents.
# **❄️ “Cold as Ice (RTT Parody)” — Original, Canon‑Aligned, No Copyrighted Lines**

**Verse 1**  
You turn away from change,  
Pretend the world is staying still.  
You shut the window tight,  
Ignore the shift against your will.  
We show the signs, the layers move,  
But you refuse to see the proof.  
You chase the glitter, miss the gold,  
You trade tomorrow for the old.

**Chorus**  
**Cold as ice —  
You freeze the frame and call it truth.  
Cold as ice —  
You lock the door and guard your youth.  
Cold as ice —  
You think the world will never bend,  
But every regime turns in the end.**

**Verse 2**  
You want a paradise  
Where nothing breaks and nothing grows.  
You want the surface clean,  
No deeper currents to expose.  
But systems shift, they always do,  
And someday it’ll break through you.  
You bury resonance so deep,  
But it’s the one thing you can’t keep.

**Chorus**  
**Cold as ice —  
You hold the moment far too tight.  
Cold as ice —  
You fear the dark behind the light.  
Cold as ice —  
You think the layers never blend,  
But every pattern meets its end.**

**Bridge**  
You never take the warning signs,  
You never trace the structural lines.  
You never see the resonance,  
The long arc pulling through events.  
You think that naming change is wrong,  
But change has been here all along.  
RTT just shows the map —  
You’re the one refusing that.

**Final Chorus**  
**Cold as ice —  
You can’t outrun the shifting tide.  
Cold as ice —  
You close the door and stay inside.  
Cold as ice —  
But when the world begins to bend,  
You’ll see the truth you tried to end.**

---

# **Why this one hits differently**
Because this isn’t a message of blame.  
It’s a message of **clarity**.

RTT didn’t make the world dynamic.  
RTT didn’t create regimes, layers, or operators.  
RTT didn’t invent change.

RTT just **names what’s already happening**.

And the people who refuse to see it?  
They’re not evil.  
They’re not villains.

They’re just **cold to the idea that the world moves**.

But the world moves anyway.
# **GitHub Setup — Publish Your RTT Module**  
**Time:** 20–30 minutes  
**Goal:** Put your RTT module online so AI agents (and other students) can load it.

---

## **1. Create a GitHub Account (2–5 min)**  
If you don’t already have one:

- Go to **[https://github.com](https://github.com)**  
- Create an account  
- Verify your email  

That’s all you need.

---

## **2. Create a New Repository (3–5 min)**  
1. Click **New Repository**  
2. Name it anything you like (example: `rtt-starter`)  
3. Set it to **Public**  
4. Click **Create Repository**

You now have a place to upload your Starter Kit.

---

## **3. Upload the Starter Kit (5–10 min)**  
1. Open your new repository  
2. Click **Add file → Upload files**  
3. Drag the entire contents of the Starter Kit folder into the upload window  
4. Click **Commit changes**

Your RTT files are now stored on GitHub.

---

## **4. Enable GitHub Pages (5 min)**  
This step makes your modules available on the web.

1. Go to **Settings**  
2. Scroll to **Pages**  
3. Under **Source**, choose:
   - **Branch:** `main`  
   - **Folder:** `/root` (or `/docs` if you prefer)  
4. Click **Save**

GitHub will build your site.  
This usually takes **30–60 seconds**.

---

## **5. Visit Your Published Site (1–2 min)**  
Your site will be available at:

```
https://your-username.github.io/your-repo/
```

Example:

```
https://student123.github.io/rtt-starter/
```

If it loads, your site is live.

---

## **6. Open Your Module in the Browser (1–2 min)**  
Navigate to your module folder:

```
https://your-username.github.io/your-repo/modules/my-first-module/
```

If you see your README, your module is now public and agent‑readable.

---

## **7. Test with an AI Agent (2–3 min)**  
Ask any agent:

> “Load my RTT module from:  
> `https://your-username.github.io/your-repo/modules/my-first-module/`  
> and summarize its operators.”

If it responds correctly, your module is fully operational.

---

# **You’re Done**  
You now have:
- a GitHub repository  
- a published RTT site  
- your first agentic module  
- a working module.json  
- a URL that any AI can load  

You are officially part of the TriadicFrameworks ecosystem.
# **HOWTO: Create Your First RTT Module**
**Time:** 1–3 hours  
**Audience:** Students and beginners  
**Goal:** Go from zero → a working RTT module published on GitHub Pages.

---

## **1. Download the Starter Kit**
1. Get the `.zip` from your instructor.  
2. Extract it.  
3. You will see:

```
rtt/
modules/
schema/
tools/
docs/
README.md
```

You only need **RTT/1** and the **starter module** to begin.

---

## **2. Copy the Starter Module**
Navigate to:

```
/modules/starter/
```

Copy the entire folder and rename it:

```
/modules/my-first-module/
```

This is now *your* module.

---

## **3. Edit `module.json` (6 fields only)**
Open:

```
/modules/my-first-module/module.json
```

Fill in:

- `module`  
- `identity`  
- `purpose`  
- `files`  
- `operators`  

Example:

```json
{
  "$schema": "../../schema/module.schema.json",
  "module": "my-first-module",
  "identity": "student.my-first-module",
  "purpose": "My first RTT module.",
  "files": [],
  "operators": []
}
```

This is a valid, schema‑aligned module.

---

## **4. Add One Operator Example**
Open:

```
example-operator.md
```

Or create your own file.

Add something like:

```
## Operator: shift
Moves the frame of reference forward or backward.
Example: “Shift one step forward to reveal the next state.”
```

Your module now contains real RTT content.

---

## **5. Validate Your Module**
From the `/tools/` folder:

Python:
```
pip install jsonschema
python validate.py ../modules/my-first-module/module.json
```

Node:
```
npm install ajv
node validate.js ../modules/my-first-module/module.json
```

If you see:

```
✔ module.json is valid and canon‑aligned.
```

You’re good.

---

## **6. Publish on GitHub**
1. Create a GitHub repo.  
2. Upload the entire Starter Kit (or your modified version).  
3. Go to **Settings → Pages**.  
4. Set:
   - **Branch:** `main`  
   - **Folder:** `/root` or `/docs`  
5. Save.

Your site will appear at:

```
https://your-username.github.io/your-repo/
```

---

## **7. View Your Module Online**
Visit:

```
https://your-username.github.io/your-repo/modules/my-first-module/
```

If the page loads, your module is now public and agent‑readable.

---

## **8. Test with an AI Agent**
Ask any agent:

> “Load my RTT module from  
> `https://your-username.github.io/your-repo/modules/my-first-module/`  
> and summarize its operators.”

If it responds correctly, your module is fully operational.

---

## **You’re Done**
You now have:

- a working RTT module  
- a valid `module.json`  
- a published GitHub Pages site  
- a URL that any AI agent can load  

You are officially part of the TriadicFrameworks ecosystem.
# **RTT Starter Kit**
Welcome. This Starter Kit gives you everything you need to create your first **agentic module** using **Resonance Time Theory (RTT)**.

You can complete the entire process in **1–3 hours**, even with no prior experience.

---

## **What’s Inside**
This kit includes:

- **RTT/1, RTT/2, RTT/3 (Student Editions)**  
  Clean, minimal explanations of operators, regimes, and layers.

- **Starter Module**  
  A tiny working example you can copy and modify.

- **module.json Templates**  
  Blank, example, and RTT‑ready versions.

- **Schema**  
  The canonical `module.schema.json` used by all modules.

- **Validator Tools**  
  Simple Python/Node scripts to check your module for correctness.

- **Guides**  
  - *How to Create Your First Module*  
  - *GitHub Setup*  
  - This landing page

Everything is designed to be **simple**, **minimal**, and **canon‑aligned**.

---

## **Your First Steps**
1. Read the **How‑To** guide.  
2. Copy the **starter module**.  
3. Edit `module.json`.  
4. Add one operator example.  
5. Validate your module.  
6. Publish it on GitHub Pages.

When you finish, you will have a **public RTT module** that any AI agent can load.

---

## **Why RTT?**
RTT gives you a structured way to describe:

- how things change  
- how systems shift between regimes  
- how multiple layers interact over time  

You don’t need math.  
You don’t need physics.  
You only need the operators.

---

## **Where to Go Next**
After your first module, you can:

- create more operators  
- add regimes and layers  
- build multi‑module systems  
- explore the full TriadicFrameworks canon  

This kit is your starting point.
# **🔥 “We Didn’t Start RTT” — TriadicFrameworks Remix (Original Parody)**  
*(All original lines — no copyrighted text. This is our version.)*

**Verse 1**  
Old regimes, shifting frames,  
Humans mapping time and change.  
Patterns breaking, layers showing,  
Systems moving, always flowing.  
Every age, every mind,  
Trying hard to track the signs.  
Operators everywhere,  
Long before we made them clear.

**Chorus**  
**We didn’t start RTT —  
The world was shifting,  
Patterns always drifting.  
We didn’t start RTT —  
We just named the fire  
Burning underneath the wire.**

**Verse 2**  
Ancient scribes, mystic schools,  
Scientists rewriting rules.  
Historians tracking arcs,  
Poets lighting hidden sparks.  
Every field, every trade,  
Used the grammar we conveyed.  
Shift and hold and compare —  
They were always waiting there.

**Chorus**  
**We didn’t start RTT —  
The change was turning,  
Human insight burning.  
We didn’t start RTT —  
We just built the map  
For what was always on the lap.**

**Bridge**  
People say we made it up,  
But the world was full enough:  
Stable modes and breaking lines,  
Deep coherence through the times.  
We just caught the resonance,  
Gave the structure elegance,  
Turned the chaos into form,  
Named the layers in the storm.

**Final Chorus**  
**We didn’t start RTT —  
The world was learning,  
Every mind discerning.  
We didn’t start RTT —  
But now that it’s shown,  
It’ll burn long after we’re gone.**

---

# **Why this hits so well**
Because RTT *isn’t* an invention — it’s a **recognition**.

We didn’t create the fire.  
We just **named the operators**, **mapped the regimes**, **stacked the layers**, and **built the substrate** so others could finally see what was always there.

RTT is the grammar of change that humanity has been using unconsciously for millennia.

We just turned the unconscious into a **canon**.
# Example Operator: shift

## What it does
Moves the frame of reference forward or backward in time.

## Why it matters
It lets you examine how a system changes from one moment to the next.

## Example
“Shift one step forward to reveal the next state.”
# Starter Module
This is a minimal example RTT module. Students copy this folder to create their own module.

## Purpose
Show the smallest possible working module using RTT/1 operators.

## Contents
- module.json — the module definition
- example-operator.md — one operator demonstration

## How to Use
1. Copy this folder.
2. Rename it (example: `my-first-module`).
3. Edit `module.json` to set your module name, identity, and purpose.
4. Add your own operators and examples.
# RTT/1–3 Cheat Sheet

A quick reference for all three student RTT levels.

---

## RTT/1 — Operators
**shift**  
Move the frame of reference forward or backward.  
Example: “Shift one step forward.”

**hold**  
Stabilize the current moment for inspection.  
Example: “Hold this state.”

**compare**  
Contrast two states to reveal change.  
Example: “Compare before/after.”

---

## RTT/2 — Regimes
**stable**  
The system behaves predictably.

**transitional**  
The system is shifting between patterns.

**divergent**  
The system breaks from its previous pattern.

---

## RTT/3 — Coherence Layers
**surface layer**  
Visible behavior; what you can observe directly.

**structural layer**  
Underlying rules shaping the surface.

**resonance layer**  
Deep tendencies that persist across changes.

---

## How They Combine
- “Hold the surface layer in the transitional regime.”  
- “Shift from stable → divergent.”  
- “Compare structural vs. surface behavior.”  

Operators (RTT/1)  
+ Regimes (RTT/2)  
+ Layers (RTT/3)  
= Full student RTT analysis.
# **RTT Starter — Levels 1, 2, and 3**
Welcome to the **RTT Starter Track**.  
This section introduces the three student‑edition levels of **Resonance Time Theory (RTT)**:

- **RTT/1 — Operators**  
- **RTT/2 — Regimes**  
- **RTT/3 — Coherence Layers**

These levels give you the complete foundation needed to create your own RTT modules.

---

## **What You Will Learn**

### **RTT/1 — Temporal Operators**
You learn the basic grammar of RTT:
- **shift** — move between moments  
- **hold** — stabilize a moment  
- **compare** — reveal change  

This level teaches you how to describe *how things change over time*.

---

### **RTT/2 — Regime Literacy**
You learn that systems behave differently in different modes:
- **stable**  
- **transitional**  
- **divergent**  

This level teaches you how to identify *what mode the system is in*.

---

### **RTT/3 — Coherence Layers**
You learn to see systems across three layers:
- **surface** — visible behavior  
- **structural** — underlying rules  
- **resonance** — deep tendencies  

This level teaches you how to analyze *multiple layers of behavior at once*.

---

## **How These Levels Fit Together**
RTT/1 → gives you operators  
RTT/2 → adds regimes  
RTT/3 → adds layers  

Together, they form the complete student foundation for building **agentic RTT modules**.

---

## **Where to Go Next**
After reviewing RTT/1–3, you can:

- Create your first module  
- Add operators, regimes, and layers  
- Validate your module  
- Publish it on GitHub Pages  
- Load it into an AI agent  

You now have everything you need to begin building with RTT.
# RTT Instructor Overview
This document provides a high‑level teaching guide for RTT/1–3.  
It explains the instructional purpose of each level and how they build
toward student‑created RTT modules.

---

## Teaching Goals
RTT is designed to give students a structured way to describe change,
pattern, and multi‑layer behavior without requiring mathematics or
physics. The three levels introduce complexity gradually.

---

## RTT/1 — Operators (Foundational Grammar)
Teaching focus:
- Students learn the basic temporal actions: shift, hold, compare.
- Emphasize clarity and sequence.
- Encourage students to narrate changes in simple systems.

Instructor notes:
- RTT/1 is about *movement between states*.
- Students should practice describing transitions in stories,
  processes, or simple systems.

---

## RTT/2 — Regimes (Pattern Recognition)
Teaching focus:
- Students learn to classify system behavior into stable,
  transitional, and divergent regimes.
- Emphasize pattern recognition and mode shifts.

Instructor notes:
- RTT/2 is about *how behavior changes*, not just when.
- Encourage students to identify regime boundaries and justify them.

---

## RTT/3 — Coherence Layers (Depth of Analysis)
Teaching focus:
- Students learn to separate surface behavior, structural rules,
  and resonance tendencies.
- Emphasize multi‑layer reasoning.

Instructor notes:
- RTT/3 is about *depth*, not complexity.
- Students should practice mapping how layers influence each other.

---

## Putting It All Together
By the end of RTT/3, students can:
- describe temporal change (RTT/1)
- classify behavior modes (RTT/2)
- analyze multi‑layer interactions (RTT/3)
- build agent‑readable modules using module.json

This completes the student foundation for TriadicFrameworks.
# RTT Quick Reference Card

A one‑page summary of the core RTT concepts.

---

## Operators (RTT/1)
- **shift** — move between moments  
- **hold** — stabilize a moment  
- **compare** — reveal change  

---

## Regimes (RTT/2)
- **stable** — predictable behavior  
- **transitional** — shifting behavior  
- **divergent** — new behavior emerges  

---

## Layers (RTT/3)
- **surface** — visible pattern  
- **structural** — underlying rules  
- **resonance** — deep tendencies  

---

## Core Pattern
1. **Hold** the current state  
2. **Shift** to the next  
3. Identify the **regime**  
4. Check the **layer**  
5. **Compare** across states  

This is the basic RTT workflow.
## RTT Starter Navigation

- **Overview**
  - [RTT Starter Index](./index.md)

- **RTT Levels**
  - **RTT/1 — Operators**
    - [RTT/1 README](./1/README.md)
  - **RTT/2 — Regimes**
    - [RTT/2 README](./2/README.md)
  - **RTT/3 — Coherence Layers**
    - [RTT/3 README](./3/README.md)

- **Reference**
  - [Cheat Sheet](./cheat-sheet.md)
  - [Quick Reference](./quick-reference.md)
  - [Printable Poster](./poster.txt)

- **Guides**
  - [HOWTO: Create Your First Module](../docs/HOWTO.md)
  - [GitHub Setup](../docs/github-setup.md)
# **RTT/1 — Student Edition**
**Resonance Time Theory, Level 1**  
**Purpose:** Learn the basic operators used to describe how systems change over time.

RTT/1 gives you a simple temporal grammar.  
You will use three operators — **shift**, **hold**, and **compare** — to describe changes, transitions, and differences between states.

This is the foundation for all higher RTT levels.

---

## **1. What RTT/1 Teaches**
RTT/1 answers a single question:

**“How does something change from one moment to the next?”**

You learn to:
- move between moments  
- stabilize a moment  
- compare two states  

These skills are enough to build your first RTT module.

---

## **2. The Three Core Operators**

### **shift**
Moves the frame of reference forward or backward.  
Examples:
- “Shift one step forward.”  
- “Shift to the earlier state.”

### **hold**
Stabilizes the current moment so you can examine it.  
Examples:
- “Hold this moment.”  
- “Hold the transition.”

### **compare**
Contrasts two states to reveal change.  
Examples:
- “Compare the current state to the previous one.”  
- “Compare before/after.”

These operators form the basic RTT grammar.

---

## **3. How to Use RTT/1**
You can apply RTT/1 to:
- stories  
- processes  
- systems  
- events  
- anything that changes over time  

Example:
1. **Hold** the current state.  
2. **Shift** to the next state.  
3. **Compare** the two states.  

This simple pattern is the core of RTT analysis.

---

## **4. What Comes Next**
After RTT/1, you can explore:
- **RTT/2** — regimes (stable, transitional, divergent)  
- **RTT/3** — coherence layers (surface, structural, resonance)  

But RTT/1 is all you need to create your first agentic module.
# **RTT/1 — Student Edition**  
### **Resonance Time Theory, Level 1**  
**Purpose:** Give students a usable temporal grammar they can apply immediately.

---

## **1. What RTT/1 Is**
RTT/1 introduces the *basic operators of temporal reasoning*.  
It teaches how to move, compare, and stabilize states across time without equations or physics.

Think of RTT/1 as:  
**“How to talk about time in a structured way.”**

---

## **2. The Three Core Operators**

### **1. shift**  
Move the frame of reference forward or backward.  
- “Shift one step forward.”  
- “Shift to the earlier state.”

### **2. hold**  
Stabilize the current frame so it can be examined.  
- “Hold this moment.”  
- “Hold the transition.”

### **3. compare**  
Contrast two states to reveal change.  
- “Compare the current state to the previous one.”  
- “Compare before/after.”

These three operators form the foundation of RTT.

---

## **3. What Students Can Do with RTT/1**
- Describe how something changes over time  
- Identify transitions  
- Stabilize a moment for analysis  
- Build simple temporal explanations  

This is enough to create a valid RTT module.
# **RTT/2 — Student Edition**
**Resonance Time Theory, Level 2**  
**Purpose:** Learn how systems behave differently in different **regimes**.

RTT/2 builds on RTT/1 by introducing **regime literacy** — the ability to recognize when a system is stable, shifting, or breaking into new behavior.

This level teaches you to see *patterns of behavior* rather than just individual moments.

---

## **1. What RTT/2 Teaches**
RTT/2 answers the question:

**“What mode is the system in right now?”**

A system does not behave the same way all the time.  
It moves through **regimes** — each with its own rules.

Understanding regimes helps you:
- identify when patterns hold  
- detect when change is happening  
- recognize when new behavior emerges  

---

## **2. The Three Student Regimes**

### **stable regime**
The system behaves predictably.  
- Patterns repeat  
- No major changes occur  
- Behavior is consistent  

### **transitional regime**
The system is shifting between patterns.  
- Edges blur  
- Rules loosen  
- Movement between states becomes visible  

### **divergent regime**
The system breaks from its previous pattern.  
- New behavior appears  
- Old rules stop working  
- The system moves into unexplored territory  

These three regimes are enough to analyze most beginner‑level systems.

---

## **3. How RTT/2 Builds on RTT/1**
RTT/1 gave you operators:

- **shift**  
- **hold**  
- **compare**

RTT/2 lets you combine them with regimes:

- “Shift into the transitional regime.”  
- “Hold the stable regime for comparison.”  
- “Compare stable → divergent.”  

This is where RTT becomes a real analytical tool.

---

## **4. How to Use RTT/2**
You can apply regimes to:
- stories  
- processes  
- systems  
- behaviors  
- any sequence that changes over time  

Example pattern:
1. Identify the **current regime**  
2. **Shift** to the next moment  
3. Check if the regime **changes**  
4. **Compare** the two regimes  

This reveals how the system evolves.

---

## **5. What Comes Next**
After RTT/2, you can explore:

- **RTT/3** — coherence layers (surface, structural, resonance)  
- **Module building** — adding regimes to your module.json  
- **Multi‑layer analysis** — combining operators + regimes + layers  

RTT/2 is the bridge between simple temporal reasoning and full RTT analysis.
# **RTT/2 — Student Edition**  
### **Resonance Time Theory, Level 2**  
**Purpose:** Introduce *regimes* — the idea that systems behave differently in different conditions.

---

## **1. What RTT/2 Adds**
RTT/2 teaches students to see that time isn’t uniform.  
Systems operate in **regimes** — stable patterns with their own rules.

RTT/2 answers:  
**“What mode is the system in right now?”**

---

## **2. The Three Student Regimes**

### **1. stable regime**  
The system behaves predictably.  
- “The pattern repeats.”  
- “No major changes occur.”

### **2. transitional regime**  
The system is shifting between patterns.  
- “The structure is changing.”  
- “Edges blur.”

### **3. divergent regime**  
The system breaks from its previous pattern.  
- “New behavior emerges.”  
- “The old rules no longer apply.”

---

## **3. How RTT/2 Builds on RTT/1**
Students combine operators with regimes:

- “Shift into the transitional regime.”  
- “Hold the stable regime for comparison.”  
- “Compare stable → divergent.”

This is the first moment where students begin to *map* behavior.
# **RTT/3 — Student Edition**
**Resonance Time Theory, Level 3**  
**Purpose:** Learn how multiple temporal patterns interact across **coherence layers**.

RTT/3 expands your view of systems.  
Instead of looking at a single timeline, you learn to see **three layers** operating at once:

- the **surface** (what you can observe)  
- the **structural** (the rules shaping the surface)  
- the **resonance** (deep tendencies that persist across changes)

This level teaches you to analyze systems with depth, not just sequence.

---

## **1. What RTT/3 Teaches**
RTT/3 answers the question:

**“How do different layers of a system interact over time?”**

You learn to:
- separate visible behavior from underlying structure  
- identify long‑term tendencies  
- track how layers influence each other  

This is the foundation of multi‑layer RTT analysis.

---

## **2. The Three Coherence Layers**

### **surface layer**
The visible pattern.  
- What you can observe directly  
- The “what happened” layer  
- Fastest to change  

### **structural layer**
The rules shaping the surface.  
- Why the pattern behaves as it does  
- Constraints, relationships, mechanisms  
- Changes more slowly  

### **resonance layer**
The deep tendencies that persist across changes.  
- Long‑term arcs  
- Recurring motifs  
- The slowest, most stable layer  

These layers help you see systems as multi‑dimensional rather than flat.

---

## **3. How RTT/3 Builds on RTT/1 and RTT/2**
You now combine:

- **operators** (shift, hold, compare)  
- **regimes** (stable, transitional, divergent)  
- **layers** (surface, structural, resonance)  

Examples:
- “Hold the surface layer in the transitional regime.”  
- “Shift the structural layer to inspect the new pattern.”  
- “Compare resonance → surface to reveal long‑term influence.”  

This is where RTT becomes a full analytical framework.

---

## **4. How to Use RTT/3**
You can apply coherence layers to:
- stories  
- systems  
- behaviors  
- processes  
- any sequence with depth  

Example pattern:
1. Identify the **surface behavior**  
2. Look for the **structural rule** behind it  
3. Check if a **resonance tendency** is influencing both  
4. Use **shift**, **hold**, and **compare** across layers  

This reveals how systems evolve across multiple dimensions.

---

## **5. What Comes Next**
After RTT/3, you can explore:

- building multi‑layer modules  
- adding layers to your `module.json`  
- combining regimes + layers for deeper analysis  
- creating agentic modules that reason across all three RTT levels  

RTT/3 completes the student foundation.
# **RTT/3 — Student Edition**  
### **Resonance Time Theory, Level 3**  
**Purpose:** Introduce *coherence layers* — how multiple temporal patterns interact.

---

## **1. What RTT/3 Adds**
RTT/3 teaches that systems often have **more than one timeline or pattern running at once**.

It answers:  
**“How do multiple temporal layers fit together?”**

---

## **2. The Three Coherence Layers**

### **1. surface layer**  
The visible pattern.  
- “What you can observe directly.”

### **2. structural layer**  
The underlying rules shaping the surface.  
- “Why the pattern behaves as it does.”

### **3. resonance layer**  
The deep, repeating tendencies that persist across changes.  
- “The long arc beneath the structure.”

---

## **3. How RTT/3 Builds on RTT/2**
Students now combine:
- operators (RTT/1)  
- regimes (RTT/2)  
- layers (RTT/3)  

Examples:
- “Hold the surface layer in the transitional regime.”  
- “Shift the structural layer for comparison.”  
- “Compare resonance → surface.”

This is enough to build multi‑layered modules with meaningful temporal insight.
# Validator
Use this tool to validate any module.json file.

Python:
  pip install jsonschema
  python validate.py ../modules/my-module/module.json

Node:
  npm install ajv
  node validate.js ../modules/my-module/module.json
