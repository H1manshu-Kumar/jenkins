# Lab 03 — Multi-Stage Declarative Pipeline with Real App

## What this lab demonstrates

Most Jenkins tutorials use `echo "hello world"` as the app.
This lab uses **DevPulse** — a real Flask web app with a SQLite backend,
REST API endpoints, and a working test suite — to show what a production-style
CI/CD pipeline actually looks like.

## Pipeline stages

| Stage | What it does | Fails if... |
|---|---|---|
| Install | pip install in virtualenv | package missing |
| Lint | flake8 on app.py + models.py | any style violation |
| Test | pytest with -v flag | any test fails |
| Build Artifact | zip project into devpulse-build.zip | zip command errors |
| Health Check | start app → curl /health → kill | /health not returning ok |
| Archive | saves zip via archiveArtifacts | build already failed |

## How to run locally
```bash
cd app/
pip install -r requirements.txt
python app.py
# visit http://localhost:5000
```

## How to set up Jenkins job

1. Create a new Pipeline job in Jenkins
2. Set Definition → Pipeline script from SCM
3. Point SCM to this repo, branch: main
4. Set Script Path: lab03-multi-stage-pipeline/Jenkinsfile
5. Save → Build Now

## Key learning from this lab

- How a lint gate stops bad code from reaching test stage
- How to run a background process inside a Jenkins sh step and kill it cleanly
- How archiveArtifacts creates downloadable build outputs
- Why the post{} block matters for real team visibility
