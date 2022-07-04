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
  
  
