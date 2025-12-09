from pydantic import BaseModel, ConfigDict
from typing import Any, Optional

class APIResponse(BaseModel):
    status_code: int
    message: str
    data: Optional[Any] = None

    model_config = ConfigDict(from_attributes=True)
