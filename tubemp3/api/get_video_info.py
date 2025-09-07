import yt_dlp as youtube_dl
from tubemp3.api_deizer import get_info_music
from tubemp3.api.models import Music





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
