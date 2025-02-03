import yt_dlp as youtube_dl
from tubemp3.api_deizer import get_info_music





def get_video_info(video_url):
    ydl_opts = {
        'quiet': True,  # Minimiza os logs
        'extract_flat': False,  # Extrai informações completas do vídeo
        'dump_single_json': True,  # Retorna resultados como JSON
        'noplaylist': True,  # Não inclui playlists nos resultados
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        try:
            # Extrai as informações do vídeo
            result = ydl.extract_info(video_url, download=False)
            return result
        except Exception as e:
            print(f"Erro ao extrair informações do vídeo: {e}")
            return None




def search_youtube(query, max_results=10):
    ydl_opts = {
        'quiet': True,  # Minimiza os logs
        'extract_flat': True,  # Extrai apenas metadados, sem baixar o vídeoi
#        'quiet': True,  # Minimiza os logs
        'format': 'bestaudio/best',  # Define o melhor formato de áudio
        'no_warnings': True,  # Evita exibir avisos desnecessários
        'ignoreerrors': True,  # Ignora erros em vídeos específicos
        'skip_download': True,
        'dump_single_json': True,  # Retorna resultados como JSON
#        'noplaylist': True,  # Não inclui playlists nos resultados
        'default_search': "ytmusic"  # Define que a busca deve ser feita no YouTube
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        try:
            # Realiza a pesquisa e retorna os resultados
            result = ydl.extract_info(f"ytsearch{max_results}:{query}", download=False)        
#            for i in range(len(result)):
#                result[i]['query'] = query
            print('Size yt result:',len(result))
#            for m in result['entries']:
#                print("\n")
#                for key, value in m.items(): 
#                    print(key,':',value)
            return result
        except Exception as e:
            print(f"Erro ao realizar pesquisa no YouTube: {e}")
            return None



def extract_video_info(video_ids,query=None):
    ydl_opts = {
        'quiet': True,  # Minimiza os logs
        'format': 'bestaudio/best',  # Define o melhor formato de áudio
        'no_warnings': True,  # Evita exibir avisos desnecessários
        'ignoreerrors': True,  # Ignora erros em vídeos específicos
        'skip_download': True  # Não baixa os vídeos, apenas extrai informações
    }
    result_videos = []
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
#        print(f'size result yt: {len(video_ids)}')
        for video_id in video_ids:
            try:
                video_info = {}
                video_yt = ydl.extract_info(video_id, download=False)
                #print(video_yt)
                video_info['query'] = query if query else video_yt['title']
                video_info['url'] = video_yt['url']
                video_info['title'] = video_yt['title']
                
                # api deizer

                info_music = get_info_music(video_yt["title"])
                if(info_music):
                    video_info["track"] = info_music["title"]
                    video_info["artist"] = info_music["artist"]
                    video_info["album"] = info_music["album"]
                    video_info["art_album"] = info_music["art_album"]
                else:
                    # print("api deizer not work")
                    video_info["artist"] = video_yt["channel"]
                    video_info["album"] = "Unknown"
                    video_info["art_album"] = video_yt["thumbnail"]
                    video_info["track"] = video_yt["title"]

                #api yt
                video_info['filesize'] = video_yt['filesize']
                video_info['duration'] = video_yt['duration']
                video_info['channel'] = video_yt['channel']
                video_info['thumbnail'] = video_yt['thumbnail']
                video_info['format'] = video_yt['audio_ext']
                video_info['year'] = video_yt['upload_date'][:4]
                result_videos.append(video_info)
            except Exception as e:
                print("erro ao capturar informações do video")
#    return result_videos if len(result_videos) > 2 else result_videos[0]
    size_search = len(result_videos)
    print(f'Size result search: {size_search}')
    if size_search > 1:
#        print('Is a list.',f"Size: {size_search} music's info")
        return result_videos
    else:
        print('Is a single music.')
        return result_videos[0]




def search_music(query,number_search:int=10,base_info=True):
#    print(f"getting info from music '{query}'...")
    result = search_youtube(query+" music hq",max_results=number_search)
    
    print(f"Extracting info...")
    if result and 'entries' in result:
        video_ids = [entry['id'] for entry in result['entries']]
        
        return extract_video_info(video_ids,query)
    else:
        print("Nenhum resultado encontrado.")
        return None



def get_info_link(link):
    #https://music.youtube.com/watch?v=yspAcpXEzSM&si=wVDm_1YrdKTCj3DL
    v = link.split('v=')[1].split('&')[0]
    res = extract_video_info([v])
    print("info music link:")
    for key,value in res.items():
        print(f"'{key}': '{value}'")
    return res
