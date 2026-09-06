# Screenshot Checklist

Capture the following with the repository name and relevant URL or command visible where possible.

1. Repository structure showing application, tests, Dockerfile, workflows, README, and REPORT.
2. `feature/prediction-api` branch.
3. PR #1 showing title, description, and checks.
4. Deliberately failed CI run.
5. Corrected test commit and passing CI.
6. Successful PR CI checks.
7. Branch protection settings for `main`.
8. Successful `docker build` output.
9. `docker ps` showing port mapping.
10. `/health` response from the running container.
11. GHCR `1.0.0` package tag.
12. GHCR `1.1.0` package tag.
13. GHCR `latest` tag.
14. Successful release workflow run.
15. Git tags `v1.0.0` and `v1.1.0`.
16. Traceability table populated with SHA, tag, and digest.
17. Rollback running the previous registry image without a rebuild.

Store images in the submission evidence folder and name them `01-structure.png` through `17-rollback.png`.
