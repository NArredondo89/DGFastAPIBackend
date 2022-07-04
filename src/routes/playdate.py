from sqlalchemy import Column, String, TIMESTAMP

from database import Base 


class PlayDate(Base): 
  __tablename__ = 'playdate'
  playdate_id = Column(String(36), primary_key=True)
  comment = Column(String(45))
  date = Column(String(45))
  time = Column(String(45))

