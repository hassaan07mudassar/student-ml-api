# Traceability Record

Record one row for each release after GitHub provides the final values.

| Release | PR number | Merge SHA | Git tag | Docker version tag | Commit-SHA tag | Image digest | Evidence URL |
|---|---:|---|---|---|---|---|---|
| 1.0.0 | `<PR number>` | `<merge SHA>` | `v1.0.0` | `1.0.0` | `<commit SHA>` | `sha256:<digest>` | `<release/run URL>` |
| 1.1.0 | `<PR number>` | `<merge SHA>` | `v1.1.0` | `1.1.0` | `<commit SHA>` | `sha256:<digest>` | `<release/run URL>` |

## Chain

`PR -> merge commit -> Git tag -> GitHub Actions run -> image tags -> immutable digest`

Use `docker inspect` locally and the Packages page or `docker pull` output to capture the digest. The release workflow uses the same `GITHUB_SHA` as the commit-SHA image tag and OCI revision label.
