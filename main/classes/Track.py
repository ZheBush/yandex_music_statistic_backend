import sqlalchemy as db
from sqlalchemy.orm import relationship

from classes.Base import Base
from classes.User import User


class Track(Base):
    __tablename__ = 'tracks'

    id = db.Column(db.String, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    title = db.Column(db.String)
    duration = db.Column(db.Integer)
    artist_id = db.Column(db.String)
    artist_name = db.Column(db.String)
    album_id = db.Column(db.String)
    album_title = db.Column(db.String)
    album_genre = db.Column(db.String)
    label_id = db.Column(db.String)
    label_title = db.Column(db.String)