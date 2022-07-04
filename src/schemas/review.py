from pydantic import BaseModel, Field
from typing import Optional 
import datetime


class Review(BaseModel):
  review_id: str
  review_description: str
  date_created: datetime.datetime
  class Config:
    orm_mode = True

class CreateReview(BaseModel):
  review_description: str
  date_created: datetime.datetime = datetime.datetime.now()

  class Config:
    orm_mode = True


class UpdateReview(BaseModel):
  review_description: Optional[str] = Field(defaults="")

  class Config:
    orm_mode = True
