# The uniform optimal depth law

The optimal depth is determined by the competition between local coherent propagation and the number of reliable reports needed to join the remaining intervals. Both bounds retain the number of intervals, which is of order $`L/T`$. Replacing it by $`L`$ loses the uniform dependence on detector quality.

The [model](model.md) fixes the operation and report interface. The [construction](construction.md) provides the upper bound. The converse uses [blind-strip separability](blind_strip.md), the [random-strip information bound](information_bound.md), and [heralding bounds](heralding.md). This page carries out the inversion, with constants independent of distance, detector quality, and target accuracy.

## 1. Statement

Let $`L\ge2`$, $`0<p<1/2`$, and $`0<\epsilon\le1/4`$. Hold the microscopic memory, gate range, and report density fixed. Write

```math
D=D(p)=-\frac12\log[4p(1-p)]>0.
```

Let $`T_{\mathrm{det}}`$ be the minimum worst-case depth of a deterministic protocol with physical Bell fidelity at least $`1-\epsilon`$. For a fixed $`s_0\in(0,1]`$, let $`T_{\mathrm{her}}`$ be the minimum worst-case depth with success probability at least $`s_0`$ and conditional Bell fidelity at least $`1-\epsilon`$.

Define $`\tau>0`$ by

```math
D\tau^2=\log\frac{L}{\epsilon\tau},
\qquad
\mathcal T=\max\{1,\min\{L,\tau\}\}.
```

**Theorem.** There are constants $`c>0`$ and $`C<\infty`$ such that

```math
\boxed{
c\mathcal T
\le T_{\mathrm{her}}(L,\epsilon,p;s_0)
\le T_{\mathrm{det}}(L,\epsilon,p)
\le C\mathcal T.
}
```

The lower constant may depend on $`r,\nu,s_0`$, and the upper constant on the fixed implementation convention. Neither depends on $`L,p,\epsilon`$. Under the native nearest-neighbor SWAP and QND convention of the construction, one valid upper constant is $`C=15`$. The constants are not optimized.

The construction needs one memory qubit and one simultaneous report per site. It therefore fits every model in the stated family with $`q,\nu\ge1`$ and the required local operations. Taking $`s_0=1`$ gives the deterministic lower bound. A deterministic construction also satisfies every smaller success requirement.

## 2. The inverse scale

The function

```math
g(x)=Dx^2+\log x-\log(L/\epsilon)
```

is continuous and strictly increasing on $`x>0`$, with limits $`-\infty`$ and $`+\infty`$. Its unique zero is $`\tau`$. Rearranging its equation gives

```math
\tau^2 e^{2D\tau^2}=(L/\epsilon)^2,
\qquad
\boxed{
\tau=\sqrt{\frac{W_0\!\left(2D(L/\epsilon)^2\right)}{2D}}.
}
```

Here $`W_0(z)e^{W_0(z)}=z`$ for $`z\ge0`$. The implicit equation is sufficient for the proof; no asymptotic expansion of Lambert W is required.

For an elementary comparison, put $`w=W_0(z)`$. The inequalities

```math
e^w\le1+we^w\le e^{2w}
```

hold for $`w\ge0`$. The first follows from $`e^{-w}\ge1-w`$; the second from $`2\sinh w\ge w`$. Taking logarithms proves

```math
\frac12\log(1+z)\le W_0(z)\le\log(1+z).
```

Consequently

```math
\frac{\log[1+2D(L/\epsilon)^2]}{4D}
\le\tau^2
\le\frac{\log[1+2D(L/\epsilon)^2]}{2D}.
```

The same depth order can therefore be expressed using $`\sqrt{\log[1+D(L/\epsilon)^2]/D}`$, followed by the microscopic floor and linear cap.

## 3. Uniform constructive upper bound

Set

```math
x=\max\{1,\tau\},
\qquad b=2\lceil x\rceil,
\qquad t=b,
\qquad n=L+1.
```

The block length $`b`$ is even and satisfies $`2x\le b\le4x`$. Also,

```math
Dx^2\ge\log\frac{L}{\epsilon x},
```

because $`x\ge\tau`$ and $`g`$ is increasing.

### At least two blocks fit

Suppose $`n\ge2b`$. Use the explicit unequal-block partition in the [construction](construction.md#5-an-explicit-partition-for-every-chain-length). Its block lengths lie in $`[b,2b-1]`$, its boundary count obeys $`M<n/b`$, and every latent bit receives at least $`b^2/2`$ reports. Thus

```math
\begin{aligned}
1-F
&\le2M e^{-Db^2/2}\\
&\le\frac{n}{x}e^{-2Dx^2}\\
&\le\frac{n}{x}\left(\frac{\epsilon x}{L}\right)^2
=\frac nL\frac xL\epsilon^2.
\end{aligned}
```

Since $`L\ge2`$, $`n/L\le3/2`$. The condition $`n\ge2b\ge4x`$ gives $`x/L\le3/8`$. Therefore

```math
1-F\le\frac9{16}\epsilon^2<\epsilon.
```

The schedule has

```math
T\le2b+t+3=3b+3\le6x+9\le15x.
```

In this case $`x\le3L/8<L`$, so $`\mathcal T=x`$ and $`T\le15\mathcal T`$.

### Fewer than two blocks fit

If $`n<2b`$, use the exact unitary Bell-distribution circuit. Its depth is

```math
T_{\mathrm{unit}}
=\left\lceil\frac n2\right\rceil+1
\le\frac32L.
```

Moreover $`L<n<2b\le8x`$, so $`T_{\mathrm{unit}}<12x`$. These two inequalities imply

```math
T_{\mathrm{unit}}\le12\min\{L,x\}=12\mathcal T.
```

This circuit has fidelity one and success one for every $`p`$. It supplies the linear cap without extrapolating an amplification estimate beyond the size of the chain.

The two cases prove the upper bound. They also cover $`\tau<1`$: the choice $`x=1`$ uses fixed-size blocks and a fixed number of readouts. Thus the microscopic floor follows from an actual bounded-depth construction, not an informal cutoff of a vanishing expression.

## 4. A uniform lower estimate before inversion

The [information bound](information_bound.md) and [heralding analysis](heralding.md) give, whenever $`M\ge1`$ disjoint blind strips fit,

```math
s(2f-1)
\le\sqrt{\frac{e^{2kD}-1}{M}},
\qquad
\epsilon\ge\frac{s^3}{4}e^{-6kD}
```

for a protocol with $`s\ge s_0`$ and $`f\ge1-\epsilon`$. Their definitions are

```math
w=2rT+1,
\qquad k=\nu wT,
\qquad M=\left\lfloor\frac{L-1}{w}\right\rfloor.
```

The first inequality controls the number of possible strips; the second controls high accuracy even after heralding. The following calculation shows explicitly that their combination is uniform in $`\epsilon`$.

Let

```math
y=kD,
\qquad a=\frac{s_0^2}{4},
\qquad y_0=\frac12\log(1+a)>0.
```

Because $`2f-1\ge1-2\epsilon\ge1/2`$,

```math
e^{2y}\ge1+aM,
\qquad y\ge y_0,
\qquad \log M\le2y+\log(1/a).
```

The accuracy inequality gives

```math
\log(1/\epsilon)\le6y+\log(4/s_0^3).
```

Adding the two bounds, and using $`y\ge y_0`$ to absorb the constant, yields

```math
\log\frac M\epsilon
\le\left[8+\frac{\log(16/s_0^5)}{y_0}\right]y.
```

Hence a permissible constant is

```math
\kappa_{s_0}
=\left[8+\frac{\log(16/s_0^5)}{\tfrac12\log(1+s_0^2/4)}\right]^{-1}>0,
\qquad
\boxed{kD\ge\kappa_{s_0}\log\frac M\epsilon.}
```

This argument avoids an additive term depending on $`\epsilon`$ or a tacit restriction to extremely small target error. Only the fixed success threshold enters $`\kappa_{s_0}`$.

For deterministic preparation, one can instead use the sharper finite comparison directly:

```math
kD\ge\frac12\log\!\left[
1+M\left(\frac1{\sqrt{4\epsilon(1-\epsilon)}}-1\right)
\right].
```

The unified heralded estimate above is sufficient to prove the order for both tasks.

## 5. Strip packing and inversion

An initially separable state cannot meet the Bell target with zero quantum layers, even after classical heralding. Thus $`T\ge1`$.

Put

```math
A_r=2r+1,
\qquad B_r=4A_r.
```

First suppose $`T\le L/B_r`$. Since $`T\ge1`$,

```math
w\le A_rT,
\qquad k\le\nu A_rT^2.
```

Using $`L-1\ge L/2`$ and the fact that $`(L-1)/w\ge2`$, the floor obeys

```math
M\ge\frac{L-1}{2w}\ge\frac{L}{B_rT}\ge1.
```

Let $`H_T=\log[L/(T\epsilon)]`$. Because $`L/T\ge B_r`$ and $`\epsilon\le1/4`$,

```math
H_T\ge\log(4B_r),
\qquad
\log\frac M\epsilon
\ge H_T-\log B_r
\ge\frac{\log4}{\log(4B_r)}H_T.
```

Combining these estimates with the preceding lower bound gives

```math
DT^2\ge c_1\log\frac{L}{T\epsilon},
\qquad
c_1=
\frac{\kappa_{s_0}\log4}
     {\nu A_r\log(4B_r)}>0.
```

If $`T<\tau`$, the right-side logarithm is larger than $`\log[L/(\tau\epsilon)]=D\tau^2`$. Hence $`T\ge\sqrt{c_1}\tau`$. If $`T\ge\tau`$, no inversion is needed. Together these cases imply

```math
T\ge\sqrt{\min\{1,c_1\}}\,\tau
\qquad\text{when }T\le L/B_r.
```

In the remaining regime, $`T>L/B_r`$ already implies $`T\ge B_r^{-1}\min\{L,\tau\}`$. Therefore, with

```math
c=\min\!\left\{\frac1{B_r},\sqrt{\min\{1,c_1\}}\right\},
```

every allowed protocol satisfies $`T\ge c\min\{L,\tau\}`$. Combining this with $`T\ge1`$ and $`c\le1`$ proves

```math
T\ge c\max\{1,\min\{L,\tau\}\}=c\mathcal T.
```

The displayed constants establish the required uniform quantifiers. No limit with fixed $`p`$ or fixed $`\epsilon`$ was taken in the proof.

## 6. Detector and accuracy regimes

For fixed $`p\in(0,1/2)`$ and fixed accuracy, $`D`$ is a positive constant and the theorem reduces to

```math
T_{\mathrm{opt}}=\Theta(\sqrt{\log L}).
```

### Every fixed target above the separable threshold

**Corollary.** Fix $`p\in(0,1/2)`$ and $`F_0\in(1/2,1)`$ independently of $`L`$. The minimum deterministic depth for physical Bell fidelity at least $`F_0`$ is $`\Theta_{p,F_0}(\sqrt{\log L})`$. With a fixed success threshold $`s_0\in(0,1]`$, the minimum depth for conditional fidelity at least $`F_0`$ is $`\Theta_{p,F_0,s_0}(\sqrt{\log L})`$.

This includes $`F_0<3/4`$, outside the displayed uniform theorem's accuracy domain. For the lower bound, the [finite heralded witness inequality](heralding.md#finite-heralded-bounds) gives

```math
2kD(p)\ge\log\left[1+M s_0^2(2F_0-1)^2\right].
```

For $`T=o(L)`$, the strip count is $`M=\Theta(L/T)`$ and $`k=O(T^2)`$. If $`T=o(\sqrt{\log L})`$, the left side is $`o(\log L)`$ while the right side is $`(1-o(1))\log L`$, a contradiction. More quantitatively, taking $`T\le c\sqrt{\log L}`$ with a sufficiently small fixed $`c>0`$ gives the same contradiction for all sufficiently large $`L`$. Depths of order $`L`$ already satisfy the claimed lower bound. For deterministic preparation take $`s_0=1`$.

For the upper bound, use the existing deterministic construction with target fidelity $`\max\{F_0,3/4\}`$. Its target infidelity lies in $`(0,1/4]`$, so the uniform theorem supplies depth $`O_{p,F_0}(\sqrt{\log L})`$ and success probability one. Constants in this corollary may depend on the fixed gap $`F_0-1/2`$; no uniform claim is made as that gap vanishes.

### Variable accuracy and detector quality

At fixed detector quality but variable accuracy, the usual expression

```math
T_{\mathrm{opt}}
=\Theta\!\left(\min\{L,\sqrt{\log(L/\epsilon)}\}\right)
```

also follows, with constants depending on that fixed $`p`$. It cannot be made uniform merely by placing $`D`$ in its denominator.

For example, hold accuracy fixed and choose

```math
D(p_L)=\frac{\log L}{L^2}.
```

The uniform law gives

```math
T_{\mathrm{opt}}
=\Theta\!\left(L\sqrt{\frac{\log\log L}{\log L}}\right)=o(L).
```

The expression $`\min\{L,\sqrt{\log(L/\epsilon)/D}\}`$ would instead predict linear depth. The discrepancy comes from its replacement of the boundary count $`L/T`$ by $`L`$.

For weak detector bias $`\delta=1-2p`$,

```math
D=-\frac12\log(1-\delta^2)
=\frac{\delta^2}{2}+O(\delta^4).
```

The inverse bias in the intermediate-depth scale reflects the $`\delta^{-2}`$ report count required to distinguish the two almost identical report distributions. The construction supplies reports through both space and time, giving an area of order $`T^2`$ per boundary.

## 7. The coherent crossover

Consider an asymptotic family with $`L\to\infty`$, allowing both $`p`$ and $`\epsilon`$ to vary within the theorem's domain. Put

```math
S=D(p)L^2,
\qquad H=\log(1/\epsilon),
\qquad z=\frac\tau L.
```

The inverse equation becomes

```math
Sz^2=H+\log(1/z),
\qquad
z^2=\frac{W_0(2Se^{2H})}{2S}.
```

If the optimal depth is $`o(L)`$, the uniform theorem implies $`z\to0`$. Eventually $`z<1`$, so $`H/S\le z^2\to0`$. Conversely, if $`S/H\to\infty`$, then $`S\to\infty`$ because $`H\ge\log4`$. The elementary Lambert bound gives

```math
z^2
\le\frac{\log(1+2Se^{2H})}{2S}
\le\frac{2H+\log(1+2S)}{2S}
\longrightarrow0.
```

The microscopic floor contributes only $`1/L`$ to the depth ratio. Therefore

```math
\boxed{
T_{\mathrm{opt}}=o(L)
\quad\Longleftrightarrow\quad
\frac{D(p)L^2}{\log(1/\epsilon)}\longrightarrow\infty.
}
```

At fixed accuracy this becomes $`D(p)L^2\to\infty`$. Near uninformative readout it is equivalent to $`\delta L\to\infty`$. When $`S\to\infty`$ and the microscopic floor is inactive, the fixed-accuracy ratio is $`\Theta(\sqrt{\log S/S})`$. If $`S`$ remains bounded, the optimum stays proportional to $`L`$.

The theorem and its crossover concern the physical output state at bounded worst-case operation depth. The [interpretation](interpretation.md) discusses the free-classical-control convention, the unflagged detector interface, and the distinction from protocols with noisy coherent links.
