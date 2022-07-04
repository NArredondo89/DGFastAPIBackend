from sqlalchemy import Column, String, TIMESTAMP
from database import Base 


class Hole(Base):
  __tablename__ = 'hole'
  hole_id = Column(String(36), primary_key=True)
  number = Column(String(45))
  par = Column(String(45))
  feet = Column(String(45))
  mandatory = Column(String(45))
  double_mandatory = Column(String(45))
  out_of_bounds = Column(String(45))
  hazzard = Column(String(45))
  drop_zone= Column(String(45))
  date_created= Column(TIMESTAMP)