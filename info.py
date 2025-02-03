from tubemp3.api import search_music

query = "like a player wolverine deadpool chor"
music = search_music(query)[0]

for key,value in music.items():
    print(f"'{key}': '{value}'")
