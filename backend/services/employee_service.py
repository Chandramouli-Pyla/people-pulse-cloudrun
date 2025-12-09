from http.client import HTTPException

from sqlalchemy.orm import Session
from datetime import date

from backend.db.db_utils import add_employee, get_all_employees, delete_employee_by_emp_code, get_median_age, \
    get_median_salary
from backend.models.employee import Employee
from backend.schemas.employee_request import EmployeeRequest
from backend.schemas.employee_response import EmployeeResponse
from backend.core.logging_config import logger


def create_employee(db: Session, employee_request: EmployeeRequest) -> EmployeeResponse:
    """
    Add a new employee using EmployeeRequest schema.
    """
    try:
        # Convert Pydantic model to dict for DB insert
        employee_data = employee_request.model_dump()

        # Call db_utils function
        new_employee: Employee = add_employee(db, employee_data)

        # Compute age from date_of_birth
        today = date.today()
        age = today.year - new_employee.date_of_birth.year - (
            (today.month, today.day) < (new_employee.date_of_birth.month, new_employee.date_of_birth.day)
        )

        # Build response schema
        response = EmployeeResponse(
            id=new_employee.id,
            first_name=new_employee.first_name,
            last_name=new_employee.last_name,
            email=new_employee.email,
            phone_number=new_employee.phone_number,
            house_number=new_employee.house_number,
            street=new_employee.street,
            apartment=new_employee.apartment,
            city=new_employee.city,
            state=new_employee.state,
            country=new_employee.country,
            zip_code=new_employee.zip_code,
            employee_code=new_employee.employee_code,
            department=new_employee.department,
            position=new_employee.position,
            salary=new_employee.salary,
            date_of_joining=new_employee.date_of_joining,
            date_of_birth=new_employee.date_of_birth,
            age=age
        )

        logger.info(f"Employee created: {new_employee}")
        return response

    except Exception as e:
        logger.error(f"Failed to create employee: {e}")
        raise e


def list_employees(db: Session) -> list[EmployeeResponse]:
    employees = get_all_employees(db)  # list of Employee instances
    return [EmployeeResponse.model_validate(emp) for emp in employees]  # list of Pydantic models


def delete_employee(db: Session, employee_code: str) -> dict:
    try:
        result = delete_employee_by_emp_code(db, employee_code)
        return result
    except HTTPException as e:
        raise e


def calculate_median_age(db: Session) -> dict:
    """Service layer to fetch median age."""
    median_age = get_median_age(db)
    return {"median_age": median_age}

def calculate_median_salary(db: Session) -> dict:
    median_sal = get_median_salary(db)
    return {"median_salary": median_sal}