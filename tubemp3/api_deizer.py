import requests as req
import urllib.parse

API_DEIZER = 'https://api.deezer.com/search?q='

def get_info_music(query):
    query_url = urllib.parse.quote(query)
    try:
        res = req.get(API_DEIZER+query_url).json()['data'][0]
        info_music = { 
            "title":res["title"],
            "artist":res["artist"]["name"],
            "album":res["album"]["title"],
            "art_album":res["album"]["cover_big"]
            }
        return info_music
    except Exception as e:
#        print("error =>",req.get(API_DEIZER+query_url).json())
        return 0




