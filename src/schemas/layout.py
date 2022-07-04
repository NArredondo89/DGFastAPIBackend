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


