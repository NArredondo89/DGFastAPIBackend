from sqlalchemy import Column, String, Timestamp
from database import Base 


class Event(Base):
  __tablename__ = 'event'
  event_id = Column(String(36), primary_key=True)
  event_title = Column(String(45))
  event_photo = Column(String(45))
  small_event_description = Column(String(45))
  large_event_description = Column(String(45))
  tournament_director = Column(String(45))
  tournament_director_email = Column(String(45))
  tournament_director_phone = Column(String(45))
  label = Column(String(45))
  start_time = Column(String(45))
  day_of_week = Column(String(45))
  start_format = Column(String(45))
  play_format = Column(String(45))
  
  
