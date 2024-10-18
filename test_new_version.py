
from tubemp3.api import search_music
from tubemp3.file import download

music = search_music("the landing")[0]

download(music)
