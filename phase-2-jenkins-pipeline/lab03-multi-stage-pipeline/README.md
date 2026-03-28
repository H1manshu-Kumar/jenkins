<div align="center">

<img src="https://img.shields.io/badge/Jenkins-D24939?style=for-the-badge&logo=jenkins&logoColor=white" alt="Jenkins"/>
<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
<img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask"/>
<img src="https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite"/>
<img src="https://img.shields.io/badge/pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white" alt="pytest"/>
<img src="https://img.shields.io/badge/flake8-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="flake8"/>

<br/><br/>

# 🚀 Lab 03 — Multi-Stage Declarative Pipeline

### *Real CI/CD. Real App. Not Hello World.*

<br/>

> **DevPulse** is a developer metrics tracker built with Flask + SQLite.  
> This lab uses it as the target app to demonstrate a production-style  
> Jenkins declarative pipeline with lint gates, smoke tests, and artifact archiving.

<br/>

[![Pipeline Stages](https://img.shields.io/badge/Pipeline_Stages-7-2ea44f?style=flat-square)](#-pipeline-overview)
[![App Endpoints](https://img.shields.io/badge/App_Endpoints-4-blue?style=flat-square)](#-devpulse-app)
[![Test Cases](https://img.shields.io/badge/Test_Cases-5-purple?style=flat-square)](#-test-suite)
[![Lab Status](https://img.shields.io/badge/Lab_Status-Completed-success?style=flat-square)](#)

</div>

---

## 📌 Why This Lab Exists

Most Jenkins tutorials look like this:

```groovy
pipeline {
    agent any
    stages {
        stage('Hello') {
            steps {
                echo 'Hello World'
            }
        }
    }
}
```

**This lab doesn't.**

A real pipeline needs a real app. **DevPulse** is a working Flask web application with a database, REST API endpoints, a test suite, and linting — exactly what a production pipeline would run against. Every stage in this Jenkinsfile does something meaningful and can **actually fail** for a real reason.

---

## 📁 Folder Structure

```
lab03-multi-stage-pipeline/
│
├── devpulse/                   # Flask application source
│   ├── app.py                  # Main app — routes and startup
│   ├── models.py               # SQLite DB logic
│   ├── requirements.txt        # Flask, pytest, flake8
│   ├── templates/
│   │   ├── index.html          # Log entry form
│   │   └── dashboard.html      # Metrics dashboard
│   └── static/
│       └── style.css           # Clean flat UI styles
│
├── tests/
│   └── test_app.py             # 5 pytest cases (all endpoints covered)
│
├── Jenkinsfile                 # ⭐ Declarative pipeline — 7 stages
│
├── docs/
│   ├── pipeline-stages.md      # Why each stage exists
│   ├── lessons-learned.md      # Real issues hit during setup
│   └── screenshots/            # Jenkins build evidence
│       ├── pipeline-success.png
│       ├── lint-failure.png
│       └── test-report.png
│
└── README.md                   # This file
```

---

## 🛠 DevPulse App

DevPulse is a personal developer metrics tracker. It lets you log your daily work and view a running summary — tasks done, bugs fixed, PRs raised.

### Endpoints

| Method | Endpoint | Description | Used by Jenkins |
|--------|----------|-------------|-----------------|
| `GET` | `/` | Entry form | - |
| `POST` | `/log` | Submit a daily entry | - |
| `GET` | `/dashboard` | View all entries + totals | - |
| `GET` | `/health` | Returns `{"status": "ok", "db": "connected"}` | ✅ Health Check stage |
| `GET` | `/api/stats` | Returns `{total_tasks, total_bugs, total_prs}` | ✅ Test suite |

### Run it locally

```bash
cd devpulse/
pip install -r requirements.txt
python app.py
# → http://localhost:5000
```

> SQLite DB is created automatically on first run. No setup needed.

---

## ⚙️ Pipeline Overview

```
 ┌─────────────┐     ┌──────────────┐     ┌────────┐     ┌────────┐
 │  1.Checkout │────▶│ 2. Install   │────▶│ 3.Lint │────▶│ 4.Test │
 └─────────────┘     └──────────────┘     └────────┘     └────────┘
                                               ❌                ❌
                                          fails on          fails on
                                         flake8 error     pytest fail
                                                               │
                              ┌────────────────────────────────┘
                              ▼
                    ┌──────────────────┐     ┌──────────────┐     ┌─────────┐
                    │ 5. Build Artifact│────▶│ 6.HealthCheck│────▶│7.Archive│
                    └──────────────────┘     └──────────────┘     └─────────┘
                                                    ❌
                                             fails if /health
                                             doesn't return ok

                                        ┌───────────────────┐
                                        │  post { always }  │
                                        │  success / failure │
                                        └───────────────────┘
```

### Stage Breakdown

<details>
<summary><strong>Stage 1 — Checkout</strong></summary>

Jenkins handles this automatically when the pipeline is configured with SCM. This stage is a placeholder with an echo to confirm the workspace is ready.

```groovy
stage('Checkout') {
    steps {
        echo 'Source code checked out by Jenkins SCM'
    }
}
```

</details>

<details>
<summary><strong>Stage 2 — Install Dependencies</strong></summary>

Creates a Python virtualenv and installs all packages from `requirements.txt`. Using a virtualenv keeps the Jenkins agent environment clean and prevents package conflicts across jobs.

```groovy
stage('Install Dependencies') {
    steps {
        sh '''
            python3 -m venv venv
            . venv/bin/activate
            pip install -r devpulse/requirements.txt
        '''
    }
}
```

**Why this matters:** In real teams, the agent may be shared across multiple pipelines. A virtualenv ensures this job's dependencies don't bleed into others.

</details>

<details>
<summary><strong>Stage 3 — Lint (flake8) 🔴 Can fail build</strong></summary>

Runs `flake8` on `app.py` and `models.py`. If any style violation is found, the build fails here — before tests even run.

```groovy
stage('Lint') {
    steps {
        sh '''
            . venv/bin/activate
            flake8 devpulse/app.py devpulse/models.py --max-line-length=100
        '''
    }
}
```

**Why lint runs before tests:** Linting is cheap (milliseconds). Tests are expensive (they start the app, hit a DB, etc.). Fail fast on obvious issues first.

**Real-world parallel:** Most teams run lint as both a pre-commit hook and a CI gate. CI is the safety net when devs skip the hook.

</details>

<details>
<summary><strong>Stage 4 — Test (pytest) 🔴 Can fail build</strong></summary>

Runs all 5 pytest cases with verbose output. Any test failure fails the build.

```groovy
stage('Test') {
    steps {
        sh '''
            . venv/bin/activate
            pytest tests/ -v
        '''
    }
}
```

**Tests covered:**
- `GET /` returns 200
- `POST /log` inserts record and redirects
- `GET /dashboard` returns 200 and contains "Dashboard"
- `GET /health` returns `{"status": "ok"}`
- `GET /api/stats` returns correct metric keys

</details>

<details>
<summary><strong>Stage 5 — Build Artifact</strong></summary>

Zips the project into `devpulse-build.zip`, excluding cache and git files. This is the deployable artifact.

```groovy
stage('Build Artifact') {
    steps {
        sh '''
            zip -r devpulse-build.zip . \
                --exclude="*.pyc" \
                --exclude="__pycache__/*" \
                --exclude=".git/*" \
                --exclude="venv/*"
        '''
    }
}
```

**In production this would be:** An S3 upload, Nexus push, or Docker image build. The zip pattern is the same — package, version, store.

</details>

<details>
<summary><strong>Stage 6 — Health Check 🔴 Can fail build</strong></summary>

Starts the Flask app in the background, waits for it to be ready, curls the `/health` endpoint, then kills the process. This is a smoke test — it answers one question: *does the app actually start?*

```groovy
stage('Health Check') {
    steps {
        sh '''
            . venv/bin/activate
            cd devpulse
            python app.py &
            APP_PID=$!
            sleep 2
            RESPONSE=$(curl -s http://localhost:5000/health)
            echo "Health response: $RESPONSE"
            echo $RESPONSE | grep -q '"status": "ok"'
            kill $APP_PID
        '''
    }
}
```

**Why this exists:** pytest verifies logic. Health Check verifies the app actually boots in a real environment. These are different things.

**Real-world parallel:** Kubernetes liveness probes, AWS ALB target health checks, and uptime monitors all follow this exact pattern.

</details>

<details>
<summary><strong>Stage 7 — Archive</strong></summary>

Saves `devpulse-build.zip` to Jenkins' internal artifact storage, making it downloadable from the build page.

```groovy
stage('Archive') {
    steps {
        archiveArtifacts artifacts: 'devpulse-build.zip', fingerprint: true
    }
}
```

</details>

<details>
<summary><strong>Post Block — Always runs</strong></summary>

The `post` block runs regardless of whether the pipeline passed or failed. This is where you notify teams, clean up, or log outcomes.

```groovy
post {
    always {
        echo 'Pipeline finished'
    }
    success {
        echo 'Build passed — DevPulse artifact ready'
    }
    failure {
        echo 'Build failed — check logs above for the failing stage'
    }
}
```

**In production this would be:** Slack notification, email alert, Jira ticket creation, or PagerDuty trigger.

</details>

---

## 🧪 Test Suite

```python
# tests/test_app.py

def test_home_returns_200(client):               # GET /
def test_log_entry_redirects(client):            # POST /log
def test_dashboard_loads(client):                # GET /dashboard
def test_health_endpoint(client):                # GET /health → {"status": "ok"}
def test_stats_returns_metric_keys(client):      # GET /api/stats → keys present
```

Run locally:
```bash
pytest tests/ -v
```

---

## 🔧 Jenkins Job Setup

### Option A — Pipeline from SCM (recommended)

1. Open Jenkins → **New Item** → **Pipeline**
2. Under **Pipeline**, set Definition → `Pipeline script from SCM`
3. SCM → `Git` → paste your repo URL
4. Branch → `main`
5. Script Path → `lab03-multi-stage-pipeline/Jenkinsfile`
6. **Save** → **Build Now**

### Option B — Paste Jenkinsfile manually

1. Open Jenkins → **New Item** → **Pipeline**
2. Under **Pipeline**, set Definition → `Pipeline script`
3. Paste the contents of `Jenkinsfile` directly
4. **Save** → **Build Now**

### Prerequisites on Jenkins agent

| Requirement | Check |
|-------------|-------|
| Python 3 | `python3 --version` |
| pip | `pip --version` |
| zip | `zip --version` |
| curl | `curl --version` |

---

## 💡 Lessons Learned

Real issues hit while building this lab. Each one taught something worth knowing.

<details>
<summary><strong>Issue 1 — virtualenv doesn't persist across sh steps</strong></summary>

**Problem:** Activated the virtualenv in one `sh` step. It wasn't active in the next step.

**Why:** Each `sh` block in Jenkins runs in a fresh subshell. Activating a virtualenv sets environment variables in the current shell — which dies at the end of the step.

**Fix:** Source `activate` at the start of every `sh` step that needs it.

```groovy
sh '. venv/bin/activate && pytest tests/ -v'
```

</details>

<details>
<summary><strong>Issue 2 — curl fails because app isn't ready yet</strong></summary>

**Problem:** Health Check stage was failing — curl ran before Flask finished starting.

**Why:** Python app startup takes ~1-2 seconds. The `&` operator starts the process but returns immediately.

**Fix:** Added `sleep 2` after the background start.

```bash
python app.py &
sleep 2   # give Flask time to bind to port 5000
curl http://localhost:5000/health
```

</details>

<details>
<summary><strong>Issue 3 — PID variable lost between sh steps</strong></summary>

**Problem:** Tried to save the background app's PID in one `sh` step and kill it in another. The variable was gone.

**Why:** Shell variables don't persist between separate `sh` blocks — same subshell isolation issue as virtualenv.

**Fix:** Start the app, curl it, and kill it all inside the same `sh` block using `$!`.

```bash
python app.py &
APP_PID=$!
sleep 2
curl http://localhost:5000/health
kill $APP_PID
```

</details>

---

## 🗺 What's Next

This lab is the foundation. Here is what builds on top of it:

| Next Lab | Concept | Builds on this by... |
|----------|---------|----------------------|
| Lab 04 | Parameterized Builds | Pass `APP_PORT` as Jenkins parameter — run DevPulse on any port |
| Lab 05 | Multi-Branch Pipeline | Auto-build feature branches — `feat/*` gets lint+test, `main` gets full pipeline |
| Lab 06 | Shared Libraries | Extract virtualenv setup into a reusable `vars/pythonBuild.groovy` |
| Lab 07 | Docker Integration | Replace virtualenv with a Docker container — no agent dependencies |
| Lab 08 | Notifications | Add Slack/email alerts in the `post` block on failure |

---

## 🔗 Part of a Larger Journey

This lab is part of my **QA → DevOps** transition, documented publicly on GitHub.

| Lab | Topic | Status |
|-----|-------|--------|
| Lab 01 | Jenkins setup, first pipeline, plugins | ✅ Done |
| Lab 02 | Pipeline architecture, backup/restore | ✅ Done |
| **Lab 03** | **Multi-stage pipeline with real app** | ✅ Done |
| Lab 04 | Parameterized builds | 🔄 In progress |
| Lab 05 | Multi-branch pipeline | 📋 Planned |

> 📌 Follow the full journey: [github.com/H1manshu-Kumar/jenkins](https://github.com/H1manshu-Kumar/jenkins)

---

<div align="center">

**Built while learning in public.**  
*If this helped you, drop a ⭐ — it keeps the motivation going.*

<br/>

![Made with Jenkins](https://img.shields.io/badge/Made_with-Jenkins-D24939?style=flat-square&logo=jenkins&logoColor=white)
![Learning in Public](https://img.shields.io/badge/Learning-In_Public-0A9EDC?style=flat-square)
![QA to DevOps](https://img.shields.io/badge/QA_→_DevOps-Transition-2ea44f?style=flat-square)

</div>
