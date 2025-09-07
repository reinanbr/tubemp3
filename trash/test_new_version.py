
from tubemp3.api import search_music
from tubemp3.file import download

musics = search_music("danny elfman - responsibility theme suite (slowed + pitched) ~ Spider-Man 1, 2 & 3")

for music in musics:
    print("music info:",music)
    print('')

download(musics[0])