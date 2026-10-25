# Finite circuit verification

Two deterministic checks implement [the local construction](../science/construction.md), with explicit state-vector gates and no circuit-library compiler or random sampling. Both use the same centered Bell-link preparation, pointer domains, and Pauli convention as the scientific account. Neither reads files from another repository.

- [verify_bell_layout.py](verify_bell_layout.py) preserves the original twelve-qubit audit, its independent dense engine, and its [expected case](expected/bell_layout.json).
- [verify_construction.py](verify_construction.py) extends coverage to unequal blocks, short-chain fallback, compiled SWAPs, exact classical error probabilities, and the uniform constructive parameter choice. Its cases and acceptance criteria are in [expected/construction.json](expected/construction.json).

## Run

From the repository root, using Python 3.12:

```sh
python3 -m pip install -r verification/requirements.txt
python3 verification/verify_bell_layout.py
python3 verification/verify_construction.py
```

The [requirements file](requirements.txt) pins NumPy for the dense twelve-qubit audit. The extended script uses only the Python standard library and supports Python 3.10 or later. Each program reads its expected cases and tolerances, prints JSON, and creates no result files. A failed check raises an exception and exits unsuccessfully; checks remain active under Python's `-O` option. Success is `"passed": true` for the original audit and `"status": "PASS"` for the extension.

## Original twelve-qubit audit

The case has three blocks of four sites, two simultaneous Bell-swap boundaries, and two physical copies of each of the four latent pointer bits. Its six unitary layers are followed by one readout layer and one endpoint-correction layer. The script verifies the exact depth convention $`T=b+t+3=8`$ and the report count $`m=bt/2=2`$ for this case.

The script checks that every layer uses disjoint sites and only nearest-neighbor two-qubit gates. It verifies disjoint copying domains, excludes both output qubits from readout, and confirms the number of layers and reports.

It then enumerates all sixteen true Bell-outcome strings. For each string, it verifies the outcome probability, the equality of every copied pointer to its original value, and the corrected two-qubit endpoint density matrix. The correction uses the Z parity of the first boundary bits and the X parity of the second boundary bits. All other quantum systems are traced out.

Projecting the original pointer registers is enough for this finite calculation: the separate copy assertions establish that Z readout of the remaining copies gives the same true values with probability one. Independent report flips and repeated QND readouts enter the analytical majority formula in [the construction](../science/construction.md#3-decoding-and-exact-output-fidelity).

The expected JSON specifies exact integer counts and floating-point tolerances, rather than a platform-dependent exact decimal transcript. A successful run reports `passed: true`, all sixteen checked branches, and numerical errors below $`10^{-12}`$.

## Extended physical and probability checks

### Schedule and resource accounting

For every chain length $`2\le n\le64`$ and each even block parameter $`b\in\{2,4,6,8,10,12,14\}`$, the extension emits the actual gate, readout, correction, and optional cleanup layers. These 441 cases include the one-long-block partition, odd block lengths, and unitary fallback. Every operand is checked for chain membership, nearest-neighbor locality, and disjoint use in its layer. Pointer banks must be disjoint and exclude the two output sites. Layer counts, gate counts, report counts, and optional final reset counts must match the resource formulas.

Every schedule is also checked after replacing each SWAP with three alternating CNOTs. For bank circuits, the native and compiled depths are respectively $`2c+t+3`$ and $`4c+t+1`$, where $`c=\max_j\lceil\ell_j/2\rceil`$. Both even and odd unitary fallback chains are covered.

### Quantum states and noisy correction

An independent sparse state-vector engine simulates thirteen layouts of up to nineteen qubits. They include three fallback cases, minimum-size banks, unequal banks, the maximum long-block remainder, and four simultaneous links. The engine compares the link-preparation checkpoint with the intended tensor product of Bell links and zero interiors. Native-SWAP and compiled circuits must agree as state vectors.

The engine then enumerates every true outcome branch. It checks normalization, uniform outcome probabilities, equality of every pointer copy, zero unused interiors, and unit Bell fidelity after the prescribed endpoint correction. Fixing a bank outcome fixes every non-output basis register, so tracing them out leaves the checked endpoint vector. Repeated ideal QND measurements preserve those true values; the program subsequently enumerates the independent reporting errors rather than introducing an apparatus simulation.

For each bank layout, all decoded-error patterns are applied as actual endpoint Paulis and averaged over all true outcomes. The resulting fidelity must agree with the unequal-bank parity-product formula. This gives 120 noisy quantum cases, using one, two, and three readout rounds and $`p\in\{0,1/5,49/100,1/2\}`$. The eight-site, four-reports-per-pointer example at $`p=1/5`$ is also checked exactly: $`e_4=13/125`$ and $`F=12544/15625`$.

### Exact probabilities and uniform parameters

Seventy-two checks enumerate every raw report string for one through nine reports, for both true values and all four noise rates above. Even ties use an independent fair bit, as in the construction. `fractions.Fraction` makes their comparison with the binomial error formula exact. The tests also verify that fair-tie decoding of an even count has the same error probability as discarding one predetermined report. Twelve separate exact checks enumerate the two error parities, including unequal per-pointer error probabilities.

Another 168 cases solve the defining equation for $`\tau`$ and check the [uniform upper-bound parameter choice](../science/depth_law.md#3-uniform-constructive-upper-bound), including its error union bound and $`T\le15\mathcal T`$. Distances run up to $`999999`$, detector coefficients from $`10^{-12}`$ to $`1000`$, and target errors down to $`10^{-12}`$. The cases cover bank and unitary schedules, the microscopic floor, and the linear cap. They evaluate finite formulas and do not allocate large quantum states or establish a universal converse.

The extension's state-vector and noisy-fidelity tolerance is $`3\times10^{-12}`$; probability enumerations use exact rational equality. Its expected file fixes coverage counts as well as test inputs, so accidental removal of a family of cases fails the run. Floating-point output is diagnostic rather than an exact decimal snapshot.

## Provenance

The extension adapts the sparse engine, exhaustive report/parity enumeration, schedule inspection, and SWAP-compilation checks developed in Adaptive-Entanglement-Depth. It implements this repository's construction throughout: centered links, the one-long-block partition, variable pointer-domain sizes, and fair-tie decoding. The earlier balanced-segment schedule and odd-vote convention are not a second active implementation here. The original dense audit and its expected JSON remain unchanged.

## Analytical scope

These finite calculations check gate layout, pointer reuse, normalization, Bell byproducts, noisy correction, and sampled constructive parameter choices. The arbitrary-size construction, majority bound, and integer block partition are proved in [construction.md](../science/construction.md). The universal converse is proved in [blind_strip.md](../science/blind_strip.md), [information_bound.md](../science/information_bound.md), and [heralding.md](../science/heralding.md). Their uniform inversion is in [depth_law.md](../science/depth_law.md).

A successful finite check does not establish those asymptotic statements. Their validity rests on the corresponding analytical proofs.
