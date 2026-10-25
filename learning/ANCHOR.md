# Reading anchor: Watrous (2018)

The selected educational source is **John Watrous, _The Theory of Quantum Information_, Cambridge University Press, 2018**. The [author's book page](https://cs.uwaterloo.ca/~watrous/TQI/) identifies the April 2018 publication and provides a manuscript for personal reading. This guide uses the **2018 pre-publication manuscript in its standard layout**, whose status and copyright year appear in the [front matter](https://cs.uwaterloo.ca/~watrous/TQI/TQI.frontmatter.pdf). Page numbers below are the printed page numbers in that manuscript, not PDF viewer page numbers. The [author's errata](https://cs.uwaterloo.ca/~watrous/TQI/TQI.errata.pdf) accompany the source.

Watrous is the one educational anchor for this project. Its channels, instruments, and separability language provide the foundation for the proof. The project's geometry, noise assumptions, circuit schedule, and optimal depth law are developed in the repository. The linked manuscript is not reproduced here.

## A route into the argument

The question is how much local quantum processing is necessary to prepare a Bell pair between distant, prescribed qubits when every classical readout report has a fixed independent error probability. Quantum operations and measurement backaction are ideal. Both gates and readout rounds contribute to depth.

The following route supplies the concepts needed to follow that question through the [bridge](BRIDGE.md). The [milestones](MILESTONES.md) organize the individual proof steps.

| Passage in the selected source | What to extract | Where it enters this project |
|---|---|---|
| [Chapter 2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf), Sections 2.1.1–2.1.3, pp. 58–71 | Registers, density operators, mixtures, and partial trace | Separate the physical qubits from the classical transcript and retain only the endpoint output |
| Chapter 2, Sections 2.2.1–2.2.2, pp. 72–90 | Completely positive maps and trace-preserving channels | Describe every allowed quantum operation and the evolution when an outcome is forgotten |
| Chapter 2, Sections 2.3.1–2.3.2, pp. 100–113 | Measurement probabilities and instruments with a retained quantum output | Distinguish the true outcome, the noisy report, and the measured qubit |
| [Chapter 3](https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf), Section 3.2, Definition 3.11, p. 139 | The source's root-fidelity convention | Translate it to the Bell overlap used by the theorem |
| [Chapter 6](https://cs.uwaterloo.ca/~watrous/TQI/TQI.6.pdf), Sections 6.1.1–6.1.2, pp. 310–332 | Separable operators and local operations with classical communication | Show why deleting quantum interactions across a cut leaves separable endpoint branches |
| Chapter 6, Section 6.3.1, especially Example 6.50, pp. 365–366 | Bell measurement and outcome-dependent corrections in qubit teleportation | Understand why entanglement swapping needs two reliable correction bits |

Two precise passages are especially useful for the converse. Chapter 2, Theorem 2.26 on p. 87 states that a map preserves trace exactly when its adjoint preserves the identity. Section 2.3.2, Eqs. (2.258)–(2.262) on pp. 112–113, describes instruments as completely positive branches that sum to a channel and packages their outcomes into a classical register. The adjoint itself is defined in [Chapter 1](https://cs.uwaterloo.ca/~watrous/TQI/TQI.1.pdf), Section 1.1.2, Eq. (1.112), pp. 21–22.

For unnormalized branch notation, Chapter 2, Section 2.1.2, Eqs. (2.9)–(2.11) on p. 63 treats an ensemble element as a positive operator whose trace gives its probability. For the cut argument, Chapter 6, Definition 6.1 on p. 311 and Proposition 6.26 on p. 332 provide the separable-operator and LOCC framework. These specific passages suffice; the extremality results and later capacity chapters are not prerequisites for this proof.

## Translating the notation

The book uses matrix and vector notation throughout. The research pages also use Dirac notation for circuits and Bell states. The following translations prevent several otherwise easy ambiguities.

| Source notation or convention | Project notation or convention | Meaning |
|---|---|---|
| Standard basis vector $e_a$ | $\lvert a\rangle$ | A computational-basis state vector |
| Pure-state operator $uu^*$ | $\lvert u\rangle\langle u\rvert$ | The density operator associated with a unit vector |
| Matrix unit $E_{a,b}$ | $\lvert a\rangle\langle b\rvert$ | An operator, not a probability |
| Identity $1_{\mathcal X}$ | $I_{\mathcal X}$, often $I$ | The identity operator on a register's state space |
| Adjoint map $\Phi^*$ | $\mathcal T^\dagger$ or $\mathcal E^\dagger$ | The map used to propagate observables backward |
| Instrument branch $\Phi_a$ | $\mathcal M_b$ for a true outcome; $\mathcal I_y$ for a reported outcome | A completely positive map that generally does not preserve trace |
| Ensemble element $\eta(a)$ | An unnormalized branch such as $\rho^c_{AB}$ | Its trace is the probability of the associated record |
| $\mathrm{Sep}(\mathcal X:\mathcal Y)$ | Separability across a physical cut, or across $A:B$ | Positive sums of product operators for the specified bipartition |
| The book's fidelity function | The project's Bell overlap $F$ | The project uses the square of the book's fidelity when the second argument is the pure Bell target |

The fidelity conversion is explicit. With $\Pi_+=\lvert\Phi^+\rangle\langle\Phi^+\rvert$ and normalized endpoint state $\rho_{AB}$,

```math
F_{\mathrm{project}}
=\mathrm{Tr}(\Pi_+\rho_{AB})
=F_{\mathrm{Watrous}}(\rho_{AB},\Pi_+)^2.
```

Consequently the project's separable threshold $F_{\mathrm{project}}\leq 1/2$ corresponds to $F_{\mathrm{Watrous}}\leq 1/\sqrt{2}$. The symbol $\Phi$ also needs context: a script letter such as $\mathcal M$ denotes a map in the project, while $\lvert\Phi^+\rangle$ denotes the target state.

## From the source to the research pages

The [bridge](BRIDGE.md) applies these definitions to noisy reports and explains why the converse preserves unnormalized transcript branches. It then connects the probability of a forgotten corridor to the explicit Bell-link construction.

The [model](../science/model.md) fixes the physical resources and quantifiers. The [converse](../science/converse.md) proves the adaptive causal-cut statement and its probability bound. The [construction](../science/construction.md) supplies the nearest-neighbor schedule and matching upper bound. The [related-work account](../references/RELATED_WORK.md) attributes the established research methods and compares the precise assumptions.

The claim to be understood is that, for each fixed $p\in(0,1/2)$ and fixed $F_0\in(1/2,1)$, the minimum depth on a chain with one qubit per site satisfies $D_{\min}(L;p,F_0)=\Theta_{p,F_0}(\sqrt{\log L})$ as the endpoint separation $L$ grows. It is not a theorem stated in the selected textbook.

