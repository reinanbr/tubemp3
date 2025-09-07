from dataclasses import dataclass
from typing import List, Optional
from json import dumps, loads

@dataclass
class Music:
    id: str
    title: str
    url: str
    duration: Optional[int] = None
    uploader: Optional[str] = None
    is_search: Optional[bool] = False
    artist: Optional[str] = None
    album: Optional[str] = None
    track: Optional[str] = None
    art_album: Optional[str] = None
    filesize: Optional[int] = None
    channel: Optional[str] = None
    year: Optional[str] = None
    format: Optional[str] = None
    thumbnail: Optional[str] = None
    query: Optional[str] = None
    # Add more fields based on the metadata you want to store

    def __str__(self):
        return dumps(self.__dict__, indent=4)

    def __get_state__(self):
        return self.__dict__

    def __get__(self, key):
        return self.__dict__.get(key, None)





def music_from_dict(data: dict) -> Music:
    return Music(
        id=data.get('id', ''),
        title=data.get('title', ''),
        url=data.get('url', ''),
        duration=data.get('duration'),
        uploader=data.get('uploader'),
        is_search=data.get('is_search', False),
        artist=data.get('artist'),
        album=data.get('album'),
        track=data.get('track'),
        art_album=data.get('art_album'),
        filesize=data.get('filesize'),
        channel=data.get('channel'),
        year=data.get('year'),
        format=data.get('format'),
        thumbnail=data.get('thumbnail'),
        query=data.get('query')
    )
