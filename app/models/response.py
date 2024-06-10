from typing import Any, Optional, List
from pydantic import BaseModel


class GenericResponse(BaseModel):
    success: bool
    message: Optional[str] = None
    data: Optional[Any] = None
