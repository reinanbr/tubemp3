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
link_music,file_mp3 = sys.argv[1],sys.argv[2]
print(file_mp3)
def main():
   gfl(link_music).download_mp3(file_mp3)
