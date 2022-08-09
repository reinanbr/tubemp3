
'''
get infovideo from only url 
'''

import requests as rq
from youtube_dl import YoutubeDL
import re
import time

ydl = YoutubeDL()

class get_from_link(object):
    def __init__(self,url:str) -> None:
        print('oi')
        
        token_video = url.split('/')[-1]
        
        url = f'https://www.youtube.com/watch?v={token_video}'
        r = ydl.extract_info(url, download=False)
        
        
        
        title = r.get('title')
        title = re.sub('[^A-Za-z0-9]+', '', title)
        print(title)
        self.title = title
        # if any link will do 
        formats_ = [format for format in r['formats']]
        print(formats_)
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
            
        self.types = types
        self.formats = formats
    
    def __download(self,url,format):
        #url = self.types['m4a']['url']
        res = rq.get(url,stream=True)
        res.raise_for_status()
        
        size = int(res.headers.get('content-length'))
        size_mb = size/(1024**2)
        filename=f'{self.title}.{format}'
        bdiv = 1024
        with open(filename,'bw') as file:
            b = 0
            init_time = time.time()
            for byte in res.iter_content(chunk_size=bdiv):
                b=b+1
                file.write(byte)
                time_end = time.time() - init_time
                b_mb = b/bdiv
                down_fast = ((b)/time_end)
                percent = (((b/bdiv)/size_mb)*100)
                eta = ((size/(bdiv))-b)/down_fast
                print(f'[{filename[:7]+"..."}{filename[-7:]}  {percent:.2f}%  {(b_mb):.2f}MB/{size_mb:.2f}MB  {down_fast:.2f}Kb/s  eta:{eta:.0f}s  {time_end:.0f}s ',end='\r',flush=False)
        
        return filename
    
    def download_video(self,width=364):
        # try:
        #     url = self.formats[f'{width}']['url']
        # except:
        #     print(f'ERROR: width ({width}) not founded!')
        #     print(f'you can get the widht"s [{self.formats.keys()}] from it url')
        #     exit()
        print('please, choice a format')
        i = 1
        formats = []
        for format in self.formats.keys():
            print(f'{i} - {format} - {self.formats[format]["fps"]}fps')
            formats.append(self.formats[format]['url'])
            i+=1
            
        choice = input('enter the number of your choice: ')
        choice = int(choice)-1
        url = formats[choice]
        self.__download(url,'mp4')
        pass