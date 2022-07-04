from sqlalchemy import Column, String, Timestamp
from database import Base 


class Route(Base):
  __tablename__ = 'route'
  route_id = Column(String(36), primary_key=True)
  title = Column(String(36), primary_key=True)
  content = Column(String(45))
  video = Column(String(45))

