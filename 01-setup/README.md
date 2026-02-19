# 🚀 Jenkins Phase 0 - Setup & Foundation (CI/CD Platform Bootstrapping)

Welcome to **Jenkins Phase 0**, where the focus is on building a strong foundation for CI/CD by installing, configuring, and validating Jenkins in a production‑style environment.

This phase emphasizes **hands‑on setup**, **operational understanding**, and **platform thinking** - ensuring Jenkins is ready for pipelines, automation workflows, and real‑world CI/CD scenarios.

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

## 🐳 Step 1 - Run Jenkins Using Docker

Pull Jenkins LTS image:

```bash
docker pull jenkins/jenkins:lts
```
<img width="805" height="541" alt="image" src="https://github.com/user-attachments/assets/726aa669-0733-436f-b4fb-f54ac913fcaf" />   

Run container with persistent volume:

```bash
docker run -d --name jenkins -p 8181:8080 -p 50000:50000 -v jenkins_home:/var/jenkins_home jenkins/jenkins:lts
```
**Note:** my host machine 8080 port is already occupied hence I am using 8181 port   
</br>
Verify container:

```bash
docker ps
```
<img width="1200" height="81" alt="image" src="https://github.com/user-attachments/assets/c485d238-0f4c-472f-b6ff-52d54462df61" />   

---

## 🔐 Step 2 - Unlock Jenkins

Open:

👉 http://localhost:8181   
</br>
<img width="921" height="441" alt="image" src="https://github.com/user-attachments/assets/797800ae-7a8a-4ee5-9aca-1eca61e925e9" />

Retrieve admin password:

```bash
docker exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword
```

Paste into UI.

---

## 🔌 Step 3 - Install Suggested Plugins

Install recommended plugins including:

- Git plugin
- Pipeline plugin
- Credentials plugin
- SSH plugin
- GitHub integration

These enable CI/CD workflows.

---

## 👤 Step 4 - Create Admin User

Create secure admin credentials for Jenkins management.    

<img width="921" height="741" alt="image" src="https://github.com/user-attachments/assets/4e11f79c-07c2-4fe0-9f49-b4c819fa38aa" />   
<img width="921" height="323" alt="image" src="https://github.com/user-attachments/assets/5bdf78d4-63e9-465e-9b8c-ddb64fae1b80" />

---

## 🧪 Step 5 - Validate Jenkins (Smoke Test)

Create a Freestyle Job:

Build step:

```bash
echo "Jenkins is working"
```
</br>
<img width="901" height="292" alt="image" src="https://github.com/user-attachments/assets/bc9f18a2-b8ab-4cfe-9b5b-1c28cccecb9f" />
<img width="953" height="227" alt="image" src="https://github.com/user-attachments/assets/82c4c06c-29a8-4ae0-bd88-bd465fd2f4c1" />

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

## 🔄 Persistence Validation

Restart container:

```bash
docker stop jenkins
docker start jenkins
```

Verify:

✅ Jobs still exist  
✅ Configuration preserved  

<img width="249" height="43" alt="image" src="https://github.com/user-attachments/assets/c40caa69-d2be-40cd-ab5e-b43a594d3893" /> </br>

<img width="249" height="43" alt="image" src="https://github.com/user-attachments/assets/91a969bf-c1cb-4fdb-8801-4c876ab829c9" /> </br>

<img width="1264" height="393" alt="image" src="https://github.com/user-attachments/assets/fa253636-8c19-460a-8a1d-3d5bc2319f59" />

---

## 🛠 Troubleshooting Notes

Common issues:

- Jenkins not accessible → Check container status
- Plugins slow → Restart Jenkins
- Port conflict → Verify port mapping

---

## 📚 Lessons Learned

- CI/CD reliability starts with a stable Jenkins foundation.
- Poor setup leads to pipeline instability later.
- Documentation and validation are part of platform engineering, not optional tasks.
- Even local setups should follow production thinking (security, persistence, reproducibility).

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

## ✍️ Author

**[Himanshu Kumar](https://www.linkedin.com/in/h1manshu-kumar/)** - Learning by building, documenting, and sharing 🚀

