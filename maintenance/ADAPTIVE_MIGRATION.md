# Adaptive source preservation and integration

Readout-Entanglement-Limits is the canonical scientific home for the common Readout/Adaptive contribution. The fixed-noise, fixed-fidelity depth law is included within the broader detector/accuracy account on `main`; it is not counted as a second independent result.

The migration uses Adaptive-Entanglement-Depth at `9b596727e74356bbc7add127da1426066431c066` (its `v1.0.0`), and Readout-Entanglement-Limits at `be70050ce95de9e274422bfa92512d7670e51bbd`. The unchanged MIT license names the same copyright holder in both sources.

## Preserved source

The [exact source snapshot](https://github.com/GoGoKo699/Readout-Entanglement-Limits/tree/65cd110ceab7f63f4ef828e4e596b2aedd4c4e0b) lives in this repository's `archive/adaptive-entanglement-depth-20261025` branch. Its complete tree is `147b00efb675a38c4623bb972757a11e49e2a52f`, byte-identical to all 17 tracked files of the source release. Links inside that tree remain relative to its own files. This historical snapshot is not a second active account or learning route.

[The self-contained Git bundle](archive/adaptive-entanglement-depth.bundle) additionally retains all seven original commits, all four distinct source trees, four branches, three pull-request head refs, the release tag and HEAD. [Restoration instructions](archive/README.md), [checksums](archive/SHA256SUMS), and [verification evidence](archive/verification.json) travel with it. An offline mirror restore passed `git fsck --full --strict` and exact ref/commit checks. The source repository is not needed to restore the archived Git history.

The compressed [GitHub metadata export](archive/adaptive-entanglement-depth-metadata.json.gz) preserves the inspected repository metadata, source commit records, release and three merged PR records. There were no standalone issues, PR comments/reviews, attached release assets or Actions runs at inspection. Separate wiki content and account administration are outside this scientific/Git archive. No source repository has been modified or deleted by this migration.

## Source-to-destination map

Every source file is preserved exactly in the snapshot and Git bundle. The table identifies what is integrated into the current account rather than importing duplicate active pages.

| Source path | Current destination and disposition |
|---|---|
| `LICENSE` | Existing identical `LICENSE`, preserved unchanged. |
| `README.md` | Current `README.md` now points explicitly to the full fixed-fidelity corollary and expanded checks; the uniform theorem remains the principal result. |
| `llms.txt` | Current `llms.txt` routes to the unified scientific account, verification, and this preservation record. |
| `science/README.md` | Existing topic routes in `README.md`, `llms.txt` and `science/model.md` remain authoritative. |
| `science/model.md` | `science/model.md` and `science/depth_law.md`: explicit layer timing, charged noisy heralding filters, and every fixed target above Bell fidelity one-half. |
| `science/converse.md` | `science/blind_strip.md` and `science/heralding.md`: success-weighted elementary witness and policy clarification. The stronger unflagged random-strip proof is retained. |
| `science/construction.md` | `science/construction.md`: exact operation/readout counts, compiled-SWAP depth, fallback and optional cleanup, adapted to the existing centered-link schedule. The older balanced-segment schedule remains archived. |
| `science/interpretation.md` | `science/interpretation.md` and `science/depth_law.md`: endpoint noise channels, fixed-fidelity scope and the distinction from the stronger uniform law. |
| `references/RELATED_WORK.md` | `references/RELATED_WORK.md`: selected amplification, physical Bell-chain and encoded spatial-resource comparisons, checked against primary sources. Unsupported tree-connectivity wording is not carried into the active account. |
| `references/references.bib` | `references/references.bib`: five relevant sources added without duplicating existing keys; the complete earlier bibliography remains archived. |
| `verification/verify_construction.py` | `verification/verify_construction.py`: sparse quantum engine and exact report/parity checks adapted to centered links, variable banks, fair ties and the uniform parameter choice. |
| `verification/README.md` | `verification/README.md`: independent dense and extended checks, deterministic expectations, provenance and explicit evidence limits. |
| `verification/results.json` | Archived original result. Current `verification/expected/construction.json` fixes cases/tolerances; fresh execution prints its own results rather than reusing the earlier transcript. |
| `learning/README.md` | Existing single Wilde route remains active; source entry point is retained in the snapshot. |
| `learning/ANCHOR.md` | Source Watrous guide retained exactly in the snapshot; it does not replace or duplicate the selected Wilde route. |
| `learning/BRIDGE.md` | `learning/WILDE_BRIDGE.md`: useful eight-site spatial-plus-temporal copying example adapted to the centered nine-layer schedule and fair ties. |
| `learning/MILESTONES.md` | Preserved exactly in the snapshot; the existing project-defined thirty-milestone map on `main` is unchanged. |

## Verification and limits

The original dense twelve-qubit audit and the expanded audit pass under Python 3.12.14, NumPy 2.3.5 and optimized Python execution. The expanded audit checks 441 geometry/resource cases in native and compiled gate conventions, thirteen quantum layouts, 120 noisy quantum corrections, 72 exact raw-report cases, twelve exact parity cases, and 168 finite uniform-parameter cases. It reproduces the eight-site bridge example exactly. No runtime path depends on Adaptive-Entanglement-Depth.

The original uniform theorem and its parameter choice are retained. The added fixed-fidelity corollary and success-weighted bound were checked against the existing proof assumptions; exact count formulas were independently checked against emitted schedules. These are scoped mathematical and finite implementation checks, not external peer review or an exhaustive priority certificate.

Source and destination heads, branch/ref coverage, checksums, local links and the actual merged tree are checked before confirming the migration. Deleting the source repository remains Arthur's separate action.
