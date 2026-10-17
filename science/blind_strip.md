# A blind strip makes the endpoint state separable

A region whose measurement reports contain no information about the physical outcomes cannot support an arbitrarily fast measurement-assisted connection across the chain. The statement below makes this obstruction precise for adaptive circuits. The proof retains all relevant outside measurement records before removing trace-preserving operations.

The [model](model.md) fixes the physical assumptions. This page proves the geometric step used in the [information bound](information_bound.md) and its [heralded extension](heralding.md). The treatment of measurement-assisted propagation is related to the local-circuit bounds of [Friedman et al.](../references/RELATED_WORK.md#friedman2023); the separability statement needed here is proved in full below.

## Circuit and readout conventions

Sites are $`0,1,\ldots,L`$, and the designated output qubits $`A`$ and $`B`$ are at sites $`0`$ and $`L`$. The input is a product across sites. Shared classical randomness is allowed: after fixing its value, the quantum input must still be a product across sites.

There are $`T`$ quantum layers. Each layer consists of operations on disjoint sets of physical quantum systems, and every operation has spatial diameter at most $`r`$. Thus a backward quantum causal cone expands by at most $`r`$ sites per layer. Operations may be unitary or completely positive and trace preserving (CPTP). Their environments cannot supply initially shared entanglement. Any environment or coherent record retained for later use is part of the physical local memory and obeys the same density and range constraints.

Readout is site-local. A binary instrument at a site has completely positive maps $`\mathcal I_0`$ and $`\mathcal I_1`$, with $`\mathcal I_0+\mathcal I_1`$ trace preserving. Ideal projective measurement is the principal example. The instrument can leave a local quantum record. Every classical use of its fresh outcome passes through the prescribed detector interface. There are at most $`\nu`$ potential binary readout slots per site per layer, where $`\nu`$ is fixed.

The classical controller can use all previously reported outcomes, together with shared randomness, to choose operations anywhere in the chain. Its processing and communication are unrestricted. It cannot directly use an unreported physical outcome. Quantum control through a retained local record is allowed and is included in the local quantum circuit.

An idle slot contributes no instrument. Padding the schedule with idle slots gives a fixed set of potential readout addresses even when the protocol chooses its measurements adaptively or stops early.

## Blind-strip lemma

Let

```math
I=\{u+1,\ldots,u+w\}\subseteq\{1,\ldots,L-1\},
\qquad w>2rT.
```

Suppose every report produced at a site in $`I`$ is an independent fair coin, independent of the physical measurement outcome and of the preceding history. Outside $`I`$, the readout can follow the original binary symmetric channel. Fixed outside flip bits, or any fixed mixture of perfect and independent-coin reports, are also allowed.

**Lemma.** For every heralding event determined by the allowed public information, the corresponding unnormalized endpoint operator is separable. In particular, the unconditional endpoint state is separable, and every success-conditioned endpoint state with nonzero success probability has Bell fidelity at most $`1/2`$.

Here an unnormalized operator is separable if it belongs to the cone

```math
\mathrm{Sep}_+(A:B)
=\left\{\sum_j X_j\otimes Y_j:\ X_j\ge0,\ Y_j\ge0\right\}.
```

The lemma does not assert that the two endpoints are statistically independent after the public record is discarded. They may share classical correlations.

## Proof

### 1. Refine the public record without selecting an inside outcome

Fix the controller's shared randomness. Decompose the output by the complete public transcript, including the reported bits, adaptive measurement locations, and any heralding decision. Further refine each transcript by the true physical outcomes of all measurements **outside** $`I`$. Denote this refined record by $`h`$.

All gate choices and instrument choices are now fixed. A record inconsistent with the controller's rules contributes zero. A consistent record determines a nonadaptive local quantum circuit, multiplied by a nonnegative scalar $`\gamma_h`$ containing the relevant readout probabilities and the probability of the shared randomness.

At an outside measurement, its selected true outcome $`x`$ contributes the branch map $`\mathcal I_x`$. The probability of its reported value, conditional on $`x`$, is a scalar included in $`\gamma_h`$.

At an inside measurement, the probability of the selected public report is $`1/2`$ for either true outcome. The true outcome is not included in $`h`$. Consequently its quantum contribution is

```math
\frac12\sum_{x=0}^1\mathcal I_x,
```

where the factor $`1/2`$ can be absorbed into $`\gamma_h`$. The remaining map is CPTP. This replacement is valid throughout the adaptive circuit because every later classical choice is fixed by the public record. A later quantum operation may still respond coherently to a local record left by the instrument; that record is part of the instrument's output, so the summed map retains this physical dependence.

The resulting branch contains trace-decreasing maps outside the strip. They cannot be discarded by a trace-preserving cancellation argument. The next step retains their outcome registers explicitly.

### 2. Retain every outside outcome register

For each outside instrument in the fixed circuit, replace its selected map by the CPTP map

```math
\mathcal C(\rho)
=\sum_{x=0}^1\mathcal I_x(\rho)\otimes|x\rangle\langle x|_R.
```

The register $`R`$ is a mathematical copy of the classical outcome. Retain it until the end, and do not use it for any additional control. Projecting it onto the selected value in $`h`$ recovers the original branch map exactly. Introducing this register does not provide an additional physical readout interface to the controller.

Let $`R_{\mathrm L}`$ collect all such registers originating at sites at most $`u`$, and let $`R_{\mathrm R}`$ collect those originating at sites at least $`u+w+1`$. Retain $`A,R_{\mathrm L},B,R_{\mathrm R}`$ and trace out every other final quantum system. Before selecting the values of the retained registers, this construction is a nonadaptive depth-$`T`$ CPTP circuit. Call its output

```math
\Xi^h_{A R_{\mathrm L} B R_{\mathrm R}}.
```

The superscript indicates that the local operation choices were fixed using $`h`$. It does not mean the retained outside outcomes have already been selected.

### 3. The two retained quantum histories are disjoint

Start backward quantum causal cones from $`A`$ and every register in $`R_{\mathrm L}`$. A register is an output at its measurement time; retaining it adds no later quantum interaction. At a time slice $`t`$, every site in the union of these cones lies at or to the left of

```math
u+r(T-t).
```

The union of the cones from $`B`$ and $`R_{\mathrm R}`$ lies at or to the right of

```math
u+w+1-r(T-t).
```

These unions are disjoint because $`w>2rT`$. A quantum operation cannot connect the two retained histories: if it had an output in each, its inputs would belong to both backward cones.

To remove the rest of the circuit, work backward from the traced outputs. Every operation not in a retained backward cone is trace preserving. Its adjoint therefore sends the identity to the identity,

```math
\mathcal E^\dagger(\mathbf 1)=\mathbf 1.
```

Such an operation cancels when all its outputs are traced. Repeating this cancellation removes the unretained part of the circuit. In particular, no selected outside measurement has been canceled: all outside outcome registers were retained before this step. Inside measurements are nonselective CPTP maps and can be canceled when they lie outside the retained cones.

The remaining circuit has two disjoint components, with disjoint sets of input sites. The initial state factors across those sets. Hence

```math
\Xi^h_{A R_{\mathrm L} B R_{\mathrm R}}
=\Xi^h_{A R_{\mathrm L}}\otimes\Xi^h_{B R_{\mathrm R}}.
```

Equivalently, this equality follows by propagating product observables backward through the two disjoint cones. Their expectation values factor on the product input, and product observables span the retained operator space.

### 4. Select the refined record and sum positive product branches

Let $`P_{h,\mathrm L}`$ and $`P_{h,\mathrm R}`$ be the projectors selecting the outside outcome registers specified by $`h`$. The endpoint contribution of this refined record is

```math
\begin{aligned}
\Omega_{AB}(h)
&=\gamma_h\,
\mathrm{Tr}_{R_{\mathrm L}}
\!\left[(\mathbf 1_A\otimes P_{h,\mathrm L})\Xi^h_{A R_{\mathrm L}}\right]
\otimes
\mathrm{Tr}_{R_{\mathrm R}}
\!\left[(\mathbf 1_B\otimes P_{h,\mathrm R})\Xi^h_{B R_{\mathrm R}}\right]\\
&=\gamma_h\,\Omega_A(h)\otimes\Omega_B(h),
\end{aligned}
```

with positive factors. The positivity is also evident by placing each register projector on both sides before taking the partial trace.

The two factors may both depend on the entire refined record. This is where unrestricted global classical feedforward enters: it changes the chosen local maps, but it introduces no quantum edge between the fixed-branch components.

Summing over $`h`$ and averaging over shared randomness gives a positive sum of product endpoint operators. Conditioning on an allowed heralding event selects a subset of these records, or applies nonnegative classical weights to them. The resulting unnormalized operator remains in $`\mathrm{Sep}_+(A:B)`$. This proves the lemma.

## From separability to Bell fidelity

For $`|\Phi^+\rangle=(|00\rangle+|11\rangle)/\sqrt2`$ and positive single-qubit operators $`X,Y`$,

```math
\langle\Phi^+|X\otimes Y|\Phi^+\rangle
=\frac12\mathrm{Tr}(X^{\mathsf T}Y)
\le\frac12\mathrm{Tr}(X)\,\mathrm{Tr}(Y).
```

The inequality follows from $`X^{\mathsf T}\le\mathrm{Tr}(X)\mathbf1`$. Therefore every unnormalized separable operator obeys

```math
\mathrm{Tr}(\Pi_\Phi\Omega_{AB})
\le\frac12\mathrm{Tr}(\Omega_{AB}),
\qquad \Pi_\Phi=|\Phi^+\rangle\langle\Phi^+|.
```

The same bound holds for any fixed Bell state after a local change of basis. Applying it to the accepted branch proves the heralded statement.

## Finite strip count

For integer $`r,T\ge1`$, use

```math
w=2rT+1,
\qquad
k=\nu wT,
\qquad
M=\left\lfloor\frac{L-1}{w}\right\rfloor.
```

The $`L-1`$ interior sites contain $`M`$ disjoint strips of width $`w`$. Padding each strip to $`\nu`$ potential readouts per site per layer gives exactly $`k`$ table positions. A protocol may use fewer positions. Randomizing the entire padded table still makes the strip blind.

The later information bounds require $`M\ge1`$. If no such strip fits, the geometric argument gives no finite inequality of that form; in that regime $`T`$ is already proportional to $`L`$ for fixed $`r`$.

These constants use site-local readout. The proof also covers general **site-local** instruments, because only complete positivity and trace preservation of their sum were used. An instrument whose reported outcome has a larger spatial support changes the location of the retained record's quantum cone. The displayed width and slot count should not be transferred to that model without accounting for its support.

## An elementary bound at fixed detector quality

A BSC with crossover probability $`0<p<1/2`$ admits the representation

```math
Y=
\begin{cases}
X,&\text{with probability }1-2p,\\
C,&\text{with probability }2p,
\end{cases}
```

where $`C`$ is an independent fair coin. The choice of branch is hidden. Presample independent branch choices for all potential readout slots, including idle ones.

A strip is blind whenever all its $`k`$ choices take the independent-coin branch. This event has probability $`q_{\mathrm{blind}}=(2p)^k`$. The corresponding events for disjoint strips are independent. Conditional on at least one blind strip, the endpoint state is separable by the lemma. One can partition that event according to the first blind strip and then average the resulting separable states.

Writing $`F=\mathrm{Tr}(\Pi_\Phi\rho_{AB})`$, it follows that

```math
F\le\frac12+\frac12[1-(2p)^k]^M
\le\frac12+\frac12\exp[-M(2p)^k].
```

The [information bound](information_bound.md) improves the detector-quality dependence by comparing the actual noise with a mixture in which the location of one blind strip is unknown. It uses the original unflagged BSC interface throughout.
