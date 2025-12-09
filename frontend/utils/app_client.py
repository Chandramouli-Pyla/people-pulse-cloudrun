import requests

BASE_URL = "https://peoplepulse-backend-846180434882.us-central1.run.app"

if not BASE_URL:
    raise ValueError("BASE_URL not set")

def add_employee(payload):
    return requests.post(f"{BASE_URL}/employee", json=payload)

def get_employees():
    return requests.get(f"{BASE_URL}/employees")

def delete_employee(employee_code):
    return requests.delete(f"{BASE_URL}/employees/{employee_code}")

def get_median_age():
    return requests.get(f"{BASE_URL}/stats/median-age")

def get_median_salary():
    return requests.get(f"{BASE_URL}/stats/median-salary")
