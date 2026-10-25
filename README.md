# Readout Entanglement Limits

**How much local operation depth is needed to distribute a Bell pair when every measurement report is noisy?** This repository gives matching lower and upper bounds for a one-dimensional chain with fixed local resources, independent binary readout errors, and unrestricted ideal classical feedforward.

The target is a physically corrected Bell pair between fixed endpoints. Using measurements to reduce the depth below coherent propagation requires sufficiently reliable information about local outcomes, even when the classical controller can communicate across the whole chain instantaneously. The complete scientific account is organized by topic under [science/](science/model.md).

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
| Which ingredients and nearby results come from prior work? | [Related work](references/RELATED_WORK.md), [bibliography](references/references.bib) |

For the connected argument, read the model, the blind-strip and information bounds, heralding, the construction, and the depth law, then the interpretation. For a circuit-first route, follow the model with the construction before returning to the converse. The [LLM guide](llms.txt) maps more specific questions to these files.

## Study the project

The single educational anchor is **Mark M. Wilde, *Quantum Information Theory*, second edition (2017)**. The [Wilde bridge](learning/WILDE_BRIDGE.md) gives selective source readings, translates the book's conventions, and connects them to the project's arguments. Its four-qubit example explains noisy reports and physical correction; an eight-qubit example combines spatial copies, repeated readout and fair-tie majority decoding.

The [30-milestone map](learning/MILESTONES.md) organizes the understanding route for every reader, including LLMs. Fourteen background milestones connect quantum states, instruments, and locality with the required classical statistics. Sixteen research milestones assemble the construction and blind-strip mechanism into the global resource law.

| Phase | Route | Understanding developed |
|---|---|---|
| Background/preliminaries | [M01–M14](learning/MILESTONES.md#background-preliminaries) | Physical registers and measurement records, local quantum control, independent readout errors, and statistical comparison |
| Narrative/innovation | [M15–M21](learning/MILESTONES.md#m15) | The Bell circuit, reliable pointer reports, and the separability mechanism inside a blind strip |
| Narrative/innovation | [M22–M30](learning/MILESTONES.md#m22) | The common adaptive comparison, accuracy and heralding bounds, uniform optimum, crossover, and physical interpretation |

Use the listed Wilde sections alongside the bridge and milestone explanations. Each milestone points to the authoritative scientific statements and proofs; the source bridge identifies the steps developed specifically for this project.

## Reproduce the finite construction checks

From the repository root, using Python 3.12:

```sh
python3 -m pip install -r verification/requirements.txt
python3 verification/verify_bell_layout.py
python3 verification/verify_construction.py
```

The first deterministic state-vector check examines a twelve-qubit circuit with three blocks, two swapping boundaries, and all sixteen true Bell-outcome strings. The second checks additional even and odd block layouts, arbitrary-length partitions, native and CNOT-compiled schedules, exact operation counts, physical output fidelity under noisy reports, and finite choices of the uniform construction parameters. It also verifies the bridge's eight-qubit example. Success is reported as `"passed": true` by the original check and `"status": "PASS"` by the extension; the [verification guide](verification/README.md) specifies their fixed cases and tolerances.

The verification guide records the executed environment and exact scope. These finite calculations check implementation consistency. The general converse, arbitrary-size construction, and asymptotic depth law rest on the written analytical arguments.

## Consequential assumptions

The input is a product over sites, conditional on any shared classical randomness. Quantum memory per site, gate range, and binary reports per site and layer are fixed. All measurement information entering the controller passes through independent, **unflagged** binary symmetric report channels. Coherent local pointers remain quantum resources and obey the local propagation and memory limits.

The matching construction assumes ideal coherent gates, memories, and repeatable pointer readout. Depth counts gate and readout layers under instantaneous classical communication; it does not model geographic communication latency. The heralded theorem holds at a fixed positive success requirement. These assumptions and their role in the proofs are specified in the [model](science/model.md) and [interpretation](science/interpretation.md).

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
