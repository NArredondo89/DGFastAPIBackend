from pydantic import BaseModel, Field
from typing import Optional
import datetime


class User(BaseModel):
  user_id: str 
  email: str
  password: str
  sign_up_date : datetime.datetime
  home_course: str
  slogan: str

  class Config:
    orm_mode = True

class CreateUser(BaseModel):
  email: str
  password: str
  sign_up_date : datetime.datetime = datetime.datetime.now()
  location: str
  home_course: str
  slogan: str

  class Config:
    orm_mode = True

class UpdateUser(BaseModel):
  email: Optional[str] = Field(defaults="")
  password: Optional[str] = Field(defaults="")
  sign_up_date : Optional[str] = Field(defaults="")
  location: Optional[str] = Field(defaults="")
  home_course: Optional[str] = Field(defaults="")
  slogan: Optional[str] = Field(defaults="")

  class Config:
    orm_mode = True
    
class UserCredentials:
  email: str
  password: Optional[str]
  class Config:
    orm_mode = True


class ReturnUser(User):
  course_name: str