from mutagen.easyid3 import EasyID3
from mutagen.id3 import ID3, APIC, error
from mutagen.mp3 import MP3

def save_metadata(file_path, title, artist, album, year, album_art_path):
    # Carrega o arquivo MP3
    audio = MP3(file_path, ID3=EasyID3)

    # Atualiza os metadados
    audio['title'] = title
    audio['artist'] = artist
    audio['album'] = album
    audio['date'] = year

    # Salva as alterações
    audio.save()

    # Adiciona a capa do álbum (thumbnail)
    audio = ID3(file_path)
    with open(album_art_path, 'rb') as album_art:
        audio['APIC'] = APIC(
            encoding=3,         # UTF-8
            mime='image/jpeg',  # MIME type do arquivo da imagem (pode ser 'image/png')
            type=3,             # 3 é a capa do álbum
            desc='Cover',
            data=album_art.read()
        )

    # Salva a capa e outras alterações
    print(f"saving metadata from `{file_path}...")
    audio.save(v2_version=3)

# Exemplo de uso

'''
file_path = 'music.mp3'
title = 'Song Title'
artist = 'Artist Name'
album = 'Album Name'
year = '2024'
album_art_path = 'cover.jpg'  # Imagem da capa do álbum

save_metadata(file_path, title, artist, album, year, album_art_path)
'''

