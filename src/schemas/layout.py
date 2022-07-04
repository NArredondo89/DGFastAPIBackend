from pydantic import BaseModel, Field
from typing import Optional 
import datetime


class Layout(BaseModel):
  layout_id: str
  layout_title: str
  total_holes: str
  total_par: str
  total_feet: str
  layout_information: str
  hazzard: str
  out_of_bounds: str
  date_created: datetime.datetime
  

  class Config:
    orm_mode = True

class CreateLayout(BaseModel):
  layout_title: str
  total_holes: str
  total_par: str
  total_feet: str
  layout_information: str
  hazzard: str
  out_of_bounds: str
  date_created: datetime.datetime = datetime.datetime.now()
  

  class Config:
    orm_mode = True


class UpdateLayout(BaseModel):
  layout_title: Optional[str] = Field(defaults="")
  total_holes: Optional[str] = Field(defaults="")
  total_par: Optional[str] = Field(defaults="")
  commtotal_feetent: Optional[str] = Field(defaults="")
  layout_information: Optional[str] = Field(defaults="")
  hazzard: Optional[str] = Field(defaults="")
  out_of_bounds: Optional[str] = Field(defaults="")

  class Config:
    orm_mode = True
