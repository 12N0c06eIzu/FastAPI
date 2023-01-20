import pytest
from fastapi.testclient import TestClient

from api.main import app
import json

client = TestClient(app)

def test_check_main():
    res = client.get("/tasks")
    assert res.status_code == 200
    assert res.json() != None
    print(res.json())
