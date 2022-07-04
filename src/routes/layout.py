from sqlalchemy import Column, String, TIMESTAMP

from database import Base 


class Layout(Base):
  __tablename__ = 'layout'
  layoutID = Column(String(36), primary_key=True)
  layout_title = Column(String(45))
  total_holes = Column(String(45))
  total_par = Column(String(45))
  total_feet = Column(String(45))
  layout_information = Column(String(45))
  hazzard = Column(String(45))
  out_of_bounds = Column(String(45))


