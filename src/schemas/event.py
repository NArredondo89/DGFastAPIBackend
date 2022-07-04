from pydantic import BaseModel, Field
from typing import Optional 
import datetime


class Event(BaseModel):
  event_id :str
  event_title:str
  event_photo:str
  small_event_description:str
  large_event_description:str
  tournament_director:str
  tournament_director_email:str
  tournament_director_phone:str
  label:str
  start_time:str
  day_of_week:str
  start_format:str
  play_format:str
  date_created: datetime.datetime
  
  
  class Config:
    orm_mode = True

class CreateEvent(BaseModel):
  event_title:str
  event_photo:str
  small_event_description:str
  large_event_description:str
  tournament_director:str
  tournament_director_email:str
  tournament_director_phone:str
  label:str
  start_time:str
  day_of_week:str
  start_format:str
  play_format:str
  date_created: datetime.datetime = datetime.datetime.now()
  

  class Config:
    orm_mode = True


class UpdateEvent(BaseModel):
  event_title: Optional[str] = Field(defaults="")
  event_photo: Optional[str] = Field(defaults="")
  small_event_description: Optional[str] = Field(defaults="")
  large_event_description: Optional[str] = Field(defaults="")
  tournament_director: Optional[str] = Field(defaults="")
  tournament_director_email: Optional[str] = Field(defaults="")
  tournament_director_phone: Optional[str] = Field(defaults="")
  label: Optional[str] = Field(defaults="")
  start_time: Optional[str] = Field(defaults="")
  day_of_week: Optional[str] = Field(defaults="")
  start_format: Optional[str] = Field(defaults="")
  play_format: Optional[str] = Field(defaults="")
  
  class Config:
    orm_mode = True

  
