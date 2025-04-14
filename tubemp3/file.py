from tubemp3.api import search_music, extract_video_info
from tqdm import tqdm
import requests 
import subprocess
from tubemp3.metadata import save_metadata
import os

dir_cache = '/tmp'
if not os.path.exists(dir_cache):
    dir_cache = os.path.expanduser('~') + '/.cache/tubemp3'
    if not os.path.exists(dir_cache):
        os.makedirs(dir_cache)


def download_file(url: str, file_name: str):
    """Downloads a file from the specified URL and saves it with the given name.
    Args:
        url (str): URL of the file to download.
        file_name (str): Full path where the file will be saved.
    """
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get('content-length', 0))

    with open(file_name, 'wb') as file:
        with tqdm(total=total_size, unit='B', unit_scale=True, desc=file_name) as progress_bar:
            for data in response.iter_content(1024):
                file.write(data)
                progress_bar.update(len(data))


def download_thumbnail(music):
    """Downloads the album thumbnail associated with the music.
    Args:
        music (dict): Dictionary containing the music metadata.
    Returns:
        str: Path to the downloaded thumbnail file or None in case of an error.
    """
    query = music['query']
    url_thumbnail = music['art_album']
    ext = url_thumbnail.split('.')[-1]
    file_thumbnail = f"{dir_cache}/{query}.{ext}"
    try:
        download_file(url_thumbnail, file_thumbnail)
        return file_thumbnail
    except:
        print("Error saving thumbnail.")
        return None 



def convert_webm_to_mp3(input_file: str, output_file: str):
    """Converts an audio file from WebM format to MP3.
    Args:
        input_file (str): Path to the input WebM file.
        output_file (str): Path to the output MP3 file.
    """
    command = ['ffmpeg', "-hide_banner", '-i', input_file, '-vn', '-ab', '256k', '-ar', '44100', '-y', output_file]
    subprocess.run(command, check=True)



def download_webm(music: dict):
    """Downloads an audio file in WebM format.
    Args:
        music (dict): Dictionary containing the music metadata.
    Returns:
        str: Path to the downloaded WebM file.
    """
    url = music['url']
    title = music['query']
    ext = music['format']
    file_webm = f"{dir_cache}/{title}_.{ext}"
    print(f"Downloading `{file_webm}`")
    if os.path.isfile(file_webm):
        print(f"`{file_webm}` already exists in `{dir_cache}`")
    else:
        download_file(url, file_webm)
    return file_webm



def download(music: dict, path: str = None):
    """Downloads a song, converts it to MP3, and adds metadata.
    Args:
        music (dict): Dictionary containing the music metadata.
        path (str, optional): Path where the MP3 file will be saved. If None, uses the song name.
    Returns:
        str: Path to the generated MP3 file.
    """
    is_search = music.get('is_search',None)
    music = extract_video_info([music['id']]) if is_search else music
    file_webm = download_webm(music)
    file_thumb = download_thumbnail(music)
    file_mp3 = music['title'] + '.mp3' if not path else path
    print(f"Converting {file_webm} to {file_mp3}...")
    convert_webm_to_mp3(file_webm, file_mp3)
    save_metadata(file_path=file_mp3,
                  title=music.get('track', 'title'),
                  artist=music['artist'],
                  album=music["album"],
                  year=music['year'],
                  album_art_path=file_thumb)
    return file_mp3
