from pydantic import BaseModel, EmailStr, Field, ConfigDict
from typing import Optional

class PersonRequest(BaseModel):
    first_name: str = Field(..., min_length=2, max_length=50)
    last_name: str = Field(..., min_length=2, max_length=50)
    email: EmailStr
    phone_number: str = Field(...,pattern=r'^\+?\d{10,15}$')
    house_number: Optional[str] = None
    street: Optional[str] = None
    apartment: Optional[str] = None
    city: str = Field(..., min_length=2)
    state: str = Field(..., min_length=2)
    country: str = Field(..., min_length=2)
    zip_code: str = Field(..., pattern=r'^\d{5}(-\d{4})?$')

    model_config = ConfigDict(from_attributes=True)
