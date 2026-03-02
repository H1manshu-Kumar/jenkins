# 🧪 Lab 06 - Plugin Failure Simulation

> Learn how Jenkins plugins can impact stability and how to troubleshoot failures caused by them.

---

## 🎯 Objective

In this lab, we will:

- Install a new plugin
- Observe its impact
- Simulate pipeline failure
- Troubleshoot plugin-related issues
- Understand plugin dependency risks

This mirrors real CI environments where plugins are a major source of instability.

---

## 🧠 Why This Lab Matters

In production:

- Plugins extend Jenkins functionality
- Poor plugin management causes failures
- Version conflicts break pipelines

Understanding plugin behavior is critical for CI reliability.

---

## 🏗️ Plugin Flow

Plugin Installed → Pipeline Uses Feature → Conflict Occurs → Build Fails

---

## 🧰 Prerequisites

- Lab 01 to 05 completed
- Jenkins controller running
- Agent connected

---

## 🚀 Step 1 — Install Plugin

Go to:

Manage Jenkins → Plugins → Available

Install:

- Workspace Cleanup Plugin

Restart Jenkins if required.

---

## 🧪 Step 2 — Modify Pipeline

Update pipeline:

```groovy
pipeline {
    agent { label 'docker' }

    stages {
        stage('Cleanup') {
            steps {
                cleanWs()
            }
        }
    }
}
```

Run build.

---

## 🔍 Step 3 — Observe Behavior

Notice:

- Workspace cleaned
- Plugin functionality used

---

## 🔥 Step 4 — Disable Plugin

Go to:

Manage Jenkins → Plugins → Installed

Disable the plugin.

Run pipeline again.

Observe:

Pipeline fails.

---

## 📊 Expected Behavior

- Pipeline works with plugin
- Pipeline fails without plugin

---

## 🧠 Deep Learning Notes

Plugins:

- Extend Jenkins core
- Can introduce failures
- Require lifecycle management

---

## 🛠️ Failure Simulation

Install outdated plugin version.

Observe compatibility issues.

---

## 🧑‍💻 Real Production Insights

Plugin issues can cause:

- Build failures
- Security risks
- System instability

Best practice:

Manage plugin versions carefully.

---

## 🎓 Interview Talking Points

Be ready to explain:

- Why plugins cause instability?
- How to troubleshoot plugin failures?
- Plugin dependency risks?

Strong answer:

“Plugins extend Jenkins but must be managed carefully to avoid compatibility issues.”

---

## 🧩 Evidence To Add

- Plugin install screenshot
- Failure logs
- Pipeline success vs failure

---

## 📌 Lessons Learned (Fill After Lab)

- …
- …
- …

---

## 🚀 Stretch Exercise

Try:

Install conflicting plugin.

---

## 🏁 Lab Completion Checklist

- [ ] Plugin installed
- [ ] Pipeline tested
- [ ] Plugin disabled
- [ ] Failure observed

---

> Plugin management is essential for Jenkins stability.

