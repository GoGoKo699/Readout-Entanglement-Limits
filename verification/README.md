# Finite circuit verification

The deterministic check in [verify_bell_layout.py](verify_bell_layout.py) implements the twelve-qubit instance of [the local construction](../science/construction.md). It uses explicit state-vector gates and traces, with no circuit-library compiler or random sampling.

The case has three blocks of four sites, two simultaneous Bell-swap boundaries, and two physical copies of each of the four latent pointer bits. Its six unitary layers are followed by one readout layer and one endpoint-correction layer. The script verifies the exact depth convention $`T=b+t+3=8`$ and the report count $`m=bt/2=2`$ for this case.

## Run

From the repository root, using Python 3.12:

```sh
python3 -m pip install -r verification/requirements.txt
python3 verification/verify_bell_layout.py
```

The packaged check was executed with Python 3.12.14 and NumPy 2.3.5. The [requirements file](requirements.txt) pins the NumPy version. The program reads its case and acceptance tolerances from [expected/bell_layout.json](expected/bell_layout.json) and prints a JSON result. It creates no result files. A failed check raises an `AssertionError` and exits unsuccessfully; the checks also remain active under Python's `-O` option.

## What is checked

The script checks that every layer uses disjoint sites and only nearest-neighbor two-qubit gates. It verifies disjoint copying domains, excludes both output qubits from readout, and confirms the number of layers and reports.

It then enumerates all sixteen true Bell-outcome strings. For each string, it verifies the outcome probability, the equality of every copied pointer to its original value, and the corrected two-qubit endpoint density matrix. The correction uses the Z parity of the first boundary bits and the X parity of the second boundary bits. All other quantum systems are traced out.

Projecting the original pointer registers is enough for this finite calculation: the separate copy assertions establish that Z readout of the remaining copies gives the same true values with probability one. Independent report flips and repeated QND readouts enter the analytical majority formula in [the construction](../science/construction.md#3-decoding-and-exact-output-fidelity).

The expected JSON specifies exact integer counts and floating-point tolerances, rather than a platform-dependent exact decimal transcript. A successful run reports `passed: true`, all sixteen checked branches, and numerical errors below $`10^{-12}`$.

## Analytical scope

This finite calculation checks the gate layout, pointer reuse, normalization, and Bell-byproduct convention. The arbitrary-size construction, majority bound, and integer block partition are proved in [construction.md](../science/construction.md). The universal converse is proved in [blind_strip.md](../science/blind_strip.md), [information_bound.md](../science/information_bound.md), and [heralding.md](../science/heralding.md). Their uniform inversion is in [depth_law.md](../science/depth_law.md).

A successful finite check does not establish those asymptotic statements. Their validity rests on the corresponding analytical proofs.
