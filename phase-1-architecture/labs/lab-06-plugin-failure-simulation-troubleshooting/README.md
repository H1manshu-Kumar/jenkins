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

## 🚀 Step 1 - Install Plugin

Go to:

Manage Jenkins → Plugins → Available

Install:

- Distrubuted workspace Cleanup

Restart Jenkins if required.

---

## 🧪 Step 2 - Create new Plugin Pipeline
Create new pipeline:

lab06-plugin-failure-simulation

Add:

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

<img width="954" height="44" alt="image" src="https://github.com/user-attachments/assets/c74ecf3a-f998-417c-85d6-ab819d8131fd" />

---

## 🔍 Step 3 - Observe Behavior

Notice:

- Workspace cleaned
- Plugin functionality used
<img width="994" height="219" alt="image" src="https://github.com/user-attachments/assets/96e6ee80-3e94-4c13-9fc6-50ff8e2653b0" />

---

## 🔥 Step 4 - Disable Plugin

Go to:

Manage Jenkins → Plugins → Installed

Disable the plugin.    

<img width="961" height="126" alt="image" src="https://github.com/user-attachments/assets/b7145b9a-ffe7-44e4-86fd-3c5e5accfef8" />

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

## 📌 Lessons Learned

* Jenkins plugins extend core functionality.
* Pipelines may depend on plugin features.
* Disabling required plugins causes build failures.
* Plugin versions can impact compatibility.
* Outdated plugins may introduce instability.
* Missing plugins break pipeline execution.
* Plugin lifecycle must be managed carefully.
* Jenkins stability depends on plugin health.
* Troubleshooting often requires checking plugins.
* Controlled plugin usage improves CI reliability.

---

## 🏁 Lab Completion Checklist

- [x] Plugin installed
- [x] Pipeline tested
- [x] Plugin disabled
- [x] Failure observed

---

> Plugin management is essential for Jenkins stability.

---

## ✍️ Author

**[Himanshu Kumar](https://www.linkedin.com/in/h1manshu-kumar/)** - Learning by building, documenting, and sharing 🚀 

