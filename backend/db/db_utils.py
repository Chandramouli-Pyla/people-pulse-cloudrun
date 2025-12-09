# backend/db/db_utils.py
from http.client import HTTPException
from statistics import median

from sqlalchemy.orm import Session
from backend.models.employee import Employee
from datetime import date
from sqlalchemy.exc import IntegrityError
from backend.core.logging_config import logger

def add_employee(db: Session, employee_data: dict) -> Employee:
    """
    Add a new employee to the database.
    Args:
        db: SQLAlchemy Session
        employee_data: dict containing employee fields (from EmployeeRequest)
    Returns:
        Employee instance
    """
    try:
        # Create Employee instance using **dict unpacking
        employee = Employee(**employee_data)
        db.add(employee)
        db.commit()
        db.add(employee)
        db.commit()
        db.refresh(employee)
        return employee

    except IntegrityError as e:
        db.rollback()
        logger.error(f"Error adding employee: {e}")
        raise e


def get_all_employees(db: Session) -> list[type[Employee]]:
    """
    Fetch all employees from the database.
    """
    return db.query(Employee).all()


def delete_employee_by_emp_code(db: Session, employee_code: str) -> dict:
    employee = db.query(Employee).filter(Employee.employee_code == employee_code).first()
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")

    db.delete(employee)
    db.commit()
    return {"status": "success", "message": f"Employee with code {employee_code} deleted successfully"}


def get_median_age(db: Session) -> float:
    """Calculate the median age of all employees."""
    employees = db.query(Employee).all()

    if not employees:
        raise HTTPException(status_code=404, detail="No employees found")

    ages = []
    today = date.today()

    for emp in employees:
        age = today.year - emp.date_of_birth.year
        if (today.month, today.day) < (emp.date_of_birth.month, emp.date_of_birth.day):
            age -= 1
        ages.append(age)

    return median(ages)


def get_median_salary(db: Session) -> float:
    """Calculate the median age of all employees."""
    employees = db.query(Employee).all()
    if not employees:
        raise HTTPException(status_code=404, detail="No employees found")
    salaries = []
    for emp in employees:
        salaries.append(emp.salary)
    return median(salaries)
