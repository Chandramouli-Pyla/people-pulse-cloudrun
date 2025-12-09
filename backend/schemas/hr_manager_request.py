from pydantic import BaseModel, EmailStr, Field, ConfigDict
from typing import Optional
from datetime import date

class HRManagerRequest(BaseModel):
    first_name: str = Field(..., min_length=2, max_length=50)
    last_name: str = Field(..., min_length=2, max_length=50)
    email: EmailStr
    phone_number: Optional[str] = None

    # Address fields
    house_number: Optional[str] = None
    street: Optional[str] = None
    apartment: Optional[str] = None
    city: str = Field(..., min_length=2)
    state: str = Field(..., min_length=2)
    country: str = Field(..., min_length=2)
    zip_code: str = Field(..., regex=r'^\d{5}(-\d{4})?$')

    # Employee fields
    employee_code: str
    department: str
    position: str
    salary: Optional[float] = None
    date_of_joining: date

    # HR-specific fields
    can_approve_leaves: bool = True
    can_access_salary_data: bool = True

    model_config = ConfigDict(from_attributes=True)
