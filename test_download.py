
from tubemp3.api import search_music
from tubemp3.file import download


query = "like a player wolverine deadpool chor"

music = search_music(query)[0]

download(music)
