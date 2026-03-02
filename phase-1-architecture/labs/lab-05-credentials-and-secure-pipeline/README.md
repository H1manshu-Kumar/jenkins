# 🧪 Lab 05 — Credentials & Secure Pipelines

> Learn how Jenkins securely manages secrets and how to prevent sensitive data exposure in pipelines.

---

## 🎯 Objective

In this lab, we will:

- Store credentials securely in Jenkins
- Inject secrets into pipelines
- Mask sensitive data in logs
- Avoid hardcoding secrets
- Understand secure pipeline design

This mirrors real CI environments where secure secret handling is critical.

---

## 🧠 Why This Lab Matters

In production:

- Hardcoded secrets create major security risks
- Leaked credentials can compromise systems
- Secure injection is mandatory

Proper secret management is a core DevOps responsibility.

---

## 🏗️ Secret Flow

Jenkins Credentials Store → Pipeline → Secure Injection → Masked Logs

---

## 🧰 Prerequisites

- Lab 01 to 04 completed
- Jenkins controller running
- Agent connected

---

## 🚀 Step 1 — Add Credential

Go to:

Manage Jenkins → Credentials → Global → Add Credentials

Add:

- Kind: Secret Text
- ID: demo-secret
- Secret: super-secret-value

Save.

---

## 🧪 Step 2 — Create Secure Pipeline

Create new pipeline:

lab05-secure-pipeline

Add:

```groovy
pipeline {
    agent { label 'docker' }

    stages {
        stage('Inject Secret') {
            steps {
                withCredentials([string(credentialsId: 'demo-secret', variable: 'SECRET')]) {
                    sh 'echo Using secret'
                }
            }
        }
    }
}
```

---

## ▶️ Step 3 — Run Build

Click **Build Now**

Observe:

- Secret not printed
- Logs remain masked

---

## 🔍 Step 4 — Attempt Unsafe Usage

Modify pipeline:

```groovy
sh 'echo $SECRET'
```

Run build.

Observe:

Secret is masked.

---

## 🔥 Step 5 — Hardcode Secret (Anti-pattern)

Test:

```groovy
sh 'echo super-secret-value'
```

Observe:

Not masked — insecure.

---

## 📊 Expected Behavior

- Injected secrets masked
- Hardcoded values visible

---

## 🧠 Deep Learning Notes

Credentials:

- Stored encrypted
- Injected temporarily
- Not persisted in workspace

---

## 🛠️ Failure Simulation

Use wrong credential ID.

Observe:

Pipeline fails.

---

## 🧑‍💻 Real Production Insights

Secrets should:

- Never be hardcoded
- Be injected dynamically
- Be rotated periodically

---

## 🎓 Interview Talking Points

Be ready to explain:

- How Jenkins manages secrets?
- Why hardcoding is dangerous?
- How masking works?
- Secret lifecycle in pipelines?

Strong answer:

“Jenkins credentials are securely stored and injected at runtime, preventing exposure in code.”

---

## 🧩 Evidence To Add

- Credential config screenshot
- Masked logs
- Pipeline run

---

## 📌 Lessons Learned (Fill After Lab)

- …
- …
- …

---

## 🚀 Stretch Exercise

Try:

Use Username/Password credential.

---

## 🏁 Lab Completion Checklist

- [ ] Credential added
- [ ] Secret injected
- [ ] Masking verified
- [ ] Hardcoding tested

---

> Secure pipelines are essential for protecting infrastructure.

