from fastapi import APIRouter, Depends, HTTPException, status, Path
from sqlalchemy.orm import Session

from backend.schemas.employee_request import EmployeeRequest
from backend.schemas.employee_response import EmployeeResponse
from backend.schemas.api_response import APIResponse
from backend.services.employee_service import create_employee, list_employees, delete_employee, \
    calculate_median_age, calculate_median_salary
from backend.dependencies.db_dependencies import get_db
from backend.core.logging_config import logger

router = APIRouter(
    prefix="",
    tags=["Employee"]
)


@router.post("/employee", response_model=APIResponse, status_code=status.HTTP_201_CREATED)
async def add_employee(
    employee_request: EmployeeRequest,
    db: Session = Depends(get_db)
):
    """
    Add a new employee.
    """
    try:
        employee_response: EmployeeResponse = create_employee(db, employee_request)
        return APIResponse(
            status_code=status.HTTP_201_CREATED,
            message="Employee created successfully",
            data=employee_response
        )
    except Exception as e:
        logger.error(f"Error adding employee: {e}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Failed to add employee: {e}"
        )

@router.get("/employees", response_model=APIResponse, status_code=status.HTTP_200_OK)
async def get_employees(db:Session=Depends(get_db)):
    try:
        return (
            APIResponse(status_code=status.HTTP_200_OK,
                        message="Employee Data Retrieved Successfully",
                        data= list_employees(db)
            )
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete("/employees/{employee_code}", status_code=status.HTTP_200_OK)
async def delete_employee_by_id(
    employee_code: str = Path(..., description="Employee code to delete"),
    db: Session = Depends(get_db)
):
    response = delete_employee(db, employee_code)
    return APIResponse(
        status_code=status.HTTP_200_OK,
        message="Employee deleted successfully",
        data=response
    )


@router.get("/stats/median-age", response_model=APIResponse)
async def get_median_age(db: Session = Depends(get_db)):
    try:
        response = calculate_median_age(db)
        return APIResponse(
            status_code=200,
            message="Median age calculated successfully",
            data=response
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))



@router.get("/stats/median-salary", response_model=APIResponse, status_code=status.HTTP_200_OK)
async def get_median_salary(db: Session = Depends(get_db)):
    try:
        response = calculate_median_salary(db)
        return APIResponse(
        status_code=status.HTTP_200_OK,
        message="Median salary calculated successfully",
        data=response
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))