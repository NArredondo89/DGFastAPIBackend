from pydantic import BaseModel, Field
from typing import Optional 
import datetime


class Review(BaseModel):
  review_id: str
  review_description: str
  review_timestamp: datetime.datetime
