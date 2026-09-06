# Branch Protection

Configure GitHub repository settings at **Settings -> Branches -> Add branch ruleset** for `main`.

- Require a pull request before merging. This ensures review and a visible audit trail.
- Require status checks to pass: the `Test API` and `Validate Docker build` jobs must be green.
- Require branches to be up to date before merging. This prevents merging a branch tested against stale `main`.
- Disable direct pushes by restricting who can push to `main` and requiring pull requests.
- Require conversation resolution and at least one approving review where available.
- Block force pushes and branch deletion.
- Choose Squash and Merge as the only permitted merge method.

After saving, capture the rule configuration for screenshot 7 and verify that a direct push is rejected.
