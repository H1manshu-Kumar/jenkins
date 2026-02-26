# 🧪 Lab 01 - Jenkins Controller + Agent Setup

> Learn how Jenkins distributes builds across nodes and why production setups never run workloads on the controller.

---

## 🎯 Objective

In this lab, we will:

- Run Jenkins controller in Docker
- Create a separate Jenkins agent
- Connect agent to controller
- Execute pipeline on agent
- Observe distributed build behavior

This simulates how CI systems run builds safely in production environments.

---

## 🧠 Why This Lab Matters

In real infrastructure:

- Controller orchestrates pipelines
- Agents execute workloads
- Separation improves scalability and reliability

Running builds on controller can:

- Cause resource contention
- Slow UI responsiveness
- Risk outages

Understanding this model is fundamental for CI/CD operations.

---

## 🏗️ Architecture Overview

Developer → Jenkins Controller → Build Queue → Agent → Workspace → Build Execution

Controller schedules → Agent runs.

---

## 🧰 Prerequisites

- Docker installed
- Docker Compose (optional but helpful)
- Basic Jenkins setup completed
- Internet access

---

## 🚀 Step 1 - Run Jenkins Controller

Pull Jenkins image:

```bash
docker pull jenkins/jenkins:lts
```

Run container:

```bash
docker run -d   --name jenkins-controller   -p 8181:8080   -p 50000:50000   -v jenkins_home:/var/jenkins_home   jenkins/jenkins:lts
```

---

## 🔎 Step 2 - Unlock Jenkins

Get admin password:

```bash
docker exec jenkins-controller cat /var/jenkins_home/secrets/initialAdminPassword
```

Open:

http://localhost:8181

Install suggested plugins.

Create admin user.

---

## ⚙️ Step 3 - Configure Agent in Jenkins

Go to:

Manage Jenkins → Nodes → New Node

Create:

- Name: docker-agent
- Type: Permanent Agent

Configure:

- Executors: 2
- Remote root directory: /home/jenkins/agent
- Labels: docker
- Launch method: Launch agent via JNLP

Save.   

<img width="1264" height="377" alt="image" src="https://github.com/user-attachments/assets/71f38d1e-9a6c-4873-8e9e-e2df537dc0ff" />

---

## 🧱 Step 4 - Run Agent Container

Run agent:

```bash
docker run -d --name jenkins-agent --network host jenkins/inbound-agent -url http://localhost:8181 -secret <JENKINS_AGENT_SECRET> -name docker-agent -workDir=/home/jenkins/agent

```

Get secret from node configuration page.

---

## ✅ Step 5 - Verify Agent Connection

In Jenkins UI:

Manage Nodes → docker-agent

Status should show:

✅ Connected   

<img width="1264" height="377" alt="image" src="https://github.com/user-attachments/assets/800b79ed-529f-443d-b42e-abbd69f2d90b" />

---

## 🧪 Step 6 - Create Test Pipeline

Create pipeline job:

New Item → Pipeline → lab01-test

Pipeline script:

```groovy
pipeline {
    agent { label 'docker' }

    stages {
        stage('Verify Agent') {
            steps {
                sh 'hostname'
                sh 'whoami'
            }
        }
    }
}
```

Run build.

---

## 🔍 What To Observe

- Build runs on agent (not controller)
- Console shows agent hostname
- Workspace created on agent
- Executor usage visible
</br>
<img width="953" height="477" alt="image" src="https://github.com/user-attachments/assets/1f7c84fa-393c-405f-85dd-0d14e417ebcf" />

---

## 🧪 Step 7 - Observe Queue Behavior

Trigger multiple builds quickly.

Watch:

- Build Queue
- Executors
- Node utilization

Understand scheduling.

---

## 📊 Expected Outcome

You should see:

- Controller idle
- Agent doing work
- Pipeline execution logs

---

## 🔥 Failure Simulation

Stop agent:

```bash
docker stop jenkins-agent
```

Trigger build.

Observe:

- Build waiting in queue
- Label restriction behavior

Restart agent:

```bash
docker start jenkins-agent
```

Build resumes.

---

## 🧠 Deep Learning Notes

Notice:

- Controller schedules tasks
- Agent maintains workspace
- Build logs streamed back
- Network connectivity required

---

## 🛠️ Troubleshooting Guide

### Agent not connecting

Check:

- URL reachable
- Secret correct
- Port 50000 open

---

### Build stuck in queue

Check:

- Agent online
- Label mismatch
- Executor availability

---

### Permission issues

Ensure agent directory writable.

---

## 🧑‍💻 Real Production Insights

Large companies use:

- Kubernetes agents
- Auto-scaling workers
- Ephemeral build nodes

Static agents are rarely used at scale.

---

## 🎓 Interview Talking Points


- Why controller should not run builds
- How Jenkins schedules builds
- What happens if agent goes offline
- How to scale Jenkins horizontally
- Difference between executor vs node

Strong answer example:

“Controller handles orchestration while agents execute workloads to prevent resource contention.”

---

## 📌 Lessons Learned
- Jenkins controller schedules builds while agents execute workloads.
- Running builds on the controller can cause performance and stability issues.
- Agents authenticate using a secret token to ensure secure connections.
- Labels control where pipelines run and help route workloads.
- Build queue behavior depends on executor availability.
- If an agent goes offline, builds remain queued until capacity returns.
- Workspaces are created on agents and persist between builds unless cleaned.
- Logs from both controller and agent are critical for debugging connectivity issues.
- Distributed builds improve scalability and isolate failures.
- Understanding node configuration is essential for troubleshooting CI problems.

---

## 🚀 Stretch Exercise

Try:

- Add second agent
- Run parallel builds
- Observe load distribution

---

> Mastering distributed builds is the first step toward designing scalable CI systems.

---

## ✍️ Author

**[Himanshu Kumar](https://www.linkedin.com/in/h1manshu-kumar/)** - Learning by building, documenting, and sharing 🚀

