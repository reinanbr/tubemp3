from tubemp3.api import search_music
from tqdm import tqdm
import requests 
import subprocess
from tubemp3.metadata import save_metadata
import os


dir_cache = '/tmp'

def download_file(url, file_name):
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get('content-length', 0))

    with open(file_name, 'wb') as file:
        with tqdm(total=total_size, unit='B', unit_scale=True, desc=file_name) as progress_bar:
            for data in response.iter_content(1024):
                file.write(data)
                progress_bar.update(len(data))



def download_thumbnail(music):
    query = music['query']
    url_thumbnail = music['art_album']
    ext = url_thumbnail.split('.')[-1]
    file_thumbnail = f"{dir_cache}/{query}.{ext}"
    try:
        download_file(url_thumbnail,file_thumbnail)
        return file_thumbnail
    except:
        print("error save thumbnail.")
        return None 



def convert_webm_to_mp3(input_file, output_file):
    command = ['ffmpeg',"-hide_banner", '-i', input_file, '-vn', '-ab', '256k', '-ar', '44100', '-y', output_file]
    subprocess.run(command, check=True)





def download_webm(music):
    url = music['url']
    title = music['query']
    ext = music['format']
    file_webm = f"{dir_cache}/{title}_.{ext}"
    print(f"downloading `{file_webm}`")
    if os.path.isfile(file_webm):
        print(f"`{file_webm}` exists in `{dir_cache}`")
    else:
        download_file(url,file_webm)
    return file_webm




def download(music,path=None):
    file_webm = download_webm(music)
    file_thumb = download_thumbnail(music)
    file_mp3 = music['query'] +'.mp3' if not path else path
    print(f"converting {file_webm} to {file_mp3}...")
    convert_webm_to_mp3(file_webm,file_mp3)
    save_metadata(file_path=file_mp3,
                  title=music.get('track','title'),
                  artist=music['artist'],
                  album=music["album"],
                  year=music['year'],
                  album_art_path=file_thumb)
    return file_mp3
