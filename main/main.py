import sqlalchemy as db
from fastapi import FastAPI
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm import Session
from yandex_music import Client

from classes.User import User
from classes.Track import Track
from classes.UserInput import UserInput

app = FastAPI()
engine = db.create_engine('postgresql://postgres:xm6idbip@localhost/postgres', echo=True)
metadata = db.MetaData()


@app.post('/user_input')
def get_data(user_input: UserInput):
    client = Client(user_input.user_token).init()

    try:
        users = db.Table('users', metadata,
                         db.Column('id', db.Integer, primary_key=True),
                         db.Column('user_token', db.String, primary_key=True),
                         db.Column('username', db.String))
    except InvalidRequestError:
        pass

    try:
        tracks = db.Table('tracks', metadata,
                          db.Column('id', db.Integer, primary_key=True),
                          db.Column('title', db.String),
                          db.Column('duration', db.Integer),
                          db.Column('artist_id', db.Integer),
                          db.Column('artist_name', db.String),
                          db.Column('album_id', db.Integer),
                          db.Column('album_title', db.String),
                          db.Column('album_genre', db.String),
                          db.Column('label_id', db.Integer),
                          db.Column('label_title', db.String))
    except InvalidRequestError:
        pass

    metadata.create_all(engine)

    with Session(autoflush=False, bind=engine) as session:

        track_list = client.usersLikesTracks().fetch_tracks()
        user_tracks = []

        for i in track_list:
            try:
                track = Track(
                    id=i.id,
                    title=i.title,
                    duration=i.duration_ms,
                    artist_id=i.artists,
                    artist_name=i.artists,
                    album_id=i.albums[0].id,
                    album_title=i.albums[0].title,
                    album_genre=i.albums[0].genre,
                    label_id=i.albums[0].labels[0].id,
                    label_title=i.albums[0].labels[0].name
                )
            except IndexError:
                track = Track(
                    id=i.id,
                    title=i.title,
                    duration=i.duration_ms,
                    artist_id=i.artists,
                    artist_name=i.artists,
                    album_id=None,
                    album_title=None,
                    album_genre=None,
                    label_id=None,
                    label_title=None
                )
            user_tracks.append(track)

        if not session.query(db.exists().where(User.id == client.me['account']['uid'])).scalar():
            user = User(
                id = client.me['account']['uid'],
                user_token = user_input.user_token,
                username = client.me['account']['login']
            )
            user.tracks = user_tracks

        else:
            user = session.query(User).filter_by(id = client.me['account']['uid']).one()
            user.tracks.extend(user_tracks)

        session.add(user)
        session.commit()
