from pydantic import BaseModel, Field
from typing import Optional 
import datetime


class Review(BaseModel):
  review_id: str
  review_description: str
  review_timestamp: datetime.datetime
  class Config:
    orm_mode = True

class CreateReview(BaseModel):
  review_description: str
  review_timestamp: datetime.datetime

  class Config:
    orm_mode = True


class UpdateReview(BaseModel):
  review_description: Optional[str] = Field(defaults="")
  review_timestamp: Optional[str] = Field(defaults="")

  class Config:
    orm_mode = True
