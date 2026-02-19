# 🚀 Jenkins Phase 0 — Setup & Foundation (CI/CD Platform Bootstrapping)

Welcome to **Jenkins Phase 0**, where the focus is on building a strong foundation for CI/CD by installing, configuring, and validating Jenkins in a production‑style environment.

This phase emphasizes **hands‑on setup**, **operational understanding**, and **platform thinking** — ensuring Jenkins is ready for pipelines, automation workflows, and real‑world CI/CD scenarios.

---

## 🧭 Phase Goal

Establish a fully functional Jenkins environment with:

✅ Containerized Jenkins setup (Docker)  
✅ Persistent storage configuration  
✅ Initial security setup  
✅ Plugin installation  
✅ Admin user creation  
✅ Environment validation via test job  
✅ Documentation + screenshots  
✅ Operational understanding  

---

## 🔎 SEO Keywords

Jenkins setup, Jenkins Phase 0, Jenkins installation guide, Jenkins Docker setup, CI/CD pipeline foundation, Jenkins beginner guide, Jenkins hands‑on lab, Jenkins environment setup, DevOps Jenkins tutorial, Jenkins configuration best practices, Jenkins learning roadmap.

---

## 🏗 Architecture Overview

Jenkins follows a **controller‑agent architecture**:

- 🧠 Controller → Orchestrates jobs, manages configuration
- ⚙️ Agents → Execute builds and pipelines
- 🔌 Plugins → Extend capabilities
- 📦 JENKINS_HOME → Stores state and configuration

---

## 🐳 Step 1 — Run Jenkins Using Docker

Pull Jenkins LTS image:

```bash
docker pull jenkins/jenkins:lts
```

Run container with persistent volume:

```bash
docker run -d \
  --name jenkins \
  -p 8080:8080 \
  -p 50000:50000 \
  -v jenkins_home:/var/jenkins_home \
  jenkins/jenkins:lts
```

Verify container:

```bash
docker ps
```

---

## 🔐 Step 2 — Unlock Jenkins

Open:

👉 http://localhost:8080

Retrieve admin password:

```bash
docker exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword
```

Paste into UI.

---

## 🔌 Step 3 — Install Suggested Plugins

Install recommended plugins including:

- Git plugin
- Pipeline plugin
- Credentials plugin
- SSH plugin
- GitHub integration

These enable CI/CD workflows.

---

## 👤 Step 4 — Create Admin User

Create secure admin credentials for Jenkins management.

---

## 🧪 Step 5 — Validate Jenkins (Smoke Test)

Create a Freestyle Job:

Build step:

```bash
echo "Jenkins is working"
```

Confirm successful build.

---

## 📂 Jenkins Data Persistence

All Jenkins state stored in:

```
/var/jenkins_home
```

Includes:

- Jobs
- Plugins
- Credentials
- Logs
- Configurations

---

## 🖼 Screenshots Section

📸 Add evidence of hands‑on:

- Jenkins dashboard
- Plugin installation
- Unlock screen
- Successful build output
- Manage Jenkins page

Example:

```
screenshots/dashboard.png
screenshots/build-success.png
```

---

## 🔄 Persistence Validation

Restart container:

```bash
docker stop jenkins
docker start jenkins
```

Verify:

✅ Jobs still exist  
✅ Configuration preserved  

---

## 🛠 Troubleshooting Notes

Common issues:

- Jenkins not accessible → Check container status
- Plugins slow → Restart Jenkins
- Port conflict → Verify port mapping

---

## 📚 Lessons Learned (Fill During Hands‑On)

- ____________________________________
- ____________________________________
- ____________________________________
- ____________________________________

---

## 🧠 Key Concepts to Understand

- CI/CD fundamentals
- Jenkins controller role
- Plugin ecosystem
- Persistent storage importance
- Automation server responsibilities

---

## 🛡 Production Considerations

- Avoid running builds on controller
- Secure credentials properly
- Monitor Jenkins resource usage
- Keep plugins updated

---

## ✔ Phase Completion Checklist

- [ ] Jenkins container running
- [ ] UI accessible
- [ ] Plugins installed
- [ ] Admin user created
- [ ] Test job successful
- [ ] Persistence verified
- [ ] Screenshots added
- [ ] Notes documented

---

## 🌟 Outcome

You now have a working Jenkins environment ready for:

➡ Pipeline as Code  
➡ Git integration  
➡ Distributed builds  
➡ CI/CD automation  

---

## 🚀 Next Phase Preview

Phase 1 will dive into:

- Jenkins architecture deep dive
- Controller vs agent internals
- Pipeline fundamentals

---


