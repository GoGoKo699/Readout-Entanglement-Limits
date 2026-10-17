# Spatial and temporal readout amplification

The construction gives each Bell-measurement pointer both spatial copies and repeated readout time. It uses one quantum memory qubit per chain site. The same qubits first distribute short Bell links and then store the pointers needed to join those links.

The [model](model.md) specifies ideal coherent gates, independent BSC report errors with probability $`p`$, and free global classical processing. This page proves the finite protocol and its fidelity. The [depth law](depth_law.md) chooses its parameters and matches it to the universal converse.

Entanglement swapping and repetition-based readout are established ingredients. The [related-work account](../references/RELATED_WORK.md) identifies the measurement-locality and readout-amplification sources. The resource accounting below combines those ingredients at fixed spatial density.

## 1. Equal blocks and layer conventions

Take $`n=L+1=Kb`$ sites, where $`b\ge2`$ is even. Block $`j`$ has left endpoint $`a_j`$ and right endpoint $`b_j`$. The symbol $`b_j`$ labels a qubit; the unindexed $`b`$ denotes the block length. There are $`M=K-1`$ boundaries. All qubits start in $`|0\rangle`$.

Each layer contains disjoint nearest-neighbor gates or site-local operations. A native SWAP counts as one two-qubit gate, a one-qubit gate counts as one layer, and one QND readout of every selected site counts as one readout layer. Classical processing between layers is free. These conventions are needed for the exact depth below. Compiling a SWAP into several elementary gates changes its constant prefactor.

For a block starting at site $`s`$, the two central sites are $`s+b/2-1`$ and $`s+b/2`$. Prepare a Bell pair on them with a Hadamard followed by CNOT. Then swap its two halves outward in parallel until they reach the block endpoints. The remaining qubits are again in $`|0\rangle`$: each SWAP moves the Bell half into a zero state and leaves a zero state behind.

The complete schedule is as follows. Different blocks and boundaries operate in parallel.

| Stage | Operations | Layers |
|---|---|---:|
| Block Bell links | Central Hadamard, central CNOT, then outward SWAPs | $`b/2+1`$ |
| Boundary decoding | CNOT from $`b_j`$ to $`a_{j+1}`$, then Hadamard on $`b_j`$ | $`2`$ |
| Pointer copying | Nearest-neighbor CNOT chains away from each boundary | $`b/2-1`$ |
| Repeated readout | QND Z readout of every pointer copy, repeated $`t\ge1`$ times | $`t`$ |
| Endpoint correction | One Pauli gate selected by the decoded global parities | $`1`$ |

The left half of a block is reserved for its left endpoint pointer, and the right half for its right endpoint pointer. At each internal boundary, the decoded left qubit is copied leftward into the right half of its block; the decoded right qubit is copied rightward into the left half of the next block. The two domains in an internal block are disjoint. A CNOT chain of depth $`b/2-1`$ creates $`b/2`$ copies of each pointer, including the original.

The outer endpoints $`a_1`$ and $`b_K`$ are retained as the output and are never read. The unused outer half-blocks do not enter the correction. There is no additional quantum memory hidden in the copying step.

Consequently the specified schedule has

```math
\boxed{T=b+t+3,\qquad m=\frac{bt}{2},}
```

where $`m`$ is the number of independent reports per latent boundary bit. If $`K=1`$, no swapping measurement is required; the block Bell-link preparation alone gives an exact output.

## 2. The two Bell byproducts

Let $`u_j`$ denote the Z-basis value of $`b_j`$ after its Hadamard, and let $`v_j`$ denote the value of $`a_{j+1}`$ after the boundary CNOT. Thus $`u_j`$ is the first, left Bell-measurement bit and $`v_j`$ the second, right bit. Define

```math
U=\bigoplus_{j=1}^{M}u_j,
\qquad
V=\bigoplus_{j=1}^{M}v_j.
```

The conditional endpoint state is

```math
\boxed{
|\psi_{u,v}\rangle_{a_1b_K}
=(I\otimes X^V Z^U)|\Phi^+\rangle
}
```

up to a global phase. This fixes the convention: the first bit contributes Z and the second bit contributes X.

To prove the formula, write the product of block links as

```math
\bigotimes_{j=1}^{K}|\Phi^+\rangle_{a_jb_j}
=2^{-K/2}\sum_{x_1,\ldots,x_K}
\bigotimes_{j=1}^{K}|x_j\rangle_{a_j}|x_j\rangle_{b_j}.
```

Boundary decoding followed by selection of $`u_j,v_j`$ imposes

```math
v_j=x_j\oplus x_{j+1}
```

and contributes the Hadamard phase $`(-1)^{u_jx_j}/\sqrt2`$. Therefore

```math
x_j=x_1\oplus\bigoplus_{\ell=1}^{j-1}v_\ell,
\qquad
\sum_{j=1}^{M}u_jx_j
=Ux_1+\chi(u,v)\pmod{2},
```

where

```math
\chi(u,v)=\sum_{j=1}^{M}u_j
                 \left(\bigoplus_{\ell=1}^{j-1}v_\ell\right)\pmod{2}.
```

Only the two terms $`x_1=0,1`$ remain. If $`\mathcal B`$ denotes the product of the boundary CNOT-Hadamard decoders, their unnormalized endpoint vector is exactly

```math
\langle u,v|\mathcal B
\bigotimes_{j=1}^{K}|\Phi^+\rangle_{a_jb_j}
=2^{-M}(-1)^{\chi(u,v)}
 (I\otimes X^VZ^U)|\Phi^+\rangle.
```

Every one of the $`4^M`$ outcome strings has probability $`4^{-M}`$. In particular, the $`2M`$ latent bits are independent and uniform.

Pointer copying maps a basis state $`|x\rangle|0\cdots0\rangle`$ to $`|x\cdots x\rangle`$. It introduces no phase and does not change the preceding probabilities or conditional endpoint states. Reading the copies therefore produces repeated noisy reports of the same latent bit.

## 3. Decoding and exact output fidelity

For $`m`$ reports of one latent bit, use majority decoding. Break an even-size tie with an independent fair classical bit. The decoding error is

```math
e_m(p)
=\Pr\!\left[\mathrm{Bin}(m,p)>\frac m2\right]
+\frac12\Pr\!\left[\mathrm{Bin}(m,p)=\frac m2\right].
```

The BSC symmetry makes this error probability independent of the latent bit's value. Distinct pointers use disjoint report slots and independent tie breakers, so their decoding errors are independent. Let $`\widehat U,\widehat V`$ be the parities of the decoded bits. Apply

```math
Z^{\widehat U}X^{\widehat V}
```

to the right output qubit. The residual Pauli is, up to a global phase,

```math
X^{\widehat V\oplus V}Z^{\widehat U\oplus U}.
```

The four residual Paulis produce four orthogonal Bell states. Thus the corrected output has fidelity one on a noise realization precisely when both error parities vanish.

For $`M`$ independent Bernoulli($`e_m`$) errors, the probability of even parity is

```math
\Pr(\text{even})
=\frac{1+(1-2e_m)^M}{2}.
```

The X and Z parities use disjoint error sets. The exact physical output fidelity is therefore

```math
\boxed{
F_{\mathrm{Bell}}
=\left[\frac{1+(1-2e_m(p))^M}{2}\right]^2.
}
```

This expression is for the corrected two-qubit state after every other quantum register is discarded. It is not a fidelity estimate obtained by reweighting measurement data.

## 4. Chernoff estimate

Define the detector coefficient as in the [model](model.md):

```math
D(p)=-\frac12\log[4p(1-p)]>0.
```

For $`S\sim\mathrm{Bin}(m,p)`$ and $`\lambda\ge0`$,

```math
e_m(p)\le\Pr(S\ge m/2)
\le\left[e^{-\lambda/2}(1-p+pe^\lambda)\right]^m.
```

Choosing $`\lambda=\log[(1-p)/p]`$ gives

```math
e_m(p)\le[2\sqrt{p(1-p)}]^m=e^{-D(p)m}.
```

A union bound over the $`2M`$ decoded bits then yields

```math
\boxed{
1-F_{\mathrm{Bell}}
\le2M e_m(p)
\le2M\exp\!\left[-D(p)\frac{bt}{2}\right].
}
```

Several bit errors can cancel in a global parity, which is why the exact fidelity can exceed this lower estimate. The bound is sufficient for the uniform depth theorem.

## 5. An explicit partition for every chain length

No divisibility assumption is needed for the asymptotic result. Fix an even integer $`b\ge2`$ and suppose $`n=L+1\ge2b`$. Set

```math
K=\left\lfloor\frac nb\right\rfloor,
\qquad R=n-Kb,
\qquad 0\le R<b.
```

Use one block of length $`b+R`$ and $`K-1`$ blocks of length $`b`$. Every block length $`\ell_j`$ lies between $`b`$ and $`2b-1`$, and $`K\ge2`$. The longer block may be odd.

Split a length-$`\ell_j`$ block into a left domain of size $`\lfloor\ell_j/2\rfloor`$ and a right domain of size $`\lceil\ell_j/2\rceil`$. Create the central Bell pair at the adjacent sites where those domains meet. Its two halves reach the block endpoints after at most $`\lceil\ell_j/2\rceil-1`$ SWAP layers. After boundary decoding, copy each endpoint pointer inward through its own domain. This takes at most the same number of CNOT layers.

Let $`c=\max_j\lceil\ell_j/2\rceil\le b`$. Padding the stages by idle gates where necessary gives

```math
T=2c+t+3\le2b+t+3.
```

At boundary $`j`$, the report counts are

```math
m_{j,u}=t\left\lceil\frac{\ell_j}{2}\right\rceil,
\qquad
m_{j,v}=t\left\lfloor\frac{\ell_{j+1}}{2}\right\rfloor.
```

Both are at least $`bt/2`$. Writing $`e_{j,u}=e_{m_{j,u}}(p)`$ and $`e_{j,v}=e_{m_{j,v}}(p)`$, the parity proof gives the unequal-block fidelity

```math
F_{\mathrm{Bell}}
=\frac{1+\prod_{j=1}^{M}(1-2e_{j,u})}{2}
 \frac{1+\prod_{j=1}^{M}(1-2e_{j,v})}{2}.
```

In particular,

```math
\boxed{
1-F_{\mathrm{Bell}}
\le 2M e^{-D(p)bt/2},
\qquad M=K-1<\frac nb.
}
```

The homogeneous squared expression and exact depth $`b+t+3`$ belong to equal even blocks. The formulas in this section specify the different constants for arbitrary lengths.

If fewer than two length-$`b`$ blocks fit, prepare a Bell pair centrally in the whole chain and swap its halves to the two outputs. This produces the Bell state exactly in

```math
T_{\mathrm{unit}}=\left\lceil\frac n2\right\rceil+1=O(L)
```

layers under the same gate convention. No readout is required.

## 6. Readout implementation and finite verification

The one-qubit-per-site construction uses repeatable Z readout: after the first projection, a pointer remains a computational-basis value, while each public report receives a fresh independent flip. If the device's readout is destructive, retain a pointer register and use a separate resettable readout register at each site. Copying into that register, measuring it, and resetting it introduces fixed overhead in memory and layers. The exact depth $`b+t+3`$ is not assigned to that modified schedule, but its asymptotic order is unchanged.

The [verification guide](../verification/README.md) packages a deterministic twelve-qubit state-vector check. It verifies the actual disjoint nearest-neighbor layers, all sixteen latent Bell-outcome branches, the copied pointer values, and the corrected endpoint density matrices. That calculation checks the layout and Pauli convention. The arbitrary-size construction and the uniform optimum follow from the analytical arguments here and in [the depth law](depth_law.md).
