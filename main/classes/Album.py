import sqlalchemy as db

from classes.Base import Base


class Album(Base):
    __tablename__ = 'albums'

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String)
    number_of_this_album = db.Column(db.Integer)
    genre = db.Column(db.String)
    cover = db.Column(db.String)
    year = db.Column(db.Integer)

    # def __init__(self, title, genre, cover, year):
    #     self.title = title
    #     self.genre = genre
    #     self.cover = cover
    #     self.year = year