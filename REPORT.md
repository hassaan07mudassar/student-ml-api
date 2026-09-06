# MLOps Assignment Report: student-ml-api

## Student Information

- **Student Name:** Muhammad Hassaan Mudassar
- **Roll Number:** i230536
- **Section:** A

## Objective

The objective was to implement a traceable Flask prediction API and demonstrate a professional MLOps lifecycle: feature development, pull-request review, CI validation, Docker packaging, semantic releases, GHCR publishing, provenance, reproducibility, failure analysis, and rollback.

## Implementation

The Flask service in `app.py` provides `GET /health` and `POST /predict`. Prediction is deterministic: numeric `value * 2`. Invalid, missing, malformed, or non-object input is rejected with HTTP 400. The version is stored in `VERSION` and is included in the health response.

## Automated Tests

`tests/test_app.py` contains tests for health, successful prediction, missing input, invalid input, and malformed JSON. The test job runs `python -m pytest -q`.

## Git Workflow

Development begins on `feature/prediction-api`, with commits:

- `feat: add Flask prediction API`
- `test: add API unit tests`
- `docs: add project documentation`

The second release uses `feature/model-metadata` and updates the health response to include application and model versions.

## PR Workflow

A pull request targets `main`. Reviewers use `PR_TEMPLATE.md`, inspect the change, and require green CI. Direct pushes are blocked by branch protection. Squash and Merge is selected to preserve a clean, review-centered history while retaining the PR as the detailed audit record.

## CI Workflow

`ci.yml` checks out code, installs Python 3.11 dependencies, runs pytest, and builds the Docker image. The Docker job requires the test job. A failed test or build therefore fails the workflow and blocks the PR.

## Release Workflow

`release.yml` triggers on `v*.*.*`, runs tests again, logs into GHCR with the built-in `GITHUB_TOKEN`, extracts the version from `GITHUB_REF_NAME`, builds the image with OCI metadata, and pushes version, `latest`, and commit-SHA tags. CI validates; release publishes only after a tag is created on approved code.

## Dockerization

The Dockerfile uses `python:3.11-slim`, sets `/app` as the working directory, installs from `requirements.txt` with `--no-cache-dir`, copies application files, exposes port 5000, and runs `python app.py`. OCI labels record version, revision, repository source, and creation time. `.dockerignore` excludes source-control files, caches, virtual environments, secrets, and documentation.

## Registry Publishing

The expected image format is `ghcr.io/<github-owner>/student-ml-api:<tag>`. GitHub Actions requires `packages: write`; the repository does not store a personal token. The release produces `1.0.0`, `latest`, and the full commit SHA, then repeats the pattern for `1.1.0`.

## Version 1.0.0 Release

1. Merge `feature/prediction-api` after successful PR checks.
2. Run `git tag v1.0.0` and `git push origin v1.0.0`.
3. Confirm the release workflow passes.
4. Verify the GHCR package contains `1.0.0`, `latest`, and the commit-SHA tag.
5. Record the digest in `docs/TRACEABILITY.md`.

## Version 1.1.0 Release

1. Create `feature/model-metadata`.
2. Change `VERSION` to `1.1.0` and update the health test.
3. Open, validate, review, and squash-merge the PR.
4. Run `git tag v1.1.0` and `git push origin v1.1.0`.
5. Verify the health response contains `application_version: 1.1.0` and `model_version: model-1`.
6. Record the published digest and SHA tag.

## Rollback Demonstration

A production issue can be mitigated by stopping the current container and running `ghcr.io/<owner>/student-ml-api:1.0.0` or a previously recorded commit-SHA image. This requires no rebuild and no source changes. The registry image is immutable by digest, which makes the rollback reproducible.

## Failure Demonstration

The deliberate pytest failure changes the health expectation to `wrong`, produces a failed CI run, and is corrected with `fix: correct health endpoint test`. A second failure demonstrates an incorrect host-to-container port mapping; `docker ps` reveals the mismatch and rerunning with `-p 5000:5000` resolves it. See `docs/FAILURE_ANALYSIS.md`.

## Traceability

The required chain is PR number -> merge SHA -> Git tag -> Actions run -> Docker version/latest/SHA tags -> registry digest. The evidence table is in `docs/TRACEABILITY.md` and must be populated with values from the actual repository and GHCR run.

## Screenshots Section

Capture the 17 items listed in `docs/SCREENSHOT_CHECKLIST.md`: repository structure, branch, PR, failed and fixed CI, branch protection, Docker build/run, endpoint, registry tags, release workflow, Git tags, traceability, and rollback proof.

## Branch Protection

Protect `main` with required pull requests, required `Test API` and `Validate Docker build` status checks, up-to-date branches, no direct pushes, resolved conversations, no force pushes, and no deletion. See `docs/BRANCH_PROTECTION.md`.

## Conclusions

This project separates validation from publication, produces traceable container artifacts, records standard OCI metadata, and provides a no-rebuild rollback path. The workflow is reproducible because runtime versions, Python dependencies, image labels, Git tags, and commit-SHA references are explicit.
