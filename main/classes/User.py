import sqlalchemy as db
from sqlalchemy.orm import relationship

from classes.Base import Base


class User(Base):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    user_token = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    tracks = relationship('Track', backref='user')