
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')

from tubemp3 import get_info_link as gil
from tubemp3.file import download


def test_get_link():
     music = gil('https://music.youtube.com/watch?v=yspAcpXEzSM&si=gKIVwPIQ-tbQjKQ_')
     print(music)