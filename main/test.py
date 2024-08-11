import sqlalchemy as db
from sqlalchemy.orm import Session
from yandex_music import Client, Account

from user_token import token

client = Client(token).init()
engine = db.create_engine('postgresql://postgres:xm6idbip@localhost/postgres', echo=True)

with Session(autoflush=False, bind=engine) as session:
    track = client.usersLikesTracks().fetch_tracks()[0]
    print(track)