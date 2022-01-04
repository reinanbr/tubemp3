from __future__ import unicode_literals
from ast import Return
import os
from unittest import result
import youtube_dl
#from googlesearch import search # in now moment, we dont need form it....
from requests import get

ydlt = youtube_dl.YoutubeDL({'outtmpl': '%(id)s.%(ext)s'})

ydtl_opt={'format': 'bestaudio', 'noplaylist':'True'}
##search youtube##
def search_ytdl(arg,ytdl_client=False):
    dtl_opt={'format': 'bestaudio', 'noplaylist':'True'}
    
    ydtl_opt = ytdl_client if (ytdl_client) else dtl_opt
    arg = arg+' hq music'
    with youtube_dl.YoutubeDL(ydtl_opt) as ydl:
        try:
            get(arg) 
        except:
            videos = ydl.extract_info(f"ytsearch:{arg}", download=False)['entries'][0]
            #videos = ydl.extract_info(arg, download=False)
            #print(videos)
        else:
            videos = ydl.extract_info(arg, download=False)
            
    if len(videos)>1:
        print(1)
        return videos
    else:
        videos = videos[0]
        print(videos)
        video = {}
        video['title'] = videos.get('title',None)
        video['duration'] = videos.get('duration',None)
        video['url'] = videos.get('url',None)
        video['channel']=videos.get('channel',None)
        video['thumbnail'] = videos.get('thumbnail',None)
        video['id'] = videos.get('id',None)
        video['year'] = videos.get('year',None)
        video['date'] = videos.get('date',None)
        video['album'] = videos.get('album',None)
        return video

## in now moment, we dont need from it function... ##
# def search_gyt(q:str,pesq_size=100):
#    # ydl_opts =  {'ottmpl': 'music.%(ext)s','postprocessors': [{'key': 'FFmpegExtractAudio','preferredcodec': 'mp3','preferredquality': '192'}]} 
    
    
    
#     search_q = f'music {q} site:youtube.com'
#     results_term = search(q,num_results=pesq_size)
#     results_term = [i for i in results_term if 'youtube' in i]
#     assert len(results_term)>0, 'not founded music from youtube'
#     results = []
#     s=0
#     for i in results_term:
#         result = ydlt.extract_info(i,download=False)
#         if 'entries' in result:
#             # Can be a playlist or a list of videos
#             video = result['entries'][0]
#         else:
#             # Just a video
#             video = result
#         #results.append(video)
#         title = video.get('title',None)
#         url = video.get('url',None)
#         duration = video.get('duration',None)
#         channel = video.get('channel',None)
#         url_thumb = video.get('thumbnail',None)
#         result={}
#         result['title']=title
#         result['duration']=duration
#         result['url']=url
#         result['thumbnail']=url_thumb
#         result['link_g']=i
#         result['q']=q
        
#         results.append(result)
#         #print(title,duration)
#         #print(video)
#         s+=1
#     #print(results_term)
    
#     #link_result = results_term[0]
#     return results

def download_yt(video,path_file:str='',path_dir:str='mp3',download=True):
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
#get_music_yt('clubbed of death')
#print(get_music_yt('telephone'))
