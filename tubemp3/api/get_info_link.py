from tubemp3.api.extract_video_info import extract_video_info
from kitano import puts
from tubemp3.api.models import Music


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
    if type(result) == Music:
        puts("Single result found.")
        return result
    for key, value in result.items():
        print(f"'{key}': '{value}'")
    return result
