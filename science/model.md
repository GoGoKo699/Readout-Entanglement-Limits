# Circuit model and preparation task

We study the preparation of a Bell pair between two distant physical qubits on a line. The processor can use local quantum operations, measurements during the circuit, and unrestricted classical feedback. Quantum operations and measurement backaction are ideal. The only noise is an independent error in each reported measurement bit. The question is how many circuit rounds are required when both quantum gates and repeated readouts take time.

The [converse](converse.md) applies to arbitrary adaptive protocols in this model. The [construction](construction.md) attains its distance scaling with a nearest-neighbor Clifford circuit and repeated quantum nondemolition readout. The [interpretation](interpretation.md) explains the operational scope of the resulting depth law.

## Geometry, initial state, and retained memory

Let $L\geq1$ be an integer. The main model is a chain with one physical qubit at each site $x=0,1,\ldots,L$. The designated output qubits are $A$ at site $0$ and $B$ at site $L$. Their separation is $L$ nearest-neighbor edges. Their locations are fixed before the protocol starts.

For the converse, we also allow a strip with at most $w\geq1$ physical qubits in each column $x$, where $w$ is an integer. The main chain is the case $w=1$. Quantum operations may connect qubits in the same column or in two neighboring columns. They have no direct quantum connection between nonadjacent columns. The two outputs remain single physical qubits in columns $0$ and $L$.

The initial state is a product across columns:

```math
\rho_{\mathrm{in}}=\bigotimes_{x=0}^{L}\rho_x.
```

Within a column, $\rho_x$ may be arbitrary. Shared classical randomness may also select a mixture of such product states. Conditioning on that randomness recovers the displayed form, so the converse covers all states separable across the columns. The construction starts with every qubit in $|0\rangle$.

All quantum memory retained between rounds counts toward the physical width $w$. A fresh ancilla can occupy an unused physical slot, and an existing slot can be reset and reused. These operations preserve the same width limit. An environment used to implement a local quantum channel is discarded; an environment that remains available for later quantum processing is part of the retained memory and must be counted. In particular, the processor starts without entanglement shared across columns.

Depth is measured after the initial product state is available. Including its parallel initialization adds a constant layer. Subsequent resets, gates, and readouts are included in the circuit depth.

## A circuit round

A protocol of depth $D$ consists of $D$ synchronous rounds. The operations in a round act on disjoint sets of physical qubits. Each operation is one of the following:

- An ideal quantum gate or trace-preserving quantum channel supported within one column or across two neighboring columns.
- An ideal single-qubit binary instrument, followed by one noisy report of its outcome.
- An idle operation on a physical qubit.

A reset is a local trace-preserving channel. Allowing general local channels makes the converse at least as permissive as the usual unitary gate model. The explicit construction uses single-qubit Clifford gates, nearest-neighbor two-qubit gates, and single-qubit readouts.

Each physical qubit participates in at most one operation per round. In particular, it supplies at most one reported measurement bit in that round. A joint observable is measured by first coupling it to a readout qubit through the charged local circuit. Its classical report is then a single-qubit outcome port.

All operations for round $t$ are selected using records available before that round. Reports produced during round $t$ become available for round $t+1$. Thus there is no within-round chain of quantum operations hidden inside instantaneous classical feedback. Gates selected from the previous history may vary arbitrarily with that history, subject to the same locality and depth conditions.

Classical memory, computation, communication, and independent randomness are otherwise unrestricted, reliable, and free. Classical messages may travel across the whole line between consecutive rounds. This gives the controller the strongest possible classical processing capability while keeping the physical quantum operations local.

## Noise acts on the report

A binary instrument on a physical qubit consists of completely positive maps $\mathcal M_0$ and $\mathcal M_1$ whose sum is trace preserving. The instrument can depend on the earlier accessible history. For an input state $\rho$, the unnormalized state conditioned on the true outcome $b$ is $\mathcal M_b(\rho)$, and its trace is the probability of that outcome.

The true outcome is reported through a binary symmetric channel with fixed error probability $p$:

```math
\Pr(y\mid b)=
\begin{cases}
1-p,&y=b,\\
p,&y\ne b.
\end{cases}
\qquad 0<p<\frac12.
```

Consequently, the physical operation conditioned on the accessible report $y$ is

```math
\mathcal I_y
=(1-p)\mathcal M_y+p\mathcal M_{1-y}.
```

At each actual readout, a fresh flip $Z$ with Bernoulli distribution of parameter $p$ is drawn and the accessible report is $y=b\oplus Z$. This flip is independent of the prior history, the current true instrument outcome, and the controller's independent random seed. Repeated readouts of the same qubit receive fresh independent flips under the same rule. Future quantum states and true outcomes may depend on past reported bits through feedback. The instrument backaction is ideal; no additional quantum fault is inserted by the reporting channel. The true outcome and the apparatus environment are unavailable as separate classical inputs to the controller.

The measured qubit can remain in the processor. A later gate may act coherently on its post-measurement state, and the qubit may be measured again. Both operations are charged to later rounds. For example, ideal quantum nondemolition measurement of $Z$ has

```math
\mathcal M_b(\rho)=P_b\rho P_b,
\qquad P_b=|b\rangle\langle b|.
```

After the first such measurement, repeated ideal $Z$ measurements have the same true outcome. Their reports still contain independent errors. This distinction between physical backaction and assignment error is the resource used by the matching construction.

General quantum instruments are useful for the converse because they include changes of measurement basis and outcome-dependent local backaction. No particular gate set, stabilizer description, or classical decoder is assumed in the lower bound.

## Bell fidelity and success

The target is the two-qubit state

```math
|\Phi^+\rangle_{AB}
=\frac{|00\rangle+|11\rangle}{\sqrt2},
\qquad
\Phi_{AB}=|\Phi^+\rangle\langle\Phi^+|.
```

After all charged quantum operations, trace out every physical system except $A$ and $B$. Let $c$ denote the accessible classical transcript, including any declared classical randomness. The unnormalized conditional endpoint state is $\rho_{AB}^{c}$. The actual output state and its fidelity are

```math
\rho_{AB}=\sum_c\rho_{AB}^{c},
\qquad
F=\mathrm{Tr}(\Phi_{AB}\rho_{AB}).
```

Here fidelity means the Bell overlap itself. For this pure target it equals the square of the convention in which fidelity is defined as a square root. Every separable two-qubit state has $F\leq1/2$, so $F>1/2$ certifies endpoint entanglement.

The protocol can also declare a success event $S$ based on the accessible transcript. The endpoints remain quantum outputs when success is declared. Define

```math
\tau_{AB}^{S}=\sum_{c\in S}\rho_{AB}^{c},
\qquad
P_S=\mathrm{Tr}\tau_{AB}^{S},
\qquad
F_S=\frac{\mathrm{Tr}(\Phi_{AB}\tau_{AB}^{S})}{P_S}
\quad(P_S>0).
```

A local quantum filter used to generate a success flag is part of the charged circuit, and its report obeys the same noise rule. Selecting a classical estimate after destructively measuring the endpoints is a different output task. The quantity bounded in the converse is the fidelity of the retained physical pair.

## The optimization problem

For the width-one chain, fix $p\in(0,1/2)$ and a target $F_0\in(1/2,1)$ independently of $L$. Write

```math
D_{\min}(L;p,F_0)
=\min\left\{
D:\text{a permitted depth-}D\text{ protocol has }F\geq F_0
\right\}.
```

The target excludes both the separable threshold and exact fidelity one. Combining the universal [lower bound](converse.md) with the explicit [upper bound](construction.md) gives

```math
D_{\min}(L;p,F_0)
=\Theta_{p,F_0}\!\left(\sqrt{\log L}\right)
\qquad(L\longrightarrow\infty).
```

The constants may depend on the fixed noise rate and target fidelity. Logarithms are natural unless stated otherwise; their base changes only the constants in this asymptotic statement. The statement is a depth law in the endpoint separation. Its finite-size converse also tracks physical width and heralding probability. The [related-work account](../references/RELATED_WORK.md) compares the precise noise and resource assumptions with measurement-assisted locality, noisy quantum buses, and single-shot state preparation.
