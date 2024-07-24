import yandex_music

client = yandex_music.Client('y0_AgAAAABEFw_SAAG8XgAAAADuNm8liYO1L9GcSr-M24xZsMj81t5iq-Y').init()

for i in client.usersLikesTracks():
    print(i.fetch_track().artists_name())