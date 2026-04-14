# 🐳 Lab 06 - Docker + Jenkins CI Pipeline (Build, Tag & Push)

> Extend the DevPulse CI pipeline to containerize the application, build a production-ready Docker image, and push it to DockerHub — turning your app into a deployable container artifact.

---

## 🎯 Project Overview

This lab extends **Lab-05's artifact management pipeline** by introducing Docker as the primary CI artifact format. Instead of packaging the app as a `.tar.gz` and uploading to S3, we now **build a Docker image**, tag it with version metadata, and **push it to DockerHub** — the industry-standard way to ship deployable artifacts in modern DevOps.

**Key Achievement:** Successfully containerized the DevPulse Flask app, built a production-ready Docker image from Jenkins CI, and published it to DockerHub with proper versioning.

---

## 🧠 Why Docker Images as CI Artifacts?

| Lab-05 Approach (S3 Tarball) | Lab-06 Approach (Docker Image) |
|---|---|
| `.tar.gz` stored in S3 | Docker image stored in DockerHub |
| Needs Python + deps on target machine | Self-contained — runs anywhere |
| Manual environment setup for deployment | `docker run` is all you need |
| Good for archiving | Good for deploying |

> **Real-world context:** In production, Docker images are the most portable artifact format. Kubernetes, ECS, and any container platform pulls directly from a registry. This is why Docker CI integration is a **must-have skill** for any DevOps engineer.

---

## 🏗️ Architecture & Pipeline Flow

```text
┌──────────┐   ┌──────────┐   ┌────────┐   ┌────────┐   ┌──────────────┐
│ Checkout │ → │  Setup   │ → │  Lint  │ → │  Test  │ → │ Install      │
└──────────┘   └──────────┘   └────────┘   └────────┘   │ Docker CLI   │
                                                          └──────┬───────┘
                                                                 │
                                                                 ▼
                                                          ┌──────────────┐
                                                          │ Docker Build │
                                                          └──────┬───────┘
                                                                 │
                                                                 ▼
                                                          ┌──────────────┐
                                                          │ Docker Login │
                                                          └──────┬───────┘
                                                                 │
                                                                 ▼
                                                          ┌──────────────┐
                                                          │ Docker Push  │
                                                          └──────┬───────┘
                                                                 │
                                                                 ▼
                                                          ┌──────────────┐
                                                          │ Validate     │
                                                          │ Image        │
                                                          └──────────────┘
```

---

## 🚀 Technologies & Tools

| Technology | Purpose |
|---|---|
| Jenkins | CI/CD Orchestration |
| Docker | Image build & containerization |
| DockerHub | Container image registry |
| Python 3.11-slim | Jenkins Docker agent + app base image |
| pytest | Unit Testing |
| flake8 | Code Linting |
| Docker socket mount | DooD — Docker-out-of-Docker |

---

## 📋 Prerequisites

- Jenkins running in Docker container (local Linux machine)
- Docker installed on host machine
- DockerHub account (free at hub.docker.com)
- Jenkins credentials configured:
  - ID: `dockerhub-creds`
  - Type: Username with Password

### Verify Docker Socket Access

```bash
# - Check Docker is running on host
docker ps

# - Verify Jenkins container can reach Docker socket
docker exec -it <jenkins-container-name> docker --version
```

---

## ⚙️ Step-by-Step Implementation

### Step 1 - Add DockerHub Credentials to Jenkins

> **Why:** Docker push requires authentication. We never hardcode credentials — we use Jenkins Credentials Store.

1. Go to `Manage Jenkins` → `Credentials` → `Global` → `Add Credentials`
2. Fill in:
   - **Kind:** Username with password
   - **Username:** your DockerHub username
   - **Password:** DockerHub **Access Token** (not your password — see below)
   - **ID:** `dockerhub-creds`
   - **Description:** DockerHub Registry Credentials

> **Best Practice:** Always use a **DockerHub Access Token**, not your actual account password.
> Generate one at: `hub.docker.com` → Account Settings → Security → New Access Token

---

### Step 2 - Create the Dockerfile

Place `Dockerfile` in `phase-2-jenkins-pipeline/devpulse/`:

```dockerfile
FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

COPY *.py ./
COPY templates/ ./templates/
COPY static/ ./static/

RUN useradd --create-home --shell /bin/bash devpulse \
    && chown -R devpulse:devpulse /app
USER devpulse

EXPOSE 5000

HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:5000/')" || exit 1

CMD ["python", "app.py"]
```

**Why each instruction matters:**

| Instruction | Why It's There |
|---|---|
| `python:3.11-slim` | Smaller base image — fewer vulnerabilities, faster pulls |
| `COPY requirements.txt` first | Layer caching — pip install only re-runs if deps change |
| `--no-cache-dir` | Keeps image size small |
| `useradd devpulse` | Run as non-root — production security standard |
| `HEALTHCHECK` | Tells Docker/Kubernetes if container is actually ready |

---

### Step 3 - Update Jenkinsfile

Key sections explained:

#### Agent — Docker socket mount

```groovy
agent {
    docker {
        image 'python:3.11-slim'
        args '--user root -v /var/run/docker.sock:/var/run/docker.sock'
    }
}
```

- `-v /var/run/docker.sock:/var/run/docker.sock` — this is **DooD (Docker-out-of-Docker)**
- The Jenkins agent container uses the **host's Docker daemon** to build images
- `--user root` — needed to install Docker CLI inside the agent

#### Environment block

```groovy
environment {
    DOCKERHUB_USERNAME = 'your-dockerhub-username'   // ← Update this
    IMAGE_NAME         = "${DOCKERHUB_USERNAME}/${APP_NAME}"
    IMAGE_TAG          = "${APP_VERSION}"
}
```

#### Docker Build — dual tagging strategy

```groovy
sh """
    docker build \
        -t ${IMAGE_NAME}:${IMAGE_TAG} \
        -t ${IMAGE_NAME}:latest \
        .
"""
```

> **Why two tags?**
> - `1.0.42` → versioned tag for traceability, rollback, and audit
> - `latest` → convenience tag for dev/staging environments

#### Docker Login — secure credentials

```groovy
withCredentials([usernamePassword(
    credentialsId: 'dockerhub-creds',
    usernameVariable: 'DOCKER_USER',
    passwordVariable: 'DOCKER_PASS'
)]) {
    sh 'echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin'
}
```

> **Why `--password-stdin`?** Passing password as a flag (`-p`) exposes it in process logs. Stdin is secure.

---

### Step 4 - Project Structure

```text
phase-2-jenkins-pipeline/
└── devpulse/
    ├── Dockerfile              ← NEW in Lab-06
    ├── Jenkinsfile             ← Extended from Lab-05
    ├── app.py
    ├── requirements.txt
    ├── templates/
    ├── static/
    └── tests/
```

---

## 🔐 DooD vs DinD — Key Concept

| | Docker-out-of-Docker (DooD) | Docker-in-Docker (DinD) |
|---|---|---|
| How | Mount host Docker socket | Run full Docker daemon inside container |
| Used in | This lab ✅ | Some CI systems |
| Security | Moderate (host socket access) | Higher risk (privileged mode) |
| Performance | Fast — uses host daemon cache | Slower — fresh daemon each time |
| Common in | Jenkins on Docker | GitLab CI |

---

## 📸 Screenshots to Capture

- [ ] Jenkins pipeline stage view (all 9 stages green)
- [ ] Docker Build stage logs (showing layer caching)
- [ ] Docker Push stage logs (both tags pushed)
- [ ] DockerHub repository page (new tags visible)
- [ ] Validate Image stage output (smoke test passed)

---

## 🐛 Troubleshooting Guide

| Issue | Cause | Fix |
|---|---|---|
| `docker: command not found` | Docker CLI not in agent image | `Install Docker CLI` stage handles this |
| `permission denied /var/run/docker.sock` | Socket not mounted or wrong perms | Add `-v /var/run/docker.sock:/var/run/docker.sock` to agent args |
| `unauthorized: authentication required` | Wrong credential ID | Verify ID is exactly `dockerhub-creds` in Jenkins |
| `denied: requested access to resource is denied` | DockerHub token has no push permission | Recreate token with Read/Write/Delete permissions |
| `no such file or directory: templates/` | App structure different | Update `COPY` instructions in Dockerfile to match your actual structure |
| Smoke test fails | App import error | Check `app.py` has a valid Flask `app` object |
| Image builds but is huge | No `.dockerignore` | Add `.dockerignore` (see below) |

### Add `.dockerignore` to Keep Image Lean

```text
venv/
__pycache__/
*.pyc
*.pyo
.pytest_cache/
reports/
dist/
.git/
*.md
Jenkinsfile
```

---

## 🎓 Key Learnings & Best Practices

### ✅ What This Lab Implements

- **Dual image tagging** — versioned + latest for traceability and convenience
- **Layer caching optimization** — `requirements.txt` copied before source code
- **Non-root container user** — production security standard
- **Secure credential handling** — `withCredentials` block, never hardcoded
- **Docker socket mount (DooD)** — lightweight, cache-sharing Docker builds
- **Smoke test validation** — confirms image is pullable and app starts clean
- **Image cleanup** — removes local images in `post { always }` to save disk

### 🏢 Production Considerations

- Images should be **scanned for vulnerabilities** before push (Trivy, Snyk — Phase 3)
- Use **private registries** (AWS ECR, GCR) for production workloads
- Tag with **git commit SHA** in addition to build number for full traceability
- **Multi-stage builds** can further reduce image size (Phase 3 topic)
- Combine with **S3 artifact storage from Lab-05** — tarball for rollback, image for deploy

---

## 🎯 Interview Talking Points

> "In Lab-06, I extended the DevPulse CI pipeline to build and publish Docker images from Jenkins. I configured Docker-out-of-Docker by mounting the host socket into the Jenkins agent container, implemented a dual-tagging strategy with versioned and latest tags, and used Jenkins Credentials Store with `withCredentials` to securely authenticate with DockerHub. The pipeline runs lint and tests before building — so only verified code gets containerized."

**Key Highlights:**
- ✅ Docker image as CI artifact (industry standard)
- ✅ DooD pattern — Docker socket mount
- ✅ Dual-tag strategy — versioned + latest
- ✅ Secure DockerHub authentication via `withCredentials`
- ✅ Image smoke test — validates registry push end-to-end
- ✅ Layer caching — optimized Dockerfile structure
- ✅ Non-root container user — production security

---

## 📊 Lab-05 vs Lab-06 — Artifact Strategy Comparison

| | Lab-05 | Lab-06 |
|---|---|---|
| Artifact type | `.tar.gz` tarball | Docker image |
| Storage | AWS S3 | DockerHub |
| Deployment method | Extract + run on server | `docker run` anywhere |
| Versioning | `APP_VERSION` in S3 path | Image tag |
| Rollback | Download old tarball from S3 | Pull old image tag from DockerHub |
| Best for | Archiving, compliance | Deploying to containers / K8s |

> **Pro Tip:** In mature pipelines, you do **both** — push the Docker image to a registry AND store the build manifest in S3 for audit and compliance.

---

## 🚀 Next - Phase 3 Preview

- Trigger builds via **GitHub Webhooks** (auto-trigger on push)
- **Parallel pipeline stages** (lint + test run simultaneously)
- **Docker image vulnerability scanning** with Trivy
- **Multi-stage Dockerfiles** for smaller production images
- **Jenkins agents on Kubernetes** (dynamic scaling)

---

📁 **Project Structure**

```text
lab06-docker-jenkins/
├── Dockerfile      ← Container image definition
├── Jenkinsfile     ← Extended CI pipeline
└── README.md       ← This file
```

---

✍️ **Author**

Himanshu Kumar
DevOps Engineer | Docker | Jenkins | AWS | CI/CD Automation

Containerizing applications, one pipeline at a time 🐳

---

🔥 *"A Docker image is not just an artifact — it's a promise that your app runs the same way everywhere."*
