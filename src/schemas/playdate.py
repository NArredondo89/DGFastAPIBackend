from pydantic import BaseModel, Field
from typing import Optional 



class PlayDate(BaseModel): 
  playdate_id: str
  comment: str
  date: str
  time: str

