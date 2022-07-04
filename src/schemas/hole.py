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
  drop_zon:str
  