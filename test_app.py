#!/usr/bin/python3
import os
import tempfile
import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_valid_transaction(client):
    card = {
        "status": True,
        "number": 123456,
        "limit": 1000,
        "transaction": {
            "amount": 500
        }
    }
    rv = client.post("/api/transaction", json=card)
    assert rv.get_json().get("approved") == True
    assert rv.get_json().get("newLimit") == 500

def test_above_limit(client):
    card = {
        "status": True,
        "number": 123456,
        "limit": 1000,
        "transaction": {
            "amount": 1500
        }
    }
    rv = client.post("/api/transaction", json=card)
    assert rv.get_json().get("approved") == False
    assert "Transaction above the limit" in rv.get_json().get("reason")

def test_blocked_card(client):
    card = {
        "status": False,
        "number": 123456,
        "limit": 1000,
        "transaction": {
            "amount": 500
        }
    }
    rv = client.post("/api/transaction", json=card)
    assert rv.get_json().get("approved") == False
    assert "Blocked Card" in rv.get_json().get("reason")


