from __future__ import unicode_literals
from ast import Return
import os
from unittest import result
import youtube_dl
from googlesearch import search
from requests import get

import stagger
import eyed3
from eyed3.id3.frames import ImageFrame


ydlt = youtube_dl.YoutubeDL({'outtmpl': '%(id)s.%(ext)s'})

ydtl_opt={'format': 'bestaudio', 'noplaylist':'True'}

##search youtube##
def search_ytdl(arg):
    with youtube_dl.YoutubeDL(ydtl_opt) as ydl:
        try:
            get(arg) 
        except:
            videos = ydl.extract_info(f"ytsearch:{arg}", download=False)['entries'][0]
        else:
            videos = ydl.extract_info(arg, download=False)
    if len(videos)>1:
        return videos
    else:
        videos = videos[0]
        video = {}
        video['title'] = videos.get('title',None)
        video['duration'] = videos.get('duration',None)
        video['url'] = videos.get('url',None)
        video['thumbnail'] = videos.get('thumbnail',None)
        return video

#search for musics from youtube
def search_google_yt(q:str,pesq_size=100):
    '''
    about:
    This function is for search on google.com for the name
    from music/video in that you writing on the param "q".
    Using it, you can search for music/video as "Making Love Out of Nothing", from AirSuply
    ...
    Atrr
    q: str
      => name from music/video youtube for search
    pesq_size: int => number of searchs for try
    '''
     # ydl_opts =  {'ottmpl': 'music.%(ext)s','postprocessors': [{'key': 'FFmpegExtractAudio','preferredcodec': 'mp3','preferredquality': '192'}]} 
    search_q = f'{q} hq music site:youtube.com'
    results_term = search(q,num_results=pesq_size)
    results_term = [i for i in results_term if 'youtube' in i]
    assert len(results_term)>0, 'not founded music/video from youtube'
    results = []
    s=0
    for i in results_term:
        result = ydlt.extract_info(i,download=False)
        if 'entries' in result:
            # Can be a playlist or a list of videos
            video = result['entries'][0]
        else:
            # Just a video
            video = result
        #results.append(video)
        title = video.get('title',None)
        url = video.get('url',None)
        duration = video.get('duration',None)
        url_thumb = video.get('thumbnail',None)
        result={}
        result['is_search']=True
        result['title']=title
        result['duration']=duration
        result['url']=url
        result['thumbnail']=url_thumb
        result['link_g']=i
        result['q']=q
        
        results.append(result)
        #print(title,duration)
        #print(video)
        s+=1
    #print(results_term)
    
    #link_result = results_term[0]
    return results


#for downloader audio from your video searched
def music_from_video_s(video,path_file:str='',path_dir:str='mp3',download=True):
    '''
    About:
    This function is a downloader audio in mp3 type
    from video searched on 'search_google_yt' result.
    This can download with title video, or using the term
    'q' used im your search.
    ...
    Obs:
    this work power is only for result search from function
    'search_google_yt', because on this work we need from
    link and title from video.
    ...
    Attr
    _____
    video :dict
      => video dict result from 'search_google_yt' search list
    path_file :str
      => path for name of file for download
    path_dir :str
      => path for directory for download
    ...
    Response: 
      {'link':(link from video founded on googleSearch :str),
      {'path':(path from your download :str)
    '''
    if type(video)==dict:
      assert 'is_search' in list(video.keys()), 'this dict_video is not from the "search_google_yt" function'
    if os.path.isdir(path_dir):
        pass
    else:
        os.mkdir(path_dir)
    
    if path_file=='':
        path_file = '_'.join(video['q'].split(' '))
    
    ydl_opts = {
    'outtmpl': f'{path_dir}/{path_file}.%(ext)s',
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        }
    if download:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video['link_g']])
            
    
    return {'link':video['link_g'],
            'path':f'{path_dir}/{path_file}'
            }


#principal function form fanatics of musics Youtube
#function for download audio/music from linkVideo
def music_from_link(link,path_dir='mp3',
                    path_file=None,
                    pref_quality=256,
                    pref_decodec='mp3'
):
   '''
    About:
    This work is for downloader music's from link present's 
    in the site Youtube only, the download is in mp3 (RECOMMENDED IS MP3) format.
    Using this power, you can download music's as 'Jane',
    from 'Desejo de Menina' or 'Kang the Conquerator - Theme'.
    ...
    Note:
      We too will config the tags from your music,
      adding artist, title song, picture, 
    ...
    Obs:
    Only links from video/music
    ...
    Attr
    ______
    link :str 
      => link from video/music from YouTube site
    path_dir :str
      => path from directory for download your music.
    If this path don't exists, we will creat and make the downloader.
    path_file :str
      => name for your download. If you don't
    config it, your namefile download will be the title from video/music present on YouTube.
    pref_quality :int
      => size quality from your audio in download,
      (recommended is 192)
    pref_decodec :str
      => type/format that your file will save on path_dir
      (RECOMMENDED IS 'mp3')
    ...
    Response:
      {'path': (path from your download :str)}
   '''
   
   if os.path.isdir(path_dir):
      pass
   else:
      os.mkdir(path_dir)
   
   dir_data = f'{path_dir}/.data'
   if os.path.isdir(dir_data):
      pass
   else:
      os.mkdir(dir_data)
      
   if path_file:
      pass
   else:
       video = ydlt.extract_info(link,download=False)
       title = video.get('title',None)
       channel = video.get('channel',None)
       thumbnail_url = video.get('thumbnail',None)
       
       #saving the thumbnail for making the image album
       
       print(channel)
       path_file = '_'.join(f'{title}_{channel}'.split(' '))
       content_thumb = get(thumbnail_url).content
       path_thumb=f'{dir_data}/{path_file}.png'
       
       with open(path_thumb,'wb') as file_thumb:
          file_thumb.write(content_thumb)
      
   path_music = f'{path_dir}/{path_file}.mp3'
     #options specials for work from youtube_dl in present work
   ydl_opts = {
       'outtmpl': f'{path_dir}/{path_file}.%(ext)s',
           'format': 'bestaudio/best',
           'postprocessors': [{
               'key': 'FFmpegExtractAudio',
               'preferredcodec': pref_decodec,
               'preferredquality': f'{pref_quality}',
      }],
   }
   
   #making the your download
   with youtube_dl.YoutubeDL(ydl_opts) as ydl:
       ydl.download([link])
   
   mp3 = stagger.read_tag(path_music)
   mp3.artist = channel
   mp3.song = title
   mp3.title = title
   #mp3.picture = path_thumb
   mp3.write()

   audiofile = eyed3.load(path_music)
   if (audiofile.tag == None):
       audiofile.initTag()

   audiofile.tag.images.set(ImageFrame.FRONT_COVER, open(
       path_thumb, 'rb').read(), 'image/jpeg')
   audiofile.tag.save()

   return {'path': f'{path_dir}/{path_file}.mp3'}
   


  
  
  
#get_music_yt('clubbed of death')
#print(get_music_yt('telephone'))
