# 📊 DevPulse

> **Track your developer productivity metrics with ease**

A lightweight Flask-based web application for developers to log and visualize their daily work metrics including tasks completed, bugs fixed, and pull requests raised. Perfect for personal productivity tracking, team standups, and performance reviews.

[![Python](https://img.shields.io/badge/Python-3.12-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.0.0-green.svg)](https://flask.palletsprojects.com/)
[![SQLite](https://img.shields.io/badge/Database-SQLite-lightgrey.svg)](https://www.sqlite.org/)
[![Tests](https://img.shields.io/badge/Tests-Pytest-orange.svg)](https://pytest.org/)

---

## 🚀 Features

✅ **Daily Logging** - Track tasks, bugs, and PRs with date-stamped entries  
✅ **Dashboard Analytics** - View all entries and cumulative statistics  
✅ **RESTful API** - JSON endpoints for health checks and stats  
✅ **Responsive UI** - Clean, modern interface with custom CSS  
✅ **SQLite Database** - Lightweight, zero-config data persistence  
✅ **Unit Tested** - Comprehensive test coverage with pytest  
✅ **Production Ready** - Health check endpoint for monitoring  

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| **Flask** | Web framework |
| **SQLite** | Database |
| **Python 3.12** | Backend language |
| **HTML/CSS** | Frontend |
| **Pytest** | Testing framework |
| **Flake8** | Code linting |

---

## 📁 Project Structure

```
devpulse/
├── app.py                 # Main Flask application
├── models.py              # Database models and operations
├── requirements.txt       # Python dependencies
├── devpulse.db           # SQLite database (auto-generated)
├── templates/
│   ├── index.html        # Entry logging page
│   └── dashboard.html    # Analytics dashboard
├── static/
│   └── style.css         # Custom styling
└── tests/
    └── test_app.py       # Unit tests
```

---

## 🏃 Quick Start

### Prerequisites
- Python 3.12+
- pip

### Installation

1. **Clone the repository**
```bash
git clone <repository-url>
cd devpulse
```

2. **Create virtual environment**
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run the application**
```bash
python app.py
```

5. **Access the app**
```
http://localhost:5000
```
<img width="1280" height="716" alt="image" src="https://github.com/user-attachments/assets/fae0402a-2093-4e02-9ef1-f8eedc29e9a0" />


<img width="1280" height="611" alt="image" src="https://github.com/user-attachments/assets/b735407a-85c2-4ecb-8113-f1ff89fe6ecf" />


---

## 🎯 Usage

### Log Daily Metrics
1. Navigate to the home page (`/`)
2. Fill in the form with:
   - Date
   - Tasks completed
   - Bugs fixed
   - Pull requests raised
   - Optional notes
3. Submit to save your entry

### View Dashboard
- Access `/dashboard` to see:
  - All logged entries (newest first)
  - Total statistics across all entries
  - Historical data overview

### API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Home page with entry form |
| `/log` | POST | Submit new entry |
| `/dashboard` | GET | View all entries and stats |
| `/health` | GET | Health check (returns JSON) |
| `/api/stats` | GET | Get statistics (returns JSON) |

**Example API Response:**
```json
{
  "total_tasks": 45,
  "total_bugs": 12,
  "total_prs": 8
}
```

---

## 🧪 Testing

Run the test suite:
```bash
pytest tests/
```

Run with coverage:
```bash
pytest tests/ -v
```

Lint code:
```bash
flake8 app.py models.py
```

---

## 🐳 Docker Deployment (Optional)

```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]
```

Build and run:
```bash
docker build -t devpulse .
docker run -p 5000:5000 devpulse
```

---

## 🔧 Configuration

The application runs with the following defaults:
- **Host:** `0.0.0.0` (accessible from network)
- **Port:** `5000`
- **Debug Mode:** `True` (disable in production)
- **Database:** `devpulse.db` (SQLite)

To modify, edit `app.py`:
```python
app.run(debug=False, host='0.0.0.0', port=5000)
```

---

## 📊 Database Schema

```sql
CREATE TABLE entries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT NOT NULL,
    tasks_done INTEGER NOT NULL,
    bugs_fixed INTEGER NOT NULL,
    prs_raised INTEGER NOT NULL,
    notes TEXT
);
```

---

## 🚀 CI/CD Integration

This project is designed for Jenkins pipeline integration:
- Automated testing with pytest
- Code quality checks with flake8
- Health check endpoint for monitoring
- Easy containerization for deployment

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 License

This project is open source and available under the MIT License.

---

## ✍️ Author

**[Himanshu Kumar](https://www.linkedin.com/in/h1manshu-kumar/)** - Learning by building, documenting, and sharing 🚀

---

## 🔗 Keywords

`python` `flask` `sqlite` `web-application` `developer-tools` `productivity` `metrics-tracking` `rest-api` `pytest` `devops` `ci-cd` `jenkins` `full-stack` `backend-development`

---

## 📞 Support

For issues, questions, or suggestions, please open an issue in the GitHub repository.

---

**⭐ If you find this project useful, please consider giving it a star!**
