
from tubemp3.api import get_info_link as gil
from tubemp3.file import download

music = gil('https://music.youtube.com/watch?v=yspAcpXEzSM&si=gKIVwPIQ-tbQjKQ_')
download(music)
