# Phase 3 - Jenkins Agents + Distributed Builds

---

## 📌 Why This Phase Exists

In Phase 0-2, every build ran on the **Jenkins Controller** - the brain of Jenkins.

That works for learning. It does not work in production.

Here is what happens when you run builds on the controller:

- A heavy build eats controller CPU → Jenkins UI becomes slow or unresponsive
- One bad build script can corrupt Jenkins configuration
- No isolation → builds interfere with each other
- Security risk → build code runs with controller-level permissions

**Phase 3 solves this.** You learn how to move all build execution off the controller and onto **Agents** - isolated, dedicated, scalable workers that do the actual work.

This is how every real Jenkins setup works.

---

## 🧠 Core Concept — How Agents Work

```
                        ┌─────────────────────────────┐
                        │      Jenkins Controller      │
                        │  - Manages jobs & pipelines  │
                        │  - Schedules builds          │
                        │  - Stores configuration      │
                        │  - NEVER runs builds itself  │
                        └────────────┬────────────────┘
                                     │
                    Assigns build via JNLP / SSH / Docker
                                     │
              ┌──────────────────────┼──────────────────────┐
              │                      │                       │
   ┌──────────▼──────┐   ┌──────────▼──────┐   ┌──────────▼──────┐
   │  Static Agent   │   │  Docker Agent   │   │    K8s Agent    │
   │  (Permanent VM) │   │  (Ephemeral     │   │  (Pod-based)    │
   │                 │   │   Container)    │   │                 │
   │  - Long-lived   │   │  - Spins up     │   │  - Scales to    │
   │  - Pre-installed│   │    per build    │   │    zero         │
   │    dependencies │   │  - Destroyed    │   │  - Cloud-native │
   │                 │   │    after build  │   │                 │
   └─────────────────┘   └─────────────────┘   └─────────────────┘
```

**Key rule:** The Controller decides WHAT to run and WHERE. The Agent does the actual work.

---

## 🗺️ What This Phase Covers

| Lab | Topic | Core Concept | Real-World Use Case |
|-----|-------|-------------|---------------------|
| [Lab 3.1](./lab-3.1-static-agent/) | Static Agent Setup | SSH-based permanent agent | Dedicated build servers in enterprise |
| [Lab 3.2](./lab-3.2-docker-agent/) | Docker Agent | Ephemeral container-based agent | Clean, isolated build per run |
| [Lab 3.3](./lab-3.3-multi-agent/) | Multi-Agent Pipeline | Different stages on different agents | Parallel environments per stage |
| [Lab 3.4](./lab-3.4-multibranch/) | Multibranch Pipeline | Branch-based pipeline behavior | Git flow automation |

---

## 🔗 QA-to-DevOps Mental Mapping

If you are coming from a QA background, these concepts are not new - just named differently.

| QA Concept | DevOps Equivalent | How It Maps |
|-----------|-------------------|-------------|
| Selenium Grid Hub | Jenkins Controller | Coordinates where work runs |
| Selenium Grid Node | Jenkins Agent | Does the actual execution |
| Parallel test threads | Parallel stages on agents | Same idea, different layer |
| Clean browser session per test | Ephemeral Docker agent | Fresh environment every run |
| Test environment (dev/staging) | Agent labels | Route work to right environment |
| Test report (JUnit XML) | `junit` post step | Same format - Jenkins reads it natively |

Your QA instinct of **"tests should run in isolation and leave no side effects"** is exactly the principle behind ephemeral Docker agents. You already think this way.

---

## ⚙️ Tech Stack Used In This Phase

```
Jenkins Controller    Running via Docker (from Phase 0 setup)
Docker               Used as agent runtime in Lab 3.2 and 3.3
Python 3.11-slim     Docker image used for build agent
pytest               Test framework running inside agent
SSH                  Used in Lab 3.1 for static agent connection
GitHub Webhook       Used in Lab 3.4 for multibranch triggers
```

---

## 📂 Folder Structure

```
phase-3-agents/
│
├── README.md                      ← You are here
│
├── lab-3.1-static-agent/
│   ├── Jenkinsfile
│   ├── setup-notes.md             ← Step-by-step setup commands
│   └── README.md                  ← What, why, what broke, what I learned
│
├── lab-3.2-docker-agent/
│   ├── Jenkinsfile
│   └── README.md
│
├── lab-3.3-multi-agent/
│   ├── Jenkinsfile
│   └── README.md
│
└── lab-3.4-multibranch/
    ├── Jenkinsfile
    └── README.md
```

---

## 📋 Lab Progress Tracker

| Lab | Status | Commit | Key Problem Solved |
|-----|--------|--------|--------------------|
| Lab 3.1 - Static Agent | ⏳ Not Started | - | - |
| Lab 3.2 - Docker Agent | ⏳ Not Started | - | - |
| Lab 3.3 - Multi-Agent  | ⏳ Not Started | - | - |
| Lab 3.4 - Multibranch  | ⏳ Not Started | - | - |

> Update this table as you complete each lab. Replace ⏳ with ✅.
> Add the commit hash and the real problem you solved in each lab.

---

## ⚠️ Common Mistakes In This Phase

These are the mistakes most beginners make. Read them before starting.

- **Running builds on the controller** because agent setup feels complex - don't take the shortcut
- **Not cleaning agent workspace** — disk fills up silently over time
- **Pinning to `latest` Docker image** — breaks when the image updates upstream
- **Skipping the `agent none` pattern** — leads to accidental controller builds
- **Setting up everything at once** before verifying one working build on an agent
- **Not labeling agents** — you lose the ability to route stages to specific agents

---

## 🎯 Phase 3 Completion Criteria

This phase is done when you can check off every item below:

```
Agents
[ ] At least one build runs on an agent — not the controller
[ ] You can prove it: hostname in console log shows agent, not controller

Docker Agent
[ ] Pipeline uses a Docker container as ephemeral agent
[ ] Test results are published via junit even after container is destroyed
[ ] You have changed the Docker image version and seen the impact

Multi-Agent
[ ] One pipeline uses different agents for different stages
[ ] agent none is declared at top level

Multibranch
[ ] Jenkins auto-detects branches from GitHub
[ ] main branch triggers full pipeline
[ ] develop branch triggers partial pipeline
[ ] feature/* branches trigger tests only

Documentation
[ ] Every lab has a README with: what I built, what broke, how I fixed it
[ ] This README has the progress tracker updated
[ ] Phase 3 summary section below is filled in
```

---

## 🔍 Interview Questions This Phase Prepares You For

After completing Phase 3, you should be able to answer these without hesitation:

**Architecture**
- Why should Jenkins Controller never run builds?
- What is the difference between a static agent and a Docker agent?
- What does `agent none` at the top of a pipeline mean?

**Agents**
- How do you connect a Docker container as a Jenkins agent?
- What happens to the agent workspace after a Docker agent build finishes?
- How do you route a specific stage to a specific agent?

**Multibranch**
- How does Jenkins detect new branches automatically?
- How do you write a Jenkinsfile where feature branches only run tests?
- What is the `when { branch 'main' }` directive and how does it work?

**Troubleshooting**
- A build works on the controller but fails on the agent — how do you debug it?
- Docker agent build fails with "permission denied on docker socket" — what do you check?

---

## 📝 My Learnings - Phase 3 Retrospective

> ✏️ **Fill this section after completing all labs.**
> Be honest. This is your learning journal — not a marketing document.
> Future you (and future employers) will appreciate the honesty more than polished summaries.

### What I Built

<!-- Describe the end state. What does your Phase 3 setup look like? -->

### What Was Harder Than Expected

<!-- Which lab gave you the most trouble? What specifically was confusing? -->

### What Clicked That Wasn't Obvious Before

<!-- What concept made sense only after you built it? -->

### Mistakes I Made

<!-- Real mistakes. Real fixes. No sanitizing. -->

### What I Would Do Differently

<!-- If you started Phase 3 again, what would you change about your approach? -->

### Commands I Find Myself Using Repeatedly

```bash
# Add the commands that became muscle memory during this phase
```

### How My QA Background Helped (or Didn't)

<!-- Honest reflection on where your QA instincts were an advantage and where they were a wrong mental model -->

---

## 🔗 References

- [Jenkins Distributed Builds — Official Docs](https://www.jenkins.io/doc/book/using/using-agents/)
- [Docker Pipeline Plugin](https://plugins.jenkins.io/docker-workflow/)
- [Multibranch Pipeline — Official Docs](https://www.jenkins.io/doc/book/pipeline/multibranch/)
- [Pipeline `when` directive](https://www.jenkins.io/doc/book/pipeline/syntax/#when)

---

*Part of the [Jenkins DevOps Learning Labs](../README.md)*
