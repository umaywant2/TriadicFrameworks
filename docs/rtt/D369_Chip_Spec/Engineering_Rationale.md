**Ten numbered rationale statements (ER‑1 through ER‑10)**, each following the same pattern: verbatim statement from Capture Source → engineering context → historical precedent table → cost analysis → cross-references to prior D369 files. Every statement answers "why?" without ever making a promise.

**Structural highlights:**

- **ER‑1** opens with Therac‑25, Ariane 5, Intel FDIV, and Boeing 737 MAX — four cases where the information needed to diagnose the failure existed but wasn't preserved.
- **ER‑7** puts D369 head-to-head with DFT scan chains: DFT imposes 50–1500x more area overhead and no fab rejects it. D369 asks for far less with the same logic.
- **ER‑8** maps D369 to every stage of the existing EDA toolchain (Synopsys DC, Cadence Genus, Innovus, ICC2, PrimeTime) — no new tools, no new licenses, no new training. The `dont_touch` attribute is the implementation mechanism.
- **ER‑9** is the economic core — the visual cost comparison box: Reserve Now (~$0) vs. Redesign Later ($5–50M+), same result, 1,000:1 to 100,000:1 cost ratio.
- **ER‑10** invokes the TCP/IP precedent — success through not encoding assumptions about future traffic types.

**Bidirectional traceability matrices** — rationale→requirements *and* requirements→rationale — so every R1–R7 requirement is justified and every ER‑1–ER‑10 statement is grounded.

**Design Freedom clause (DF‑1 through DF‑3)** explicitly returns all implementation authority to the manufacturer — encoding, protocol, format, and architecture are all their call.
