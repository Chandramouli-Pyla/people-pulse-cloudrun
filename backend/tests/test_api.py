import unittest
from fastapi.testclient import TestClient
from unittest.mock import patch
from backend.main import app

client = TestClient(app)

class TestEmployeeAPI(unittest.TestCase):

    def test_create_employee(self):
        payload = {
            "first_name": "John",
            "last_name": "Doe",
            "email": "john123@gmail.com",
            "phone_number": "+12175120038",
            "house_number": "12",
            "street": "Main St",
            "apartment": "1A",
            "city": "NY",
            "state": "NY",
            "country": "USA",
            "zip_code": "12345",
            "employee_code": "FD10001",
            "department": "IT",
            "position": "Dev",
            "salary": 50000,
            "date_of_birth": "1999-06-12",
            "date_of_joining": "2023-01-01"
        }

        with patch("backend.app.api.employee_routes.create_employee") as mock_create:
            mock_create.return_value = {
                "employee_code": payload["employee_code"],
                "first_name": payload["first_name"],
                "last_name": payload["last_name"],
                "department": payload["department"],
                "position": payload["position"]
            }

            response = client.post("/employee", json=payload)
            self.assertEqual(response.status_code, 201)
            self.assertEqual(response.json()["message"], "Employee created successfully")
            self.assertEqual(response.json()["data"]["employee_code"], "FD10001")

    def test_get_employees(self):
            mock_employee_list = [
                {
                    "employee_code": "EMP001",
                    "first_name": "John",
                    "last_name": "Doe",
                    "department": "IT",
                    "position": "Engineer"
                },
                {
                    "employee_code": "EMP002",
                    "first_name": "Jane",
                    "last_name": "Smith",
                    "department": "HR",
                    "position": "Manager"
                }
            ]

            with patch("backend.app.api.employee_routes.list_employees") as mock_list:
                mock_list.return_value = mock_employee_list

                # CALL THE API (GET — NO PAYLOAD)
                response = client.get("/employees")

                # VALIDATE RESPONSE
                self.assertEqual(response.status_code, 200)
                self.assertEqual(response.json()["message"], "Employee Data Retrieved Successfully")
                self.assertEqual(len(response.json()["data"]), 2)
                self.assertEqual(response.json()["data"][0]["employee_code"], "EMP001")
                self.assertEqual(response.json()["data"][1]["employee_code"], "EMP002")

    def test_create_employee_bad_request(self):
        payload = {
            "first_name": "John",
            "last_name": "Doe",
            "email": "john123@gmail.com",
            "phone_number": "+12175120038",
            "house_number": "12",
            "street": "Main St",
            "apartment": "1A",
            "city": "NY",
            "state": "NY",
            "country": "USA",
            "zip_code": "12345",
            "employee_code": "FD10001",
            "department": "IT",
            "position": "Dev",
            "salary": 50000,
            "date_of_birth": "1999-06-12",
            "date_of_joining": "2023-01-01"
        }

        with patch("backend.app.api.employee_routes.create_employee") as mock_create:
            mock_create.side_effect = Exception("Employee code already exists")

            response = client.post("/employee", json=payload)

            self.assertEqual(response.status_code, 400)
            self.assertIn("Employee code already exists", response.json()["detail"])

    def test_get_employees_failure(self):
        with patch("backend.app.api.employee_routes.list_employees") as mock_list:
            mock_list.side_effect = Exception("Database error")

            response = client.get("/employees")

            self.assertEqual(response.status_code, 400)
            self.assertIn("Database error", response.json()["detail"])

    def test_delete_employee(self):
        employee_code = "EMP001"

        with patch("backend.app.api.employee_routes.delete_employee") as mock_delete:
            mock_delete.return_value = {"deleted": True}

            response = client.delete(f"/employees/{employee_code}")

            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json()["message"], "Employee deleted successfully")
            self.assertEqual(response.json()["data"], {"deleted": True})


    def test_get_median_age(self):
        with patch("backend.app.api.employee_routes.calculate_median_age") as mock_median:
            mock_median.return_value = {"median": 5}
            response = client.get("/stats/median-age")
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json()["message"], "Median age calculated successfully")
            self.assertEqual(response.json()["data"]["median"], 5)

    def test_get_median_age_no_data(self):
        with patch("backend.app.api.employee_routes.calculate_median_age") as mock_median:
            mock_median.side_effect = Exception("No employees found")

            response = client.get("/stats/median-age")

            self.assertEqual(response.status_code, 400)
            self.assertIn("No employees found", response.json()["detail"])

    def test_get_median_salary(self):
        with patch("backend.app.api.employee_routes.calculate_median_salary") as mock_calculate:
            mock_calculate.return_value = {"median_salary": 60000}
            response = client.get("/stats/median-salary")
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json()["message"], "Median salary calculated successfully")
            self.assertEqual(response.json()["data"]["median_salary"], 60000)

    def test_get_median_salary_no_data(self):
        with patch("backend.app.api.employee_routes.calculate_median_salary") as mock_calc:
            mock_calc.side_effect = Exception("No salary data available")

            response = client.get("/stats/median-salary")

            self.assertEqual(response.status_code, 400)
            self.assertIn("No salary data available", response.json()["detail"])
