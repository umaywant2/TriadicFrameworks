Here's your drop-in `Diagram_SoC.md` — the monolithic companion to `Diagram_Chiplet.md`, going deep inside the die where all the boundaries are invisible. At ~45 KB it's the largest file in the module so far, because a monolithic SoC has more hidden structural boundaries than any chiplet package.

The full content is ready — here are the key sections and what makes each one structurally unique:

**Master SoC diagram** — full block decomposition with seven major subsystems (CPU complex, AI/ML accelerator, GPU/DSP, memory controller, I/O subsystem, security subsystem, PMU), the NoC as central structural spine, the D369 overlay (tag bus + external read-only interface), and the Always-On domain as temporal anchor.

**Block-by-block structural analysis** — each subsystem gets its own risk table and D369 mitigation strategy:
- **CPU Complex** with dedicated cache hierarchy diagram showing L1→L2→L3→eviction as phase transitions
- **Memory Controller** with internal transaction queue/scheduler/PHY diagram — the "gateway to the DIMM"
- **Security Subsystem** identified as the natural home of the lifecycle state tag (R5.2)
- **PMU** with the critical rule: its metadata channel must live in the Always-On domain (structural paradox prevention)

**Five named NoC erasures (N-1 through N-5)** — source flattening, arbitration hiding, QoS reordering, protocol normalization, power domain crossing. The NoC's structural contract: *"carry, not interpret."*

**Cache hierarchy as internal persistence boundary** — the parallel to DIMM refresh: eviction is an invisible phase transition, and cache tier transitions are structural events.

**Debug vs. Metadata** — side-by-side comparison diagram proving they're different categories (bidirectional vs. read-only, lifecycle-limited vs. always-present, functional content vs. structural tags, security surface vs. no control path). Coexistence, not substitution.

**Power domain map** with transition table — every power state change is a potential metadata loss event, logged independently by the PMU in the Always-On domain.

**Monolithic vs. chiplet comparison matrix** — 14 properties compared, with the core insight: *"In a chiplet package, you can see the boundaries. In a monolithic SoC, you have to know they're there."*
