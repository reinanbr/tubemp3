'''
[getmusic in line terminal]
   about:
      a easy method ofr getting music's without write a code
_______________________________
Reinan Br
'''

from tubemp3.getmusic import getmusic as gm
import sys

name_music = sys.argv[1]
def main():
   gm(name_music)
