from pydantic import BaseModel, Field, constr, EmailStr

class UserCreate(BaseModel):
    email: EmailStr
    username: str = Field(..., min_length=3)
    password: constr(min_length=6)
    confirm_password: constr(min_length=6)
