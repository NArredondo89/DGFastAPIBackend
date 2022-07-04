from sqlalchemy import Column, String, TIMESTAMP

from database import Base 


class Review(Base):
  __tablename__ = 'review'
  review_id = Column(String(36), primary_key=True)
  review_description = Column(String(45))
  date_created= Column(TIMESTAMP)
