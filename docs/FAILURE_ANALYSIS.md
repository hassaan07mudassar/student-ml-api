# Failure Analysis

## Failure 1: pytest failure

**Symptom:** The pull-request CI test job failed and the PR could not merge.

**Root cause:** A deliberately incorrect assertion expected `data["status"] == "wrong"` instead of `data["status"] == "healthy"`.

**Evidence:** The pytest output identifies the failing health endpoint assertion, and the failed GitHub Actions run is linked in the submission evidence.

**Correction:** Restore the expected value, commit `fix: correct health endpoint test`, push the branch, and rerun CI. The subsequent run must show all tests passing.

## Failure 2: wrong container port

**Symptom:** The container was running, but `curl http://localhost:5000/health` failed to connect.

**Root cause:** The container port was published incorrectly, for example `-p 8000:5000`, while the verification command targeted host port 5000.

**Evidence:** `docker ps` showed the incorrect host mapping and the curl command returned a connection error.

**Correction:** Stop and remove the container, then run `docker run -d --name student-ml-api -p 5000:5000 student-ml-api:1.0.0`. Verify the mapping with `docker ps` and repeat curl.
