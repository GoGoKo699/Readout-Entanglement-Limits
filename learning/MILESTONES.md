# Thirty milestones for readout-limited preparation

This map contains exactly thirty project-defined understanding targets. It develops the physical Bell-pair problem on a line and its two-dimensional toric-ground-space extension through one noisy-report interface. The single educational anchor is John Preskill, *Quantum Information*, Chapter 7, *Quantum Error Correction*, March 2026 author draft. The [source bridge](PRESKILL_BRIDGE.md#edition-and-source-map) identifies the source and section locators, translates conventions, and supplies the statistical and preparation-specific arguments absent from the chapter.

## Allocation and connected route

| Phase | Milestones | Local-to-global progression |
|---|---|---|
| Background/preliminaries | M01–M12 | Individual states and records, channels and local resources, detector information, then the complete two-task model. |
| Narrative/innovation | M13–M30 | Bell circuit and converse components, the uniform Bell law, then the buffered toric transfer, protected-root circuit, and global synthesis. |

The twelve background targets supply the quantum, geometric, and statistical language needed by both tasks. The eighteen narrative targets first assemble the established Bell result, then derive and match the toric extension through two independent proof routes. The map follows the project's dependencies rather than the textbook's table of contents. Each record contains a central question, an understanding target, dependencies and story role, a conceptual connection, and source pointers. The last target of each phase integrates that phase. Specialist proofs remain in the scientific account; these targets organize global understanding without claiming to cover every technical detail.

<a id="background-preliminaries"></a>
## Background/preliminaries: M01–M12

<a id="m01"></a>
### M01. Qubits and orthogonal pointer records

**Phase:** Background/preliminaries.

**Central question:** What can a local pointer store and copy?

**Understanding target:** Distinguish superpositions from orthogonal basis records, and explain why CNOT fanout of a pointer does not clone an arbitrary quantum state.

**Dependencies and story role:** No earlier milestone is required. Introduces data and record registers before assigning geometry.

**Conceptual connection:** Physical redundancy needs actual local registers.

**Source pointers:** Preskill §7.10; [states and records](PRESKILL_BRIDGE.md#states-records-and-local-channels); [pointer resources](../science/model.md#2-the-report-interface).

<a id="m02"></a>
### M02. Composite states and physical output

**Phase:** Background/preliminaries.

**Central question:** Which density operator is assessed at the end?

**Understanding target:** Explain partial trace, selection, and squared Bell overlap; distinguish a corrected physical state from an unapplied Pauli-frame description.

**Dependencies and story role:** Uses [M01](#m01). Connects individual registers into a quantum output task.

**Conceptual connection:** Discarding and conditioning need different proof operations.

**Source pointers:** Preskill §§7.3.2–7.3.3; [task conventions](PRESKILL_BRIDGE.md#conventions-and-physical-tasks); [physical Bell output](../science/model.md#3-classical-control-and-physical-output).

<a id="m03"></a>
### M03. Bell byproducts as check information

**Phase:** Background/preliminaries.

**Central question:** How do two local measurement bits determine a distant Bell correction?

**Understanding target:** Identify the phase and bit byproducts after CNOT/Hadamard decoding and explain how an incorrect estimate changes the actual Bell state.

**Dependencies and story role:** Uses [M01](#m01), [M02](#m02). Provides the smallest operational example of outcome-dependent preparation.

**Conceptual connection:** Commuting parity information specifies a correction.

**Source pointers:** Preskill §§7.7,7.10; [complete Bell example](PRESKILL_BRIDGE.md#a-complete-bell-pair-example); [byproducts](../science/construction.md#2-the-two-bell-byproducts).

<a id="m04"></a>
### M04. Instruments, true outcomes, and reports

**Phase:** Background/preliminaries.

**Central question:** Where is the noise placed in the measurement process?

**Understanding target:** Describe instrument branches and their trace-preserving sum; separate the true outcome and postmeasurement state from the public BSC report.

**Dependencies and story role:** Uses [M01](#m01), [M02](#m02). Defines what the controller can observe.

**Conceptual connection:** A correct quantum projection can have a wrong classical report.

**Source pointers:** Preskill §§7.2,7.3.2–7.3.3; [channels and records](PRESKILL_BRIDGE.md#states-records-and-local-channels); [report interface](../science/model.md#2-the-report-interface).

<a id="m05"></a>
### M05. Retained outcomes and local environments

**Phase:** Background/preliminaries.

**Central question:** How can a selected branch be analyzed without invalid trace-preserving cancellation?

**Understanding target:** Construct the CPTP outcome-register completion and explain why selection happens after the register is retained; distinguish this mathematical device from an available ideal readout.

**Dependencies and story role:** Uses [M02](#m02), [M04](#m04). Supplies the channel language used in both blind-region arguments.

**Conceptual connection:** An environment can preserve information without supplying it to a controller.

**Source pointers:** Preskill §§7.3.2–7.3.3; [retained records](PRESKILL_BRIDGE.md#states-records-and-local-channels); [outside-register completion](../science/blind_strip.md#2-retain-every-outside-outcome-register).

<a id="m06"></a>
### M06. Depth, range, and density

**Phase:** Background/preliminaries.

**Central question:** What local resources fit inside a depth-T causal neighborhood?

**Understanding target:** Explain disjoint support layers, range-limited backward cones, charged readouts, fixed quantum memory, and fixed report slots per site and layer.

**Dependencies and story role:** Uses [M01](#m01), [M04](#m04), [M05](#m05). Adds spatial and temporal cost to the local operations.

**Conceptual connection:** Spatial copies and repeated time are both bounded physical resources.

**Source pointers:** Preskill §§7.19–7.20 for geometric background; [local model](../science/model.md#1-sites-time-and-initial-resources); [toric model](../science/toric_extension.md#model-and-physical-target).

<a id="m07"></a>
### M07. Adaptive public control

**Phase:** Background/preliminaries.

**Central question:** How can a fixed-branch analysis coexist with instantaneous global classical feedforward?

**Understanding target:** Explain why fixing the complete public history fixes local choices, while neither that history nor a proof refinement exposes hidden true outcomes to the controller.

**Dependencies and story role:** Uses [M04](#m04), [M05](#m05), [M06](#m06). Joins classical control with quantum causal geometry.

**Conceptual connection:** Free classical communication does not create free coherent gates or ideal outcome access.

**Source pointers:** Preskill §§7.3.2–7.3.3 as channel background; [blind-strip history refinement](../science/blind_strip.md#1-refine-the-public-record-without-selecting-an-inside-outcome); [public control](../science/model.md#3-classical-control-and-physical-output).

<a id="m08"></a>
### M08. Independent unflagged readout

**Phase:** Background/preliminaries.

**Central question:** Which information is available from a binary symmetric detector?

**Understanding target:** Interpret crossover probability, bias, independent potential-slot flips, and the distinction between an unflagged BSC and a channel revealing hidden fair-report flags.

**Dependencies and story role:** Uses [M04](#m04), [M07](#m07). Specifies the local classical interface exactly.

**Conceptual connection:** An auxiliary noise decomposition cannot grant a receiving protocol extra records.

**Source pointers:** Preskill §§7.2,7.6 as error-model background; [interface conventions](PRESKILL_BRIDGE.md#conventions-and-physical-tasks); [BSC assumptions](../science/model.md#2-the-report-interface).

<a id="m09"></a>
### M09. Repetition and the Chernoff coefficient

**Phase:** Background/preliminaries.

**Central question:** How do space and repeated time improve a pointer estimate?

**Understanding target:** Use fair-tie majority error and its exponent D(p); explain inverse-square weak-bias cost and independence of the decoding error from the latent bit.

**Dependencies and story role:** Uses [M01](#m01), [M08](#m08). Turns detector uses into quantitative reliability.

**Conceptual connection:** The same classical coefficient enters both constructions and statistical converses.

**Source pointers:** Preskill §7.6 for repetition background; [supplied statistical derivation](PRESKILL_BRIDGE.md#spatial-copies-and-repeated-readout); [exact decoding](../science/construction.md#3-decoding-and-exact-output-fidelity).

<a id="m10"></a>
### M10. Statistical alternatives and common algorithms

**Phase:** Background/preliminaries.

**Central question:** What does comparing one algorithm under different noise laws establish?

**Understanding target:** Explain a common flip-table channel, likelihood ratios, unknown alternative locations, and why a binary physical-output test cannot improve distinguishability.

**Dependencies and story role:** Uses [M05](#m05), [M07](#m07), [M08](#m08), [M09](#m09). Builds the statistical prerequisite for a universal converse.

**Conceptual connection:** The proof varies the detector law while preserving the adaptive algorithm.

**Source pointers:** Preskill §§7.3.2–7.3.3 as channel background; [local statistical bridge](PRESKILL_BRIDGE.md#a-common-statistical-comparison); [information proof](../science/information_bound.md).

<a id="m11"></a>
### M11. Stabilizers, toric checks, and string boundaries

**Phase:** Background/preliminaries.

**Central question:** Which physical defects does a toric Z string change?

**Understanding target:** Define stars, plaquettes, even total star parity, logical labels, and boundary syndrome; distinguish physical ground-space weight from later logical recoverability.

**Dependencies and story role:** Uses [M01](#m01), [M02](#m02), [M03](#m03). Adds the second output task using code language.

**Conceptual connection:** The Bell byproduct and toric syndrome are both check information but have different success criteria.

**Source pointers:** Preskill §§7.7,7.10,7.18.1,7.18.3; [toric syndrome bridge](PRESKILL_BRIDGE.md#toric-syndromes-and-physical-ground-space-weight); [toric target](../science/toric_extension.md#model-and-physical-target).

<a id="m12"></a>
### M12. The complete preparation-resource setting

**Phase:** Background/preliminaries.

**Central question:** Which assumptions must be fixed before comparing the two tasks?

**Understanding target:** Assemble product initialization, shared randomness, local channels, fixed density, noisy public information, actual corrections, and the two different physical targets into one coherent model comparison.

**Dependencies and story role:** Uses [M02](#m02), [M05](#m05), [M06](#m06), [M07](#m07), [M08](#m08), [M10](#m10), [M11](#m11). Integrates the background phase from local objects to global operational tasks.

**Conceptual connection:** The same detector interface can constrain distinct quantum outputs without equating their observables or parameter scopes.

**Source pointers:** Preskill §§7.3.2–7.3.3,7.10,7.18; [conventions](PRESKILL_BRIDGE.md#conventions-and-physical-tasks); [Bell model](../science/model.md); [toric model](../science/toric_extension.md#model-and-physical-target).

<a id="narrative-innovation"></a>
## Narrative/innovation: M13–M30

<a id="m13"></a>
### M13. Local Bell links

**Phase:** Narrative/innovation.

**Central question:** How does a block supply a long Bell link without uncounted quantum propagation?

**Understanding target:** Explain central Bell preparation and outward swaps, freed local qubits, unequal blocks, and the O(b) depth needed before link fusion.

**Dependencies and story role:** Uses [M03](#m03), [M06](#m06), [M12](#m12). Starts the research narrative with one physical circuit component.

**Conceptual connection:** The lower-depth global protocol still pays local propagation within each block.

**Source pointers:** Preskill §7.10 as circuit/check background; [construction bridge](PRESKILL_BRIDGE.md#spatial-copies-and-repeated-readout); [local links](../science/construction.md#1-equal-blocks-and-layer-conventions).

<a id="m14"></a>
### M14. Fusion and final Bell parities

**Phase:** Narrative/innovation.

**Central question:** Which measurement bits matter to the physical endpoint correction?

**Understanding target:** Derive the two accumulated Bell byproduct parities and explain both uniform latent outcomes and cancellation of some individual decoding errors.

**Dependencies and story role:** Uses [M03](#m03), [M07](#m07), [M13](#m13). Connects local links into the global endpoint state.

**Conceptual connection:** The success criterion depends on final physical byproducts rather than the correctness of every internal estimate.

**Source pointers:** Preskill §§7.7,7.10; [Bell example](PRESKILL_BRIDGE.md#a-complete-bell-pair-example); [byproduct proof](../science/construction.md#2-the-two-bell-byproducts).

<a id="m15"></a>
### M15. Protected Bell pointer reports

**Phase:** Narrative/innovation.

**Central question:** How is reliable endpoint correction implemented at fixed density?

**Understanding target:** Combine counted local pointer copying and repeatable readout, compute exact Bell parity fidelity, and identify the O(b+t) circuit depth and Θ(bt) reports per pointer.

**Dependencies and story role:** Uses [M09](#m09), [M13](#m13), [M14](#m14). Completes the constructive Bell mechanism.

**Conceptual connection:** Orthogonal redundancy and temporal repetition jointly protect the required classical information.

**Source pointers:** Preskill §§7.6,7.10; [protected reports](PRESKILL_BRIDGE.md#spatial-copies-and-repeated-readout); [construction fidelity](../science/construction.md#3-decoding-and-exact-output-fidelity).

<a id="m16"></a>
### M16. Blind-strip separability

**Phase:** Narrative/innovation.

**Central question:** Why can one sufficiently wide blind strip prevent Bell entanglement?

**Understanding target:** Reconstruct retained-outside-register completion, disjoint endpoint histories before selection, and the positive product-branch sum giving Bell fidelity at most one half.

**Dependencies and story role:** Uses [M05](#m05), [M06](#m06), [M07](#m07), [M12](#m12). Establishes the quantum step of the Bell converse.

**Conceptual connection:** The proof isolates an inaccessible region without cutting valid coherent wires by assumption.

**Source pointers:** Preskill §§7.3.2–7.3.3; [blind-strip bridge](PRESKILL_BRIDGE.md#why-an-unread-strip-obstructs-bell-delivery); [full lemma](../science/blind_strip.md).

<a id="m17"></a>
### M17. Unknown blind locations

**Phase:** Narrative/innovation.

**Central question:** Why must a high-fidelity output distinguish a mixture of localized detector alternatives?

**Understanding target:** Explain strip packing, k=O(T²), M=Θ(L/T), and the exact diluted likelihood second moment; keep the hidden location inaccessible.

**Dependencies and story role:** Uses [M10](#m10), [M16](#m16). Adds the statistical step to the quantum obstruction.

**Conceptual connection:** Local unread regions become a universal information requirement without assuming bitwise decoding.

**Source pointers:** Preskill channel background; [statistical bridge](PRESKILL_BRIDGE.md#a-common-statistical-comparison); [random-strip bound](../science/information_bound.md).

<a id="m18"></a>
### M18. The uniform Bell depth law

**Phase:** Narrative/innovation.

**Central question:** How are converse, construction, floor, and coherent cap matched?

**Understanding target:** Explain D(p)τ²=log[L/(ετ)] and the max-one/min-linear depth law, including integer blocks and the reason τ remains inside the logarithm when p varies.

**Dependencies and story role:** Uses [M09](#m09), [M15](#m15), [M17](#m17). Combines the Bell mechanisms into the full deterministic theorem.

**Conceptual connection:** Reliability and the number of required regions jointly determine the implicit optimum.

**Source pointers:** Preskill error-model background; [complete Bell law](PRESKILL_BRIDGE.md#the-complete-one-dimensional-law); [uniform proof](../science/depth_law.md).

<a id="m19"></a>
### M19. Accuracy and public success

**Phase:** Narrative/innovation.

**Central question:** What extra work is needed when successful runs are selected?

**Understanding target:** Separate success probability from conditional Bell fidelity, explain unnormalized accepted operators, and identify why a fixed positive success requirement preserves the one-dimensional depth order.

**Dependencies and story role:** Uses [M02](#m02), [M07](#m07), [M10](#m10), [M16](#m16), [M18](#m18). Adds the proved success convention rather than extrapolating deterministic fidelity.

**Conceptual connection:** A postselected state and its yield must be controlled together.

**Source pointers:** Preskill §§7.3.2–7.3.3; [heralding account](../science/heralding.md); [scope](../science/model.md#3-classical-control-and-physical-output).

<a id="m20"></a>
### M20. Meaning of the Bell result

**Phase:** Narrative/innovation.

**Central question:** What does square-root-logarithmic operation depth physically measure?

**Understanding target:** Explain fixed-detector scaling, weak-bias crossover, targets above the separable threshold, ideal coherent operations, and free classical latency within the original theorem.

**Dependencies and story role:** Uses [M12](#m12), [M18](#m18), [M19](#m19). Integrates the first task before extending its proof mechanism.

**Conceptual connection:** A physical-output resource law is distinct from error mitigation or hardware wall-clock latency.

**Source pointers:** Preskill §7.2 for noise background; [interpretation](../science/interpretation.md); [fixed-fidelity theorem](../science/depth_law.md#every-fixed-target-above-the-separable-threshold).

<a id="m21"></a>
### M21. The local toric two-loop test

**Phase:** Narrative/innovation.

**Central question:** Which local code identities replace Bell separability in two dimensions?

**Understanding target:** Define the commuting projector K from a closed X loop and two alternative open Z strings; explain how its range supplies the inherited braiding identities and a 16/17 local-channel overlap bound.

**Dependencies and story role:** Uses [M05](#m05), [M06](#m06), [M11](#m11), [M12](#m12). Introduces the new receiving-task obstruction.

**Conceptual connection:** A receiving target needs its own valid local observable; Bell separability cannot simply be relabeled.

**Source pointers:** Preskill §§7.10,7.14,7.18; [two-loop account](../science/toric_extension.md#buffered-blindness-and-outside-records); [proof home](https://github.com/GoGoKo699/Topological-Communication-Cost/blob/c9aca22ecd2489da883de8a0c2b91e696f837213/science/noisy-readout.md).

<a id="m22"></a>
### M22. Buffering before outside conditioning

**Phase:** Narrative/innovation.

**Central question:** Why is the toric core smaller than the region whose reports are blinded?

**Understanding target:** Explain the >2rT separation, retained outside instrument registers and other test outputs, and factorization before selecting any outside outcomes.

**Dependencies and story role:** Uses [M05](#m05), [M07](#m07), [M16](#m16), [M21](#m21). Transfers the valid proof order to the new geometry.

**Conceptual connection:** Outside postselection must remain represented until disjoint quantum histories have been established.

**Source pointers:** Preskill §§7.3.2–7.3.3,7.14; [buffered proof route](../science/toric_extension.md#buffered-blindness-and-outside-records).

<a id="m23"></a>
### M23. Many blind cores without marginal independence

**Phase:** Narrative/innovation.

**Central question:** How can local overlap deficits accumulate in an adaptive global state?

**Understanding target:** Apply the per-core trace inequality after other-core tests, distinguish sequential conditioning from independent final marginals, and explain why hidden fair-report patterns remain analysis variables.

**Dependencies and story role:** Uses [M08](#m08), [M21](#m21), [M22](#m22). Turns one local obstruction into a global ground-space bound.

**Conceptual connection:** Commuting physical tests and buffered retained histories justify multiplication.

**Source pointers:** Preskill §§7.10,7.14; [simultaneous-core proof route](../science/toric_extension.md#buffered-blindness-and-outside-records); [finite bound](../science/toric_extension.md#fixed-detector-theorem-and-finite-bounds).

<a id="m24"></a>
### M24. The two-dimensional depth lower bound

**Phase:** Narrative/innovation.

**Central question:** What follows from the number and spacetime volume of blind blocks?

**Understanding target:** Explain M=floor[L/(36(rT+1))]², k=1296ν(rT+1)²T, and F_TC≤[1−(2p)^k/17]^M; infer the fixed-p cube-root-log lower bound without claiming a uniform crossover.

**Dependencies and story role:** Uses [M06](#m06), [M08](#m08), [M10](#m10), [M23](#m23). Extracts a resource consequence from the new geometric proof.

**Conceptual connection:** The O(T³) slot count and Θ(L²/T²) possible obstructions are separate ingredients.

**Source pointers:** Preskill geometric background; [finite toric bounds](../science/toric_extension.md#fixed-detector-theorem-and-finite-bounds).

<a id="m25"></a>
### M25. Actual star syndrome pointers

**Phase:** Narrative/innovation.

**Central question:** What quantum state exists before any noisy toric report?

**Understanding target:** Explain coherent star extraction, local pointer dephasing, the uniform-even cq syndrome state, and the canonical identity Z(E)ψ_z=ψ_(z⊕∂E).

**Dependencies and story role:** Uses [M04](#m04), [M05](#m05), [M11](#m11), [M12](#m12). Begins the independent toric upper construction.

**Conceptual connection:** A pointer must record the actual data defect before the report channel corrupts its public description.

**Source pointers:** Preskill §§7.7,7.10,7.18; [compression account](../science/toric_extension.md#compression-before-noisy-reporting); [worked path](PRESKILL_BRIDGE.md#toric-syndromes-and-physical-ground-space-weight).

<a id="m26"></a>
### M26. Constant-memory physical syndrome compression

**Phase:** Narrative/innovation.

**Central question:** How can raw syndrome information be removed without noiseless controller access?

**Understanding target:** Follow child-to-parent pointer CNOT, pointer-controlled physical Z, and child reset; verify the pointer/data invariant and explain why only one actual root defect remains per block.

**Dependencies and story role:** Uses [M05](#m05), [M06](#m06), [M25](#m25). Builds the local defect-removal mechanism.

**Conceptual connection:** Discarded raw information can remain in local environments while the data is physically corrected.

**Source pointers:** Preskill §§7.3.2–7.3.3,7.10,7.18; [compression mechanism](../science/toric_extension.md#compression-before-noisy-reporting).

<a id="m27"></a>
### M27. Area-sized protected root readout

**Phase:** Narrative/innovation.

**Central question:** How are Θ(b²t) reports supplied with only one pointer per toric cell?

**Understanding target:** Explain freeing pointer registers, local fanout in O(b) depth, t QND repetitions, fixed report density, and why XORing already noisy raw reports does not implement this channel.

**Dependencies and story role:** Uses [M01](#m01), [M06](#m06), [M09](#m09), [M26](#m26). Connects compression to reliable public information.

**Conceptual connection:** Fixed-density two-dimensional area and repeated time supply a cubic report budget.

**Source pointers:** Preskill §§7.6,7.10; [protected root pointers](PRESKILL_BRIDGE.md#protected-toric-root-pointers); [toric readout](../science/toric_extension.md#protected-pointers-and-the-actual-corrected-output).

<a id="m28"></a>
### M28. Unconditional toric physical overlap

**Phase:** Narrative/innovation.

**Central question:** When does the actually corrected toric output lie in the ground space?

**Understanding target:** Decode B−1 roots, infer the last by even parity, physically apply the estimated Z correction, and derive F_TC=∏[1−e_(a_jt)]; distinguish this from Bell parity cancellation and logical recoverability.

**Dependencies and story role:** Uses [M02](#m02), [M11](#m11), [M14](#m14), [M26](#m26), [M27](#m27). Completes the upper construction under the requested physical criterion.

**Conceptual connection:** An even pattern of residual defects still fails the global ground-space projector.

**Source pointers:** Preskill §§7.10.4,7.18.3; [exact overlap](../science/toric_extension.md#protected-pointers-and-the-actual-corrected-output).

<a id="m29"></a>
### M29. Matching the toric law and checking its scope

**Phase:** Narrative/innovation.

**Central question:** What is proved when the two independent toric arguments are combined?

**Understanding target:** Match the fixed-p lower bound to b≈t≈(log L)^(1/3), account for q=3 and all charged layers, identify what finite circuit checks establish, and separate unproved uniform, heralded, and noisy-gate extensions.

**Dependencies and story role:** Uses [M20](#m20), [M24](#m24), [M28](#m28). Combines the new construction and converse into a bounded theorem.

**Conceptual connection:** A complete supported match needs both valid transfer and fully counted physical achievability.

**Source pointers:** Preskill §§7.19–7.20 for background boundaries; [toric theorem](../science/toric_extension.md#fixed-detector-theorem-and-finite-bounds); [verification](../verification/README.md); [comparison](../references/RELATED_WORK.md#toric-report-noise-extension).

<a id="m30"></a>
### M30. One information mechanism, two physical tasks

**Phase:** Narrative/innovation.

**Central question:** What does the complete scientific account establish across the line and torus?

**Understanding target:** Explain shared report protection and retained-record proof discipline, the different output tests and geometric counts, exact inherited ownership, and the difference between the uniform Bell theorem and fixed-detector toric theorem.

**Dependencies and story role:** Uses [M12](#m12), [M18](#m18), [M19](#m19), [M20](#m20), [M21](#m21), [M22](#m22), [M23](#m23), [M24](#m24), [M25](#m25), [M26](#m26), [M27](#m27), [M28](#m28), [M29](#m29). Integrates the narrative phase from local quantum records to both global preparation laws.

**Conceptual connection:** The interaction adds a valid geometric extension while preserving the operational and parameter boundaries of each task.

**Source pointers:** Preskill §§7.3.2–7.3.3,7.10,7.14,7.18; [task synthesis](PRESKILL_BRIDGE.md#what-the-two-tasks-share); [interpretation](../science/interpretation.md); [ownership](../science/toric_extension.md#ownership-and-limits-of-the-connection).
