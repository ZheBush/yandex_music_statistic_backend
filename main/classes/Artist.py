import sqlalchemy as db

from classes.Base import Base


class Artist(Base):
    __tablename__ = 'artists'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    number_of_this_artist = db.Column(db.Integer)
    cover = db.Column(db.String)

    # def __init__(self, name, cover):
    #     self.name = name
    #     self.cover = cover
