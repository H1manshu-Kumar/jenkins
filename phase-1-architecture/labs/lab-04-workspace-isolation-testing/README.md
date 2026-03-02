# 🧪 Lab 04 - Workspace Behavior & Build Isolation

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

## 🚀 Step 1 - Create Workspace Test Pipeline

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
<img width="946" height="59" alt="image" src="https://github.com/user-attachments/assets/fba4dfbc-2477-4276-b78c-fa19352239c1" />

---

## ▶️ Step 2 - Run Build

Click **Build Now**

Observe:

- File created
- Workspace used
<img width="974" height="618" alt="image" src="https://github.com/user-attachments/assets/25bb4953-477f-45a3-a565-6f7a7560a654" />

---

## 🔍 Step 3 - Run Again

Trigger second build.

Notice:

- File already exists
- Workspace reused
<img width="974" height="618" alt="image" src="https://github.com/user-attachments/assets/d528a435-0908-4af2-8b47-2c94e9bd9c30" />

---

## 🔥 Step 4 - Delete Workspace

Go to:

Node → Workspace

Delete workspace manually.

---

## ▶️ Step 5 - Run Build Again

Observe:

- Workspace recreated
- Build runs successfully
<img width="974" height="618" alt="image" src="https://github.com/user-attachments/assets/78f04819-3202-4254-a3fa-8b80097b0980" />

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
<img width="974" height="580" alt="image" src="https://github.com/user-attachments/assets/5f088b9d-220c-47eb-9964-6e584ab362af" />   
<img width="983" height="681" alt="image" src="https://github.com/user-attachments/assets/465e3748-7467-4860-89af-89b31e92d08a" />


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

## 📌 Lessons Learned

* Jenkins reuses workspace across builds by default.
* Persistent workspace can introduce hidden dependencies.
* Dirty workspace may cause unpredictable build failures.
* Deleting workspace forces clean execution.
* Jenkins automatically recreates missing workspace.
* Build reproducibility improves with clean environments.
* Workspace reuse improves speed but risks stability.
* Manual or automated cleanup ensures isolation.
* Flaky pipelines are often caused by leftover files.
* Proper workspace management enhances CI reliability.

---

## 🏁 Lab Completion Checklist

- [x] Workspace reused
- [x] Workspace deleted
- [x] Workspace recreated
- [x] Failure simulated

---

> Understanding workspace lifecycle helps prevent flaky pipelines.

---

## ✍️ Author

**[Himanshu Kumar](https://www.linkedin.com/in/h1manshu-kumar/)** - Learning by building, documenting, and sharing 🚀
