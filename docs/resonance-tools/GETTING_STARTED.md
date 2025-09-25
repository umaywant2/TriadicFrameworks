# 🚀 Getting Started with the Resonance CLI Suite

Welcome to the **Resonance CLI Suite**—a living organism of tools that model resonance across time, frameworks, numbers, loops, technology, physics, and integration.

This guide will help you install, run, and chain the tools together.

---

## 📦 Installation

Clone the repo:
```bash
git clone https://github.com/umaywant2/TriadicFrameworks.git
cd TriadicFrameworks/docs/resonance-tools
```
(Optionally, set up a virtual environment.)
```bash
python3 -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```
Install dependencies (if any are added later):
```bash
pip install -r requirements.txt
```
---
## 🖥️ Running Tools
Each tool has its own CLI entrypoint. Run them like this:
```bash
python resonant-time/cli.py --define
python tfe/cli.py --apply computing
python triadic-numbers/cli.py --genesis 3
python harmonic-loops/cli.py --nest 2
python tft-extended/cli.py --apply cpu
python fff/cli.py --forces 3
python integrations/cli.py --demo
```
---
## 🔗 First Pipeline Demo
Let’s run the **heartbeat → DNA → skeleton → hands → muscle → mind** pipeline.

### Step 1: Generate Resonant-Time
```bash
python resonant-time/cli.py --cycle 3 --ascii
```
Output:
```bash
E → M → OC
```
### Step 2: Map into Triadic Numbers
```bash
python triadic-numbers/cli.py --map "E M OC"
```
### Step 3: Contextualize with TFE
```bash
python tfe/cli.py --apply computing
```
### Step 4: Apply TFT (CPU)
```bash
python tft-extended/cli.py --apply cpu
```
### Step 5: Add FFF (forces/flows/frequencies)
```bash
python fff/cli.py --forces 2 --fluids 1 --frequency 1
```
### Step 6: Orchestrate with Integrations
```bash
python integrations/cli.py --demo
```
## 📊 Example Dashboard
```bash
python integrations/cli.py --dashboard cpu
```
OutPut:
```
{
  "Domain": "cpu",
  "Time": "E → M → OC",
  "TFT": ["E = Instruction flow", "M = Clock cycles", "OC = Interrupt/branch"],
  "FFF": {
    "forces": ["Force vector 1"],
    "fluids": ["Fluid state 1"],
    "frequency": ["Oscillation cycle 1"]
  }
}
```





