from pydantic import BaseModel, Field
from typing import Optional 
import datetime


class Route(BaseModel):
  route_id: str
  title: str
  content: str
  video: str

