# Release Notes

## v1.0.0

Initial Flask prediction API. `/health` returns application health and version; `/predict` doubles a validated numeric value. Published image tags are `1.0.0`, `latest`, and the release commit SHA.

## v1.1.0 implementation plan

Create `feature/model-metadata`, update `VERSION` to `1.1.0`, and use the version-aware health response:

```json
{
  "status": "healthy",
  "application": "student-ml-api",
  "application_version": "1.1.0",
  "model_version": "model-1"
}
```

Update the health test, commit the change, open and merge the PR, then run:

```bash
git tag v1.1.0
git push origin v1.1.0
```

The release workflow publishes `1.1.0`, `latest`, and the commit SHA. Roll back by running the `1.0.0` or known-good SHA image directly from GHCR.
