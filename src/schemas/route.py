from pydantic import BaseModel, Field
from typing import Optional 
import datetime


class Route(BaseModel):
  route_id: str
  title: str
  content: str
  video: str
  class Config:
    orm_mode = True

class CreateRoute(BaseModel):
  title: str
  content: str
  video: str
  class Config:
    orm_mode = True


class UpdateRoute(BaseModel):
  title: Optional[str] = Field(defaults="")
  content: Optional[str] = Field(defaults="")
  video : Optional[str] = Field(defaults="")
  
  class Config:
    orm_mode = True
