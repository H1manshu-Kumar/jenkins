# 🚀 Lab 02 - Declarative Jenkinsfile (Pipeline as Code)

> Moving from UI-based pipelines to **Pipeline as Code using Jenkinsfile
> stored in GitHub**.

------------------------------------------------------------------------

## 📌 Lab Overview

This lab introduces **Jenkinsfile**, which allows you to define pipelines as code and store them in version control.

You will: - Create a **Jenkinsfile** - Store it in GitHub - Configure Jenkins to pull pipeline from SCM

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

### Step 1 - Create GitHub Repository

Example: - `jenkins-pipeline-demo`

------------------------------------------------------------------------

### Step 2 - Add Jenkinsfile

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

### Step 3 - Configure Jenkins Job

-   Create Pipeline Job\
-   Select **Pipeline script from SCM**\
-   SCM: Git\
-   Add repo URL\
-   Script Path: `Jenkinsfile`

<img width="870" height="515" alt="image" src="https://github.com/user-attachments/assets/bb8b96d4-6ab2-430e-a3c4-f4c922f1d5bf" />

<img width="870" height="141" alt="image" src="https://github.com/user-attachments/assets/57d292f6-377a-4fac-83c9-523386d81d3a" />

------------------------------------------------------------------------

### Step 4 - Run Pipeline

-   Click **Build Now**
-   Observe:
    -   Stages executed from Jenkinsfile
    -   Logs pulled from SCM-based pipeline
<img width="842" height="522" alt="image" src="https://github.com/user-attachments/assets/2ea8d55e-d92e-4c18-a747-a9c5008dc0cf" />

------------------------------------------------------------------------

## 📊 Expected Output

``` text
Building applicaiton...
Running Tests!!
Deploying Applicaiton!
```
<img width="992" height="613" alt="image" src="https://github.com/user-attachments/assets/413d0f95-b3a0-421b-97fd-1ccc1cfec27b" />
<img width="1012" height="593" alt="image" src="https://github.com/user-attachments/assets/8be997fc-2157-4eef-96b7-d9cfbe6b0717" />


------------------------------------------------------------------------

## 💡 Key Concepts Learned

-   Jenkinsfile enables Pipeline as Code\
-   Pipelines should be version-controlled\
-   Jenkins integrates with SCM (GitHub)\
-   Declarative syntax provides structure and readability

------------------------------------------------------------------------


## 🔥 Jenkinsfile vs UI Pipeline (Interview Gold)

|Feature |Jenkins UI |Jenkinsfile |
|---|---|---|
| Version Control | ❌ No | ✅ Yes |
| Collaboration | ❌ Hard | ✅ Easy |
| Reusability | ❌ Limited | ✅ High |
| Audit/History | ❌ No | ✅ Git History |
| Best Practice | ❌ No | ✅ Industry Standard |



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

## 🎯 Key Takeaways

-   I can create and use Jenkinsfile for pipeline automation\
-   I understand why Pipeline as Code is important\
-   I can integrate Jenkins with GitHub repositories\
-   I know the difference between UI pipelines and Jenkinsfile\
-   I can explain real-world CI/CD pipeline flow

------------------------------------------------------------------------

## 🚀 Next Lab

➡️ Lab 03 - Multi-Stage CI Pipeline

------------------------------------------------------------------------

## ✍️ Author

**[Himanshu Kumar](https://www.linkedin.com/in/h1manshu-kumar/)** - Learning by building, documenting, and sharing 🚀

------------------------------------------------------------------------

🔥 *This is where Jenkins becomes a real CI/CD tool.*

