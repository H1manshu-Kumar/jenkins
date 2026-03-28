import pytest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app
from models import init_db


@pytest.fixture
def client():
    app.config['TESTING'] = True
    if os.path.exists('devpulse.db'):
        os.remove('devpulse.db')
    init_db()
    with app.test_client() as client:
        yield client


def test_index_returns_200(client):
    response = client.get('/')
    assert response.status_code == 200


def test_log_entry_inserts_and_redirects(client):
    response = client.post('/log', data={
        'date': '2024-01-15',
        'tasks_done': '5',
        'bugs_fixed': '2',
        'prs_raised': '1',
        'notes': 'Good day'
    }, follow_redirects=False)
    assert response.status_code == 302
    assert '/dashboard' in response.location


def test_dashboard_returns_200_with_content(client):
    response = client.get('/dashboard')
    assert response.status_code == 200
    assert b'Dashboard' in response.data


def test_health_endpoint_returns_ok(client):
    response = client.get('/health')
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data['status'] == 'ok'


def test_api_stats_returns_correct_keys(client):
    response = client.get('/api/stats')
    assert response.status_code == 200
    json_data = response.get_json()
    assert 'total_tasks' in json_data
    assert 'total_bugs' in json_data
    assert 'total_prs' in json_data
