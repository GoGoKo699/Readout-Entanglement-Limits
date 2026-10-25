# A universal depth bound from noisy measurement records

Reliable classical feedback can use a measurement record only when some information about the physical outcome survives. Independent reporting errors contain a component in which the true outcome is completely forgotten. A sufficiently wide region containing only such reports prevents information at its central cut from reaching an accessible outcome port within the available circuit depth. Removing the quantum operations across that cut then leaves the endpoint output unchanged. The resulting circuit uses only local quantum operations and classical communication across the cut, so its endpoint state is separable.

This argument does not assume an entanglement-swapping architecture. It applies to every adaptive protocol in the [model](model.md), including coherent copying, repeated measurements, resets, and arbitrary classical decoding.

The locality ingredient follows the interaction-cut method of [Friedman, Yin, Hong, and Lucas](https://arxiv.org/abs/2206.09929), especially their treatment of adaptive measurements in Sections 4.2 and Supplement 6.5 through 6.7. Rare fully broken cuts also underlie [Choe and König's quantum-bus converse](https://arxiv.org/html/2209.09774v1), Theorem 8.2. The proof here applies these ideas to the fixed readout-only noise model. Because quantum gates are perfect, a single layer of forgotten reports at one spatial cut is insufficient. The separating event covers a corridor whose width grows with circuit depth.

## Finite-size theorem

**Theorem 1.** Consider a protocol of depth $D$ with integer $D\geq1$ on columns $0,1,\ldots,L$, at most $w$ physical qubits per column, and independent binary reporting error $p\in(0,1/2)$. The designated physical output qubits lie in columns $0$ and $L$. Set

```math
b=2D+2,
\qquad
K=\left\lfloor\frac{L-1}{b}\right\rfloor,
\qquad
q=(2p)^{wbD}=(2p)^{2wD(D+1)}.
```

For every success event $S$ with retained endpoint state, its probability and conditional Bell overlap satisfy

```math
P_S(2F_S-1)
\leq(1-q)^K
\leq\exp(-Kq).
```

When $P_S=0$, interpret the left side as zero. For deterministic preparation this gives

```math
F\leq\frac12+\frac12(1-q)^K
\leq\frac12+\frac12\exp\!\left[
-K(2p)^{2wD(D+1)}
\right].
```

If $K=0$, the bound reduces to the trivial inequality $F\leq1$. A depth-zero circuit starts from a state separable across columns, so $F\leq1/2$ directly. The theorem uses the total number of physical rounds, including readouts.

The proof has three parts: an exact refinement of the report-noise instrument, a causal separation lemma for a fixed refinement, and a probability bound on disjoint corridors.

## Refining a noisy report

At any readout, let $\mathcal M_0,\mathcal M_1$ be its ideal binary instrument. The noisy reported-outcome map has the identity

```math
\begin{aligned}
\mathcal I_y
&=(1-p)\mathcal M_y+p\mathcal M_{1-y}\\
&=(1-2p)\mathcal M_y
+p(\mathcal M_0+\mathcal M_1).
\end{aligned}
```

This is implemented by the following exact refinement. Draw a flag $E$ independently of the quantum state, with

```math
\Pr(E=1)=2p,
\qquad
\Pr(E=0)=1-2p.
```

If $E=0$, report the true instrument outcome. If $E=1$, forget the true outcome and report an independent fair bit $R$. Conditional on $E=1$ and the replacement bit, the physical quantum map is the trace-preserving channel

```math
\mathcal T=\mathcal M_0+\mathcal M_1.
```

Averaging over the flag and replacement bit gives $\mathcal I_y$ exactly. The refinement concerns information in the classical report; the measured qubit still undergoes its proper instrument backaction.

### Potential slots and adaptive schedules

Label every possible single-qubit readout slot by its column, physical slot within that column, and round. There are at most $w(L+1)D$ such slots. Pad unused physical slots if necessary, and sample independent flags and replacement bits for the whole array. When a protocol performs a readout, it uses the variables assigned to that physical slot and round. Variables assigned to unused slots have no effect.

This produces the original independent noise law for every adaptive schedule. In the original protocol, the decision to use a slot can depend on earlier reports but cannot depend on the unused independent flag at that slot. Sampling in advance changes neither the joint quantum instrument nor the distribution of the reports.

For the lower bound, grant the controller the entire flag array and replacement-bit array before it starts. This permits more strategies than the original model. The proof below holds even if the controller chooses its instruments, initial separable state, and gate schedule using those arrays. The original protocol is recovered by ignoring the additional information.

Pre-sampling is useful because the event that a whole corridor is erased can refer to every potential slot. Its probability remains a product of independent flag probabilities even when the enhanced controller chooses where to measure. A controller can avoid an individual erased slot; it cannot obtain a truthful report from a corridor in which every potential slot is erased.

## Separation by an erased corridor

**Lemma 2.** Fix the flag array, replacement bits, and independent classical random seed. Let a corridor lying strictly between the endpoint columns consist of

```math
B=\{a,a+1,\ldots,a+2D+1\}.
```

Thus $a\geq1$ and $a+2D+1\leq L-1$. Suppose every potential readout slot in $B$ has flag $E=1$. Let $C$ be the cut between columns $a+D$ and $a+D+1$. Delete every quantum operation whose support crosses $C$, replacing it by the identity on that support and preserving the rest of the adaptive control policy. Then the complete classical–quantum state of the accessible transcript and the two endpoints is unchanged.

Consequently, each unnormalized endpoint state conditioned on an accessible transcript is separable across $A:B$. The same holds after any postselection using that transcript.

### Proof of equality of the output instruments

Keep the flags and replacement bits fixed. An erased readout emits a predetermined classical bit and applies $\mathcal T=\mathcal M_0+\mathcal M_1$ to the physical qubit. Its true outcome is summed out. Every quantum-dependent accessible outcome is therefore produced outside $B$.

Now fix an admissible complete accessible transcript $c$. This fixes every adaptive choice in both the original and modified circuits: at each round, use the same control policy evaluated on the same preceding transcript. The policy is defined on all possible histories, including histories of zero probability. A branch inconsistent with a fixed replacement bit has zero weight and can be omitted.

Let $\mathcal E_c$ be the unnormalized completely positive branch map for the original circuit. At a truthful readout, the local branch map is $\mathcal M_{c_j}$. At an erased readout, it is the sum $\mathcal T$, not either of its individual outcome maps. All other local maps are trace preserving. Let $\widetilde{\mathcal E}_c$ be the corresponding branch map with cut-crossing operations replaced by identities.

For any endpoint operator $O_{AB}$, consider

```math
\mathrm{Tr}\!\left[
O_{AB}\mathrm{Tr}_{(AB)^c}\mathcal E_c(\rho_{\mathrm{in}})
\right]
=\mathrm{Tr}\!\left[
\mathcal E_c^{\dagger}(O_{AB}\otimes I_{(AB)^c})
\rho_{\mathrm{in}}
\right].
```

Propagate the observable backwards through the branch's adjoint local maps. Three facts control its support.

First, the adjoint of a trace-preserving channel is unital. An operation on a region where the observable is the identity cannot introduce support there. This applies to an erased instrument because its true outcome has already been summed out.

Second, a truthful outcome map need not have a unital adjoint. Even when its site carries an identity factor, the adjoint can insert the effect $\mathcal M_{c_j}^{\dagger}(I)$. We therefore include the site of every truthful readout as a possible support seed. All these seeds lie outside $B$.

Third, local operations in one round have disjoint physical supports and connect only equal or adjacent columns. They enlarge previously existing support by at most one column in that round. A single-qubit readout introduces its support seed at that qubit. It creates no additional spatial jump.

It follows that every intermediate backwards observable is supported inside the union of neighborhoods of radius $D$ of the endpoints and all truthful-readout sites in that branch. The two columns adjacent to $C$ are at distance at least $D+1$ from every site outside $B$. Hence neither belongs to this support. At every step, the observable has an identity factor on the support of each cut-crossing operation. Applying that operation's unital adjoint or applying the identity gives the same observable.

Backward induction through all rounds now gives the exact operator equality

```math
\mathcal E_c^{\dagger}(O_{AB}\otimes I_{(AB)^c})
=\widetilde{\mathcal E}_c^{\dagger}(O_{AB}\otimes I_{(AB)^c}).
```

This holds for every $c$ and every $O_{AB}$. Therefore the unnormalized endpoint states agree branch by branch:

```math
\mathrm{Tr}_{(AB)^c}\mathcal E_c(\rho_{\mathrm{in}})
=\mathrm{Tr}_{(AB)^c}\widetilde{\mathcal E}_c(\rho_{\mathrm{in}}).
```

The equality includes each branch probability, obtained by setting $O_{AB}=I_{AB}$. Summing with the classical labels $|c\rangle\langle c|$ proves equality of the full accessible-transcript and endpoint state.

The argument uses unnormalized branches throughout. A scalar identity factor from a fixed classical probability does not enlarge operator support. In particular, fixing a reported replacement bit without conditioning on its sampling coin would give the map $\mathcal T/2$, whose adjoint maps $I$ to $I/2$; the same support conclusion holds. Conditioning on the replacement coins merely removes these scalar factors.

### Why the cut implies separability

In the modified circuit, every remaining quantum operation acts entirely on one side of $C$. The two sides exchange only classical information. The initial state is separable across that cut, including when chosen using the fixed classical arrays. Each branch of such a local-operations-and-classical-communication protocol preserves separability. Tracing out the other physical qubits preserves it as well.

Thus the modified circuit's endpoint state is separable for each accessible transcript. The branchwise equality transfers that conclusion to the original circuit under the fixed erased-corridor flag pattern. Sums over transcripts, including any selected success event, are sums of positive separable operators and remain separable. This proves the lemma.

### Coherent copies and adaptive choices

The lemma permits a measured qubit to retain its post-measurement state and to control later quantum gates. Such use of a hidden outcome propagates through the physical quantum circuit. A copy that affects an accessible outcome or the retained endpoints must lie on a corresponding causal path. The support proof counts every gate on that path. A corridor of width $2D+2$ leaves its central cut outside all those paths.

Global classical feedback can select gates inside the corridor based on observations made outside it. Fixing the accessible transcript fixes these choices. The feedback cannot expose a hidden physical outcome without a later quantum-dependent accessible port, and every such port is included among the support seeds. The proof therefore covers arbitrary adaptive measurement locations and bases, rather than only a fixed measurement pattern.

## Packing independent corridors

Return to the random flag array. Choose the $K$ disjoint corridors

```math
B_j=\{(j-1)b+1,\ldots,jb\},
\qquad j=1,\ldots,K.
```

These corridors lie strictly between columns $0$ and $L$. Each has $wbD$ potential readout slots after padding. Let $A_j$ be the event that all their flags equal one. Then

```math
\Pr(A_j)=(2p)^{wbD}=q.
```

The events $A_j$ are independent because their potential-slot sets are disjoint. This independence concerns the externally sampled arrays, not the adaptively selected set of actual measurements. Thus

```math
\Pr\!\left(\bigcap_{j=1}^{K}A_j^c\right)=(1-q)^K.
```

Whenever at least one $A_j$ occurs, Lemma 2 makes every transcript-conditioned endpoint state separable. Different flag patterns can select different cuts, but the retained bipartition is always the same pair $A:B$. Averaging these conditional states still gives a separable contribution to the endpoint output.

## From separability to a heralded fidelity bound

For normalized single-qubit vectors $|u\rangle,|v\rangle$,

```math
\left|\langle\Phi^+|\bigl(|u\rangle\otimes|v\rangle\bigr)\right|^2
=\frac12|u^{\mathsf T}v|^2
\leq\frac12.
```

By convexity, every positive unnormalized separable two-qubit operator $\tau$ obeys

```math
\mathrm{Tr}(\Phi_{AB}\tau)
\leq\frac12\mathrm{Tr}\tau.
```

Introduce the Hermitian Bell witness

```math
W=2\Phi_{AB}-I_{AB}.
```

Its expectation is nonpositive on separable positive operators, and its largest eigenvalue is one. For any fixed flag pattern with an erased corridor, the success-conditioned unnormalized endpoint state $\tau^S$ is separable, so $\mathrm{Tr}(W\tau^S)\leq0$. For a pattern without an erased corridor,

```math
\mathrm{Tr}(W\tau^S)\leq\mathrm{Tr}\tau^S\leq1.
```

Average over the flags, replacement coins, and any independent classical randomness. This gives

```math
P_S(2F_S-1)
=\mathrm{Tr}(W\tau_{AB}^{S})
\leq\Pr\!\left(\bigcap_{j=1}^{K}A_j^c\right)
=(1-q)^K.
```

Finally, $(1-q)^K\leq e^{-Kq}$. This proves Theorem 1. The success event may depend on all information granted to the enhanced controller, so the bound also holds for success decisions based only on the original noisy reports.

## Consequence for fixed target fidelity

For deterministic preparation, fix $F_0\in(1/2,1)$ and set

```math
\eta=2F_0-1\in(0,1),
\qquad
\alpha=\log\frac1{2p}>0.
```

If $F\geq F_0$ and $K\geq1$, Theorem 1 implies

```math
K\exp[-2w\alpha D(D+1)]\leq-\log\eta,
```

or equivalently,

```math
2w\alpha D(D+1)
\geq\log K-\log(-\log\eta).
```

This is an explicit finite-size necessary condition. To obtain the asymptotic law, hold $p$, $w$, and $F_0$ fixed. If $D\leq c\sqrt{\log L}$, then

```math
K=\Omega\!\left(\frac{L}{\sqrt{\log L}}\right),
\qquad
q\geq L^{-2w\alpha c^2-o(1)}.
```

Choose $c>0$ with $2w\alpha c^2<1$. Then $Kq$ diverges as $L$ grows, so the finite-size theorem forces $F\leq1/2+o(1)$. Such depths cannot reach the fixed target $F_0$. Therefore

```math
D=\Omega_{p,w,F_0}\!\left(\sqrt{\log L}\right).
```

For heralded preparation, the same conclusion holds whenever $P_S\geq s_0$ and $F_S\geq F_0$, with fixed $s_0\in(0,1]$ and $F_0\in(1/2,1)$: replace $\eta$ by $s_0(2F_0-1)$ in the finite-size condition. This is a lower bound even when the success event can exploit the revealed flags.

The [width-one construction](construction.md) reaches every fixed target $F_0\in(1/2,1)$ in $O_{p,F_0}(\sqrt{\log L})$ rounds. Together the two bounds determine the optimal distance scaling for the stated task.

## What is used from earlier converse methods

The proof's local separation step is a finite-depth form of the measurement-assisted locality argument of [Friedman et al.](https://arxiv.org/abs/2206.09929). Its probabilistic use of independently broken regions has a close precedent in [Choe and König](https://arxiv.org/html/2209.09774v1), whose Theorem 8.2 constructs damaging local stochastic quantum faults and obtains a depth–width condition proportional to $\log L$.

Here the faulty resource is the measurement report itself. Perfect quantum gates can still carry information coherently through a site whose reports have been forgotten. The converse therefore suppresses accessible outcome ports over a depth-wide corridor, with $\Theta(wD^2)$ potential readouts. This is why the exponent depends quadratically on total depth. The [related-work comparison](../references/RELATED_WORK.md) details the distinct assumptions and explains how the matching construction distinguishes this resource law from full circuit-noise fault tolerance.
