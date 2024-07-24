from yandex_music import Client
from classes.Artist import Artist
from classes.Album import Album

# import matplotlib.pyplot as plt

client = Client('y0_AgAAAABiTbtqAAG8XgAAAAEK5rh7AADaPWHW4hlOAZTqiIQ1rVb6h7hQtw').init()


# top_artists = {}
# top_albums = {}
# top_genres = {}

def get_artists():
    artist_list = []
    for i in client.usersLikesTracks():
        if not (i.fetch_track() in artist_list):
            artist_list.append(i.fetch_track())

    return artist_list


print(get_artists())

    # for i in track_list:
    #     if not (i.name in top_artists):
    #         top_artists[i.name] = 1
    #     else:
    #         top_artists[i.name] += 1
    #
    # for i in album_list:
    #     if not (i.genre in top_genres):
    #         top_genres[i.genre] = 1
    #     else:
    #         top_genres[i.genre] += 1
    #
    #     if not (i.title in top_albums):
    #         top_albums[i.title] = 1
    #     else:
    #         top_albums[i.title] += 1
    #
    # top_albums = dict(sorted(top_albums.items(), key = lambda item: item[1]))
    # top_genres = dict(sorted(top_genres.items(), key = lambda item: item[1]))
    # top_artists = dict(sorted(top_artists.items(), key = lambda item: item[1]))
    #
    #
    # fig, ax = plt.subplots(figsize = (12, 4))
    #
    # plt.barh(
    #     list(top_albums.keys()),
    #     list(top_albums.values()),
    #     height = 0.7,
    #     # padding = 3
    # )
    #
    # plt.show()
