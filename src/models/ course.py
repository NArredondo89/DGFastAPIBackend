from sqlalchemy import Column, String, Timestamp
from database import Base 


class Course(Base):
  __tablename__ = 'course'
  course_id = Column(String(36), primary_key=True)
  course_name = Column(String(45))
  course_description = Column(String(45))
  condition = Column(String(45))
  location = Column(String(45))
  holes = Column(String(45))
  services = Column(String(45))
  year_established: Column(String(45))
  property = Column(String(45))
  tees = Column(String(45))
  availability = Column(String(45))
  targets = Column(String(45))
  parkphoto = Column(String(45))
  location_type: Column(String(45))
  city: Column(String(45))
  street: Column(String(45))
  postal_code: Column(String(45))
  state_province_name: Column(String(45))
  country: Column(String(45))
  basket_types: Column(String(45))
  tee_types: Column(String(45))
  fees: Column(String(45))
