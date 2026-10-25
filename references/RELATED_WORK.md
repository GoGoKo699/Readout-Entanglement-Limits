# Related work and attribution

This account separates the established ingredients from their use in the [readout-limited entanglement problem](../science/model.md). It specifies the source versions used for section and equation references. Bibliographic entries are available in [references.bib](references.bib).

## Ingredients and their roles

| Ingredient | Attribution | Role in this project |
|---|---|---|
| Measurement-assisted locality and separable comparison states | [Friedman et al.](#friedman2023) | The blind-strip argument is a fixed-cut circuit specialization of this geometric framework. |
| Rare entanglement-breaking cuts in a noisy quantum bus | [Choe and König](#choe2024) | A close converse strategy, with quantum noise and repeater resources different from the report-only model. |
| Readout Chernoff information and repeated binary decoding | [D'Anjou](#danjou2021), [Chernoff](#chernoff1952) | The detector coefficient and the exponential reliability of repeated reports are established ingredients. |
| Coherent processing to improve imperfect measurements | [Kim et al.](#kim2025), [Byrne et al.](#byrne2026) | Amplification is known. The construction here accounts for its local space and time cost. |
| Spatial repetition encoding and temporal readout voting | [Günther et al., Hicks et al., and Hartung et al.](#repetition-readout) | Established primitives protect individual outcomes before feedforward; both kinds of redundancy are charged in the present schedule. |
| Repetition-protected Bell generation on a cluster chain | [Huang](#huang2026) | A direct precedent for improving the physical endpoint Bell state, distinct from a universal depth optimum at fixed density. |
| Block fusion with majority-voted boundary records | [Waring et al.](#waring2026) | A close construction antecedent for preparing local entangled blocks and fusing them through redundant reports. |
| Fault-tolerant single-shot logical-state preparation | [Bergamaschi and Liu](#bergamaschi2025) | Constant-depth encoded entanglement uses a different graph and spatial overhead, so output type and geometry must both be compared. |
| Mixtures of alternatives and likelihood second moments | [Chen, Li, and O'Donnell](#chen2022) | The statistical comparison method is standard; the proof evaluates it for disjoint blinded strips. |
| Classical data processing and comparison with order-two divergence | [van Erven and Harremoës](#vanerven2014); explicit log-sum and Jensen arguments in the proof | Established information inequalities connect a separable comparison output to Bell fidelity. |
| Readout mitigation and postselected dynamic circuits | [Koh et al.](#koh2026), [Smith et al.](#smith2026) | These motivate a precise distinction between delivered states, mitigated estimates, and success-conditioned outputs. |

The statement established here concerns the matched dependence on distance, detector information, and infidelity at fixed quantum-memory density and report bandwidth. The [information bound](../science/information_bound.md) applies to every adaptive protocol in the model. The [construction](../science/construction.md) supplies an explicit protocol with the same order of depth. The geometric lemma, Chernoff coefficient, amplification idea, and statistical inequalities do not individually carry a priority claim.

<a id="friedman2023"></a>
## Friedman, Yin, Hong, and Lucas: measurement-assisted locality

**Aaron J. Friedman, Chao Yin, Yifan Hong, and Andrew Lucas, “Locality and error correction in quantum dynamics with measurement.”** [arXiv:2206.09929v4](https://arxiv.org/abs/2206.09929v4), revised July 3, 2023; first submitted June 20, 2022. The locators below refer to this expanded version and its Supplemental Material.

Main-text Eq. (1) gives the measurement-region resource bound. The closest proof ingredients are SM Lemma 4, SM Proposition 6 in Sec. 6.5, and SM Theorem 5 with its adaptive extension in Sec. 6.7. The paragraph immediately before Proposition 6 explains why finite-support circuit light cones make the comparison exact. Equation (S149) constructs unnormalized separable reference states on selected adaptive trajectories. Main-text Sec. 4.7 covers weak measurements and other local channels.

The [blind-strip lemma](../science/blind_strip.md) uses the same cut geometry after unread outcomes have been summed into local trace-preserving maps. It needs a supplied separating strip, rather than an aggregate bound on all measurement regions. The additional task is to quantify imperfect access to reports with fixed local bandwidth. The cited geometric statements do not provide the uniform binary-symmetric-channel optimum proved here.

<a id="choe2024"></a>
## Choe and König: noisy quantum-bus converses

**Shin Ho Choe and Robert König, “Long-range data transmission in a fault-tolerant quantum bus architecture.”** *npj Quantum Information* **10**, 132 (2024). [Published article](https://doi.org/10.1038/s41534-024-00928-4), [published supplement](https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41534-024-00928-4/MediaObjects/41534_2024_928_MOESM1_ESM.pdf), [arXiv:2209.09774v1](https://arxiv.org/abs/2209.09774v1). Published December 26, 2024; the supplement is dated August 12, 2024.

The published supplement's Sec. 6.1 contains Corollary 6.1, Eq. (92), Theorem 6.2, and Lemma 6.3, Eqs. (94)–(95). Their arXiv counterparts are Sec. 8.1, Corollary 8.1, Theorem 8.2, and Lemma 8.3. The proof replaces inter-repeater gates by Bell resources and accumulates cuts whose resources are completely depolarized. Its theorem supplies a separable component under a suitable local stochastic quantum-noise model. Corollary 6.1 gives, in their notation, the restriction

```math
R\le\left(\frac{3}{4p_0^2}\right)^{\Delta m}
```

at the stated constant-fidelity threshold.

The quantifiers and noise location matter. Their fault-tolerant protocol must withstand arbitrary local stochastic noise, including preparation and gates. Here the specified iid errors corrupt classical reports, while coherent gates remain available. A single blinded spatial cut can therefore be crossed coherently; the present comparison needs width proportional to depth. It establishes a different resource law, without extending the present construction to noisy-gate fault tolerance.

### Comparison of the two noise models

| Resource or assumption | Quantum-bus setting above | Present report-only setting |
|---|---|---|
| Quantum storage at each position | Repeater size may grow with distance | Fixed number of qubits per site |
| Asymptotic resource | Primarily repeater size at constant depth | Operation depth at fixed spatial density |
| Noise in the converse | A suitable local stochastic quantum error within the allowed adversarial class | One prescribed iid BSC acting on reported bits |
| Quantum controls in the upper bound | Fault tolerance is part of the construction | Ideal coherent controls and storage |
| Separating obstruction | Loss of quantum entanglement across a repeater boundary | Reports blinded across a strip wider than the quantum cones |

<a id="danjou2021"></a>
## D'Anjou: the detector-information coefficient

**B. D'Anjou, “Generalized figure of merit for qubit readout.”** *Physical Review A* **103**, 042404 (2021). [Published article](https://doi.org/10.1103/PhysRevA.103.042404), [arXiv:2008.08630v3](https://arxiv.org/abs/2008.08630v3), revised April 2, 2021.

Equations (5)–(6) identify the asymptotic repeated-readout error exponent with classical Chernoff information. Appendix D.1, Eq. (D5), gives the symmetric binary expression

```math
C_b=-\frac12\log[4p(1-p)],
```

which is exactly this project's $`D(p)`$. The paper also treats analog confidence information and explains why single-shot assignment error alone does not characterize a general detector.

The present theorem uses the unflagged symmetric binary interface. It connects this established coefficient to a spatial Bell-preparation cost. It does not establish an equally sharp theorem for every analog or asymmetric readout channel.

<a id="chernoff1952"></a>
## Chernoff: exponential repetition bounds

**Herman Chernoff, “A measure of asymptotic efficiency for tests of a hypothesis based on the sum of observations.”** *The Annals of Mathematical Statistics* **23**(4), 493–507 (1952). [DOI](https://doi.org/10.1214/aoms/1177729330).

The construction uses the standard exponential-moment bound for a binomial majority error. It is derived explicitly in [construction.md](../science/construction.md), so the precise finite-sample convention, including ties, does not depend on an asymptotic citation. D'Anjou's Eqs. (5)–(6) and Appendix D identify the same discrimination exponent in repeated qubit readout. Majority decoding is a sufficient construction for the symmetric binary model; no claim of its optimality for arbitrary adaptive measurement devices is needed.

<a id="kim2025"></a>
## Kim, Yun, and Bae: measurement purification

**Jaemin Kim, Jiyoung Yun, and Joonwoo Bae, “Purification of noisy measurements and faithful distillation of entanglement.”** *Journal of Physics A: Mathematical and Theoretical* **58**(3), 03LT01 (2025). [DOI](https://doi.org/10.1088/1751-8121/ada0fa), [arXiv:2404.10538v3](https://arxiv.org/abs/2404.10538v3), revised January 7, 2025. The [authors' institutional record](https://pure.kaist.ac.kr/en/publications/purification-of-noisy-measurements-and-faithful-distillation-of-e/) identifies the journal article and issue year.

Section II and Eq. (4) of the inspected arXiv version use controlled operations to spread pointer information before noisy measurement. The protocol is applied to entanglement distillation. This establishes that measurement purification and its usefulness for entanglement predate the present construction. The depth theorem here additionally charges finite-range coherent propagation, local memory, and readout layers.

<a id="byrne2026"></a>
## Byrne, Linden, and Skrzypczyk: adaptive measurement processing

**James Byrne, Noah Linden, and Paul Skrzypczyk, “Reducing measurement error with adaptivity.”** [arXiv:2606.21283v2](https://arxiv.org/abs/2606.21283v2), revised August 21, 2026; first submitted June 19, 2026.

This work shows that adaptive circuits combining uses of a noisy measuring device can outperform nonadaptive measurement circuits and establishes limits for such processing. It concerns device-use resources without the spatial entanglement-distribution constraint imposed here. The present converse permits adaptive quantum processing and therefore cannot be justified by assuming every protocol repeats or independently decodes the construction's Bell bits. Its common noise-table channel handles that freedom directly.

<a id="repetition-readout"></a>
## Repetition encoding and repeated readout

**Jakob M. Günther, Francesco Tacchino, James R. Wootton, Ivano Tavernelli, and Panagiotis Kl. Barkoutsos, “Improving readout in quantum simulations with repetition codes.”** *Quantum Science and Technology* **7**, 015009 (2022). [DOI](https://doi.org/10.1088/2058-9565/ac3386), [arXiv:2105.13377v2](https://arxiv.org/abs/2105.13377v2), revised June 14, 2021. Section II.1, Eq. (1), encodes a basis label through CNOT gates and explicitly distinguishes that redundancy from cloning an unknown state.

**Rebecca Hicks, Bryce Kobrin, Christian W. Bauer, and Benjamin Nachman, “Active readout-error mitigation.”** *Physical Review A* **105**, 012419 (2022). [DOI](https://doi.org/10.1103/PhysRevA.105.012419), [arXiv:2108.12432v3](https://arxiv.org/abs/2108.12432v3), revised September 7, 2022. Section II of the [accepted manuscript](https://link.aps.org/accepted/10.1103/PhysRevA.105.012419) describes encoding immediately before measurement to improve individual reported outcomes. It is a physical encoding primitive, so the general distinction between delivered states and mitigated expectation values should not be used to dismiss it.

**Tobias Hartung, Stephan Schuster, Joachim von Zanthier, and Karl Jansen, “Real-time measurement error mitigation for one-way quantum computation.”** *Scientific Reports* (2026), published September 19, 2026. [DOI](https://doi.org/10.1038/s41598-026-70209-x), [arXiv:2411.09084v2](https://arxiv.org/abs/2411.09084v2), revised September 2, 2026. Sections 3–5 distinguish report errors from projection errors, analyze repeated readout when backaction permits it, and introduce a verification register with majority voting.

These works establish the amplification ingredients. The present [construction](../science/construction.md) additionally places the banks inside the fixed-density chain, reuses the Bell-link interiors, and charges their propagation and readout time. The matching [converse](../science/information_bound.md) addresses arbitrary adaptive protocols under the specified report interface; it is not supplied by the amplification primitive alone.

<a id="huang2026"></a>
## Huang: repetition-protected physical Bell generation

**He-Liang Huang, “Exponential measurement error mitigation in quantum sampling.”** *npj Unconventional Computing* **3**, 47 (2026). [Published article](https://doi.org/10.1038/s44335-026-00094-0), [publisher PDF](https://www.nature.com/articles/s44335-026-00094-0.pdf).

Figure 3 applies repetition encoding to measurements on a one-dimensional cluster chain used to generate an endpoint Bell pair. The Methods discussion, Eqs. (15)–(20), follows the measurement parities through physical feedforward corrections and evaluates the resulting Bell overlap. This is a direct application precedent for readout-protected Bell delivery, not only for correcting estimates of observables.

The inspected treatment varies the encoding size and includes faults in its encoding gates. It does not establish a minimum total preparation depth on the fixed-density line over all adaptive protocols. The present distinction is the local resource accounting and matched converse, including detector and accuracy dependence. Repetition-protecting Bell-generation records is therefore an inherited idea; the [depth theorem](../science/depth_law.md) does not claim priority for that application.

<a id="bergamaschi2025"></a>
## Bergamaschi and Liu: single-shot encoded entanglement

**Thiago Bergamaschi and Yunchao Liu, “On Fault Tolerant Single-Shot Logical State Preparation and Robust Long-Range Entanglement.”** *ITCS 2025*, LIPIcs **325**, 16:1–16:9. [Proceedings record](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ITCS.2025.16), [full manuscript, arXiv:2411.04405v1](https://arxiv.org/abs/2411.04405v1), submitted November 7, 2024.

The full manuscript's introduction and Theorem 1.1 give constant-depth preparation with one measurement round and feedforward for CSS quantum LDPC codes, using $`O(nT)`$ ancillas for an $`n`$-qubit code and their parameter $`T`$. Their $`T`$ controls the number of alternating-Tanner-graph layers; it is not the operation depth defined in this repository. Figure 1 and Section 3 describe the graph construction; the encoded GHZ application supplies robust long-range entanglement.

This is a spatial-resource distinction as well as an output distinction. A bounded-degree graph with growing ancillary layers is not automatically a fixed-width nearest-neighbor line. Conversely, physical Bell output alone is insufficient to separate the models: the [Choe–König bus](#choe2024) also delivers a physical pair with different repeater resources. The present result fixes local density and report bandwidth before optimizing depth.

<a id="waring2026"></a>
## Waring, Le Beux, and Pere: block fusion with redundant reports

**Jean-Baptiste Waring, Sébastien Le Beux, and Christophe Pere, “Robust GHZ State Preparation via Majority-Voted Boundary Measurements.”** [arXiv:2602.19405v3](https://arxiv.org/abs/2602.19405v3), revised May 4, 2026; first submitted February 23, 2026.

Sections III.A–III.B, Fig. 1, and Algorithm 2 partition a coupling graph, prepare local GHZ states in parallel, and fuse them using redundant boundary measurements with majority-voted feedforward. This is a close antecedent for the construction's block-fusion strategy. The present one-dimensional schedule accounts for the coherent propagation and repeated-readout time at fixed local storage. Its accompanying converse bounds arbitrary adaptive protocols, beyond the particular choice of blocks or majority decoding.

<a id="chen2022"></a>
## Chen, Li, and O'Donnell: statistical mixtures of alternatives

**Sitan Chen, Jerry Li, and Ryan O'Donnell, “Toward Instance-Optimal State Certification With Incoherent Measurements.”** *Proceedings of the 35th Conference on Learning Theory*, PMLR **178**, 2541–2596 (2022). [Proceedings record](https://proceedings.mlr.press/v178/chen22b.html), [published PDF](https://proceedings.mlr.press/v178/chen22b/chen22b.pdf), [arXiv:2102.13098v2](https://arxiv.org/abs/2102.13098v2).

Section 2.1 explains the established Ingster–Suslina approach: compare a null distribution with a mixture of alternatives, then bound their total variation through likelihood second moments. This is a methodological antecedent, not a Bell-distribution theorem. Here disjoint report blocks yield the elementary exact identity

```math
\chi^2\!\left(\frac1M\sum_{j=1}^M Q_j\middle\Vert P\right)
=\frac{e^{2kD(p)}-1}{M}.
```

The [information proof](../science/information_bound.md) derives it from independence of the noise variables. Its quantum input is that every $`Q_j`$ produces a separable endpoint state. The statistical mixture technique itself is not introduced by this project.

<a id="vanerven2014"></a>
## Classical information inequalities and order-two divergence

**Tim van Erven and Peter Harremoës, “Rényi Divergence and Kullback–Leibler Divergence.”** *IEEE Transactions on Information Theory* **60**(7), 3797–3820 (2014). [DOI](https://doi.org/10.1109/TIT.2014.2320500), [arXiv:1206.2459v2](https://arxiv.org/abs/1206.2459v2), revised April 24, 2014.

Theorem 3 of the inspected arXiv version states monotonicity in Rényi order. Its order-one and order-two specialization is

```math
D_{\mathrm{KL}}(Q\Vert P)
\le D_2(Q\Vert P)
=\log[1+\chi^2(Q\Vert P)].
```

The implemented [information proof](../science/information_bound.md) derives this comparison by Jensen's inequality. It obtains data processing from the classical log-sum inequality applied to the Bell-test kernel conditioned on a noise table. Quantum relative-entropy contraction is not required. The total-variation estimate and the two heralding comparisons use elementary Cauchy–Schwarz inequalities, also stated explicitly in the proof files. These established inequalities are mathematical ingredients of the resource theorem.

<a id="koh2026"></a>
## Koh, Koh, and Thompson: mitigation of feedforward readout errors

**Jin Ming Koh, Dax Enshan Koh, and Jayne Thompson, “Readout Error Mitigation for Mid-Circuit Measurements and Feedforward.”** *PRX Quantum* **7**, 010317 (2026). [Published article](https://doi.org/10.1103/cj89-4h5t), [arXiv:2406.07611v2](https://arxiv.org/abs/2406.07611v2), revised February 3, 2025.

This work develops mitigation for mid-circuit readout errors in feedforward circuits. The distinction relevant here is the output criterion: a mitigated expectation assembled over executions is not a physical endpoint density matrix with the stated Bell fidelity. The present theorem concerns delivered entanglement, including a success-conditioned version, rather than the sampling overhead of estimating ideal observables.

The same paper also benchmarks repeated physical readout: Sec. IV defines Rep-MAJ, which majority-decodes consecutive reports, and Rep-ALL, which accepts only unanimous reports. Section IV.2 and Fig. 5 interpolate between unitary and feedforward GHZ preparation by preparing local blocks and fusing them through measurements. These are direct antecedents for temporal repetition and block fusion in the present construction. Their finite hardware comparisons do not establish the uniform optimal-depth law in distance, detector quality, and target infidelity proved here.

<a id="smith2026"></a>
## Smith, Pokharel, Maurya, and Takita: error-detected dynamic circuits

**Kevin C. Smith, Bibek Pokharel, Satvik Maurya, and Maika Takita, “Resilience Beyond the Light Cone: Error-Detected Primitives for Practical Dynamic Circuits.”** [arXiv:2609.08925v1](https://arxiv.org/abs/2609.08925v1), submitted September 8, 2026.

The work trades infidelity for postselection overhead in dynamic-circuit primitives and demonstrates an entangled Bell pair across a 100-qubit chain. The [heralding theorem](../science/heralding.md) addresses an asymptotic resource question under the specified iid report channel: success probability must remain above a fixed positive constant while length and accuracy vary. It does not exclude finite-size improvements or protocols whose success probability vanishes with size. The experiment also includes hardware errors beyond the ideal coherent-control model of the matching construction.

## Scope of the comparison

The source identities and locators above support attribution to particular results. They do not constitute a guarantee that every relevant prior paper has been found. The resource theorem should be assessed through its explicit assumptions, finite bounds, and constructive match. Extensions to analog detectors, correlated report errors, nonzero gate noise, or finite-speed classical control need separate statements and proofs.

<a id="wilde2017"></a>
## Educational anchor

**Mark M. Wilde, *Quantum Information Theory*, second edition, Cambridge University Press (2017).** [Publisher's edition record](https://www.cambridge.org/core/books/quantum-information-theory/247A740E156416531AA8CB97DFDAE438), [DOI](https://doi.org/10.1017/9781316809976), [printed contents](https://assets.cambridge.org/97811071/76164/toc/9781107176164_toc.pdf).

Wilde is the single educational anchor for the [30-milestone map](../learning/MILESTONES.md). The [source bridge](../learning/WILDE_BRIDGE.md) gives the relevant readings and convention translations, using the publisher's 2017 section/page locators and explicitly labeled locators in the related [author draft, arXiv:1106.1445v8](https://arxiv.org/abs/1106.1445v8). The book supplies quantum-information foundations; the project-specific resource proofs and their research antecedents are identified separately in the scientific pages and the account above.
