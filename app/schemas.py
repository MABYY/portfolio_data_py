from pydantic import BaseModel, EmailStr
from typing import Optional

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class FundCreate(BaseModel):
    Api: int
    Nombre_Fondo : str
    Fecha: str

class FundSelect(BaseModel):   
    Nombre_Fondo : str
    Fecha: str

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[str] = None