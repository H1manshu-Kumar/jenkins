# 🧪 Lab 07 — Backup & Restore Jenkins

> Learn how to back up and restore Jenkins to simulate disaster recovery scenarios.

---

## 🎯 Objective

In this lab, we will:

- Understand Jenkins Home structure
- Perform Jenkins backup
- Simulate controller failure
- Restore Jenkins from backup
- Validate recovery

This mirrors real production incidents where CI systems must be restored quickly.

---

## 🧠 Why This Lab Matters

In production:

- Controllers may crash
- Disk corruption may occur
- Accidental deletion can happen
- Disaster recovery is critical

Without backup, CI pipelines and history are permanently lost.

---

## 🏗️ What Needs Backup

Jenkins stores data in:

/var/jenkins_home

This includes:

- Jobs
- Build history
- Credentials
- Plugins
- Configuration
- Workspace metadata

---

## 🧰 Prerequisites

- Lab 01 to 06 completed
- Jenkins running in Docker
- Some pipelines already created

---

## 🚀 Step 1 — Verify Jenkins Home Volume

Check running container:

```bash
docker inspect jenkins-controller
```

Confirm volume mapping:

jenkins_home → /var/jenkins_home

---

## 💾 Step 2 — Take Backup

Run:

```bash
docker cp jenkins-controller:/var/jenkins_home ./jenkins_backup
```

Verify backup folder exists locally.

---

## 🔥 Step 3 — Simulate Failure

Stop Jenkins:

```bash
docker stop jenkins-controller
```

Remove container:

```bash
docker rm jenkins-controller
```

(Optional: remove volume to simulate data loss)

---

## ♻️ Step 4 — Restore Jenkins

Create new container:

```bash
docker run -d   --name jenkins-controller   -p 8080:8080   -p 50000:50000   -v $(pwd)/jenkins_backup:/var/jenkins_home   jenkins/jenkins:lts
```

---

## 👀 Step 5 — Validate Restoration

Open:

http://localhost:8080

Verify:

- Jobs restored
- Build history present
- Credentials intact
- Plugins available

---

## 📊 Expected Behavior

- Jenkins loads previous configuration
- All jobs visible
- No data loss

---

## 🧠 Deep Learning Notes

Jenkins durability depends entirely on:

Jenkins Home persistence.

If Jenkins Home is lost:

Everything is lost.

---

## 🛠️ Failure Simulation

Corrupt a job config file.

Restart Jenkins.

Observe failure in job loading.

---

## 🧑‍💻 Real Production Insights

Best practices:

- Regular automated backups
- Store backups offsite
- Monitor disk usage
- Test restoration periodically

---

## 🎓 Interview Talking Points

Be ready to explain:

- What should be backed up in Jenkins?
- How do you restore Jenkins?
- What happens if Jenkins Home is lost?
- How to design disaster recovery?

Strong answer:

“Jenkins durability depends on Jenkins Home persistence; regular backups are essential.”

---

## 🧩 Evidence To Add

- Backup folder screenshot
- Restore validation screenshot
- Jobs restored view

---

## 📌 Lessons Learned (Fill After Lab)

- …
- …
- …

---

## 🚀 Stretch Exercise

Try:

Automate backup using cron inside host.

---

## 🏁 Lab Completion Checklist

- [ ] Backup taken
- [ ] Failure simulated
- [ ] Jenkins restored
- [ ] Jobs verified

---

> Backup strategy defines CI reliability in production.

