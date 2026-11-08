# From Preskill's error correction chapter to readout-limited preparation

An unreliable detector can leave the quantum measurement perfectly sharp while corrupting the classical bit used to correct its byproduct. This bridge explains why protecting that bit costs local quantum resources, first for a distant physical Bell pair and then for a physical toric-code ground state.

The single educational anchor is John Preskill, [*Quantum Information*, Chapter 7, *Quantum Error Correction*, March 2026 author draft](https://www.preskill.caltech.edu/ph219/chap7_26_6A.pdf), linked from the [author's course page](https://www.preskill.caltech.edu/ph219/index.html). The [30-milestone map](MILESTONES.md) organizes this project's understanding targets. The scientific accounts remain authoritative for the [Bell theorem](../science/model.md) and [toric extension](../science/toric_extension.md).

## Edition and source map

The selected source is the 92-page March 2026 Chapter 7 draft, rather than a different edition of the complete lecture notes. The following are section-start locators. Printed page $`p`$ is PDF page $`p+6`$. Some passages in §§7.18.2–7.18.3 are unfinished, and §7.18.4 is a heading. Read the material present; the derivations below and in the scientific accounts supply missing project steps.

| Source section | Printed / PDF page | Role in this project |
|---|---:|---|
| §7.2; §§7.3.2–7.3.3 | 4 / 10; 9 / 15 | Noise, environments, and reference systems; [retained records](#states-records-and-local-channels) |
| §7.7 | 21 / 27 | CSS separation of $`X`$ and $`Z`$ errors; §7.6 supplies classical parity-check background |
| §§7.10.1–7.10.2 | 27 / 33; 30 / 36 | Stabilizers and syndrome extraction |
| §7.10.4 | 33 / 39 | Logical Pauli labels and physical corrections |
| §7.14 | 43 / 49 | Changing operator support with stabilizers |
| §7.18.1; §7.18.3 | 52 / 58; 55 / 61 | Toric checks, strings, and syndrome boundaries |
| §§7.19–7.20 | 60 / 66; 63 / 69 | Geometric background; distinct code-parameter and thermal questions |

Preskill supplies code language and the distinction between physical errors, syndromes, and logical information. The independent BSC interface, operation-depth models, Chernoff and noise-table calculations, blind-region proofs, and matched preparation bounds are supplied here. Research citations are distinct from this one educational anchor; see [related work](../references/RELATED_WORK.md).

## Conventions and physical tasks

All logarithms in this project are natural. $`L`$ is a chain's endpoint separation in the Bell problem and a torus's side length in the toric problem. $`T`$ counts synchronous quantum gate and readout layers on every execution path. Fixed gate range $`r`$, fixed report density $`\nu`$, and fixed quantum memory refer to local spatial resources. Free global classical processing sees public reports only.

| Object | Convention and operational meaning |
|---|---|
| Bell target | $`\lvert\Phi^+\rangle=(\lvert00\rangle+\lvert11\rangle)/\sqrt2`$ |
| Bell fidelity | $`F_{\mathrm B}=\langle\Phi^+\rvert\rho_{AB}\lvert\Phi^+\rangle`$, a squared overlap |
| Toric target | $`F_{\mathrm{TC}}=\mathrm{Tr}(P_{\mathrm{TC}}\rho)`$, weight in the full physical code space |
| Preskill's $`X_s,Z_P`$ | Stars $`A_v`$ and plaquettes $`B_a`$ here |
| Binary syndrome | Check value $`(-1)^{z_v}`$; syndrome zero means check value $`+1`$ |
| Quantum pointer | An orthogonal basis record retained in local quantum memory |
| Public report | $`Y=X\oplus E`$, with independent $`\Pr(E=1)=p`$ |
| Detector exponent | $`D(p)=-\tfrac12\log[4p(1-p)]`$ |

The construction uses only Hermitian $`X`$ and $`Z`$ Pauli operators. Preskill's §7.10.1 convention $`Y=ZX=i\sigma_y`$ is not needed. In the toric problem $`N=2L^2`$ is the number of data qubits; the code has two logical qubits. Neither count is the number of blocks used to protect readout.

## States, records, and local channels

A density operator describes either a pure quantum state or a probabilistic mixture. Discarding a register means taking its partial trace; selecting an outcome means retaining one branch and renormalizing it. These operations have different effects. A local measurement instrument has completely positive maps $`\mathcal I_x`$ whose sum is trace preserving. Its physical outcome $`x`$ can determine the postmeasurement quantum state even when its public report is wrong.

The CPTP representation retaining the outcome is

```math
\rho\longmapsto\sum_x\mathcal I_x(\rho)\otimes|x\rangle\langle x|_R.
```

Selecting register $`R`$ later recovers the desired branch. In a proof, such a retained mathematical register keeps track of postselection; it is not an ideal second readout available to the controller. Preskill's environment/reference-system discussion provides the channel viewpoint. The geometric scheduling and report interface are explicit project assumptions.

A CNOT can map $`|x\rangle|0\rangle`$ to $`|x\rangle|x\rangle`$ for $`x=0,1`$. Applied to a superposition, it produces an entangled state rather than two arbitrary identical unknown states. The construction copies orthogonal pointer alternatives and counts where every resulting register sits.

## A complete Bell-pair example

Put four sites on a line, numbered 0 through 3. Prepare $`|\Phi^+\rangle_{01}|\Phi^+\rangle_{23}`$. Apply CNOT from site 1 to site 2 and then Hadamard at site 1. Measuring sites 1 and 2 in the computational basis produces independent uniform bits $`u,v`$. The conditional endpoint state is, up to a global phase,

```math
|\psi_{u,v}\rangle_{03}
=(I\otimes X^vZ^u)|\Phi^+\rangle.
```

Thus $`u`$ determines the phase byproduct and $`v`$ the bit byproduct. Applying the inverse correction using estimates $`\widehat u,\widehat v`$ succeeds exactly when both estimates are correct. A classical record declaring a correction does not itself transform the physical endpoints.

Suppose each pointer is read nondestructively three times. Every true readout repeats the same bit, but its report receives a fresh BSC flip. Majority has error

```math
e_3(p)=3p^2(1-p)+p^3=3p^2-2p^3.
```

At $`p=0.1`$, this is $`0.028`$. The physically corrected Bell overlap is $`(1-e_3)^2=0.944784`$. A single report per pointer would give $`(1-p)^2=0.81`$. The improvement has cost three readout layers; the pointer qubits remain physical memory throughout. The Bell-link preparation, basis change, and final correction also consume local layers.

This finite example explains the noise and correction, rather than a depth advantage at four sites. Coherent propagation is a competing protocol and must be included when optimizing the general task.

## Spatial copies and repeated readout

For a long chain, first prepare Bell links within blocks of length $`b`$. Joining adjacent links gives two orthogonal boundary pointers. Freed sites in neighboring blocks can hold local copies of each pointer, formed by counted nearest-neighbor CNOT chains. This needs $`O(b)`$ depth and supplies $`\Theta(b)`$ copies per pointer at fixed spatial density. Reading them for $`t`$ layers supplies $`m=\Theta(bt)`$ independent reports.

For $`m`$ reports, use majority with an independent fair coin to break a tie:

```math
e_m(p)=\Pr[\mathrm{Bin}(m,p)\gt m/2]
+\tfrac12\Pr[\mathrm{Bin}(m,p)=m/2]
\le e^{-D(p)m}.
```

The binomial variable counts wrong reports. BSC symmetry and fair ties make the decoding error independent of the true pointer value. Near random guessing, with $`\delta=1-2p`$, one has $`D(p)=\delta^2/2+O(\delta^4)`$. Weak detector bias therefore requires inverse-square additional reports for the same exponent. The coefficient is inherited Chernoff information, not a new quantum effect.

With $`M`$ Bell-link boundaries, the final endpoint correction depends on the XOR of the first pointer family and the XOR of the second. If every pointer has error probability $`e`$, exact physical fidelity is

```math
F_{\mathrm B}
=\frac14\left[1+(1-2e)^M\right]^2.
```

Two wrong estimates within one family can cancel. The construction proof retains that exact parity calculation rather than requiring every raw estimate to be correct. A union bound still gives a convenient sufficient accuracy estimate. [The local construction](../science/construction.md) specifies the full gates, layouts, probabilities, and integer conventions.

## Why an unread strip obstructs Bell delivery

A strip's reports are called blind when they are independent fair coins. Its physical instruments are still present, and its local pointers can still act coherently. A strip wider than $`2rT`$ separates the two retained endpoint histories after all outside outcome registers have been retained.

Fix a complete public history, freezing the controller's choices. Sum true outcomes inside the blind strip. Complete every outside instrument to a CPTP channel that retains its true-outcome register at its creation. Before selecting those registers, the left and right retained backward cones are disjoint. Their states factor on the product input. Selecting outside records then gives positive product endpoint operators; averaging gives a separable endpoint state. Its Bell overlap is at most $`1/2`$.

The order matters. A selected outside branch is trace decreasing and cannot be discarded using trace-preserving cancellation. Conditioning first can create correlations absent from an unconditioned reduced state. The [blind-strip proof](../science/blind_strip.md) supplies the exact argument, including arbitrary public heralding events.

## A common statistical comparison

An adaptive algorithm must be held fixed while its detector law is changed. Presample flips at every potential report address, including unused ones. For each full table, run the same controller and local quantum rules. This defines one map from a classical noise table to the final physical output.

In a strip of width $`O(T)`$, the number of potential reports is $`k=O(T^2)`$. Replace all flips in a chosen strip by fair flips. There are $`M=\Theta(L/T)`$ disjoint candidate strips. Averaging over an unknown location dilutes the distinguishability of that alternative. The exact noise-table second moment is

```math
\chi^2(Q\Vert P)
=\frac{e^{2kD(p)}-1}{M}.
```

This identity follows because disjoint strips use independent flip variables: distinct likelihood ratios have product expectation one, while one strip's second moment is $`e^{2kD(p)}`$. A binary mathematical Bell test cannot distinguish the resulting output laws more reliably than the original noise tables. Relative entropy and second-moment bounds therefore connect high physical fidelity to $`kD(p)`$ and $`\log M`$. The [information proof](../science/information_bound.md) gives the finite inequalities; the [heralding proof](../science/heralding.md) separately accounts for success probability.

The unknown strip and hidden fair-report flags are analysis devices. Revealing them to the controller would change the physical channel.

## The complete one-dimensional law

The circuit attains $`T=O(b+t)`$ with $`m=\Theta(bt)`$ reports per pointer and $`\Theta(L/b)`$ boundaries. The arbitrary-protocol lower proof has $`k=O(T^2)`$ and $`\Theta(L/T)`$ candidate blind strips. Their match, including accuracy, integer partitions and coherent propagation, gives

```math
D(p)\tau^2=\log\frac{L}{\epsilon\tau},
\qquad
T_{\mathrm{opt}}
=\Theta\!\left(\max\{1,\min\{L,\tau\}\}\right).
```

This statement is uniform in $`L\ge2`$, $`0\lt p\lt 1/2`$, and $`0\lt \epsilon\le1/4`$. The same order holds with a fixed positive heralding success requirement, with constants allowed to depend on that requirement. At each fixed $`p`$ and fixed Bell target above $`1/2`$, depth is $`\Theta(\sqrt{\log L})`$.

The microscopic floor prevents a claimed depth below one layer; the linear cap is supplied by a coherent exact preparation. These facts are part of the proof, rather than extrapolations of the intermediate-depth equation. See [the depth law](../science/depth_law.md).

## Toric syndromes and physical ground-space weight

On the two-dimensional torus, stars and plaquettes commute because they share zero or two edges. The product of all stars is identity, so a star syndrome has even total parity. A physical $`Z`$ edge string flips the stars at its boundary and preserves every plaquette. These are the code facts supplied by Preskill §§7.10 and 7.18.

Start all data edges in $`|0\rangle`$. They already have every plaquette and both chosen logical $`Z`$ labels equal to $`+1`$. Coherent star extraction followed by local pointer dephasing creates a mixture of uniformly even star syndromes $`z`$, with a corresponding physical data state $`|\psi_z\rangle`$. Its canonical phase is defined by normalizing $`\Pi_z|0\rangle^{\otimes N}`$, where $`\Pi_z=\prod_v[I+(-1)^{z_v}A_v]/2`$. The pointers are correlated with actual defects. Neither the controller nor a noisy report creates that correlation.

A three-vertex path illustrates the local compression. Suppose consecutive pointers contain $`(1,1,0)`$, and their data stars have the same syndrome. CNOT the first into the second, giving pointers $`(1,0,0)`$. Controlled $`Z`$ on their shared data edge flips both data stars, giving data syndrome $`(0,0,0)`$. Reset the first pointer. All remaining pointers now agree with their data syndromes. If the initial pair were $`(1,0)`$, its parent would retain the defect instead. The operation removes the child's actual defect and carries only the pair's parity forward.

Perform this operation up a height-$`O(b)`$ tree in every $`b`$-scale rectangle. Every nonroot defect vanishes, and only one parity pointer remains per block. All other pointers are zero and can be reused. The discarded raw information stays in inaccessible reset environments; the controller does not have to decode it. This explains why the raw syndrome's extensive entropy is not a lower bound on necessary public information.

## Protected toric root pointers

There are $`B=\lfloor L/b\rfloor^2`$ rectangular blocks. Local fanout spreads each root pointer through its $`a_j\ge b^2`$ freed pointer registers in $`O(b)`$ depth. Repeatable readout for $`t`$ layers supplies $`a_jt`$ reports of that root value, all with fresh independent report flips. This uses exactly two data qubits and one pointer per toric cell; the report density is one per cell per readout layer.

Decode $`B-1`$ roots, infer the last using the known even total parity, compute an edge correction from those public estimates, and physically apply the local $`Z`$ gates in a counted final layer. The physical output is in the ground space precisely when all independently decoded roots were correct:

```math
F_{\mathrm{TC}}
=\prod_{j=1}^{B-1}[1-e_{a_jt}(p)]
\ge1-(B-1)e^{-D(p)b^2t},
\qquad T\le16b+t-4.
```

Even two wrong root estimates leave two residual physical defects. They do not cancel merely because their parity is even. This is the reason the exact toric-overlap formula differs from the Bell parity formula above.

The final correction can depend instantaneously on all public reports because classical communication is free in this model. The operation-depth statement is not a real-time signal-latency estimate. Destructive readout can be implemented with an additional resettable local readout ancilla, changing the sufficient memory constant and layer constants. The stated three-qubit count assumes repeatable QND readout.

## A buffered blind core and the cube-root result

A toric ground state passes the commuting two-loop test

```math
K=\frac{I+A_0}{2}\frac{I+B_0B'_0}{2}.
```

The open strings $`B_0,B'_0`$ have the same endpoints, and the closed $`X`$ loop $`A_0`$ crosses each once. The identities on the test's range give the inherited local braiding obstruction $`\mathrm{Tr}(K\rho)\le16/17`$ for a product-input shallow local channel.

A side-$`32(rT+1)`$ core is placed inside a side-$`36(rT+1)`$ blind block. This extra buffer keeps the core's backward quantum cone disjoint from all retained outside outcome histories and other tested outputs. Retain those outside records **before** selecting them. The local $`16/17`$ trace inequality then survives outside conditioning and can be applied successively across blind cores.

With

```math
M=\left\lfloor\frac{L}{36(rT+1)}\right\rfloor^2,
\qquad k=1296\nu(rT+1)^2T,
```

the hidden truthful/fair decomposition of the BSC gives

```math
F_{\mathrm{TC}}\le\left[1-\frac{(2p)^k}{17}\right]^M.
```

For any fixed $`p\in(0,1/2)`$ and fixed $`F_0\in(0,1)`$, this forces $`T=\Omega((\log L)^{1/3})`$. The independent protected-root construction, taking $`b\asymp t\asymp(\log L)^{1/3}`$, supplies the matching upper bound. Thus the cube-root law is established in this fixed-detector regime. It was not inferred just by replacing a one-dimensional volume with a two-dimensional one.

The [toric extension](../science/toric_extension.md) states the model, finite bounds, ownership, and detailed proof route. A uniformly matched detector/accuracy crossover and a two-dimensional heralded law are not asserted here. The one-dimensional uniform theorem remains available with its original stronger parameter scope.

## What the two tasks share

| Task | Local protected reports | Number of relevant regions | Established match |
|---|---|---|---|
| Physical Bell pair on a line | $`\Theta(T^2)`$ | $`\Theta(L/T)`$ | Uniform detector/accuracy law; fixed-$`p`$ square-root log |
| Physical toric ground space in 2D | $`\Theta(T^3)`$ | $`\Theta(L^2/T^2)`$ | Fixed-$`p`$, fixed positive target cube-root log |

Both require an actual local quantum mechanism, a defined report interface, and the physical corrected state. A classical outcome table, a chosen Pauli frame, a small energy density, or hypothetical perfect recovery describes a different output. The numerical checks in [verification](../verification/README.md) cover finite circuits and probability formulas; the universal converses and asymptotic bounds rest on the analytical proofs. Preskill's chapter supplies the code language, and the primary research sources retain credit for the geometric and statistical ingredients.
