# 🧪 Lab 04 — Workspace Behavior & Build Isolation

> Understand how Jenkins manages workspaces and how build isolation prevents flaky pipelines.

---

## 🎯 Objective

In this lab, we will:

- Explore Jenkins workspace lifecycle
- Understand how workspaces are created
- Observe behavior across builds
- Simulate workspace deletion
- Learn build isolation impact

This mirrors real CI environments where workspace issues cause flaky builds.

---

## 🧠 Why This Lab Matters

In production:

- Dirty workspaces cause unpredictable builds
- Cached files may break deployments
- Build reproducibility depends on isolation

Understanding workspace behavior helps prevent pipeline instability.

---

## 🏗️ Workspace Flow

Pipeline → Agent → Workspace Created → Files Written → Build Completed → Workspace Reused

---

## 🧰 Prerequisites

- Lab 01 completed
- Lab 02 completed
- Lab 03 completed
- Jenkins controller running
- Agent connected

---

## 🚀 Step 1 — Create Workspace Test Pipeline

Create new pipeline:

lab04-workspace-test

Add:

```groovy
pipeline {
    agent { label 'docker' }

    stages {
        stage('Create File') {
            steps {
                sh 'echo Build Run > build.txt'
            }
        }

        stage('List Files') {
            steps {
                sh 'ls -l'
            }
        }
    }
}
```

---

## ▶️ Step 2 — Run Build

Click **Build Now**

Observe:

- File created
- Workspace used

---

## 🔍 Step 3 — Run Again

Trigger second build.

Notice:

- File already exists
- Workspace reused

---

## 🔥 Step 4 — Delete Workspace

Go to:

Node → Workspace

Delete workspace manually.

---

## ▶️ Step 5 — Run Build Again

Observe:

- Workspace recreated
- Build runs successfully

---

## 📊 Expected Behavior

- Workspace persists across builds
- Jenkins recreates workspace if missing

---

## 🧠 Deep Learning Notes

Workspace persistence can:

- Improve speed
- Cause flaky builds

Clean workspace ensures reproducibility.

---

## 🛠️ Failure Simulation

Modify pipeline:

```groovy
stage('Fail if Exists') {
    steps {
        sh 'test ! -f build.txt'
    }
}
```

Run build twice.

Observe failure.

---

## 🧑‍💻 Real Production Insights

Workspace issues can cause:

- Inconsistent builds
- Hidden dependencies
- Deployment failures

Best practice:

Clean workspace when needed.

---

## 🎓 Interview Talking Points

Be ready to explain:

- What is Jenkins workspace?
- Why builds fail due to dirty workspace?
- How to ensure build isolation?
- Workspace reuse vs cleanup tradeoff?

Strong answer:

“Workspace reuse improves speed but may introduce instability if not managed properly.”

---

## 🧩 Evidence To Add

- Workspace file screenshot
- Reuse behavior
- Recreated workspace

---

## 📌 Lessons Learned (Fill After Lab)

- …
- …
- …

---

## 🚀 Stretch Exercise

Try:

Add:

```groovy
cleanWs()
```

Observe clean build behavior.

---

## 🏁 Lab Completion Checklist

- [ ] Workspace reused
- [ ] Workspace deleted
- [ ] Workspace recreated
- [ ] Failure simulated

---

> Understanding workspace lifecycle helps prevent flaky pipelines.

