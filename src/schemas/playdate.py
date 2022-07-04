from pydantic import BaseModel, Field
from typing import Optional 



class PlayDate(BaseModel): 
  playdate_id: str
  comment: str
  date: str
  time: str

  class Config:
    orm_mode = True

class CreatePlayDate(BaseModel):
  comment: str
  date: str
  time: str

  class Config:
    orm_mode = True


class UpdatePlayDate(BaseModel):
  comment: Optional[str] = Field(defaults="")
  date: Optional[str] = Field(defaults="")
  time: Optional[str] = Field(defaults="")
  class Config:
    orm_mode = True
