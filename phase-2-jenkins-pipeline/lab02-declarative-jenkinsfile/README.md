# 🚀 Lab 02 -- Declarative Jenkinsfile (Pipeline as Code)

> Moving from UI-based pipelines to **Pipeline as Code using Jenkinsfile
> stored in GitHub**.

------------------------------------------------------------------------

## 📌 Lab Overview

This lab introduces **Jenkinsfile**, which allows you to define
pipelines as code and store them in version control.

You will: - Create a **Jenkinsfile** - Store it in GitHub - Configure
Jenkins to pull pipeline from SCM

------------------------------------------------------------------------

## 🎯 Objective

-   Understand Pipeline as Code\
-   Integrate Jenkins with GitHub\
-   Replace UI pipelines with Jenkinsfile

------------------------------------------------------------------------

## 🧠 Why This Matters

-   Industry standard → pipelines are **always stored in Git**
-   Enables **version control, collaboration, and rollback**
-   Critical for **real-world CI/CD systems**

------------------------------------------------------------------------

## 🏗️ Pipeline Flow

``` text
GitHub Repo (Jenkinsfile)
        ↓
Jenkins Pipeline Trigger
        ↓
Fetch Jenkinsfile
        ↓
Execute Stages (Build → Test → Deploy)
```

------------------------------------------------------------------------

## ⚙️ Step-by-Step Implementation

### Step 1 -- Create GitHub Repository

Example: - `jenkins-pipeline-demo`

------------------------------------------------------------------------

### Step 2 -- Add Jenkinsfile

Create a file named `Jenkinsfile` in repo:

``` groovy
pipeline {
    agent any

    stages {

        stage('Build') {
            steps {
                echo 'Building application...'
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying application...'
            }
        }

    }
}
```

------------------------------------------------------------------------

### Step 3 -- Configure Jenkins Job

-   Create Pipeline Job\
-   Select **Pipeline script from SCM**\
-   SCM: Git\
-   Add repo URL\
-   Script Path: `Jenkinsfile`

------------------------------------------------------------------------

### Step 4 -- Run Pipeline

-   Click **Build Now**
-   Observe:
    -   Stages executed from Jenkinsfile
    -   Logs pulled from SCM-based pipeline

------------------------------------------------------------------------

## 📸 Screenshots to Capture

-   GitHub repo with Jenkinsfile\
-   Jenkins SCM configuration\
-   Pipeline stage view\
-   Console output

------------------------------------------------------------------------

## 📊 Expected Output

``` text
Building application...
Running tests...
Deploying application...
```

------------------------------------------------------------------------

## 💡 Key Concepts Learned

-   Jenkinsfile enables Pipeline as Code\
-   Pipelines should be version-controlled\
-   Jenkins integrates with SCM (GitHub)\
-   Declarative syntax provides structure and readability

------------------------------------------------------------------------

## 🔥 Jenkinsfile vs UI Pipeline (Interview Gold)

  Feature           Jenkins UI   Jenkinsfile
  ----------------- ------------ ----------------------
  Version Control   ❌ No        ✅ Yes
  Collaboration     ❌ Hard      ✅ Easy
  Reusability       ❌ Limited   ✅ High
  Audit/History     ❌ No        ✅ Git History
  Best Practice     ❌ No        ✅ Industry Standard

------------------------------------------------------------------------

## 🔐 Best Practices

-   Always store Jenkinsfile in Git\
-   Keep pipeline simple and modular\
-   Use meaningful stage names\
-   Avoid hardcoding secrets

------------------------------------------------------------------------

## ❌ Common Mistakes

-   Writing pipelines only in Jenkins UI\
-   Not committing Jenkinsfile to repo\
-   Incorrect script path in Jenkins\
-   Not using version control

------------------------------------------------------------------------

## 🎯 Interview Questions

### Q1: What is Jenkinsfile?

A Jenkinsfile is a text file that defines the Jenkins pipeline and is
stored in version control.

------------------------------------------------------------------------

### Q2: Why Pipeline as Code?

-   Version control\
-   Reusability\
-   Easy collaboration\
-   Auditability

------------------------------------------------------------------------

### Q3: Difference between UI pipeline and Jenkinsfile?

Jenkinsfile is version-controlled and follows DevOps best practices,
while UI pipelines are not.

------------------------------------------------------------------------

## 🧩 Real DevOps Insight

In real projects:

``` text
Developer pushes code → Jenkins fetches Jenkinsfile → Pipeline executes automatically
```

This is the foundation of **CI/CD automation**.

------------------------------------------------------------------------

## 📝 Learning Points

-   Jenkinsfile is the standard way to define pipelines\
-   Pipeline as Code enables collaboration and versioning\
-   GitHub + Jenkins integration is core to CI/CD\
-   Declarative pipelines improve readability and maintenance

------------------------------------------------------------------------

## 🎯 Interview Takeaways

-   I can create and use Jenkinsfile for pipeline automation\
-   I understand why Pipeline as Code is important\
-   I can integrate Jenkins with GitHub repositories\
-   I know the difference between UI pipelines and Jenkinsfile\
-   I can explain real-world CI/CD pipeline flow

------------------------------------------------------------------------

## 🚀 Next Lab

➡️ Lab 03 -- Multi-Stage CI Pipeline

------------------------------------------------------------------------

🔥 *This is where Jenkins becomes a real CI/CD tool.*

