
from tubemp3.api import search_music
from tubemp3.file import download

music = search_music("empinadinha wesley")
print("music info:",music)
download(music,'/sdcard/Alarms/empinadinha.mp3')
