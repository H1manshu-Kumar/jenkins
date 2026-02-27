# 🧪 Lab 03 — Queue Bottleneck Simulation

> Understand how Jenkins schedules builds and what happens when executor capacity is exhausted.

---

## 🎯 Objective

In this lab, we will:

- Simulate executor shortage
- Observe Jenkins build queue behavior
- Understand scheduling delays
- Analyze how builds wait for resources
- Learn impact of limited agents/executors

This mirrors real-world CI environments where build demand exceeds capacity.

---

## 🧠 Why This Lab Matters

In production:

- Multiple pipelines trigger simultaneously
- Limited executors create bottlenecks
- Builds wait in queue
- Release timelines can get delayed

Understanding queue behavior helps in designing scalable CI systems.

---

## 🏗️ Execution Flow

Trigger Build → Jenkins Queue → Executor Availability → Agent → Execution

---

## 🧰 Prerequisites

- Lab 01 completed
- Lab 02 completed
- Jenkins controller running
- Agent connected

---

## 🚀 Step 1 — Limit Executors

Go to:

Manage Jenkins → Nodes → docker-agent → Configure

Set:

Executors = 1

Save.

This creates an artificial resource constraint.

---

## 🧪 Step 2 — Create Queue Test Pipeline

Create new pipeline:

lab03-queue-test

Add:

```groovy
pipeline {
    agent { label 'docker' }

    stages {
        stage('Simulate Load') {
            steps {
                sh 'sleep 60'
            }
        }
    }
}
```

---

## ▶️ Step 3 — Trigger Multiple Builds

Click **Build Now** 3–4 times quickly.

---

## 🔍 Step 4 — Observe Queue

Go to:

Build Queue

Notice:

- Only one build runs
- Others wait in queue

---

## 👀 Step 5 — Observe Scheduling

Watch:

- Queue length
- Executor usage
- Start time differences

---

## 📊 Expected Behavior

- First build runs immediately
- Remaining builds stay queued
- Each build starts only after previous finishes

---

## 🔥 Step 6 — Increase Executors

Change:

Executors = 2

Trigger builds again.

Observe:

- Parallel execution begins

---

## 🧠 Deep Learning Notes

Queue delay is caused by:

- Limited executors
- Busy agents
- Label constraints

Jenkins scheduling is resource-driven.

---

## 🛠️ Failure Simulation

Disconnect agent during queue wait.

Observe:

- Queue grows
- Builds do not start

Reconnect agent → builds resume.

---

## 🧑‍💻 Real Production Insights

Queue bottlenecks can cause:

- Delayed deployments
- CI slowdowns
- Release blockers

Scaling requires:

- More agents
- Auto-scaling
- Better workload distribution

---

## 🎓 Interview Talking Points

Be ready to explain:

- What causes Jenkins queue bottlenecks?
- How executors impact throughput?
- How to reduce build wait time?
- Difference between node vs executor scaling?

Strong answer:

“Executor availability determines build throughput; insufficient capacity causes queue delays.”

---

## 🧩 Evidence To Add

- Queue screenshot
- Parallel vs serial execution comparison
- Executor config screenshot

---

## 📌 Lessons Learned (Fill After Lab)

- …
- …
- …

---

## 🚀 Stretch Exercise

Try:

- Add second agent
- Run parallel builds across nodes

---

## 🏁 Lab Completion Checklist

- [ ] Executors limited
- [ ] Queue observed
- [ ] Parallel execution tested
- [ ] Failure simulation done

---

> Understanding build queues is key to designing scalable CI pipelines.

