from pydantic import BaseModel, EmailStr, Field, ConfigDict
from typing import Optional
from datetime import date


class EmployeeRequest(BaseModel):
    # Person fields
    first_name: str = Field(..., min_length=3, max_length=50)
    last_name: str = Field(..., min_length=2, max_length=50)
    email: EmailStr
    phone_number: Optional[str] = Field(None, pattern=r'^\+?\d{10,15}$')
    house_number: Optional[str] = None
    street: Optional[str] = None
    apartment: Optional[str] = None
    city: str = Field(..., min_length=2)
    state: str = Field(..., min_length=2)
    country: str = Field(..., min_length=2)
    zip_code: str = Field(..., pattern=r'^\d{5}(-\d{4})?$')

    # Employee-specific fields
    employee_code: str = Field(..., pattern=r'^FD\d{5}$', description="Format: FD followed by 5 digits")
    department: str = Field(..., min_length=2)
    position: str = Field(..., min_length=2)
    salary: Optional[float] = Field(None, ge=0, le=150000)  # salary cannot be negative
    date_of_birth: date = Field(...)
    date_of_joining: date = Field(...)  # required field

    model_config = ConfigDict(from_attributes=True)
