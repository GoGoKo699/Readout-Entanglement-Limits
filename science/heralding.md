# Heralding probability and conditional accuracy

Postselection can improve a prepared state's fidelity by reducing the probability of obtaining it. The lower bound therefore keeps the heralding probability explicit. At success probability bounded below by a constant, heralding obeys the same depth scaling as deterministic preparation, including its dependence on the target infidelity.

Use the [model](model.md), the [blind-strip lemma](blind_strip.md), and the readout-table representation in the [information bound](information_bound.md). The herald is determined by the allowed public information. A fresh unknown physical outcome cannot be used directly as an ideal heralding signal.

There are $`M\ge1`$ disjoint blind-strip alternatives, with $`k`$ potential readout slots in each. Define

```math
\delta=1-2p,
\qquad
D(p)=-\frac12\log[4p(1-p)],
\qquad 0<p<1/2.
```

For the site-local readout convention, one can use

```math
w=2rT+1,
\qquad k=\nu wT,
\qquad M=\left\lfloor\frac{L-1}{w}\right\rfloor.
```

Let $`s>0`$ be the actual success probability, and let $`F_s=1-\epsilon>1/2`$ be the Bell fidelity conditioned on success.

## Finite heralded bounds

**Theorem.** Every allowed heralded protocol satisfies

```math
2kD(p)\ge\log\left[1+Ms^2(1-2\epsilon)^2\right],
```

and

```math
\epsilon\ge
\frac{s^3}{4(1+\delta^2)^{2k}e^{2kD(p)}}
\ge\frac{s^3}{4}e^{-6kD(p)}.
```

Equivalently, the second inequality gives

```math
kD(p)\ge\frac16\log\frac{s^3}{4\epsilon}.
```

This last logarithmic form can be vacuous when its right-hand side is negative. The exact lower bound on $`\epsilon`$ is positive for every $`s>0`$ and finite $`k`$. In particular, exact conditional Bell preparation is impossible in the strip regime at nonzero success probability and $`p>0`$.

The proof separates the two requirements. Mixing the location of a blind strip controls the geometric dependence on $`M`$. A comparison with one blind strip controls how accurately the accepted branch can approach a Bell state.

The [elementary erasure-component argument](blind_strip.md#an-elementary-bound-at-fixed-detector-quality) also gives $`s(2F_s-1)\le[1-(2p)^k]^M`$. It is useful for every fixed target above $`1/2`$, but its detector coefficient does not replace the uniform unflagged-BSC bounds proved here.

## Accepted output as a function of the error table

Let $`P`$ be the actual independent BSC flip-table distribution. For a fixed complete table $`e`$, write $`\omega_{\mathrm{acc}}(e)`$ for the unnormalized endpoint operator on the accepted branch, after averaging intrinsic outcomes and independent controller randomness.

Define

```math
h(e)=\mathrm{Tr}\,\omega_{\mathrm{acc}}(e),
\qquad
b(e)=\mathrm{Tr}[(\mathbf1-\Pi_\Phi)\omega_{\mathrm{acc}}(e)].
```

These functions satisfy $`0\le b(e)\le h(e)\le1`$. The actual success probability and conditional infidelity give

```math
\mathbb E_P h=s,
\qquad
\mathbb E_P b=s\epsilon.
```

The Bell projector is used only to evaluate the endpoint state. It does not represent an extra operation granted to the preparation protocol.

For any one random-strip distribution $`Q_j`$, the blind-strip lemma applies to the accepted branch itself. Therefore

```math
\mathbb E_{Q_j}b\ge\frac12\mathbb E_{Q_j}h.
```

This inequality is valid even if the success probability under $`Q_j`$ differs from $`s`$. It also avoids dividing by a counterfactual success probability that might be small.

## Geometry at a fixed success probability

For the statistical comparison, replace the rejected branch by $`|00\rangle\langle00|`$, whose overlap with $`\Pi_\Phi`$ is $`1/2`$. Equivalently, define the table test

```math
\widetilde f(e)
=\mathrm{Tr}[\Pi_\Phi\omega_{\mathrm{acc}}(e)]
+\frac12[1-h(e)].
```

This function lies in $`[0,1]`$. The replacement is an analytical postprocessing of the original output and herald. The depth $`T`$, and hence $`k`$ and $`M`$, continue to describe the original protocol.

Under the actual table distribution,

```math
\mathbb E_P\widetilde f
=\frac12+s\left(\frac12-\epsilon\right).
```

Under any $`Q_j`$, the accepted branch is separable and the rejected replacement is a product state. Hence $`\mathbb E_{Q_j}\widetilde f\le1/2`$. The same is true for the mixture $`Q=M^{-1}\sum_jQ_j`$.

The chi-square calculation in [the information proof](information_bound.md#exact-chi-square-calculation) gives

```math
\chi^2(Q\Vert P)=\frac{e^{2kD(p)}-1}{M}.
```

Applying the total-variation estimate to $`\widetilde f`$ yields

```math
s(1-2\epsilon)
\le\sqrt{\frac{e^{2kD(p)}-1}{M}}.
```

Rearrangement proves the first heralded inequality.

## Conditional accuracy from two likelihood-ratio moments

Fix one strip and write $`Q=Q_j`$ in this section. Introduce the likelihood ratios

```math
\Lambda(e)=\frac{P(e)}{Q(e)},
\qquad R(e)=\frac{Q(e)}{P(e)}.
```

All ratios are finite because $`0<p<1/2`$. Only the $`k`$ replaced slots contribute to their moments.

For one replaced slot,

```math
\mathbb E_Q \Lambda^2
=2(1-p)^2+2p^2
=1+\delta^2.
```

For the complete table this gives

```math
\mathbb E_Q \Lambda^2=(1+\delta^2)^k,
\qquad
\mathbb E_P R^2=e^{2kD(p)}.
```

The first moment comparison controls acceptance under the blind-strip distribution. Cauchy-Schwarz, followed by $`h^2\le h`$, gives

```math
\begin{aligned}
s^2
&=\left(\mathbb E_Q[\Lambda h]\right)^2\\
&\le\mathbb E_Q \Lambda^2\,\mathbb E_Q h^2\\
&\le(1+\delta^2)^k\,\mathbb E_Qh.
\end{aligned}
```

Thus

```math
\mathbb E_Qh\ge\frac{s^2}{(1+\delta^2)^k}.
```

The second comparison controls accepted Bell-test failures. Using $`b^2\le b`$,

```math
\begin{aligned}
\left(\mathbb E_Qb\right)^2
&=\left(\mathbb E_P[Rb]\right)^2\\
&\le\mathbb E_P R^2\,\mathbb E_Pb^2\\
&\le e^{2kD(p)}s\epsilon.
\end{aligned}
```

Conditional separability supplies the relation between these two comparisons:

```math
\frac{s^2}{2(1+\delta^2)^k}
\le\frac12\mathbb E_Qh
\le\mathbb E_Qb
\le e^{kD(p)}\sqrt{s\epsilon}.
```

Squaring and dividing by $`s>0`$ proves

```math
\epsilon\ge
\frac{s^3}{4(1+\delta^2)^{2k}e^{2kD(p)}}.
```

Finally,

```math
\log(1+\delta^2)
\le-\log(1-\delta^2)=2D(p),
```

because $`(1+\delta^2)(1-\delta^2)\le1`$. Substitution gives the simpler $`s^3e^{-6kD(p)}/4`$ bound and completes the proof.

## Constant-success consequence

Suppose $`s\ge s_0>0`$ and $`0<\epsilon\le\epsilon_0<1/2`$, with $`s_0`$ and $`\epsilon_0`$ fixed. The first bound implies

```math
kD(p)\ge c_1\log(1+M)
```

for a constant $`c_1>0`$ depending only on $`s_0,\epsilon_0`$. For example, concavity of the logarithm permits

```math
c_1=\frac12s_0^2(1-2\epsilon_0)^2.
```

The second bound gives

```math
kD(p)\ge
\frac16\left[\log(1/\epsilon)-\log(4/s_0^3)\right].
```

Together these imply

```math
kD(p)\ge
c\left[\log(1+M)+\log(1/\epsilon)\right]
```

for some fixed $`c>0`$ depending on $`s_0,\epsilon_0`$. To see that the additive constant causes no difficulty, split into $`\log(1/\epsilon)\ge2\log(4/s_0^3)`$ and its complement. In the first case the accuracy bound controls $`\log(1/\epsilon)/12`$. In the second, that logarithm is bounded by a constant, which is absorbed by the geometric bound because $`M\ge1`$.

Using $`k=\Theta(T^2)`$ and $`M=\Theta(L/T)`$ gives the same necessary condition as deterministic preparation, up to constants:

```math
D(p)T^2\gtrsim\log\frac{L}{T\epsilon}.
```

The finite inequalities retain the dependence on $`s`$ when success is allowed to decay. The constant-success conclusion should not be extended to arbitrarily rare postselection without that dependence.

## Exact-erasure form

The independent blind-strip events from [the elementary erasure bound](blind_strip.md#an-elementary-bound-at-fixed-detector-quality) have probability $`(2p)^k`$ each. Let $`G`$ be the event that none of the $`M`$ strips is blind. Then

```math
\Pr(G)=[1-(2p)^k]^M.
```

The accepted endpoint operator on $`G^{\mathrm c}`$ is separable. Its Bell overlap is at most half its trace. The accepted operator on $`G`$ has Bell overlap at most its trace. Therefore

```math
sF_s\le\frac12s+\frac12\Pr(\mathrm{accept}\cap G)
\le\frac12s+\frac12[1-(2p)^k]^M,
```

and

```math
F_s\le\frac12+\frac{[1-(2p)^k]^M}{2s}.
```

This form can be useful at fixed $`p`$. The information and moment bounds above provide the sharper dependence as the unflagged detector approaches a fair coin.
