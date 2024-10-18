import yt_dlp as youtube_dl
from tubemp3.api_deizer import get_info_music


def search_youtube(query, max_results=5):
    ydl_opts = {
        'quiet': True,  # Minimiza os logs
        'extract_flat': True,  # Extrai apenas metadados, sem baixar o vídeo
        'dump_single_json': True,  # Retorna resultados como JSON
        'noplaylist': True,  # Não inclui playlists nos resultados
        'default_search': "ytmusic"  # Define que a busca deve ser feita no YouTube
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        try:
            # Realiza a pesquisa e retorna os resultados
            result = ydl.extract_info(f"ytsearch{max_results}:{query}", download=False)        
#            for i in range(len(result)):
#                result[i]['query'] = query
            print('len videos',len(result))
            return result
        except Exception as e:
            print(f"Erro ao realizar pesquisa no YouTube: {e}")
            return None



def extract_video_info(video_ids,query):
    ydl_opts = {
        'quiet': True,  # Minimiza os logs
        'format': 'bestaudio/best',  # Define o melhor formato de áudio
        'no_warnings': True,  # Evita exibir avisos desnecessários
        'ignoreerrors': True,  # Ignora erros em vídeos específicos
        'skip_download': True  # Não baixa os vídeos, apenas extrai informações
    }
    result_videos = []
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        for video_id in video_ids:
            try:
                video_info = {}
                video_yt = ydl.extract_info(video_id, download=False)
                #print(video_yt)
                video_info['query'] = query
                video_info['url'] = video_yt['url']
                video_info['title'] = video_yt['title']
                
                # api deizer
                info_music = get_info_music(video_yt["title"])
                video_info["track"] = info_music["title"]
                video_info["artist"] = info_music["artist"]
                video_info["album"] = info_music["album"]
                video_info["art_album"] = info_music["art_album"]
            
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
    return result_videos






def search_music(query,number_search:int=1,base_info=True):
    print(f"getting info from music '{query}'...")
    result = search_youtube(query+" music")

    if result and 'entries' in result:
        video_ids = [entry['id'] for entry in result['entries'][:number_search]]
        
        return extract_video_info(video_ids,query)
    else:
        print("Nenhum resultado encontrado.")
        return None





