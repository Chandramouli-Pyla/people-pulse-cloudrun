from pydantic import BaseModel, EmailStr, ConfigDict
from typing import Optional
from datetime import date

class HRManagerResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: EmailStr
    phone_number: Optional[str] = None

    # Address fields
    house_number: Optional[str] = None
    street: Optional[str] = None
    apartment: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    country: Optional[str] = None
    zip_code: Optional[str] = None

    # Employee fields
    employee_code: str
    department: str
    position: str
    salary: Optional[float] = None
    date_of_joining: date

    # HR-specific fields
    can_approve_leaves: bool
    can_access_salary_data: bool

    model_config = ConfigDict(from_attributes=True)
