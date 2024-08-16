from typing import Any, Optional
from pydantic import BaseModel


class GenericResponse(BaseModel):
    success: bool
    message: Optional[str] = None
    data: Optional[Any] = None


class GenericPaginatedResponse(BaseModel):
    success: bool
    message: Optional[str] = None
    data: Optional[Any] = None
    page: int
    page_size: int
    total_pages: int
    total_count: int
