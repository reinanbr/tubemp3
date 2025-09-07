import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')
from tubemp3 import search_music
from tubemp3.file import download

def test_download():
    query = "the landing first man"
    music = search_music(query)[0]
    download(music,path='landing.mp3')
    assert os.path.exists('landing.mp3')
# music = search_music("like a player wolverine deadpool chor")[0]



