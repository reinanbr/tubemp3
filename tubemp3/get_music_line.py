'''
[getmusic in line terminal]
   about:
      a easy method ofr getting music's without write a code
_______________________________
Reinan Br
'''


from tubemp3 import get_from_link as gfl
import sys

#name_music = sys.argv[1]
link_music = f"{sys.argv[1].replace('music.','').split('&si')[0]}" if ('music.' in sys.argv[1]) else sys.argv[1]
file_mp3 = sys.argv[2]
print(f"link: {link_music}")

def main():
   print(f"link: {link_music}")

   gfl(link_music).download_mp3(file_mp3)
