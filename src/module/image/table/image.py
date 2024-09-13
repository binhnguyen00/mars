from sqlalchemy import (Column, String);
from src.module.database.initial import (Base, db);

class Image(Base):
  __tablename__ = 'image'
  name = Column(String(255), nullable=False, unique=True)
  upload_format = Column(String(10))
  result_format = Column(String(10))

  @classmethod
  def query_property(cls):
    return db.session.query(cls)

  @classmethod
  def get_by_name(cls, name: str):
    return cls.query_property().filter_by(name=name).first()