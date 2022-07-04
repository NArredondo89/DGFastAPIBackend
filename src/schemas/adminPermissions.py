from pydantic import BaseModel, Field
from typing import Optional 
import datetime


class AdminPermission(BaseModel):
  permission_id:str
  event_id: str
  course_id:str
  permission:bool
  date_created: datetime.datetime 

  class Config:
    orm_mode = True

class CreateAdminPermission(BaseModel):
  event_id: str
  course_id:str
  permission:bool
  date_created: datetime.datetime 

  class Config:
    orm_mode = True


class UpdateAdminPermission(BaseModel):
  event_id: Optional[str] = Field(defaults="")
  course_id: Optional[str] = Field(defaults="")
  permission: Optional[bool] = Field(defaults="")

  
  class Config:
    orm_mode = True

class ReturnAdminPermissions(AdminPermission):
  course_name: str
  event_name:str
  user_id: str