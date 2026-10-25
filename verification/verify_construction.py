#!/usr/bin/env python3
"""Finite audit of science/construction.md and its uniform upper-bound choice.

The sparse engine and exhaustive report checks extend the verification developed
in Adaptive-Entanglement-Depth. This version implements this repository's centered
Bell links, one-long-block partition, variable banks, and fair-tie majority rule.
It uses only the standard library and never reads another repository.
"""

from collections import Counter
from dataclasses import dataclass, replace
from fractions import Fraction
from itertools import product
import json
import math
from pathlib import Path


EXPECTED_PATH = Path(__file__).resolve().parent / "expected" / "construction.json"


def require(condition, message):
    """Keep every check active under Python -O."""
    if not condition:
        raise AssertionError(message)


@dataclass(frozen=True)
class Gate:
    name: str
    qubits: tuple[int, ...]


@dataclass(frozen=True)
class Plan:
    sites: int
    block_size: int
    rounds: int
    mode: str
    blocks: tuple[int, ...]
    links: tuple[tuple[int, int], ...]
    banks: tuple[tuple[int, ...], ...]
    layers: tuple[tuple[Gate, ...], ...]
    link_end: int
    cleanup: bool


def gate(name, *qubits):
    return Gate(name, qubits)


def make_plan(sites, block_size, rounds, cleanup=False):
    """Emit the canonical physical schedule, including short-chain fallback."""
    require(sites >= 2 and block_size >= 2 and block_size % 2 == 0
            and rounds >= 1, "Invalid parameters")
    count, remainder = divmod(sites, block_size)
    blocks = ((block_size + remainder,) + (block_size,) * (count - 1)
              if count >= 2 else (sites,))
    links, centers = [], []
    start = 0
    for size in blocks:
        links.append((start, start + size - 1))
        centers.append((start + size // 2 - 1, start + size // 2))
        start += size
    layers = [tuple(gate("H", left) for left, _ in centers),
              tuple(gate("CX", left, right) for left, right in centers)]
    radius = max((size + 1) // 2 for size in blocks)
    for step in range(radius - 1):
        layer = []
        for (a, b), (left, right) in zip(links, centers):
            if left - step > a:
                layer.append(gate("SWAP", left - step, left - step - 1))
            if right + step < b:
                layer.append(gate("SWAP", right + step, right + step + 1))
        layers.append(tuple(layer))
    link_end = len(layers)
    if count < 2:
        return Plan(sites, block_size, rounds, "unitary", blocks, tuple(links),
                    (), tuple(layers), link_end, False)

    layers.append(tuple(gate("CX", links[j][1], links[j + 1][0])
                        for j in range(count - 1)))
    layers.append(tuple(gate("H", links[j][1]) for j in range(count - 1)))
    banks = []
    for j in range(count - 1):
        left, right = links[j][1], links[j + 1][0]
        banks.extend((tuple(left - k for k in range((blocks[j] + 1) // 2)),
                      tuple(right + k for k in range(blocks[j + 1] // 2))))
    for step in range(radius - 1):
        layers.append(tuple(gate("CX", bank[step], bank[step + 1])
                            for bank in banks if step + 1 < len(bank)))
    readout_layer = tuple(gate("MZ", q) for bank in banks for q in bank)
    layers.extend(readout_layer for _ in range(rounds))
    final = [gate("CORRECTION", sites - 1)]
    if cleanup:
        final.extend(gate("RESET", q) for q in range(1, sites - 1))
    layers.append(tuple(final))
    return Plan(sites, block_size, rounds, "banks", blocks, tuple(links),
                tuple(banks), tuple(layers), link_end, cleanup)


def compile_swaps(plan):
    """Replace each disjoint SWAP layer by three alternating CNOT layers."""
    layers, link_end = [], None
    for number, layer in enumerate(plan.layers, 1):
        if any(op.name == "SWAP" for op in layer):
            require(all(op.name == "SWAP" for op in layer), "Mixed SWAP layer")
            for reverse in (False, True, False):
                layers.append(tuple(gate("CX", *(op.qubits[::-1] if reverse
                                                   else op.qubits))
                                    for op in layer))
        else:
            layers.append(layer)
        if number == plan.link_end:
            link_end = len(layers)
    return replace(plan, layers=tuple(layers), link_end=link_end)


def check_layers_and_costs(plan, compiled=False):
    """Inspect every operand before comparing independently derived costs."""
    counts = Counter()
    for number, layer in enumerate(plan.layers, 1):
        used = set()
        require(bool(layer), f"Empty layer {number}")
        for op in layer:
            require(all(0 <= q < plan.sites for q in op.qubits), "Outside chain")
            require(not used.intersection(op.qubits), f"Overlap in layer {number}")
            require(len(set(op.qubits)) == len(op.qubits), "Repeated operand")
            used.update(op.qubits)
            if op.name in ("CX", "SWAP"):
                require(len(op.qubits) == 2 and abs(op.qubits[0] - op.qubits[1]) == 1,
                        f"Nonlocal gate: {op}")
            else:
                require(op.name in ("H", "MZ", "CORRECTION", "RESET")
                        and len(op.qubits) == 1, f"Invalid operation: {op}")
            counts[op.name] += 1

    if plan.mode == "unitary":
        swaps = plan.sites - 2
        expected = Counter(H=1, CX=1)
        depth = 2 + (3 if compiled else 1) * ((plan.sites - 1) // 2)
        require(not plan.banks, "Unitary fallback has banks")
    else:
        count = len(plan.links)
        radius = max((size + 1) // 2 for size in plan.blocks)
        require(sum(plan.blocks) == plan.sites, "Partition does not fill chain")
        require(min(plan.blocks) == plan.block_size, "Minimum block mismatch")
        require(max(plan.blocks) < 2 * plan.block_size, "Long block too large")
        flat = tuple(q for bank in plan.banks for q in bank)
        require(len(flat) == len(set(flat)), "Banks overlap")
        require(0 not in flat and plan.sites - 1 not in flat, "Endpoint in bank")
        require(len(plan.banks) == 2 * (count - 1), "Wrong bank count")
        require(min(map(len, plan.banks)) >= plan.block_size // 2,
                "Bank smaller than guaranteed domain")
        outer_domains = plan.blocks[0] // 2 + (plan.blocks[-1] + 1) // 2
        measured = plan.sites - outer_domains
        require(len(flat) == measured, "Measured-site count mismatch")
        swaps = plan.sites - 2 * count
        expected = Counter(H=2 * count - 1, CX=measured + 1,
                           MZ=measured * plan.rounds, CORRECTION=1)
        if plan.cleanup:
            expected["RESET"] = plan.sites - 2
        depth = (4 * radius + 1 if compiled else 2 * radius + 3) + plan.rounds
    if compiled:
        expected["CX"] += 3 * swaps
    elif swaps:
        expected["SWAP"] = swaps
    require(counts == expected, f"Gate count mismatch: {counts} != {expected}")
    require(len(plan.layers) == depth, "Depth formula disagrees with schedule")


def apply_unitary(state, op):
    """Sparse state-vector engine independent of the schedule and formulas."""
    if op.name == "H":
        q, = op.qubits
        out = {}
        for basis, amplitude in state.items():
            zero = basis & ~(1 << q)
            one = zero | (1 << q)
            scale = amplitude / math.sqrt(2)
            out[zero] = out.get(zero, 0j) + scale
            out[one] = out.get(one, 0j) + (-scale if basis & (1 << q) else scale)
        return {basis: amp for basis, amp in out.items() if abs(amp) > 1e-15}
    if op.name == "CX":
        control, target = op.qubits
        return {basis ^ ((1 << target) if basis & (1 << control) else 0): amp
                for basis, amp in state.items()}
    if op.name == "SWAP":
        a, b = op.qubits
        return {basis ^ (((1 << a) | (1 << b))
                         if ((basis >> a) ^ (basis >> b)) & 1 else 0): amp
                for basis, amp in state.items()}
    raise ValueError(f"Not a unitary primitive: {op}")


def simulate_prefix(plan):
    state, checkpoint = {0: 1 + 0j}, None
    for number, layer in enumerate(plan.layers, 1):
        if any(op.name == "MZ" for op in layer):
            break
        for op in layer:
            state = apply_unitary(state, op)
        if number == plan.link_end:
            checkpoint = dict(state)
    require(checkpoint is not None, "Link checkpoint missing")
    return checkpoint, state


def state_distance(first, second):
    return math.sqrt(sum(abs(first.get(basis, 0) - second.get(basis, 0)) ** 2
                         for basis in first.keys() | second.keys()))


def expected_links(links):
    state = {}
    amplitude = 2 ** (-len(links) / 2)
    for values in product((0, 1), repeat=len(links)):
        basis = sum(((1 << a) | (1 << b)) * bit
                    for (a, b), bit in zip(links, values))
        state[basis] = amplitude
    return state


def corrected_fidelity(vector, phase, bit):
    """Apply Z^phase X^bit to the right endpoint, then measure Bell overlap."""
    corrected = [0j] * 4
    for basis, amplitude in enumerate(vector):
        destination = basis ^ (2 if bit else 0)
        if phase and ((destination >> 1) & 1):
            amplitude = -amplitude
        corrected[destination] += amplitude
    return abs((corrected[0] + corrected[3]) / math.sqrt(2)) ** 2


def project_banks(plan, state, tolerance):
    """Enumerate every true branch; its fixed environment can be traced out."""
    measured = {q for bank in plan.banks for q in bank}
    unused = set(range(1, plan.sites - 1)) - measured
    branches = {}
    require(abs(sum(abs(amp) ** 2 for amp in state.values()) - 1) < tolerance,
            "Premeasurement state is not normalized")
    for basis, amplitude in state.items():
        truth = tuple((basis >> bank[0]) & 1 for bank in plan.banks)
        require(all(all(((basis >> q) & 1) == truth[j] for q in bank)
                    for j, bank in enumerate(plan.banks)), "Bank copies disagree")
        require(all(not ((basis >> q) & 1) for q in unused), "Unused qubit not zero")
        endpoint = (basis & 1) | (((basis >> (plan.sites - 1)) & 1) << 1)
        branches.setdefault(truth, [0j] * 4)[endpoint] += amplitude
    require(len(branches) == 2 ** len(plan.banks), "Some true branches missing")
    normalized = {}
    for truth, vector in branches.items():
        probability = sum(abs(amp) ** 2 for amp in vector)
        require(abs(probability - 2 ** (-len(plan.banks))) < tolerance,
                "True outcomes are not uniform")
        vector = [amp / math.sqrt(probability) for amp in vector]
        fidelity = corrected_fidelity(vector, sum(truth[0::2]) % 2,
                                      sum(truth[1::2]) % 2)
        require(abs(fidelity - 1) < tolerance, "Wrong endpoint Bell correction")
        normalized[truth] = (probability, vector)
    return normalized


def majority_error(votes, p):
    """Exact binomial tail with an independent fair tie breaker."""
    require(votes > 0, "Votes must be positive")
    a, b = p.numerator, p.denominator
    numerator = sum(math.comb(votes, k) * a ** k * (b - a) ** (votes - k)
                    for k in range(votes // 2 + 1, votes + 1))
    error = Fraction(numerator, b ** votes)
    if votes % 2 == 0:
        error += Fraction(math.comb(votes, votes // 2) * a ** (votes // 2)
                          * (b - a) ** (votes // 2), 2 * b ** votes)
    return error


def report_enumeration(votes, p, truth):
    """Enumerate all raw records and both values of the independent tie coin."""
    error = Fraction(0)
    for reports in product((0, 1), repeat=votes):
        flips = sum(value != truth for value in reports)
        weight = p ** flips * (1 - p) ** (votes - flips)
        for tie_coin in (0, 1):
            decoded = tie_coin if 2 * sum(reports) == votes else int(2 * sum(reports) > votes)
            if decoded != truth:
                error += weight / 2
    return error


def error_weight(errors, rates):
    return math.prod(q if error else 1 - q for error, q in zip(errors, rates))


def parity_fidelity(rates):
    return math.prod((1 + math.prod(1 - 2 * q for q in rates[axis::2])) / 2
                     for axis in (0, 1))


def parity_enumeration(rates):
    return sum((error_weight(errors, rates)
                for errors in product((0, 1), repeat=len(rates))
                if sum(errors[0::2]) % 2 == 0 and sum(errors[1::2]) % 2 == 0),
               Fraction(0))


def noisy_quantum_fidelity(branches, rates):
    """Physically apply every decoded Pauli to each projected endpoint vector."""
    terms = []
    for truth, (weight, vector) in branches.items():
        for errors in product((0, 1), repeat=len(truth)):
            probability = error_weight(errors, rates)
            decoded = tuple(value ^ error for value, error in zip(truth, errors))
            overlap = corrected_fidelity(vector, sum(decoded[0::2]) % 2,
                                         sum(decoded[1::2]) % 2)
            terms.append(weight * float(probability) * overlap)
    return math.fsum(terms)


def inverse_scale(distance, coefficient, error):
    """Find tau from the monotone defining equation by log-space bisection."""
    target = math.log(distance / error)
    low, high = -100.0, target
    for _ in range(200):
        middle = (low + high) / 2
        residual = coefficient * math.exp(2 * middle) + middle - target
        if residual > 0:
            high = middle
        else:
            low = middle
    return math.exp((low + high) / 2)


def check_uniform_parameter_choice(config, tolerance):
    """Check finite upper-bound formulas; do not allocate large-chain states."""
    cases, bank_cases, floor_cases, cap_cases = 0, 0, 0, 0
    for distance, coefficient, error in product(
            config["distances"], config["detector_coefficients"], config["errors"]):
        tau = inverse_scale(distance, coefficient, error)
        require(abs(coefficient * tau * tau - math.log(distance / (error * tau)))
                < tolerance * max(1, math.log(distance / error)), "Inverse equation failed")
        scale = max(1, min(distance, tau))
        x = max(1, tau)
        block_size = 2 * math.ceil(x)
        sites = distance + 1
        count, remainder = divmod(sites, block_size)
        if count >= 2:
            radius = (block_size + remainder + 1) // 2
            depth = 2 * radius + block_size + 3
            # Log form avoids underflow, including nearly ideal detectors.
            log_union = math.log(2 * (count - 1)) - coefficient * block_size ** 2 / 2
            require(log_union <= math.log(error) + tolerance, "Target error not reached")
            require(depth <= 3 * block_size + 3, "Unequal-block depth bound failed")
            bank_cases += 1
        else:
            depth = (sites + 1) // 2 + 1
        require(depth <= 15 * scale + tolerance, "Uniform upper constant failed")
        floor_cases += tau < 1
        cap_cases += tau > distance
        cases += 1
    require(bank_cases and floor_cases and cap_cases, "Missing uniform regimes")
    return {"cases": cases, "bank_cases": bank_cases, "unitary_cases": cases - bank_cases,
            "microscopic_floor_cases": floor_cases, "linear_cap_cases": cap_cases}


def run():
    expected = json.loads(EXPECTED_PATH.read_text(encoding="utf-8"))
    tolerance = expected["tolerance"]
    exact = expected["exact"]
    geometry = expected["geometry"]
    geometry_cases = 0
    for sites, block_size in product(range(geometry["sites_min"], geometry["sites_max"] + 1),
                                     geometry["block_sizes"]):
        plan = make_plan(sites, block_size, geometry["readout_rounds"], cleanup=True)
        check_layers_and_costs(plan)
        check_layers_and_costs(compile_swaps(plan), compiled=True)
        geometry_cases += 1

    probabilities = tuple(Fraction(*pair) for pair in expected["probabilities"])
    raw_cases = 0
    for votes, p, truth in product(range(1, expected["raw_votes_max"] + 1), probabilities, (0, 1)):
        require(report_enumeration(votes, p, truth) == majority_error(votes, p),
                "Raw report enumeration disagrees with majority formula")
        if votes % 2 == 0:
            require(majority_error(votes, p) == majority_error(votes - 1, p),
                    "Fair tie and one predetermined discarded vote disagree")
        raw_cases += 1

    parity_cases = 0
    for boundaries in range(1, 5):
        for rates in ((Fraction(0),) * (2 * boundaries),
                      (Fraction(1, 2),) * (2 * boundaries),
                      tuple(Fraction(j + 1, 4 * boundaries + 3)
                            for j in range(2 * boundaries))):
            require(parity_enumeration(rates) == parity_fidelity(rates),
                    "Exact heterogeneous two-parity formula fails")
            parity_cases += 1

    example = exact["eight_site_example"]
    example_plan = make_plan(8, 4, 2)
    require(all(len(bank) * example_plan.rounds == example["reports_per_pointer"]
                for bank in example_plan.banks), "Eight-site example report count failed")
    example_error = majority_error(example["reports_per_pointer"], Fraction(1, 5))
    require(example_error == Fraction(*example["error_probability"])
            and parity_fidelity((example_error, example_error))
            == Fraction(*example["bell_fidelity"]), "Eight-site example exact result failed")

    quantum_results = []
    largest_fidelity_discrepancy = largest_state_discrepancy = 0.0
    noise_cases = 0
    for sites, block_size in expected["quantum_layouts"]:
        plan = make_plan(sites, block_size, 2)
        compiled = compile_swaps(plan)
        check_layers_and_costs(plan)
        check_layers_and_costs(compiled, compiled=True)
        checkpoint, state = simulate_prefix(plan)
        compiled_checkpoint, compiled_state = simulate_prefix(compiled)
        discrepancies = (state_distance(checkpoint, expected_links(plan.links)),
                         state_distance(checkpoint, compiled_checkpoint),
                         state_distance(state, compiled_state))
        largest_state_discrepancy = max(largest_state_discrepancy, *discrepancies)
        require(max(discrepancies) < tolerance, "Bell links, zero interiors, or SWAP compile failed")
        branches = project_banks(plan, state, tolerance)
        if plan.mode == "banks":
            for rounds, p in product(expected["quantum_readout_rounds"], probabilities):
                rates = tuple(majority_error(len(bank) * rounds, p) for bank in plan.banks)
                observed = noisy_quantum_fidelity(branches, rates)
                predicted = float(parity_fidelity(rates))
                discrepancy = abs(observed - predicted)
                largest_fidelity_discrepancy = max(largest_fidelity_discrepancy, discrepancy)
                require(discrepancy < tolerance, "Physical corrected fidelity disagrees")
                noise_cases += 1
        quantum_results.append({"sites": sites, "block_size": block_size,
                                "mode": plan.mode, "blocks": plan.blocks,
                                "bank_sizes": tuple(map(len, plan.banks)),
                                "true_branches": len(branches),
                                "readout_rounds": 2 if plan.mode == "banks" else 0,
                                "native_depth": len(plan.layers),
                                "cnot_depth": len(compiled.layers)})

    uniform = check_uniform_parameter_choice(expected["uniform_parameters"], tolerance)
    counts = {"geometry_parameter_cases": geometry_cases, "raw_report_cases_exact": raw_cases,
              "parity_cases_exact": parity_cases, "uniform_parameter_cases": uniform["cases"],
              "quantum_layouts": len(quantum_results), "noisy_quantum_cases": noise_cases}
    require(all(value == exact[key] for key, value in counts.items()),
            f"Coverage counts differ from expected: {counts}")
    return {"status": "PASS", "coverage": counts, "uniform_parameter_regimes": uniform,
            "quantum_layouts": quantum_results, "tolerance": tolerance,
            "largest_state_discrepancy": largest_state_discrepancy,
            "largest_fidelity_discrepancy": largest_fidelity_discrepancy}


if __name__ == "__main__":
    print(json.dumps(run(), indent=2, sort_keys=True))
