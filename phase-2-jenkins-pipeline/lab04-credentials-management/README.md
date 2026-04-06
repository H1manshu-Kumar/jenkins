# 🔐 Lab 04 - Jenkins Credentials & Secure Pipelines

> Implementing secure CI/CD pipelines using Jenkins Credentials Store
> (no hardcoded secrets).

------------------------------------------------------------------------

## 📌 Lab Overview

This lab focuses on **secure secret management in Jenkins pipelines**, a critical DevOps practice.

You will: - Store secrets in Jenkins Credentials - Access them securely in pipeline - Avoid hardcoding sensitive data

------------------------------------------------------------------------

## 🎯 Objective

-   Understand Jenkins Credentials Store\
-   Secure pipelines using `withCredentials`\
-   Follow DevOps security best practices

------------------------------------------------------------------------

## 🧠 Why This Matters

-   Hardcoding secrets = **security risk**
-   Real pipelines use:
    -   API tokens
    -   Git credentials
    -   Docker registry credentials
-   Frequently asked in **DevOps interviews**

------------------------------------------------------------------------

## 🏗️ Secure Pipeline Flow

``` text
Credentials Store
        ↓
Jenkins Pipeline
        ↓
Inject Secret (env variable)
        ↓
Use Securely in Steps
```

------------------------------------------------------------------------

## ⚙️ Step-by-Step Implementation

### Step 1 - Add Credentials in Jenkins

-   Manage Jenkins → Credentials\
-   Global → Add Credentials

Types: - Secret Text (API key) - Username/Password - SSH Key

Example: - ID: `my-secret` - Type: Secret Text

<img width="1003" height="463" alt="image" src="https://github.com/user-attachments/assets/44a26b8e-c66e-46bc-9621-f9cc515b0868" />

------------------------------------------------------------------------

### Step 2 - Jenkinsfile (Secure Pipeline)

``` groovy
pipeline {

    agent any

    stages {

        stage('Use Secret') {
            steps {
                withCredentials([string(credentialsId: 'my-secret', variable: 'SECRET')]) {
                    sh 'echo "Using secret safely"'
                }
            }
        }

        stage('Simulate Secure API Call') {
            steps {
                withCredentials([string(credentialsId: 'my-secret', variable: 'SECRET')]) {
                    sh 'echo "Calling API with token (masked)"'
                }
            }
        }
    }
}
```

------------------------------------------------------------------------

## 💡 Key Concepts Learned

-   Jenkins Credentials Store centralizes secrets\
-   `withCredentials` injects secrets securely\
-   Secrets should never be printed in logs\
-   Pipelines must avoid hardcoded credentials

------------------------------------------------------------------------

## 🔐 Best Practices

-   Use least privilege credentials\
-   Rotate secrets regularly\
-   Avoid exposing secrets in logs\
-   Use environment variables via Jenkins

------------------------------------------------------------------------

## ❌ Common Mistakes

-   Hardcoding passwords in Jenkinsfile\
-   Printing secrets in logs\
-   Using wrong credentials ID\
-   Not masking sensitive data

------------------------------------------------------------------------

## 🧩 Real DevOps Insight

In production:

``` text
Jenkins → Credentials Store → Secure API / Docker / Git Access
```

All secrets are **externalized and secured**.

------------------------------------------------------------------------

## 📝 Learning Points

-   Secure pipelines are mandatory in DevOps\
-   Jenkins Credentials Store prevents secret leakage\
-   Pipelines must never expose sensitive data\
-   Secrets are injected dynamically at runtime

------------------------------------------------------------------------

## 🎯 Interview Takeaways

-   I can securely manage secrets in Jenkins pipelines\
-   I understand how to use `withCredentials`\
-   I know why secret management is critical in CI/CD\
-   I can design secure pipelines following best practices

------------------------------------------------------------------------

## 🚀 Next Lab

➡️ Lab 05 - Artifact Management (real artifact storage)

------------------------------------------------------------------------

## ✍️ Author

**[Himanshu Kumar](https://www.linkedin.com/in/h1manshu-kumar/)** - Learning by building, documenting, and sharing 🚀

------------------------------------------------------------------------

🔥 *Secure pipelines are a must-have skill for every DevOps engineer.*
