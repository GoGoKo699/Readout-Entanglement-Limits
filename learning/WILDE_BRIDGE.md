# From Wilde's quantum information theory to readout-limited entanglement

Place qubits in a line. Adjacent qubits can interact, and a classical computer can communicate across the line instantly. The task is to prepare a Bell pair between the two ends. Local measurements can help join short entangled links, but every measurement result reaching the computer may be wrong. How much local operation time is needed to deliver a reliable physical Bell pair?

This bridge develops that question from the language of states, instruments, teleportation, and statistical distinguishability in **Mark M. Wilde, *Quantum Information Theory*, second edition (2017)**. It supplies the project-specific geometry, noise comparison, and resource accounting alongside those foundations. The [30-milestone map](MILESTONES.md) gives the common understanding targets; the [scientific model](../science/model.md) and its linked proofs remain authoritative for the theorem.

The [four-qubit example](#four-qubit-example) shows the mechanism before the universal lower bound. The later sections explain why an arbitrary adaptive protocol faces the same resource constraint, even if its circuit looks entirely different. The section map below is selective reference material, not a requirement to finish the book first.

<a id="edition-and-access"></a>
## Edition and access

The selected anchor is the **2017 second edition**, Cambridge University Press, ISBN 9781107176164, DOI [10.1017/9781316809976](https://doi.org/10.1017/9781316809976). Its [publisher record](https://www.cambridge.org/core/books/quantum-information-theory/247A740E156416531AA8CB97DFDAE438) and [edition-specific contents](https://assets.cambridge.org/97811071/76164/toc/9781107176164_toc.pdf) identify the printed section and page references used here.

An accessible author manuscript is [*From Classical to Quantum Shannon Theory*, arXiv:1106.1445v8](https://arxiv.org/abs/1106.1445v8), submitted July 14, 2019; its [PDF](https://arxiv.org/pdf/1106.1445v8) has a July 16, 2019 cover. This is a later draft associated with the selected book. The [current author-hosted PDF](https://www.markwilde.com/qit-notes.pdf) has a December 5, 2021 cover and also differs in pagination. The bridge links these sources without copying the book into the repository.

**Printed page references below mean the 2017 edition. Definition and equation locators explicitly marked “v8” mean the 2019 arXiv draft.** For example, the printed fidelity section starts on page 243, while v8 starts it on page 263. Some equation numbers also change between drafts. The [bibliographic record](../references/RELATED_WORK.md#wilde2017) distinguishes this educational anchor from the project's research antecedents.

<a id="selective-section-map"></a>
## Selective section map

The printed locations in this table are verified against the [publisher's second-edition contents](https://assets.cambridge.org/97811071/76164/toc/9781107176164_toc.pdf). Each row points to the bridge where that material enters the project.

| Printed 2017 sections | Starting pages | Connection here |
|---|---:|---|
| 3.2–3.6; 4.1–4.3 | 54–81; 102–117 | [States, composites, and records](#states-records-and-instruments) |
| 4.4–4.6; 5.2–5.4 | 129–143; 168–180 | [Instruments and retained pointers](#states-records-and-instruments) |
| 6.1–6.2 | 186–188 | [Bell-link fusion](#four-qubit-example) |
| 7.1–7.4, optional | 208–213 | [Coherent processing of pointer information](#local-construction) |
| 9.1–9.3 | 230–253 | [Fidelity and distance conventions](#notation-and-assumptions) |
| 10.5 and 10.7 | 276; 279 | [Classical statistical comparison](#statistical-mixture) |
| 19.2 | 522 | [Separability and the geometric obstruction](#blind-strip) |

The local light-cone argument and the mixture over blinded strips are supplied in this repository. Chapter 11's quantum relative-entropy machinery is optional background: the implemented converse uses the classical log-sum inequality after expressing Bell fidelity as a binary test.

<a id="notation-and-assumptions"></a>
## Notation and assumptions

Three convention choices deserve an explicit translation.

| Quantity | Wilde locator in arXiv v8 | Convention in this project |
|---|---|---|
| Fidelity | Definition 9.2.2, Eq. (9.89); Theorem 9.2.1, Eq. (9.102) | The squared convention agrees directly: $`F=\langle\Phi^+\rvert\rho\lvert\Phi^+\rangle`$. |
| Trace distance | Definition 9.1.2, Eq. (9.21); Lemma 9.1.1, Eq. (9.27) | Wilde calls $`\lVert\rho-\sigma\rVert_1`$ the trace distance. Binary-test probability differences use $`\frac12\lVert\rho-\sigma\rVert_1`$. |
| Logarithms | Convention following Eq. (1.1) | Wilde defaults to base two. The project uses natural logarithms; a relative entropy in bits is multiplied by $`\ln 2`$ to obtain nats. |

These locators are in the [versioned author manuscript](https://arxiv.org/pdf/1106.1445v8). Thus taking an additional square of the project's Bell overlap would change its meaning. Likewise, classical total variation is

```math
\operatorname{TV}(P,Q)=\frac12\sum_e|P(e)-Q(e)|,
```

which equals the half-norm distance of the corresponding diagonal density matrices.

The physical assumptions come from [the project model](../science/model.md), rather than from a general textbook resource model. There are $`L+1`$ sites, so the endpoint separation $`L`$ counts edges. A depth-$`T`$ protocol has at most $`T`$ synchronous gate or readout layers on every branch. The local quantum memory $`q`$, interaction range $`r`$, and maximum number $`\nu`$ of binary report slots per site per layer stay fixed as the chain grows.

The initial quantum state is a product across sites, possibly selected using shared classical randomness. Global classical processing and communication are free. Quantum operations, including the final correction, take layers. Every fresh physical outcome entering the classical controller passes through an independent, unflagged binary symmetric channel:

```math
y=x\oplus e,\qquad \Pr(e=1)=p,\qquad 0<p<\frac12.
```

Here $`x`$ is the physical outcome, $`e`$ an unknown detector flip, and $`y`$ the available report. A true outcome may remain in a local quantum pointer, whose storage and movement obey the quantum rules. No reset flag, timing signal, or other public interface carries an extra perfect copy of $`x`$.

These assumptions explain the resource question. Ideal classical communication can distribute a report immediately. It cannot make that report more accurate without information from additional physical resources. The matching construction has ideal coherent gates and storage, so its depth isolates the remaining cost of readout information.

<a id="states-records-and-instruments"></a>
## States, records, and instruments

A single qubit has basis states $`|0\rangle`$ and $`|1\rangle`$. A density operator describes both pure states and mixtures. For several qubits, a reduced density operator describes the subsystem retained after all other registers are discarded. These distinctions make the target precise:

```math
|\Phi^+\rangle_{AB}
=\frac{|00\rangle+|11\rangle}{\sqrt2},
\qquad
F=\operatorname{Tr}(\Pi_\Phi\rho_{AB}),
\qquad
\Pi_\Phi=|\Phi^+\rangle\langle\Phi^+|.
```

The two-qubit state $`\rho_{AB}`$ is the delivered output after the report-dependent correction. Its fidelity is also the probability of passing the mathematical test with projector $`\Pi_\Phi`$. This test interpretation agrees with Wilde's v8 Definition 9.2.2 and Exercise 9.2.2 in [Section 9.2](https://arxiv.org/pdf/1106.1445v8#page=264). Introducing the test in an argument does not add a nonlocal measurement to the preparation protocol.

A quantum instrument records both a state change and an outcome. Write its two completely positive outcome maps as $`\mathcal I_0,\mathcal I_1`$, with $`\mathcal I_0+\mathcal I_1`$ trace preserving. The local reported instrument in this project is

```math
\mathcal J_p(\rho)
=\sum_{x,y=0}^1 B_p(y|x)\,
  \mathcal I_x(\rho)\otimes|y\rangle\langle y|_Y,
\qquad
B_p(y|x)=
\begin{cases}
1-p,&y=x,\\
p,&y\ne x.
\end{cases}
```

The controller sees $`Y`$. The quantum output of $`\mathcal I_x`$ can include a local pointer. This distinction is an application of the instrument and coherent-record language in Wilde's [v8 Sections 5.3–5.4, Eqs. (5.79)–(5.90)](https://arxiv.org/pdf/1106.1445v8#page=198).

For example, a controlled operation can correlate a qubit with a fresh pointer:

```math
\alpha|0\rangle|0\rangle
+\beta|1\rangle|0\rangle
\longmapsto
\alpha|0\rangle|0\rangle
+\beta|1\rangle|1\rangle.
```

Before the pointer is read, this can still be a coherent joint state. It is not two copies of the arbitrary state $`\alpha|0\rangle+\beta|1\rangle`$. What can be copied perfectly is the orthogonal basis label. The construction uses that label to obtain many noisy observations of one eventual measurement outcome.

If the public report is completely uninformative, its value carries no evidence about $`x`$. For each fixed reported value, summing the physical outcomes gives a multiple of $`\mathcal I_0+\mathcal I_1`$. The physical quantum action remains a channel, including any local pointer it leaves behind. This observation will be the starting point of the blind-strip proof.

This material supports [M01–M07](MILESTONES.md#m01); the distinction between public and coherent records continues through [M09](MILESTONES.md#m09) and [M14](MILESTONES.md#m14).

<a id="four-qubit-example"></a>
## A complete four-qubit example

Take four sites $`0,1,2,3`$, initially in $`|0000\rangle`$. The output qubits are at sites $`0`$ and $`3`$, so $`L=3`$. Use two blocks of length $`b=2`$, giving $`K=2`$ blocks and one fusion boundary. Each boundary pointer is read $`t=3`$ times, with independent report-flip probability $`p=1/10`$.

The circuit follows the convention of [the construction](../science/construction.md): a parallel one-qubit layer costs one, a parallel nearest-neighbor two-qubit layer costs one, and repeated readout is quantum nondemolition (QND) Z readout.

| Layer | Physical operation | Result or purpose |
|---|---|---|
| 1 | Hadamard on sites 0 and 2 | Start the two block Bell pairs. |
| 2 | CNOT $`0\to1`$ and CNOT $`2\to3`$ | Prepare $`\lvert\Phi^+\rangle_{01}\lvert\Phi^+\rangle_{23}`$. |
| 3 | CNOT $`1\to2`$ | Start the boundary Bell-basis decoder. |
| 4 | Hadamard on site 1 | Make its two Bell bits readable in the Z basis. |
| 5–7 | Z readout of sites 1 and 2 | Obtain three independently corrupted reports of each bit. |
| 8 | A report-selected Pauli on site 3 | Apply the endpoint correction. |

There are no outward SWAPs or extra pointer copies when $`b=2`$. The general count specializes to

```math
T=b+t+3=8,
\qquad
m=\frac{bt}{2}=3
```

reports per pointer.

Let $`u`$ be the physical Z outcome at site 1 after its Hadamard, and $`v`$ the outcome at site 2. The state after the boundary decoder can be written, with the middle and endpoint registers grouped, as

```math
|\Psi\rangle
=\frac12\sum_{u,v=0}^1
|u\rangle_1|v\rangle_2
\otimes(I\otimes X^vZ^u)|\Phi^+\rangle_{03}.
```

Thus all four outcome pairs have probability $`1/4`$. Conditioned on the true pair, the endpoints already form a Bell state. The problem is to identify its Pauli label accurately. The first physical readout fixes each pointer's basis value; QND repetition observes that same value again, with a fresh flip on every public report.

Let $`\widehat u,\widehat v`$ be the two majority decisions. Apply $`Z^{\widehat u}X^{\widehat v}`$ to site 3. Up to an irrelevant phase, the remaining endpoint Pauli is

```math
X^{v\oplus\widehat v}Z^{u\oplus\widehat u}.
```

For three reports, majority fails when two or three detector flips occur:

```math
e_3(p)=3p^2(1-p)+p^3,
\qquad
e_3(1/10)=\frac7{250}.
```

The two decisions use independent flips. They therefore give the following **physical output mixture**:

| Residual Pauli on site 3 | Bell state | Probability |
|---|---|---:|
| $`I`$ | $`\lvert\Phi^+\rangle`$ | $`(243/250)^2=59049/62500`$ |
| $`Z`$ | $`\lvert\Phi^-\rangle`$ | $`1701/62500`$ |
| $`X`$ | $`\lvert\Psi^+\rangle`$ | $`1701/62500`$ |
| $`XZ`$ | $`\lvert\Psi^-\rangle`$, up to phase | $`49/62500`$ |

The probabilities sum to one, and the target overlap is

```math
F=\left(\frac{243}{250}\right)^2
=0.944784.
```

This small example checks the outcome convention, repeated reports, correction, resource count, and delivered density matrix. It does not demonstrate a depth advantage at four sites. A central Bell pair followed by the two disjoint outward SWAPs gives an exact endpoint Bell pair in three layers. The measurement-assisted advantage is an asymptotic result requiring the accounting below.

The example's one fusion boundary is also distinct from the converse's number of fitting blind strips. At $`L=3,r=1,T=8`$, the latter count is zero. The finite strip inequalities are not applied to this example.

The general mechanics appear in [M15–M18](MILESTONES.md#m15), with the Pauli convention prepared in [M07](MILESTONES.md#m07).

<a id="local-construction"></a>
## Using space and readout time together

The four-qubit circuit gives only temporal repetition. A long chain also supplies nearby qubits that can hold spatial copies of each pointer. The [construction proof](../science/construction.md) shows how to use the same one-qubit-per-site memory for both purposes.

First divide $`n=L+1=Kb`$ sites into even blocks of length $`b`$. In parallel, prepare a Bell pair at each block's center and swap its halves to that block's ends. This takes $`b/2+1`$ layers. Each SWAP leaves a zero state behind, making the block's interior available for the next stage.

The two adjacent qubits at each block boundary undergo the same two-layer Bell decoder as the example. Copy its left pointer inward through the right half of the block on its left, and its right pointer through the left half of the block on its right. These domains are disjoint. A nearest-neighbor CNOT chain takes $`b/2-1`$ layers and gives $`b/2`$ copies of each pointer, counting the original. The outermost qubits are retained as outputs and are never read.

Reading every pointer copy for $`t`$ rounds gives

```math
T=b+t+3,
\qquad
m=\frac{bt}{2},
\qquad
M=K-1.
```

Here $`M`$ counts fusion boundaries. The copies share one physical bit; the detector errors on their reports are independent. This is why their useful report count multiplies space by time.

For one bit, let $`e_m(p)`$ be the majority error, with a fair random decision on an even tie. The construction derives

```math
e_m(p)\le
\left[2\sqrt{p(1-p)}\right]^m
=e^{-D(p)m},
\qquad
D(p)=-\frac12\ln[4p(1-p)].
```

This $`D(p)`$ is a discrimination exponent. In natural-log units it also equals

```math
D_{\mathrm{KL}}\!\left(\operatorname{Ber}(1/2)
\middle\Vert\operatorname{Ber}(p)\right).
```

The detector coefficient and repetition bound are established ingredients, attributed in [the research references](../references/RELATED_WORK.md#danjou2021). Their finite derivation and spatial use are given in [construction.md](../science/construction.md#4-chernoff-estimate).

There are two global Pauli parities. For $`M`$ independent bit-decision errors, one parity is correct with probability $`[1+(1-2e_m)^M]/2`$. The two parity errors are independent, so

```math
F=
\left[\frac{1+(1-2e_m(p))^M}{2}\right]^2,
\qquad
1-F\le2M e^{-D(p)bt/2}.
```

For a fixed available depth, choosing $`b`$ and $`t`$ of comparable size supplies order $`T^2`$ reports to each boundary, while leaving order $`L/T`$ boundaries. Both counts matter. The [arbitrary-length partition](../science/construction.md#5-an-explicit-partition-for-every-chain-length) handles remainders with fixed overhead. Destructive readout can be implemented with a retained pointer and a resettable local readout register, changing the exact schedule constants.

<a id="blind-strip"></a>
## The quantum reduction: why one blind strip is enough

A converse must cover every allowed adaptive protocol. It cannot start by assuming that the competing protocol creates Bell links, repeats individual bits, or uses majority decoding. Its quantum starting point is instead a statement about a region through which quantum information cannot travel quickly enough when its measurement reports reveal nothing.

Take an interior strip of width $`w>2rT`$. Replace every report in the strip by an independent fair coin, leaving the quantum instruments in place. The [blind-strip lemma](../science/blind_strip.md#blind-strip-lemma) proves that the endpoint operator is separable, including after any allowed public success selection.

Separability is the required obstruction. A two-qubit separable state has the form $`\sum_h a_h\rho_A^h\otimes\rho_B^h`$, with $`a_h\ge0`$ and $`\sum_h a_h=1`$. For a product of pure qubit states,

```math
\left|\langle\Phi^+|\bigl(|a\rangle\otimes|b\rangle\bigr)\right|^2
=\frac12|\langle a^*|b\rangle|^2
\le\frac12.
```

Convexity extends the bound to every separable state. Classical correlation between the endpoints therefore remains compatible with the obstruction; an endpoint product state is not required.

The proof joins instrument language to local circuit geometry in four steps.

1. **Fix shared randomness and the public history, then refine the outside outcomes.** Fix the controller's shared randomness so that the quantum input is a product across sites. Together with the reported bits, it determines all adaptive choices. For the argument, also specify the true outcomes of every measurement outside the strip. Keep the true outcomes inside the strip summed. Factor out the outcome-independent fair-coin probabilities of the selected inside reports. The remaining summed quantum maps are CPTP; each unnormalized reported branch is a scalar multiple of such a map.

2. **Retain all outside outcome registers.** An outside outcome that has been selected contributes a trace-decreasing branch map. Removing it as if it were trace preserving would be invalid. Instead, represent its instrument as a channel with a retained outcome register, and postpone selecting that register until the end.

3. **Separate the retained quantum histories.** Keep the left endpoint and all outside-left outcome registers, and do the same on the right. Their backward quantum cones enter the strip by at most $`rT`$ sites from each side. Because $`w>2rT`$, the two histories are disjoint. Every operation outside those histories can be removed under a trace: a trace-preserving map has adjoint satisfying $`\mathcal E^\dagger(I)=I`$.

4. **Select and average positive branches.** The product input factors across the two disjoint histories. Selecting the retained outside outcomes gives a positive product endpoint operator for each refined history. Summing histories and averaging over shared randomness, or keeping a publicly chosen subset, gives a separable operator.

Global feedforward is included: both local factors may depend on the same complete public history. It determines which operations occur but supplies no quantum interaction between the disjoint histories. A coherent inside pointer is also included, since it is a local quantum system with the same propagation limit.

The outside registers introduced in the proof are mathematical records of the existing instruments, not additional usable quantum memory or an ideal readout channel. The order of retaining, tracing, and selecting is what makes the argument valid. Wilde supplies the channel and instrument language; the [project proof](../science/blind_strip.md#proof) supplies this geometric specialization, with [Friedman's framework credited](../references/RELATED_WORK.md#friedman2023).

This connects the background on causal cones and adaptive histories to [M19–M21](MILESTONES.md#m19).

<a id="noise-table"></a>
## One adaptive protocol for every noise table

The blind-strip lemma concerns completely uninformative reports. The actual detector has $`p<1/2`$. To compare them without restricting the algorithm, presample a flip at every possible site, layer, and report index, including slots that might remain unused.

For a fixed complete table $`e`$, run the same protocol and average over its quantum outcomes and independent controller randomness. Call its normalized endpoint state $`\rho(e)`$. Adaptivity remains inside this definition: earlier reports select later instruments and locations. The table merely determines how each physical result becomes a report when its address is used.

If a probability distribution $`R`$ is assigned to the table, the average output is

```math
\mathcal P(R)=\sum_e R(e)\rho(e).
```

This is one common classical-to-quantum channel. Its existence does not give the controller access to $`e`$. Changing $`R`$ changes the detector-noise distribution while retaining the same algorithm. This is the content of [M22](MILESTONES.md#m22) and the [common-map argument](../science/information_bound.md#a-common-protocol-map-for-every-readout-table).

Under the actual distribution $`P`$, every table bit is independently Bernoulli($`p`$). For strip $`j`$, define $`Q_j`$ by replacing just its table bits with independent fair bits. A fresh fair flip makes the report independent of the physical outcome, including conditional on the past. Thus $`\mathcal P(Q_j)`$ is separable by the quantum lemma.

<a id="statistical-mixture"></a>
## Hiding the position of the blind strip

At a proposed depth $`T`$, choose

```math
w=2rT+1,
\qquad
k=\nu wT,
\qquad
M=\left\lfloor\frac{L-1}{w}\right\rfloor.
```

Now $`M`$ counts disjoint comparison strips, and $`k`$ counts the potential report slots in one strip. The following argument requires $`M\ge1`$. The construction's boundary count and this strip count have the same order in the intermediate-depth regime, but they are separately defined quantities.

Choose the alternative distribution

```math
Q=\frac1M\sum_{j=1}^M Q_j.
```

Its output is separable because each component output is separable. Its strip label is undisclosed. The comparison is useful because uncertainty about the location of the changed reports can make $`Q`$ close to the actual distribution $`P`$.

Write $`R_j(e)=Q_j(e)/P(e)`$. Since $`0<p<1/2`$, the denominator has full support. The ratio depends only on strip $`j`$, and distinct strips use independent table bits. Consequently,

```math
\mathbb E_P R_j=1,
\qquad
\mathbb E_P R_j^2
=\left[\frac1{4p}+\frac1{4(1-p)}\right]^k
=e^{2kD(p)}.
```

The mixture likelihood is the average of these independent ratios. Its variance is therefore

```math
\chi^2(Q\Vert P)
=\mathbb E_P\left(\frac QP-1\right)^2
=\frac{e^{2kD(p)}-1}{M}.
```

The denominator $`M`$ is the benefit of mixing alternatives with unknown positions. A comparison against only one fixed strip would miss this dependence. The exact calculation is supplied in [the information proof](../science/information_bound.md#exact-chi-square-calculation); mixture and likelihood methods are [established statistical ingredients](../references/RELATED_WORK.md#chen2022).

To turn the calculation into an entanglement constraint, define

```math
f(e)=\operatorname{Tr}[\Pi_\Phi\rho(e)].
```

This number lies in $`[0,1]`$. Under $`P`$, its average is the actual fidelity $`F`$. Under $`Q`$, its average $`F_0`$ is at most $`1/2`$. Therefore

```math
F-\frac12
\le\operatorname{TV}(P,Q)
\le\frac12\sqrt{\chi^2(Q\Vert P)},
```

For $`F>1/2`$, the Bell advantage is positive, so squaring and rearranging gives

```math
2kD(p)\ge\ln\!\left[1+M(2F-1)^2\right].
```

An almost indistinguishable change in the input noise cannot change this output-test probability very much. The quantum lemma guarantees that the alternative test probability is at most one half. These two statements explain the lower bound together. The connection is developed in [M23–M24](MILESTONES.md#m23).

<a id="accuracy-and-heralding"></a>
## Accuracy and public success selection

The total-variation inequality forces enough information to obtain a fidelity separated from $`1/2`$. Accuracy tending to one needs a sharper comparison. Applying classical data processing to the same binary test gives

```math
d(F_0\Vert F)\le D_{\mathrm{KL}}(Q\Vert P),
```

where $`d`$ is relative entropy between two Bernoulli laws. This is the log-sum step described in [the information proof](../science/information_bound.md#reverse-relative-entropy-gives-the-accuracy-dependence), connected to the classical inequalities of Wilde's Sections 10.5 and 10.7.

The first argument is the separable alternative. For $`F_0\le1/2<F`$,

```math
d(F_0\Vert F)
\ge-\frac12\ln[4F(1-F)].
```

In the other direction, Jensen's inequality gives

```math
D_{\mathrm{KL}}(Q\Vert P)
=\mathbb E_Q\ln(Q/P)
\le\ln\mathbb E_Q(Q/P)
=\ln[1+\chi^2(Q\Vert P)].
```

Combining them produces the finite high-accuracy bound

```math
2kD(p)\ge
\ln\!\left\{
1+M\left([4\epsilon(1-\epsilon)]^{-1/2}-1\right)
\right\}
```

whenever the deterministic output has $`F\ge1-\epsilon`$. Its right side grows as the target error decreases. Quantum relative-entropy contraction is not needed: all distributions in this comparison are classical distributions of the noise table and the binary test.

### Why acceptance requires its own argument

Suppose a protocol declares success with probability $`s`$ and has accepted Bell fidelity $`f`$. Acceptance can preferentially select favorable noise, so the original product distribution cannot simply be reused as the noise law of accepted runs.

The [heralding proof](../science/heralding.md) instead keeps unnormalized success and failure probabilities. At a fixed table, let $`h(e)`$ be the probability of acceptance and $`b(e)`$ the probability of acceptance followed by Bell-test failure. Then

```math
0\le b(e)\le h(e)\le1,
\qquad
\mathbb E_P h=s,
\qquad
\mathbb E_P b=s(1-f).
```

For one blind-strip distribution $`Q_j`$, accepted separability gives $`\mathbb E_{Q_j}b\ge\mathbb E_{Q_j}h/2`$. The two likelihood directions have exactly calculable moments:

```math
\mathbb E_{Q_j}(P/Q_j)^2=(1+\delta^2)^k,
\qquad
\mathbb E_P(Q_j/P)^2=e^{2kD(p)},
\qquad \delta=1-2p.
```

Cauchy-Schwarz then controls how much acceptance and accepted failure can change:

```math
\mathbb E_{Q_j}h\ge\frac{s^2}{(1+\delta^2)^k},
\qquad
\mathbb E_{Q_j}b\le e^{kD(p)}\sqrt{s(1-f)}.
```

Combining these estimates with accepted separability yields

```math
1-f\ge
\frac{s^3}{4(1+\delta^2)^{2k}e^{2kD(p)}}
\ge\frac{s^3}{4}e^{-6kD(p)}.
```

The mixture over strips also gives

```math
s(2f-1)\le
\sqrt{\frac{e^{2kD(p)}-1}{M}}.
```

For a fixed success threshold $`s\ge s_0>0`$ and $`f\ge1-\epsilon`$, the two inequalities together retain both the distance logarithm and the accuracy logarithm. They imply the same order of depth as deterministic preparation. If success is allowed to vanish, the displayed factors of $`s`$ must remain in the analysis. This is the distinction addressed by [M25](MILESTONES.md#m25).

<a id="uniform-depth"></a>
## Combining the two spatial counts into the depth law

The converse and construction now meet at the same pair of counts:

| Argument | Reports associated with one region | Number of relevant regions |
|---|---|---|
| Converse | $`k=\Theta(T^2)`$ slots in a strip of width $`\Theta(T)`$ | $`M=\Theta(L/T)`$ disjoint strips |
| Construction | $`m=bt/2=\Theta(T^2)`$ reports when $`b,t=\Theta(T)`$ | $`M=\Theta(L/T)`$ fusion boundaries |

For an optimal depth $`T`$ in the intermediate regime $`1\ll T\ll L`$, with the microscopic floor and coherent cap inactive, the lower bound requires and the upper bound attains, up to constants,

```math
D(p)T^2\asymp\ln\frac{L}{T\epsilon}.
```

The count $`L/T`$ decreases as coherent depth increases. Keeping it inside the logarithm is necessary when the detector quality also varies with length. This is the organizing connection in [M26](MILESTONES.md#m26).

For a uniform statement, define the unique positive solution $`\tau`$ of

```math
D(p)\tau^2=\ln\frac{L}{\epsilon\tau},
\qquad
\mathcal T=\max\{1,\min\{L,\tau\}\}.
```

The [depth theorem](../science/depth_law.md#1-statement) gives

```math
T_{\mathrm{det}}=\Theta(\mathcal T),
\qquad
T_{\mathrm{her}}(\,\cdot\,;s_0)=\Theta_{s_0}(\mathcal T),
```

for $`L\ge2`$, $`0<p<1/2`$, and $`0<\epsilon\le1/4`$. Constants can depend on the fixed microscopic resources and, in the heralded case, $`s_0`$. They are independent of $`L,p,\epsilon`$.

The floor represents a finite operation count. The linear cap is attained by creating a central Bell pair and moving its halves coherently to the outputs, without reading any pointer. The intermediate equation must not be extrapolated past those regimes. Integer partitions and both caps are handled explicitly in [the uniform proof](../science/depth_law.md).

An equivalent expression uses the principal Lambert W function, defined by $`W_0(z)e^{W_0(z)}=z`$:

```math
\tau=
\sqrt{\frac{W_0\!\left(2D(p)(L/\epsilon)^2\right)}{2D(p)}}.
```

The implicit equation already conveys the physical balance. Lambert W merely writes its inverse compactly.

At fixed $`p`$ and fixed target accuracy, the optimum is $`\Theta(\sqrt{\ln L})`$. Close to an uninformative detector,

```math
D(p)=-\frac12\ln(1-\delta^2)
=\frac{\delta^2}{2}+O(\delta^4).
```

Weak bias therefore requires many reports of each physical bit; space and repeated time supply those reports jointly. Along asymptotic families with variable accuracy, the exact crossover is

```math
T_{\mathrm{opt}}=o(L)
\quad\Longleftrightarrow\quad
\frac{D(p)L^2}{\ln(1/\epsilon)}\longrightarrow\infty.
```

At fixed accuracy near $`p=1/2`$, this reduces to $`\delta L\to\infty`$. A concrete reason to retain the uniform formula is the family $`D(p_L)=\ln L/L^2`$: at fixed accuracy its optimum is

```math
\Theta\!\left(
L\sqrt{\frac{\ln\ln L}{\ln L}}
\right)=o(L).
```

Replacing $`L/T`$ by $`L`$ in the intermediate logarithm would miss this sublinear regime. The precise limit arguments appear in [the detector regimes and crossover](../science/depth_law.md#6-detector-and-accuracy-regimes), supporting [M27–M28](MILESTONES.md#m27).

<a id="scope-and-complete-story"></a>
## The complete information-resource explanation

The quantum circuit can create short entangled links quickly. Reading and combining their Pauli information allows those links to become a known physical Bell pair over a long distance. A local pointer can be copied in its basis and read repeatedly, but finite local storage, interaction range, and report density charge space and time for that redundancy.

The converse captures the same limitation without assuming any particular link circuit. A sufficiently wide region with uninformative reports leaves separable endpoints. Mixing over many possible positions of that region gives a separable alternative whose distinguishability is determined by classical detector likelihoods. High Bell fidelity forces the alternative to be distinguishable, while public selection at fixed success probability cannot remove either the distance or accuracy cost.

Wilde supplies the common language for states, instruments, retained records, Bell corrections, and information inequalities. The repository supplies the local geometric reduction, the exact noise-table comparison, the finite construction, and their uniform resource match. Their research attribution is recorded separately in [RELATED_WORK.md](../references/RELATED_WORK.md).

The statement concerns operation depth with free classical communication and a specified unflagged report interface. The attaining circuit uses ideal coherent controls and storage. Correlated report errors, disclosed erasure flags, unrestricted parallel readout, initially shared entanglement, or finite-speed classical control change the model. Extra local quantum noise remains within the converse's channel framework, but achieving the same upper bound with noisy gates requires a separate implementation argument.

The [verification guide](../verification/README.md) checks a finite circuit's layout, pointer values, Pauli correction, and output states. Those checks support the implementation; the universal claims rest on the analytical proofs. [M29](MILESTONES.md#m29) connects this evidence to scope and attribution, and [M30](MILESTONES.md#m30) integrates the complete resource explanation.
