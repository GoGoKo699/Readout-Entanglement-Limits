# Related work and attribution

The problem studied here is the depth needed to prepare a physical Bell pair between specified sites of a one-dimensional nearest-neighbor device. The input is a product state, the number of qubits per site is fixed, and quantum gates, resets, and measurement backaction are ideal. Each binary measurement report independently passes through a binary symmetric channel with a fixed error probability $p\in(0,1/2)$. Classical computation and feedforward are unrestricted and noiseless. Depth counts both quantum gates and readout layers.

For a fixed target Bell overlap $F_0\in(1/2,1)$, the result concerns the optimal scaling $\Theta(\sqrt{\log L})$ with endpoint separation $L$. The distinction from the works below is the combination of this noise model, fixed physical width, and a matching converse over arbitrary adaptive protocols. Entanglement swapping, repetition readout, and the use of separable contributions in noisy communication converses are established methods.

## Locality with measurement and feedback

[Friedman, Yin, Hong, and Lucas](https://arxiv.org/abs/2206.09929) bound quantum-information propagation when outcomes from measurements in $M$ local regions are available, even with instantaneous classical communication. Their reference-evolution argument removes interactions across a cut far from the accessible measurement regions and the endpoints. The reference output is separable; locality controls the difference from the original output. The framework includes adaptive locations and nonunitary local operations. See the discussion of the reference cut in the [full manuscript](https://arxiv.org/html/2206.09929v4).

This supplies the relevant causal structure. The present lower bound needs an additional step: a fixed noisy classical channel is decomposed into informative and completely forgotten reports, and a spacetime corridor with only forgotten reports permits the cut removal. Counting measurement regions alone does not give the claimed scaling, because many regions still contain informative reports. The geometry of a completely forgotten corridor, including all possible adaptive measurement slots, determines its probability.

## The closest noisy-communication converse

[Choe and König](https://www.nature.com/articles/s41534-024-00928-4) prove limits on low-latency quantum buses subject to general local stochastic noise. For an adaptive protocol of depth $\Delta$ with $m$ qubits per repeater, Theorem 8.2 of their [full preprint, Section 8.1](https://arxiv.org/html/2209.09774v1), constructs allowed noise with a separable contribution of weight at least

```math
1-\exp\!\left[-R(4p^2/3)^{\Delta m}\right].
```

Robustness against all noise in that class therefore requires a logarithmic dependence on distance in $\Delta m$. Their proof replaces inter-repeater gates with Bell-assisted local operations and classical communication, then uses a depolarizing-channel mixture to obtain independent separable cuts.

That converse does not directly imply a bound for fixed independent readout flips: its constructed noise can damage quantum resources corresponding to entangling gates, whereas those gates are perfect here. The present proof must instead establish that lost classical records in a sufficiently wide causal buffer prevent perfect local gates from contributing endpoint entanglement. The independent-cut probability argument is closely related and should be credited accordingly.

## Readout amplification and Bell-distribution constructions

Encoding the computational-basis information of a measured qubit into a repetition register is established readout-error correction. [Günther et al.](https://arxiv.org/abs/2105.13377) study repetition layouts for quantum simulations. [Hicks et al.](https://arxiv.org/abs/2108.12432) analyze active readout-error mitigation that improves individual measurement shots by encoding immediately before measurement. These works supply precedents for the local amplification primitive, rather than for a universal depth limit.

[Hartung et al.](https://www.nature.com/articles/s41598-026-70209-x) apply verification ancillas and majority voting during one-way quantum computation. Their [full manuscript](https://arxiv.org/html/2411.09084v2), particularly Sections 3–5, distinguishes errors in the classical readout from errors in the quantum projection. It discusses repeated readout for the former and spatial verification registers. Its tree-fanout construction has connectivity different from a fixed-width nearest-neighbor line. Both temporal repetition and spatial copying must therefore be treated as inherited techniques.

[Huang](https://www.nature.com/articles/s44335-026-00094-0) is a particularly close application precedent: the repetition-readout scheme is explicitly applied to Bell generation at the ends of a one-dimensional cluster chain. Intermediate measurements receive verification registers, and decoding suppresses errors in the feedforward information. This already establishes the relevance of repetition readout to the same physical output task. The treatment inspected there does not give the minimum total depth at fixed qubit density or a converse over arbitrary adaptive circuits. The result here concerns that resource accounting and optimality; adding repetition to a Bell-distribution circuit is not itself a new contribution.

In the construction studied here, spatial amplification and repeated sampling are arranged within the existing chain. A block scale $r$ and sampling time $s$ provide order $rs$ noisy reports at depth order $r+s$. The upper bound relies on the explicit nearest-neighbor schedule, including the recovery of usable link-interior qubits. A protocol that copies an already corrupted classical report would not achieve this amplification: the copies must retain the underlying quantum outcome before its information is discarded.

## Single-shot fault tolerance uses different spatial resources

[Bergamaschi and Liu](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ITCS.2025.16) prove noisy single-shot logical-state preparation for CSS quantum LDPC codes using a constant-depth circuit, one round of measurement, and classical feedforward. The [full version](https://arxiv.org/html/2411.04405v1) constructs an alternating Tanner graph with additional space. Bounded degree in that graph does not imply a fixed-width one-dimensional physical embedding. The output is an encoded state with controlled residual noise.

Physical Bell-pair output alone does not distinguish the present task from all single-shot protocols. The Choe–König bus also produces a physical pair, but with a cross-section that grows with the communication distance. Fixed width and the noise model are essential parts of the comparison.

Their later paper, [Choe and König, *How to Fault-Tolerantly Realize Any Quantum Circuit with Local Operations*](https://doi.org/10.1103/PRXQuantum.6.010357), uses such communication primitives to realize circuits with three-dimensional or quasi-two-dimensional local architectures and additional qubits. It does not remove the spatial-resource distinction.

## Ideal preparation frameworks and hardware studies

[Sahay and Verresen](https://doi.org/10.1103/PRXQuantum.6.010329) characterize one-dimensional states obtainable with a single round of measurements and specified unitary feedback. [Styliaris and Trivedi](https://arxiv.org/abs/2609.39764) relate exact measurement-and-feedforward implementations to quantum error-correcting codes. These ideal preparation frameworks identify which transformations admit measurement-assisted realizations. They do not, in the statements inspected, determine their optimal depth under independently corrupted classical reports.

[Bäumer et al.](https://doi.org/10.1103/PRXQuantum.5.030339) experimentally study long-range entangling operations with dynamic circuits and compare them with unitary implementations on local hardware. Their [error budgets](https://arxiv.org/html/2308.13065v2) include mid-circuit measurement, gate, and idle errors. This establishes the practical relevance of feedforward errors, while addressing specified implementations rather than a universal circuit-depth converse.

## Targeted checks of later work

Two later directions were checked because they could otherwise obscure the model comparison. [Yarkoni et al.'s Pangaea architecture](https://arxiv.org/html/2608.01887) uses a quantum bus between logical code patches, a code-distance parameter, and repeated syndrome extraction. Its analysis includes quantum noise and independent measurement flips. It does not provide a fixed-width physical-pair depth theorem. [Czabán et al.](https://arxiv.org/html/2606.30606v1) compare repetition-readout layouts across superconducting and trapped-ion hardware, including majority-vote correction. This supports the established status of the amplification primitive and its dependence on encoding noise; it does not give an all-protocol geometric lower bound.

These comparisons delimit the claim supported by this project. They do not establish that all prior literature has been exhausted. In particular, the result should not be described as the first noisy adaptive-circuit converse, the first use of independent separable cuts, or the first readout-protected long-range Bell protocol. Its proposed distinction is the matched depth law for independent readout noise with fixed one-dimensional width and ideal quantum operations.

## Reference map

Bibliographic metadata and stable source identifiers are in [references.bib](references.bib). The main comparisons use the following keys.

| Topic | BibTeX keys |
|---|---|
| Measurement-assisted locality | `Friedman2022Locality` |
| Noisy quantum-bus converse | `ChoeKoenig2024Bus` |
| Repetition readout | `Gunther2022Readout`, `Hicks2022ActiveReadout`, `Hartung2026Readout`, `Huang2026Sampling` |
| Single-shot preparation and local architectures | `BergamaschiLiu2025SingleShot`, `ChoeKoenig2025Local` |
| Ideal measurement preparation | `SahayVerresen2025Classification`, `StyliarisTrivedi2026Codes` |
| Dynamic-circuit experiments | `Baumer2024LongRange` |
| Later architecture and readout checks | `Yarkoni2026Pangaea`, `Czaban2026Repetition` |
