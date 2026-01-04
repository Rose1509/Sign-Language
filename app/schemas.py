from pydantic import BaseModel, Field, constr

class UserCreate(BaseModel):
    full_name: str = Field(..., min_length=1)
    username: str = Field(..., min_length=3)
    password: constr(min_length=6)
    confirm_password: constr(min_length=6)
