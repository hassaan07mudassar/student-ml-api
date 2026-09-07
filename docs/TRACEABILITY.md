# Traceability Record

This record links each approved pull request to its Git tag, published container
tags, and immutable GHCR digest.

| Release | PR number | Merge SHA / release revision | Git tag | Docker version tag | Commit-SHA tag | Image digest | Evidence URL |
|---|---:|---|---|---|---|---|---|
| 1.0.0 | 1 | `ee593b2481d099d8083b29030e3020f4297e4afb` | `v1.0.0` | `1.0.0` | `ee593b2481d099d8083b29030e3020f4297e4afb` | `sha256:21382f1f5a8a429f695255f1ff8a87d2552fa643757313b921b2be7a60591a17` | [GHCR package](https://github.com/hassaan07mudassar/student-ml-api/pkgs/container/student-ml-api) |
| 1.1.0 | 2 | `c33b554394502f11d32089c52343370c43c83fdf` | `v1.1.0` | `1.1.0` | `c33b554394502f11d32089c52343370c43c83fdf` | `sha256:fd6e13c873608f1f3fda4996068f1498c5e02b57869b5af7f27499626eccc0c23` | [GHCR package](https://github.com/hassaan07mudassar/student-ml-api/pkgs/container/student-ml-api) |

## Chain

`PR -> merge commit -> Git tag -> GitHub Actions run -> image tags -> immutable digest`

The GHCR package evidence is available at
https://github.com/hassaan07mudassar/student-ml-api/pkgs/container/student-ml-api.
The release workflow evidence is available at
https://github.com/hassaan07mudassar/student-ml-api/actions.
The release workflow uses the same `GITHUB_SHA` as the commit-SHA image tag and OCI revision label.
