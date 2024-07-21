from sqlalchemy import (
    Column, Integer, Float, String, DateTime, Boolean
)
from sqlalchemy.dialects.postgresql import JSONB

from database import Base

class User(Base):
    __tablename__ = 'user'
    id =
    name =
    login =
    password =
