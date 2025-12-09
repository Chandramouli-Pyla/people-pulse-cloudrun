import unittest
from unittest.mock import patch, MagicMock

from frontend.utils.app_client import (
    add_employee,
    get_employees,
    delete_employee,
    get_median_age,
    get_median_salary
)

# ============================================================
#                  ADD EMPLOYEE TESTS
# ============================================================
class TestAddEmployee(unittest.TestCase):

    @patch("frontend.utils.app_client.requests.post")
    def test_add_employee_success(self, mock_post):
        mock_response = MagicMock()
        mock_response.status_code = 201
        mock_response.json.return_value = {
            "message": "Employee created successfully",
            "data": {"id": 1, "first_name": "John"}
        }

        mock_post.return_value = mock_response

        payload = {
            "first_name": "John",
            "last_name": "Doe",
            "email": "john@gmail.com"
        }

        response = add_employee(payload)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()["data"]["first_name"], "John")
        mock_post.assert_called_once()

    @patch("frontend.utils.app_client.requests.post")
    def test_add_employee_validation_error(self, mock_post):
        mock_response = MagicMock()
        mock_response.status_code = 422
        mock_response.json.return_value = {"detail": "Invalid email"}

        mock_post.return_value = mock_response

        response = add_employee({"email": "bad-email"})

        self.assertEqual(response.status_code, 422)
        self.assertEqual(response.json()["detail"], "Invalid email")

    @patch("frontend.utils.app_client.requests.post")
    def test_add_employee_server_error(self, mock_post):
        mock_response = MagicMock()
        mock_response.status_code = 500
        mock_response.json.return_value = {"detail": "Internal Server Error"}

        mock_post.return_value = mock_response

        response = add_employee({"first_name": "John"})

        self.assertEqual(response.status_code, 500)

    @patch("frontend.utils.app_client.requests.post")
    def test_add_employee_network_failure(self, mock_post):
        mock_post.side_effect = Exception("Network down")

        with self.assertRaises(Exception):
            add_employee({"first_name": "John"})


# ============================================================
#                  GET EMPLOYEES TESTS
# ============================================================
class TestGetEmployees(unittest.TestCase):

    @patch("frontend.utils.app_client.requests.get")
    def test_get_employees_success(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "data": [
                {"employee_code": "FD12345", "first_name": "John"},
                {"employee_code": "FD54321", "first_name": "Mary"},
            ]
        }

        mock_get.return_value = mock_response

        response = get_employees()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()["data"]), 2)

    @patch("frontend.utils.app_client.requests.get")
    def test_get_employees_empty(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"data": []}

        mock_get.return_value = mock_response

        response = get_employees()
        self.assertEqual(response.json()["data"], [])

    @patch("frontend.utils.app_client.requests.get")
    def test_get_employees_server_error(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 500

        mock_get.return_value = mock_response

        response = get_employees()
        self.assertEqual(response.status_code, 500)

    @patch("frontend.utils.app_client.requests.get")
    def test_get_employees_network_failure(self, mock_get):
        mock_get.side_effect = Exception("Network down")

        with self.assertRaises(Exception):
            get_employees()


# ============================================================
#                  DELETE EMPLOYEE TESTS
# ============================================================
class TestDeleteEmployee(unittest.TestCase):

    @patch("frontend.utils.app_client.requests.delete")
    def test_delete_employee_success(self, mock_delete):
        mock_response = MagicMock()
        mock_response.status_code = 204

        mock_delete.return_value = mock_response

        response = delete_employee("FD12345")

        self.assertEqual(response.status_code, 204)
        mock_delete.assert_called_once()

    @patch("frontend.utils.app_client.requests.delete")
    def test_delete_employee_not_found(self, mock_delete):
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_response.json.return_value = {"detail": "Employee not found"}

        mock_delete.return_value = mock_response

        response = delete_employee("INVALID")

        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json()["detail"], "Employee not found")

    @patch("frontend.utils.app_client.requests.delete")
    def test_delete_employee_server_error(self, mock_delete):
        mock_response = MagicMock()
        mock_response.status_code = 500

        mock_delete.return_value = mock_response

        response = delete_employee("FD12345")
        self.assertEqual(response.status_code, 500)

    @patch("frontend.utils.app_client.requests.delete")
    def test_delete_employee_network_failure(self, mock_delete):
        mock_delete.side_effect = Exception("Network down")

        with self.assertRaises(Exception):
            delete_employee("FD12345")


# ============================================================
#               MEDIAN AGE & SALARY TESTS
# ============================================================
class TestStats(unittest.TestCase):

    @patch("frontend.utils.app_client.requests.get")
    def test_get_median_age_success(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"median_age": 29}

        mock_get.return_value = mock_response

        response = get_median_age()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["median_age"], 29)

    @patch("frontend.utils.app_client.requests.get")
    def test_get_median_salary_success(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"median_salary": 54000}

        mock_get.return_value = mock_response

        response = get_median_salary()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["median_salary"], 54000)

    @patch("frontend.utils.app_client.requests.get")
    def test_median_age_failure(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 500

        mock_get.return_value = mock_response

        response = get_median_age()
        self.assertEqual(response.status_code, 500)

    @patch("frontend.utils.app_client.requests.get")
    def test_median_salary_failure(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 500

        mock_get.return_value = mock_response

        response = get_median_salary()
        self.assertEqual(response.status_code, 500)

    @patch("frontend.utils.app_client.requests.get")
    def test_stats_network_failure(self, mock_get):
        mock_get.side_effect = Exception("Network down")

        with self.assertRaises(Exception):
            get_median_age()
