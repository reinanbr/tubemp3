import yt_dlp as youtube_dl

def search_youtube(query, max_results=5):
    ydl_opts = {
        'quiet': True,  # Minimiza os logs
        'extract_flat': True,  # Extrai apenas metadados, sem baixar o vídeo
        'dump_single_json': True,  # Retorna resultados como JSON
        'noplaylist': True,  # Não inclui playlists nos resultados
        'default_search': 'ytsearch'  # Define que a busca deve ser feita no YouTube
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        try:
            # Realiza a pesquisa e retorna os resultados
            result = ydl.extract_info(f"ytsearch{max_results}:{query}", download=False)
            return result
        except Exception as e:
            print(f"Erro ao realizar pesquisa no YouTube: {e}")
            return None



def extract_video_info(video_ids):
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
                video_info = ydl.extract_info(video_id, download=False)
                result_videos.append(video_info)
            except Exception as e:
                print("erro ao capturar informações do video")
    return result_videos



def search_music(query,number_search:int=1):
    print(f"getting info from music '{query}'...")
    result = search_youtube(query+" music")

    if result and 'entries' in result:
        video_ids = [entry['id'] for entry in result['entries'][:number_search]]
        
        return extract_video_info(video_ids)
    else:
        print("Nenhum resultado encontrado.")
        return None





