# The information cost of measurement-assisted entanglement

The [optimal-depth theorem](model.md#5-uniform-optimal-depth-theorem) identifies a specific resource in a dynamic quantum circuit: reliable classical information about local measurement outcomes. Using measurements to improve on coherent propagation requires this information even with perfect coherent control and instantaneous classical communication. Spatial pointer copies and repeated readout can supply it, and their local cost determines the achievable entanglement range.

## 1. Why reported outcomes matter

Consider a sequence of short Bell links. A Bell measurement between two adjacent links joins their distant endpoints. Its two outcome bits determine a Pauli correction. Repeating this operation along the line leaves only two global parities to correct, even though the intermediate measurement record contains many bits.

The number of final correction bits therefore does not determine their acquisition cost. Each is a parity of many locally generated outcomes. One unrecognized report flip can reverse a parity and apply the wrong endpoint correction.

For a simple unamplified swapping protocol with $`M`$ independent fusion boundaries, suppose each latent Bell bit is reported once through a binary symmetric channel with error $`p`$. The probability that a parity of $`M`$ report errors is even is

```math
P_{\mathrm{even}}=\frac{1+(1-2p)^M}{2}.
```

The two Pauli parities have independent error patterns, so the final Bell fidelity is

```math
F_{\mathrm{simple}}
=\left[\frac{1+(1-2p)^M}{2}\right]^2.
```

For any fixed nonzero $`p`$, this particular protocol approaches fidelity $`1/4`$ as the number of boundaries grows. That calculation diagnoses an unprotected correction rule. The universal converse needs a different argument because a more capable protocol can amplify, encode or adapt its measurements rather than accept those raw errors.

The [information bound](information_bound.md) permits all such processing. It proves that every fixed-depth protocol in the model eventually loses its fixed Bell-fidelity advantage above the separable threshold $`1/2`$. Preparing the product state $`|00\rangle`$ already attains that threshold, so the converse is about an actual entanglement advantage.

## 2. The quantum role of an unread strip

The central comparison removes all measurement information from one sufficiently wide interior strip. The strip is not deleted, and its qubits may still undergo arbitrary allowed local quantum operations. Its reports simply become independent fair bits.

If the strip is wider than twice the quantum cone radius available in depth $`T`$, endpoint entanglement cannot pass through it by coherent propagation alone. With no informative outcomes from inside, conditioning the public record does not supply the missing connection. The precise statement is [blind-strip separability](blind_strip.md), including states conditioned on a public success event.

This step distinguishes the argument from a classical reliability calculation. It places the comparison output inside the separable set for every adaptive quantum protocol. The Bell projector then provides a common operational test: its expectation is at most one half for every comparison state, while the actual protocol aims for a value close to one.

The quantum operations in the original protocol are left unchanged in every comparison. Its controller does not receive the index of the blinded strip and is not retuned for a different detector model. The single common map from the complete report-flip table to the output state makes this condition exact.

## 3. Why the local information budget scales as depth squared

A depth-$`T`$ quantum causal cone has spatial radius of order $`T`$. A candidate strip that interrupts the two retained cones therefore has width of order $`T`$. With at most a fixed number of reports per site and layer, this strip contains only order $`T^2`$ potential reports over the entire execution.

When $`T`$ is below a fixed sufficiently small fraction of $`L`$, the number of disjoint candidate strips is of order $`L/T`$. The information converse compares the real noise distribution with a mixture in which one of those candidates is fully unread. For equal strip report count $`k`$ and count $`M`$, the exact identity is

```math
\chi^2(Q\Vert P)=\frac{e^{2kD(p)}-1}{M}.
```

The numerator is the statistical cost of making one strip uninformative. The denominator reflects the unknown location of that change. If the two experiments remain close in statistical distance, a high-fidelity Bell output in the real experiment would also occur with substantial probability in a separable comparison experiment. The Bell witness rules that out.

Within this depth regime, the resulting necessary condition at high accuracy is of the same order as

```math
D(p)T^2\gtrsim\log\frac{L}{T\epsilon}.
```

The [uniform depth proof](depth_law.md) treats the microscopic floor and the coherent linear-depth cap explicitly.

This expression has an operational interpretation, but the proof does not assign independently readable hidden Bell bits to an arbitrary protocol. It compares whole adaptive experiments through their physical output.

The mixture and second-moment methods are standard statistical tools. The quantum geometric constraint is what makes each localized alternative an entanglement obstruction. The [related-work account](../references/RELATED_WORK.md) separates these ingredients from the resulting resource theorem.

## 4. How the construction uses space and time

The [attaining circuit](construction.md) creates an ideal Bell link across each block of length $`b`$ and fuses adjacent links locally. It then stores the two latent Bell bits from each fusion as orthogonal quantum pointer states.

Each pointer is copied to order $`b`$ sites within its neighboring block. This is an ordinary controlled copying operation on basis states. It does not copy an unknown quantum state. Every copy is read $`t`$ times, giving order $`bt`$ independent noisy reports of the same latent bit.

The spatial propagation and pointer copying take order $`b`$ gate layers. The repeated reads take $`t`$ layers. Thus

```math
T=\Theta(b+t),
\qquad m=\Theta(bt).
```

Balancing spatial and temporal resources gives $`b\asymp t\asymp T`$ and $`m=\Theta(T^2)`$. The detector's binary discrimination exponent controls majority-decoding error:

```math
e_m(p)\le e^{-D(p)m}.
```

There remain only order $`L/b`$ fusion boundaries. Combining their error probabilities gives the sufficient condition with the same $`\log[L/(T\epsilon)]`$ dependence as the converse.

Temporal repetition alone would allocate only order $`T`$ reports per bit and miss this optimum. Conversely, copying a pointer to distant sites takes local quantum depth; spatial redundancy is not free. The balanced construction respects both costs while using a fixed number of qubits per site.

## 5. Detector quality and the crossover

The coefficient

```math
D(p)=-\frac12\log[4p(1-p)]
```

is the established Chernoff information of the symmetric binary readout laws. Near random reporting, write $`\delta=1-2p`$. Then $`D(p)\sim\delta^2/2`$. A weak bias therefore requires an inverse-square increase in the number of independent reports needed to achieve a fixed discrimination error exponent.

The exact BSC decomposition into a truthful report with probability $`\delta`$ and an independent fair report otherwise can obscure this distinction. If an extra flag reveals which component occurred, an informative result arrives with probability of order $`\delta`$. The unflagged detector considered here does not reveal that event. Its small information per use is of order $`\delta^2`$.

The [erasure-component bound](blind_strip.md#an-elementary-bound-at-fixed-detector-quality) and the sharp information bound consequently answer related but different finite questions. A positive fully erased component is useful for proving separability events. The mixture comparison is needed to obtain the uniform unflagged detector coefficient.

At fixed target accuracy, the sharp crossover is particularly simple:

- If $`\delta L\to\infty`$, the optimal depth is sublinear in $`L`$.
- If $`\delta L`$ is bounded, the optimum is of order $`L`$.

For example, take $`D(p_L)=\log L/L^2`$ at fixed accuracy. Then

```math
T_{\mathrm{opt}}
=\Theta\!\left(L\sqrt{\frac{\log\log L}{\log L}}\right).
```

This is still sublinear. Dropping the $`T`$ inside the logarithm of the intermediate-depth law would incorrectly predict linear depth. The [uniform theorem](depth_law.md) keeps the changing number of fusion interfaces and includes the exact coherent $`O(L)`$ alternative when measurement assistance ceases to improve the asymptotic order.

With variable accuracy, the criterion becomes $`D(p)L^2/\log(1/\epsilon)\to\infty`$. Very demanding accuracy can activate the coherent linear-depth alternative even for a detector that is useful at fixed fidelity.

The endpoint channels can be treated directly, separately from the theorem's open interval $`0<p<1/2`$:

| Readout channel | Optimal depth at fixed $`F_0\in(1/2,1)`$ | Mechanism |
|---|---:|---|
| Perfect reports, $`p=0`$ | $`\Theta(1)`$ | Fixed-size Bell links, simultaneous swapping, exact correction |
| Fixed informative noise, $`0<p<1/2`$ | $`\Theta_{p,F_0}(\sqrt{\log L})`$ | Spatial copies and repeated reports match the converse |
| Independent fair reports, $`p=1/2`$ | $`\Theta(L)`$ | Only local coherent propagation can supply endpoint entanglement |

For $`p=0`$, fixed-size blocks and one readout layer make the [construction](construction.md) exact. At $`p=1/2`$, fix every independent report coin, the controller's randomness, and the initial shared random variable $`\lambda`$. The selected operations are then a predetermined local CPTP circuit: true outcomes are summed out, and any retained quantum pointer remains part of that circuit. Disjoint endpoint backward cones factor on the resulting product input. Averaging the fixed classical variables preserves separability, including for any accepted subset of public records. Thus fidelity above $`1/2`$ requires linear depth. Central Bell preparation followed by outward SWAPs provides the exact linear-depth upper bound without using readout. The middle row includes the lower-fidelity targets by the [fixed-fidelity corollary](depth_law.md#every-fixed-target-above-the-separable-threshold).

## 6. What constant-success postselection can change

Postselection may substantially improve a finite experiment's conditional fidelity. The cost is its probability of success. A universal comparison must track both.

The blind-strip comparison state stays separable after a public acceptance event. The mixture witness gives a finite constraint on $`s(2f-1)`$, while a separate two-sided likelihood-moment argument controls the high-accuracy limit. Together they yield the same optimal order whenever $`s\ge s_0>0`$ independently of distance, detector quality and target error.

This does not identify the optimal constant prefactor or rule out a useful finite-size improvement from error detection. It states that fixed-yield postselection cannot change the asymptotic depth order in this model. If yield is allowed to vanish with the problem parameters, it is a different optimization problem. The exact inequalities in [the heralding account](heralding.md) retain the success probability for assessing that distinction.

## 7. Ideal coherent control and physical implementations

The matching construction isolates measurement-report noise. It assumes ideal coherent gates and memories, together with reliable storage of a basis pointer between repeated reads. A larger block increases coherent propagation and storage time. On hardware with nonzero gate or memory noise, those operations introduce additional error and can require further protection.

The theorem therefore gives a fundamental resource cost after coherent control has been idealized. It does not assign numerical crossover distances to a specific device. A hardware implementation must supply its gate, memory, readout and communication models before converting the asymptotic law into a performance prediction.

The converse has a broader robustness role. Additional local quantum channels cannot remove the readout-information obstruction while the initial-resource, propagation, density and reporting assumptions remain unchanged. Fault-tolerance resources that increase local density, introduce a different graph, or supply initially encoded entanglement must be counted in the model used for that implementation.

Similarly, instantaneous classical communication is a deliberate convention. It allows a clean comparison of quantum operation depths. A finite signal speed contributes its own physical latency to delivering and using a distant Bell pair; that elapsed-time problem is not the quantity optimized here.

## 8. The resulting resource statement

The main theorem connects three descriptions of the same task. The geometry identifies a strip whose unavailable measurement information forces separability. The statistical comparison measures how difficult it is to distinguish such a strip from the real noisy detector. The constructive circuit invests local space and readout time to reach precisely that information scale.

At fixed detector quality, useful distance grows exponentially in depth squared up to the polynomial interface factor and fixed constants. As readout approaches random guessing, the uniform coefficient locates the transition back to linear coherent preparation. High target accuracy and fixed-success heralding fit the same resource law.

Read [the exact model](model.md), [finite information bounds](information_bound.md), and [constructive uniform proof](depth_law.md) together when applying these conclusions. The [finite verification](../verification/README.md) checks the circuit's implemented branch structure and corrections; the universal and asymptotic statements follow from the analytical arguments.
