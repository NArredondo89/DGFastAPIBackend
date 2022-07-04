from pydantic import BaseModel, Field
from typing import Optional 


class User(BaseModel):
  user_id: str 
  email: str
  password: str
  sign_up_date : str
  location: str
  home_course: str
  slogan: str

