# Execution Commands

## Required demonstration

Run these steps from a clean folder and capture the terminal output for the
submission evidence.

```powershell
git clone https://github.com/hassaan07mudassar/student-ml-api.git
cd student-ml-api
git log --oneline --decorate --all
git show --stat --oneline ee593b2
```

Open the repository Pull Requests page and show PRs `#1` and `#2`. Open the
Actions page and show the failed CI run, successful CI run, and successful
release run. Then pull and run the published image:

```powershell
docker pull ghcr.io/hassaan07mudassar/student-ml-api:1.1.0
docker run -d --name student-ml-api -p 5000:5000 ghcr.io/hassaan07mudassar/student-ml-api:1.1.0
curl http://localhost:5000/health
curl -Method POST -Uri http://localhost:5000/predict -Headers @{"Content-Type"="application/json"} -Body '{"value":10}'
```

Demonstrate rollback without rebuilding:

```powershell
docker rm -f student-ml-api
docker pull ghcr.io/hassaan07mudassar/student-ml-api:1.0.0
docker run -d --name student-ml-api -p 5000:5000 ghcr.io/hassaan07mudassar/student-ml-api:1.0.0
curl http://localhost:5000/health
```

The first health response is the v1.1.0 metadata response. The rollback
response is the v1.0.0 response, proving that the previous registry artifact
was restored without a source checkout or Docker rebuild.

## Git workflow

```bash
git checkout main
git pull origin main
git checkout -b feature/prediction-api
git add .
git commit -m "feat: add Flask prediction API"
git push -u origin feature/prediction-api
```

After tests and documentation are added:

```bash
git add .
git commit -m "test: add API unit tests"
git add .
git commit -m "docs: add project documentation"
git push origin feature/prediction-api
```

Open a PR from `feature/prediction-api` into `main`. Use Squash and Merge after required checks pass.

## Deliberate CI failure

```bash
# On the feature branch, temporarily change the health assertion.
# assert data["status"] == "wrong"
git add tests/test_app.py
git commit -m "test: demonstrate CI failure"
git push origin feature/prediction-api
```

Restore the assertion and push the fix:

```bash
# assert data["status"] == "healthy"
git add tests/test_app.py
git commit -m "fix: correct health endpoint test"
git push origin feature/prediction-api
```

## Docker

```bash
docker build -t student-ml-api:1.0.0 .
docker run -d --name student-ml-api -p 5000:5000 student-ml-api:1.0.0
docker images
docker ps
docker logs student-ml-api
docker inspect student-ml-api
docker exec -it student-ml-api sh
curl http://localhost:5000/health
curl -X POST http://localhost:5000/predict -H "Content-Type: application/json" -d "{\"value\":10}"
```

Container ID and port are shown by `docker ps`; image ID by `docker images`; command, working directory, and labels by `docker inspect`.

## GHCR setup and release

```bash
echo "$GITHUB_TOKEN" | docker login ghcr.io -u USERNAME --password-stdin
git tag v1.0.0
git push origin v1.0.0
```

The token needs `contents: read` and `packages: write`. GitHub Actions uses its built-in `GITHUB_TOKEN`; no token is committed to the repository. The workflow extracts `1.0.0` from `v1.0.0` and pushes `1.0.0`, `latest`, and the full commit SHA.

## Reproducibility and rollback

```bash
docker rm -f student-ml-api
docker rmi ghcr.io/USERNAME/student-ml-api:1.0.0
docker pull ghcr.io/USERNAME/student-ml-api:1.0.0
docker run -d --name student-ml-api -p 5000:5000 ghcr.io/USERNAME/student-ml-api:1.0.0
curl http://localhost:5000/health
```

Replace `USERNAME` with the GitHub owner. For rollback, pull and run the known-good version or SHA tag directly; do not rebuild it.

## Docker cache experiment

```bash
docker build --progress=plain -t student-ml-api:cache-1 .
# Change app.py, then rebuild and observe the dependency layer is reused.
docker build --progress=plain -t student-ml-api:cache-2 .
# Change requirements.txt, then rebuild and observe pip install runs again.
docker build --progress=plain -t student-ml-api:cache-3 .
```
