# Readout-limited preparation of a two-dimensional toric code

The same noisy-report interface that limits Bell distribution also constrains preparation of a physical toric-code ground state. The new geometric ingredient is a local two-loop test inside a buffered blind region. The constructive ingredient is local removal of raw syndrome information before protected readout. These steps establish a fixed-detector cube-root logarithmic depth law; dimensional analogy alone would not establish it.

The authoritative detailed proof and compiled construction are in [Topological Communication Cost: noisy measurement reports](https://github.com/GoGoKo699/Topological-Communication-Cost/blob/c9aca22ecd2489da883de8a0c2b91e696f837213/science/noisy-readout.md). This page defines the receiving model, states the consequence, and explains the transfer. The original [one-dimensional Bell theorem](model.md#5-uniform-optimal-depth-theorem), including its uniform detector/accuracy dependence and heralding result, retains its own scope.

## Model and physical target

Use an $`L\times L`$ cell torus, with $`L\ge2`$. Each cell owns its east-going and north-going data edge qubits, so the data size is $`N=2L^2`$. The star $`A_v`$ is the product of $`X`$ on the four edges incident to vertex $`v`$; the plaquette $`B_a`$ is the product of $`Z`$ around face $`a`$. Their common ground-space projector is

```math
P_{\mathrm{TC}}=\prod_v\frac{I+A_v}{2}\prod_a\frac{I+B_a}{2}.
```

The task is to achieve

```math
F_{\mathrm{TC}}=\mathrm{Tr}(P_{\mathrm{TC}}\rho_{\mathrm{out}})\ge F_0,
\qquad 0<F_0<1,
```

where $`F_0`$ is fixed independently of $`L`$. The density operator is the unconditional physical data output after all actual correction gates. Ground-space weight and decoded logical recoverability are different criteria: a state with even a single residual anyon pair has zero weight in this projector despite possible later recoverability.

Import the [report interface](model.md#2-the-report-interface) into this two-dimensional geometry. Input resources are product across cells after fixing shared randomness. Local gate layers have disjoint cell supports of diameter at most a fixed $`r`$. The worst-case depth $`T`$ includes gates, readout, and physical corrections. At most $`\nu`$ binary reports per cell and layer pass through independent unflagged $`\mathrm{BSC}(p)`$ channels, with $`0<p<1/2`$. The controller has free global access to public reports and no ideal access to true outcomes. A retained local quantum pointer obeys the local propagation and memory rules. Ideal CPTP maps, including reset and dephasing, are allowed.

The upper construction uses two data qubits and one pointer qubit per cell, $`q=3`$, nearest-neighbor gates, and one repeatable site-local pointer readout per readout layer. The lower bound permits arbitrary finite local dimensions while retaining fixed range and report density. This extension changes the geometry and target; it does not add a hidden finite-speed constraint on the global classical controller.

## Fixed-detector theorem and finite bounds

**Theorem.** For every fixed $`p\in(0,1/2)`$, $`F_0\in(0,1)`$, fixed gate range and report density, the minimum deterministic preparation depth satisfies

```math
T_{\mathrm{TC}}(L,p,F_0)
=\Theta_{p,F_0}\!\left((\log L)^{1/3}\right)
\qquad (L\longrightarrow\infty),
```

when the available local operations include the $`q=3`$ construction above. Constants may also depend on the fixed microscopic conventions. The upper bound prepares a specified pure toric ground state whenever its root estimates are correct. The lower bound concerns the entire ground space and makes no assumption about the competing protocol's syndrome representation or decoder.

For a finite converse, put

```math
R=rT,\quad s=R+1,\quad
M=\left\lfloor\frac{L}{36s}\right\rfloor^2,
\qquad k=1296\nu s^2T.
```

Every allowed protocol obeys

```math
F_{\mathrm{TC}}
\le\left[1-\frac{(2p)^k}{17}\right]^M
\le\exp\!\left[-\frac{M(2p)^k}{17}\right].
```

If $`M=0`$, this particular estimate gives $`F_{\mathrm{TC}}\le1`$. The factor $`k=O(T^3)`$ counts every potential report slot in one buffered two-dimensional block, including unused slots. It is not a claim that an arbitrary protocol produces or decodes a syndrome bit at every slot.

For the upper bound, partition the torus into $`B=\lfloor L/b\rfloor^2`$ rectangles with side lengths in $`[b,2b-1]`$, where $`1\le b\le L`$. Let $`a_j`$ be rectangle $`j`$'s number of cells. With $`t\ge1`$ readout layers, the compiled circuit has

```math
T\le16b+t-4,\qquad
1-F_{\mathrm{TC}}
\le(B-1)\exp[-D(p)b^2t],
\qquad
D(p)=-\frac12\log[4p(1-p)].
```

Choosing $`t=b`$ and $`b`$ proportional to $`(\log L)^{1/3}`$ gives any fixed $`F_0<1`$. Together with the finite converse, this proves the displayed fixed-detector theorem. For a single rectangle, all defects are removed locally, its parity is known to be even, and exact preparation requires no noisy report.

The finite inequalities retain useful detector and accuracy information. The fixed-detector theorem does **not** assert a uniformly matched $`p,\epsilon,L`$ crossover, a two-dimensional heralded theorem, or an analogous law with faulty data gates or storage. Those statements require their own bounds.

## Buffered blindness and outside records

In an inherited side-$`32s`$ toric braiding patch, let $`A_0`$ be a contractible closed $`X`$ loop and let $`B_0,B'_0`$ be alternative open $`Z`$ strings with the same endpoints. The strings differ by a contractible plaquette product; $`A_0`$ anticommutes with each open string. The two commuting loop constraints define

```math
K=\frac{I+A_0}{2}\frac{I+B_0B'_0}{2},
\qquad P_{\mathrm{TC}}\preceq K.
```

On the range of $`K`$, the identities $`A_0=+1`$ and $`B_0=B'_0`$ supply exactly the local algebra used in [the inherited braiding obstruction](https://github.com/GoGoKo699/Topological-Communication-Cost/blob/47e2a2632a939c96546b199b3ff08a1cd059f194/science/local-braiding.md). Local dilation and projection onto this range therefore give $`\mathrm{Tr}(K\rho)\le16/17`$ for every product-input local CPTP circuit of depth $`T`$. The test involves contractible loops, rather than a prescribed pair of logical operators around the torus.

Place that core in a side-$`36s`$ block, separated from its complement by more than $`2R`$. Make every public report in the block a fair coin independent of its true outcome. For each fixed complete public history, the local operations are fixed. Sum the true inside outcomes, preserving their local quantum pointer outputs. For every outside instrument, first replace the selected branch by a CPTP instrument retaining its true-outcome register at its creation time. Retain other cores' test outputs too.

Only **after** this completion do disjoint backward quantum cones yield factorization between the core and the retained outside history. Selected outside outcomes and previously selected other-core tests then multiply the core state by a nonnegative scalar. The $`16/17`$ bound survives these selections. It can be applied successively to any collection of blind cores without assuming that the actual adaptive output has independent core marginals.

This is the essential transfer from the [blind-strip proof](blind_strip.md#proof). A mathematical copy of an outside outcome register supplies no extra readout to the physical controller. Selecting outside outcomes first and then canceling their trace-decreasing maps as though they were trace preserving would be invalid.

Finally, write each BSC as a hidden mixture of a truthful report with probability $`1-2p`$ and an independent fair report with probability $`2p`$. A whole padded block is blind with probability $`(2p)^k`$. These events are independent across disjoint blocks. Conditional on their hidden pattern, every blind core contributes a factor $`16/17`$ to the ground-space test. Averaging gives the finite converse above. The mixture flags remain inaccessible to the controller.

## Compression before noisy reporting

Initially put every data edge in $`|0\rangle`$. Coherently extract the commuting star syndrome into one local pointer per vertex, then dephase those pointers locally without a public outcome. This gives a classical-quantum mixture over uniformly even syndromes $`z`$:

```math
2^{-(L^2-1)}\sum_{z:\,\oplus_v z_v=0}
|\psi_z\rangle\langle\psi_z|\otimes|z\rangle\langle z|.
```

Use the canonical phase convention

```math
\Pi_z=\prod_v\frac{I+(-1)^{z_v}A_v}{2},
\qquad
|\psi_z\rangle=\frac{\Pi_z|0\rangle^{\otimes N}}
{\|\Pi_z|0\rangle^{\otimes N}\|}.
```

For every even syndrome this normalized state has star syndrome $`z`$, all plaquettes $`+1`$, and both selected logical $`Z`$ labels $`+1`$. All nonzero branch norms coincide. Since $`Z(E)|0\rangle^{\otimes N}=|0\rangle^{\otimes N}`$, any physical edge set $`E`$ satisfies the exact ket identity

```math
Z(E)|\psi_z\rangle=|\psi_{z\oplus\partial E}\rangle.
```

Choose a rooted tree of height $`O(b)`$ within each rectangle. For adjacent child and parent vertices, CNOT the child pointer into the parent pointer, apply $`Z`$ on their shared data edge controlled by the child pointer, then reset the child pointer. These are counted local quantum operations. They set the child's actual data syndrome to zero and update the parent's actual syndrome and pointer to their XOR. Repetition removes every nonroot defect. Only the block parity remains at its root, and all nonroot pointer registers are free for reuse.

Thus the controller need not learn the $`L^2-1`$ raw syndrome bits. Their locally removed information goes into inaccessible reset environments. Reading the raw syndrome once through noisy reports and XOR-compressing those reports would not maintain the pointer/data invariant.

## Protected pointers and the actual corrected output

Copy each remaining orthogonal root pointer along local row and column trees into the freed pointer registers in its rectangle. This costs $`O(b)`$ layers, uses one pointer per cell, and gives $`a_j`$ copies of the same root value. Repeated QND readout for $`t`$ layers supplies $`a_jt`$ independent noisy reports. The measured basis alternatives can be copied; arbitrary unknown quantum states are not being cloned.

Decode $`B-1`$ root bits by majority with independent fair tie breaking. Infer the last from known even total parity. Let

```math
e_m(p)=\Pr[\mathrm{Bin}(m,p)>m/2]
+\tfrac12\Pr[\mathrm{Bin}(m,p)=m/2].
```

Use free global processing of those public estimates to compute an edge set whose boundary is the estimated root syndrome. Apply its $`Z`$ gates physically in one final counted local layer. The residual physical star syndrome is the true root vector XOR its estimate. Consequently,

```math
F_{\mathrm{TC}}
=\prod_{j=1}^{B-1}[1-e_{a_jt}(p)].
```

Every nonzero independent root-error pattern fails the ground-space test, including patterns with an even number of wrong roots. This differs from Bell distribution, where some byproduct errors cancel in a final parity. The formula is averaged over all initial quantum outcomes and all report errors; it uses neither postselection nor a nominal frame correction.

## Ownership and limits of the connection

Topological Communication Cost supplies the physical toric target, the local braiding geometry, local-channel obstruction, and block-sweep/coarse-tree preparation framework. Its geometric obstruction is credited to Li, Lee and Yoshida. Readout Entanglement Limits supplies the unflagged report interface, outside-register retention, noise-table comparison, and spatial plus temporal pointer-readout method. The two-loop buffered transfer and the constant-memory protected-root construction are the shared new consequence. The detailed proof has one authoritative home in the linked toric account.

This theorem does not transfer the toric model's charged-communication frontier into a free classical controller model unchanged. It also does not turn a logical-memory or single-shot recovery threshold into a physical-ground-space preparation theorem. The [related-work comparison](../references/RELATED_WORK.md#toric-report-noise-extension) separates these operational tasks.
