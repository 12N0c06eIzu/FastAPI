import pytest
from fastapi.testclient import TestClient

from api.main import app

client = TestClient(app)

def test_check_main():
    res = client.get("/")
    assert res.status_code == 200
    assert res.json() == {"msg": "Hello world"}
