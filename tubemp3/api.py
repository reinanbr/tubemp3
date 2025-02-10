import yt_dlp as youtube_dl
from tubemp3.api_deizer import get_info_music

def get_video_info(video_url):
    """Retrieves detailed information about a YouTube video.
    
    Args:
        video_url (str): URL of the YouTube video.
    
    Returns:
        dict: Video metadata or None if an error occurs.
    """
    ydl_opts = {
        'quiet': True,
        'extract_flat': False,
        'dump_single_json': True,
        'noplaylist': True,
    }
    
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        try:
            return ydl.extract_info(video_url, download=False)
        except Exception as e:
            print(f"Error extracting video information: {e}")
            return None

def search_youtube(query, max_results=10):
    """Searches for music on YouTube.
    
    Args:
        query (str): Search query.
        max_results (int, optional): Number of search results. Defaults to 10.
    
    Returns:
        dict: Search results or None if an error occurs.
    """
    ydl_opts = {
        'quiet': True,
        'extract_flat': True,
        'format': 'bestaudio/best',
        'no_warnings': True,
        'ignoreerrors': True,
        'skip_download': True,
        'dump_single_json': True,
        'default_search': "ytmusic"
    }
    
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        try:
            result = ydl.extract_info(f"ytsearch{max_results}:{query}", download=False)
            return result
        except Exception as e:
            print(f"Error searching YouTube: {e}")
            return None

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
    result_videos = []
    
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        for video_id in video_ids:
            try:
                video_info = {}
                video_yt = ydl.extract_info(video_id, download=False)
                video_info['query'] = query if query else video_yt['title']
                video_info['url'] = video_yt['url']
                video_info['title'] = video_yt['title']
                
                info_music = get_info_music(video_yt["title"])
                if info_music:
                    video_info.update({
                        "track": info_music["title"],
                        "artist": info_music["artist"],
                        "album": info_music["album"],
                        "art_album": info_music["art_album"]
                    })
                else:
                    video_info.update({
                        "artist": video_yt["channel"],
                        "album": "Unknown",
                        "art_album": video_yt["thumbnail"],
                        "track": video_yt["title"]
                    })
                
                video_info.update({
                    'filesize': video_yt['filesize'],
                    'duration': video_yt['duration'],
                    'channel': video_yt['channel'],
                    'thumbnail': video_yt['thumbnail'],
                    'format': video_yt['audio_ext'],
                    'year': video_yt['upload_date'][:4]
                })
                result_videos.append(video_info)
            except Exception:
                print("Error retrieving video information")
    
    return result_videos if len(result_videos) > 1 else result_videos[0]

def search_music(query, number_search: int = 10):
    """Searches for music using YouTube and extracts relevant metadata.
    
    Args:
        query (str): Music search query.
        number_search (int, optional): Number of search results. Defaults to 10.
    
    Returns:
        list: List of video metadata dictionaries or None if no results.
    """
    result = search_youtube(query + " music hq", max_results=number_search)
    
    if result and 'entries' in result:
        #return [entry for entry in result['entries']]
        musics = []
        for entry in result['entries']:
            music = entry
            music['is_search'] = True
            musics.append(music)
        return musics
    else:
        print("No results found.")
        return None





def get_info_link(link):
    """Extracts music information from a YouTube video link.
    
    Args:
        link (str): YouTube video link.
    
    Returns:
        dict: Extracted music metadata.
    """
    video_id = link.split('v=')[1].split('&')[0]
    result = extract_video_info([video_id])
    print("Music info:")
    for key, value in result.items():
        print(f"'{key}': '{value}'")
    return result
