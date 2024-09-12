from src.module.database.initial import db

class DBConnectionUtils():

  def commit(self):
    db.session.commit()

  def rollback(self):
    db.session.rollback()

  def insert(self, obj):
    db.session.add(obj)
    self.commit()

  def delete(self, obj):
    db.session.delete(obj)
    self.commit()