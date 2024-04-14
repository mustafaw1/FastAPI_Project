from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_employee():
    response = client.post("/employees/", json={
        "employee_id": 1,
        "name": "Mustafa Hassan",
        "email": "mustafahassan@gmail.com",
        "department": "Engineering",
        "position": "Software Engineer",
        "hire_date": "2022-01-01"
    })
    assert response.status_code == 200
    assert response.json()["name"] == "John Doe"

def test_get_employees():
    response = client.get("/employees/")
    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0]["name"] == "John Doe"

def test_create_shift():
    response = client.post("/shifts/", json={
        "shift_id": 1,
        "employee_id": 1,
        "start_time": "08:00",
        "end_time": "16:00",
        "shift_date": "2024-04-14",
        "location": "Office",
        "role": "Software Development"
    })
    assert response.status_code == 200
    assert response.json()["role"] == "Software Development"

def test_get_employee_shifts():
    response = client.get("/employees/1/shifts")
    assert response.status_code == 200
    assert response.json()[0]["employee_id"] == 1
