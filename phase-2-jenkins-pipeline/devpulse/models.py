import sqlite3


def get_connection():
    conn = sqlite3.connect('devpulse.db')
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS entries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            tasks_done INTEGER NOT NULL,
            bugs_fixed INTEGER NOT NULL,
            prs_raised INTEGER NOT NULL,
            notes TEXT
        )
    ''')
    conn.commit()
    conn.close()


def add_entry(date, tasks_done, bugs_fixed, prs_raised, notes):
    conn = get_connection()
    conn.execute(
        'INSERT INTO entries (date, tasks_done, bugs_fixed, prs_raised, notes) '
        'VALUES (?, ?, ?, ?, ?)',
        (date, tasks_done, bugs_fixed, prs_raised, notes)
    )
    conn.commit()
    conn.close()


def get_all_entries():
    conn = get_connection()
    entries = conn.execute(
        'SELECT * FROM entries ORDER BY date DESC'
    ).fetchall()
    conn.close()
    return entries


def get_stats():
    conn = get_connection()
    result = conn.execute(
        'SELECT SUM(tasks_done) as total_tasks, '
        'SUM(bugs_fixed) as total_bugs, '
        'SUM(prs_raised) as total_prs FROM entries'
    ).fetchone()
    conn.close()
    return {
        'total_tasks': result['total_tasks'] or 0,
        'total_bugs': result['total_bugs'] or 0,
        'total_prs': result['total_prs'] or 0
    }
