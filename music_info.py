from tubemp3.api import search_music

query = "segunda opcao"
musics = search_music(query)


if type(musics) == list:
    for n,music in enumerate(musics):
        print(f'\nmusic {n}:')
        for key,value in music.items():
                print(f'{key}: {value}')
else:
    for key,value in musics.items():
        print(f'"{key}": "{value}"')
