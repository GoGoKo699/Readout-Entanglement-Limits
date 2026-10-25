# Learning route

This route develops the objects, operations, and proof ideas behind the optimal depth of adaptive Bell-pair preparation with noisy measurement reports. The single educational anchor is **John Watrous, *The Theory of Quantum Information* (Cambridge University Press, 2018)**. The [source guide](ANCHOR.md) identifies the relevant sections and explains how their notation maps to this repository.

## Start here

| Page | Purpose |
|---|---|
| [Anchor and reading guide](ANCHOR.md) | Connect states, channels, instruments, separability, and teleportation to verified sections of Watrous |
| [From the source to this project](BRIDGE.md) | Develop the noisy instrument, the transcript-output separator, and the matching protocol, including a complete eight-site example |
| [30-milestone map](MILESTONES.md) | State the conceptual targets, dependencies, and source pointers for the complete argument |
| [Scientific account](../science/README.md) | Read the precise model, proofs, construction, and limitations |
| [Verification](../verification/README.md) | Reproduce the finite circuit and probability checks |

## Two phases, one argument

The map contains exactly 30 milestones. Its allocation follows the dependencies of this project.

| Phase | Milestones | Progression |
|---|---|---|
| Background and preliminaries | M01–M12 | From individual states and operations to classical records, locality, separability, and the physical preparation task |
| Narrative and innovation | M13–M30 | From one corrupted report to a universal converse, then from one Bell junction to a complete construction, optimality, and scope |

The first phase supplies 12 distinct foundations used in the proof. The second needs 18 milestones because it develops two complementary arguments: an obstruction that applies to every allowed protocol and an explicit circuit that attains the same depth order. The final milestones bring these arguments together and identify the physical resources and parameter regimes on which the result depends.

The bridge is a continuous explanation; the milestone map makes its dependencies explicit. The scientific pages give the authoritative statements and derivations. Watrous supplies the quantum-information foundations, while the project-specific geometry, reporting-noise argument, and resource accounting are developed here and compared with the primary literature in [Related work](../references/RELATED_WORK.md).

[Repository overview](../README.md) · [Scientific route](../science/README.md)
