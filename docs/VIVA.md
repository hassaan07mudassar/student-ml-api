# Viva Preparation

## Why use a feature branch?
It isolates work from `main`, allows review, and makes CI results part of the integration decision.

## Why use pull requests?
A PR creates an auditable review boundary. Required checks must pass before protected code can merge.

## Why does CI run on pull requests?
It detects regressions before merge and gives reviewers objective evidence about tests and image buildability.

## Why should CI not publish images?
Pull requests can be untrusted or unmerged. Publishing from CI risks distributing code that has not been approved. CI should validate; the tag-driven release workflow should publish.

## Why is `python:3.11-slim` used?
It pins the major/minor runtime and reduces image size compared with a full Python image. It is more reproducible than `latest`.

## What does semantic versioning mean?
`MAJOR.MINOR.PATCH`: breaking API changes increment major, compatible features increment minor, and fixes increment patch.

## Why tag images with a commit SHA?
A SHA tag identifies the exact source revision and supports auditing and rollback even if a mutable tag changes.

## What are OCI labels?
Standard image metadata labels record version, revision, source, creation time, and other provenance information.

## Why order Dockerfile COPY instructions?
Dependencies change less frequently than source code. Copying `requirements.txt` and installing before application files lets Docker reuse the dependency layer when only code changes.

## How does rollback work?
Stop the current container and run a known-good immutable version or commit-SHA image from GHCR. No source checkout or rebuild is required.

## What is the difference between an image ID and a digest?
An image ID is a local Docker identifier. A registry digest is a content-addressed immutable reference for a pushed image manifest.

## How is malformed JSON handled?
The endpoint checks `request.is_json`, parses silently, and returns HTTP 400 with a stable error message when the body is not valid JSON.

## How is traceability maintained?
The PR, merge SHA, Git tag, GitHub Actions run, version/latest/SHA image tags, OCI revision, and registry digest are recorded together.
