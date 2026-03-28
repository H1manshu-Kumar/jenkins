from flask import Flask, render_template, request, redirect, jsonify
from models import init_db, add_entry, get_all_entries, get_stats

app = Flask(__name__)
init_db()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/log', methods=['POST'])
def log_entry():
    date = request.form['date']
    tasks = int(request.form['tasks_done'])
    bugs = int(request.form['bugs_fixed'])
    prs = int(request.form['prs_raised'])
    notes = request.form['notes']
    add_entry(date, tasks, bugs, prs, notes)
    return redirect('/dashboard')


@app.route('/dashboard')
def dashboard():
    entries = get_all_entries()
    stats = get_stats()
    return render_template('dashboard.html', entries=entries, stats=stats)


@app.route('/health')
def health():
    return jsonify({"status": "ok", "db": "connected"})


@app.route('/api/stats')
def api_stats():
    stats = get_stats()
    return jsonify(stats)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
