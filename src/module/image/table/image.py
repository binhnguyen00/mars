from sqlalchemy import (Column, String)
from src.module.database.initial import Base

class Image(Base):
  __tablename__ = 'image'
  name = Column(String(255), nullable=False)
  path = Column(String(255), nullable=False)