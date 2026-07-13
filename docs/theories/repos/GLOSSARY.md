# GLOSSARY — docs/theories/repos/

TriadicFrameworks Canonical Documentation
Scope: Quantum-theoretic module registry — `docs/theories/repos/`
Status: Canonical · Living Document
Generated: 2026-07-13

---

## Purpose

This glossary defines the formal vocabulary in use across the three quantum-theoretic modules
registered in `docs/theories/repos/`. It is the single source of truth for term definitions
within this triadic cluster. All terms are canonical: they carry specific architectural meaning
within TriadicFrameworks and must not be used loosely or interchangeably.

Entries are organized alphabetically. Each entry identifies the module(s) to which the term is
native or across which it is materially relevant: **[QB]** = `quantum_basis`,
**[QL]** = `quantum-lattice`, **[LQ]** = `LattiQ`, **[ALL]** = all three modules,
**[META]** = triadic meta-term governing the cluster as a whole.

Cross-references are indicated with **→ See also**.

---

## Terms

---

**Abstraction Boundary** [LQ] [META]: The enforced separation between the internal structure of
a triadic cluster and the interface it exposes to external consumers. `LattiQ` is the abstraction
boundary of this cluster. Callers of `LattiQ` are explicitly prohibited from reasoning about
lattice topology or basis primitives directly; all such complexity is mediated through the
interface. Abstraction boundaries are the mechanism by which triadic clusters achieve
compositional stability. → See also: *Integration Seam*, *Interface (Layer III)*, *LattiQ*.

**Algebraic Composition Rules** [QB]: The formal rules governing how basis vectors and operators
combine within the Hilbert space. These rules are defined in `quantum_basis` and constitute part
of the canonical unit type contract that all higher modules must respect. → See also:
*Canonical Unit Type*, *Formal Postulate*, *State-Space Primitive*.

**Alpha (α)** [LQ]: A configurable hyperparameter in `LattiQ` controlling the fraction of the
probability distribution used in the CVaR loss function. Tuning α trades off noise robustness
against solution fidelity in VQE and QAOA solvers. → See also: *CVaR*, *QAOA*, *VQE*.

**ARPACK-NG** [QB]: An open-source library of Arnoldi/Lanczos eigenvalue routines used by
`quantum_basis` as a backend eigensolver for large sparse Hamiltonians. → See also:
*Eigensolver*, *Lanczos Method*.

**Basis Vector** [QB]: An element of the many-body Hilbert-space basis as constructed by
`quantum_basis`. Basis vectors are the primitive objects from which all quantum-state
representations in this cluster are formed. A basis vector encodes a specific occupancy
configuration of the degrees of freedom present in the model. → See also: *Hilbert Space*,
*Many-Body Basis*, *State-Space Primitive*.

**Band Structure** [QL]: The energy dispersion relation E(k) of a lattice model as a function of
crystal momentum k, computed by `quantum-lattice`. Band structures are a primary output of
tight-binding calculations and serve as phenomenological fingerprints that feed into both ED
verification and VQA encoding. → See also: *Hamiltonian*, *Tight-Binding Model*.

**Bogoliubov–de Gennes (BdG) Formalism** [QL]: A mean-field framework implemented in
`quantum-lattice` for describing superconducting systems via a Nambu spinor basis. BdG
Hamiltonians capture particle-hole symmetry and are used to model unconventional
superconductivity on lattice geometries. → See also: *Nambu Basis*, *Superconductivity (Unconventional)*.

**Bosonic Degree of Freedom** [QB]: A quantum degree of freedom obeying Bose–Einstein statistics,
characterized by commutation relations rather than anti-commutation. `quantum_basis` supports
mixed bosonic and fermionic configurations within the same many-body basis. → See also:
*Fermionic Degree of Freedom*, *Many-Body Basis*.

**Canonical Review** [META]: The governance process required before any module is added to, or
any breaking change is made to, the `docs/theories/repos/` directory. Canonical review assesses
whether a proposed change preserves triadic slot integrity and does not destabilize the
cluster's interface contract. → See also: *Governance*, *Triadic Slot*.

**Canonical Unit Type** [QB] [ALL] [META]: The formally defined primitive types — basis vectors,
operators, state representations — that `quantum_basis` establishes and that all modules in
this cluster must use without alteration. Canonical unit types are the mechanism of type
coherence across the cluster: they are enforced at the substrate level rather than retrofitted
at integration seams. → See also: *Algebraic Composition Rules*, *Formal Postulate*,
*Integration Seam*, *Type Coherence*.

**Chern Number** [QL]: An integer-valued topological invariant computed by `quantum-lattice` that
classifies the topology of energy bands in two-dimensional lattice systems. A non-zero Chern
number is the signature of a quantum Hall phase. → See also: *Topological Invariant*, *Z₂ Invariant*.

**Cluster** [ALL] [META]: The collective term for the three modules — `quantum_basis`,
`quantum-lattice`, `LattiQ` — treated as a single composable unit within TriadicFrameworks. The
cluster is the atom of canonical composition: external theories interact with the cluster
through its Layer III interface, not with individual modules. → See also: *Quantum-Theoretic
Primitive Cluster*, *Triadic Unit*.

**Cluster Versioning** [META]: The practice of incrementing the version of all three modules
simultaneously when a breaking change is made to `quantum_basis`. Because `quantum_basis` is
the dependency terminus, changes to it propagate to the entire cluster; versioning must reflect
that propagation. → See also: *Dependency Terminus*, *quantum_basis*.

**Compositional Direction** [META]: The architectural principle that triadic clusters compose
upward through their Layer III interface modules. Cross-cluster dependencies are always
Layer-III–to–Layer-III bindings; no cluster reaches into another cluster's Layer I or Layer II
internals. → See also: *Abstraction Boundary*, *Integration Seam*, *Interface (Layer III)*.

**Conditional Value-at-Risk (CVaR)** [LQ]: A loss function used in `LattiQ` in place of the
standard expectation-value objective. CVaR averages only the lowest-energy fraction α of
measurement outcomes, providing robustness against quantum hardware noise. → See also:
*Alpha (α)*, *QAOA*, *VQE*.

**Cross-Canon Impact Assessment** [META]: A mandatory governance step triggered whenever
`LattiQ`'s interface contract is modified. The assessment evaluates which other triadic clusters
or higher-order TriadicFrameworks theories depend on `LattiQ` as a boundary and whether those
dependencies remain satisfiable. → See also: *Canonical Review*, *Interface (Layer III)*, *LattiQ*.

**Dependency Terminus** [QB] [META]: The module in a triadic cluster that has no upstream
dependencies within the cluster. In this cluster, `quantum_basis` is the dependency terminus —
the floor. All other modules depend on it; it depends on none of them. → See also:
*quantum_basis*, *Cluster*.

**Downward Grounding** [ALL] [META]: One of two integration directions of the quantum-theoretic
cluster within the broader TriadicFrameworks canon. Downward grounding means this cluster
provides the mathematical and structural foundation for any canon module that makes claims about
quantum state, superposition, entanglement, or measurement. Such claims must be grounded through
`LattiQ`'s interface. → See also: *Upward Composition*, *Interface (Layer III)*.

**Eigensolver** [QB]: A numerical routine that computes eigenvalues and eigenvectors of a sparse
Hamiltonian matrix. `quantum_basis` exposes two eigensolver backends: Lanczos and FEAST. The
output of an eigensolver constitutes the exact diagonalization (ED) spectrum, which serves as
the benchmark against which higher-level approximations are measured. → See also:
*Exact Diagonalization*, *FEAST Eigensolver*, *Lanczos Method*.

**Entanglement Geometry** [QL] [META]: The structural encoding, within `quantum-lattice`, of
entanglement relationships between quantum states as explicit first-class objects. Entanglement
geometries are not emergent side-effects in this canon; they are declared structural elements of
the lattice. → See also: *Lattice Topology*, *Superposition Arrangement*.

**Exact Diagonalization (ED)** [QB]: The numerical paradigm implemented by `quantum_basis`, in
which the full Hamiltonian matrix is constructed in the many-body Hilbert-space basis and
diagonalized to obtain exact eigenvalues and eigenvectors. ED produces ground-truth spectra
against which tight-binding and variational results are benchmarked. → See also:
*Eigensolver*, *Hamiltonian*, *Many-Body Basis*.

**Extension Hook** [LQ] [META]: A documented integration point in `LattiQ` through which the
quantum-theoretic cluster can be composed with other triadic clusters in the TriadicFrameworks
canon. Extension hooks are the canonical mechanism for cross-cluster composition; they must
not expose internal lattice topology or basis primitives. → See also: *Integration Seam*,
*Compositional Direction*.

**FastVQA** [LQ]: The open-source variational quantum algorithm framework on which `LattiQ` is
built. FastVQA provides the circuit execution and optimization substrate; `LattiQ` layers
lattice-problem encoding and SVP-specific configuration on top. → See also: *LattiQ*, *VQE*, *QAOA*.

**FEAST Eigensolver** [QB]: A contour-integration-based eigensolver used in `quantum_basis` for
computing eigenvalues within a specified energy window. FEAST is suited to mid-spectrum queries
where Lanczos iteration is less efficient. → See also: *Eigensolver*, *Lanczos Method*.

**Fermionic Degree of Freedom** [QB]: A quantum degree of freedom obeying Fermi–Dirac
statistics, characterized by anti-commutation relations. `quantum_basis` supports arbitrary
combinations of fermionic and bosonic degrees of freedom in constructing the many-body basis.
→ See also: *Bosonic Degree of Freedom*, *Many-Body Basis*.

**Formal Postulate** [QB] [META]: An axiomatic constraint, defined in `quantum_basis`, that
determines what counts as a valid quantum-theoretic object within TriadicFrameworks. Formal
postulates are the canon's ontological commitments. No module in this cluster may define
quantum objects that violate these postulates. → See also: *Canonical Unit Type*,
*Quantum Ontology*.

**Foundation Layer** [QB] [META]: The TriadicFrameworks designation for `quantum_basis` in its
role as the rigorous, fully quantum-mechanical ground truth of the cluster. The Foundation
Layer provides exact spectra against which all phenomenological and variational approximations
(Layers II and III) are validated. → See also: *Dependency Terminus*, *Primitive (Layer I)*,
*quantum_basis*.

**Generalized Lin Table** [QB]: A data structure used in `quantum_basis` for encoding the
many-body basis with or without translational symmetry. The Lin Table provides an efficient
bijection between basis states and their integer indices, enabling fast matrix-vector products
in the Lanczos loop. → See also: *Many-Body Basis*, *Translational Symmetry*.

**Governance** [ALL] [META]: The set of policies governing modification, addition, and
deprecation of modules within `docs/theories/repos/`. Governance is enforced at the cluster
level: changes to any module are evaluated for their impact on the full triadic dependency
chain, not in isolation. → See also: *Canonical Review*, *Triadic Slot*.

**Green's Function** [QL]: A many-body propagator computed by `quantum-lattice`, characterizing
how a quantum system responds to perturbations as a function of energy and momentum. Green's
functions are used to compute spectral functions and local density of states, and are
fundamental inputs to recursive boundary methods for semi-infinite systems. → See also:
*Local Density of States*, *Spectral Function*.

**Hamiltonian** [QB] [QL] [LQ]: The operator encoding the total energy of a quantum system,
central to all three modules. In `quantum_basis`, it is represented as a sparse matrix in the
many-body basis and passed to eigensolvers. In `quantum-lattice`, it is constructed
phenomenologically from tight-binding and mean-field parameters. In `LattiQ`, it appears as an
Ising-mapped form encoding the lattice optimization problem. → See also: *Exact Diagonalization*,
*Ising Spin Hamiltonian*, *Tight-Binding Model*.

**Hilbert Space** [QB] [META]: The complete complex vector space of quantum states for a given
system, as defined and constructed by `quantum_basis`. The Hilbert space is the mathematical
container within which all quantum-theoretic operations in this cluster are performed. Its
dimension grows exponentially with system size, motivating the approximation strategies of
Layers II and III. → See also: *Many-Body Basis*, *State-Space Primitive*.

**Interface (Layer III)** [LQ] [META]: The third and outermost layer in any triadic cluster; the
module that makes the cluster's internal structure legible and composable to external consumers.
In this cluster, `LattiQ` occupies Layer III. The Layer III interface is the only sanctioned
point of contact between this cluster and the broader TriadicFrameworks canon. → See also:
*Abstraction Boundary*, *Extension Hook*, *LattiQ*.

**Integration Seam** [ALL] [META]: The defined boundary at which two modules or two clusters
connect. Within the cluster, integration seams exist between Layer I and Layer II (at the
point where `quantum_basis` types are consumed by `quantum-lattice`) and between Layer II and
Layer III (where `quantum-lattice` structural constructs are translated by `LattiQ`). Canonical
unit types enforce coherence at these seams. Across clusters, integration seams are always
Layer-III–to–Layer-III. → See also: *Canonical Unit Type*, *Compositional Direction*,
*Type Coherence*.

**Intel MKL** [QB]: Intel Math Kernel Library, used by `quantum_basis` as a high-performance
backend for sparse linear algebra operations underlying Hamiltonian construction and
eigensolver routines. → See also: *Eigensolver*, *Hamiltonian*.

**Ising Spin Hamiltonian** [LQ]: The binary optimization formulation used in `LattiQ`, in which
the target problem (SVP) is encoded as an energy function over spin-½ variables (±1 or 0/1).
The Ising encoding is the bridge between classical lattice geometry and quantum circuit
execution. → See also: *Hamiltonian*, *Shortest Vector Problem*, *VQE*, *QAOA*.

**Join / Meet Structure** [QL] [META]: The lattice-theoretic operations — least upper bound
(join, ∨) and greatest lower bound (meet, ∧) — through which `quantum-lattice` encodes the
partial-order relationships between quantum states. The join/meet structure is the algebraic
backbone of the lattice topology. → See also: *Lattice Topology*, *Partial Order*.

**Kagome Lattice** [QB]: One of the bundled example lattice geometries in `quantum_basis`, used
to demonstrate exact diagonalization on geometrically frustrated systems. → See also:
*Lattice Geometry*, *Exact Diagonalization*.

**Kernel Polynomial Method (KPM)** [QB]: A spectral expansion technique used in `quantum_basis`
to compute spectral functions and the density of states without full diagonalization. KPM
approximates spectral quantities via Chebyshev polynomial expansion of the Hamiltonian,
enabling access to large system sizes. → See also: *Spectral Function*, *Eigensolver*.

**Kondo Lattice Model** [QB]: A bundled example model in `quantum_basis` representing itinerant
electrons coupled to localized spins. Used to validate the many-body basis construction and ED
pipeline for models with competing energy scales. → See also: *Exact Diagonalization*,
*Many-Body Basis*.

**Landau Level** [QL]: A quantized energy level arising in a two-dimensional electron system
under a perpendicular magnetic field, computable by `quantum-lattice`. Landau levels underpin
the integer quantum Hall effect; their structure in lattice models is accessible through the
module's Hamiltonian machinery. → See also: *Quantum Hall Edge State*, *Band Structure*.

**Lanczos Method** [QB]: An iterative Krylov-subspace algorithm used by `quantum_basis` to
compute low-energy eigenvalues and eigenvectors of large sparse Hamiltonians without full
diagonalization. The Lanczos method is the primary eigensolver for ground-state and
low-spectrum queries. → See also: *Eigensolver*, *FEAST Eigensolver*.

**LattiQ** [LQ]: The Layer III — Interface module of this triadic cluster. A C++ framework,
built atop FastVQA, for solving lattice optimization problems on quantum hardware or simulators.
Its primary target is the Shortest Vector Problem, encoded as an Ising spin Hamiltonian and
solved via VQE or QAOA. As Layer III, `LattiQ` is the public face of the quantum-theoretic
cluster: the sole sanctioned entry point for external canon modules and higher-order theories.
Author: Miloš Prokop. License: MIT. → See also: *FastVQA*, *Interface (Layer III)*,
*Ising Spin Hamiltonian*, *Shortest Vector Problem*.

**Lattice Geometry** [QB] [QL] [LQ]: The spatial arrangement and connectivity of sites in a
lattice model — including square, honeycomb, Kagome, and arbitrary geometries. Lattice geometry
is specified in `quantum-lattice`, consumed by both `quantum_basis` (for ED benchmarking) and
`LattiQ` (for Ising encoding). → See also: *Hamiltonian*, *Tight-Binding Model*.

**Lattice Topology** [QL] [META]: The partial-order and join/meet structure through which
`quantum-lattice` encodes how quantum states relate to one another — which states are reachable
from which, under what operations. Lattice topology is the structural core of Layer II; it is
what `quantum-lattice` contributes to the cluster that neither Layer I nor Layer III provide.
→ See also: *Join / Meet Structure*, *Partial Order*, *Structure (Layer II)*.

**Layer** [ALL] [META]: One of three positions in a triadic cluster, designated I (Primitive),
II (Structure), or III (Interface). Each module in `docs/theories/repos/` occupies exactly one
layer. Layers are not ranks of importance but roles in a dependency and composability chain.
→ See also: *Primitive (Layer I)*, *Structure (Layer II)*, *Interface (Layer III)*.

**Lin Table** → See *Generalized Lin Table*.

**Living Document** [META]: A canonical document designation indicating that the document is
maintained and updated as the canon evolves, but does not grow by arbitrary revision —
only by justified canonical instantiation. Both `ABOUT.md` and this `GLOSSARY.md` carry Living
Document status. → See also: *Governance*.

**Load-Bearing Node** [ALL] [META]: The designation for each of the three modules within the
triadic cluster, conveying that each module is architecturally necessary — the cluster's
coherence depends on the presence and integrity of all three. The removal or failure of any
single node dissolves the cluster's functional arc. → See also: *Cluster*, *Triadic Unit*.

**Local Density of States (LDOS)** [QL]: A spatially-resolved spectral quantity computed by
`quantum-lattice`, characterizing the distribution of electronic states as a function of
energy at a specific lattice site. LDOS is computed via Green's function methods and recursive
techniques for semi-infinite systems. → See also: *Green's Function*, *Spectral Function*.

**Many-Body Basis** [QB]: The complete set of basis vectors spanning the many-body Hilbert space
for a given lattice model, as constructed by `quantum_basis`. The many-body basis is the
fundamental data structure of Layer I: it is the object over which all subsequent operations —
diagonalization, spectral computation, variational optimization — are ultimately defined.
→ See also: *Basis Vector*, *Hilbert Space*, *Generalized Lin Table*.

**Mean-Field Theory** [QL]: A classical approximation scheme implemented in `quantum-lattice`
that replaces quantum many-body interactions with an effective single-particle field. Mean-field
calculations produce phenomenological Hamiltonians that can be passed upward to `LattiQ` for
variational quantum optimization. → See also: *Hamiltonian*, *Tight-Binding Model*.

**Module** [ALL] [META]: Within this directory, a module is a curated ontological record
pairing an upstream open-source repository with its TriadicFrameworks canonical role, layer
assignment, and integration contract. A module is not merely a library; it is a load-bearing
node in the triadic architecture. → See also: *Load-Bearing Node*, *Triadic Slot*.

**Module JSON** [ALL] [META]: The structured metadata file (`*_module.json`) that constitutes the
TriadicFrameworks canonical record for each upstream repository. Module JSON files are metadata
documents, not derivative works of the upstream source code; they are therefore not subject to
upstream licenses (GPL-3.0 or MIT). → See also: *Module*, *Governance*.

**Nambu Basis** [QL]: A spinor representation used in `quantum-lattice` for BdG Hamiltonians,
pairing particle and hole degrees of freedom to encode superconducting order parameters and
particle-hole symmetry explicitly. → See also: *Bogoliubov–de Gennes (BdG) Formalism*,
*Superconductivity (Unconventional)*.

**Non-Collinear Magnetism** [QL]: A magnetic configuration in which spin orientations are neither
fully parallel nor fully anti-parallel, supported by `quantum-lattice` through its full
treatment of spin-orbit coupling and general spin texture. → See also: *Spin-Orbit Coupling*.

**Ontological Record** [ALL] [META]: The authoritative canonical description of a module's
conceptual territory, triadic role, and integration contract within TriadicFrameworks. Each
module JSON and associated documentation in this directory functions as an ontological record.
The directory as a whole is the canonical ontological registry for the quantum-theoretic cluster.
→ See also: *Module*, *Module JSON*.

**Operator** [QB] [QL]: A matrix-valued object acting on the Hilbert space or single-particle
state space. In `quantum_basis`, operators are defined by the user in terms of matrix
representations of elementary degrees of freedom and used to construct the Hamiltonian. In
`quantum-lattice`, operators appear as Hamiltonian terms encoding hopping, coupling, and
symmetry-breaking fields. → See also: *Hamiltonian*, *State-Space Primitive*.

**Partial Order** [QL] [META]: A binary relation ≤ on the set of quantum states that is
reflexive, antisymmetric, and transitive, forming the structural backbone of the lattice as
implemented in `quantum-lattice`. The partial order, together with join/meet operations,
defines the lattice topology that `LattiQ` translates into canonical interface types.
→ See also: *Join / Meet Structure*, *Lattice Topology*.

**Post-Quantum Cryptography** [LQ]: The domain of cryptographic algorithms designed to resist
attacks by quantum computers. `LattiQ`'s primary application target — the Shortest Vector
Problem — is a cornerstone hardness assumption in post-quantum cryptographic schemes. The
module thus situates the quantum-theoretic cluster at the intersection of quantum simulation
and cryptographic security research. → See also: *Shortest Vector Problem*.

**Primitive (Layer I)** [QB] [META]: The first and foundational layer of a triadic cluster,
responsible for defining the mathematical substrate and state-space vocabulary from which all
higher layers are constructed. `quantum_basis` occupies Layer I in this cluster. Primitives
without structure are unordered — mathematically present but operationally inert.
→ See also: *Dependency Terminus*, *Foundation Layer*, *quantum_basis*.

**Quantum-Theoretic Primitive Cluster** [ALL] [META]: The formal TriadicFrameworks designation
for the collective `{quantum_basis, quantum-lattice, LattiQ}` as a closed functional arc. As a
primitive cluster, it provides the quantum-theoretic grounding for the broader canon; no other
cluster within TriadicFrameworks is authorized to define independent quantum ontology without
grounding through this cluster's `LattiQ` interface. → See also: *Cluster*, *Downward Grounding*,
*Upward Composition*.

**Quantum Hall Edge State** [QL]: A conducting state localized at the boundary of a topological
insulator or quantum Hall system, arising from bulk-boundary correspondence. `quantum-lattice`
computes edge states as part of its topological invariant and band structure machinery.
→ See also: *Chern Number*, *Landau Level*, *Topological Invariant*.

**Quantum Ontology** [QB] [META]: The set of ontological commitments — what kinds of objects
exist, what their properties are, and what operations on them are valid — established by the
formal postulates of `quantum_basis`. Quantum ontology is the canon's source of truth for all
quantum-theoretic reasoning within TriadicFrameworks. → See also: *Formal Postulate*,
*Canonical Unit Type*.

**quantum_basis** [QB]: The Layer I — Primitive module of this triadic cluster. A C++ library
for constructing the many-body Hilbert-space basis for arbitrary condensed-matter lattice
models. Supports any combination of bosonic and fermionic degrees of freedom; eigensolvers
include Lanczos and FEAST; spectral access via KPM; sparse algebra backed by Intel MKL and
ARPACK-NG. Upstream: `wztzjhn/quantum_basis`. Author: Zhentao Wang. License: GPL-3.0.
→ See also: *Exact Diagonalization*, *Foundation Layer*, *Primitive (Layer I)*.

**quantum-lattice** [QL]: The Layer II — Structure module of this triadic cluster. A Python
(+ Fortran kernel) toolkit for designing and solving single-particle and mean-field
Hamiltonians on arbitrary lattice geometries. Capabilities include non-collinear magnetism,
spin-orbit coupling, unconventional superconductivity, topological invariants, Green's functions,
Landau levels, and an interactive PyQt GUI. Upstream: `joselado/quantum-lattice`.
Author: Jose Lado. License: GPL-3.0. → See also: *Hamiltonian*, *Simulation Layer*,
*Structure (Layer II)*.

**Rank** [LQ]: A configurable hyperparameter in `LattiQ` controlling the truncation or
approximation rank of the SVP encoding, affecting circuit depth and solution accuracy on
near-term quantum hardware. → See also: *Shortest Vector Problem*, *LattiQ*.

**Recursive Method** [QL]: A numerical technique used in `quantum-lattice` for computing
Green's functions and local density of states in semi-infinite systems, enabling the simulation
of surface and interface physics without modeling a full finite slab. → See also:
*Green's Function*, *Local Density of States*.

**Simulation Layer** [QL] [META]: The TriadicFrameworks designation for `quantum-lattice` in its
role as the primary Hamiltonian factory of the cluster. The Simulation Layer generates
phenomenological models that feed both the ED benchmarking engine (`quantum_basis`) and the
variational quantum optimizer (`LattiQ`). → See also: *Hamiltonian*, *Structure (Layer II)*,
*quantum-lattice*.

**Shortest Vector Problem (SVP)** [LQ]: The computational problem of finding the shortest
non-zero vector in a given lattice. SVP is the primary application target of `LattiQ`, which
encodes it as an Ising spin Hamiltonian and solves it via VQE or QAOA. SVP hardness underlies
many post-quantum cryptographic security proofs. → See also: *Ising Spin Hamiltonian*,
*Post-Quantum Cryptography*, *VQE*, *QAOA*.

**Simulation Layer** → See *quantum-lattice*.

**Sparse Matrix Algebra** [QB]: The set of numerical operations on matrices with predominantly
zero entries, used by `quantum_basis` to represent and manipulate large Hamiltonians
efficiently. Backed by Intel MKL and ARPACK-NG. → See also: *Hamiltonian*, *Intel MKL*,
*ARPACK-NG*.

**Spectral Function** [QB] [QL]: A frequency-domain quantity characterizing how a quantum system
responds to perturbations at each energy. In `quantum_basis`, the spectral function is computed
via KPM. In `quantum-lattice`, it is accessible through momentum-resolved Green's functions.
Spectral functions from the ED layer serve as high-fidelity benchmarks for the variational
layer. → See also: *Kernel Polynomial Method*, *Green's Function*.

**Spin-Orbit Coupling** [QL]: An interaction between a particle's spin and its orbital motion,
implemented in `quantum-lattice` as a Hamiltonian term that mixes spin-up and spin-down
channels. Spin-orbit coupling is essential for modeling topological insulators, anomalous Hall
effects, and non-collinear magnetic textures. → See also: *Non-Collinear Magnetism*,
*Topological Invariant*.

**State-Space Primitive** [QB] [META]: The foundational objects — basis vectors, Hilbert space
representations, and the algebraic rules governing their composition — established by
`quantum_basis`. State-space primitives are the raw material from which all structural and
interface constructs in Layers II and III are built. → See also: *Basis Vector*,
*Canonical Unit Type*, *Hilbert Space*.

**Structure (Layer II)** [QL] [META]: The second layer of a triadic cluster, responsible for
arranging the primitives of Layer I into topologically coherent relational structures. `quantum-lattice`
occupies Layer II in this cluster. Structure without primitives is form without content —
valid topology over empty space. Layer II is the module most likely to evolve as theoretical
refinement occurs, because structure is where theoretical maturation lives. → See also:
*Lattice Topology*, *quantum-lattice*, *Simulation Layer*.

**Superconductivity (Unconventional)** [QL]: Superconducting phenomena not explained by
conventional BCS theory — including d-wave, p-wave, and topological superconductors —
modeled in `quantum-lattice` via BdG Hamiltonians with general pairing symmetries.
→ See also: *Bogoliubov–de Gennes (BdG) Formalism*, *Nambu Basis*.

**Superposition Arrangement** [QL] [META]: The structural encoding of quantum superposition
relationships within `quantum-lattice` as explicit first-class objects. Superposition
arrangements are not computed on demand; they are declared as structural elements of the
lattice, making them accessible to `LattiQ` for interface translation. → See also:
*Entanglement Geometry*, *Lattice Topology*.

**Synthesis Module** [LQ] [META]: An alternate designation for the Layer III module (`LattiQ`),
emphasizing its role as the operational synthesis of the cluster's theoretical content into
a composable interface. → See also: *Interface (Layer III)*, *LattiQ*.

**t-J Model** [QB]: A bundled example model in `quantum_basis` describing strongly correlated
electrons with nearest-neighbor hopping (t) and antiferromagnetic exchange (J), relevant to
high-temperature superconductivity. → See also: *Exact Diagonalization*, *Kondo Lattice Model*.

**Tight-Binding Model** [QL]: A single-particle lattice model in which electrons hop between
sites with specified amplitudes, implemented in `quantum-lattice`. Tight-binding models are
the primary phenomenological tool of Layer II, producing band structures and Hamiltonians that
feed into both the ED solver and the VQA optimizer. → See also: *Band Structure*, *Hamiltonian*,
*Mean-Field Theory*.

**Topological Invariant** [QL]: A quantity characterizing the global topology of the quantum
state space of a band structure that cannot change under smooth deformations of the Hamiltonian.
`quantum-lattice` computes Chern numbers and Z₂ invariants. → See also: *Chern Number*,
*Z₂ Invariant*, *Quantum Hall Edge State*.

**Traversal Rule** [QL] [META]: One of the composition rules defined by `quantum-lattice` that
specify how the lattice topology may be navigated — which transitions between states are
permitted and under what conditions. Traversal rules constitute the grammar that `LattiQ`
translates into canonical interface operations. → See also: *Lattice Topology*, *Partial Order*.

**Triadic Dependency Chain** [ALL] [META]: The directed dependency sequence
`quantum_basis` → `quantum-lattice` → `LattiQ` that governs the flow of types, constructs, and
interface contracts within the cluster. Changes anywhere in the chain must be evaluated for
propagation effects toward the chain's output end (`LattiQ`). → See also: *Dependency Terminus*,
*Layer*, *Cluster*.

**Triadic Slot** [ALL] [META]: One of the three designated positions (Layer I, II, or III) that
a module may occupy within a triadic cluster. A triadic slot is a role, not merely a position:
it carries specific responsibilities (primitive definition, structural arrangement, interface
synthesis) and governance implications. New modules must occupy a defined triadic slot; no
module may augment an existing slot. → See also: *Layer*, *Governance*, *Canonical Review*.

**Triadic Unit** [ALL] [META]: A complete, closed cluster of exactly three modules — one per
layer — that together constitute a single coherent functional arc from raw formalism to applied
interface. The `{quantum_basis, quantum-lattice, LattiQ}` set is a triadic unit. A triadic unit
is the minimal composable element in the TriadicFrameworks canon. → See also: *Cluster*,
*Quantum-Theoretic Primitive Cluster*.

**Twisted Bilayer Graphene** [QL]: A lattice system composed of two graphene layers with a
small relative rotation angle, supported by `quantum-lattice` as a superlattice model. At
the magic angle (~1.1°), the system exhibits flat bands and strongly correlated phenomena
accessible via tight-binding Hamiltonians. → See also: *Tight-Binding Model*, *Band Structure*.

**Type Coherence** [ALL] [META]: The property of a triadic cluster in which all modules share
a common type vocabulary — the canonical unit types — without implicit conversion or
re-definition at integration seams. Type coherence is enforced in this cluster at the substrate
level by `quantum_basis`. → See also: *Canonical Unit Type*, *Integration Seam*.

**Upward Composition** [ALL] [META]: One of two integration directions of the quantum-theoretic
cluster within the broader TriadicFrameworks canon. Upward composition means the cluster, via
`LattiQ`'s extension hooks, can be composed with other triadic clusters. Cross-cluster
dependencies are always Layer-III–to–Layer-III bindings. → See also: *Downward Grounding*,
*Extension Hook*, *Compositional Direction*.

**Variational Quantum Algorithm (VQA)** [LQ]: A class of hybrid quantum-classical algorithms in
which a parameterized quantum circuit is optimized by a classical optimizer to minimize an
energy or cost function. `LattiQ` implements VQA via VQE and QAOA as interchangeable solvers
for the SVP encoding. → See also: *VQE*, *QAOA*, *FastVQA*.

**Variational Quantum Eigensolver (VQE)** [LQ]: A VQA that estimates the ground-state energy of
a Hamiltonian by optimizing a parameterized quantum circuit's output expectation value. In
`LattiQ`, VQE is applied to the Ising Hamiltonian encoding of SVP. → See also:
*Quantum Approximate Optimization Algorithm (QAOA)*, *Ising Spin Hamiltonian*, *CVaR*.

**Quantum Approximate Optimization Algorithm (QAOA)** [LQ]: A VQA designed for combinatorial
optimization, alternating between problem and mixer Hamiltonians through p layers of parameterized
unitaries. In `LattiQ`, QAOA is an interchangeable solver with VQE for the Ising-encoded SVP.
→ See also: *VQE*, *Ising Spin Hamiltonian*, *Shortest Vector Problem*.

**Z₂ Invariant** [QL]: A topological invariant taking values in {0, 1}, classifying systems
with time-reversal symmetry into topologically trivial (0) or non-trivial (1) phases. The Z₂
invariant is computed by `quantum-lattice` and is the relevant topological index for
time-reversal-invariant topological insulators. → See also: *Chern Number*, *Topological Invariant*.

---

## Module Reference Summary

| Module | Layer | Role | Key Vocabulary Domain |
|---|---|---|---|
| `quantum_basis` | I — Primitive | Foundation Layer; dependency terminus | Hilbert space, many-body basis, exact diagonalization, canonical unit types, formal postulates |
| `quantum-lattice` | II — Structure | Simulation Layer; Hamiltonian factory | Lattice topology, tight-binding, mean-field, topological invariants, entanglement geometry |
| `LattiQ` | III — Interface | Synthesis Module; public cluster face | VQE, QAOA, SVP, Ising encoding, abstraction boundary, extension hooks |

---

## Cross-Reference Index

| If you are looking for… | Start with… |
|---|---|
| What constitutes a valid quantum object | *Formal Postulate*, *Quantum Ontology*, *Canonical Unit Type* |
| How modules connect to each other | *Integration Seam*, *Triadic Dependency Chain*, *Type Coherence* |
| How the cluster connects to the rest of the canon | *Extension Hook*, *Upward Composition*, *Downward Grounding* |
| Governance and change policy | *Canonical Review*, *Cluster Versioning*, *Triadic Slot*, *Governance* |
| The public interface for external callers | *Interface (Layer III)*, *Abstraction Boundary*, *LattiQ* |
| Quantum computing / VQA terms | *VQE*, *QAOA*, *CVaR*, *Ising Spin Hamiltonian*, *FastVQA* |
| Topological phenomena | *Topological Invariant*, *Chern Number*, *Z₂ Invariant*, *Quantum Hall Edge State* |
| Exact diagonalization pipeline | *Exact Diagonalization*, *Lanczos Method*, *FEAST Eigensolver*, *KPM* |
| The meaning of triadic architecture terms | *Cluster*, *Layer*, *Triadic Unit*, *Triadic Slot*, *Load-Bearing Node* |

---

*This document is maintained as part of the TriadicFrameworks canonical record.*
*It describes vocabulary and conceptual architecture, not implementation.*
*For implementation details, consult each module's own documentation.*

Generated by TriadicFrameworks · `docs/theories/repos/GLOSSARY.md` · 2026-07-13
