# Bell links with spatially repeated readout

The construction prepares a Bell pair between the prescribed endpoints of a chain using depth $O(\sqrt{\log L})$ at any fixed readout error rate $0<p<1/2$ and fixed target fidelity $F_0\in(1/2,1)$. It first creates independent Bell links, then joins them by entanglement swapping. Each of the two classical bits produced by a swap is distributed across a small bank of qubits and read repeatedly. Spatial copies and repeated measurements supply a quadratic number of noisy samples in the available depth.

The [model](model.md) counts every quantum gate and every readout round. Classical decoding and feedforward have no depth cost. Coherent gates, reset operations and measurement backaction are ideal. The [converse](converse.md) proves that the resulting depth scaling is optimal for fixed $p\in(0,1/2)$ and fixed $F_0\in(1/2,1)$.

## Chain and bank parameters

Write $N=L+1\geq 2$ for the number of sites, numbered $0,\ldots,N-1$. Every site initially holds $|0\rangle$. Choose integers $r\geq 0$ and $s\geq 1$. Each outcome bank will contain its original qubit and $r$ additional copies; each bank qubit will undergo $s$ readouts.

Set

```math
\ell=2r+2,
\qquad
m=\left\lfloor\frac{N}{\ell}\right\rfloor.
```

When $m\geq 2$, divide the chain into $m$ contiguous segments with balanced lengths $n_1,\ldots,n_m$: each length is either $\lfloor N/m\rfloor$ or $\lceil N/m\rceil$, and their sum is $N$. Thus each segment has at least $2r+2$ sites. Let $a_j$ and $b_j=a_j+n_j-1$ be its first and last sites, and let

```math
B=\max_j n_j=\left\lceil\frac{N}{m}\right\rceil.
```

The largest segment satisfies $B\leq 3r+3$. Indeed, write $N=m\ell+h$ with $0\leq h<\ell$. Then $B=\ell+\lceil h/m\rceil\leq 2r+2+(r+1)$ because $m\geq 2$.

The case $m<2$ uses the [unitary fallback](#short-chains-and-a-unitary-fallback) below. No extra sites are introduced to make a segment fit.

## Preparing the links and returning their interiors to zero

For each segment $j$, apply $H$ at $a_j$, followed by $\mathrm{CNOT}_{a_j\to a_j+1}$. This creates a Bell pair on the first two sites. Move its second half to $b_j$ using the sequence

```math
\mathrm{SWAP}_{a_j+1,a_j+2},\;
\mathrm{SWAP}_{a_j+2,a_j+3},\;\ldots,\;
\mathrm{SWAP}_{b_j-1,b_j}.
```

Each SWAP moves the entangled qubit into a site holding zero and leaves zero behind. Execute the sequences for different segments in parallel, padding shorter sequences with idle layers. After $B$ layers in total, the state is

```math
\bigotimes_{j=1}^{m}|\Phi^+\rangle_{a_jb_j}
\;\otimes\!
\bigotimes_{q\notin\{a_1,b_1,\ldots,a_m,b_m\}}|0\rangle_q,
\qquad
|\Phi^+\rangle=\frac{|00\rangle+|11\rangle}{\sqrt 2}.
```

The segment interiors are available for the readout banks. Their return to zero follows from the explicit SWAP sequence; it is not an additional initialization resource.

## Joining the links and creating disjoint banks

At each junction $j=1,\ldots,m-1$, the qubits $b_j$ and $a_{j+1}$ are nearest neighbors. In one layer, apply the gate

```math
\mathrm{CNOT}_{b_j\to a_{j+1}}
```

at every junction. In the next layer, apply $H$ at every $b_j$. Computational-basis measurement of these qubits would now be a Bell measurement. Denote its two true bits by

```math
u_j=\text{the computational-basis bit at }b_j,
\qquad
v_j=\text{the computational-basis bit at }a_{j+1}.
```

The bits have not yet been read out. First distribute their computational-basis values into the zero interiors by CNOT fanout. The two banks for junction $j$ are

```math
\mathcal B^u_j=\{b_j,b_j-1,\ldots,b_j-r\},
\qquad
\mathcal B^v_j=\{a_{j+1},a_{j+1}+1,\ldots,a_{j+1}+r\}.
```

In fanout layer $k=1,\ldots,r$, apply

```math
\mathrm{CNOT}_{b_j-k+1\to b_j-k},
\qquad
\mathrm{CNOT}_{a_{j+1}+k-1\to a_{j+1}+k}
```

at every junction. All these gates are nearest-neighbor gates. Within an internal segment, the bank from its left junction occupies its first $r+1$ sites, and the bank from its right junction occupies its last $r+1$ sites. The condition $n_j\geq 2r+2$ makes the banks disjoint, including when the segment has the minimum length. Neither endpoint of the full chain belongs to a bank.

To see the state being produced, consider the computational-basis branches of the junction qubits after the Bell-basis rotations. The $2(m-1)$ bits $(u_1,v_1,\ldots,u_{m-1},v_{m-1})$ have a uniform distribution. Conditional on one branch, the endpoint state is, up to a global phase,

```math
|\Phi_{U,V}\rangle
=\left(I\otimes X^{V}Z^{U}\right)|\Phi^+\rangle,
\qquad
U=\bigoplus_{j=1}^{m-1}u_j,
\quad
V=\bigoplus_{j=1}^{m-1}v_j.
```

For two links, the identity follows directly from

```math
\left(H_b\mathrm{CNOT}_{b\to a}\right)
|\Phi^+\rangle_{Ab}|\Phi^+\rangle_{aC}
=\frac12\sum_{u,v=0}^{1}
|u\rangle_b|v\rangle_a\otimes
\left(I_A\otimes X_C^vZ_C^u\right)|\Phi^+\rangle_{AC}.
```

Joining the next link adds its two labels modulo two; reordering the Paulis can only produce a global phase in a fixed branch. Iteration gives the stated parity labels and uniform branch probabilities. The fanout replaces each branch bit by identical computational-basis values on its bank. It preserves the endpoint state in that branch and its probability. The first simultaneous readout of all banks selects a branch; every subsequent ideal QND readout of a bank has the same true bit.

## Decoding the noisy records

Read every bank qubit in the computational basis in each of $s$ layers. There are $n_{\mathrm{raw}}=(r+1)s$ reported samples for each true bit. By the assumed readout model, every report is independently flipped with probability $p$, including reports from repeated measurements of the same qubit.

Use the largest odd number $M\leq n_{\mathrm{raw}}$ of samples, discarding one predetermined report if $n_{\mathrm{raw}}$ is even. Majority decoding then has no tie. Its error probability is exactly

```math
q_M(p)
=\sum_{k=(M+1)/2}^{M}
\binom{M}{k}p^k(1-p)^{M-k}.
```

The error probability is the same for true bit zero and true bit one. The decoded-bit errors are independent across banks, since different banks use disjoint independent readout noise variables. These statements also hold conditional on all the true junction bits.

Let $\widehat u_j,\widehat v_j$ be the decoded bits. Apply the single-qubit Pauli $X^{\widehat V}Z^{\widehat U}$ to the right endpoint, where

```math
\widehat U=\bigoplus_j\widehat u_j,
\qquad
\widehat V=\bigoplus_j\widehat v_j.
```

The residual error is a Bell-state label determined by the two decoded-error parities. A parity of $m-1$ independent errors, each occurring with probability $q$, is even with probability $[1+(1-2q)^{m-1}]/2$. The phase and bit-error parities are independent. Consequently the endpoint Bell fidelity is exactly

```math
F_{m,M}(p)
=\left[
\frac{1+\left(1-2q_M(p)\right)^{m-1}}{2}
\right]^2.
```

This formula concerns the physical corrected endpoint state after averaging over all true outcomes and all reporting errors. It does not condition on successful decoding or postselect a favorable transcript.

For the depth bound, a simpler estimate is useful. Define

```math
c_p=-\log\!\left(2\sqrt{p(1-p)}\right)>0,
\qquad 0<p<\frac12,
```

with natural logarithms. Applying the exponential Markov inequality to a binomial variable and choosing the parameter $\log((1-p)/p)$ gives

```math
q_M(p)\leq e^{-c_p M}.
```

An endpoint error requires at least one incorrectly decoded junction bit, so

```math
1-F_{m,M}(p)
\leq 2(m-1)q_M(p)
\leq 2(m-1)e^{-c_pM}.
```

The union bound is sufficient for achievability; the exact fidelity formula shows how multiple errors can also cancel in the two parities.

## Exact quantum costs

The following schedule counts a native SWAP as one nearest-neighbor two-qubit gate. It starts from the specified product input.

| Stage | Layers |
|---|---:|
| Hadamards starting the $m$ Bell links | $1$ |
| Initial CNOTs for the links | $1$ |
| Moving one half of each link to the segment boundary | $B-2$ |
| Junction CNOTs | $1$ |
| Junction Hadamards | $1$ |
| Outward bank fanout | $r$ |
| Repeated bank readout | $s$ |
| Endpoint Pauli correction | $1$ |
| **Total depth** | **$B+r+s+3$** |

Every layer contains disjoint quantum operations. The construction uses exactly $N$ physical qubits, one per original site. The gate and readout counts are

| Operation | Count |
|---|---:|
| Hadamard | $2m-1$ |
| CNOT, excluding a possible decomposition of SWAPs | $2m-1+2r(m-1)$ |
| SWAP | $N-2m$ |
| Binary readout | $2(m-1)(r+1)s$ |
| Final single-qubit Pauli | At most $1$ |

If only CNOT is native among the used two-qubit gates, replace each SWAP by three alternating-direction CNOTs. The resulting depth is

```math
D_{\mathrm{CNOT}}=3B+r+s-1,
```

and the CNOT count increases by $3(N-2m)$. This constant-factor change leaves the depth scaling unchanged.

No reset is required to produce the endpoint state. If clean final work qubits are desired, reset every non-endpoint qubit to $|0\rangle$ in the final correction layer. These $N-2$ perfect local resets act on sites disjoint from the correction and do not change the endpoint state. This optional cleanup uses the reset operation already allowed by the model.

## Choosing the parameters for a fixed fidelity

Fix $0<p<1/2$ and $F_0\in(1/2,1)$, and set $\varepsilon_0=1-F_0$. Choose

```math
t=\max\left\{
1,\left\lceil\sqrt{\frac{\log(N/\varepsilon_0)}{c_p}}\right\rceil
\right\},
\qquad r=s=t.
```

If the balanced partition has $m\geq 2$, the number of retained samples is

```math
M=t(t+1)-1\geq t^2.
```

Since $2(m-1)\leq N$, the fidelity obeys

```math
1-F_{m,M}(p)
\leq N e^{-c_p t^2}
\leq\varepsilon_0.
```

The schedule therefore reaches $F\geq F_0$, with

```math
D\leq 5t+6,
\qquad
D_{\mathrm{CNOT}}\leq 11t+8.
```

For fixed $p$ and fixed $F_0$, this is $O(\sqrt{\log L})$ as $L$ grows. The constants depend on those fixed parameters. In particular, the statement does not claim uniform constants as $p$ approaches $1/2$.

## Short chains and a unitary fallback

When $m<2$, a bank partition is unnecessary. Set $a=\lfloor(N-2)/2\rfloor$, apply $H_a$, and apply $\mathrm{CNOT}_{a\to a+1}$. In outward round $k=0,1,\ldots$, swap sites $a-k$ and $a-k-1$ if $a-k>0$, and simultaneously swap sites $a+1+k$ and $a+2+k$ if $a+2+k<N$. Stop when both halves reach the physical endpoints. The two gates in any such round are disjoint. Every site traversed by a Bell half initially holds zero, so all intermediate sites return to zero. This produces the exact endpoint Bell pair with no readout and depth

```math
D_{\mathrm{unitary}}
=2+\left\lceil\frac{L-1}{2}\right\rceil
=1+\left\lceil\frac N2\right\rceil.
```

The counts are one Hadamard, one CNOT and $N-2$ SWAPs. With the three-CNOT implementation of SWAP, the depth is $2+3\lceil(L-1)/2\rceil$.

For the parameter choice above, $m<2$ implies $N<4t+4$. The fallback then has depth at most $2t+3$, so it also satisfies the displayed overall depth bound. This covers arbitrary chain lengths, including the two-site case, without padding the physical array.

The same fallback explains a boundary on possible precision extensions: arbitrarily small target error can always be reached by an ideal unitary circuit of linear depth. The fixed-fidelity result does not claim an unrestricted lower bound proportional to $\sqrt{\log(L/\varepsilon)}$ for all vanishing errors $\varepsilon$.

## Limiting cases and verification

At $p=0$, choose $r=0$ and $s=1$. Ideal swapping gives constant depth, at most seven layers for the balanced construction, with the unitary fallback handling very short chains. At $p=1/2$, a majority decoder has error probability $1/2$ regardless of the number of samples. The bank construction with at least two links then has fidelity $1/4$; the linear-depth unitary route remains exact. The [converse](converse.md) and [interpretation](interpretation.md) explain why uninformative classical records cannot supply the constant-depth advantage.

The [verification script](../verification/verify_construction.py) implements the gate schedule, checks disjoint nearest-neighbor layers for chains with unequal segment lengths, and simulates all true measurement branches of small instances. It independently enumerates noisy reports and compares the quantum endpoint state with the exact majority/parity formula. The [verification guide](../verification/README.md) specifies the scope of these finite checks. The general argument above supplies the analytical construction and its asymptotic bound.
