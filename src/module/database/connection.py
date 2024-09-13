from src.module.database.initial import db

def commit():
  db.session.commit()

def rollback():
  db.session.rollback()

def insert(obj):
  db.session.add(obj)
  commit()

def delete(obj):
  db.session.delete(obj)
  commit()