# 🚀 Lab 01 - First Jenkins Pipeline

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

<img width="1000" height="312" alt="image" src="https://github.com/user-attachments/assets/1b6cb552-5027-489a-8939-d488982f04a8" />

------------------------------------------------------------------------

### 2. Add Pipeline Script

-   Scroll to **Pipeline section**\
-   Select: *Pipeline script*\
-   Paste the Jenkinsfile script
<img width="1280" height="489" alt="image" src="https://github.com/user-attachments/assets/0433ee42-696e-48ea-b954-f9b33131267c" />

------------------------------------------------------------------------

### 3. Build the Pipeline

-   Click **Build Now**\
-   Observe execution
<img width="1280" height="489" alt="image" src="https://github.com/user-attachments/assets/b274655f-0656-40a0-9731-055616494ae8" />

<img width="1280" height="434" alt="image" src="https://github.com/user-attachments/assets/78eec880-7f0f-4926-8e9f-05028e2b9f55" />

------------------------------------------------------------------------

## 📊 Expected Output

Console log should show:

    Hello from Jenkins Pipeline

<img width="983" height="347" alt="image" src="https://github.com/user-attachments/assets/92dc58b1-ecdf-41e3-adb8-500354ee259f" /> </br>

Stage View:

    Hello ✔   
    
<img width="665" height="550" alt="image" src="https://github.com/user-attachments/assets/02d05a6b-e213-4af6-9538-13015cd38dfc" />

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
## 📌 Lessons Learned

- Jenkins Pipeline automates CI/CD workflows using code
- Declarative pipeline provides structured and readable syntax
- A pipeline is divided into stages and steps for execution clarity
- `agent any` allows execution on any available Jenkins node
- Console logs are essential for debugging pipeline failures
- Even a simple pipeline follows the same structure as real CI/CD systems

------------------------------------------------------------------------

## 🎯 Key Takeaways

- I understand how to create and run a Jenkins Pipeline job
- I can explain the structure of a declarative pipeline (agent, stages, steps)
- I know how pipeline execution is visualized using Stage View and logs
- I can debug basic pipeline issues using console output
- I understand how this simple pipeline scales into real CI/CD workflows

------------------------------------------------------------------------

## 📈 Next Step

➡️ Move to **Lab 02 - Declarative Jenkinsfile**

-   Store pipeline in Git\
-   Introduce real CI/CD workflow

------------------------------------------------------------------------

## ✍️ Author

**[Himanshu Kumar](https://www.linkedin.com/in/h1manshu-kumar/)** - Learning by building, documenting, and sharing 🚀

------------------------------------------------------------------------

## ⭐ Summary

This lab establishes the **foundation of Jenkins Pipelines**, which is
critical for building real CI/CD workflows in DevOps.

------------------------------------------------------------------------

🔥 *First step from manual jobs to automated pipelines.*


