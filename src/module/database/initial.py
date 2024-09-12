from flask_sqlalchemy import SQLAlchemy;
from sqlalchemy import (Column, DateTime, Integer, func);
from sqlalchemy.orm import DeclarativeBase;
from src.module.server.initial import server;

class BaseMixin:
  __abstract__ = True
  id = Column(Integer, primary_key=True, autoincrement=True)
  created_time = Column(DateTime, default=func.now())
  modified_time = Column(DateTime, default=func.now(), onupdate=func.now())  # Automatically update when modified

class Base(DeclarativeBase, BaseMixin):
  pass

db = SQLAlchemy(model_class=Base, app=server)