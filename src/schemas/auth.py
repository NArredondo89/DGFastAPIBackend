from pydantic import BaseModel, Field

class Credentials(BaseModel):
  email: str= Field(default="null")
  password: str= Field(default="null")
  fullname: str= Field(default="null")
  course_id: str= Field(default="null")
  is_course_admin: bool= Field(default="null")
  is_event_admin: bool= Field(default="null")
  access: list= Field(default=[])
  
  class Config:
    orm_mode = True
    
