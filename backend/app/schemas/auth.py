from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class TokenSchema(BaseModel):
    access_token: str
    token_type: str = "bearer"


class TokenData(BaseModel):
    sub: Optional[str] = None
    type: Optional[str] = None


class LoginSchema(BaseModel):
    username: str
    password: str
