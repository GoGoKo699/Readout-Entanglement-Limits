# Adaptive Entanglement Depth

**How does noisy readout change the minimum depth needed to create long-range entanglement?**

On a one-dimensional nearest-neighbor chain, independent measurement-report noise changes the optimal depth from constant to square-root logarithmic. For a fixed report-flip probability $0<p<1/2$ and fixed target Bell overlap $1/2<F_0<1$,

```math
D_{\min}(L;p,F_0)
=\Theta_{p,F_0}\!\left(\sqrt{\log L}\right).
```

Here $L$ is the separation of two designated output qubits. The circuit starts from a product state, has one qubit per site, and uses perfect local quantum operations with unrestricted reliable classical feedforward. **Depth includes quantum gates and readout rounds.**

| Measurement reports | Optimal depth at fixed target fidelity |
|---|---:|
| Perfect, $p=0$ | $\Theta(1)$ |
| Independently noisy, fixed $0<p<1/2$ | $\Theta(\sqrt{\log L})$ |
| Completely uninformative, $p=1/2$ | $\Theta(L)$ |

## The obstruction and the construction

A noisy binary report admits an exact representation as a truthful outcome or an independent random bit whose underlying measurement outcome is forgotten. If every potential readout in a depth-wide corridor is forgotten, all operations across its central cut can be removed without changing the accessible transcript or endpoint state. The resulting endpoint state is separable.

For depth $D\geq1$, define

```math
K=\left\lfloor\frac{L-1}{2D+2}\right\rfloor,
\qquad
q=(2p)^{2D(D+1)}.
```

Every allowed adaptive protocol obeys

```math
F_{\mathrm{Bell}}
\leq\frac12+\frac12(1-q)^K.
```

The same argument gives the heralded bound
$\Pr(S)(2F_S-1)\leq(1-q)^K$.

The matching protocol prepares local Bell links, performs Bell-basis gates at their junctions, and protects each junction outcome with nearby copying qubits and repeated readout. Spatial replication over $r+1$ qubits and $s$ readout rounds provides order $rs$ independent samples at depth order $r+s$. Choosing both resources of order $\sqrt{\log L}$ attains the lower-bound scaling.

The locality, rare-cut, and repetition ingredients have established precedents. The [related-work account](references/RELATED_WORK.md) identifies those ingredients and compares the sharp readout-only depth law with the closest quantum-bus and measurement-mitigation results.

## Read the science

Start with the [scientific route](science/README.md) and [exact model and claims](science/model.md).

| To understand or check | Read |
|---|---|
| Why arbitrary adaptive control cannot evade the bound | [Converse and full transcript-output proof](science/converse.md) |
| How to attain the depth on an arbitrary chain length | [Construction and resource counts](science/construction.md) |
| Physical meaning, limiting cases, and charged resources | [Interpretation](science/interpretation.md) |
| Inherited methods and closest comparisons | [Related work](references/RELATED_WORK.md) and [bibliography](references/references.bib) |
| Reproducible finite calculations | [Verification](verification/README.md) |
| A question-directed map of the repository | [LLM reading guide](llms.txt) |

## Learn the argument

The [learning route](learning/README.md) connects John Watrous's *The Theory of Quantum Information* (2018) to this project. Its [source guide](learning/ANCHOR.md) identifies the relevant sections and notation. The [bridge](learning/BRIDGE.md) develops the measurement-report model, the separator mechanism, and a complete eight-site example.

The [30-milestone map](learning/MILESTONES.md) has two phases: 12 milestones establish the mathematical and operational foundations, and 18 follow the converse and construction through to the optimal-depth law and its limits. Each phase moves from individual objects and operations to their role in the complete argument.

## Reproduce the checks

From the repository root, run:

```bash
python3 verification/verify_construction.py
```

The checks use Python's standard library. They inspect actual nearest-neighbor circuits, parallel scheduling, measurement branches, endpoint corrections, and the noisy-decoding fidelity. The universal lower bound and asymptotic optimum rest on the written proofs. See [Verification](verification/README.md) for the executed checks and their limits.

## Scope

The result isolates independent noise in the classical measurement reports. Gates, initialization, storage, and measurement backaction are ideal. The output is a retained physical endpoint Bell pair. Readout samples and quantum operations are charged, while classical communication and computation are free.

The headline fixes the noise rate and target fidelity strictly inside their stated intervals. It does not give optimal constants as these parameters vary, a full noisy-gate threshold, or a joint optimum for growing transverse width. A measurement-free unitary protocol prepares an exact Bell pair in linear depth and bounds any extension toward vanishing infidelity.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).

