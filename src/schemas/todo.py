from datetime import date
from typing import Optional

from pydantic import BaseModel, EmailStr, Field, field_validator


class ContactSchema(BaseModel):  # TodoSchema
    firstname: str = Field("default", min_length=3, max_length=15)
    lastname: str = Field(min_length=3, max_length=15)
    email: str = EmailStr
    phone: str = Field(min_length=3, max_length=25)
    birthday: Optional[date] = Field(None, description="The birthday date Day-Month-Year")
    completed: Optional[bool] = False


class ContactUpdateSchema(ContactSchema):
    completed: bool


class ContactResponse(BaseModel):
    id: int = 1
    firstname: str
    lastname: str
    email: str
    phone: str
    birthday: Optional[date]
    completed: bool

    class Config:
        from_attributes: True