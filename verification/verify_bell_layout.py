#!/usr/bin/env python3
"""Deterministic state-vector check of the twelve-qubit Bell layout.

This verifies the finite circuit, pointer copies, and Pauli convention in
science/construction.md. The general converse and depth law are analytical.
Run from the repository root: python3 verification/verify_bell_layout.py
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path

import numpy as np


EXPECTED_PATH = Path(__file__).resolve().parent / "expected" / "bell_layout.json"
HADAMARD = np.array([[1, 1], [1, -1]], dtype=complex) / np.sqrt(2)
IDENTITY = np.eye(2, dtype=complex)
PAULI_X = np.array([[0, 1], [1, 0]], dtype=complex)
PAULI_Z = np.diag([1, -1]).astype(complex)


@dataclass(frozen=True)
class Gate:
    name: str
    sites: tuple[int, ...]


def require(condition: bool, message: str) -> None:
    """Keep numerical assertions active even when Python uses -O."""
    if not condition:
        raise AssertionError(message)


def make_layers(n: int, block_size: int):
    require(block_size >= 2 and block_size % 2 == 0, "Use even blocks.")
    require(n % block_size == 0, "The fixed audit uses equal blocks.")
    require(n // block_size >= 2, "At least one swap boundary is required.")
    half = block_size // 2
    starts = list(range(0, n, block_size))

    block_layers = [
        [Gate("H", (start + half - 1,)) for start in starts],
        [Gate("CX", (start + half - 1, start + half)) for start in starts],
    ]
    for distance in range(1, half):
        layer = []
        for start in starts:
            left = start + half - distance
            right = start + half + distance - 1
            layer.extend(
                [Gate("SWAP", (left, left - 1)), Gate("SWAP", (right, right + 1))]
            )
        block_layers.append(layer)

    boundaries = [(site - 1, site) for site in range(block_size, n, block_size)]
    decode_layers = [
        [Gate("CX", pair) for pair in boundaries],
        [Gate("H", (left,)) for left, _ in boundaries],
    ]
    copy_layers = []
    for distance in range(1, half):
        layer = []
        for left, right in boundaries:
            layer.extend(
                [
                    Gate("CX", (left - distance + 1, left - distance)),
                    Gate("CX", (right + distance - 1, right + distance)),
                ]
            )
        copy_layers.append(layer)

    pointer_sites = [site for pair in boundaries for site in pair]
    copy_domains = []
    for left, right in boundaries:
        copy_domains.extend(
            [
                [left - offset for offset in range(half)],
                [right + offset for offset in range(half)],
            ]
        )
    counts = {
        "block_links": len(block_layers),
        "boundary_decoding": len(decode_layers),
        "pointer_copying": len(copy_layers),
    }
    return block_layers + decode_layers + copy_layers, pointer_sites, copy_domains, counts


def verify_geometry(layers: list[list[Gate]], n: int) -> None:
    for layer_index, layer in enumerate(layers):
        used = set()
        for gate in layer:
            arity = 1 if gate.name == "H" else 2
            require(gate.name in {"H", "CX", "SWAP"}, "Unknown gate.")
            require(len(gate.sites) == arity, "Incorrect gate arity.")
            require(len(set(gate.sites)) == arity, "Repeated site in a gate.")
            require(all(0 <= site < n for site in gate.sites), "Site outside chain.")
            require(max(gate.sites) - min(gate.sites) <= 1, "Nonlocal gate.")
            require(
                used.isdisjoint(gate.sites),
                f"Overlapping operations in layer {layer_index}.",
            )
            used.update(gate.sites)


def apply_gate(state: np.ndarray, gate: Gate) -> np.ndarray:
    dimension = len(state)
    result = np.zeros_like(state)
    if gate.name == "H":
        qubit = gate.sites[0]
        for index in range(dimension):
            if not (index >> qubit) & 1:
                paired = index | (1 << qubit)
                result[index] = (
                    HADAMARD[0, 0] * state[index]
                    + HADAMARD[0, 1] * state[paired]
                )
                result[paired] = (
                    HADAMARD[1, 0] * state[index]
                    + HADAMARD[1, 1] * state[paired]
                )
    elif gate.name == "CX":
        control, target = gate.sites
        for index in range(dimension):
            destination = index ^ (((index >> control) & 1) << target)
            result[destination] = state[index]
    else:
        first, second = gate.sites
        for index in range(dimension):
            destination = index
            if ((index >> first) & 1) != ((index >> second) & 1):
                destination ^= (1 << first) ^ (1 << second)
            result[destination] = state[index]
    return result


def endpoint_density(branch: np.ndarray, n: int) -> np.ndarray:
    """Trace sites 1,...,n-2; endpoint basis is |00>,|01>,|10>,|11>."""
    density = np.zeros((4, 4), dtype=complex)
    for middle_bits in range(1 << (n - 2)):
        vector = np.array(
            [
                branch[(middle_bits << 1) | left | (right << (n - 1))]
                for left in range(2)
                for right in range(2)
            ]
        )
        density += np.outer(vector, vector.conj())
    return density


def run() -> dict:
    expected = json.loads(EXPECTED_PATH.read_text(encoding="utf-8"))
    case = expected["case"]
    exact = expected["exact"]
    tolerances = expected["tolerances"]
    n = case["qubits"]
    block_size = case["block_size"]
    readout_rounds = case["readout_rounds"]
    require(n // block_size == case["blocks"], "Unexpected block count.")
    require(case["blocks"] - 1 == case["swap_nodes"], "Unexpected boundary count.")

    layers, stores, domains, counts = make_layers(n, block_size)
    verify_geometry(layers, n)
    counts.update({"readout": readout_rounds, "correction": 1})
    counts["total"] = sum(counts.values())
    require(counts == expected["layer_counts"], "Layer counts differ from expected.")
    require(counts["total"] == block_size + readout_rounds + 3, "Depth identity failed.")
    require(len(layers) == exact["unitary_layers"], "Unexpected unitary depth.")

    copies_per_pointer = block_size // 2
    reports_per_pointer = copies_per_pointer * readout_rounds
    require(copies_per_pointer == exact["copies_per_pointer"], "Copy count mismatch.")
    require(reports_per_pointer == exact["reports_per_pointer"], "Report count mismatch.")
    readout_sites = [site for domain in domains for site in domain]
    require(len(readout_sites) == len(set(readout_sites)), "Pointer domains overlap.")
    require(all(0 < site < n - 1 for site in readout_sites), "Output qubit was read.")

    dimension = 1 << n
    state = np.zeros(dimension, dtype=complex)
    state[0] = 1
    for layer in layers:
        for gate in layer:
            state = apply_gate(state, gate)
    require(
        abs(float(np.vdot(state, state).real) - 1) <= tolerances["probability"],
        "Premeasurement state is not normalized.",
    )

    branch_count = 1 << len(stores)
    require(branch_count == exact["outcome_branches"], "Unexpected outcome count.")
    require(
        exact["branch_probability"] == 1 / branch_count,
        "Expected branch probability is inconsistent.",
    )
    indices = np.arange(dimension)
    phi = np.array([1, 0, 0, 1], dtype=complex) / np.sqrt(2)
    phi_density = np.outer(phi, phi.conj())
    probabilities = []
    copy_errors = []
    fidelities = []
    density_errors = []

    for label in range(branch_count):
        bits = [(label >> bit_index) & 1 for bit_index in range(len(stores))]
        selected = np.ones(dimension, dtype=bool)
        for bit, site in zip(bits, stores):
            selected &= ((indices >> site) & 1) == bit
        branch = state * selected
        probability = float(np.vdot(branch, branch).real)
        require(probability > 0, f"Missing outcome branch {label}.")
        probabilities.append(probability)

        copies_match = np.ones(dimension, dtype=bool)
        for bit, domain in zip(bits, domains):
            for site in domain:
                copies_match &= ((indices >> site) & 1) == bit
        wrong_copies = branch[~copies_match]
        copy_errors.append(float(np.vdot(wrong_copies, wrong_copies).real) / probability)

        # Store order is u_1,v_1,u_2,v_2,... . Correct the right endpoint.
        z_parity = sum(bits[0::2]) % 2
        x_parity = sum(bits[1::2]) % 2
        correction = (PAULI_Z if z_parity else IDENTITY) @ (
            PAULI_X if x_parity else IDENTITY
        )
        endpoint_correction = np.kron(IDENTITY, correction)
        density = endpoint_density(branch, n) / probability
        corrected = endpoint_correction @ density @ endpoint_correction.conj().T
        fidelities.append(float(np.vdot(phi, corrected @ phi).real))
        density_errors.append(float(np.max(np.abs(corrected - phi_density))))

    metrics = {
        "max_outcome_probability_error": max(
            abs(probability - exact["branch_probability"]) for probability in probabilities
        ),
        "total_probability_error": abs(sum(probabilities) - 1),
        "max_copy_error_probability": max(copy_errors),
        "min_corrected_bell_fidelity": min(fidelities),
        "max_corrected_density_matrix_error": max(density_errors),
    }
    require(
        metrics["max_outcome_probability_error"] <= tolerances["probability"],
        "Bell outcomes are not uniform.",
    )
    require(
        metrics["total_probability_error"] <= tolerances["probability"],
        "Outcome probabilities do not sum to one.",
    )
    require(
        metrics["max_copy_error_probability"] <= tolerances["copy_probability"],
        "A fanout register differs from its latent pointer.",
    )
    require(
        metrics["min_corrected_bell_fidelity"] >= 1 - tolerances["fidelity"],
        "An endpoint correction does not recover the Bell state.",
    )
    require(
        metrics["max_corrected_density_matrix_error"] <= tolerances["density_matrix"],
        "Corrected endpoint density matrix differs from the target.",
    )
    return {
        "passed": True,
        "case": case,
        "layer_counts": counts,
        "outcome_branches_checked": branch_count,
        "copies_per_pointer": copies_per_pointer,
        "reports_per_pointer": reports_per_pointer,
        "disjoint_nearest_neighbor_layers": True,
        "metrics": metrics,
    }


if __name__ == "__main__":
    print(json.dumps(run(), indent=2, sort_keys=True))
