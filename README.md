# Readout Entanglement Limits

**How much local operation depth is needed to distribute a Bell pair when every measurement report is noisy?** This repository gives matching lower and upper bounds for a one-dimensional chain with fixed local resources, independent binary readout errors, and unrestricted ideal classical feedforward.

The target is a physically corrected Bell pair between fixed endpoints. Using measurements to reduce the depth below coherent propagation requires sufficiently reliable information about local outcomes, even when the classical controller can communicate across the whole chain instantaneously. The complete scientific account is organized by topic under [science/](science/model.md).

A [joint extension with Topological Communication Cost](science/toric_extension.md) establishes preparation depth $`\Theta_{p,F_0}((\log L)^{1/3})`$ for unconditional physical toric-code ground-space overlap in two dimensions, for fixed $`p\in(0,1/2)`$ and fixed target $`F_0\in(0,1)`$. It allows ideal local operations with two data qubits and one reusable pointer per cell, and free global classical feedforward. A buffered two-loop blind-core bound matches constant-memory syndrome compression and protected root readout. The [companion proof account](https://github.com/GoGoKo699/Topological-Communication-Cost/blob/771934f46773adb81138ced09c3d8e356fca035f/science/noisy-readout.md) owns the detailed shared derivation. The one-dimensional uniform Bell theorem below retains its stated parameter and success scope.

## Principal result

Let $`L\ge2`$ be the endpoint distance, $`p\in(0,1/2)`$ the independent report-flip probability, and $`\epsilon\in(0,1/4]`$ the target Bell infidelity. Define

```math
D(p)=-\frac12\log[4p(1-p)],
\qquad
D(p)\tau^2=\log\frac{L}{\epsilon\tau}.
```

The second equation has a unique positive solution. The minimum depth satisfies

```math
T_{\mathrm{opt}}(L,\epsilon,p)
=\Theta\!\left(\max\{1,\min\{L,\tau\}\}\right).
```

The constants are independent of distance, detector quality, and accuracy. The same order holds for heralded preparation whose success probability has a fixed positive lower bound. The [model](science/model.md) states the complete quantifiers, and the [depth-law proof](science/depth_law.md) supplies the finite bounds, uniform constants, integer rounding, and limiting regimes.

| Result | Scientific meaning | Account |
|---|---|---|
| At fixed detector quality and any fixed target $`F_0\in(1/2,1)`$, $`T_{\mathrm{opt}}=\Theta_{p,F_0}(\sqrt{\log L})`$ | Both spatial copies and repeated readout contribute to reliability, including targets below $`3/4`$. | [Construction](science/construction.md), [fixed-fidelity corollary](science/depth_law.md#every-fixed-target-above-the-separable-threshold) |
| In the intermediate regime, $`D(p)T^2\asymp\log[L/(T\epsilon)]`$ | A depth-$`T`$ neighborhood supplies order $`T^2`$ reports, while order $`L/T`$ neighborhoods must be connected. | [Information bound](science/information_bound.md), [interpretation](science/interpretation.md) |
| At fixed accuracy near uninformative readout, sublinear depth occurs precisely when $`(1-2p)L\to\infty`$ | The weak-detector crossover follows from the uniform law. | [Depth law](science/depth_law.md) |
| A fixed success requirement preserves the same depth order | Postselection can change constants without removing the distance or accuracy cost. | [Heralding](science/heralding.md) |

The universal converse allows arbitrary adaptive protocols in the stated model. It does not assume a particular swapping circuit, bitwise decoder, or majority rule. The matching upper bound is an explicit local circuit.

## Read the science

| Reader's question | Authoritative page |
|---|---|
| What exactly is the physical task, noise interface, and theorem? | [Model and main theorem](science/model.md) |
| Why does replacing one strip's reports by fair bits force separability? | [Blind-strip lemma](science/blind_strip.md) |
| How does the detector-information coefficient enter the lower bound? | [Random-strip information comparison](science/information_bound.md) |
| How are conditional accuracy and success probability controlled together? | [Heralded preparation](science/heralding.md) |
| Which gates, memories, reports, and corrections attain the bound? | [Local construction](science/construction.md) |
| How are the lower and upper bounds matched uniformly? | [Optimal depth and crossover](science/depth_law.md) |
| What does the result imply for measurement-assisted entanglement? | [Physical interpretation](science/interpretation.md) |
| How does the proof mechanism extend to a physical toric ground state in 2D? | [Toric report-noise extension](science/toric_extension.md) |
| Which ingredients and nearby results come from prior work? | [Related work](references/RELATED_WORK.md), [bibliography](references/references.bib) |

For the connected argument, read the model, the blind-strip and information bounds, heralding, the construction, and the depth law, then the interpretation. For a circuit-first route, follow the model with the construction before returning to the converse. The [LLM guide](llms.txt) maps more specific questions to these files.

## Study the project

The single educational anchor is **John Preskill, *Quantum Information*, Chapter 7, *Quantum Error Correction*, March 2026 author draft**. The [Preskill bridge](learning/PRESKILL_BRIDGE.md) gives selective verified section locators, explains states and records, and supplies the report-noise statistics and preparation arguments developed specifically for these tasks. A four-site Bell example and a local toric syndrome example make the physical corrections concrete.

The [30-milestone map](learning/MILESTONES.md) connects local records to both global preparation laws. Twelve background milestones assemble states, instruments, locality, detector information, and stabilizer language. Eighteen narrative milestones develop the Bell theorem before the toric transfer and its independent construction.

| Phase | Route | Understanding developed |
|---|---|---|
| Background/preliminaries | [M01–M12](learning/MILESTONES.md#background-preliminaries) | Local physical records, composite resources, statistical comparisons, and the complete two-task model |
| Narrative/innovation | [M13–M20](learning/MILESTONES.md#m13) | Protected Bell reports, blind-strip separability, uniform accuracy and success bounds |
| Narrative/innovation | [M21–M30](learning/MILESTONES.md#m21) | Buffered two-loop tests, actual syndrome compression, physical toric overlap, and joint scope |

The bridge uses one educational source. Primary research attribution remains in the scientific pages and [related-work account](references/RELATED_WORK.md).

## Verify the construction

From the repository root, using Python 3.12:

```sh
python3 -m pip install -r verification/requirements.txt
python3 verification/check.py
```

This command runs two complementary audits and reports `"status": "PASS"` only when both succeed. A dense state-vector engine checks the twelve-qubit Bell circuit and every true outcome branch. A separate sparse engine checks additional layouts, noisy corrections, exact operation counts, compiled gates, and finite choices of the uniform construction parameters. The [verification guide](verification/README.md) records the cases, requirements and tolerances.

These finite calculations check implementation consistency. The general converse, arbitrary-size construction, and asymptotic depth law rest on the written analytical arguments.

## Consequential assumptions

The input is a product over sites, conditional on any shared classical randomness. Quantum memory per site, gate range, and binary reports per site and layer are fixed. All measurement information entering the controller passes through independent, **unflagged** binary symmetric report channels. Coherent local pointers remain quantum resources and obey the local propagation and memory limits.

The matching construction assumes ideal coherent gates, memories, and repeatable pointer readout. Depth counts gate and readout layers under instantaneous classical communication; it does not model geographic communication latency. The heralded theorem holds at a fixed positive success requirement. These assumptions and their role in the proofs are specified in the [model](science/model.md) and [interpretation](science/interpretation.md).

## Purpose and contact

The project is currently under collaboration, and the manuscript is being written. For questions, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).

[License](LICENSE) · [Source provenance](references/PROVENANCE.md)
