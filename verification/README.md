# Finite verification of the Bell-bank construction

The [verification script](verify_construction.py) executes the physical gate schedule in [construction.md](../science/construction.md). It checks the mechanisms on which the upper bound depends: clearing link interiors, placing two disjoint banks in an internal segment, assigning the two Bell correction bits, and retaining the required fidelity after independent noisy readout.

## Run

From the repository root, run:

```sh
python3 verification/verify_construction.py
```

Python 3.10 or later is sufficient. The script uses only the Python standard library and requires no package installation, network access, or random seed. A failed check raises an exception and returns a nonzero exit status. A successful run prints JSON with `"status": "PASS"`. The saved [results](results.json) record the checked layouts and numerical discrepancy from one successful run.

To replace that record after editing the script:

```sh
python3 verification/verify_construction.py > verification/results.json
```

## What is checked

### Physical schedule and arbitrary-length edge cases

`make_plan` partitions an actual chain of $N$ sites into balanced segments. It emits separate Hadamard, CNOT, SWAP, fanout, readout, and correction layers. When fewer than two segments fit, it emits the centered Bell-pair preparation and simultaneous outward SWAPs instead. It does not add sites or assume that $N$ is divisible by a segment length.

For $2\leq N\leq64$ and $0\leq r\leq6$, with three readout rounds, the script inspects every emitted layer. It checks that all operands lie on the chain, two-qubit gates act on neighboring sites, and no qubit participates in two operations in one layer. It checks bank disjointness, exclusion of the two physical endpoints, and the minimum and maximum segment lengths. It then compares the actual layer and operation counts with the formulas in the construction. Optional final resets are included in these scheduling checks.

The same checks are applied after replacing every native SWAP with three alternating CNOTs. This tests the claimed resource accounting under both gate conventions. The fallback cases include both even and odd chain lengths.

### Actual quantum states and every true branch

An independent sparse state-vector engine applies the generated Hadamard, CNOT, and SWAP gates. It checks 13 selected layouts, including equal and unequal segments, minimum-size banks, the cases attaining the bound $B=3r+3$, four simultaneous links, and the unitary fallback. The largest simulated array has 19 qubits. Sparse storage is possible because these small circuits occupy only a small part of the full computational basis.

At the end of link preparation, the simulated state is compared with the tensor product of the intended Bell links and zero interiors. After the junction rotations and fanout, the script projects every possible true bank outcome. It checks that all qubits within each bank have the same true value, unused interior qubits remain zero, the branch probabilities are uniform, and the stated endpoint correction gives $|\Phi^+\rangle$ in every branch. The native-SWAP circuit and the circuit using three CNOTs per SWAP are also compared as state vectors.

The projection is a joint enumeration of the commuting computational-basis measurements. Once a branch has been selected, each bank qubit is in the corresponding computational-basis state. Repeating its ideal QND readout therefore leaves the true bit fixed; the remaining randomness is the independent reporting channel. The script uses this exact reduction rather than simulating an apparatus environment for each repeated measurement. It does not insert quantum faults into ideal backaction.

Finally, for the bank layouts, it enumerates every pattern of decoded-bit errors and physically applies the corresponding endpoint Pauli to the simulated branch vector. It averages the Bell overlaps over true outcomes and decoded errors, and compares the result with

```math
F_{m,M}(p)=\left[\frac{1+(1-2q_M(p))^{m-1}}{2}\right]^2.
```

The readout cases include $p=0$, $p=1/5$, $p=49/100$, and $p=1/2$, with one, two, and three readout rounds. Complex amplitudes use floating-point arithmetic with an absolute test tolerance of $3\times10^{-12}$. The saved run's largest discrepancy is about $1.1\times10^{-15}$.

### Independent exact probability checks

The probability checks use `fractions.Fraction`, so their comparisons are exact.

- For one through nine raw samples, the script enumerates every reported bit string for both true values. If the raw count is even, it discards the last sample before majority decoding. The resulting error probability must equal the binomial tail $q_M(p)$ for the retained odd count $M$.
- Separately, it enumerates both decoded-error parities and compares their joint even probability with the squared parity formula. This check uses neither the quantum state engine nor the raw-report enumeration.
- It checks the stated fixed-target parameter choice on small chains and large values up to $N=10^6$, for three fixed noise rates and three target fidelities. The exact binomial tail must satisfy the fidelity union bound whenever banks are used. Fallback cases and both depth conventions must satisfy their stated finite-size bounds. These checks at large $N$ evaluate the formulas and do not simulate a million-qubit circuit.

The two sources of numerical arithmetic are kept separate: quantum-state overlaps are checked within a stated tolerance, while the finite classical probability identities and the fidelity union bound are checked with rational arithmetic. The parameter $t$ is selected using ordinary floating-point logarithms; the resulting integer choice is then checked against the exact probability bound.

## Scope

These checks can expose overlapping gates, insufficient bank space, a misplaced Bell half, nonzero work qubits after link preparation, a phase/bit correction error, incorrect handling of an even sample count, or a faulty finite-size depth formula. They support the explicit upper-bound construction.

They do not prove the general construction for all chain lengths. That proof is the gate-by-gate argument and the probability bounds in [construction.md](../science/construction.md). They do not verify the universal adaptive [converse](../science/converse.md), establish publication novelty, model gate noise, or test robustness to correlated reporting errors. Repeated ideal QND backaction and independent binary reporting errors are assumptions of the [model](../science/model.md).
