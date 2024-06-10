from pydantic import BaseModel


class UserModelIn(BaseModel):
    email: str
    password: str


class UserModelOut(BaseModel):
    id: int
    email: str
    password: str
