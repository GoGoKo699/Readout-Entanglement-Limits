# Milestones for the adaptive-entanglement depth argument

This map follows the preparation of a retained Bell pair on the fixed endpoints of a one-dimensional chain. Its single textbook anchor is John Watrous, *The Theory of Quantum Information* (2018), introduced in [ANCHOR.md](ANCHOR.md). The [bridge](BRIDGE.md) explains how the book's formalism enters the project. Section and page references below use the book's printed numbering and link to the author's chapter files.

The first 12 milestones establish the mathematical objects that the argument uses: physical registers, channels, instruments, classical records, adjoint maps, separability, and the output criterion. The remaining 18 follow the actual proof and construction. This allocation gives separate treatment to the adaptive separator and the physical readout banks, then brings them together at the optimal-depth statement. The textbook supplies the underlying quantum-information formalism. The project's spatial model, reporting-noise decomposition, causal proof, probability estimates, and depth law are developed in the linked scientific pages.

## Phase I: Background and preliminaries (M01–M12)

The route begins with one register and one operation, then builds the language needed to describe a spatially distributed adaptive protocol and its retained output.

### M01. Physical registers and spatial tensor factors

**Central question:** What physical systems exist in the preparation task, and how does the state space encode their locations?

**Understanding target:** Identify a qubit register, its computational basis, and the tensor product of the registers at sites $0,\ldots,L$. Distinguish the endpoint separation $L$, the total site count $N=L+1$, and the number $w$ of physical qubits permitted per column. Understand why retained ancillas and reusable quantum memory occupy physical slots.

**Dependencies:** None.

**Story role and connection:** Locality becomes a statement about which tensor factors an operation can act on. This fixes the physical meaning of both the converse's cut and the construction's banks.

**Sources:** [Watrous §§2.1.1–2.1.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf), registers and states; [geometry, initial state, and retained memory](../science/model.md#geometry-initial-state-and-retained-memory).

### M02. The retained endpoint state

**Central question:** Which quantum state is judged after the other qubits have finished their work?

**Understanding target:** Describe mixed states and reductions by partial trace. Identify $|\Phi^+\rangle=(|00\rangle+|11\rangle)/\sqrt2$ as the target on the designated endpoints, whose individual reductions are mixed. Separate the reduced physical pair from the joint processor state and from classical data obtained by destructively measuring that pair.

**Dependencies:** M01.

**Story role and connection:** The output criterion concerns two retained registers. Every later equality, separability statement, and fidelity calculation must refer to these same registers.

**Sources:** [Watrous §§2.1.2–2.1.3](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf), states and reductions; [§6.3.1, Example 6.50](https://cs.uwaterloo.ca/~watrous/TQI/TQI.6.pdf), qubit Bell states; [Bell fidelity and success](../science/model.md#bell-fidelity-and-success).

### M03. Channels, discarded environments, and reset

**Central question:** How can a local physical operation be described without assuming that it is unitary?

**Understanding target:** Interpret completely positive, trace-preserving maps as channels and distinguish their input and output registers. Include unitary gates, discarded local environments, and reset within this language. Recognize that a quantum environment retained for later use must be counted as memory rather than silently discarded from the resource model.

**Dependencies:** M01.

**Story role and connection:** General channels make the lower bound apply beyond Clifford circuits, while the construction uses a specific permitted gate set. Trace preservation will later control backward observable support.

**Sources:** [Watrous §§2.2.1–2.2.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf), channels and their representations; [retained memory](../science/model.md#geometry-initial-state-and-retained-memory) and [a circuit round](../science/model.md#a-circuit-round).

### M04. Instruments and unnormalized branches

**Central question:** How does a measurement specify both an outcome probability and a conditional quantum state?

**Understanding target:** Use completely positive outcome maps $\mathcal M_b$ with trace-preserving sum. Interpret $\mathcal M_b(\rho)$ as a positive operator whose trace is the outcome probability, and normalization as a separate operation. Understand why summing outcomes gives a channel while selecting one outcome generally gives a trace-decreasing map.

**Dependencies:** M03.

**Story role and connection:** Unnormalized branches retain the probability weights needed for adaptive composition and heralding. Normalizing them prematurely would obscure the equality required in the separator proof.

**Sources:** [Watrous §2.3.2, pp. 112–113, Eqs. (2.258)–(2.262)](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf), instruments; [noise acts on the report](../science/model.md#noise-acts-on-the-report).

### M05. Classical records beside quantum states

**Central question:** What information does an accessible transcript contain, and what quantum state remains conditional on it?

**Understanding target:** Represent a classical record by orthogonal labels and the joint record-output state by a sum of labeled unnormalized positive operators. Distinguish the true instrument outcome, its accessible report, an independent controller seed, and an unobserved variable. Summing an unobserved outcome and conditioning on a known outcome are different operations.

**Dependencies:** M01, M04.

**Story role and connection:** The converse must preserve the whole accessible transcript together with the endpoints. An endpoint marginal alone would not justify later conditioning on a success event.

**Sources:** [Watrous §2.1.2, p. 63, Eqs. (2.9)–(2.11), and §2.3.2, Eq. (2.262)](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf), ensembles and classical-quantum output; [Bell fidelity and success](../science/model.md#bell-fidelity-and-success).

### M06. Report noise and repeatable quantum backaction

**Central question:** What does a noisy readout change when its quantum backaction is ideal?

**Understanding target:** Interpret the report-conditioned map $\mathcal I_y=(1-p)\mathcal M_y+p\mathcal M_{1-y}$. For a QND computational-basis instrument, understand why the first measurement fixes a basis value and later measurements have that same true value. Each report receives a fresh independent Bernoulli flip with parameter $p$, although future quantum states may depend on earlier reports through feedback.

**Dependencies:** M04, M05.

**Story role and connection:** The distinction between backaction and reported data permits repeated sampling of one physical bit. It is also the distinction that makes the lower bound a statement about missing information in records.

**Sources:** [Watrous §2.3.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf), the instrument formalism; [the project's reporting channel and QND example](../science/model.md#noise-acts-on-the-report).

### M07. Bell labels, local gates, and classical correction

**Central question:** Why can a small classical label determine which Bell state a physical pair occupies?

**Understanding target:** Relate the four Bell states to single-qubit Pauli labels and the Bell-basis measurement to Hadamard and CNOT gates. Understand teleportation's separation between a quantum resource, a classical measurement result, and a conditional correction. Identify a SWAP as movement of a register's quantum state through local gates.

**Dependencies:** M02, M03, M05.

**Story role and connection:** This supplies the operational language for joining Bell links. The project must additionally schedule these operations on nearest-neighbor sites and charge their depth.

**Sources:** [Watrous §6.3.1, especially Example 6.50, pp. 365–366](https://cs.uwaterloo.ca/~watrous/TQI/TQI.6.pdf), teleportation; [link preparation](../science/construction.md#preparing-the-links-and-returning-their-interiors-to-zero) and [joining links](../science/construction.md#joining-the-links-and-creating-disjoint-banks).

### M08. Adjoint maps and identity factors

**Central question:** How can an output observable be followed backward through a quantum operation?

**Understanding target:** Use the adjoint relation between Schrödinger-picture state propagation and Heisenberg-picture observable propagation. Apply the equivalence between trace preservation and a unital adjoint. Distinguish an identity tensor factor from a nontrivial operator factor, and understand why a selected measurement outcome can act differently on the identity from an outcome-summed channel.

**Dependencies:** M03, M04.

**Story role and connection:** This algebra is the local engine of the separator proof. It identifies where an observable can acquire support rather than assuming that every conditioned operation has a unitary light cone.

**Sources:** [Watrous §1.1.2, pp. 21–22, Eq. (1.112)](https://cs.uwaterloo.ca/~watrous/TQI/TQI.1.pdf), adjoints of linear maps; [§2.2.2, Theorem 2.26, p. 87](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf), trace preservation and unitality; [proof of output-instrument equality](../science/converse.md#proof-of-equality-of-the-output-instruments).

### M09. Separability across a spatial cut

**Central question:** What remains possible when two regions share classical correlations but no entanglement?

**Understanding target:** Distinguish product states from convex mixtures of product states and use the cone of positive, possibly unnormalized, separable operators. Understand closure under positive sums and local partial trace. Relate the model's separable initialization across columns to separability across every cut that separates the endpoints.

**Dependencies:** M01, M02.

**Story role and connection:** The lower bound requires separability, not independence. Shared randomness and classical communication can correlate the endpoints without supplying the entanglement certified by the target.

**Sources:** [Watrous §6.1.1](https://cs.uwaterloo.ca/~watrous/TQI/TQI.6.pdf), separable operators and states; [initial state](../science/model.md#geometry-initial-state-and-retained-memory) and [why the cut implies separability](../science/converse.md#why-the-cut-implies-separability).

### M10. Local operations, communication, and conditioning

**Central question:** Why does selecting a classical transcript of an LOCC protocol preserve separability of a separable input?

**Understanding target:** Follow a sequence of local instruments whose choices can depend on communicated classical outcomes. Interpret each branch as a separability-preserving operation with its probability weight retained. Distinguish this branchwise property from the weaker statement that an averaged output is separable.

**Dependencies:** M04, M05, M09.

**Story role and connection:** After a quantum cut is deleted, unlimited classical feedback still remains. The LOCC argument is what turns that modified circuit into a useful obstruction, including for heralded preparation.

**Sources:** [Watrous §6.1.2, including Proposition 6.26, p. 332](https://cs.uwaterloo.ca/~watrous/TQI/TQI.6.pdf), LOCC and separable channels; [why the cut implies separability](../science/converse.md#why-the-cut-implies-separability).

### M11. Bell overlap and a linear entanglement witness

**Central question:** How can separability constrain the fidelity of the retained pair while keeping success probabilities explicit?

**Understanding target:** Use the project's Bell overlap $\mathrm{Tr}(\Phi\rho)$, which is the square of Watrous's root-fidelity convention for a pure target. Understand the separable threshold $1/2$ and the witness $W=2\Phi-I$. For an unnormalized separable operator $\tau$, its witness expectation is nonpositive; for any positive $\tau$, it is at most $\mathrm{Tr}\tau$.

**Dependencies:** M02, M09.

**Story role and connection:** A linear witness can be averaged over noise patterns and selected transcripts. This avoids replacing a weighted heralded output by its conditional fidelity alone.

**Sources:** [Watrous §3.2, Definition 3.11, p. 139](https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf), fidelity convention; [§6.1.1](https://cs.uwaterloo.ca/~watrous/TQI/TQI.6.pdf), separability; [the project's Bell witness](../science/converse.md#from-separability-to-a-heralded-fidelity-bound).

### M12. The complete depth-minimization task

**Central question:** Which resources are fixed or charged when comparing all adaptive protocols?

**Understanding target:** Assemble the synchronous model: disjoint local quantum operations in each round, at most one readout per qubit per round, and reports available to control the next round. Include perfect local quantum operations, fresh independent report errors, free reliable classical processing, no initial shared entanglement, and fixed physical outputs. Define $D_{\min}(L;p,F_0)$ with fixed $p\in(0,1/2)$ and $F_0\in(1/2,1)$.

**Dependencies:** M06, M07, M08, M10, M11.

**Story role and connection:** This makes the optimization a physical circuit question. The locality, timing, width, and fidelity conventions are project assumptions added to the textbook formalism.

**Sources:** [Watrous §§2.2–2.3](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf), channels and measurements; [the full model](../science/model.md), especially [a circuit round](../science/model.md#a-circuit-round) and [the optimization problem](../science/model.md#the-optimization-problem).

## Phase II: Narrative and innovation (M13–M30)

The converse begins with one noisy report and grows to a statement about every adaptive circuit on a long chain. The construction begins with one Bell link and grows to a complete physical schedule. Their final comparison identifies the optimal depth and the assumptions on which it depends.

### M13. Parallel swapping and its two global parities

**Central question:** How do many local Bell links become one distant Bell pair when all reports are reliable?

**Understanding target:** Follow the two-link swapping identity and its iteration. Identify the uniform junction bits $u_j,v_j$ and the endpoint label $X^VZ^U$, where $U$ and $V$ are their respective parities. Understand why simultaneous local junction operations and free classical parity computation give constant depth with perfect reports, while independent errors in unprotected reports accumulate in those parities.

**Dependencies:** M07, M11, M12.

**Story role and connection:** This establishes the task's noiseless advantage and identifies the classical information that the construction must protect. It does not restrict the converse to swapping protocols.

**Sources:** [Watrous §6.3.1](https://cs.uwaterloo.ca/~watrous/TQI/TQI.6.pdf), teleportation; [the two-link identity and junction labels](../science/construction.md#joining-the-links-and-creating-disjoint-banks), [decoding](../science/construction.md#decoding-the-noisy-records), and [three readout regimes](../science/interpretation.md#three-readout-regimes).

### M14. A report channel with a forgotten-outcome component

**Central question:** Which exact decomposition of a binary reporting error exposes complete loss of outcome information?

**Understanding target:** Interpret $\mathcal I_y=(1-2p)\mathcal M_y+p(\mathcal M_0+\mathcal M_1)$ as truthful reporting with probability $1-2p$ and an independent fair report with probability $2p$. Conditional on the latter event and its replacement coin, the physical map is the trace-preserving sum of the true-outcome maps. The measured qubit retains the correct instrument backaction.

**Dependencies:** M04, M06, M08.

**Story role and connection:** The refinement removes information from a report without inserting a quantum gate fault. This distinction determines the geometry required by the converse.

**Sources:** [Watrous §2.3.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf), instruments and summing outcomes; [refining a noisy report](../science/converse.md#refining-a-noisy-report).

### M15. Potential readout slots and revealed flags

**Central question:** How can independent noise events be defined before an adaptive protocol chooses where to measure?

**Understanding target:** Index potential slots by column, physical qubit, and round, including unused slots. Pre-sample independent erasure flags and replacement coins on this whole array. Understand why this realizes the original noise law when the arrays are hidden, and why proving a bound for a controller that knows them in advance also bounds the original controller. The enhanced controller may choose its schedule using the arrays.

**Dependencies:** M05, M12, M14.

**Story role and connection:** Independence belongs to the externally sampled slots, rather than to a random list of measurements chosen adaptively. This is what later permits independent corridor events.

**Sources:** [Watrous §§2.1.1 and 2.3.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf), classical registers and instruments; [potential slots and adaptive schedules](../science/converse.md#potential-slots-and-adaptive-schedules).

### M16. Fixed transcripts without hidden conditioning

**Central question:** What becomes fixed when an adaptive circuit is analyzed on one accessible transcript?

**Understanding target:** Condition on the sampled arrays and independent controller seed, then fix a complete accessible transcript. This fixes the chosen gates and instruments under the same policy, including its definition on zero-probability histories. Keep truthful outcome maps selected, erased true outcomes summed, and all branch weights unnormalized. Distinguish conditioning on a replacement coin from revealing the hidden physical outcome.

**Dependencies:** M04, M05, M15.

**Story role and connection:** The fixed branch is a definite composition of local CP maps. This permits an adjoint proof without granting access to hidden outcomes that could themselves enable entanglement swapping.

**Sources:** [Watrous §2.3.2, Eqs. (2.258)–(2.262)](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf), weighted outcome maps; [proof of equality of the output instruments](../science/converse.md#proof-of-equality-of-the-output-instruments).

### M17. A corridor beyond every accessible support seed

**Central question:** How wide must a region of forgotten reports be to isolate its central cut for $D$ rounds?

**Understanding target:** Track backward support from the endpoints and every truthful outcome map. Trace-preserving maps cannot seed support on an identity factor; truthful selected maps can. Place an erased corridor on $2D+2$ interior columns, whose two central cut columns lie at distance at least $D+1$ from all outside sites. Disjoint local operations expand support by at most one column per round.

**Dependencies:** M08, M12, M14, M16.

**Story role and connection:** A single erased site is insufficient because perfect gates can transport a hidden value coherently. The depth-wide corridor accounts for every charged path to an accessible outcome or endpoint.

**Sources:** [Watrous §2.2.2, Theorem 2.26](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf), unital adjoints; [separation by an erased corridor](../science/converse.md#separation-by-an-erased-corridor) and [coherent copies and adaptive choices](../science/converse.md#coherent-copies-and-adaptive-choices).

### M18. Deleting the cut preserves the full output instrument

**Central question:** Why does removing every quantum operation across the central cut leave all accessible predictions unchanged?

**Understanding target:** Use backward induction to compare the original and cut-deleted branch maps on every endpoint observable. Each deleted operation sees an identity factor and has a unital adjoint. Obtain equality of the unnormalized endpoint state for every transcript, including its probability by taking the identity observable. Scalar probability factors do not enlarge support. Retaining the classical transcript labels gives equality of the full classical-quantum output.

**Dependencies:** M16, M17.

**Story role and connection:** This is the central separator statement. Its branchwise strength is what protects the argument against arbitrary later success decisions and adaptive choices based on records outside the corridor.

**Sources:** [Watrous §1.1.2, Eq. (1.112)](https://cs.uwaterloo.ca/~watrous/TQI/TQI.1.pdf), adjoints; [§2.3.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf), output instruments; [the complete equality proof](../science/converse.md#proof-of-equality-of-the-output-instruments).

### M19. Separation survives accessible postselection

**Central question:** What does the deleted-cut circuit imply about each retained endpoint branch?

**Understanding target:** Regard the two sides of the cut as parties connected only by classical communication. From the allowed separable initialization, every transcript branch of the modified circuit has a separable endpoint state. Transfer this property through the output-instrument equality. Summing any selected set of positive branch operators preserves separability, including when success uses the revealed arrays.

**Dependencies:** M09, M10, M18.

**Story role and connection:** LOCC supplies a separability conclusion even when the endpoints remain classically correlated. The argument addresses conditional outputs directly instead of assuming that postselection preserves an averaged statement.

**Sources:** [Watrous §§6.1.1–6.1.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.6.pdf), separable operators and LOCC; [why the cut implies separability](../science/converse.md#why-the-cut-implies-separability).

### M20. Independent corridors along the whole chain

**Central question:** How does one separating region become a distance-dependent obstruction?

**Understanding target:** Pack $K=\lfloor(L-1)/(2D+2)\rfloor$ disjoint interior corridors. With width $w$, each contains $2wD(D+1)$ potential readout slots and is fully erased with probability $q=(2p)^{2wD(D+1)}$. Recognize independence from disjoint slot sets, even under flag-informed scheduling. Any erased corridor gives a separable contribution on the same retained pair $A:B$, although its spatial cut may vary.

**Dependencies:** M15, M17, M19.

**Story role and connection:** The proof now combines local geometry with repeated probabilistic opportunities across a long device. The relevant exponent counts space and time together.

**Sources:** [Watrous §6.1.1](https://cs.uwaterloo.ca/~watrous/TQI/TQI.6.pdf), closure of the separable cone; [packing independent corridors](../science/converse.md#packing-independent-corridors).

### M21. The finite deterministic and heralded theorem

**Central question:** How does the probability of avoiding all separating corridors bound useful endpoint entanglement?

**Understanding target:** Average the Bell witness over flag patterns and success-selected branches. Flag patterns with at least one fully erased corridor contribute a nonpositive expectation; all remaining patterns contribute at most their probability mass. Obtain $P_S(2F_S-1)\leq(1-q)^K\leq e^{-Kq}$ and the deterministic specialization $F\leq[1+(1-q)^K]/2$. Interpret $P_S=0$, the trivial $K=0$ bound, and the separately separable depth-zero case.

**Dependencies:** M11, M19, M20.

**Story role and connection:** Keeping success probability on the left prevents arbitrarily rare favorable records from being mistaken for deterministic preparation. The finite theorem is the quantitative form of the separator.

**Sources:** [Watrous §6.1.1](https://cs.uwaterloo.ca/~watrous/TQI/TQI.6.pdf), separability; [finite-size theorem](../science/converse.md#finite-size-theorem) and [heralded witness argument](../science/converse.md#from-separability-to-a-heralded-fidelity-bound).

### M22. The square-root logarithmic lower scale

**Central question:** Which total depth can sustain a fixed Bell advantage over the separable threshold as the chain grows?

**Understanding target:** With fixed $p\in(0,1/2)$, $w$, and $F_0\in(1/2,1)$, compare $K$ of order $L/D$ when $D=o(L)$ with $q$ exponentially small in $wD^2$. Read the finite condition $Kq\leq-\log(2F_0-1)$ and its implication $D=\Omega(\sqrt{\log L})$. The same obstruction applies with success probability bounded below. At fixed depth it gives an upper bound on accessible separation exponential in $D^2$.

**Dependencies:** M12, M21.

**Story role and connection:** The lower exponent comes from a depth-wide erased region repeated over the duration of the circuit. A matching range or depth claim still requires a physical construction.

**Sources:** [Watrous §2.3.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf), the instrument foundation, and [§6.1.1](https://cs.uwaterloo.ca/~watrous/TQI/TQI.6.pdf), separability; [fixed-target consequence](../science/converse.md#consequence-for-fixed-target-fidelity) and [finite range](../science/interpretation.md#finite-size-statements-and-accessible-range).

### M23. Local Bell links with reusable interiors

**Central question:** How can the same physical chain provide both entangled links and space for protecting their measurement records?

**Understanding target:** Partition the existing $N$ sites into balanced contiguous segments of minimum length $2r+2$, when at least two segments fit. Prepare a Bell pair on the first two sites of each segment, then move one half to its far boundary by SWAPs. Track the displaced zero states to see that every interior site returns to zero. The parallel link stage costs the largest segment length $B\leq3r+3$.

**Dependencies:** M03, M07, M12, M13.

**Story role and connection:** The construction obtains its ancillary space from the specified array. Returning the link interiors to zero makes the later banks compatible with width one.

**Sources:** [Watrous §§2.2.1–2.2.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf), unitary channels; [chain and bank parameters](../science/construction.md#chain-and-bank-parameters) and [link preparation](../science/construction.md#preparing-the-links-and-returning-their-interiors-to-zero).

### M24. Coherent banks for the two swapping records

**Central question:** How can each junction's two basis labels be distributed locally without consuming the endpoint qubits?

**Understanding target:** Apply all junction Bell-basis rotations in parallel, then fan each $u_j$ leftward and each $v_j$ rightward through $r$ adjacent zero qubits. Verify the disjointness of the two banks in every internal segment and their exclusion of the global endpoints. Interpret fanout coherently in the computational-basis branches, preserving their probabilities and endpoint Bell labels. Only orthogonal labels are copied.

**Dependencies:** M06, M13, M23.

**Story role and connection:** Spatial redundancy costs local depth. The explicit layout makes that cost visible and avoids assuming free distant copies or cloning an arbitrary state.

**Sources:** [Watrous §6.3.1](https://cs.uwaterloo.ca/~watrous/TQI/TQI.6.pdf), Bell-measurement labels; [joining links and creating disjoint banks](../science/construction.md#joining-the-links-and-creating-disjoint-banks).

### M25. Repeated reports and majority decoding

**Central question:** Which samples are independent when many readouts refer to the same physical basis value?

**Understanding target:** Read every bank qubit for $s$ QND rounds, obtaining $(r+1)s$ reports per junction bit. Keep the largest odd sample count $M$ by discarding one predetermined report when necessary. Identify the majority error as the binomial tail $q_M(p)$. Conditional on all true junction bits, decoding errors are independent across banks and have the same probability for either true value.

**Dependencies:** M06, M24.

**Story role and connection:** The basis values within a bank agree; the fresh report flips supply the independent trials. This connects the physical QND schedule to an ordinary repetition decoder without assuming independent quantum outcomes.

**Sources:** [Watrous §2.3.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf), repeated instrument use; [the project's exact majority decoder](../science/construction.md#decoding-the-noisy-records).

### M26. Exact physical fidelity from the two error parities

**Central question:** How do local decoding errors determine the averaged corrected endpoint state?

**Understanding target:** Track the residual phase and bit labels after the endpoint correction. Each is the parity of $m-1$ independent decoded errors, and the two parities are independent. Relate the probability that both are even to the exact Bell overlap $F_{m,M}(p)=[(1+(1-2q_M(p))^{m-1})/2]^2$. Distinguish the cancellations captured by this formula from the simpler union bound used for achievability.

**Dependencies:** M11, M13, M25.

**Story role and connection:** This calculation concerns the actual retained pair averaged over every true outcome and report error. It does not assume successful decoding or a favorable postselected transcript.

**Sources:** [Watrous §6.3.1](https://cs.uwaterloo.ca/~watrous/TQI/TQI.6.pdf), Pauli corrections; [§3.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf), fidelity convention; [exact decoding and fidelity](../science/construction.md#decoding-the-noisy-records).

### M27. Balancing spatial and temporal repetition

**Central question:** How does a quadratic number of independent noisy reports fit into a depth that grows only as their square root?

**Understanding target:** Use $q_M(p)\leq e^{-c_pM}$ with $c_p=-\log(2\sqrt{p(1-p)})>0$ and $1-F\leq2(m-1)e^{-c_pM}$. Count the complete native-SWAP schedule as $B+r+s+3$ rounds. Choose $r=s=t$ with $t$ of order $\sqrt{\log(N/(1-F_0))}$ for fixed $p$, yielding $M=t(t+1)-1\geq t^2$ and a fixed-target upper depth of order $\sqrt{\log L}$.

**Dependencies:** M12, M23, M25, M26.

**Story role and connection:** Both local copying and repeated readout are charged. Their product supplies the sample count while their sum determines depth, matching the spacetime structure seen in the converse.

**Sources:** [Watrous §2.3.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf), the underlying measurement formalism; [the project's probability bound](../science/construction.md#decoding-the-noisy-records), [exact quantum costs](../science/construction.md#exact-quantum-costs), and [fixed-fidelity parameter choice](../science/construction.md#choosing-the-parameters-for-a-fixed-fidelity).

### M28. Completing the construction on every finite chain

**Central question:** Does the upper bound remain a valid physical circuit when segment lengths are unequal or too few segments fit?

**Understanding target:** Account for balanced unequal segments without adding sites, all disjoint layers, total physical count $N$, and the constant-factor change when SWAPs use three CNOTs. When fewer than two segments fit, follow centered Bell preparation and simultaneous outward SWAPs, with exact output and depth $1+\lceil N/2\rceil$. Understand why this fallback stays within the stated fixed-target bound. Distinguish finite layout and state checks from the analytical proof for all lengths.

**Dependencies:** M23, M24, M27.

**Story role and connection:** Resource accounting completes the upper bound at finite size. The measurement-free route will also bound what can be claimed at very high target precision.

**Sources:** [Watrous §§2.2.1–2.2.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf), channel composition; [exact costs](../science/construction.md#exact-quantum-costs), [short chains and the unitary fallback](../science/construction.md#short-chains-and-a-unitary-fallback), and [verification scope](../verification/README.md#scope).

### M29. Boundary channels and resource limits

**Central question:** Which changes in noise or task definition alter the claimed depth law?

**Understanding target:** Separate the three regimes: constant depth at $p=0$, the interior theorem for fixed $p$, and linear depth at $p=1/2$. In the last regime, conditioning on the report coins and controller seed leaves predetermined local trace-preserving maps, whose disjoint endpoint cones cannot entangle a product input. Recognize the exact linear-depth unitary route at fidelity one and why the main result is not a uniform vanishing-error law. Keep gate noise, growing-width optimality, distance-dependent classical latency, and mitigated estimators outside the established statement.

**Dependencies:** M08, M10, M12, M22, M28.

**Story role and connection:** These boundaries connect the fixed-parameter theorem to its operational assumptions. They prevent an optimum for one physical task from being treated as a general fault-tolerance or communication-speed theorem.

**Sources:** [Watrous §§2.2.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf) and [6.1.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.6.pdf), channels and LOCC; [three readout regimes](../science/interpretation.md#three-readout-regimes) and [resources determining the statement](../science/interpretation.md#the-resources-that-determine-the-statement).

### M30. One optimal law from two complementary mechanisms

**Central question:** What has been established for all allowed protocols, and why does the explicit circuit attain the same depth order?

**Understanding target:** Combine the adaptive converse and width-one construction to obtain $D_{\min}(L;p,F_0)=\Theta_{p,F_0}(\sqrt{\log L})$ for fixed $p\in(0,1/2)$ and $F_0\in(1/2,1)$. Relate the largest fixed-fidelity range to $\exp[\Theta_{p,F_0}(D^2)]$. Identify the full transcript-output separator as the universal step and charged spatial-temporal repetition as the matching mechanism. Distinguish inherited locality and rare-cut methods from the result for this independent readout-only model, and distinguish proof from finite executable verification.

**Dependencies:** M18, M21, M22, M27, M28, M29.

**Story role and connection:** The complete route connects one noisy instrument to a global optimum. Both mechanisms account for the space and time needed to make measurement records reliable under the specified independent reporting noise.

**Sources:** [Watrous §2.3.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf) and [§6.1.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.6.pdf), foundational instruments and LOCC; [scientific account](../science/README.md), [optimal depth and interpretation](../science/interpretation.md), [attribution and closest models](../references/RELATED_WORK.md), and [verification scope](../verification/README.md#scope).
