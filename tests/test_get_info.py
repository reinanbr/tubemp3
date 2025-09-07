
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')

from tubemp3 import search_music
from tubemp3  import get_info_link
from kitano import puts

def test_get_info_music():
    query = "like a player wolverine deadpool chor"
    musics = search_music(query)
    puts('--- Music Search Results ---')
    puts(musics)
    puts('--- End of Search Results ---')
    assert len(musics) > 0
    puts(f"Total musics found: {len(musics)}")

    if musics:
        music = musics[0]
        puts('--- Getting Info for First Music ---')
        info = get_info_link(music.url)
        puts('--- Music Info ---')
        puts(info)
