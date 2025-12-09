from pydantic import BaseModel, EmailStr, ConfigDict


class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    is_active: bool
    is_admin: bool

    model_config = ConfigDict(from_attributes=True)
