from sqlalchemy import Column, String, Timestamp
from database import Base 


class User(Base):
  __tablename__ = 'user'
  user_id = Column(String(36), primary_key=True)
  email = Column(String(45))
  password = Column(String(45))
  sign_up_date = Timestamp(String(45))
  location = Column(String(45))

