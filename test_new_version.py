
from tubemp3.api import search_music


video_list = search_music("the landing")
i = 0
for video_info in video_list:
    print(f"n[{i}]")
    for key,value in video_info.items():
        print(f"{key}: {value}")
    i+=1



