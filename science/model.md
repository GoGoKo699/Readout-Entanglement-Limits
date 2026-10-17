# Noisy readout and distant entanglement

Measurement-assisted circuits can connect distant qubits through local entanglement swapping and a global classical correction. With perfect measurement records, the quantum operations can have constant depth. If every record is unreliable, the correction depends on information that must first be recovered from noisy reports. This project asks for the minimum local operation depth needed to deliver a high-fidelity physical Bell pair under that constraint.

The result is a matched law in distance, detector quality, and target accuracy. The classical controller may communicate instantaneously across the entire chain. The obstruction therefore concerns the information supplied by local readout and the quantum resources needed to make that information reliable.

## Scientific route

| Question | Authoritative account |
|---|---|
| What resources and output are specified? | The model and theorem below |
| Why does one unread interior strip destroy endpoint entanglement? | [Blind-strip separability](blind_strip.md) |
| How does readout information enter a universal converse? | [The random-strip information bound](information_bound.md) |
| Can postselection change the accuracy or distance dependence? | [Heralding at fixed success probability](heralding.md) |
| Which local circuit attains the bound? | [Spatial and temporal readout amplification](construction.md) |
| How do the finite bounds give a uniform optimum and crossover? | [The optimal depth law](depth_law.md) |
| What physical limitation does the theorem identify? | [Resource interpretation](interpretation.md) |
| Which ingredients are established prior work? | [Related work](../references/RELATED_WORK.md) |

The geometric lemma supplies the quantum step in the converse. An exact comparison of classical noise distributions then gives its detector and accuracy dependence. The independent construction saturates the resulting order. The theorem does not assume that an arbitrary competing protocol uses entanglement swapping or decodes individual Bell-measurement bits.

## 1. Sites, time, and initial resources

The sites of a one-dimensional line are $`0,1,\ldots,L`$, with fixed output qubits at sites $`0`$ and $`L`$. The distance $`L\ge2`$ is measured in lattice edges. Each site has at most a fixed number $`q\ge1`$ of quantum memory qubits. Local preparation and reset are allowed within that memory bound.

Initially, the quantum state is a product over sites. A shared classical random variable $`\lambda`$ may select the product state and protocol:

```math
\rho_{\mathrm{in}}
=\sum_\lambda \pi(\lambda)
  \bigotimes_{x=0}^{L}\rho_x^{(\lambda)}.
```

One can prove every converse after fixing $`\lambda`$ and then average. Local environments and fresh ancillas do not supply initially shared quantum entanglement. Any quantum system retained for later use is subject to the local memory and propagation constraints.

The depth $`T`$ is a worst-case bound on the number of synchronous operation layers. Adaptive stopping is allowed within that bound and is padded by idle layers. A gate layer consists of parallel local quantum channels with disjoint supports of diameter at most a fixed integer $`r\ge1`$. Its quantum backward cone expands by at most $`r`$ lattice sites in one layer. A readout layer consists of site-local instruments and is counted in $`T`$. Sequential overlapping operations require separate layers. Replacing these elementary layers by a fixed-size local gate schedule only changes fixed constants in the asymptotic result.

Local channels may be arbitrary completely positive trace-preserving maps. Thus local coherent processing, discarding, reset, and additional local noise are allowed in the converse. The operation set for the matching upper bound contains ideal nearest-neighbor CNOT and SWAP gates, one-qubit gates, and local readout. This ideal set already fits one memory qubit per site with repeatable pointer measurements.

The microscopic parameters $`q,r`$ and the report density defined next are held fixed as $`L,p,\epsilon`$ vary. The resource restriction is spatial density as well as gate range: arbitrary amounts of instantaneous parallel local readout are not supplied.

## 2. The report interface

A local binary instrument has completely positive outcome maps $`\mathcal M_0,\mathcal M_1`$ whose sum is trace preserving. A physical outcome $`x\in\{0,1\}`$ is converted to a public report

```math
y=x\oplus e,
\qquad
\Pr(e=1)=p,
\qquad 0<p<\frac12.
```

Every potential report slot has its own independent flip bit. The full flip table is independent of the initial quantum resources and the controller's shared randomness. The controller may know $`p`$ and choose its protocol for the specified $`L,p,\epsilon`$, but it does not know the realized flips. There are at most $`\nu\ge1`$ binary slots per site and layer, with fixed $`\nu`$. A slot is indexed by site, layer, and a local report index. Unused slots can be assigned independent unused flip bits for the proof. A flip bit cannot be reused in another slot.

The instrument, basis, later operations, and choice of which slots are used may depend arbitrarily on previously available public reports. All outcome information entering the classical controller passes through the specified binary symmetric channels. A measurement's presence, duration, reset flag, or other interface cannot carry an additional noiseless copy of its true outcome. Classical choices based only on the public history and shared randomness obey this requirement.

The true outcome can be retained as a local quantum pointer. Such pointers are quantum memory, and any movement or processing of them obeys the local gate rules. This permits coherent copying of orthogonal pointer states before readout. It does not grant the controller an ideal copy of the true outcome.

The physical report channel is **unflagged**. In particular, the controller receives neither the flip bit $`e`$ nor a label identifying a truthful component in an auxiliary erasure decomposition. That qualification matters near $`p=1/2`$: a flagged erasure channel with the same binary marginal is a stronger information resource.

The authoritative model uses site-local reported instruments. A fixed-range instrument implemented by a fixed-depth local circuit and site-local readout inherits the asymptotic theorem with the corresponding depth and memory constants. The exact strip width and report count must then be applied to that implemented circuit. A nonlocal measurement interface cannot be added without accounting for its quantum support and reports.

## 3. Classical control and physical output

Classical computation and global classical communication are ideal and instantaneous. The controller can process the entire public transcript, use shared randomness, adapt the next layer, and determine the final endpoint correction. Physical correction gates are quantum operations and count toward the depth. The stated time is therefore circuit-operation depth, including readout layers, under a free classical-communication convention.

The target Bell state and projector are

```math
|\Phi^+\rangle=\frac{|00\rangle+|11\rangle}{\sqrt2},
\qquad
\Pi=|\Phi^+\rangle\langle\Phi^+|.
```

For deterministic preparation, the two endpoint qubits after all corrections have density operator $`\rho_{AB}`$ and Bell fidelity

```math
F=\operatorname{Tr}(\Pi\rho_{AB})\ge1-\epsilon,
\qquad 0<\epsilon\le\frac14.
```

This convention uses the squared overlap with the pure Bell state. All other registers are discarded. A record of a possibly incorrect Pauli frame alone is not the required output; the physical corrected endpoint state must meet the fidelity target. Nor is a signed estimator of Bell observables, assembled over several executions, an entangled output state.

A heralded protocol also produces a public success flag. Let $`s`$ be its probability of success and $`f`$ the Bell fidelity conditioned on success. The fixed-success version requires

```math
s\ge s_0>0,
\qquad f\ge1-\epsilon,
```

where $`s_0`$ is fixed independently of $`L,p,\epsilon`$. Failure runs still respect the same worst-case depth budget. The dependence of constants on $`s_0`$ is explicit below.

## 4. Detector information and notation

All logarithms are natural. Define the detector bias and information coefficient by

```math
\delta=1-2p,
\qquad
D(p)=-\frac12\log[4p(1-p)]
     =-\frac12\log(1-\delta^2).
```

The same scalar is the relative entropy $`D_{\mathrm{KL}}(\operatorname{Ber}(1/2)\Vert\operatorname{Ber}(p))`$ and the Chernoff information between the two symmetric output laws for latent inputs zero and one. Repeated-readout Chernoff information is an established detector-quality concept; see [D'Anjou](../references/RELATED_WORK.md#danjou2021). The resource theorem connects it to a spatial entanglement-preparation task.

Near an uninformative detector,

```math
D(p)=\frac{\delta^2}{2}+O(\delta^4).
```

| Symbol | Meaning |
|---|---|
| $`L`$ | Endpoint separation in lattice edges |
| $`T`$ | Maximum number of local gate and readout layers |
| $`q,r,\nu`$ | Fixed local memory, gate range, and report-slot density |
| $`p,\delta,D(p)`$ | Report-flip probability, detector bias, and information coefficient |
| $`\epsilon`$ | Target Bell infidelity |
| $`s,s_0`$ | Actual heralding success and a fixed required lower bound |
| $`w,M,k`$ | Width, number, and potential report count of comparison strips |
| $`b,t,m`$ | Construction block length, readout repetitions, and reports per pointer bit |

The strip count and the number of construction boundaries are both denoted $`M`$ within their respective arguments. Each page defines its count before using it. Their common asymptotic order is $`L/T`$ in the intermediate-depth regime.

## 5. Uniform optimal-depth theorem

Let $`T_{\mathrm{det}}(L,\epsilon,p)`$ be the minimum depth over all deterministic protocols in the model. Let $`T_{\mathrm{her}}(L,\epsilon,p;s_0)`$ be the corresponding minimum with success at least $`s_0`$. Define $`\tau>0`$ by

```math
D(p)\tau^2=\log\frac{L}{\epsilon\tau}.
```

The left side is strictly increasing and the right side strictly decreasing, so the solution is unique. Equivalently,

```math
\tau
=\sqrt{\frac{W_0\!\left(2D(p)(L/\epsilon)^2\right)}{2D(p)}},
\qquad
\mathcal T(L,\epsilon,p)=\max\{1,\min\{L,\tau\}\},
```

where $`W_0`$ is the nonnegative principal branch of the Lambert W function.

**Theorem.** For all $`L\ge2`$, $`0<p<1/2`$, and $`0<\epsilon\le1/4`$,

```math
T_{\mathrm{det}}(L,\epsilon,p)=\Theta(\mathcal T(L,\epsilon,p)),
\qquad
T_{\mathrm{her}}(L,\epsilon,p;s_0)=\Theta_{s_0}(\mathcal T(L,\epsilon,p)).
```

The implicit constants in the first relation are independent of all three displayed parameters. They may depend on the fixed local operation and reporting conventions. In the second relation they may additionally depend on $`s_0`$. The converse covers every adaptive protocol in the model; the construction is deterministic and hence also meets every $`s_0\le1`$ requirement.

The [depth-law proof](depth_law.md) combines finite lower bounds with the local construction and handles the microscopic floor, integer block sizes, and coherent linear-depth cap. The concise intermediate-regime form is

```math
D(p)T^2\asymp\log\frac{L}{T\epsilon},
\qquad 1\ll T\ll L.
```

It is not an equality to be applied after either cap becomes active. In particular, the factor $`T`$ in the logarithm cannot be dropped uniformly when the detector quality varies with distance.

## 6. Consequences and interpretation

At fixed detector quality and fixed accuracy, the theorem gives $`T=\Theta(\sqrt{\log L})`$. The construction devotes both spatial copies and repeated readout time to each latent Bell bit. It obtains order $`T^2`$ independent reports per boundary while retaining order $`L/T`$ boundaries.

At fixed accuracy, near uninformative readout, sublinear depth occurs along asymptotic parameter families precisely when $`\delta L\to\infty`$. If $`\delta L`$ stays bounded, optimal depth is linear in $`L`$. With variable accuracy, the corresponding criterion is

```math
\frac{D(p)L^2}{\log(1/\epsilon)}\longrightarrow\infty.
```

These crossover statements follow from the uniform theorem, not from extrapolating a fixed-$`p`$ estimate. The same order survives postselection at fixed success probability because the [heralding bounds](heralding.md) control both the number of candidate cuts and the target accuracy.

The matching construction assumes ideal coherent operations and storage. Its role is to isolate and saturate the remaining readout-information cost. Additional gate and memory errors can increase the resources needed by a physical implementation. The converse still applies when those errors are described by additional local channels within the same report interface.

The geometric framework has explicit antecedents in [measurement-assisted locality](../references/RELATED_WORK.md#friedman2023), and rare-cut converses occur in [quantum-bus analysis](../references/RELATED_WORK.md#choe2024). The distinction of the present resource statement is noise confined to reported classical records at fixed spatial density. The [related-work account](../references/RELATED_WORK.md) identifies imported ingredients and the precise comparison models.

Continue with [blind-strip separability](blind_strip.md) for the quantum reduction, or [the local construction](construction.md) for the protocol that attains the optimum.
