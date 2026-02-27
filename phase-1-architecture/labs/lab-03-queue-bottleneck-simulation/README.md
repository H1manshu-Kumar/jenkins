# 🧪 Lab 03 - Queue Bottleneck Simulation

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

## 🚀 Step 1 - Limit Executors

Go to:

Manage Jenkins → Nodes → docker-agent → Configure

Set:

Executors = 1

Save.

This creates an artificial resource constraint.   

<img width="952" height="439" alt="image" src="https://github.com/user-attachments/assets/bc4bf34b-f8d6-4ed6-925e-a52ffe102178" />

---

## 🧪 Step 2 - Create Queue Test Pipeline

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
<img width="930" height="51" alt="image" src="https://github.com/user-attachments/assets/11db8b12-3195-41f5-9b04-15557210dfc3" />

---

## ▶️ Step 3 - Trigger Multiple Builds

Click **Build Now** 3-4 times quickly.   

<img width="703" height="637" alt="image" src="https://github.com/user-attachments/assets/3db893c0-402a-479c-b167-2f54ebca1ecb" />

---

## 🔍 Step 4 - Observe Queue

Go to:

Build Queue

Notice:

- Only one build runs
- Others wait in queue


<img width="703" height="637" alt="image" src="https://github.com/user-attachments/assets/3db893c0-402a-479c-b167-2f54ebca1ecb" />

---

## 👀 Step 5 - Observe Scheduling

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

## 🔥 Step 6 - Increase Executors

Change:

Executors = 2

Trigger builds again.

Observe:

- Parallel execution begins


<img width="1171" height="422" alt="image" src="https://github.com/user-attachments/assets/da21c165-922c-4d8b-acc5-c95486c1de90" />
</br>
<img width="1166" height="638" alt="image" src="https://github.com/user-attachments/assets/80b70a69-b0ff-4c26-bdb5-0313eb7eb446" />


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

## 📌 Lessons Learned
- Executor availability directly impacts build throughput.
- Limited executors create build queue delays.
- Jenkins schedules builds based on resource availability.
- Increasing executors enables parallel execution.
- Queue growth indicates capacity bottlenecks.
- Label constraints can delay build scheduling.
- Agent availability affects queue clearance.
- Scaling executors improves performance but requires resource balance.
- Queue behavior helps identify CI infrastructure limitations.
- Proper capacity planning prevents pipeline slowdowns.

---

## 🏁 Lab Completion Checklist

- [x] Executors limited
- [x] Queue observed
- [x] Parallel execution tested
- [x] Failure simulation done

---

## ✍️ Author

**[Himanshu Kumar](https://www.linkedin.com/in/h1manshu-kumar/)** - Learning by building, documenting, and sharing 🚀

