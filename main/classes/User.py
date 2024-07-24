import sqlalchemy as db
from classes.Base import Base

class User(Base):
    __tablename__ = 'users'

    token = db.Column(db.Integer, primary_key = True)
