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
