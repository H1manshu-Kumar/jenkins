# 📦 Lab 05 - Artifact Management (Production Style - Nexus/S3 Simulation)

> Simulating real-world artifact storage in CI/CD pipelines using
> Jenkins.

------------------------------------------------------------------------

## 📌 Lab Overview

This lab focuses on **artifact management**, a core part of CI/CD pipelines.

Instead of just archiving artifacts in Jenkins, we simulate **production-style storage** like:

-   Nexus Repository
-   AWS S3
-   Artifact storage systems

------------------------------------------------------------------------

## 🎯 Objective

-   Understand artifact lifecycle in CI/CD\
-   Store and manage build outputs\
-   Simulate external artifact storage\
-   Make pipeline production-ready

------------------------------------------------------------------------

## 🧠 Why This Matters

In real systems:

-   Builds are NOT stored in Jenkins
-   Artifacts are stored in:
    -   Nexus
    -   Artifactory
    -   S3

This is heavily asked in **DevOps interviews**.

------------------------------------------------------------------------

## 🏗️ Pipeline Flow

``` text
Code → Build → Test → Package → Upload Artifact → Store → Deploy
```

------------------------------------------------------------------------

## ⚙️ Step-by-Step Implementation

### Step 1 - Generate Artifact

``` groovy
stage('Package') {
    steps {
        sh 'echo "Build artifact content" > build.txt'
    }
}
```

------------------------------------------------------------------------

### Step 2 - Archive in Jenkins

``` groovy
stage('Archive') {
    steps {
        archiveArtifacts artifacts: 'build.txt'
    }
}
```

------------------------------------------------------------------------

### Step 3 - Simulate S3 Upload

``` groovy
stage('Upload Artifact (Simulated S3)') {
    steps {
        sh '''
        mkdir -p /tmp/artifacts
        cp build.txt /tmp/artifacts/
        '''
    }
}
```

------------------------------------------------------------------------

### Step 4 - Version Artifact

``` groovy
stage('Version Artifact') {
    steps {
        sh 'cp build.txt build-${BUILD_NUMBER}.txt'
    }
}
```

------------------------------------------------------------------------

## 💡 Learning Points

-   Artifacts are build outputs\
-   Jenkins archive is temporary\
-   Real systems use external storage\
-   Versioning ensures traceability

------------------------------------------------------------------------

## 🎯 Interview Takeaways

-   I understand artifact lifecycle in CI/CD\
-   I can design pipelines with artifact storage\
-   I know real-world tools like Nexus/S3\
-   I understand why artifacts must be versioned

------------------------------------------------------------------------

## ✍️ Author

**[Himanshu Kumar](https://www.linkedin.com/in/h1manshu-kumar/)** - Learning by building, documenting, and sharing 🚀

------------------------------------------------------------------------

🔥 *Artifacts are the backbone of deployment pipelines.*

