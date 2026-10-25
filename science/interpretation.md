# What readout noise changes

A long chain can contain many short Bell links prepared in parallel. With ideal measurement records, simultaneous Bell measurements connect these links, and two classically computed parity corrections determine the final Bell state. The number of quantum layers can remain constant as the chain grows. This is the operational advantage addressed by measurement-assisted locality bounds and dynamic-circuit protocols; see [the source comparison](../references/RELATED_WORK.md).

The question here is the minimum quantum-and-readout depth when every reported measurement bit is independently wrong with a fixed probability. The [model](model.md) retains perfect quantum operations and unrestricted reliable classical processing so that the effect of this one noise source can be identified.

## The optimal depth

Let $L$ be the separation of the designated endpoints. Fix a readout error probability $0<p<1/2$ and a target Bell overlap $1/2<F_0<1$. The [converse](converse.md) and [construction](construction.md) give

```math
D_{\min}(L;p,F_0)
=\Theta_{p,F_0}\!\left(\sqrt{\log L}\right).
```

This statement compares all allowed adaptive protocols with an explicit nearest-neighbor protocol. The constants may depend on $p$ and $F_0$. The result is not uniform as either parameter approaches a boundary.

The lower bound has a geometric origin. Between accessible measurement ports, local quantum propagation advances at most one site per round. If a corridor of width proportional to $D$ has no informative reports during those $D$ layers, every operation across its central cut can be removed without changing the complete accessible transcript and endpoint state. The remaining circuit uses local quantum operations and classical communication across the cut, so its endpoint state is separable.

A corridor contains order $D^2$ potential readout locations in space and time. The probability of losing all its quantum-dependent records is exponentially small in $D^2$, but a chain has order $L/D$ independent opportunities for such a corridor. This competition yields the square-root logarithm.

The construction uses the same two resources. Distributing an outcome to $r+1$ adjacent qubits takes order $r$ local layers. Reading those qubits for $s$ rounds gives order $rs$ independent reports at a total depth of order $r+s$. Taking both $r$ and $s$ of order $\sqrt{\log L}$ suppresses the probability of any relevant decoding error along the chain.

Only orthogonal basis labels are copied. The copying circuit acts coherently before the measurement, and does not clone an arbitrary unknown quantum state.

## Finite-size statements and accessible range

For one qubit per site, define

```math
K=\left\lfloor\frac{L-1}{2D+2}\right\rfloor,
\qquad
q_D=(2p)^{2D(D+1)}.
```

For integer $D\geq1$, the finite converse is

```math
F_{\mathrm{Bell}}
\leq \frac12+\frac12(1-q_D)^K
\leq \frac12+\frac12\exp(-Kq_D).
```

The expression is valid but uninformative when $K=0$. It is an analytical bound with conservative constants, not a prediction of a particular device's fidelity.

Write $\eta=2F_0-1$. A necessary condition for achieving $F_0$ is $Kq_D\leq-\log\eta$. In particular,

```math
L<
1+(2D+2)\left[
1+(-\log\eta)(2p)^{-2D(D+1)}
\right].
```

Together with the construction, this means that the largest attainable separation at fixed fidelity grows as $\exp[\Theta_{p,F_0}(D^2)]$ at large $D$, up to changes in the constants in the exponent. Readout noise therefore sets a finite useful range at every fixed depth. The range is still much larger than the distance reachable by a purely unitary circuit of the same depth.

The probability law also controls heralding. If a protocol declares success using its accessible records, retains the endpoint qubits, and has conditional Bell overlap $F_S$, then

```math
\Pr(S)(2F_S-1)\leq(1-q_D)^K.
```

A success probability bounded away from zero and a conditional Bell overlap bounded above $1/2$ require the same asymptotic depth. The success probability is part of the resource statement.

## Three readout regimes

| Readout channel | Optimal depth for fixed $1/2<F_0<1$ | Reason |
|---|---:|---|
| Perfect reports, $p=0$ | $\Theta(1)$ | Parallel local Bell preparation, swapping, and reliable frame correction |
| Fixed informative noisy reports, $0<p<1/2$ | $\Theta(\sqrt{\log L})$ | Erased-corridor obstruction and matching spatial and temporal repetition |
| Completely uninformative reports, $p=1/2$ | $\Theta(L)$ | Classical records convey no quantum-dependent information; local quantum propagation determines the range |

At $p=1/2$, all reported bits are independent fair coins. Condition on these coins and any other classical randomness. Every quantum operation is then a predetermined local trace-preserving map. If the two endpoint backward cones are disjoint, their reduced state factorizes for product initialization. Averaging the coins can create classical correlations but preserves separability. Thus depth proportional to $L$ is necessary for Bell overlap above $1/2$.

For the matching linear upper bound, prepare a Bell pair near the center of the chain and move its two halves outward using simultaneous nearest-neighbor SWAP layers. This circuit uses no measurements and prepares an exact Bell pair. With $N=L+1$ sites and native SWAP gates, its depth is $1+\lceil N/2\rceil$ for $N\geq2$.

This measurement-free circuit also limits any extension toward very small target infidelity. An upper bound of order $\sqrt{\log(L/\epsilon)}$ is useful when it is smaller than the linear unitary cost. It cannot be an unrestricted optimal law as $\epsilon$ tends to zero: exact unitary preparation remains available in order $L$ depth. The main theorem fixes $F_0<1$ and makes no claim of matching dependence on a vanishing $\epsilon$.

## The resources that determine the statement

**Quantum operations and reporting are separated.** A measurement has ideal quantum backaction, while its binary classical output passes through a noisy channel. Repeated quantum nondemolition readout therefore measures the same underlying basis value. Gate errors, storage errors, and disturbances introduced by imperfect repeated measurements can change this behavior. Their fault-tolerant treatment is a different model.

**Every readout round costs depth.** Counting only entangling gates while allowing unlimited free readout would remove the temporal cost central to this problem. The model allows at most one elementary operation per qubit in a layer. Fixed ratios between elementary gate times and readout times change constants, provided those ratios do not grow with $L$.

**The quantum width is fixed.** There is one qubit at each site of the chain. The converse also permits any fixed number $w$ per column, with $q_D=(2p)^{2wD(D+1)}$. The matching headline already holds at $w=1$. This does not establish an optimal joint width-depth tradeoff when $w$ grows with distance. Additional transverse dimensions or growing verification registers are physical resources, as in fault-tolerant quantum-bus and single-shot state-preparation protocols.

**The classical controller is unrestricted.** It can receive all accessible records, compute the decoding and Pauli corrections, and send control instructions without a depth charge. The theorem concerns quantum-and-readout circuit depth under this convention. A physical communication delay that grows with separation must be added in an implementation; the result does not assert distance-independent wall-clock classical communication.

**The output is a physical state.** Bell overlap is evaluated on two retained, designated endpoint qubits after the correction. An unbiased estimator obtained by readout-error mitigation does not by itself prepare this state. Likewise, destructive measurement of the two outputs is a different task from retaining an entangled pair for later use.

**The preparation starts without shared entanglement.** Local product inputs and local reset states are available. A pre-established long-range entangled resource would already supply part of the task and is excluded from the depth minimization.

## What is inherited and what is established here

The proof uses established ideas from measurement-assisted locality and from decomposing noise into separable components at rare cuts. Repetition encoding and majority decoding of measurement outcomes are also established. Their attribution and the distinctions between their operational models appear in [Related work](../references/RELATED_WORK.md).

The contribution is the sharp optimal depth for a fixed, independent readout channel in a fixed-width one-dimensional circuit. Perfect quantum gates can carry information through a locally uninformative measurement region, which is why a single spatial cut of corrupted reports is insufficient. The depth-wide corridor accounts for this coherent transport and produces the quadratic spacetime exponent. The explicit construction attains the resulting depth order while charging the geometry of the repetition registers.

[Scientific route](README.md) · [Exact model](model.md) · [Converse](converse.md) · [Construction](construction.md)

