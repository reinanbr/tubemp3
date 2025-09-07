import yt_dlp as youtube_dl
from tubemp3.api_deizer import get_info_music
from tubemp3.api.models import Music
from tubemp3.api.search_youtube import search_youtube


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
            music = Music(
                id=entry.get('id'),
                title=entry.get('title'),
                url=entry.get('url'),
                artist=entry.get('uploader'),
                album="Unknown",
                track=entry.get('title'),
                art_album=entry.get('thumbnail'),
                is_search=True
            )
            music.is_search = True
            musics.append(music)
        return musics
    else:
        print("No results found.")
        return None
