# From quantum instruments to the optimal depth law

A Bell measurement produces a quantum state and a classical record. This project asks how the reliability of that record limits the depth advantage of measurement and feedforward.

The physical setting is a line of sites $0,\ldots,L$, with one qubit at each site and a product initial state. Quantum operations act within a site or between neighboring sites. Quantum gates, resets, and measurement backaction are ideal. Every binary readout report is independently flipped with a fixed probability $p\in(0,1/2)$. Classical processing and communication are unrestricted and noiseless. Every quantum-operation layer, including reset and readout, contributes to depth. The output is a physical Bell pair at the prescribed endpoints, after the final correction.

For each fixed target overlap $F_0\in(1/2,1)$, the [converse](../science/converse.md) and [construction](../science/construction.md) give

```math
D_{\min}(L;p,F_0)=\Theta_{p,F_0}\!\left(\sqrt{\log L}\right).
```

This means that positive upper and lower constant multiples of $\sqrt{\log L}$ bound the optimal depth for sufficiently large $L$. Those constants may depend on the fixed noise rate and target. The [model](../science/model.md) gives the full operational assumptions.

The selected [Watrous anchor](ANCHOR.md) provides the language for the argument. This bridge derives the project-specific steps and keeps their role distinct from the textbook foundations.

## 1. Keep the quantum output and its probability together

In the instrument formalism of Watrous, Section 2.3.2, a binary measurement is represented by two completely positive maps $\mathcal M_0,\mathcal M_1$. Their sum $\mathcal T=\mathcal M_0+\mathcal M_1$ is trace-preserving. For an input state $\rho$, the positive operator $\mathcal M_b(\rho)$ contains both the outcome probability and the resulting quantum state:

```math
\Pr(b)=\mathrm{Tr}\mathcal M_b(\rho),
\qquad
\rho_b=\frac{\mathcal M_b(\rho)}
{\mathrm{Tr}\mathcal M_b(\rho)}
\quad\text{when }\Pr(b)>0.
```

Here the controller receives a report $y$ that can differ from the true outcome $b$. The map associated with the reported value is therefore

```math
\mathcal I_y=(1-p)\mathcal M_y+p\mathcal M_{1-y}.
```

This equation keeps the measurement's quantum backaction separate from corruption of its record. In particular, for an ideal QND measurement in the computational basis, $\mathcal M_b(\rho)=P_b\rho P_b$, where $P_b=\lvert b\rangle\langle b\rvert$. Once such a measurement has selected a basis state, repeated measurements have the same true bit. Their reported bits still have fresh independent errors. The construction uses this special case; the converse allows every binary instrument admitted by the model.

For a complete accessible transcript $c$, let $\tau^c_{AB}$ be the unnormalized endpoint operator. The joint classical-quantum output has the form

```math
\rho_{CAB}
=\sum_c \lvert c\rangle\langle c\rvert_C\otimes\tau^c_{AB},
\qquad
\Pr(c)=\mathrm{Tr}\tau^c_{AB}.
```

The classical register records which branch occurred. Summing the endpoint operators forgets the transcript. Keeping them unnormalized will allow the converse to preserve both the conditional output and its probability, including when the protocol heralds success.

## 2. Rewrite a flipped report as a mixture with complete forgetting

A useful algebraic identity is

```math
\mathcal I_y
=(1-2p)\mathcal M_y+p(\mathcal M_0+\mathcal M_1)
=(1-2p)\mathcal M_y+p\mathcal T.
```

It represents the same noisy instrument by the following random procedure. With probability $1-2p$, retain the true outcome and report it. With probability $2p$, forget the true outcome and report an independent fair bit. On the second component the quantum evolution, after summing the inaccessible outcome, is $\mathcal T$.

For either value of the true bit, the chance of reporting that bit is $(1-2p)+(2p)/2=1-p$, and the chance of reporting the other bit is $p$. Thus the representation reproduces the full instrument, not merely its classical error rate.

The forgetting flag is a variable used in the proof's decomposition. It is not a claim that the apparatus reveals detectable erasures. Nor does forgetting mean that the qubit has been reset: for the QND instrument, $\mathcal T$ is dephasing in the computational basis. A hidden result may still be encoded in quantum systems. The converse must account for how far those systems can propagate its influence.

## 3. A wide corridor of forgotten records permits an exact cut

The relevant channel identity is

```math
\mathrm{Tr}\!\left[O\,\mathcal T(\rho)\right]
=\mathrm{Tr}\!\left[\mathcal T^\dagger(O)\rho\right],
\qquad
\mathcal T^\dagger(I)=I
\quad\text{for a trace-preserving }\mathcal T.
```

Watrous's Theorem 2.26 supplies the second equality. In a local circuit, it has a geometric consequence: a trace-preserving operation acting only where a backward-propagated observable is the identity cannot enlarge that observable's support. A selective measurement branch can behave differently, because its adjoint need not preserve the identity.

Fix the forgetting flags, the replacement bits, the controller's random seed, and a complete accessible transcript. The adaptive policy then specifies an ordinary sequence of local maps. Every forgotten report contributes a trace-preserving map. The selective maps that can introduce additional observable support occur only at informative report locations.

Now suppose an interior corridor contains $2D+2$ consecutive columns, and every possible readout slot in that corridor is forgotten throughout a protocol of depth $D$. Its central cut is more than $D$ nearest-neighbor steps from every location outside the corridor. Backward support starting at either output or at any informative report cannot reach the quantum operations crossing that cut. Removing those operations therefore preserves each unnormalized endpoint branch exactly.

This is the project's **adaptive causal-cut lemma**. It requires the finite propagation speed of quantum operations and the absence of informative report locations throughout the entire buffer. One bad report alone would not justify such a conclusion. Coherent copies of hidden outcomes are also covered, because moving or copying them uses the same local quantum operations.

After cut removal, only local quantum operations and classical communication connect the two sides. The initial state is separable across that cut, and every retained transcript branch remains separable. This is where the separability and LOCC framework of Watrous, Sections 6.1.1–6.1.2, enters. Because the lemma preserves branch probabilities as well as endpoint operators, its conclusion survives transcript-based postselection. See the [converse proof](../science/converse.md) for the branchwise equality and the treatment of all adaptive schedules.

## 4. Convert corridor probability into a Bell-overlap bound

The converse also permits at most $w$ qubits per column, with $w$ fixed. The main construction has $w=1$. At most $wD$ potential readout slots occur in one column during depth $D$. Slots that are never used can be assigned independent flags in advance, so adaptive choices do not change the counting argument.

For a corridor of $2D+2$ columns, the event that all potential slots are forgotten has probability

```math
q=(2p)^{w(2D+2)D}.
```

One can pack

```math
K=\left\lfloor\frac{L-1}{2D+2}\right\rfloor
```

disjoint interior corridors. Their flag events are independent. Hence the probability that no packed corridor is entirely forgotten is

```math
G=(1-q)^K\leq e^{-Kq}.
```

Whenever at least one corridor is entirely forgotten, the endpoint state is separable. A normalized separable two-qubit state has Bell overlap at most $1/2$: for a product vector this follows from

```math
\left|\langle\Phi^+|u\otimes v\rangle\right|^2
=\frac12\left|u_0v_0+u_1v_1\right|^2
\leq\frac12,
```

and mixtures preserve the inequality. The remaining flag patterns have overlap at most one. Averaging gives

```math
F\leq \frac12+\frac12G
=\frac12+\frac12(1-q)^K.
```

For a heralded success event with probability $P_S>0$ and conditional Bell overlap $F_S$, the corresponding statement is

```math
P_S(2F_S-1)\leq G.
```

One obtains it by applying the witness $2\Pi_+-I$, where $\Pi_+=\lvert\Phi^+\rangle\langle\Phi^+\rvert$, to the unnormalized accepted output. Thus a rare successful branch is weighted by its actual probability.

For fixed $p$ and fixed width, $q=\exp[-O(D^2)]$, while $K$ is of order $L/D$ in the sublinear-depth regime. If $D$ is a sufficiently small constant multiple of $\sqrt{\log L}$, then $Kq$ grows without bound and the allowed Bell overlap tends to $1/2$. A fixed target above $1/2$ therefore requires depth $\Omega(\sqrt{\log L})$.

## 5. Use space and repeated readout to match the lower bound

The construction begins with Bell links on disjoint segments of the same chain. Moving one half of each link to its segment boundary returns all interior sites to zero. Neighboring link endpoints then undergo Bell-basis rotations. Each junction produces two basis bits that specify the final endpoint correction.

Before reading those bits, local CNOT gates distribute each basis value into a bank of $r+1$ qubits. This is coherent copying of a computational-basis label. If the source is in a superposition, the bank is entangled with that source; the operation does not produce independent copies of an arbitrary quantum state.

Read every bank qubit $s$ times. A bank supplies $(r+1)s$ independent noisy reports of one true bit. Choose an odd number $M$ of those reports, discarding at most one predetermined sample, and decode by majority. The exact error probability is

```math
q_M(p)=
\sum_{k=(M+1)/2}^{M}\binom Mk p^k(1-p)^{M-k}
\leq e^{-c_pM},
\qquad
c_p=-\log\!\left(2\sqrt{p(1-p)}\right)>0.
```

With $m$ Bell links there are $2(m-1)$ junction bits. A union bound gives

```math
1-F\leq 2(m-1)e^{-c_pM}.
```

Link preparation and spatial copying take depth of order $r$; sampling takes depth $s$. Taking both scales of order $\sqrt{\log L}$ makes $M$ of order $\log L$, enough to suppress the aggregate correction error while keeping total depth $O(\sqrt{\log L})$. The [construction proof](../science/construction.md) supplies the balanced partition, disjoint gate schedule, exact fidelity, and unitary fallback for short chains.

The universal lower bound is proved separately by the corridor argument. Majority decoding and the balancing of these particular resources explain why this construction reaches it.

## 6. A complete eight-qubit example

Take $N=L+1=8$ sites, numbered $0$ through $7$, and initialize every qubit in $\lvert0\rangle$. Set

```math
r=1,\qquad s=2,\qquad
\ell=2r+2=4,\qquad
m=\left\lfloor\frac{8}{4}\right\rfloor=2,\qquad
B=4.
```

The segments contain sites $0,1,2,3$ and $4,5,6,7$, respectively. The following ten-layer schedule uses native nearest-neighbor SWAP gates.

| Layer | Simultaneous operations | Purpose |
|---:|---|---|
| 1 | $H_0,\ H_4$ | Start the two links |
| 2 | $`\mathrm{CNOT}_{0\to1},\ \mathrm{CNOT}_{4\to5}`$ | Create adjacent Bell pairs |
| 3 | $`\mathrm{SWAP}_{1,2},\ \mathrm{SWAP}_{5,6}`$ | Move the right halves outward |
| 4 | $`\mathrm{SWAP}_{2,3},\ \mathrm{SWAP}_{6,7}`$ | Complete the links $(0,3)$ and $(4,7)$ |
| 5 | $\mathrm{CNOT}_{3\to4}$ | Start the junction Bell-basis rotation |
| 6 | $H_3$ | Complete that rotation |
| 7 | $`\mathrm{CNOT}_{3\to2},\ \mathrm{CNOT}_{4\to5}`$ | Create the two readout banks |
| 8 | QND $Z$ readout of sites $2,3,4,5$ | Obtain the first report from each bank qubit |
| 9 | QND $Z$ readout of sites $2,3,4,5$ | Obtain the second report from each bank qubit |
| 10 | $X^{\widehat v}Z^{\widehat u}$ on site $7$ | Apply the decoded endpoint correction |

Each row acts on disjoint supports. After layer 4, the state is a Bell pair on $(0,3)$ and another on $(4,7)$, with sites $1,2,5,6$ returned to zero. Write $u$ for the computational-basis bit of site $3$ after the Bell rotation and $v$ for that of site $4$. After layer 7, the coherent state can be written, with tensor factors ordered by their subscripts, as

```math
\frac12
\sum_{u,v\in\{0,1\}}
\lvert u,u\rangle_{2,3}
\lvert v,v\rangle_{4,5}
\left(I\otimes X^vZ^u\right)
\lvert\Phi^+\rangle_{0,7}
\otimes\lvert0,0\rangle_{1,6}.
```

The first readout layer selects $(u,v)$ with probability $1/4$ for each pair. The banks on sites $2,3$ and $4,5$ then retain their respective true bits. Each bank supplies four reports across the two readout layers. Retain three predetermined reports from each bank, for example by discarding the second report from site $2$ and the second report from site $5$. All eight performed readouts are included in the resource count.

At $p=1/5$, a three-vote majority is wrong if two or three of its reports are flipped:

```math
q_3
=3\left(\frac15\right)^2\frac45
+\left(\frac15\right)^3
=\frac{13}{125}
=0.104.
```

There is one junction. Its two decoded-bit errors are independent, so the corrected pair has the target Bell label exactly when both decoders are correct:

```math
F=(1-q_3)^2
=\left(\frac{112}{125}\right)^2
=\frac{12544}{15625}
=0.802816.
```

For completeness, if $\Pi_{uv}$ projects onto $(I\otimes X^vZ^u)\lvert\Phi^+\rangle$, the endpoint density operator is

```math
\rho_{0,7}
=\frac{12544}{15625}\Pi_{00}
+\frac{1456}{15625}(\Pi_{10}+\Pi_{01})
+\frac{169}{15625}\Pi_{11}.
```

The weights sum to one. The total depth agrees with the general schedule:

```math
D=B+r+s+3=4+1+2+3=10.
```

A direct unitary protocol on eight sites is faster: create a Bell pair at the center and move its halves outward, reaching exact fidelity in $1+\lceil N/2\rceil=5$ layers. This example illustrates the bank mechanism and its accounting. The asymptotic theorem concerns growing endpoint separation; it does not assert a small-chain advantage for this parameter choice.

## 7. What the bridge adds to the selected source

Watrous supplies the definitions of states, channels, instruments, adjoints, separability, and LOCC, together with the teleportation framework. The Bell-overlap convention is translated explicitly in [ANCHOR.md](ANCHOR.md).

The report-mixture identity follows by elementary algebra. The project-specific argument combines it with a causal corridor for arbitrary adaptive protocols, counts independent forgotten corridors, and matches the resulting lower bound with a schedule that uses the existing chain's interior qubits. The [related-work account](../references/RELATED_WORK.md) attributes the established locality, separable-mixture, entanglement-swapping, and readout-amplification methods.

The result remains a law for fixed readout noise, fixed target overlap, and fixed physical width with ideal quantum operations. It does not by itself establish a gate-noise threshold or a uniform lower bound for every vanishing target error. The exact linear-depth unitary protocol remains available throughout this model.

