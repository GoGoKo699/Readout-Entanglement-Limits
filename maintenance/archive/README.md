# Adaptive-Entanglement-Depth archive

Source: https://github.com/GoGoKo699/Adaptive-Entanglement-Depth

Captured on 2026-10-25. This archive preserves the original Git history exactly, including original commit IDs, authorship, timestamps, signed-commit data, file modes, trees and contents. No synthetic commits replace source history.

## Contents and verification

- `adaptive-entanglement-depth.bundle`: self-contained Git bundle; 68,716 bytes.
- `adaptive-entanglement-depth-metadata.json.gz`: gzip-compressed complete captured API responses for the repository, refs, branches, tag, release, issues, pull requests, comments/reviews, branch comparisons, original commits and original content trees.
- `verification.json`: machine-readable verification summary.
- `SHA256SUMS`: file-integrity checksums.

The bundle includes all eight refs returned by the source Git refs API, plus `HEAD`: four branches, three pull-request head refs, and the `v1.0.0` tag. All seven reachable original commits were reconstructed and verified against their source Git SHA-1 IDs. The four distinct root trees and all 29 unique file blobs were also verified against their source Git IDs. Main contains 17 files.

An offline mirror clone was created from this bundle. Its refs and seven reachable commit IDs matched the source inventory exactly. `git fsck --full --strict` completed successfully with no output. `git bundle verify` reported a complete history with no prerequisites.

Main commit: `9b596727e74356bbc7add127da1426066431c066`.

Main tree: `147b00efb675a38c4623bb972757a11e49e2a52f`.

Bundle SHA-256: `9c9d267f984ede77c6f9bf643eca177d16ef6a7fdf6c99f514d9f1829020a3fe`.

Bundle Git blob ID: `6491a18cdbec21d82f670447063fcf3e2ff3c4b3`.

## Restore locally

Run these commands from the directory containing the archive files. Use new destination directories.

```sh
sha256sum -c SHA256SUMS
git clone --mirror adaptive-entanglement-depth.bundle restored.git
git --git-dir=restored.git fsck --full --strict
git --git-dir=restored.git for-each-ref --format='%(refname) %(objectname)'
git --git-dir=restored.git rev-list --all --count
git clone restored.git Adaptive-Entanglement-Depth-restored
```

The commit count should be `7`. The working clone should be on `main` at the original main commit above. The mirror retains the three `refs/pull/*/head` refs in addition to branches and tags.

To republish the preserved branches and tag, create an empty destination repository and push these ref namespaces from the restored mirror:

```sh
git --git-dir=restored.git push NEW_EMPTY_REPOSITORY_URL \
  'refs/heads/*:refs/heads/*' 'refs/tags/*:refs/tags/*'
```

GitHub manages its own `refs/pull/*` namespace. Those original refs remain locally available in the bundle and restored mirror; creating new pull requests will produce new platform records.

## Platform metadata and limits

The captured source has three merged pull requests and no standalone issues. All inspected issue-comment, review-comment and review lists are empty. It has one release (`v1.0.0`) with no release assets. Discussions are disabled. A subsequent source API check found zero Actions runs. Release notes and all three pull-request titles, bodies and metadata are preserved in the JSON export.

Decompress the metadata with `gzip -dk adaptive-entanglement-depth-metadata.json.gz`. Its uncompressed SHA-256 is `3bb87c4d247602ec49de6ef658b5ed4c5120c733189dc5f4c06329fcb1b95404`.

The metadata is a historical export, not an automatic GitHub-platform restore format. GitHub issue/PR numbers, URLs, timestamps and other service identifiers generally cannot be recreated identically in a replacement repository.

This archive covers all Git objects reachable from the refs returned by the source Git refs API and the API metadata listed above. It does not include repository administration, access settings, secrets, webhook configurations, Actions logs or artifacts, or a separate wiki repository. The repository reports that the wiki feature is enabled; wiki contents were not assessed by this archive build. Unreachable or deleted Git objects are outside the inventory. These limits should be reviewed before deleting the source repository.
