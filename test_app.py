# test_app.py
from app import app
import json

def test_warning_notification():
    client = app.test_client()
    notification = {
        "Type": "Warning",
        "Name": "Disk Failure",
        "Description": "Disk space is low"
    }
    response = client.post("/notify", data=json.dumps(notification), content_type="application/json")
    assert response.status_code == 200
    assert b"forwarded" in response.data

def test_info_notification():
    client = app.test_client()
    notification = {
        "Type": "Info",
        "Name": "CPU Load",
        "Description": "CPU usage normal"
    }
    response = client.post("/notify", data=json.dumps(notification), content_type="application/json")
    assert response.status_code == 200
    assert b"ignored" in response.data

def test_invalid_notification():
    client = app.test_client()
    notification = {
        "Name": "Missing Type",
        "Description": "Oops!"
    }
    response = client.post("/notify", data=json.dumps(notification), content_type="application/json")
    assert response.status_code == 400
