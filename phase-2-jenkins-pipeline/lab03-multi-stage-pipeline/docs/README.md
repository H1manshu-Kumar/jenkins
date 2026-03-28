# DevPulse - Developer Health Dashboard

DevPulse is a lightweight Python Flask web application that helps developers track their daily work metrics including tasks completed, bugs fixed, and pull requests raised. It provides a simple dashboard to visualize productivity over time.

## What This App Does

- Log daily developer metrics (tasks, bugs, PRs) with notes
- View all entries in a clean dashboard with summary statistics
- Provides REST API endpoints for health checks and stats
- Uses SQLite for simple, file-based data persistence
- Perfect for learning Jenkins CI/CD pipelines

## Tech Stack

- **Backend**: Python 3 + Flask
- **Database**: SQLite (file-based)
- **Frontend**: HTML + CSS + Vanilla JavaScript
- **Testing**: pytest
- **Linting**: flake8

## How to Run Locally

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Installation Steps

1. Clone or download this repository

2. Create a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python app.py
```

5. Open your browser and navigate to:
```
http://localhost:5000
```

The SQLite database (`devpulse.db`) will be created automatically on first run.

### Running Tests

```bash
pytest tests/ -v
```

### Running Linter

```bash
flake8 app.py models.py --max-line-length=100
```

## API Endpoints

- `GET /` - Home page with entry form
- `POST /log` - Submit a new entry
- `GET /dashboard` - View all entries and statistics
- `GET /health` - Health check endpoint (returns JSON)
- `GET /api/stats` - Get statistics as JSON

## Setting Up Jenkins CI/CD Pipeline

### Prerequisites

- Jenkins installed and running locally
- Git plugin installed in Jenkins
- Python 3 and pip available on Jenkins agent/node

### Option 1: Pipeline Job (Recommended)

1. Open Jenkins dashboard
2. Click "New Item"
3. Enter job name (e.g., "DevPulse-Pipeline")
4. Select "Pipeline" and click OK
5. In the Pipeline section, choose one of:
   - **Pipeline script from SCM**: 
     - Select Git
     - Enter your repository URL
     - Set Script Path to `Jenkinsfile`
   - **Pipeline script**: 
     - Copy and paste the contents of `Jenkinsfile` directly

6. Save and click "Build Now"

### Option 2: Freestyle Job

1. Create a new Freestyle project
2. Configure Source Code Management (Git)
3. Add build steps manually for each stage:
   - Execute shell: Install dependencies
   - Execute shell: Run linting
   - Execute shell: Run tests
   - Execute shell: Create artifact
   - Execute shell: Health check
4. Add post-build action: Archive artifacts (`devpulse-build.zip`)

### Jenkins Pipeline Stages Explained

The `Jenkinsfile` contains a declarative pipeline with the following stages:

1. **Checkout**: Automatically checks out code from Git repository
   - Jenkins handles this automatically
   - Ensures latest code is available for build

2. **Install Dependencies**: Sets up Python environment
   - Creates a Python virtual environment
   - Installs all packages from `requirements.txt`
   - Ensures isolated and reproducible builds

3. **Lint**: Code quality check with flake8
   - Runs flake8 on `app.py` and `models.py`
   - Enforces PEP 8 style guidelines (max line length: 100)
   - Build fails if linting errors are found

4. **Test**: Runs automated test suite
   - Executes all pytest tests in `tests/` directory
   - Runs with verbose output (`-v` flag)
   - Build fails if any test fails

5. **Build Artifact**: Creates deployment package
   - Zips all project files into `devpulse-build.zip`
   - Excludes unnecessary files (git, cache, venv, database)
   - Creates a clean, deployable artifact

6. **Health Check**: Validates application functionality
   - Starts Flask app in background
   - Waits for app to initialize (5 seconds)
   - Curls the `/health` endpoint
   - Verifies response contains `"status": "ok"`
   - Stops the Flask app
   - Build fails if health check doesn't pass

7. **Archive**: Saves build artifacts in Jenkins
   - Uses Jenkins `archiveArtifacts` to store the zip file
   - Enables fingerprinting for tracking
   - Artifacts available for download from Jenkins UI

8. **Post Block**: Cleanup and notifications
   - **Always**: Prints "Pipeline finished" regardless of result
   - **Success**: Prints "Build passed" on successful build
   - **Failure**: Prints "Build failed — check logs" on failure

## Project Structure

```
devpulse/
├── app.py                 # Main Flask application with routes
├── models.py              # Database models and SQLite logic
├── requirements.txt       # Python dependencies
├── Jenkinsfile            # Declarative Jenkins pipeline
├── README.md              # This file
├── tests/
│   └── test_app.py        # Pytest test cases
├── templates/
│   ├── index.html         # Entry form page
│   └── dashboard.html     # Dashboard page
└── static/
    └── style.css          # CSS styling
```

## Troubleshooting

### Port Already in Use
If port 5000 is already in use, modify `app.py` and change the port number in the last line.

### Jenkins Health Check Fails
- Ensure port 5000 is not blocked by firewall
- Check if Flask app starts successfully in Jenkins workspace
- Verify curl is installed on Jenkins agent
- Increase sleep time in Health Check stage if app takes longer to start

### Tests Fail in Jenkins
- Ensure pytest is installed in the virtual environment
- Check that the workspace is clean (no leftover database files)
- Verify Python 3 is available on the Jenkins agent

## License

This project is for educational purposes to learn Jenkins CI/CD pipelines.
