from fastapi import APIRouter, Depends, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from database import get_db
from hashing import Hash
import uuid