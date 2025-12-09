from pydantic import BaseModel, EmailStr, Field, ConfigDict


class UserRequest(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr
    password: str = Field(..., min_length=6)  # raw password input

    model_config = ConfigDict(from_attributes=True)
