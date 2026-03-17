# 🚀 Lab 01 -- First Jenkins Pipeline

> Hands-on implementation of a basic Jenkins Pipeline to understand
> pipeline fundamentals.

------------------------------------------------------------------------

## 📌 Objective

-   Create your first Jenkins Pipeline job\
-   Understand **stages, steps, and pipeline execution flow**\
-   Get familiar with Jenkins Pipeline UI and logs

------------------------------------------------------------------------

## 🧠 Why This Lab Matters

This is your **entry point into CI/CD pipelines**.

-   Moves from freestyle jobs → pipelines\
-   Introduces **Pipeline as Code concept**\
-   Foundation for all advanced DevOps pipelines

------------------------------------------------------------------------

## 🏗️ What We Are Building

A simple pipeline with one stage:

``` text
Start → Hello Stage → End
```

------------------------------------------------------------------------

## ⚙️ Jenkins Pipeline Script

``` groovy
pipeline {
    agent any

    stages {
        stage('Hello') {
            steps {
                echo 'Hello from Jenkins Pipeline'
            }
        }
    }
}
```

------------------------------------------------------------------------

## 🔧 Step-by-Step Implementation

### 1. Create Pipeline Job

-   Go to Jenkins Dashboard\
-   Click **New Item**\
-   Enter name: `first-pipeline`\
-   Select **Pipeline**\
-   Click OK

------------------------------------------------------------------------

### 2. Add Pipeline Script

-   Scroll to **Pipeline section**\
-   Select: *Pipeline script*\
-   Paste the Jenkinsfile script

------------------------------------------------------------------------

### 3. Build the Pipeline

-   Click **Build Now**\
-   Observe execution

------------------------------------------------------------------------

## 📸 Screenshots to Capture

Add these inside `screenshots/` folder:

-   Pipeline job configuration\
-   Build execution\
-   Stage view\
-   Console output

------------------------------------------------------------------------

## 📊 Expected Output

Console log should show:

    Hello from Jenkins Pipeline

Stage View:

    Hello ✔

------------------------------------------------------------------------

## 🔍 Key Concepts Learned

-   Jenkins Pipeline basics\
-   `pipeline`, `agent`, `stages`, `steps`\
-   Stage execution flow\
-   Pipeline visualization

------------------------------------------------------------------------

## ⚠️ Common Mistakes

-   Using freestyle job instead of pipeline\
-   Syntax errors in pipeline script\
-   Not saving job before build

------------------------------------------------------------------------

## 💡 DevOps Insight

In real projects:

-   Each stage represents a **CI/CD step**\
-   Example: Build → Test → Deploy\
-   Pipelines replace manual build processes

------------------------------------------------------------------------

## 🎯 Interview Questions

**Q1: What is a Jenkins Pipeline?**\
A pipeline is a set of automated steps defined as code to build, test,
and deploy applications.

**Q2: What are stages in Jenkins?**\
Stages divide the pipeline into logical steps like build, test, and
deploy.

**Q3: What is agent in Jenkins Pipeline?**\
Agent defines where the pipeline will run (e.g., any available node).

------------------------------------------------------------------------

## 📈 Next Step

➡️ Move to **Lab 02 -- Declarative Jenkinsfile**

-   Store pipeline in Git\
-   Introduce real CI/CD workflow

------------------------------------------------------------------------

## ⭐ Summary

This lab establishes the **foundation of Jenkins Pipelines**, which is
critical for building real CI/CD workflows in DevOps.

------------------------------------------------------------------------

🔥 *First step from manual jobs to automated pipelines.*

