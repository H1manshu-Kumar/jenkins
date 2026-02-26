# 🧪 Lab 02 - Pipeline Execution Lifecycle Deep Dive

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

## 🚀 Step 1 - Create Pipeline Job

Go to:

New Item → Pipeline

Name:

lab02-pipeline-lifecycle   

<img width="945" height="53" alt="image" src="https://github.com/user-attachments/assets/d87889a1-55c1-4e78-8f20-ddeb78540f84" />

---

## 🧪 Step 2 - Add Pipeline Script

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

<img width="866" height="444" alt="image" src="https://github.com/user-attachments/assets/a2a56230-b6c2-4f89-90d3-ebf16578b3ff" />

---

## ▶️ Step 3 - Run Build

Click:

Build Now

Observe:

- Stage view
- Console output
- Node assignment

<img width="779" height="431" alt="image" src="https://github.com/user-attachments/assets/1cbe6c0d-576c-43a0-9a3a-ec28052cdfe3" />   

<img width="783" height="636" alt="image" src="https://github.com/user-attachments/assets/634cf352-70b1-4932-af45-e14607ac338d" />

---

## 🔍 Step 4 - Observe Execution Details

Look at:

- Build queue
- Executor usage
- Pipeline visualization
- Console logs

Notice how Jenkins tracks state.

---

## 🔥 Step 5 - Simulate Controller Restart

While pipeline is in sleep stage:

Restart Jenkins container:

```bash
docker restart jenkins
```
<img width="355" height="46" alt="image" src="https://github.com/user-attachments/assets/33bab3b4-a34c-46c7-85d0-d1151b0cebb9" />   
<img width="1268" height="117" alt="image" src="https://github.com/user-attachments/assets/20cce013-747c-403d-b3eb-5914c08c850d" />    

Wait for Jenkins to come back.   

<img width="666" height="540" alt="image" src="https://github.com/user-attachments/assets/7e512c3f-077a-4686-a309-6035f4f431cb" />

---

## 👀 Step 6 - Observe Build After Restart

Open build.

You should see:

- Pipeline resumes
- Stage continues or restarts
- Logs preserved

This demonstrates pipeline durability.

---

## 🧪 Step 7 - Inspect Logs

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

   
<img width="638" height="453" alt="image" src="https://github.com/user-attachments/assets/fdaa5152-263c-4d23-809f-0fa9d3d4f06c" />

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

## 📦 Step 8 - Archive Artifact Test

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

<img width="385" height="320" alt="image" src="https://github.com/user-attachments/assets/a711d5af-e9ad-4c2e-b085-919bfb05356b" />

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

## 📌 Lessons Learned
- Jenkins pipelines are stateful workflows, not simple scripts.
- Build execution is coordinated by the controller but runs on agents.
- Pipeline state is persisted in Jenkins Home.
- Controller restart does not necessarily break running pipelines.
- CPS engine enables checkpointing and build resumption.
- Long-running stages must be designed with durability in mind.
- Logs are preserved across restarts and are critical for debugging.
- Artifact archiving stores outputs independently of runtime state.
- Freestyle jobs do not provide the same durability as pipelines.
- Understanding pipeline lifecycle helps diagnose CI instability issues.
---

## 🏁 Lab Completion Checklist

- [x] Pipeline created
- [x] Restart tested
- [x] Resumption observed
- [x] Logs inspected
- [x] Artifact archived

---

> Understanding pipeline lifecycle is essential for diagnosing real CI failures.

---
## ✍️ Author

**[Himanshu Kumar](https://www.linkedin.com/in/h1manshu-kumar/)** - Learning by building, documenting, and sharing 🚀

