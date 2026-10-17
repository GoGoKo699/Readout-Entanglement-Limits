# Thirty milestones for readout-limited entanglement

This map organizes the project into exactly thirty understanding targets. It follows the scientific dependencies from individual quantum records to a uniform bound on distant Bell-pair preparation. The targets are defined by the project and remain the same for every reader.

The single educational anchor is Mark M. Wilde, *Quantum Information Theory*, second edition (2017). The [Wilde bridge](WILDE_BRIDGE.md#edition-and-access) identifies the edition and access routes. Its [selective section map](WILDE_BRIDGE.md#selective-section-map) verifies the locators used below, and its [notation guide](WILDE_BRIDGE.md#notation-and-assumptions) translates the book's conventions. The textbook supplies foundations in states, instruments, resources, and statistical distinguishability. The canonical project pages supply the local circuit geometry, the particular statistical comparison, and the matched depth theorem. [Primary research attribution](../references/RELATED_WORK.md#ingredients-and-their-roles) remains separate from the educational anchor.

## Allocation and connected route

| Phase | Milestones | Progression |
|---|---|---|
| Background/preliminaries | M01–M14 | Local states and records, composite resources, adaptive local operations, statistical information, then the complete physical task. |
| Narrative/innovation | M15–M30 | Circuit and blind-strip components, a common statistical comparison, finite accuracy and success bounds, then the uniform resource law and its meaning. |

The fourteen background milestones reflect the project's connection between quantum instruments and locality on one side, and classical statistical information on the other. Neither set of prerequisites alone explains the converse. The sixteen narrative milestones develop the two concrete mechanisms before combining them: M15–M18 account for a finite construction, M19–M21 establish the blind-strip obstruction, and M22–M30 assemble the universal comparison and its consequences.

Each entry records a central question, an understanding target, its dependencies and role, the conceptual connection, and source pointers. Dependencies refer only to earlier milestones. The final milestone of each phase integrates that phase. Detailed calculations remain in the linked scientific account; these thirty targets organize global understanding rather than enumerating every lemma or neighboring subject.

<a id="background-preliminaries"></a>
## Background/preliminaries: M01–M14

<a id="m01"></a>
### M01. Qubit states and basis records

**Phase:** Background/preliminaries.

**Central question:** What is the difference between a qubit state and a record of a known computational-basis value?

**Understanding target:** Distinguish a superposition, a statistical mixture, and an orthogonal basis record. Explain why a controlled gate can copy the alternatives $`|0\rangle`$ and $`|1\rangle`$ into an initialized register without supplying a universal copier for unknown quantum states.

**Dependencies and story role:** No earlier milestone is required. This introduces the smallest physical objects later used as data qubits, Bell-pair halves, and readout pointers.

**Conceptual connection:** The construction's redundancy comes from copying a basis record. Its resource accounting depends on what that record physically occupies and how it is moved.

**Source pointers:** Wilde §§3.2–3.3 and 4.1 through [states and records](WILDE_BRIDGE.md#states-records-and-instruments); [local quantum resources](../science/model.md#1-sites-time-and-initial-resources); [pointer-copying implementation](../science/construction.md#1-equal-blocks-and-layer-conventions).

<a id="m02"></a>
### M02. Composite registers and reduced states

**Phase:** Background/preliminaries.

**Central question:** How is the state of the two output qubits obtained from a circuit containing many other registers?

**Understanding target:** Interpret tensor products, joint density operators, and partial traces. Distinguish discarding a register from conditioning on one of its measurement outcomes, and recognize that these operations can produce different endpoint states.

**Dependencies and story role:** Uses [M01](#m01). It connects individual qubits into the register description needed for both the circuit and the converse.

**Conceptual connection:** The task concerns the reduced physical endpoint state after all corrections. The blind-strip proof must keep selected records long enough to justify which other systems can be discarded.

**Source pointers:** Wilde §§3.5 and 4.3 through [the section map](WILDE_BRIDGE.md#selective-section-map); [physical output convention](../science/model.md#3-classical-control-and-physical-output); [retained outside registers](../science/blind_strip.md#2-retain-every-outside-outcome-register).

<a id="m03"></a>
### M03. Bell states and physical fidelity

**Phase:** Background/preliminaries.

**Central question:** What property of the final endpoint state counts as successful entanglement delivery?

**Understanding target:** Identify the target Bell projector and interpret $`F=\mathrm{Tr}(\Pi\rho_{AB})`$ as its squared overlap with the output state. Distinguish a high-fidelity physical state from a classical Pauli-frame record or an estimator of ideal observables. Recognize that the project's fidelity convention agrees with Wilde's squared convention.

**Dependencies and story role:** Uses [M01](#m01) and [M02](#m02). It fixes the output criterion before discussing the operations that produce or bound it.

**Conceptual connection:** The same Bell projector evaluates the construction and later separates the actual output from a separable comparison state.

**Source pointers:** Wilde §§3.6 and 9.2 through [notation and assumptions](WILDE_BRIDGE.md#notation-and-assumptions); [target and fidelity](../science/model.md#3-classical-control-and-physical-output); [Bell overlap of separable operators](../science/blind_strip.md#from-separability-to-bell-fidelity).

<a id="m04"></a>
### M04. Instruments and the outcome/report distinction

**Phase:** Background/preliminaries.

**Central question:** Which part of a measurement changes the quantum state, and which part communicates its outcome to the controller?

**Understanding target:** Describe a binary instrument by outcome maps whose sum is trace preserving. Separate its true physical outcome from the noisy public report. Explain how ideal quantum projection can coexist with an unreliable classical record.

**Dependencies and story role:** Uses [M01](#m01) and [M02](#m02). This supplies the measurement model on which both amplification and the blind-strip comparison depend.

**Conceptual connection:** The theorem locates the prescribed noise at the report interface. Blinding that interface changes the accessible record while leaving the physical instrument in place.

**Source pointers:** Wilde §§3.4, 4.2, and 4.6 through [states, records, and instruments](WILDE_BRIDGE.md#states-records-and-instruments); [the report interface](../science/model.md#2-the-report-interface); [inside-outcome coarse graining](../science/blind_strip.md#1-refine-the-public-record-without-selecting-an-inside-outcome).

<a id="m05"></a>
### M05. Channels and outcome-register dilations

**Phase:** Background/preliminaries.

**Central question:** How can a selected measurement branch be represented inside a trace-preserving description that retains its record?

**Understanding target:** Distinguish a CPTP channel from a completely positive, trace-decreasing branch. Explain the representation $`\rho\mapsto\sum_x\mathcal I_x(\rho)\otimes|x\rangle\langle x|`$ and why selecting the retained register at the end recovers the desired branch.

**Dependencies and story role:** Uses [M02](#m02) and [M04](#m04). It connects measurement outcomes to the channel language required for a valid cancellation argument.

**Conceptual connection:** Mathematical outcome registers preserve the effect of conditioning. They do not grant the physical controller an additional readout channel.

**Source pointers:** Wilde §§4.4–4.6 and 5.2–5.4 through [instruments and dilations](WILDE_BRIDGE.md#states-records-and-instruments); [the explicit outcome-register construction](../science/blind_strip.md#2-retain-every-outside-outcome-register).

<a id="m06"></a>
### M06. Separable resources and shared randomness

**Phase:** Background/preliminaries.

**Central question:** Which correlations can be present without supplying initial entanglement across the chain?

**Understanding target:** Distinguish product states, separable mixtures, and entangled states. Explain how fixing shared classical randomness leaves a product input, and why a positive mixture of product endpoint operators remains separable. Relate separability to the Bell-fidelity threshold $`1/2`$.

**Dependencies and story role:** Uses [M02](#m02), [M03](#m03), and [M05](#m05). This identifies the free initial correlations and the comparison class used by the converse.

**Conceptual connection:** Global classical correlations are compatible with the theorem. The decisive distinction is whether a quantum connection can create entanglement between the designated endpoints.

**Source pointers:** Wilde §§4.3 and 19.2 through [the selective section map](WILDE_BRIDGE.md#selective-section-map); [initial resources](../science/model.md#1-sites-time-and-initial-resources); [separability and Bell fidelity](../science/blind_strip.md#from-separability-to-bell-fidelity).

<a id="m07"></a>
### M07. Bell transformations and Pauli corrections

**Phase:** Background/preliminaries.

**Central question:** Why do local Bell measurements leave distant endpoints entangled with an outcome-dependent correction?

**Understanding target:** Follow the two Bell-measurement bits through the CNOT and Hadamard basis change. Identify which bit contributes an X byproduct and which contributes a Z byproduct, and explain why a wrong classical correction changes the physical Bell state.

**Dependencies and story role:** Uses [M03](#m03), [M04](#m04), and [M05](#m05). It supplies a small operational example before spatial resource accounting is added.

**Conceptual connection:** Teleportation-style resource conversion gives the local fusion mechanism. The project adds noisy reports and a bounded-range implementation of its corrections and redundancy.

**Source pointers:** Wilde §§3.3 and 6.1–6.2 through [the four-qubit example](WILDE_BRIDGE.md#four-qubit-example); [the project's Bell-byproduct convention](../science/construction.md#2-the-two-bell-byproducts).

<a id="m08"></a>
### M08. Local depth and quantum causal cones

**Phase:** Background/preliminaries.

**Central question:** What can a fixed-depth circuit transmit when every quantum operation has bounded spatial range?

**Understanding target:** Interpret depth as gate and readout layers, with overlapping operations assigned separate layers. Explain the backward support of a retained output in a fixed circuit and why its quantum cone expands by at most $`r`$ sites per layer. Keep quantum propagation distinct from free classical communication.

**Dependencies and story role:** Uses [M02](#m02), [M05](#m05), and [M07](#m07). It adds geometry to the local operations already defined.

**Conceptual connection:** Wilde supplies channel and reversible-operation foundations. The lattice metric, fixed density, and causal-cone bound are explicit additional structures of this project.

**Source pointers:** Wilde §§3.3 and 4.4 through [the local-construction bridge](WILDE_BRIDGE.md#local-construction); [sites and layer conventions](../science/model.md#1-sites-time-and-initial-resources); [circuit conventions for the converse](../science/blind_strip.md#circuit-and-readout-conventions).

<a id="m09"></a>
### M09. Adaptive control and refined histories

**Phase:** Background/preliminaries.

**Central question:** How can a proof analyze local quantum propagation when operations depend on a global public record?

**Understanding target:** Explain how a complete public history fixes the operation choices, while refinement by selected true outcomes produces unnormalized quantum branches. Distinguish fixing control parameters from giving the controller access to hidden outcomes. Recognize why branch selection must be retained during trace-preserving manipulations.

**Dependencies and story role:** Uses [M04](#m04), [M05](#m05), [M06](#m06), and [M08](#m08). It joins instruments, conditioning, classical control, and local geometry.

**Conceptual connection:** The converse covers arbitrary adaptive public feedforward. Its fixed-history analysis is the route to local factorization without imposing a false locality bound on classical communication.

**Source pointers:** Wilde §§4.6, 5.3–5.4, and 19.2 through [the blind-strip bridge](WILDE_BRIDGE.md#blind-strip); [public control](../science/model.md#3-classical-control-and-physical-output); [refinement of the public record](../science/blind_strip.md#1-refine-the-public-record-without-selecting-an-inside-outcome).

<a id="m10"></a>
### M10. Independent binary readout

**Phase:** Background/preliminaries.

**Central question:** What information does an unflagged binary symmetric detector provide on each use?

**Understanding target:** Interpret $`y=x\oplus e`$, the crossover probability $`p`$, and the bias $`\delta=1-2p`$. Explain independence across potential report slots and independence from initial resources and controller randomness. Distinguish knowing the detector parameter from knowing a realized flip or an auxiliary erasure flag.

**Dependencies and story role:** Uses [M01](#m01) and [M04](#m04). It identifies the local classical channel that will be repeated in the construction and changed in the converse.

**Conceptual connection:** The prescribed detector supplies only its public binary output. Timing, measurement presence, and hidden flags cannot carry additional ideal outcome information.

**Source pointers:** Wilde §4.6 through [notation and interface assumptions](WILDE_BRIDGE.md#notation-and-assumptions); [the exact BSC interface](../science/model.md#2-the-report-interface); [potential-slot noise tables](../science/information_bound.md#a-common-protocol-map-for-every-readout-table).

<a id="m11"></a>
### M11. Repetition and detector information

**Phase:** Background/preliminaries.

**Central question:** What controls the reliability obtained by repeatedly reading the same latent bit?

**Understanding target:** Relate independent reports to a binomial decoding error, including the tie convention. Interpret $`D(p)=-\tfrac12\log[4p(1-p)]`$ as the coefficient in the repeated-report error exponent. Explain why a small bias requires a number of reports proportional to its inverse square for a fixed exponent.

**Dependencies and story role:** Uses [M10](#m10). It turns the detector description into a quantitative reliability resource.

**Conceptual connection:** The book's classical information concepts provide background; the project explicitly derives the finite Chernoff estimate. The same coefficient will reappear in the converse's likelihood moments.

**Source pointers:** Wilde §§10.5 and 10.7 through [the local-construction bridge](WILDE_BRIDGE.md#local-construction); [the finite Chernoff derivation](../science/construction.md#4-chernoff-estimate); [attribution of the detector coefficient](../references/RELATED_WORK.md#danjou2021).

<a id="m12"></a>
### M12. Statistical distance and data processing

**Phase:** Background/preliminaries.

**Central question:** How does closeness of two noise distributions constrain the difference between their physical output fidelities?

**Understanding target:** Connect a bounded test's bias to total variation, and connect a processed binary test to classical relative entropy. Preserve the normalization: Wilde uses unhalved trace distance, while the operational half-norm and classical total variation contain $`1/2`$. Translate Wilde's base-two information units to the project's natural logarithms, and keep relative entropy's argument order explicit.

**Dependencies and story role:** Uses [M03](#m03), [M05](#m05), and [M10](#m10). It links statistical comparisons to the physical output criterion.

**Conceptual connection:** The implemented proof uses a classical Bell-test kernel, log-sum, and Jensen inequalities. It does not require a separate quantum relative-entropy argument.

**Source pointers:** Wilde §§9.1–9.3, 10.5, and 10.7 through [notation translation](WILDE_BRIDGE.md#notation-and-assumptions); [Bell fidelity as a statistical test](../science/information_bound.md#bell-fidelity-as-a-statistical-test); [the reverse-relative-entropy step](../science/information_bound.md#reverse-relative-entropy-gives-the-accuracy-dependence).

<a id="m13"></a>
### M13. Product likelihoods and mixtures

**Phase:** Background/preliminaries.

**Central question:** Why can a mixture of localized alternatives be harder to distinguish than an alternative at a known location?

**Understanding target:** Interpret a likelihood ratio as a change of probability measure. Explain why independent table blocks produce independent ratio fluctuations, why ratios multiply across slots, and why a mixture averages ratios. Distinguish this statistical closeness from an exact common positive component of two channels.

**Dependencies and story role:** Uses [M10](#m10) and [M12](#m12). It supplies the final statistical ingredient before the full physical task is assembled.

**Conceptual connection:** The elementary moment calculation is supplied in the project. The book's relative-entropy and inequality sections support its language without supplying the particular blind-strip alternative.

**Source pointers:** Wilde §§10.5 and 10.7 through [the statistical-mixture bridge](WILDE_BRIDGE.md#statistical-mixture); [the likelihood-moment calculation](../science/information_bound.md#exact-chi-square-calculation); [methodological attribution](../references/RELATED_WORK.md#chen2022).

<a id="m14"></a>
### M14. The complete report-limited task

**Phase:** Background/preliminaries.

**Central question:** Which resources, outputs, and quantifiers define the optimization problem?

**Understanding target:** Assemble product inputs conditional on shared randomness, fixed local memory and range, a fixed report density, an unflagged independent detector, and arbitrary public feedforward. Identify worst-case operation depth, the physical corrected Bell output, target infidelity, and the optional fixed success requirement. Distinguish this task from a channel-capacity problem or an estimator of ideal data.

**Dependencies and story role:** Integrates [M06](#m06), [M08](#m08)–[M13](#m13). This closes the background phase with a complete model rather than another isolated prerequisite.

**Conceptual connection:** Quantum resource definitions and statistical information now specify one physical preparation problem. These conditions determine which textbook ideas transfer and which project-specific arguments remain necessary.

**Source pointers:** Wilde §§4.6, 6.1, 9.1–9.2, 10.5, and 19.2 through [notation and assumptions](WILDE_BRIDGE.md#notation-and-assumptions); [the authoritative model](../science/model.md#scientific-route); [initial resources](../science/model.md#1-sites-time-and-initial-resources) and [physical output](../science/model.md#3-classical-control-and-physical-output).

<a id="narrative-innovation"></a>
## Narrative/innovation: M15–M30

<a id="m15"></a>
### M15. Creating and fusing local Bell links

**Phase:** Narrative/innovation.

**Central question:** How can a chain be assembled from short Bell links using only local quantum gates?

**Understanding target:** Explain central Bell creation, outward SWAPs, and the local Bell-basis change at a boundary. Follow the four-qubit fusion example to its conditional endpoint state and identify the two latent correction bits. Count quantum layers under the stated gate convention.

**Dependencies and story role:** Uses [M07](#m07), [M08](#m08), and [M14](#m14). It begins the research narrative with a concrete local circuit component.

**Conceptual connection:** The familiar Bell-resource conversion is now embedded in a spatial line. This supplies the component whose outcomes must become reliable before the links yield a useful corrected output.

**Source pointers:** Wilde §§6.1–6.2 through [the four-qubit example](WILDE_BRIDGE.md#four-qubit-example); [block preparation and layers](../science/construction.md#1-equal-blocks-and-layer-conventions); [Bell byproducts](../science/construction.md#2-the-two-bell-byproducts).

<a id="m16"></a>
### M16. Spatial pointer copying at fixed memory

**Phase:** Narrative/innovation.

**Central question:** How can each boundary outcome acquire spatial redundancy without increasing memory per site with distance?

**Understanding target:** Explain the coherent CNOT copying of an orthogonal pointer into a reserved half-block. Account for disjoint copying domains, reuse of the qubits that previously carried the Bell link, and exclusion of the retained endpoints from readout. Relate the number of pointer copies to the local propagation depth.

**Dependencies and story role:** Uses [M01](#m01), [M05](#m05), [M08](#m08), and [M15](#m15). It develops the construction's spatial resource before readout time is added.

**Conceptual connection:** Coherent records support redundancy, but moving their information through a line costs depth. The one-qubit-per-site schedule makes that cost explicit.

**Source pointers:** Wilde §§5.3–5.4, with optional §§7.1–7.2, through [the local-construction bridge](WILDE_BRIDGE.md#local-construction); [the disjoint pointer domains](../science/construction.md#1-equal-blocks-and-layer-conventions).

<a id="m17"></a>
### M17. Repeated readout and bit reliability

**Phase:** Narrative/innovation.

**Central question:** How do spatial copies and repeated reads combine into reliable knowledge of one latent Bell bit?

**Understanding target:** Explain why QND Z readout preserves a pointer value while each report receives a fresh independent flip. Relate $`m=bt/2`$ reports to one decoded bit and its error bound $`e_m(p)\le e^{-D(p)m}`$. State the additional fixed resources needed when readout is destructive instead.

**Dependencies and story role:** Uses [M10](#m10), [M11](#m11), and [M16](#m16). It completes the local amplification mechanism by combining spatial redundancy with time.

**Conceptual connection:** Spatial copying and temporal repetition contribute multiplicatively to report count, while their operation depths add.

**Source pointers:** Wilde §§10.5 and 10.7 through [the local-construction bridge](WILDE_BRIDGE.md#local-construction); [majority decoding](../science/construction.md#3-decoding-and-exact-output-fidelity); [Chernoff estimate](../science/construction.md#4-chernoff-estimate); [readout implementation](../science/construction.md#6-readout-implementation-and-finite-verification).

<a id="m18"></a>
### M18. Corrected global fidelity and the finite construction

**Phase:** Narrative/innovation.

**Central question:** How do the boundary decoding errors determine the physical endpoint fidelity of the assembled circuit?

**Understanding target:** Connect the two final Pauli errors to parities of the decoded boundary errors. Explain their independence and the equal-block expression $`F=[1+(1-2e_m)^M]^2/4`$. Relate the finite union bound to $`T=b+t+3`$ and $`m=bt/2`$ under the native equal-even-block convention, and recognize that arbitrary lengths require the stated separate partition.

**Dependencies and story role:** Integrates [M15](#m15)–[M17](#m17). It establishes finite fidelity and resource bookkeeping for a particular construction, without yet claiming optimality among all protocols.

**Conceptual connection:** A small fusion example scales into a complete finite circuit by tracking its physical byproducts and report errors.

**Source pointers:** Wilde §§6.2 and 9.2 through [the worked example](WILDE_BRIDGE.md#four-qubit-example) and [construction bridge](WILDE_BRIDGE.md#local-construction); [exact corrected fidelity](../science/construction.md#3-decoding-and-exact-output-fidelity); [arbitrary chain lengths](../science/construction.md#5-an-explicit-partition-for-every-chain-length).

<a id="m19"></a>
### M19. What changes when a strip becomes blind

**Phase:** Narrative/innovation.

**Central question:** What remains physically possible inside a region whose reports reveal no measurement outcomes?

**Understanding target:** Explain the counterfactual replacement of reports by independent fair coins while retaining every permitted local quantum operation. Show why summing the hidden inside outcomes gives nonselective CPTP maps. Distinguish a blind report interface from deleting quantum wires or making every internal cut entanglement breaking.

**Dependencies and story role:** Uses [M04](#m04), [M05](#m05), [M09](#m09), and [M14](#m14). It begins the local obstruction complementary to the construction.

**Conceptual connection:** The same outcome/report separation that permits readout amplification also identifies what the comparison experiment removes.

**Source pointers:** Wilde §§4.4–4.6 and 5.3 through [the blind-strip bridge](WILDE_BRIDGE.md#blind-strip); [the comparison premise](../science/blind_strip.md#blind-strip-lemma); [inside-outcome summation](../science/blind_strip.md#1-refine-the-public-record-without-selecting-an-inside-outcome).

<a id="m20"></a>
### M20. Retaining outside records before cancellation

**Phase:** Narrative/innovation.

**Central question:** Why must the proof retain outside measurement outcomes before tracing away unobserved parts of the circuit?

**Understanding target:** Explain the obstruction caused by selected, trace-decreasing outside branches. Replace each by a CPTP instrument with a retained local outcome register, and postpone projection of that register. Identify why this construction preserves the refined branch while making trace-preserving cancellation legitimate.

**Dependencies and story role:** Uses [M05](#m05), [M09](#m09), and [M19](#m19). It supplies the technical step that makes the adaptive geometric argument valid.

**Conceptual connection:** The textbook instrument representation becomes a proof device for local histories. A mathematical record retains conditioning without becoming a new physical information resource.

**Source pointers:** Wilde §§4.6 and 5.3–5.4 through [the blind-strip bridge](WILDE_BRIDGE.md#blind-strip); [outside outcome registers](../science/blind_strip.md#2-retain-every-outside-outcome-register); [the subsequent cancellation](../science/blind_strip.md#3-the-two-retained-quantum-histories-are-disjoint).

<a id="m21"></a>
### M21. Disjoint histories and conditional separability

**Phase:** Narrative/innovation.

**Central question:** Why does a strip wider than twice the available quantum cone radius force separability even after public heralding?

**Understanding target:** Trace the retained left and right histories backward and use $`w>2rT`$ to keep them disjoint. Combine product initial resources, CPTP cancellation, and final local record projections into a positive product branch. Explain why summing refined histories or selecting a public acceptance event preserves separability despite global classical correlations.

**Dependencies and story role:** Integrates [M06](#m06), [M08](#m08), and [M19](#m19)–[M20](#m20). It completes the quantum obstruction that the statistical comparison will use.

**Conceptual connection:** Locality and correct conditioning place the comparison state in a resource-constrained set. This is the quantum input to the later classical calculation.

**Source pointers:** Wilde §§4.3 and 19.2 through [the blind-strip bridge](WILDE_BRIDGE.md#blind-strip); [disjoint retained histories](../science/blind_strip.md#3-the-two-retained-quantum-histories-are-disjoint); [positive product branches](../science/blind_strip.md#4-select-the-refined-record-and-sum-positive-product-branches).

<a id="m22"></a>
### M22. One algorithm for every noise table

**Phase:** Narrative/innovation.

**Central question:** How can the actual and counterfactual detectors be compared without changing an adaptive protocol's rules?

**Understanding target:** Explain the fixed array of potential flip slots, including idle positions, and the normalized output $`\rho(e)`$ for a fixed table. Interpret $`\mathcal P(R)=\sum_eR(e)\rho(e)`$ as one common map. Keep the controller's rule unchanged and the realized table hidden when its probability distribution is changed.

**Dependencies and story role:** Uses [M09](#m09), [M10](#m10), [M13](#m13), and [M14](#m14). It connects the local blind-strip experiment to a comparison of complete adaptive executions.

**Conceptual connection:** A classical distribution can control a quantum-output channel. The project-specific table representation makes this statement exact despite adaptive choices and stopping.

**Source pointers:** Wilde §§4.6 and 10.5 through [the noise-table bridge](WILDE_BRIDGE.md#noise-table); [the common protocol map](../science/information_bound.md#a-common-protocol-map-for-every-readout-table).

<a id="m23"></a>
### M23. Hiding the randomized strip

**Phase:** Narrative/innovation.

**Central question:** How does an unknown strip location convert many local obstructions into a strong statistical comparison?

**Understanding target:** Form $`Q=M^{-1}\sum_jQ_j`$, with each $`Q_j`$ blinding one strip. Explain separability of the mixture output and independence of the disjoint likelihood-ratio fluctuations under $`P`$. Account for both the single-strip factor and the location factor in

```math
\chi^2(Q\Vert P)=\frac{e^{2kD(p)}-1}{M}.
```

**Dependencies and story role:** Uses [M13](#m13), [M21](#m21), and [M22](#m22). It assembles the local quantum obstruction into a global alternative distribution.

**Conceptual connection:** The mixture hides where information was removed. Its usefulness comes from statistical indistinguishability, without requiring a large exact blind component in every physical detector channel.

**Source pointers:** Wilde §§10.5 and 10.7 as foundations through [the statistical-mixture bridge](WILDE_BRIDGE.md#statistical-mixture); [random-strip alternatives](../science/information_bound.md#random-strip-alternatives); [the exact moment identity](../science/information_bound.md#exact-chi-square-calculation).

<a id="m24"></a>
### M24. Bell fidelity forces statistical separation

**Phase:** Narrative/innovation.

**Central question:** Why must a successful preparation distinguish the real detector from the separable comparison experiment?

**Understanding target:** Use the Bell projector as a bounded test with expectation at most $`1/2`$ under the comparison. Connect its bias to total variation and the mixture's chi-square moment. Explain why reverse relative entropy $`D_{\mathrm{KL}}(Q\Vert P)`$ captures the additional cost as actual fidelity approaches one, and why this test adds no operation to the protocol.

**Dependencies and story role:** Uses [M03](#m03), [M06](#m06), [M12](#m12), and [M23](#m23). It turns the comparison construction into finite universal fidelity inequalities.

**Conceptual connection:** The quantum resource boundary supplies the test threshold; classical information inequalities transfer that threshold to a constraint on available readout information.

**Source pointers:** Wilde §§9.1–9.3, 10.5, and 10.7 through [the statistical-mixture bridge](WILDE_BRIDGE.md#statistical-mixture); [the Bell test](../science/information_bound.md#bell-fidelity-as-a-statistical-test); [the accuracy inequality](../science/information_bound.md#reverse-relative-entropy-gives-the-accuracy-dependence).

<a id="m25"></a>
### M25. Success probability and conditional accuracy

**Phase:** Narrative/innovation.

**Central question:** What resource cost remains when the protocol is allowed to reject some executions?

**Understanding target:** Keep success probability and conditional Bell infidelity separate. Explain why a blind comparison can have a different acceptance probability, and how the two likelihood-moment orientations control this change. Relate the resulting $`\epsilon\ge s^3e^{-6kD(p)}/4`$ bound to the geometric success-dependent bound. State why fixed positive success preserves the depth order while vanishing yield remains a different optimization.

**Dependencies and story role:** Uses [M09](#m09), [M12](#m12)–[M13](#m13), [M21](#m21), and [M24](#m24). It completes the finite converse's treatment of both output accuracy and acceptance.

**Conceptual connection:** Conditional separability and change of measure prevent postselection from removing the information cost at fixed success probability.

**Source pointers:** Wilde §§9.2, 10.5, 10.7, and 19.2 through [accuracy and heralding](WILDE_BRIDGE.md#accuracy-and-heralding); [accepted output functions](../science/heralding.md#accepted-output-as-a-function-of-the-error-table); [the two moment comparisons](../science/heralding.md#conditional-accuracy-from-two-likelihood-ratio-moments).

<a id="m26"></a>
### M26. The two competing spatial counts

**Phase:** Narrative/innovation.

**Central question:** Which spatial quantities must be counted before the construction and converse can be compared?

**Understanding target:** Relate strip width $`w=2rT+1`$ to $`k=\nu wT=O(T^2)`$ potential reports and $`M=\lfloor(L-1)/w\rfloor`$ disjoint alternatives. Compare this with the construction's $`O(bt)`$ reports per boundary and $`O(L/b)`$ boundaries. Keep the two meanings of $`M`$ within their separate arguments, and retain the changing factor $`L/T`$.

**Dependencies and story role:** Integrates [M08](#m08), [M18](#m18), [M21](#m21), and [M24](#m24)–[M25](#m25). It places the lower and upper bounds in the same geometric resource units.

**Conceptual connection:** Fixed spatial density turns available space and time into an area-like report budget. The remaining number of interfaces determines the logarithmic reliability requirement.

**Source pointers:** Wilde §§4.6, 6.1, and 10.5 as foundations through [the uniform-depth bridge](WILDE_BRIDGE.md#uniform-depth); [finite strip packing](../science/blind_strip.md#finite-strip-count); [arbitrary-length construction](../science/construction.md#5-an-explicit-partition-for-every-chain-length); [packing in the converse](../science/depth_law.md#5-strip-packing-and-inversion).

<a id="m27"></a>
### M27. The uniform depth law and its caps

**Phase:** Narrative/innovation.

**Central question:** How do finite bounds become one optimal-depth statement valid when distance, detector quality, and accuracy all vary?

**Understanding target:** Connect balanced spatial and temporal amplification to the converse's necessary information budget. Interpret the unique positive solution of $`D(p)\tau^2=\log[L/(\epsilon\tau)]`$ and the matched scale

```math
T_{\mathrm{opt}}
=\Theta\!\left(\max\{1,\min\{L,\tau\}\}\right).
```

Explain the microscopic floor, the exact coherent linear-depth alternative, integer block choices, and the fixed-success dependence of constants. Distinguish uniform quantifiers from a limit taken at fixed detector quality.

**Dependencies and story role:** Uses [M14](#m14), [M18](#m18), and [M24](#m24)–[M26](#m26). It combines the finite mechanisms into the project's principal resource theorem.

**Conceptual connection:** The implicit scale summarizes a constructive-converse match. Its geometry and inversion are supplied by the project, not by a textbook channel-capacity theorem.

**Source pointers:** Wilde §§6.1, 9.2, and 10.5 as foundations through [the uniform-depth bridge](WILDE_BRIDGE.md#uniform-depth); [the uniform statement](../science/depth_law.md#1-statement); [the inverse scale](../science/depth_law.md#2-the-inverse-scale); [uniform upper construction](../science/depth_law.md#3-uniform-constructive-upper-bound) and [lower inversion](../science/depth_law.md#5-strip-packing-and-inversion).

<a id="m28"></a>
### M28. Detector and accuracy crossovers

**Phase:** Narrative/innovation.

**Central question:** When does measurement assistance retain a sublinear-depth advantage over coherent propagation?

**Understanding target:** Explain the fixed-quality $`\sqrt{\log L}`$ regime and the weak-bias behavior $`D(p)\sim\delta^2/2`$. Interpret the variable-accuracy criterion $`D(p)L^2/\log(1/\epsilon)\to\infty`$ for sublinear depth. Use the example $`D(p_L)=\log L/L^2`$ to identify why discarding $`T`$ inside the logarithm gives the wrong crossover.

**Dependencies and story role:** Uses [M11](#m11) and [M27](#m27). It translates the uniform theorem into physical parameter regimes.

**Conceptual connection:** Detector information, geometric distance, and output accuracy jointly determine whether the coherent cap is active. A fixed-quality asymptotic estimate does not contain this full information.

**Source pointers:** Wilde §§10.5 and 10.7 as background through [the uniform-depth bridge](WILDE_BRIDGE.md#uniform-depth); [detector and accuracy regimes](../science/depth_law.md#6-detector-and-accuracy-regimes); [the coherent crossover](../science/depth_law.md#7-the-coherent-crossover); [its physical interpretation](../science/interpretation.md#5-detector-quality-and-the-crossover).

<a id="m29"></a>
### M29. Scope, attribution, and verification

**Phase:** Narrative/innovation.

**Central question:** Which conclusions are established by the theorem, the construction, the cited foundations, and the finite computation?

**Understanding target:** Keep the unflagged independent report model, fixed local resources, and free classical-communication convention attached to the result. Distinguish the ideal-control construction from the broader local-CPTP converse, and a heterogeneous-detector obstruction from a matched general law. Identify imported research ingredients and explain why the finite layout check supports circuit details without proving the universal or asymptotic statements.

**Dependencies and story role:** Uses [M14](#m14), [M18](#m18), [M21](#m21), and [M24](#m24)–[M28](#m28). It establishes the boundaries required for a faithful global explanation.

**Conceptual connection:** Resource definitions, mathematical proof, primary attribution, and finite verification provide different kinds of support. Their roles must remain distinguishable when applying the theorem.

**Source pointers:** Wilde §§4.4, 6.1, 9.2, and 19.2 through [scope and the complete story](WILDE_BRIDGE.md#scope-and-complete-story); [implementation assumptions](../science/interpretation.md#7-ideal-coherent-control-and-physical-implementations); [research ingredients](../references/RELATED_WORK.md#ingredients-and-their-roles) and [attribution limits](../references/RELATED_WORK.md#scope-of-the-comparison); [finite verification scope](../verification/README.md#analytical-scope).

<a id="m30"></a>
### M30. The complete information-resource explanation

**Phase:** Narrative/innovation.

**Central question:** Why does noisy access to local outcomes impose the matched global cost for physically delivering distant entanglement?

**Understanding target:** Connect the full argument: local Bell fusion creates outcome-dependent corrections; spatial copying and repeated readout make their information reliable; a blind strip forces conditional separability; a mixture of possible strip locations constrains any adaptive algorithm; and the constructive and converse counts match uniformly. Explain why only two final correction parities can still require information acquired throughout the chain, and carry the detector, accuracy, success, and implementation boundaries into that explanation.

**Dependencies and story role:** Integrates [M14](#m14), [M18](#m18), [M21](#m21), and [M24](#m24)–[M29](#m29). This closes the narrative phase with the complete resource statement rather than another isolated technique.

**Conceptual connection:** The project joins quantum locality to classical statistical information through a physical entanglement task. The educational anchor supplies the common language; the linked scientific account supplies the particular mechanism, proof, construction, and scope.

**Source pointers:** Wilde §§4.6, 6.1, 9.1–9.2, 10.5, and 19.2 through [the complete bridge synthesis](WILDE_BRIDGE.md#scope-and-complete-story); [the main theorem](../science/model.md#5-uniform-optimal-depth-theorem); [its consequences](../science/model.md#6-consequences-and-interpretation); [the resulting resource statement](../science/interpretation.md#8-the-resulting-resource-statement).
