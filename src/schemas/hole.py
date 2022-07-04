from pydantic import BaseModel, Field
from typing import Optional 
import datetime

class Hole(BaseModel):
  hole_id:str
  number:str
  par:str
  feet:str
  mandatory:str
  double_mandatory:str
  out_of_bounds:str
  hazzard:str
  drop_zone:str
  date_created: datetime.datetime
  
  class Config:
    orm_mode = True

class CreateHole(BaseModel):
  number:str
  par:str
  feet:str
  mandatory:str
  double_mandatory:str
  out_of_bounds:str
  hazzard:str
  drop_zone:str
  date_created: datetime.datetime = datetime.datetime.now()
  

  class Config:
    orm_mode = True


class UpdateHole(BaseModel):
  number:Optional[str] = Field(defaults="")
  par:Optional[str] = Field(defaults="")
  feet:Optional[str] = Field(defaults="")
  mandatory:Optional[str] = Field(defaults="")
  double_mandatory:Optional[str] = Field(defaults="")
  out_of_bounds:Optional[str] = Field(defaults="")
  hazzard:Optional[str] = Field(defaults="")
  drop_zone:Optional[str] = Field(defaults="")

  class Config:
    orm_mode = True

  