
from tubemp3 import get_from_link as gfl
import sys


link_music = f"{sys.argv[1].replace('music.','').split('&si')[0]}&si" if ('music.' in sys.argv[1]) else sys.argv[1]

print(f"link: {link_music}")