from pydantic import BaseModel, Field


class CreateUserRequest(BaseModel):
    name: str = Field(..., description="Name")
    password: str = Field(..., description="Password")
