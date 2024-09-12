from sqlalchemy import (Column, String)
from src.module.database.db import Base

class Image(Base):
  __tablename__ = 'image'
  name = Column(String(255))
  path = Column(String(255))