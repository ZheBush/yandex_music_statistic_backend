import sqlalchemy as db

from token import token
from sqlalchemy import exists
from sqlalchemy.orm import Session
from yandex_music import Client

from classes.Album import Album
from classes.Artist import Artist

engine = db.create_engine('postgresql://postgres:xm6idbip@localhost/postgres', echo=True)
metadata = db.MetaData()
client = Client(token).init()
# conn = engine.connect()
#
# conn.execute(
#     db.Table('artists', metadata, autoload = True, autoload_with  = engine).delete()
# )
# conn.execute(
#     db.Table('albums', metadata, autoload = True, autoload_with = engine).delete()
# )
# conn.close()

artists = db.Table('artists', metadata,
                   db.Column('id', db.Integer, primary_key = True),
                   db.Column('name', db.String),
                   db.Column('number_of_this_artist', db.Integer),
                   db.Column('cover', db.String))

albums = db.Table('albums', metadata,
                  db.Column('id', db.Integer, primary_key = True),
                  db.Column('title', db.String),
                  db.Column('number_of_this_album', db.Integer),
                  db.Column('genre', db.String),
                  db.Column('cover', db.String),
                  db.Column('year', db.String))

metadata.create_all(engine)

with Session(autoflush = False, bind = engine) as session:

    track_list = client.usersLikesTracks().fetch_tracks()

    for i in track_list:
        artist_list = i.artists_name()
        for j in range(len(artist_list)):
            if not session.query(exists().where(Artist.name == artist_list[j])).scalar():
                try:
                    one_artist = Artist(
                        id = i.artists[j].id,
                        name = artist_list[j],
                        number_of_this_artist = 1,
                        cover = i.artists[j].cover.uri
                    )
                except AttributeError:
                    one_artist = Artist(
                        name = artist_list[j],
                        number_of_this_artist = 1,
                        cover = 'None'
                    )
            else:
                one_artist = session.query(Artist).filter_by(name = artist_list[j]).one()
                one_artist.number_of_this_artist += 1

            session.add(one_artist)

        try:
            if not session.query(exists().where(Album.id == i.albums[0].id)).scalar():
                one_album = Album(
                    id = i.albums[0].id,
                    title = i.albums[0].title,
                    number_of_this_album = 1,
                    genre = i.albums[0].genre,
                    cover = i.albums[0].cover_uri,
                    year = i.albums[0].year
                )
            else:
                one_album = session.query(Album).filter_by(id = i.albums[0].id).one()
                one_album.number_of_this_album += 1
        except IndexError:
            if not session.query(exists().where(Album.title == "None")).scalar():
                one_album = Album(
                    title = 'None',
                    number_of_this_album = 1,
                    genre = 'None',
                    cover = 'None',
                    year = 0
                )
            else:
                one_album = session.query(Album).filter_by(title = 'None').one()
                one_album.number_of_this_album += 1

        session.add(one_album)
        session.commit()