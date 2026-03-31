# Pipeline stages — explained

## Why document this?

A Jenkinsfile without explanation is just syntax.
This doc explains the *why* behind each stage decision.

## Stage: Lint (flake8)

**Why it runs before tests:** Linting is cheap. Tests are expensive.
If the code has obvious style issues, fail fast before spinning up a test DB.

**Real-world parallel:** In most teams, lint runs as a pre-commit hook AND
in CI. CI is the safety net when devs skip the hook.

## Stage: Health Check

**The pattern:** start app in background → sleep 2 → curl /health → assert → kill PID

This is a smoke test, not a full test suite. It answers one question:
"Does the app even start?" — which pytest cannot tell you.

**Why /health exists in the app:** Every production service exposes a health
endpoint. Load balancers, Kubernetes liveness probes, and monitoring tools
all hit this. Building it into the app from day 1 is a DevOps habit.

## Stage: Archive

archiveArtifacts saves devpulse-build.zip to Jenkins' internal storage.
In real teams this would be an S3 upload or Nexus push. The pattern is the same.

## What I would add next

- Email/Slack notification on failure in the post{} block
- Parameterized build to pass APP_PORT as a Jenkins parameter
- Multi-branch pipeline to build feature branches separately
