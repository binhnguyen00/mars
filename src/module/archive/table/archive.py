from sqlalchemy import (Column, String)
from src.module.database.db import Base

class Archive(Base):
  __tablename__ = 'archive'
  name = Column(String(255))
  path = Column(String(255))