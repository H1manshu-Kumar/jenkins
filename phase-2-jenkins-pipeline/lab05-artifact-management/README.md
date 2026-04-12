# 📦 Lab 05 - Production-Grade Artifact Management with Jenkins & AWS S3

> Real-world CI/CD pipeline implementing artifact storage, versioning, and AWS S3 integration for enterprise deployments.

---

## 🎯 Project Overview

This lab demonstrates **production-grade artifact management** in a Jenkins CI/CD pipeline, simulating how enterprises handle build artifacts in real-world scenarios. Instead of storing artifacts locally in Jenkins, we implement external storage using **AWS S3** - a common practice in DevOps.

**Key Achievement**: Successfully built, tested, packaged, and deployed versioned artifacts to AWS S3 with automated CI/CD pipeline.

---

## 🏗️ Architecture & Pipeline Flow

```
┌─────────────┐    ┌──────────┐    ┌──────────┐    ┌─────────┐    ┌──────────┐    ┌─────────┐
│  Checkout   │ -> │  Setup   │ -> │   Lint   │ -> │  Test   │ -> │  Build   │ -> │ Archive │
└─────────────┘    └──────────┘    └──────────┘    └─────────┘    └──────────┘    └─────────┘
                                                                                          │
                                                                                          v
                                                                                    ┌──────────┐
                                                                                    │ Upload   │
                                                                                    │ to S3    │
                                                                                    └──────────┘
```

---

## 🚀 Technologies & Tools

| Technology | Purpose |
|------------|---------|
| **Jenkins** | CI/CD Orchestration |
| **AWS S3** | Artifact Storage |
| **AWS IAM** | Access Management |
| **Python 3** | Application Runtime |
| **pytest** | Unit Testing |
| **flake8** | Code Linting |
| **Docker** | Jenkins Agent |

---

## 📋 Prerequisites

- Jenkins server with Docker agent
- AWS Account with S3 bucket
- IAM user with S3 permissions
- Jenkins credentials configured:
  - `aws-access-key-id`
  - `aws-secret-access-key`

---

## 🔧 Pipeline Implementation

### 1️⃣ Environment Configuration

```groovy
environment {
    AWS_ACCESS_KEY_ID     = credentials('aws-access-key-id')
    AWS_SECRET_ACCESS_KEY = credentials('aws-secret-access-key')
    AWS_DEFAULT_REGION    = 'ap-south-1'
    S3_BUCKET             = 'jenkins-artifacts-devops1'
    APP_VERSION           = "1.0.${BUILD_NUMBER}"
}
```

**Screenshot Placeholder:**
![Environment Variables Configuration](./screenshots/01-environment-config.png)

---

### 2️⃣ Code Checkout

```groovy
stage('Checkout') {
    steps {
        checkout scm
    }
}
```

Pulls the latest code from the Git repository.

---

### 3️⃣ Python Environment Setup

```groovy
stage('Setup') {
    steps {
        dir("${WORKSPACE}/phase-2-jenkins-pipeline/devpulse") {
            sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
            '''
        }
    }
}
```

Creates isolated Python virtual environment and installs dependencies.

**Screenshot Placeholder:**
![Setup Stage Execution](./screenshots/02-setup-stage.png)

---

### 4️⃣ Code Quality - Linting

```groovy
stage('Lint') {
    steps {
        dir("${WORKSPACE}/phase-2-jenkins-pipeline/devpulse") {
            sh '''
                . venv/bin/activate
                flake8 *.py --max-line-length=100
            '''
        }
    }
}
```

Ensures code quality and adherence to Python PEP8 standards.

**Screenshot Placeholder:**
![Lint Stage Results](./screenshots/03-lint-stage.png)

---

### 5️⃣ Automated Testing

```groovy
stage('Test') {
    steps {
        dir("${WORKSPACE}/phase-2-jenkins-pipeline/devpulse") {
            sh '''
                . venv/bin/activate
                mkdir -p reports
                pytest tests/ \
                    --junitxml=reports/junit.xml \
                    --cov=. \
                    --cov-report=xml:reports/coverage.xml \
                    -v
            '''
        }
    }
    post {
        always {
            junit allowEmptyResults: true, testResults: "${WORKSPACE}/phase-2-jenkins-pipeline/devpulse/reports/junit.xml"
        }
    }
}
```

Runs unit tests with coverage reporting and publishes results to Jenkins.

**Screenshot Placeholder:**
![Test Results Dashboard](./screenshots/04-test-results.png)

---

### 6️⃣ Artifact Building

```groovy
stage('Build') {
    steps {
        dir("${WORKSPACE}/phase-2-jenkins-pipeline/devpulse") {
            sh '''
                . venv/bin/activate
                mkdir -p dist
                tar -czf dist/devpulse-${BUILD_NUMBER}.tar.gz *.py templates/ static/ requirements.txt
            '''
        }
    }
}
```

Creates versioned tarball artifact containing application code and dependencies.

**Screenshot Placeholder:**
![Build Artifact Creation](./screenshots/05-build-stage.png)

---

### 7️⃣ Jenkins Artifact Archiving

```groovy
stage('Archive') {
    steps {
        dir("${WORKSPACE}/phase-2-jenkins-pipeline/devpulse") {
            script {
                if (fileExists('dist')) {
                    archiveArtifacts artifacts: 'dist/**', allowEmptyArchive: true
                }
            }
        }
    }
}
```

Archives artifacts in Jenkins for quick access and download.

**Screenshot Placeholder:**
![Archived Artifacts in Jenkins](./screenshots/06-archive-stage.png)

---

### 8️⃣ AWS S3 Upload (Production Storage)

```groovy
stage('Upload to S3') {
    steps {
        dir("${WORKSPACE}/phase-2-jenkins-pipeline/devpulse") {
            sh '''
                echo "Uploading artifacts for version ${APP_VERSION}"
                
                if ! command -v aws &> /dev/null; then
                    echo "AWS CLI not found, installing..."
                    . venv/bin/activate
                    pip install awscli
                fi

                aws s3 cp dist/ s3://${S3_BUCKET}/devpulse/${APP_VERSION}/ \
                    --recursive \
                    --no-progress

                echo "Upload complete. Verifying..."

                aws s3 ls s3://${S3_BUCKET}/devpulse/${APP_VERSION}/
            '''
        }
    }
}
```

Uploads versioned artifacts to AWS S3 for long-term storage and distribution.

**Screenshot Placeholder:**
![S3 Upload Success](./screenshots/07-s3-upload.png)

---

### 9️⃣ Post-Build Actions

```groovy
post {
    always {
        cleanWs()
    }
    success {
        echo "Pipeline succeeded. Artifacts at s3://${S3_BUCKET}/devpulse/${APP_VERSION}/"
    }
    failure {
        echo "Pipeline failed. Check logs above."
    }
}
```

Cleans workspace and provides build status notifications.

---

## 🔐 AWS IAM Configuration

### Required IAM Policy

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:PutObject",
        "s3:GetObject",
        "s3:ListBucket"
      ],
      "Resource": [
        "arn:aws:s3:::jenkins-artifacts-devops1/*",
        "arn:aws:s3:::jenkins-artifacts-devops1"
      ]
    }
  ]
}
```

**Screenshot Placeholder:**
![IAM Policy Configuration](./screenshots/08-iam-policy.png)

---

## 📊 Pipeline Execution Results

**Screenshot Placeholder:**
![Complete Pipeline Success](./screenshots/09-pipeline-success.png)

**Screenshot Placeholder:**
![S3 Bucket with Versioned Artifacts](./screenshots/10-s3-bucket-artifacts.png)

---

## 🎓 Key Learnings & Best Practices

### ✅ What I Implemented

1. **Artifact Versioning**: Used `BUILD_NUMBER` for unique artifact versions
2. **External Storage**: Integrated AWS S3 for production-grade artifact management
3. **Security**: Implemented IAM policies with least privilege access
4. **Testing Integration**: Automated test execution with JUnit reporting
5. **Code Quality**: Enforced linting standards with flake8
6. **Clean Architecture**: Proper workspace management and cleanup

### 🏢 Production Considerations

- **Artifacts are NOT stored permanently in Jenkins** - Jenkins is for orchestration, not storage
- **External artifact repositories** (S3, Nexus, Artifactory) are industry standard
- **Versioning is critical** for rollback capabilities and traceability
- **IAM security** ensures controlled access to artifacts
- **Automated testing** validates artifacts before deployment

---

## 🎯 Interview Talking Points

> "I implemented a production-grade CI/CD pipeline with Jenkins that automates the entire build lifecycle - from code checkout to artifact storage in AWS S3. The pipeline includes automated testing with pytest, code quality checks with flake8, and versioned artifact management. I configured IAM policies for secure S3 access and implemented proper error handling throughout the pipeline stages."

**Key Highlights:**
- ✅ End-to-end CI/CD automation
- ✅ AWS S3 integration for artifact storage
- ✅ IAM security implementation
- ✅ Automated testing and code quality gates
- ✅ Artifact versioning and traceability
- ✅ Production-ready pipeline design

---

## 🐛 Troubleshooting Guide

### Common Issues & Solutions

| Issue | Solution |
|-------|----------|
| `ModuleNotFoundError: No module named 'devpulse'` | Fixed imports in test files to use relative imports |
| `AccessDenied` on S3 upload | Added IAM policy with `s3:PutObject` permission |
| `externally-managed-environment` pip error | Installed AWS CLI inside virtual environment |
| Test reports not found | Added `allowEmptyResults: true` to junit step |
| Flake8 blank line error | Removed trailing newlines from `__init__.py` |

---

## 📁 Project Structure

```
lab05-artifact-management/
├── Jenkinsfile                 # Pipeline definition
├── README.md                   # This file
└── screenshots/                # Pipeline execution screenshots
    ├── 01-environment-config.png
    ├── 02-setup-stage.png
    ├── 03-lint-stage.png
    ├── 04-test-results.png
    ├── 05-build-stage.png
    ├── 06-archive-stage.png
    ├── 07-s3-upload.png
    ├── 08-iam-policy.png
    ├── 09-pipeline-success.png
    └── 10-s3-bucket-artifacts.png
```

---

## 🔗 Related Labs

- **Lab 04**: Testing & Quality Gates
- **Lab 06**: Docker Integration
- **Lab 07**: Deployment Automation

---

## 📝 Dependencies

```txt
Flask==3.0.0
pytest==7.4.3
pytest-cov
flake8==6.1.0
```

---

## ✍️ Author

**[Himanshu Kumar](https://www.linkedin.com/in/h1manshu-kumar/)**

DevOps Engineer | AWS | Jenkins | CI/CD Automation

*Building production-ready pipelines, one commit at a time* 🚀

---

## 📜 License

This project is part of DevOps training and learning documentation.

---

**💡 Pro Tip**: In production environments, combine S3 artifact storage with CloudFront CDN for global distribution and faster deployments across multiple regions.

---

🔥 *"Artifacts are the backbone of deployment pipelines - version them, secure them, and store them right."*
