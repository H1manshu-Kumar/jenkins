# 🧪 Lab 02 — Pipeline Execution Lifecycle Deep Dive

> Understand how Jenkins pipelines are scheduled, executed, persisted, and recovered across restarts.

---

## 🎯 Objective

In this lab, we will:

- Create a multi-stage pipeline
- Observe pipeline execution flow
- Understand Jenkins queue and executor behavior
- Simulate Jenkins restart during build
- Observe pipeline durability
- Analyze logs and execution states

This mirrors real-world CI environments where builds run across infrastructure changes.

---

## 🧠 Why This Lab Matters

In production:

- Jenkins controllers restart (patching, crashes, upgrades)
- Builds must survive interruptions
- Engineers must understand execution flow to debug failures

Pipeline durability is critical for reliable CI/CD.

---

## 🏗️ Execution Flow Overview

Developer push → Jenkins webhook → Queue → Executor → Pipeline engine → Agent → Logs → Artifacts

---

## 🧰 Prerequisites

- Lab 01 completed
- Jenkins controller running
- Agent connected
- Basic pipeline job experience

---

## 🚀 Step 1 — Create Pipeline Job

Go to:

New Item → Pipeline

Name:

lab02-pipeline-lifecycle

---

## 🧪 Step 2 — Add Pipeline Script

```groovy
pipeline {
    agent { label 'docker' }

    stages {
        stage('Start') {
            steps {
                echo "Pipeline started"
            }
        }

        stage('Simulate Work') {
            steps {
                sh 'sleep 60'
            }
        }

        stage('Verification') {
            steps {
                echo "Pipeline completed"
            }
        }
    }
}
```

This creates a long-running stage.

---

## ▶️ Step 3 — Run Build

Click:

Build Now

Observe:

- Stage view
- Console output
- Node assignment

---

## 🔍 Step 4 — Observe Execution Details

Look at:

- Build queue
- Executor usage
- Pipeline visualization
- Console logs

Notice how Jenkins tracks state.

---

## 🔥 Step 5 — Simulate Controller Restart

While pipeline is in sleep stage:

Restart Jenkins container:

```bash
docker restart jenkins-controller
```

Wait for Jenkins to come back.

---

## 👀 Step 6 — Observe Build After Restart

Open build.

You should see:

- Pipeline resumes
- Stage continues or restarts
- Logs preserved

This demonstrates pipeline durability.

---

## 🧪 Step 7 — Inspect Logs

Check:

Manage Jenkins → System Log

Look for:

- Pipeline resumption messages
- Queue activity

---

## 📊 Expected Behavior

- Build survives restart
- Pipeline resumes execution
- State preserved in Jenkins Home

---

## 🧠 Deep Learning Notes

Jenkins pipelines use:

- CPS (Continuation Passing Style)
- Serialized execution state
- Persistent checkpoints

This enables recovery.

---

## 🛠️ Failure Experiment

Kill Jenkins mid-build multiple times.

Observe:

- Resumption consistency
- Stage replay behavior

---

## 📦 Step 8 — Archive Artifact Test

Update pipeline:

```groovy
stage('Artifact') {
    steps {
        sh 'echo hello > file.txt'
        archiveArtifacts artifacts: 'file.txt'
    }
}
```

Run again.

Observe artifact storage.

---

## 🧑‍💻 Real Production Insights

Important realities:

- Jenkins restarts during maintenance
- Long builds must survive
- Pipeline checkpoints prevent data loss

---

## 🎓 Interview Talking Points

Be ready to explain:

- What happens when Jenkins restarts during build?
- How pipeline state is persisted?
- What is pipeline durability?
- Difference between freestyle vs pipeline recovery

Strong answer:

“Jenkins pipelines persist execution state in Jenkins Home and resume using CPS checkpoints.”

---

## 🧩 Evidence To Add

- Pipeline stage view screenshot
- Restart test screenshot
- Logs showing resumption
- Artifact view

---

## 📌 Lessons Learned

- …
- …
- …

---

## 🚀 Stretch Exercise

Try:

- Parallel stages
- Long running builds
- Manual input step

---

## 🏁 Lab Completion Checklist

- [ ] Pipeline created
- [ ] Restart tested
- [ ] Resumption observed
- [ ] Logs inspected
- [ ] Artifact archived

---

> Understanding pipeline lifecycle is essential for diagnosing real CI failures.



