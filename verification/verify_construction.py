#!/usr/bin/env python3
"""Finite checks of the one-qubit-per-site Bell-bank construction.

Run with Python 3.10 or later; only the standard library is used. The script
executes the actual nearest-neighbor unitary gates on sparse state vectors,
projects every true measurement branch of small circuits, and enumerates
classical reporting errors. It does not prove the asymptotic converse.
"""

from collections import Counter
from dataclasses import dataclass, replace
from fractions import Fraction
from itertools import product
import json
import math


TOL = 3e-12


def require(condition, message):
    if not condition:
        raise AssertionError(message)


@dataclass(frozen=True)
class Gate:
    name: str
    qubits: tuple[int, ...]


@dataclass(frozen=True)
class Plan:
    sites: int
    copies: int
    rounds: int
    mode: str
    segments: tuple[int, ...]
    links: tuple[tuple[int, int], ...]
    banks: tuple[tuple[int, ...], ...]
    layers: tuple[tuple[Gate, ...], ...]
    link_end: int
    cleanup: bool


def gate(name, *qubits):
    return Gate(name, qubits)


def make_plan(sites, copies, rounds, cleanup=False):
    """Generate the explicit schedule, including its finite-size fallback."""
    require(sites >= 2 and copies >= 0 and rounds >= 1, "Invalid parameters")
    count = sites // (2 * copies + 2)
    if count < 2:
        left = (sites - 2) // 2
        right = left + 1
        layers = [(gate("H", left),), (gate("CX", left, right),)]
        for step in range(max(left, sites - 1 - right)):
            layer = []
            if left - step > 0:
                layer.append(gate("SWAP", left - step, left - step - 1))
            if right + step < sites - 1:
                layer.append(gate("SWAP", right + step, right + step + 1))
            layers.append(tuple(layer))
        return Plan(sites, copies, rounds, "unitary", (sites,),
                    ((0, sites - 1),), (), tuple(layers), len(layers), False)

    base, extra = divmod(sites, count)
    segments = tuple(base + (j < extra) for j in range(count))
    links = []
    start = 0
    for size in segments:
        links.append((start, start + size - 1))
        start += size
    layers = [tuple(gate("H", a) for a, _ in links),
              tuple(gate("CX", a, a + 1) for a, _ in links)]
    for step in range(max(segments) - 2):
        layers.append(tuple(gate("SWAP", a + step + 1, a + step + 2)
                            for a, b in links if a + step + 2 <= b))
    link_end = len(layers)
    layers.append(tuple(gate("CX", links[j][1], links[j + 1][0])
                        for j in range(count - 1)))
    layers.append(tuple(gate("H", links[j][1]) for j in range(count - 1)))
    banks = []
    for j in range(count - 1):
        b, a = links[j][1], links[j + 1][0]
        banks.extend((tuple(b - k for k in range(copies + 1)),
                      tuple(a + k for k in range(copies + 1))))
    for step in range(copies):
        layers.append(tuple(gate("CX", bank[step], bank[step + 1])
                            for bank in banks))
    readout_layer = tuple(gate("MZ", q) for bank in banks for q in bank)
    layers.extend(readout_layer for _ in range(rounds))
    final = [gate("CORRECTION", sites - 1)]
    if cleanup:
        final.extend(gate("RESET", q) for q in range(1, sites - 1))
    layers.append(tuple(final))
    return Plan(sites, copies, rounds, "banks", segments, tuple(links),
                tuple(banks), tuple(layers), link_end, cleanup)


def compile_swaps(plan):
    """Replace each SWAP layer by three alternating CNOT layers."""
    layers = []
    link_end = None
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
    """Check geometry directly before comparing resource formulas."""
    counts = Counter()
    for number, layer in enumerate(plan.layers, 1):
        used = set()
        require(bool(layer), f"Empty layer {number}")
        for op in layer:
            require(all(0 <= q < plan.sites for q in op.qubits), "Outside chain")
            require(not used.intersection(op.qubits), f"Overlap in layer {number}")
            require(len(set(op.qubits)) == len(op.qubits), "Repeated gate operand")
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
    else:
        count = len(plan.links)
        biggest = max(plan.segments)
        require(sum(plan.segments) == plan.sites, "Partition does not fill chain")
        require(min(plan.segments) >= 2 * plan.copies + 2, "Bank segments too short")
        require(biggest <= 3 * plan.copies + 3, "Balanced segment bound fails")
        flat = tuple(q for bank in plan.banks for q in bank)
        require(len(flat) == len(set(flat)), "Banks overlap")
        require(0 not in flat and plan.sites - 1 not in flat, "Endpoint in bank")
        require(len(plan.banks) == 2 * (count - 1), "Wrong bank count")
        swaps = plan.sites - 2 * count
        expected = Counter(H=2 * count - 1,
                           CX=2 * count - 1 + 2 * plan.copies * (count - 1),
                           MZ=2 * (count - 1) * (plan.copies + 1) * plan.rounds,
                           CORRECTION=1)
        if plan.cleanup:
            expected["RESET"] = plan.sites - 2
        depth = ((3 * biggest - 1) if compiled else (biggest + 3))
        depth += plan.copies + plan.rounds
    if compiled:
        expected["CX"] += 3 * swaps
    elif swaps:
        expected["SWAP"] = swaps
    require(counts == expected, f"Gate count mismatch: {counts} != {expected}")
    require(len(plan.layers) == depth, "Depth formula disagrees with schedule")


def apply_unitary(state, op):
    """Small sparse state-vector engine, separate from schedule generation."""
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
    state = {0: 1 + 0j}
    checkpoint = None
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
    corrected = [0j] * 4
    for basis, amplitude in enumerate(vector):
        right = (basis >> 1) & 1
        if phase and right:
            amplitude = -amplitude
        corrected[basis ^ (2 if bit else 0)] += amplitude
    return abs((corrected[0] + corrected[3]) / math.sqrt(2)) ** 2


def project_banks(plan, state):
    """Project all true branches and verify bank agreement and Bell labels."""
    measured = {q for bank in plan.banks for q in bank}
    unused = set(range(1, plan.sites - 1)) - measured
    branches = {}
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
        require(abs(probability - 2 ** (-len(plan.banks))) < TOL,
                "True outcomes are not uniform")
        vector = [amp / math.sqrt(probability) for amp in vector]
        fidelity = corrected_fidelity(vector, sum(truth[0::2]) % 2,
                                      sum(truth[1::2]) % 2)
        require(abs(fidelity - 1) < TOL, "Wrong endpoint Bell correction")
        normalized[truth] = (probability, vector)
    return normalized


def retained_votes(raw_votes):
    return raw_votes if raw_votes % 2 else raw_votes - 1


def majority_tail(votes, p):
    """Exact binomial expression, using integer arithmetic until the division."""
    require(votes > 0 and votes % 2 == 1, "Votes must be positive and odd")
    a, b = p.numerator, p.denominator
    numerator = sum(math.comb(votes, k) * a ** k * (b - a) ** (votes - k)
                    for k in range((votes + 1) // 2, votes + 1))
    return Fraction(numerator, b ** votes)


def report_enumeration(raw_votes, p, truth):
    """Enumerate every raw record, including the predetermined discarded vote."""
    votes = retained_votes(raw_votes)
    error = Fraction(0)
    for reports in product((0, 1), repeat=raw_votes):
        flips = sum(value != truth for value in reports)
        decoded = int(2 * sum(reports[:votes]) > votes)
        if decoded != truth:
            error += p ** flips * (1 - p) ** (raw_votes - flips)
    return error


def parity_enumeration(count, q):
    probability = Fraction(0)
    for errors in product((0, 1), repeat=2 * (count - 1)):
        if sum(errors[0::2]) % 2 == 0 and sum(errors[1::2]) % 2 == 0:
            probability += q ** sum(errors) * (1 - q) ** (len(errors) - sum(errors))
    return probability


def noisy_quantum_fidelity(branches, q):
    """Apply every possible decoded correction to actual projected vectors."""
    terms = []
    for truth, (weight, vector) in branches.items():
        for errors in product((0, 1), repeat=len(truth)):
            probability = q ** sum(errors) * (1 - q) ** (len(errors) - sum(errors))
            decoded = tuple(value ^ error for value, error in zip(truth, errors))
            overlap = corrected_fidelity(vector, sum(decoded[0::2]) % 2,
                                         sum(decoded[1::2]) % 2)
            terms.append(weight * float(probability) * overlap)
    return math.fsum(terms)


def check_parameter_choice():
    cases = 0
    for sites, p, target in product((2, 3, 7, 32, 100, 1000, 10**6),
                                   (Fraction(1, 10), Fraction(1, 4), Fraction(2, 5)),
                                   (Fraction(3, 5), Fraction(9, 10), Fraction(99, 100))):
        error = 1 - target
        c_p = -math.log(2 * math.sqrt(float(p * (1 - p))))
        t = max(1, math.ceil(math.sqrt(math.log(sites / float(error)) / c_p)))
        count = sites // (2 * t + 2)
        if count < 2:
            depth = 2 + (sites - 1) // 2
            cnot_depth = 2 + 3 * ((sites - 1) // 2)
            require(depth <= 2 * t + 3, "Fallback exceeds its stated bound")
        else:
            biggest = (sites + count - 1) // count
            votes = retained_votes(t * (t + 1))
            require(votes >= t * t, "Odd-vote choice loses too many samples")
            q = majority_tail(votes, p)
            require(2 * (count - 1) * q <= error, "Fixed target fidelity not reached")
            depth, cnot_depth = biggest + 2 * t + 3, 3 * biggest + 2 * t - 1
        require(depth <= 5 * t + 6 and cnot_depth <= 11 * t + 8,
                "Overall depth bound fails")
        cases += 1
    return cases


def main():
    geometry_cases = 0
    for sites, copies in product(range(2, 65), range(7)):
        plan = make_plan(sites, copies, 3, cleanup=True)
        check_layers_and_costs(plan)
        check_layers_and_costs(compile_swaps(plan), compiled=True)
        geometry_cases += 1

    raw_cases = 0
    probabilities = (Fraction(0), Fraction(1, 5), Fraction(49, 100), Fraction(1, 2))
    for raw_votes, p, truth in product(range(1, 10), probabilities, (0, 1)):
        require(report_enumeration(raw_votes, p, truth)
                == majority_tail(retained_votes(raw_votes), p),
                "Raw report enumeration disagrees with majority formula")
        raw_cases += 1

    parity_cases = 0
    for count, q in product(range(2, 6), (Fraction(0), Fraction(1, 7), Fraction(1, 2))):
        predicted = ((1 + (1 - 2 * q) ** (count - 1)) / 2) ** 2
        require(parity_enumeration(count, q) == predicted,
                "Exact two-parity formula fails")
        parity_cases += 1

    layouts = ((2, 3), (3, 3), (6, 3), (4, 0), (5, 0), (7, 0),
               (8, 1), (9, 1), (11, 1), (13, 1), (16, 1), (17, 2), (19, 2))
    quantum_results = []
    largest_discrepancy = 0.0
    noise_cases = 0
    for sites, copies in layouts:
        plan = make_plan(sites, copies, 2)
        compiled = compile_swaps(plan)
        check_layers_and_costs(plan)
        check_layers_and_costs(compiled, compiled=True)
        checkpoint, state = simulate_prefix(plan)
        compiled_checkpoint, compiled_state = simulate_prefix(compiled)
        require(state_distance(checkpoint, expected_links(plan.links)) < TOL,
                "Bell links or returned-zero interiors are incorrect")
        require(state_distance(checkpoint, compiled_checkpoint) < TOL
                and state_distance(state, compiled_state) < TOL,
                "SWAP and three-CNOT circuits disagree")
        branches = project_banks(plan, state)
        if plan.mode == "banks":
            for rounds, p in product((1, 2, 3), probabilities):
                q = majority_tail(retained_votes((copies + 1) * rounds), p)
                observed = noisy_quantum_fidelity(branches, q)
                predicted = float(((1 + (1 - 2 * q) ** (len(plan.links) - 1)) / 2) ** 2)
                discrepancy = abs(observed - predicted)
                largest_discrepancy = max(largest_discrepancy, discrepancy)
                require(discrepancy < TOL, "Physical corrected Bell fidelity disagrees")
                noise_cases += 1
        quantum_results.append({"sites": sites, "additional_copies": copies,
                                "mode": plan.mode, "segments": plan.segments,
                                "true_branches": len(branches),
                                "readout_rounds": 2 if plan.mode == "banks" else 0,
                                "native_depth": len(plan.layers),
                                "cnot_depth": len(compiled.layers)})

    print(json.dumps({"status": "PASS", "geometry_parameter_cases": geometry_cases,
                      "raw_report_cases_exact": raw_cases,
                      "parity_cases_exact": parity_cases,
                      "fixed_target_cases": check_parameter_choice(),
                      "quantum_layouts": quantum_results,
                      "noisy_quantum_cases": noise_cases,
                      "largest_fidelity_discrepancy": largest_discrepancy}, indent=2))


if __name__ == "__main__":
    main()
