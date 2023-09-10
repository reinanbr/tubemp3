'''
api code
date init: dez 31 21:27 2022
'''
import requests as rq
from youtube_dl import YoutubeDL
import re


ydl_opts_mp3 = {
       #'outtmpl': f'{path_dir}/{path_music}.%(ext)s',
           'format': 'bestaudio/best',
            'noplaylist':'True',
      #     'postprocessors': [{
      #         'key': 'FFmpegExtractAudio',
      #         'preferredcodec': 'mp3',
      #         'preferredquality': f'{pref_quality}',
      # }],
   }
ydl = YoutubeDL()




def extract_info(res_ytdl):
    vd_data=res_ytdl
    r = res_ytdl
    # print(title)
    # if any link will do 
    formats_ = [format for format in r['formats']]
    #print(formats_)
    formats = {}
    for format in formats_:
        if format.get('ext')=='mp4':
            formats[f'{format["format_note"]}'] = {'url':format['url'],
                                                    'fps':format['fps']}
        else:
            pass
    
    #self.types = [{format['ext'].split(' ')[0]:{'url':format['url']}} for format in formats]
    types = {}
    for format in formats_:
        types[format['ext'].split(' ')[0]] = {'url':format['url']}
        
    types = types
    formats = formats
    url_m4a = types['m4a']['url']
    track = vd_data.get('track','Unknown')
    channel = vd_data.get('channel',None)
    artist = vd_data.get('artist',channel)
    year = vd_data.get('upload_date',None)[:4]
    album = vd_data.get('album','Unknown')
    duration = vd_data.get('duration')
    id_video = vd_data.get('id')
    title = vd_data.get('title')
    thumbnail = vd_data.get('thumbnail')
    # title = re.sub('[^A-Za-z0-9]+', '', title)
    
    return {'title':title,'track':track,'duration':duration,'artist':artist,'channel':channel,'year':year,
            'album':album,'id_video':id_video,'url_m4a':url_m4a,'thumbnail':thumbnail,'ytdl':vd_data}
    

#info music youtube from a url
def get_info_url(url):
    res = ydl.extract_info(url, download=False)
    return extract_info(res)


def get_info_search(query:str,number_results:int=5)->list:
    list_videos = []
    videos = ydl.extract_info(f"ytsearch{number_results}:{query}", download=False)['entries']
    for video in videos:
        list_videos.append(extract_info(video))
    return list_videos