from uuid import UUID

from pyarrow import string
from pydantic import BaseModel, EmailStr, computed_field, ConfigDict
from typing import Optional
from datetime import date

class EmployeeResponse(BaseModel):
    id: str
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

    # Employee-specific fields
    employee_code: str
    department: str
    position: str
    salary: Optional[float] = None
    date_of_joining: date
    date_of_birth: date

    @computed_field
    @property
    def age(self) -> int:
        today = date.today()
        dob = self.date_of_birth
        return today.year - dob.year - (
            (today.month, today.day) < (dob.month, dob.day)
        )

    # class Config:
    #     from_attributes = True
    model_config = ConfigDict(from_attributes=True)