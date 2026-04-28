# 🐳 Lab 06 - Docker + Jenkins CI Pipeline (Build, Tag & Push)

> Extend the DevPulse CI pipeline to containerize the application, build a production-ready Docker image, and push it to DockerHub - turning your app into a deployable container artifact.

---

## 🎯 Project Overview

This lab extends **Lab-05's artifact management pipeline** by introducing Docker as the primary CI artifact format. Instead of packaging the app as a `.tar.gz` and uploading to S3, we now **build a Docker image**, tag it with version metadata, and **push it to DockerHub** - the industry-standard way to ship deployable artifacts in modern DevOps.

**Key Achievement:** Successfully containerized the DevPulse Flask app, built a production-ready Docker image from Jenkins CI, and published it to DockerHub with proper versioning.

---

## 🧠 Why Docker Images as CI Artifacts?

| Lab-05 Approach (S3 Tarball) | Lab-06 Approach (Docker Image) |
|---|---|
| `.tar.gz` stored in S3 | Docker image stored in DockerHub |
| Needs Python + deps on target machine | Self-contained - runs anywhere |
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
| Docker socket mount | DooD - Docker-out-of-Docker |

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
docker exec -it jenkins-controller docker --version
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

<!-- SCREENSHOT: Jenkins Credentials Store showing 'dockerhub-creds' entry configured -->
<img width="1052" height="83" alt="image" src="https://github.com/user-attachments/assets/97d3f447-a3a2-4072-97cc-50351a0f80a9" />

---

### Step 2 - Create the Dockerfile

Place `Dockerfile` in `phase-2-jenkins-pipeline/devpulse/`:

```dockerfile
FROM python:3.12-slim

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
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:5000/health')" || exit 1

CMD ["python", "app.py"]
```

**Why each instruction matters:**

| Instruction | Why It's There |
|---|---|
| `python:3.12-slim` | Smaller base image — fewer vulnerabilities, faster pulls |
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
        image 'python:3.12-slim'
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
    DOCKERHUB_USERNAME = 'dockerhub-creds'
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

## 📊 Pipeline Execution Results

### 1️⃣ Jenkins Pipeline - Stage View (All Stages Green)

<!-- SCREENSHOT: Jenkins Blue Ocean or classic stage view showing all 9 stages passed in green -->
<img width="1275" height="369" alt="image" src="https://github.com/user-attachments/assets/2dd7c83d-969c-4971-8394-525c4a7ede34" />

---

### 2️⃣ Setup Stage — Python Virtual Environment

<!-- SCREENSHOT: Jenkins console output for Setup stage showing venv creation and pip install success -->
<img width="1275" height="397" alt="image" src="https://github.com/user-attachments/assets/c9393539-4037-4667-83bc-c98a0281636f" />

---

### 3️⃣ Lint Stage — flake8 Code Quality Check

<!-- SCREENSHOT: Jenkins console output for Lint stage showing flake8 passing with zero errors -->
<img width="1275" height="161" alt="image" src="https://github.com/user-attachments/assets/a61507ff-2617-42dc-8730-7558204f45ae" />

---

### 4️⃣ Test Stage — pytest with Coverage

<!-- SCREENSHOT: Jenkins console output for Test stage showing pytest results and coverage percentage -->
<img width="1275" height="411" alt="image" src="https://github.com/user-attachments/assets/a6349297-2a82-456b-baac-6c99d11f2441" />

---

### 5️⃣ Install Docker CLI Stage

<!-- SCREENSHOT: Jenkins console output showing apt-get install docker.io and docker --version confirming installation -->
<img width="1275" height="411" alt="image" src="https://github.com/user-attachments/assets/a3c9c698-565a-4eb4-bb2e-3a704838f057" />   </br>

<img width="1275" height="411" alt="image" src="https://github.com/user-attachments/assets/97faacc6-4e3b-4f11-a09b-9fabe5cb67cc" />

---

### 6️⃣ Docker Build Stage — Image Layers Built

<!-- SCREENSHOT: Jenkins console output for Docker Build stage showing each layer step (Step 1/N ... Step N/N) -->

<img width="1275" height="411" alt="image" src="https://github.com/user-attachments/assets/3c642c63-8d7f-4cc3-a948-a6c58ca1cb46" />   </br>

<img width="1275" height="411" alt="image" src="https://github.com/user-attachments/assets/e955c8ce-8f91-45b9-b5e0-da2cfc1dfef0" />

---

### 7️⃣ Docker Login Stage — DockerHub Authentication

<!-- SCREENSHOT: Jenkins console output showing 'Login Succeeded' message for DockerHub -->
<img width="1275" height="210" alt="image" src="https://github.com/user-attachments/assets/4bd04967-01be-45a7-9422-e3925a3ce092" />

---

### 8️⃣ Docker Push Stage — Both Tags Pushed to DockerHub

<!-- SCREENSHOT: Jenkins console output for Docker Push stage showing push progress for versioned tag (e.g. 1.0.5) -->
<img width="1275" height="412" alt="image" src="https://github.com/user-attachments/assets/d46f9b25-81cc-4c13-a68c-5850ef011bcc" />   </br>


<!-- SCREENSHOT: Jenkins console output showing push progress for latest tag -->
<img width="1275" height="412" alt="image" src="https://github.com/user-attachments/assets/80968946-0830-4e68-8a93-2dce2e4e81bc" />


---

### 9️⃣ Validate Image Stage — Smoke Test Passed

<!-- SCREENSHOT: Jenkins console output for Validate Image stage showing docker pull and smoke test import passing -->
<img width="1275" height="236" alt="image" src="https://github.com/user-attachments/assets/c06a738d-eea1-401e-8793-fed83db1e26f" />

---

### 🐳 DockerHub — Image Published Successfully

<img width="1280" height="670" alt="image" src="https://github.com/user-attachments/assets/04ae3157-e7da-48ca-a40d-df56876af229" />

---

### 🧹 Post-Build — Cleanup & Final Status

<!-- SCREENSHOT: Jenkins console output for post{} block showing docker rmi cleanup and cleanWs() workspace wipe -->
<img width="1280" height="273" alt="image" src="https://github.com/user-attachments/assets/2313e45f-78fc-4e56-9e41-dd9b78b858e8" />

<img width="1280" height="453" alt="image" src="https://github.com/user-attachments/assets/33553498-d3ed-4486-8ed5-01c00039c41f" />

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

📁 **Project Structure**

```text
lab06-docker-jenkins/
├── Jenkinsfile         ← Extended CI pipeline
├── README.md           ← This file
```

---
## ✍️ Author

**[Himanshu Kumar](https://www.linkedin.com/in/h1manshu-kumar/)**   - *Building production-ready pipelines, one commit at a time* 🚀

---

🔥 *"A Docker image is not just an artifact - it's a promise that your app runs the same way everywhere."*
