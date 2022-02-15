'''
[getmusic]
    about:
        This work is for getting music's from YouTube.with name or with link. 
        It can get music in high quality, and get just details from music.
        It use for getting link and information from music the youtube.dl

    because:
        for download music in one easy way.

    License:
        MIT License

        Copyright (c) 2021 Reinan Br.

        Permission is hereby granted, free of charge, to any person obtaining a copy
        of this software and associated documentation files (the "Software"), to deal
        in the Software without restriction, including without limitation the rights
        to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
        copies of the Software, and to permit persons to whom the Software is
        furnished to do so, subject to the following conditions:

        The above copyright notice and this permission notice shall be included in all
        copies or substantial portions of the Software.

        THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
        IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
        FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
        AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
        LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
        OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
        SOFTWARE.


____________________________________________________________________________________

date_init: 27 dec 2021 03:18
Author: Reinan Br slimchatuba@gmail.com
'''

from .lib import search_ytdl as sy
#from __future__ import unicode_literals
import stagger
import eyed3
from eyed3.id3.frames import ImageFrame
import requests as rq
import os
import youtube_dl

##the show is start
def getmusic(name_music:str,path_dir:str='music',path_music:str=False,
             pref_quality:int=320):
    ydl_opts = {
       'outtmpl': f'{path_dir}/{path_music}.%(ext)s',
           'format': 'bestaudio/best',
            'noplaylist':'True',
           'postprocessors': [{
               'key': 'FFmpegExtractAudio',
               'preferredcodec': 'mp3',
               'preferredquality': f'{pref_quality}',
      }],
   }
    
    #getting the info from video founded in search from youtube.dl
    video=sy(name_music,ytdl_client=ydl_opts)
    
    url_music = video['url']
    url_thumbnail = video['thumbnail']
    channel=video.get('channel','Unknown')
    artist=video.get('artist',channel)
    title=video['title']
    duration=video['duration']
    id_video=video['id']
    link_yt=f'youtube.com/watch?v={id_video}'
    album=video.get('album','Unknowm')
    track=video.get('track',None)
    year=video.get('upload_date',None)[:4]
    
    assert duration < 600, print(f'ops! Music dont permition size download: [Duration: {duration}s]')
    
    time_min = int(duration//60)
    time_sec = int(duration%60)
    print(f'music: \ntitle:{title}\nduration:{time_min}:{time_sec}\nartist:{artist}\nid:{id_video}\nalbum:{album}\nyear:{year}')
    # getting the content music
    
    #verification that the pastmusic exists
    if not os.path.isdir(path_dir):
        os.mkdir(path_dir)
    else:
        pass
    #editing the name from pathfilemusic
    path_file = '_'.join(title.split(' '))
    path_file = '_'.join(path_file.split('('))
    path_file = '_'.join(path_file.split(')'))
    path_file = '_'.join(path_file.split('&'))
    path_file = '_'.join(path_file.split('"'))
    path_file = '_'.join(path_file.split("'"))
    path_file = '_'.join(path_file.split(':'))
    path_file = '_'.join(path_file.split('/'))
    path_file = '_'.join(path_file.split('-'))

    if path_music:
        path_music = f'{path_dir}/{path_file}'
        print('if',path_music)
    else:
        path_music = '_'.join(title.split(' '))
        path_music = f'{path_dir}/{path_file}'
        print('else',path_music)

    # making the download from music file
    ydl_opts = {
       'outtmpl': f'{path_music}.%(ext)s',
           'format': 'bestaudio/best',
           'postprocessors': [{
               'key': 'FFmpegExtractAudio',
               'preferredcodec': 'mp3',
               'preferredquality': f'{pref_quality}',
      }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
       ydl.download([link_yt])
   
    path_music=f'{path_music}.mp3'
    path_thumb = f'{path_dir}/{path_file}.png'
    thumb_content = rq.get(url_thumbnail).content
    with open(path_thumb,'wb') as file_thumb:
        file_thumb.write(thumb_content)
    
    
    mp3 = stagger.read_tag(path_music)
    mp3.artist = artist
    mp3.song = title
    mp3.title = track
    mp3.album=album
    #mp3.picture = path_thumb
    mp3.write()

    audiofile = eyed3.load(path_music)
    if (audiofile.tag == None):
        audiofile.initTag()

    audiofile.tag.images.set(ImageFrame.FRONT_COVER, open(
    path_thumb, 'rb').read(), 'image/jpeg')
    audiofile.tag.save()
    os.system(f'rm {path_thumb}')
    
    return path_music
