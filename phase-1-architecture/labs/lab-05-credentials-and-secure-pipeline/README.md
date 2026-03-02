# 🧪 Lab 05 - Credentials & Secure Pipelines

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

## 🚀 Step 1 - Add Credential

Go to:

Manage Jenkins → Credentials → Global → Add Credentials

Add:

- Kind: Secret Text
- ID: demo-secret
- Secret: super-secret-value

Save.   

<img width="1153" height="161" alt="image" src="https://github.com/user-attachments/assets/638e39c7-c200-45d9-a0cc-b3e6e8828976" />

---

## 🧪 Step 2 - Create Secure Pipeline

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
<img width="961" height="42" alt="image" src="https://github.com/user-attachments/assets/5886646a-fd1b-4d79-a4a1-dcf621a6c694" />

---

## ▶️ Step 3 - Run Build

Click **Build Now**

Observe:

- Secret not printed
- Logs remain masked
  
<img width="979" height="461" alt="image" src="https://github.com/user-attachments/assets/bb3f5c60-66fe-4a65-ad72-072efd0f28c1" />

---

## 🔍 Step 4 - Attempt Unsafe Usage

Modify pipeline:

```groovy
sh 'echo $SECRET'
```

Run build.

Observe:

Secret is masked.   

<img width="979" height="513" alt="image" src="https://github.com/user-attachments/assets/dd08910a-3477-4ffa-9f2a-c1a234ddfb2c" />

---

## 🔥 Step 5 - Hardcode Secret (Anti-pattern)

Test:

```groovy
sh 'echo Secret in plain text format'
```

Observe:

Not masked - insecure.   

<img width="976" height="633" alt="image" src="https://github.com/user-attachments/assets/3cb31f0c-fbea-464b-b75e-ab44ea41124e" />

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

<img width="992" height="313" alt="image" src="https://github.com/user-attachments/assets/83333f21-5802-493f-b200-845218b7f7b5" />
</br>

<img width="976" height="371" alt="image" src="https://github.com/user-attachments/assets/7e388281-a8a8-491a-adeb-87690e1bcb93" />

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

## 📌 Lessons Learned 

* Jenkins securely stores credentials in encrypted form.
* Secrets should never be hardcoded in pipelines.
* Credentials are injected only during runtime.
* Masking prevents secret exposure in logs.
* Hardcoded values are not protected by masking.
* Incorrect credential IDs cause pipeline failures.
* Secure injection improves pipeline safety.
* Secrets are not stored in workspace by default.
* Dynamic secret usage reduces security risks.
* Proper credential management protects CI infrastructure.


---

## 🏁 Lab Completion Checklist

- [x] Credential added
- [x] Secret injected
- [x] Masking verified
- [x] Hardcoding tested

---

> Secure pipelines are essential for protecting infrastructure.

---

## ✍️ Author

**[Himanshu Kumar](https://www.linkedin.com/in/h1manshu-kumar/)** - Learning by building, documenting, and sharing 🚀
