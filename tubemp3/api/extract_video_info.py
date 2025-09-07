import yt_dlp as youtube_dl
from tubemp3.api_deizer import get_info_music
from tubemp3.api.models import Music
from kitano import puts
import threading

def extract_video_info(video_ids: list, query: str = None):
    """Extracts detailed information about a list of YouTube videos.
    
    Args:
        video_ids (list): List of video IDs.
        query (str, optional): Search query for reference.
    
    Returns:
        dict or list: Video metadata as a single dictionary if one result, or a list if multiple.
    """
    ydl_opts = {
        'quiet': True,
        'format': 'bestaudio/best',
        'no_warnings': True,
        'ignoreerrors': True,
        'skip_download': True
    }
    
    result_musics = []

    # Função que será chamada dentro da thread para cada vídeo
    def process_video(video_id):
        try:
            music_info = {}
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                music_yt = ydl.extract_info(video_id, download=False)
            puts(f"Processing video_id: {video_id}")
            music_info['query'] = query if query else music_yt['title']
            music_info['url'] = music_yt['url']
            music_info['title'] = music_yt['title']
            
            puts(f"Extracted title: {music_info['title']}")
            puts(f"Extracted url: {music_info['url']}")
            puts(f"Extracted video info: {music_yt}")
            
            # Obtendo informações adicionais da música
            info_music = get_info_music(music_yt["title"])
            if info_music:
                puts(f"Extracted music info: {info_music}")
                music_info.update({
                    "track": info_music["title"],
                    "artist": info_music["artist"],
                    "album": info_music["album"],
                    "art_album": info_music["art_album"]
                })
                puts(f"Updated music info with Deezer data: {music_info}")
            else:
                music_info.update({
                    "artist": music_yt["channel"],
                    "album": "Unknown",
                    "art_album": music_yt["thumbnail"],
                    "track": music_yt["title"]
                })
                puts(f"Updated music info with YouTube data: {music_info}")

            # Informações adicionais do vídeo
            music_info.update({
                'filesize': music_yt['filesize'],
                'duration': music_yt['duration'],
                'channel': music_yt['channel'],
                'thumbnail': music_yt['thumbnail'],
                'format': music_yt['audio_ext'],
                'year': music_yt['upload_date'][:4]
            })
            puts(f"Final music info before creating Music object: {music_info}")

            music = Music(
                id=video_id,
                title=music_info['title'],
                url=music_info['url'],
                duration=music_info.get('duration'),
                uploader=music_info.get('artist'),
                is_search=bool(query),
                artist=music_info.get('artist'),
                album=music_info.get('album'),
                track=music_info.get('track'),
                art_album=music_info.get('art_album'),
                filesize=music_info.get('filesize'),
                channel=music_info.get('channel'),
                year=music_info.get('year'),
                format=music_info.get('format'),
                thumbnail=music_info.get('thumbnail'),
                query=music_info.get('query')
            )
            result_musics.append(music)
            puts(f"Created Music object: {music}")
            

        except Exception:
            print(f"Error retrieving video information for video_id: {video_id}")

    # Criando as threads para cada vídeo
    threads = []
    for video_id in video_ids:
        thread = threading.Thread(target=process_video, args=(video_id,))
        threads.append(thread)
        thread.start()

    # Aguardando todas as threads finalizarem
    for thread in threads:
        thread.join()

    if not result_musics:
        raise ValueError("No valid video information could be extracted.")
        return None
    
    # Retorna o resultado
    if len(result_musics) == 1:
        puts("One music found:")
        puts(result_musics[0])
        return result_musics[0]
    
    puts(f"{len(result_musics)} musics found:")
    return result_musics
