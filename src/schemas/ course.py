from pydantic import BaseModel, Field
from typing import Optional 
import datetime


class Course(BaseModel):
  course_id: str
  course_name: str
  course_description: str
  condition: str
  location: str
  holes: str
  services: str
  year_establishe: str
  property: str
  tees: str
  availability: str
  targets: str
  parkphoto: str
  location_typ: str
  cit: str
  stree: str
  postal_cod: str
  state_province_nam: str
  countr: str
  basket_type: str
  tee_type: str
  fee: str
  
  
  class Config:
    orm_mode = True

class CreateCourse(BaseModel):
  course_name: str
  course_description: str
  condition: str
  location: str
  holes: str
  services: str
  year_establishe: str
  property: str
  tees: str
  availability: str
  targets: str
  parkphoto: str
  location_typ: str
  cit: str
  stree: str
  postal_cod: str
  state_province_nam: str
  countr: str
  basket_type: str
  tee_type: str
  fee: str

  class Config:
    orm_mode = True


class UpdateCourse(BaseModel):
  course_name: Optional[str] = Field(defaults="")
  course_description: Optional[str] = Field(defaults="")
  condition: Optional[str] = Field(defaults="")
  location: Optional[str] = Field(defaults="")
  holes: Optional[str] = Field(defaults="")
  services: Optional[str] = Field(defaults="")
  year_establishe: Optional[str] = Field(defaults="")
  property: Optional[str] = Field(defaults="")
  tees: Optional[str] = Field(defaults="")
  availability: Optional[str] = Field(defaults="")
  targets: Optional[str] = Field(defaults="")
  parkphoto: Optional[str] = Field(defaults="")
  location_typ: Optional[str] = Field(defaults="")
  cit: Optional[str] = Field(defaults="")
  stree: Optional[str] = Field(defaults="")
  postal_cod: Optional[str] = Field(defaults="")
  state_province_nam: Optional[str] = Field(defaults="")
  countr: Optional[str] = Field(defaults="")
  basket_type: Optional[str] = Field(defaults="")
  tee_type: Optional[str] = Field(defaults="")
  fee: Optional[str] = Field(defaults="")
  class Config:
    orm_mode = True
