from app import app

import os
import pytest
from flask import jsonify

# --- Fixtures ---

@pytest.fixture()
def test_client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

# --- Test functions---

def test_index_success(test_client, monkeypatch):
    """Tests the successful connection scenario"""
    # Monkeypatch environment variables (required for testing)
    monkeypatch.setenv("DB_HOST", "test_db") 
    monkeypatch.setenv("DB_NAME", "test_db_name")
    monkeypatch.setenv("DB_USER", "test_db_user") 
    monkeypatch.setenv("DB_PASSWORD", "test_db_password")

    response = test_client.get("/")
    # assert response.status_code == 200
    assert response.json == {"status": "OK 👌"}

# def test_index_failure(test_client, monkeypatch):
#     """Tests when the connection intentionally fails"""
#     monkeypatch.setenv("DB_HOST", "wrong_host")  # Introduce an incorrect host
#     monkeypatch.setenv("DB_NAME", "test_db_name")
#     monkeypatch.setenv("DB_USER", "test_db_user")
#     monkeypatch.setenv("DB_PASSWORD", "test_db_password")

#     response = test_client.get("/")
#     assert response.status_code == 500
#     assert "error" in response.json

# --- How to run the tests ---
# Make sure you have the following packages installed:
# pip install pytest pytest-mock psycopg2-binary

# From your terminal run:
# pytest test_app.py
