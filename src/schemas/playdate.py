from pydantic import BaseModel, Field
from typing import Optional 
import datetime



class PlayDate(BaseModel): 
  playdate_id: str
  comment: str
  date_created: datetime.datetime
  

  class Config:
    orm_mode = True

class CreatePlayDate(BaseModel):
  comment: str
  date_created: datetime.datetime = datetime.datetime.now()

  class Config:
    orm_mode = True


class UpdatePlayDate(BaseModel):
  comment: Optional[str] = Field(defaults="")

  class Config:
    orm_mode = True
