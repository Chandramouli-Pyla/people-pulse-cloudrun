from pydantic import BaseModel, EmailStr, ConfigDict
from typing import Optional

class PersonResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: EmailStr
    phone_number: Optional[str] = None
    house_number: Optional[str] = None
    street: Optional[str] = None
    apartment: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    country: Optional[str] = None
    zip_code: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)
