# Scientific account

**How much depth does a one-dimensional adaptive circuit need to create distant entanglement when its measurement reports are noisy?**

For a fixed independent readout error rate $0<p<1/2$ and a fixed target Bell overlap $1/2<F_0<1$, the optimal depth is

```math
D_{\min}(L;p,F_0)=\Theta_{p,F_0}\!\left(\sqrt{\log L}\right).
```

The chain begins in a product state. Quantum operations are perfect and nearest neighbor, classical control is unrestricted, and both quantum gates and readout rounds count toward depth. The endpoint Bell pair is retained as a physical output.

## Read the argument

| Page | Scientific purpose |
|---|---|
| [Model and statements](model.md) | Defines the allowed instruments, noise, causal schedule, resources, and output criterion |
| [Adaptive-circuit converse](converse.md) | Converts reporting noise into forgotten records, proves the full transcript-output separator lemma, and packs independent corridors |
| [Nearest-neighbor construction](construction.md) | Gives the physical layout, gate schedule, repeated-readout decoder, exact fidelity, and matching depth |
| [Interpretation and limits](interpretation.md) | Explains the spacetime mechanism, accessible range, heralding, limiting channels, and resource boundaries |
| [Related work](../references/RELATED_WORK.md) | Compares the closest locality, quantum-bus, readout-amplification, and fault-tolerance results |
| [Verification](../verification/README.md) | Reproduces the finite circuit and probability checks and states their scope |

The central dependency is the separator lemma: after all quantum-dependent records in a sufficiently wide corridor are forgotten, deleting every operation across its central cut preserves the joint endpoint state and accessible transcript. This is what makes the converse apply to arbitrary adaptive control. The construction then shows that the obstruction has the correct depth order.

The written proofs establish the universal and asymptotic statements. The executable checks address finite layout, scheduling, correction, and probability identities.

For the foundations and a worked example, use the [Watrous-based learning route](../learning/README.md). Its [30 milestones](../learning/MILESTONES.md) connect the source material to the proof and the physical construction.

[Repository overview](../README.md)

