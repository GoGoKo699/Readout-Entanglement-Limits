# The information bound for noisy readout

Randomizing the reports in one sufficiently wide strip makes the endpoint state separable. If the location of that strip is chosen uniformly among many disjoint strips, the resulting noise distribution can be close to the actual detector noise. Comparing these two distributions gives a lower bound with the same detector parameter as majority decoding.

This page uses the [model](model.md) and the [blind-strip lemma](blind_strip.md). All logarithms are natural. The detector is an **unflagged** binary symmetric channel with independent crossover probability $`0<p<1/2`$ at every used readout slot. Define

```math
\delta=1-2p,
\qquad
D(p)=-\frac12\log[4p(1-p)]
=-\frac12\log(1-\delta^2).
```

In particular, $`D(p)=\delta^2/2+O(\delta^4)`$ as the readout approaches a fair coin.

## Finite theorem

Consider a depth-$`T`$ protocol. Choose $`M\ge1`$ disjoint spatial strips, each with width greater than $`2rT`$, and pad each strip to $`k`$ potential readout slots. In the site-local readout model, a convenient choice is

```math
w=2rT+1,
\qquad
k=\nu(2rT+1)T,
\qquad
M=\left\lfloor\frac{L-1}{2rT+1}\right\rfloor.
```

Let $`F>1/2`$ be the fidelity of the unconditional endpoint state with one fixed Bell state, including the protocol's report-dependent endpoint corrections.

**Theorem.** Every such protocol satisfies

```math
2kD(p)\ge\log\left[1+M(2F-1)^2\right],
```

and

```math
2kD(p)\ge
\log\left\{1+M\left([4F(1-F)]^{-1/2}-1\right)\right\}.
```

For $`F=1`$, the second right-hand side is infinite. Thus exact Bell preparation is impossible at finite depth whenever a strip fits and $`p>0`$. The theorem makes no such assertion in the linear-depth regime where no strip fits.

## A common protocol map for every readout table

Presample a flip bit $`e_z`$ for every potential site/layer/readout-index address $`z`$. Include idle slots, and use each address at most once. The table is independent of the initial quantum resources and the controller's shared randomness, as required by the memoryless BSC model. Its actual distribution is the product measure

```math
P(e_z=1)=p,
\qquad P(e_z=0)=1-p.
```

When a measurement with physical outcome $`x_z`$ is performed at that address, its public report is $`y_z=x_z\oplus e_z`$. Adaptive choices determine which slots are used and which instruments are applied, using earlier reports. The controller never receives $`e_z`$ itself.

For a fixed complete table $`e`$, run the same protocol and average over its intrinsic quantum outcomes and any independent controller randomness. This produces a normalized endpoint state $`\rho(e)`$. Early termination is handled by assigning a normalized output to every branch and leaving the remaining slots idle.

Consequently one common classical-to-quantum CPTP map describes the protocol under any table distribution $`R`$:

```math
\mathcal P(R)=\sum_e R(e)\rho(e).
```

Changing $`R`$ changes only the distribution of the detector noise. The controller's rule, measurement instruments, and quantum operations remain the same. This representation permits a distributional comparison without giving the controller access to the table.

## Random-strip alternatives

For strip $`j`$, let $`Q_j`$ replace its $`k`$ flip bits by independent fair bits and agree with $`P`$ everywhere else. All table bits remain independent under $`Q_j`$.

A fair flip bit makes the reported value a fair coin independent of the true outcome, conditional on the preceding history and the chosen instrument. Therefore strip $`j`$ is blind, even for an adaptive schedule. The [blind-strip lemma](blind_strip.md#blind-strip-lemma) implies that $`\mathcal P(Q_j)`$ is separable.

Now define

```math
Q=\frac1M\sum_{j=1}^M Q_j,
\qquad
\rho=\mathcal P(P),
\qquad
\sigma=\mathcal P(Q).
```

The state $`\sigma`$ is a convex mixture of separable states. The choice of the randomized strip is part of a mathematical alternative distribution; it is not disclosed to the controller.

### Exact chi-square calculation

Set $`R_j(e)=Q_j(e)/P(e)`$. Full support of $`P`$ makes these ratios finite. Each ratio depends only on the table positions in its strip, so the ratios are independent under $`P`$. Their first and second moments are

```math
\mathbb E_P R_j=1,
```

and

```math
\begin{aligned}
\mathbb E_P R_j^2
&=\left(\frac1{4(1-p)}+\frac1{4p}\right)^k\\
&=[4p(1-p)]^{-k}
=e^{2kD(p)}.
\end{aligned}
```

Since $`Q/P=M^{-1}\sum_jR_j`$, the variances add:

```math
\begin{aligned}
\chi^2(Q\Vert P)
&=\mathbb E_P\left(\frac QP-1\right)^2\\
&=\frac1{M^2}\sum_{j=1}^M\operatorname{Var}_P(R_j)\\
&=\frac{e^{2kD(p)}-1}{M}.
\end{aligned}
```

Unused table positions cause no difficulty. Their distributions are still independent, and replacing the entire padded strip by fair bits still produces a blind strip. Padding may weaken the estimate but does not invalidate it.

## Bell fidelity as a statistical test

Write $`\Pi_\Phi`$ for the fixed Bell projector and define the binary test kernel

```math
f(e)=\operatorname{Tr}[\Pi_\Phi\rho(e)],
\qquad 0\le f(e)\le1.
```

This is a mathematical test of the final state, not an additional readout operation available to the preparation protocol. Under the two table distributions, its success probabilities are

```math
F=\mathbb E_P f,
\qquad
F_0=\mathbb E_Q f\le\frac12,
```

where the last inequality follows from separability of $`\sigma`$.

### Total variation gives the first bound

For a function taking values in $`[0,1]`$,

```math
F-\frac12\le F-F_0\le\operatorname{TV}(P,Q).
```

Cauchy-Schwarz gives

```math
\begin{aligned}
\operatorname{TV}(P,Q)
&=\frac12\mathbb E_P\left|1-\frac QP\right|\\
&\le\frac12\sqrt{\chi^2(Q\Vert P)}.
\end{aligned}
```

Inserting the exact chi-square identity yields

```math
(2F-1)^2\le\frac{e^{2kD(p)}-1}{M},
```

which is the first theorem inequality after rearrangement. An equivalent fidelity estimate is

```math
F\le\frac12+\frac12\min\left\{1,
\sqrt{\frac{e^{2kD(p)}-1}{M}}\right\}.
```

### Reverse relative entropy gives the accuracy dependence

Let $`D_{\mathrm{KL}}`$ denote classical relative entropy and $`d`$ its binary version. Applying the log-sum inequality to the joint distributions of the table and the binary test outcome gives

```math
d(F_0\Vert F)\le D_{\mathrm{KL}}(Q\Vert P).
```

Explicitly, the binary kernel is $`K(1\mid e)=f(e)`$, $`K(0\mid e)=1-f(e)`$. The joint relative entropy of $`Q(e)K(z\mid e)`$ against $`P(e)K(z\mid e)`$ is $`D_{\mathrm{KL}}(Q\Vert P)`$. Summing over $`e`$ and applying the log-sum inequality for each $`z`$ proves the displayed bound.

For $`F_0\le1/2<F`$, the binary divergence is minimized at $`F_0=1/2`$. Hence

```math
d(F_0\Vert F)
\ge d(1/2\Vert F)
=-\frac12\log[4F(1-F)].
```

In the other direction, concavity of the logarithm gives

```math
\begin{aligned}
D_{\mathrm{KL}}(Q\Vert P)
&=\mathbb E_Q\log(Q/P)\\
&\le\log\mathbb E_Q(Q/P)\\
&=\log\left[1+\chi^2(Q\Vert P)\right].
\end{aligned}
```

Combining these inequalities yields

```math
-\frac12\log[4F(1-F)]
\le\log\left[1+\frac{e^{2kD(p)}-1}{M}\right],
```

which rearranges to the second theorem inequality. The separable alternative is the first argument of relative entropy; this direction produces the diverging obstruction as $`F`$ tends to one.

## Accuracy and geometric consequences

For a deterministic protocol with $`F\ge1-\epsilon`$, $`0<\epsilon<1/2`$, the finite high-accuracy bound is

```math
2kD(p)\ge
\log\left\{1+M\left([4\epsilon(1-\epsilon)]^{-1/2}-1\right)\right\}.
```

For $`\epsilon\le\epsilon_0<1/2`$, this controls both $`\log M`$ and $`\log(1/\epsilon)`$ up to constants depending on $`\epsilon_0`$. With fixed density and range, $`k=\Theta(T^2)`$ and $`M=\Theta(L/T)`$ whenever $`T`$ is below a fixed fraction of $`L`$. These are the quantities that enter the [uniform depth law](depth_law.md). In particular, the number of strips decreases as the allowed depth grows.

The elementary erasure estimate in [the blind-strip proof](blind_strip.md#an-elementary-bound-at-fixed-detector-quality) uses $`-\log(2p)`$, which is linear in $`\delta`$ near a fair coin. The information estimate uses $`D(p)`$, which is quadratic in $`\delta`$. The latter dependence applies to the original unflagged BSC. Revealing an additional flag that identifies perfect-read or random-read branches changes the detector interface and is outside this theorem.

At $`p=1/2`$, a fitting strip is already blind under the actual detector, so its endpoint state is separable. At $`p=0`$, the likelihood ratios used above lack full support, and the theorem is not applied. Heralded protocols are treated separately in [heralding.md](heralding.md), including their dependence on conditional infidelity.

## Independent nonuniform readout probabilities

The same comparison gives a finite obstruction for a fixed, independent detector profile $`p_z`$ across potential slots. Assume $`0<p_z<1/2`$, and set

```math
S_j=\sum_{z\in I_j\text{ slots}}D(p_z),
\qquad V_j=e^{2S_j}-1.
```

For mixture weights $`a_j\ge0`$ with $`\sum_j a_j=1`$, define $`Q=\sum_j a_jQ_j`$. Its output remains separable. Independence of disjoint strip ratios gives

```math
\chi^2(Q\Vert P)=\sum_j a_j^2V_j.
```

Cauchy-Schwarz shows that the minimizing weights and value are

```math
a_j=\frac{V_j^{-1}}{\sum_iV_i^{-1}},
\qquad
\chi^2_{\min}=\left(\sum_j\frac1{V_j}\right)^{-1}.
```

Thus the two Bell-fidelity bounds become

```math
(2F-1)^2
\le\left(\sum_j\frac1{e^{2S_j}-1}\right)^{-1},
```

and

```math
-\frac12\log[4F(1-F)]
\le\log\left[1+\left(\sum_j\frac1{e^{2S_j}-1}\right)^{-1}\right].
```

The profile must be specified independently of the unknown physical outcomes. These inequalities are an obstruction for heterogeneous detectors; they do not assert a matching construction for every profile. If every detector in one strip is exactly a fair coin, that strip is already blind and separability follows directly.
