# student-ml-api

A production-shaped Flask MLOps assignment project for Muhammad Hassaan Mudassar (i230536, Section A). It demonstrates feature branches, pull requests, automated validation, Docker packaging, semantic releases, GHCR publishing, provenance, reproducibility, and rollback.

## Project Overview

The service exposes a health endpoint and a deterministic prediction endpoint. The prediction rule is `prediction = value * 2`. The v1.0.0 baseline reads its version from `VERSION`; the version-aware application also supports the v1.1.0 model metadata response documented in `docs/RELEASE_NOTES.md`.

## Architecture

`Client -> Flask API -> pytest validation -> Docker image -> GitHub Actions -> GHCR`

CI validates pull requests and does not publish. A Git tag such as `v1.0.0` starts the release workflow, which tests, logs into GHCR with `GITHUB_TOKEN`, builds, labels, and publishes immutable and convenience tags.

## API Endpoints

### `GET /health`

v1.0.0 response:

```json
{"status":"healthy","application":"student-ml-api","version":"1.0.0"}
```

The planned v1.1.0 response adds `application_version` and `model_version` as shown in `docs/RELEASE_NOTES.md`.

### `POST /predict`

Request:

```json
{"value":10}
```

Response:

```json
{"input":10,"prediction":20}
```

Missing fields, non-numeric values, malformed JSON, and non-object JSON return HTTP 400. Boolean values are rejected because they are not meaningful numeric model inputs.

## Local Testing

```bash
python -m pip install -r requirements.txt
python -m pytest -q
python app.py
```

## Docker

```bash
docker build -t student-ml-api:1.0.0 .
docker run -d --name student-ml-api -p 5000:5000 student-ml-api:1.0.0
curl http://localhost:5000/health
```

The image uses `python:3.11-slim`, installs dependencies before application source for cache reuse, exposes port 5000, and runs with `python app.py` bound to `0.0.0.0`.

## CI/CD

`.github/workflows/ci.yml` runs pytest and Docker build validation for pull requests targeting `main`. The Docker job depends on the test job, so either failure blocks the PR.

`.github/workflows/release.yml` runs only for `v*.*.*` tags. It derives the version from the tag, never hardcodes it, and pushes:

- `ghcr.io/<owner>/student-ml-api:1.0.0`
- `ghcr.io/<owner>/student-ml-api:latest`
- `ghcr.io/<owner>/student-ml-api:<commit-sha>`

The workflow has `contents: read` and `packages: write` permissions. No personal credential is stored in the repository.

## Release Process

```bash
git checkout -b feature/prediction-api
git add .
git commit -m "feat: add Flask prediction API"
git commit -m "test: add API unit tests"
git commit -m "docs: add project documentation"
git push -u origin feature/prediction-api
```

Open a PR, wait for required checks, then use Squash and Merge. Tag the merged commit:

```bash
git tag v1.0.0
git push origin v1.0.0
```

For the second release, create `feature/model-metadata`, update `VERSION` to `1.1.0`, update the health test, open and merge a PR, then tag `v1.1.0`.

## Rollback

Rollback uses the registry image only. Stop the current container, pull a known-good immutable version or SHA tag, and run it on port 5000. This avoids rebuilding from a potentially changed source tree. Full commands are in `docs/COMMANDS.md`.

## Registry and Traceability

The release tag, merge SHA, GitHub Actions run, OCI revision label, image version tag, commit-SHA tag, and registry digest form one traceability chain. Populate the table in `docs/TRACEABILITY.md` after each real GitHub run.

## Documentation and Evidence

- [Execution commands](docs/COMMANDS.md)
- [PR description](PR_TEMPLATE.md)
- [Branch protection](docs/BRANCH_PROTECTION.md)
- [Failure analysis](docs/FAILURE_ANALYSIS.md)
- [Screenshot checklist](docs/SCREENSHOT_CHECKLIST.md)
- [Viva preparation](docs/VIVA.md)
- [Release notes](docs/RELEASE_NOTES.md)
- [Final report](REPORT.md)

## Student Information

- **Name:** Muhammad Hassaan Mudassar
- **Roll Number:** i230536
- **Section:** A
